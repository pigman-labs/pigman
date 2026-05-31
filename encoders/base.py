from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from data.schemas import EncodedObservation, Observation


class Encoder(ABC):
    modality: str

    @abstractmethod
    def encode(self, observation: Any) -> Any:
        raise NotImplementedError

    def encode_observation(self, observation: Observation) -> EncodedObservation:
        payload = observation.metadata if self.modality == "tool_trace" and observation.metadata else observation.raw_ref
        latent = self.encode(payload)
        return EncodedObservation(
            observation=observation,
            modality=self.modality,
            vector=getattr(latent, "vector", []),
            summary=str(getattr(latent, "summary", getattr(latent, "text", latent))),
            entities=[latent.__dict__] if hasattr(latent, "__dict__") else [],
        )
