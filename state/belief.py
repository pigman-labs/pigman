from __future__ import annotations

from dataclasses import dataclass, field

from dynamics.latent_state import LatentState


@dataclass
class Hypothesis:
    state: LatentState
    probability: float
    evidence: list[str] = field(default_factory=list)


@dataclass
class BeliefGraph:
    current: LatentState
    hypotheses: list[Hypothesis] = field(default_factory=list)
    contradictions: list[str] = field(default_factory=list)

    def add_contradiction(self, message: str) -> None:
        self.contradictions.append(message)

