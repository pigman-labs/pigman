from __future__ import annotations

from dataclasses import dataclass
from random import Random


@dataclass(frozen=True)
class MaskSpec:
    visible_indices: tuple[int, ...]
    target_indices: tuple[int, ...]
    mask_type: str = "block"


def block_mask(length: int, target_fraction: float = 0.4, seed: int = 7) -> MaskSpec:
    rng = Random(seed)
    target_count = max(1, int(length * target_fraction))
    target = tuple(sorted(rng.sample(range(length), target_count)))
    visible = tuple(index for index in range(length) if index not in set(target))
    return MaskSpec(visible_indices=visible, target_indices=target)

