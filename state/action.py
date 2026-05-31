from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal


ActionType = Literal[
    "say",
    "observe",
    "edit_file",
    "run_shell",
    "click",
    "type",
    "api_call",
    "query_memory",
    "simulate",
    "ask_user",
]


@dataclass(frozen=True)
class AgentAction:
    type: ActionType
    payload: dict
    reversible: bool = True
    risk_score: float = 0.0
    expected_effects: list[str] = field(default_factory=list)
    verification_required: bool = True
    timeout_seconds: int = 30

    def to_record(self):
        from data.schemas import ActionRecord

        return ActionRecord(
            type=self.type,
            payload=self.payload,
            reversible=self.reversible,
            risk_score=self.risk_score,
            expected_effects=tuple(self.expected_effects),
        )
