from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class Prediction:
    latent: Any
    uncertainty: float


class JEPAPredictor:
    def predict(self, context_latent: Any, mask: Any, action: Any | None = None) -> Prediction:
        return Prediction(
            latent={"context": context_latent, "mask": mask, "action": action},
            uncertainty=0.5,
        )

