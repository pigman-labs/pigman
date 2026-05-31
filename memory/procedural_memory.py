from __future__ import annotations

from dataclasses import dataclass, field
from time import time


@dataclass(frozen=True)
class Procedure:
    name: str
    trigger: str
    actions: tuple[dict, ...]
    importance: float = 0.5
    success_count: int = 0
    failure_count: int = 0
    updated_at: float = 0.0

    @property
    def reliability(self) -> float:
        total = self.success_count + self.failure_count
        if total == 0:
            return 0.5
        return self.success_count / total

    def score(self, goal_text: str) -> float:
        lowered = goal_text.lower()
        trigger_match = 1.0 if self.trigger.lower() in lowered else 0.0
        return trigger_match + self.importance * 0.4 + self.reliability * 0.4


@dataclass
class ProceduralMemory:
    procedures: list[Procedure] = field(default_factory=list)

    def add(self, procedure: Procedure) -> None:
        stamped = Procedure(
            procedure.name,
            procedure.trigger,
            procedure.actions,
            procedure.importance,
            procedure.success_count,
            procedure.failure_count,
            procedure.updated_at or time(),
        )
        self.procedures = [item for item in self.procedures if item.name != stamped.name]
        self.procedures.append(stamped)

    def match(self, goal_text: str, limit: int = 5) -> list[Procedure]:
        lowered = goal_text.lower()
        matches = [procedure for procedure in self.procedures if procedure.trigger.lower() in lowered]
        return sorted(matches, key=lambda procedure: procedure.score(goal_text), reverse=True)[:limit]

    def record_outcome(self, name: str, success: bool) -> None:
        updated = []
        for procedure in self.procedures:
            if procedure.name != name:
                updated.append(procedure)
                continue
            updated.append(
                Procedure(
                    procedure.name,
                    procedure.trigger,
                    procedure.actions,
                    procedure.importance,
                    procedure.success_count + int(success),
                    procedure.failure_count + int(not success),
                    time(),
                )
            )
        self.procedures = updated
