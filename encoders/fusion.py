from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from kernels.vector_math import normalize


@dataclass
class FusedLatent:
    global_summary: dict[str, Any] = field(default_factory=dict)
    entities: list[dict[str, Any]] = field(default_factory=list)
    relations: list[dict[str, Any]] = field(default_factory=list)
    vector: list[float] = field(default_factory=list)


class CrossModalFusion:
    def fuse(self, latents: list[Any]) -> FusedLatent:
        vectors = [getattr(item, "vector") for item in latents if hasattr(item, "vector")]
        vector: list[float] = []
        if vectors:
            dim = len(vectors[0])
            accum = [0.0 for _ in range(dim)]
            for item in vectors:
                for index, value in enumerate(item):
                    accum[index] += value
            vector = normalize(accum)

        entities: list[dict[str, Any]] = []
        for latent in latents:
            if hasattr(latent, "path"):
                entities.append({"type": "file", "path": latent.path, "exists": latent.exists})
            if hasattr(latent, "intent"):
                entities.append({"type": "intent", "intent": latent.intent})

        return FusedLatent(
            global_summary={
                "modalities": [type(item).__name__ for item in latents],
                "count": len(latents),
            },
            entities=entities,
            vector=vector,
        )
