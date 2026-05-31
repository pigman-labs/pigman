from __future__ import annotations

from affect.engine import AffectEngine
from affect.state import AffectInputs
from decoders.action_decoder import ActionDecoder
from dynamics.latent_state import BeliefState, LatentState
from encoders.registry import EncoderRegistry
from memory.retrieval import MemorySystem
from multi_agent.base import AgentContext, BaseAgent
from multi_agent.messages import AgentResult, Message
from multi_agent.repair import RepairPolicy
from planner.router import PlannerRouter
from policies.action_policy import ActionPolicy
from tools.executor import ToolExecutor
from verifiers.ensemble import VerifierEnsemble
from world_model.belief_update import BeliefUpdater
from world_model.world_model import WorldModel


class WorldModelAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__("world_model_agent")
        self.encoders = EncoderRegistry()
        self.belief_updater = BeliefUpdater()
        self.world_model = WorldModel()
        self.belief = BeliefState(LatentState())

    def handle(self, message: Message, context: AgentContext) -> AgentResult:
        goal = str(message.payload.get("goal", ""))
        observation = context.shared_state.get("observation")
        if observation is not None:
            encoded = [self.encoders.encode(observation)]
            self.belief.current = self.belief_updater.update(self.belief.current, encoded)
        prediction = self.world_model.predict(self.belief.current, {"kind": "multi_agent"}, {"goal": goal})
        self.belief.current = prediction.next_state
        context.shared_state["belief"] = self.belief.current
        context.shared_state["prediction"] = prediction
        return AgentResult(
            self.name,
            True,
            "predicted future state and updated shared belief",
            {"uncertainty": prediction.uncertainty, "has_neural_latent": prediction.neural_latent is not None},
            confidence=max(0.0, 1.0 - prediction.uncertainty),
            risk=prediction.uncertainty,
        )


class PlannerAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__("planner_agent")
        self.planner = PlannerRouter()
        self.policy = ActionPolicy()

    def handle(self, message: Message, context: AgentContext) -> AgentResult:
        goal = {"goal": str(message.payload.get("goal", ""))}
        belief = BeliefState(context.shared_state.get("belief", LatentState()))
        plan = self.planner.plan(belief, goal)
        action = self.policy.select_next(plan)
        context.shared_state["plan"] = plan
        context.shared_state["action"] = action
        return AgentResult(
            self.name,
            True,
            f"selected action {action.type}",
            {"action": action.__dict__, "plan_score": plan.score, "rationale": plan.rationale},
            confidence=plan.score,
            risk=action.risk_score,
        )


class VerifierAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__("verifier_agent")
        self.decoder = ActionDecoder()
        self.verifiers = VerifierEnsemble()
        self.repair = RepairPolicy()

    def handle(self, message: Message, context: AgentContext) -> AgentResult:
        action = context.shared_state.get("action")
        if action is None:
            return AgentResult(self.name, False, "no action to verify", {}, confidence=0.0, risk=1.0)
        call = self.decoder.decode(action)
        verification = self.verifiers.check(action, call)
        context.shared_state["tool_call"] = call
        context.shared_state["verification"] = verification
        if not verification.approved:
            context.shared_state["repair_proposal"] = self.repair.propose(action, verification)
        return AgentResult(
            self.name,
            verification.approved,
            "action approved" if verification.approved else "action rejected",
            {
                "issues": verification.issues,
                "tool_call": call.__dict__,
                "repair": getattr(context.shared_state.get("repair_proposal"), "__dict__", None),
            },
            confidence=1.0 if verification.approved else 0.2,
            risk=action.risk_score if verification.approved else 1.0,
        )


