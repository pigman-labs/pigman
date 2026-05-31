from __future__ import annotations

from time import time

from affect.engine import AffectEngine
from affect.state import AffectInputs
from causal.graph import CausalGraph
from causal.learner import CausalLearner
from core.ids import event_id
from data.schemas import Observation
from decoders.action_decoder import ActionDecoder
from dynamics.latent_state import BeliefState, LatentState
from encoders.registry import EncoderRegistry
from memory.retrieval import MemorySystem
from planner.router import PlannerRouter
from policies.action_policy import ActionPolicy
from storage.trajectory_log import TrajectoryLog
from tools.executor import ToolExecutor
from verifiers.ensemble import VerifierEnsemble
from world_model.belief_update import BeliefUpdater
from world_model.world_model import WorldModel


class AgentRuntime:
    def __init__(self) -> None:
        self.encoders = EncoderRegistry()
        self.belief_updater = BeliefUpdater()
        self.world_model = WorldModel()
        self.memory = MemorySystem()
        self.planner = PlannerRouter()
        self.policy = ActionPolicy()
        self.decoder = ActionDecoder()
        self.verifiers = VerifierEnsemble()
        self.executor = ToolExecutor(self.memory)
        self.trajectory = TrajectoryLog()
        self.causal_graph = CausalGraph()
        self.causal_learner = CausalLearner()
        self.belief = BeliefState(current=LatentState())
        self.affect = AffectEngine()
        self.failures_by_goal: dict[str, int] = {}

    def observe_text(self, text: str) -> Observation:
        return Observation(
            id=event_id("obs"),
            timestamp=time(),
            source="user_text",
            raw_ref=text,
        )

    def step(self, goal: dict, observations: list[Observation] | None = None) -> dict:
        if observations is None:
            observations = [self.observe_text(str(goal.get("goal", goal)))]

        encoded = [self.encoders.encode(observation) for observation in observations]
        self.belief.current = self.belief_updater.update(self.belief.current, encoded)

        query = str(goal.get("goal", goal))
        memory_bundle = self.memory.retrieve(query)
        self.belief.current.global_state["memory"] = memory_bundle

        prediction = self.world_model.predict(
            self.belief.current,
            mask={"kind": "future_action_effect"},
            action={"goal": goal},
        )
        self.belief.current = prediction.next_state

        plan = self.planner.plan(self.belief, goal)
        action = self.policy.select_next(plan)
        call = self.decoder.decode(action)
        verification = self.verifiers.check(action, call)

        execution = None
        affect_result = None
        if verification.approved:
            execution = self.executor.execute(call, action.to_record())
            self.causal_learner.update_from_result(self.causal_graph, execution)
            self.memory.add_trace(execution.observation.id, execution.stdout or execution.observation.raw_ref, execution.metadata)
            followup_encoded = [self.encoders.encode(execution.observation)]
            self.belief.current = self.belief_updater.update(self.belief.current, followup_encoded)

        success = execution.success if execution is not None else False
        goal_key = str(goal.get("goal", goal))
        self.failures_by_goal[goal_key] = 0 if success else self.failures_by_goal.get(goal_key, 0) + 1
        prediction_error = float(prediction.uncertainty)
        if prediction.neural_latent and self.belief.current.vector:
            prediction_error = min(1.0, abs(len(prediction.neural_latent) - len(self.belief.current.vector)) / 64.0 + prediction.uncertainty * 0.5)
        affect_result = self.affect.update(
            AffectInputs(
                prediction_error=prediction_error,
                novelty=min(1.0, len(self.belief.current.events) / 20.0),
                verifier_success=success if execution is not None else verification.approved,
                risk=action.risk_score,
                coping_capacity=1.0 if verification.approved else 0.3,
                goal_progress=1.0 if success else 0.0,
                goal_blockage=0.0 if success else 0.6,
                repeated_failures=self.failures_by_goal[goal_key],
                immediate_reward=1.0 if success else 0.0,
                delayed_reward=max(0.0, 1.0 - action.risk_score),
                delay=1.0 + len(plan.actions),
                bond_signal=0.05 if success else 0.0,
            ),
            entity=call.name,
        )
        self.belief.current.global_state["affect"] = affect_result.after.as_dict()
        self.belief.current.global_state["intrinsic_reward"] = affect_result.intrinsic_reward
        self.belief.current.global_state["curriculum"] = affect_result.curriculum.__dict__

        event = {
            "goal": goal,
            "plan": plan,
            "selected_action": action,
            "tool_call": call,
            "verification": verification,
            "execution": execution,
            "affect_before": affect_result.before,
            "affect_after": affect_result.after,
            "intrinsic_reward": affect_result.intrinsic_reward,
            "memory_salience": affect_result.memory_salience,
            "curriculum": affect_result.curriculum,
            "belief": self.belief.current.global_state,
        }
        self.trajectory.append(event)

        return {
            "plan": plan,
            "action": action,
            "tool_call": call,
            "verification": verification,
            "execution": execution,
            "prediction": prediction,
            "belief": self.belief.current,
            "affect": affect_result,
        }
