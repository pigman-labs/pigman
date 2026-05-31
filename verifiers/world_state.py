from __future__ import annotations

from dynamics.latent_state import LatentState
from verifiers.base import VerificationResult


class WorldStateVerifier:
    def check(self, state: LatentState) -> VerificationResult:
        issues: list[str] = []
        if not state.provenance:
            issues.append("state has no provenance")
        if state.uncertainty.get("belief", 1.0) > 0.95 and state.events:
            issues.append("belief uncertainty remained high despite observations")
        if issues:
            result = VerificationResult.pass_("world_state")
            for issue in issues:
                result = result.merge(
                    VerificationResult.fail(
                        "world_state_inconsistent",
                        issue,
                        repair_hint="refresh observations or lower confidence before acting",
                        verifier="world_state",
                    )
                )
            return result
        return VerificationResult.pass_("world_state")
