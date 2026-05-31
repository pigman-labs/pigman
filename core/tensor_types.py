from __future__ import annotations

from dataclasses import dataclass
from typing import Any


Tensor = Any


@dataclass(frozen=True)
class ShapeSpec:
    name: str
    axes: tuple[str, ...]


LATENT_GLOBAL = ShapeSpec("latent_global", ("batch", "dim"))
LATENT_SEQUENCE = ShapeSpec("latent_sequence", ("batch", "time", "dim"))
LATENT_ENTITIES = ShapeSpec("latent_entities", ("batch", "entities", "dim"))

