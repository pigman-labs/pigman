from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray


Array = NDArray[np.float64]


@dataclass
class LinearCache:
    x: Array


class Linear:
    def __init__(self, input_dim: int, output_dim: int, rng: np.random.Generator) -> None:
        scale = (2.0 / (input_dim + output_dim)) ** 0.5
        self.weight: Array = rng.normal(0.0, scale, size=(input_dim, output_dim))
        self.bias: Array = np.zeros(output_dim, dtype=np.float64)
        self.grad_weight: Array = np.zeros_like(self.weight)
        self.grad_bias: Array = np.zeros_like(self.bias)

    def forward(self, x: Array) -> tuple[Array, LinearCache]:
        return x @ self.weight + self.bias, LinearCache(x=x)

    def backward(self, grad_out: Array, cache: LinearCache) -> Array:
        self.grad_weight += cache.x.T @ grad_out / max(1, cache.x.shape[0])
        self.grad_bias += grad_out.mean(axis=0)
        return grad_out @ self.weight.T

    def zero_grad(self) -> None:
        self.grad_weight.fill(0.0)
        self.grad_bias.fill(0.0)

    def step(self, lr: float, weight_decay: float = 0.0) -> None:
        if weight_decay:
            self.grad_weight += weight_decay * self.weight
        self.weight -= lr * self.grad_weight
        self.bias -= lr * self.grad_bias

    def state_dict(self) -> dict[str, Array]:
        return {"weight": self.weight, "bias": self.bias}

    def load_state_dict(self, state: dict[str, Array]) -> None:
        self.weight = np.array(state["weight"], dtype=np.float64)
        self.bias = np.array(state["bias"], dtype=np.float64)
        self.grad_weight = np.zeros_like(self.weight)
        self.grad_bias = np.zeros_like(self.bias)

