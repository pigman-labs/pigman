from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from dynamics.latent_state import LatentState
from dynamics.transition_model import TransitionModel
from jepa.predictor import JEPAPredictor, Prediction
from neural.adapter import NeuralWorldModelAdapter


@dataclass
class WorldModelPrediction:
    jepa: Prediction
    next_state: LatentState
    expected_events: list[dict]
    uncertainty: float
    neural_latent: list[float] | None = None


class WorldModel:
    def __init__(self) -> None:
        self.jepa = JEPAPredictor()
        self.transition = TransitionModel()
        self.neural = NeuralWorldModelAdapter()

    def predict(self, state: LatentState, mask: Any, action: dict | None = None) -> WorldModelPrediction:
        jepa_prediction = self.jepa.predict(state.global_state, mask, action)
        next_state = self.transition.predict_next(state, action or {"type": "observe"})
        expected_events = [
            {
                "type": "predicted_action_effect",
                "action": action or {"type": "observe"},
                "confidence": 1.0 - jepa_prediction.uncertainty,
            }
        ]
        neural_latent = self.neural.predict_vector(state.vector, action or {"type": "observe"})
        if neural_latent is not None:
            next_state.global_state["neural_world_model"] = {
                "checkpoint": self.neural.checkpoint,
                "latent_dim": len(neural_latent),
            }
        return WorldModelPrediction(
            jepa=jepa_prediction,
            next_state=next_state,
            expected_events=expected_events,
            uncertainty=jepa_prediction.uncertainty,
            neural_latent=neural_latent,
        )
