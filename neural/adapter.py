from __future__ import annotations

from pathlib import Path

import numpy as np
from numpy.typing import NDArray

from kernels.vector_math import stable_hash_embedding
from neural.jepa_model import TrainableJEPA


Array = NDArray[np.float64]


def fixed_width(values: list[float], width: int) -> Array:
    array = np.zeros((1, width), dtype=np.float64)
    clipped = values[:width]
    if clipped:
        array[0, : len(clipped)] = np.array(clipped, dtype=np.float64)
    return array


class NeuralWorldModelAdapter:
    def __init__(self, checkpoint: str = "artifacts/checkpoints/neural_jepa.npz") -> None:
        self.checkpoint = checkpoint
        self.model = TrainableJEPA()
        self.loaded = False
        if Path(checkpoint).exists():
            self.model.load(checkpoint)
            self.loaded = True

    def predict_vector(self, state_vector: list[float], action: dict) -> list[float] | None:
        if not self.loaded:
            return None
        context = fixed_width(state_vector, self.model.input_dim)
        action_vector = fixed_width(stable_hash_embedding(str(action), self.model.action_dim), self.model.action_dim)
        prediction = self.model.predict(context, action_vector)
        return prediction[0].astype(float).tolist()
