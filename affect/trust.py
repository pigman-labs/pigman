from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class TrustStats:
    competence: float = 0.5
    benevolence: float = 0.5
    integrity: float = 0.5
    risk: float = 0.1
    observations: int = 0

    @property
    def score(self) -> float:
        numerator = 0.45 * self.competence + 0.25 * self.benevolence + 0.30 * self.integrity
        return max(0.0, min(1.0, numerator / (1.0 + self.risk)))


@dataclass
class TrustLedger:
    entities: dict[str, TrustStats] = field(default_factory=dict)

    def update(self, entity: str, competence: float, benevolence: float = 0.5, integrity: float = 0.5, risk: float = 0.1) -> float:
        stats = self.entities.setdefault(entity, TrustStats())
        n = stats.observations
        stats.competence = (stats.competence * n + competence) / (n + 1)
        stats.benevolence = (stats.benevolence * n + benevolence) / (n + 1)
        stats.integrity = (stats.integrity * n + integrity) / (n + 1)
        stats.risk = (stats.risk * n + risk) / (n + 1)
        stats.observations += 1
        return stats.score

    def score(self, entity: str) -> float:
        return self.entities.get(entity, TrustStats()).score

