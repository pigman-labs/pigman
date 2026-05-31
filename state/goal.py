from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Goal:
    description: str
    success_criteria: list[str] = field(default_factory=list)
    constraints: list[str] = field(default_factory=list)
    deadline_seconds: float | None = None

