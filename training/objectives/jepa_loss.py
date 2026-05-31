from __future__ import annotations

from jepa.losses import cosine_distance


def jepa_loss(predicted: list[float], target: list[float]) -> float:
    return cosine_distance(predicted, target)

