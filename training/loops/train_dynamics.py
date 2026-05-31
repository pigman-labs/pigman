from __future__ import annotations

from dataclasses import dataclass

from dynamics.latent_state import LatentState
from dynamics.transition_model import TransitionModel


@dataclass(frozen=True)
class DynamicsTrainStats:
    examples: int
    mean_uncertainty: float


def train_dynamics_smoke(examples: int = 4) -> DynamicsTrainStats:
    model = TransitionModel()
    state = LatentState(global_state={"phase": "train_smoke"})
    uncertainties = []
    for index in range(examples):
        state = model.predict_next(state, {"type": "synthetic", "index": index})
        uncertainties.append(state.uncertainty["transition"])
    return DynamicsTrainStats(examples=examples, mean_uncertainty=sum(uncertainties) / len(uncertainties))
