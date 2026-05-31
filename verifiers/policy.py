from __future__ import annotations

from dataclasses import dataclass

from state.action import AgentAction
from verifiers.base import Severity, VerificationIssue, VerificationResult


@dataclass(frozen=True)
class RiskPolicy:
    max_auto_risk: float = 0.8
    max_safe_risk: float = 0.4


class PolicyVerifier:
    def __init__(self, policy: RiskPolicy | None = None) -> None:
        self.policy = policy or RiskPolicy()

    def check(self, action: AgentAction) -> VerificationResult:
        if action.risk_score >= self.policy.max_auto_risk:
            return VerificationResult.fail(
                "risk_above_auto_threshold",
                f"action risk {action.risk_score:.2f} exceeds auto-execution threshold",
                Severity.CRITICAL,
                "request explicit permission or choose a lower-risk action",
                requires_permission=True,
                verifier="policy",
                evidence={"risk_score": action.risk_score, "threshold": self.policy.max_auto_risk},
            )
        if action.risk_score > self.policy.max_safe_risk:
            return VerificationResult(
                True,
                structured_issues=[
                    VerificationIssue(
                        "risk_above_safe_threshold",
                        f"action risk {action.risk_score:.2f} should be logged",
                        Severity.WARNING,
                        "keep rollback metadata and trace this action",
                        {"risk_score": action.risk_score},
                    )
                ],
                verifier="policy",
            )
        return VerificationResult.pass_("policy")
