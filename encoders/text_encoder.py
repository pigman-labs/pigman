from __future__ import annotations

from dataclasses import dataclass

from encoders.base import Encoder
from kernels.vector_math import stable_hash_embedding


@dataclass
class TextLatent:
    text: str
    tokens: tuple[str, ...]
    vector: list[float]
    intent: str
    constraints: tuple[str, ...] = ()


class TextEncoder(Encoder):
    modality = "text"

    def encode(self, observation: str) -> TextLatent:
        tokens = tuple(observation.split())
        lowered = observation.lower()
        if any(word in lowered for word in ("run", "test", "check", "build")):
            intent = "execute_or_verify"
        elif any(word in lowered for word in ("explain", "what", "why", "how")):
            intent = "answer"
        elif any(word in lowered for word in ("create", "edit", "write", "implement")):
            intent = "modify"
        else:
            intent = "observe"
        return TextLatent(
            text=observation,
            tokens=tokens,
            vector=stable_hash_embedding(observation),
            intent=intent,
        )
