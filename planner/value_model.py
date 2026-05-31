from __future__ import annotations

from dynamics.latent_state import LatentState


class ValueModel:
    def score(self, state: LatentState, goal: dict) -> float:
        if not goal:
            return 0.0
        return 0.1 if state.global_state else 0.0

