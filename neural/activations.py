from __future__ import annotations

import numpy as np
from numpy.typing import NDArray


Array = NDArray[np.float64]


def tanh(x: Array) -> Array:
    return np.tanh(x)


def tanh_grad(y: Array) -> Array:
    return 1.0 - y * y


def l2_normalize(x: Array, eps: float = 1e-8) -> Array:
    norm = np.linalg.norm(x, axis=-1, keepdims=True)
    return x / np.maximum(norm, eps)

