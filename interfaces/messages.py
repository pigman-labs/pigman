from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


@dataclass(frozen=True)
class RuntimeMessage:
    kind: Literal["observation", "action", "verification", "memory"]
    payload: dict
    trace_id: str


@dataclass(frozen=True)
class AgentResponse:
    trace_id: str
    approved: bool
    action: dict
    observation: dict
    belief_summary: dict
    issues: list[str]
