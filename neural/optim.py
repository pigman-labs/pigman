from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class OptimizerConfig:
    lr: float = 0.05
    weight_decay: float = 1e-4
    ema_tau: float = 0.99

