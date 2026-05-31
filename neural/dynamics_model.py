from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

from neural.layers import Linear
from neural.optim import OptimizerConfig


Array = NDArray[np.float64]


class TrainableLatentDynamics:
    def __init__(self, latent_dim: int = 24, action_dim: int = 8, seed: int = 11) -> None:
        rng = np.random.default_rng(seed)
        self.transition = Linear(latent_dim + action_dim, latent_dim, rng)

    def predict_delta(self, state: Array, action: Array) -> Array:
        output, _ = self.transition.forward(np.concatenate([state, action], axis=-1))
        return output

    def train_step(self, state: Array, action: Array, target_next: Array, cfg: OptimizerConfig) -> float:
        self.transition.zero_grad()
        combined = np.concatenate([state, action], axis=-1)
        pred_delta, cache = self.transition.forward(combined)
        pred_next = state + pred_delta
        diff = pred_next - target_next
        loss = float(np.mean(diff * diff))
        grad = 2.0 * diff / diff.size
        self.transition.backward(grad, cache)
        self.transition.step(cfg.lr, cfg.weight_decay)
        return loss
