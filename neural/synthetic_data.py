from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray


Array = NDArray[np.float64]


@dataclass(frozen=True)
class SyntheticBatch:
    context: Array
    action: Array
    target: Array


class SyntheticWorldDataset:
    """Deterministic linear/nonlinear world used to prove the neural loop trains."""

    def __init__(self, input_dim: int = 32, action_dim: int = 8, seed: int = 7) -> None:
        self.input_dim = input_dim
        self.action_dim = action_dim
        self.rng = np.random.default_rng(seed)
        self.true_context = self.rng.normal(0.0, 0.8, size=(input_dim, input_dim))
        self.true_action = self.rng.normal(0.0, 0.4, size=(action_dim, input_dim))

    def batch(self, batch_size: int) -> SyntheticBatch:
        context = self.rng.normal(0.0, 1.0, size=(batch_size, self.input_dim))
        action = self.rng.normal(0.0, 1.0, size=(batch_size, self.action_dim))
        noise = self.rng.normal(0.0, 0.02, size=(batch_size, self.input_dim))
        target = np.tanh(context @ self.true_context + action @ self.true_action) + noise
        return SyntheticBatch(context=context, action=action, target=target)

