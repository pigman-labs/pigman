from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PretrainStats:
    steps: int
    loss: float


def run_pretrain_smoke() -> PretrainStats:
    return PretrainStats(steps=1, loss=0.0)