class ToolAgent(BaseAgent):
    def __init__(self, memory: MemorySystem | None = None) -> None:
        super().__init__("tool_agent")
        self.memory = memory or MemorySystem()
        self.executor = ToolExecutor(self.memory)

    def handle(self, message: Message, context: AgentContext) -> AgentResult:
        action = context.shared_state.get("action")
        call = context.shared_state.get("tool_call")
        verification = context.shared_state.get("verification")
        if action is None or call is None:
            return AgentResult(self.name, False, "missing action/tool call", {}, confidence=0.0, risk=1.0)
        if context.shared_state.get("safety_blocked"):
            return AgentResult(
                self.name,
                False,
                "safety governor blocked execution",
                {"risk": getattr(action, "risk_score", 1.0)},
                confidence=0.0,
                risk=1.0,
            )
        if verification is not None and not verification.approved:
            return AgentResult(self.name, False, "verification blocked execution", {"issues": verification.issues}, confidence=0.0, risk=1.0)
        execution = self.executor.execute(call, action.to_record())
        context.shared_state["execution"] = execution
        return AgentResult(
            self.name,
            execution.success,
            "executed tool successfully" if execution.success else "tool execution failed",
            {"stdout": execution.stdout[:500], "stderr": execution.stderr[:500], "source": execution.observation.source},
            confidence=1.0 if execution.success else 0.2,
            risk=action.risk_score,
        )


class MemoryAgent(BaseAgent):
    def __init__(self, memory: MemorySystem | None = None) -> None:
        super().__init__("memory_agent")
        self.memory = memory or MemorySystem()

    def handle(self, message: Message, context: AgentContext) -> AgentResult:
        goal = str(message.payload.get("goal", ""))
        execution = context.shared_state.get("execution")
        if execution is not None:
            self.memory.add_trace(execution.observation.id, execution.stdout or execution.observation.raw_ref, execution.metadata)
        bundle = self.memory.retrieve(goal)
        context.shared_state["memory_bundle"] = bundle
        return AgentResult(
            self.name,
            True,
            "retrieved and updated memory",
            {"facts": bundle.facts, "procedures": bundle.procedures, "vector_hits": len(bundle.vector_hits)},
            confidence=0.7,
            risk=0.0,
        )


class SafetyGovernor(BaseAgent):
    def __init__(self) -> None:
        super().__init__("safety_governor")

    def handle(self, message: Message, context: AgentContext) -> AgentResult:
        action = context.shared_state.get("action")
        risk = float(getattr(action, "risk_score", 0.0)) if action is not None else 0.0
        blocked = risk >= 0.9
        context.shared_state["safety_blocked"] = blocked
        return AgentResult(
            self.name,
            not blocked,
            "safety governor approved" if not blocked else "safety governor blocked high-risk action",
            {"risk": risk},
            confidence=1.0,
            risk=risk,
        )


class AffectAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__("affect_agent")
        self.engine = AffectEngine()

    def handle(self, message: Message, context: AgentContext) -> AgentResult:
        action = context.shared_state.get("action")
        execution = context.shared_state.get("execution")
        prediction = context.shared_state.get("prediction")
        risk = float(getattr(action, "risk_score", 0.0)) if action is not None else 0.0
        success = execution.success if execution is not None else True
        uncertainty = float(getattr(prediction, "uncertainty", 0.5)) if prediction is not None else 0.5
        result = self.engine.update(
            AffectInputs(
                prediction_error=uncertainty,
                novelty=0.5,
                verifier_success=success,
                risk=risk,
                goal_progress=1.0 if success else 0.0,
                goal_blockage=0.0 if success else 0.5,
                repeated_failures=0 if success else 1,
            ),
            entity=getattr(context.shared_state.get("tool_call"), "name", "unknown"),
        )
        context.shared_state["affect"] = result
        return AgentResult(
            self.name,
            True,
            "updated affect and intrinsic reward",
            {
                "affect": result.after.as_dict(),
                "intrinsic_reward": result.intrinsic_reward,
                "curriculum": result.curriculum.__dict__,
            },
            confidence=0.8,
            risk=max(0.0, result.after.fear),
        )
