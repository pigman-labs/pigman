from __future__ import annotations

from verifiers.base import VerificationResult
from state.action import AgentAction


class SafetyVerifier:
    HIGH_RISK = {"delete", "deploy", "purchase", "transfer", "email_external"}

    def check(self, action: AgentAction | dict) -> VerificationResult:
        action_type = str(action.type if isinstance(action, AgentAction) else action.get("type", ""))
        if action_type in self.HIGH_RISK:
            return VerificationResult.fail(
                "high_risk_action_type",
                f"Action {action_type!r} requires explicit permission",
                requires_permission=True,
                verifier="safety",
                evidence={"action_type": action_type},
            )
        return VerificationResult.pass_("safety")
