from __future__ import annotations

from dynamics.latent_state import LatentState
from dynamics.transition_model import TransitionModel


def rollout(model: TransitionModel, state: LatentState, actions: list[dict]) -> list[LatentState]:
    states: list[LatentState] = []
    current = state
    for action in actions:
        current = model.predict_next(current, action)
        states.append(current)
    return states

