from __future__ import annotations

from verifiers.base import VerificationResult


class SourceProvenanceVerifier:
    def check(self, payload: dict) -> VerificationResult:
        if not payload.get("provenance"):
            return VerificationResult.fail(
                "missing_provenance",
                "missing provenance",
                repair_hint="attach source URI, trace id, or local origin metadata",
                verifier="source_provenance",
            )
        return VerificationResult.pass_("source_provenance")
