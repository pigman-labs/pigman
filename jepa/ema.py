from __future__ import annotations


def ema_update(target: float, source: float, tau: float) -> float:
    if not 0.0 <= tau <= 1.0:
        raise ValueError("tau must be in [0, 1]")
    return tau * target + (1.0 - tau) * source

