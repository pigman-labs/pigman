from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field

from multi_agent.budgets import BudgetManager
from multi_agent.bus import MessageBus
from multi_agent.messages import AgentResult, Message, MessageType


@dataclass
class AgentContext:
    bus: MessageBus
    shared_state: dict = field(default_factory=dict)
    budgets: BudgetManager = field(default_factory=BudgetManager)


class BaseAgent(ABC):
    name: str

    def __init__(self, name: str) -> None:
        self.name = name
        self.handled = 0
        self.results: list[AgentResult] = []

    def tick(self, context: AgentContext, limit: int | None = None) -> list[AgentResult]:
        outputs = []
        for message in context.bus.drain(self.name, limit):
            if not context.budgets.allow(self.name):
                result = AgentResult(
                    self.name,
                    False,
                    "agent budget exhausted",
                    {"budget": context.budgets.snapshot().get(self.name, {})},
                    confidence=0.0,
                    risk=1.0,
                )
                context.bus.publish(message.reply(self.name, result.__dict__, MessageType.ERROR))
                self.handled += 1
                self.results.append(result)
                outputs.append(result)
                continue
            try:
                result = self.handle(message, context)
            except Exception as exc:  # pragma: no cover - defensive boundary
                result = AgentResult(self.name, False, f"{type(exc).__name__}: {exc}", {"message_id": message.id}, confidence=0.0, risk=1.0)
                context.bus.publish(message.reply(self.name, result.__dict__, MessageType.ERROR))
            else:
                context.bus.publish(message.reply(self.name, result.__dict__))
            context.budgets.consume(self.name, risk=result.risk)
            self.handled += 1
            self.results.append(result)
            outputs.append(result)
        return outputs

    @abstractmethod
    def handle(self, message: Message, context: AgentContext) -> AgentResult:
        raise NotImplementedError
