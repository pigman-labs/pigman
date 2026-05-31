from __future__ import annotations

from core.ids import event_id
from data.schemas import Observation
from multi_agent.base import AgentContext, BaseAgent
from multi_agent.messages import AgentResult, Message, MessageType, Priority, TaskSpec
from multi_agent.protocols import DebateProtocol, MergeProtocol


class CoordinatorAgent(BaseAgent):
    def __init__(self, specialists: list[str]) -> None:
        super().__init__("coordinator")
        self.specialists = specialists
        self.debate = DebateProtocol()
        self.merge = MergeProtocol()

    def start(self, context: AgentContext, task: TaskSpec, observation: Observation | None = None) -> str:
        trace_id = event_id("trace")
        context.shared_state["task"] = task
        if observation is not None:
            context.shared_state["observation"] = observation
        for specialist in self.specialists:
            context.bus.publish(
                Message(
                    sender=self.name,
                    recipient=specialist,
                    type=MessageType.TASK,
                    payload={"goal": task.goal, "constraints": task.constraints, "context": task.context},
                    trace_id=trace_id,
                    priority=Priority.HIGH,
                    requires_reply=True,
                )
            )
        return trace_id

    def handle(self, message: Message, context: AgentContext) -> AgentResult:
        trace = context.bus.trace(message.trace_id)
        result_payloads = [item.payload for item in trace if item.recipient == self.name and item.type in {MessageType.RESULT, MessageType.ERROR}]
        results = []
        for payload in result_payloads:
            if {"agent", "ok", "summary"}.issubset(payload):
                results.append(
                    AgentResult(
                        agent=payload["agent"],
                        ok=payload["ok"],
                        summary=payload["summary"],
                        payload=payload.get("payload", {}),
                        confidence=payload.get("confidence", 0.5),
                        risk=payload.get("risk", 0.0),
                    )
                )
        merged = self.merge.merge(results)
        votes = self.debate.rank(results)
        context.shared_state["coordinator_summary"] = merged
        context.shared_state["votes"] = votes
        return AgentResult(
            self.name,
            merged["ok"],
            "merged specialist outputs",
            {"merged": merged, "votes": [vote.__dict__ for vote in votes]},
            confidence=merged["confidence"],
            risk=merged["risk"],
        )

