from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray

from neural.activations import l2_normalize, tanh, tanh_grad
from neural.checkpoint import load_npz, save_npz
from neural.layers import Linear
from neural.optim import OptimizerConfig


Array = NDArray[np.float64]


@dataclass
class TrainStep:
    loss: float
    prediction_norm: float
    target_norm: float


class TrainableJEPA:
    """Small but real action-conditioned JEPA trained with manual backprop."""

    def __init__(
        self,
        input_dim: int = 32,
        action_dim: int = 8,
        latent_dim: int = 24,
        hidden_dim: int = 48,
        seed: int = 7,
    ) -> None:
        self.input_dim = input_dim
        self.action_dim = action_dim
        self.latent_dim = latent_dim
        self.hidden_dim = hidden_dim
        rng = np.random.default_rng(seed)
        self.context_encoder = Linear(input_dim, latent_dim, rng)
        self.target_encoder = Linear(input_dim, latent_dim, rng)
        self.predictor_1 = Linear(latent_dim + action_dim, hidden_dim, rng)
        self.predictor_2 = Linear(hidden_dim, latent_dim, rng)
        self._copy_context_to_target()

    def _copy_context_to_target(self) -> None:
        self.target_encoder.weight = self.context_encoder.weight.copy()
        self.target_encoder.bias = self.context_encoder.bias.copy()

    def encode_context(self, context: Array) -> Array:
        z, _ = self.context_encoder.forward(context)
        return l2_normalize(tanh(z))

    def encode_target(self, target: Array) -> Array:
        z, _ = self.target_encoder.forward(target)
        return l2_normalize(tanh(z))

    def predict(self, context: Array, action: Array) -> Array:
        z_context, _ = self.context_encoder.forward(context)
        z_context = tanh(z_context)
        combined = np.concatenate([z_context, action], axis=-1)
        hidden, _ = self.predictor_1.forward(combined)
        hidden = tanh(hidden)
        pred, _ = self.predictor_2.forward(hidden)
        return l2_normalize(pred)

    def train_step(self, context: Array, action: Array, target: Array, cfg: OptimizerConfig) -> TrainStep:
        self.zero_grad()

        z_raw, z_cache = self.context_encoder.forward(context)
        z_context = tanh(z_raw)
        combined = np.concatenate([z_context, action], axis=-1)
        h_raw, h_cache = self.predictor_1.forward(combined)
        h = tanh(h_raw)
        pred_raw, pred_cache = self.predictor_2.forward(h)
        pred = l2_normalize(pred_raw)

        target_raw, _ = self.target_encoder.forward(target)
        target_latent = l2_normalize(tanh(target_raw))

        diff = pred - target_latent
        loss = float(np.mean(diff * diff))
        grad_pred = 2.0 * diff / diff.size

        # Backprop through an approximate normalized prediction path. This is
        # enough for a real trainable local baseline without pulling autograd in.
        grad_h = self.predictor_2.backward(grad_pred, pred_cache)
        grad_h_raw = grad_h * tanh_grad(h)
        grad_combined = self.predictor_1.backward(grad_h_raw, h_cache)
        grad_z = grad_combined[:, : self.latent_dim]
        grad_z_raw = grad_z * tanh_grad(z_context)
        self.context_encoder.backward(grad_z_raw, z_cache)

        self.step(cfg.lr, cfg.weight_decay)
        self.ema_target(cfg.ema_tau)

        return TrainStep(
            loss=loss,
            prediction_norm=float(np.linalg.norm(pred, axis=-1).mean()),
            target_norm=float(np.linalg.norm(target_latent, axis=-1).mean()),
        )

    def zero_grad(self) -> None:
        for layer in (self.context_encoder, self.predictor_1, self.predictor_2):
            layer.zero_grad()

    def step(self, lr: float, weight_decay: float) -> None:
        for layer in (self.context_encoder, self.predictor_1, self.predictor_2):
            layer.step(lr, weight_decay)

    def ema_target(self, tau: float) -> None:
        self.target_encoder.weight = tau * self.target_encoder.weight + (1.0 - tau) * self.context_encoder.weight
        self.target_encoder.bias = tau * self.target_encoder.bias + (1.0 - tau) * self.context_encoder.bias

    def save(self, path: str) -> None:
        save_npz(
            path,
            context_weight=self.context_encoder.weight,
            context_bias=self.context_encoder.bias,
            target_weight=self.target_encoder.weight,
            target_bias=self.target_encoder.bias,
            predictor_1_weight=self.predictor_1.weight,
            predictor_1_bias=self.predictor_1.bias,
            predictor_2_weight=self.predictor_2.weight,
            predictor_2_bias=self.predictor_2.bias,
        )

    def load(self, path: str) -> None:
        state = load_npz(path)
        self.context_encoder.load_state_dict({"weight": state["context_weight"], "bias": state["context_bias"]})
        self.target_encoder.load_state_dict({"weight": state["target_weight"], "bias": state["target_bias"]})
        self.predictor_1.load_state_dict({"weight": state["predictor_1_weight"], "bias": state["predictor_1_bias"]})
        self.predictor_2.load_state_dict({"weight": state["predictor_2_weight"], "bias": state["predictor_2_bias"]})
