from __future__ import annotations

from dataclasses import dataclass

from core.ids import event_id
from data.schemas import Observation
from multi_agent.base import AgentContext
from multi_agent.blackboard import Blackboard
from multi_agent.bus import MessageBus
from multi_agent.coordinator import CoordinatorAgent
from multi_agent.messages import Message, MessageType, Priority, TaskSpec
from multi_agent.registry import AgentRegistry
from multi_agent.specialists import (
    AffectAgent,
    MemoryAgent,
    PlannerAgent,
    SafetyGovernor,
    ToolAgent,
    VerifierAgent,
    WorldModelAgent,
)
from multi_agent.trace import TraceRecorder


@dataclass(frozen=True)
class MultiAgentRunResult:
    trace_id: str
    ok: bool
    shared_state: dict
    messages: int
    agent_results: dict[str, list]


class MultiAgentRuntime:
    def __init__(self) -> None:
        self.bus = MessageBus()
        self.context = AgentContext(self.bus, Blackboard())
        self.trace = TraceRecorder()
        self.registry = AgentRegistry()
        self.specialist_order = [
            "memory_agent",
            "world_model_agent",
            "planner_agent",
            "safety_governor",
            "verifier_agent",
            "tool_agent",
            "affect_agent",
        ]
        self.coordinator = CoordinatorAgent(self.specialist_order)
        for agent in [
            self.coordinator,
            MemoryAgent(),
            WorldModelAgent(),
            PlannerAgent(),
            SafetyGovernor(),
            VerifierAgent(),
            ToolAgent(),
            AffectAgent(),
        ]:
            self.registry.add(agent)

    def observe_text(self, text: str) -> Observation:
        from time import time

        return Observation(id=event_id("obs"), timestamp=time(), source="user_text", raw_ref=text)

    def run(self, goal: str, max_rounds: int = 3) -> MultiAgentRunResult:
        task = TaskSpec(goal=goal)
        trace_id = self.coordinator.start(self.context, task, self.observe_text(goal))
        self.trace.record(trace_id, "runtime_start", {"goal": goal})
        for _ in range(max_rounds):
            for name in self.specialist_order:
                results = self.registry.get(name).tick(self.context)
                for result in results:
                    self.trace.record(trace_id, "agent_result", result.__dict__)
            self.bus.publish(
                Message(
                    sender="runtime",
                    recipient="coordinator",
                    type=MessageType.RESULT,
                    payload={"agent": "runtime", "ok": True, "summary": "round complete"},
                    trace_id=trace_id,
                    priority=Priority.NORMAL,
                )
            )
            for result in self.coordinator.tick(self.context):
                self.trace.record(trace_id, "coordinator_result", result.__dict__)
            if self.context.shared_state.get("execution") is not None:
                break
        agent_results = {name: agent.results for name, agent in self.registry.agents.items()}
        execution = self.context.shared_state.get("execution")
        ok = bool(execution.success) if execution is not None else bool(self.context.shared_state.get("coordinator_summary", {}).get("ok", False))
        self.trace.record(trace_id, "runtime_end", {"ok": ok, "messages": len(self.bus.history)})
        return MultiAgentRunResult(
            trace_id=trace_id,
            ok=ok,
            shared_state=dict(self.context.shared_state),
            messages=len(self.bus.history),
            agent_results=agent_results,
        )
