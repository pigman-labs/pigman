from __future__ import annotations

from dynamics.latent_state import LatentState
from dynamics.transition_model import TransitionModel


def smoke_eval() -> dict:
    model = TransitionModel()
    predicted = model.predict_next(LatentState(), {"type": "observe"})
    return {"ok": "last_predicted_action" in predicted.global_state}

