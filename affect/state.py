from __future__ import annotations

from dataclasses import dataclass


def clamp01(value: float) -> float:
    return max(0.0, min(1.0, float(value)))


@dataclass(frozen=True)
class AffectState:
    happiness: float = 0.5
    curiosity: float = 0.5
    greed: float = 0.2
    fear: float = 0.1
    anger: float = 0.0
    trust: float = 0.5
    boredom: float = 0.2
    surprise: float = 0.0
    bond: float = 0.2
    frustration: float = 0.0

    def bounded(self) -> "AffectState":
        return AffectState(*(clamp01(value) for value in self.vector()))

    def vector(self) -> tuple[float, ...]:
        return (
            self.happiness,
            self.curiosity,
            self.greed,
            self.fear,
            self.anger,
            self.trust,
            self.boredom,
            self.surprise,
            self.bond,
            self.frustration,
        )

    def as_dict(self) -> dict[str, float]:
        return {
            "happiness": self.happiness,
            "curiosity": self.curiosity,
            "greed": self.greed,
            "fear": self.fear,
            "anger": self.anger,
            "trust": self.trust,
            "boredom": self.boredom,
            "surprise": self.surprise,
            "bond": self.bond,
            "frustration": self.frustration,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "AffectState":
        return cls(**{key: clamp01(data.get(key, getattr(cls(), key))) for key in cls().as_dict()})


@dataclass(frozen=True)
class AffectInputs:
    prediction_error: float = 0.0
    previous_loss: float | None = None
    current_loss: float | None = None
    novelty: float = 0.0
    verifier_success: bool | None = None
    risk: float = 0.0
    coping_capacity: float = 0.5
    goal_progress: float = 0.0
    goal_blockage: float = 0.0
    repeated_failures: int = 0
    immediate_reward: float = 0.0
    delayed_reward: float = 0.0
    delay: float = 1.0
    trust_signal: float = 0.0
    bond_signal: float = 0.0

    @property
    def learning_progress(self) -> float:
        if self.previous_loss is None or self.current_loss is None:
            return 0.0
        return max(0.0, self.previous_loss - self.current_loss)

