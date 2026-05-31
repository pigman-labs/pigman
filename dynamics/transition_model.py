from __future__ import annotations

from dynamics.latent_state import LatentState


class TransitionModel:
    def predict_next(self, state: LatentState, action: dict, goal: dict | None = None) -> LatentState:
        next_state = state.copy()
        next_state.global_state = {
            **state.global_state,
            "last_predicted_action": action,
            "goal": goal or {},
        }
        next_state.events.append({"type": "predicted", "action": action, "goal": goal or {}})
        next_state.uncertainty = {**state.uncertainty, "transition": 0.5}
        return next_state
