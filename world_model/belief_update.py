from __future__ import annotations

from data.schemas import EncodedObservation
from dynamics.latent_state import LatentState
from encoders.fusion import CrossModalFusion
from kernels.vector_math import normalize


class BeliefUpdater:
    def __init__(self) -> None:
        self.fusion = CrossModalFusion()

    def update(self, previous: LatentState, observations: list[EncodedObservation]) -> LatentState:
        state = previous.copy()
        fused = self.fusion.fuse(observations)

        if state.vector and fused.vector:
            state.vector = normalize([a + b for a, b in zip(state.vector, fused.vector, strict=True)])
        elif fused.vector:
            state.vector = fused.vector

        state.global_state.update(
            {
                "last_observation_count": len(observations),
                "last_modalities": [item.modality for item in observations],
                "fused_summary": fused.global_summary,
            }
        )
        state.entities.extend(fused.entities)
        state.events.extend(
            {
                "type": "observation",
                "source": item.observation.source,
                "summary": item.summary[:240],
                "confidence": item.confidence,
            }
            for item in observations
        )
        state.uncertainty["belief"] = max(0.05, 1.0 / (1.0 + len(state.events)))
        state.provenance.append("belief_update")
        return state
