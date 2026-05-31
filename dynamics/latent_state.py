from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class LatentState:
    global_state: dict[str, Any] = field(default_factory=dict)
    entities: list[dict[str, Any]] = field(default_factory=list)
    relations: list[dict[str, Any]] = field(default_factory=list)
    vector: list[float] = field(default_factory=list)
    events: list[dict[str, Any]] = field(default_factory=list)
    goals: list[dict[str, Any]] = field(default_factory=list)
    uncertainty: dict[str, float] = field(default_factory=dict)
    provenance: list[str] = field(default_factory=list)

    def copy(self) -> "LatentState":
        return LatentState(
            global_state=dict(self.global_state),
            entities=[dict(item) for item in self.entities],
            relations=[dict(item) for item in self.relations],
            vector=list(self.vector),
            events=[dict(item) for item in self.events],
            goals=[dict(item) for item in self.goals],
            uncertainty=dict(self.uncertainty),
            provenance=list(self.provenance),
        )


@dataclass
class BeliefState:
    current: LatentState
    hypotheses: list[LatentState] = field(default_factory=list)
    unresolved_questions: list[str] = field(default_factory=list)
