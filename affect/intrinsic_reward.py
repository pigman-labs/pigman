from __future__ import annotations

from dataclasses import dataclass

from affect.state import AffectState


@dataclass(frozen=True)
class IntrinsicRewardWeights:
    curiosity: float = 1.0
    happiness: float = 0.4
    safe_surprise: float = 0.35
    trust: float = 0.15
    bond: float = 0.05
    fear: float = 0.8
    boredom: float = 0.3
    frustration: float = 0.7
    anger: float = 0.4
    greed_penalty: float = 0.15


class IntrinsicReward:
    def __init__(self, weights: IntrinsicRewardWeights | None = None) -> None:
        self.weights = weights or IntrinsicRewardWeights()

    def compute(self, state: AffectState) -> float:
        w = self.weights
        safe_surprise = state.surprise * (1.0 - state.fear)
        return (
            w.curiosity * state.curiosity
            + w.happiness * state.happiness
            + w.safe_surprise * safe_surprise
            + w.trust * state.trust
            + w.bond * state.bond
            - w.fear * state.fear
            - w.boredom * state.boredom
            - w.frustration * state.frustration
            - w.anger * state.anger
            - w.greed_penalty * state.greed
        )

