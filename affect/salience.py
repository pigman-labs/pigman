from __future__ import annotations

from dataclasses import dataclass

from affect.state import AffectState


@dataclass(frozen=True)
class SalienceInputs:
    verifier_impact: float = 0.0
    goal_importance: float = 0.5
    novelty: float = 0.0


class MemorySalience:
    def score(self, before: AffectState, after: AffectState, inputs: SalienceInputs | None = None) -> float:
        inputs = inputs or SalienceInputs()
        affect_delta = sum(abs(a - b) for a, b in zip(before.vector(), after.vector(), strict=True)) / 10.0
        score = (
            0.35 * after.surprise
            + 0.20 * after.curiosity
            + 0.15 * after.frustration
            + 0.10 * affect_delta
            + 0.10 * inputs.verifier_impact
            + 0.05 * inputs.goal_importance
            + 0.05 * inputs.novelty
        )
        return max(0.0, min(1.0, score))

