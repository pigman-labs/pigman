from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from time import time

from core.ids import event_id


class MessageType(str, Enum):
    GOAL = "goal"
    TASK = "task"
    PROPOSAL = "proposal"
    CRITIQUE = "critique"
    VERIFICATION = "verification"
    MEMORY = "memory"
    SAFETY = "safety"
    RESULT = "result"
    ERROR = "error"


class Priority(int, Enum):
    LOW = 1
    NORMAL = 5
    HIGH = 8
    CRITICAL = 10


@dataclass(frozen=True)
class Message:
    sender: str
    recipient: str
    type: MessageType
    payload: dict
    trace_id: str
    id: str = field(default_factory=lambda: event_id("msg"))
    priority: Priority = Priority.NORMAL
    requires_reply: bool = False
    created_at: float = field(default_factory=time)

    def reply(self, sender: str, payload: dict, type: MessageType = MessageType.RESULT) -> "Message":
        return Message(
            sender=sender,
            recipient=self.sender,
            type=type,
            payload=payload,
            trace_id=self.trace_id,
            priority=self.priority,
        )


@dataclass(frozen=True)
class TaskSpec:
    goal: str
    constraints: tuple[str, ...] = ()
    context: dict = field(default_factory=dict)
    budget_steps: int = 3
    risk_tolerance: float = 0.3


@dataclass(frozen=True)
class AgentResult:
    agent: str
    ok: bool
    summary: str
    payload: dict = field(default_factory=dict)
    confidence: float = 0.5
    risk: float = 0.0

