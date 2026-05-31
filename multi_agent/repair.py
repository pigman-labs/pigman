from __future__ import annotations

from dataclasses import dataclass

from state.action import AgentAction
from verifiers.base import VerificationResult


@dataclass(frozen=True)
class RepairProposal:
    repaired_action: AgentAction
    reason: str
    requires_user: bool = False


class RepairPolicy:
    def propose(self, action: AgentAction, verification: VerificationResult) -> RepairProposal:
        issues = " ".join(verification.issues).lower()
        if verification.requires_permission:
            return RepairProposal(
                AgentAction(
                    "ask_user",
                    {"question": f"Permission required before {action.type}: {verification.issues}"},
                    risk_score=0.0,
                    verification_required=False,
                ),
                "verification requires explicit permission",
                requires_user=True,
            )
        if "shell command" in issues:
            return RepairProposal(
                AgentAction(
                    "say",
                    {"text": "The proposed shell command is malformed and needs a concrete argv list."},
                    risk_score=0.0,
                    verification_required=False,
                ),
                "malformed shell command",
            )
        if "filesystem" in issues or "path" in issues:
            return RepairProposal(
                AgentAction(
                    "say",
                    {"text": "The file operation is missing a valid path and cannot be executed."},
                    risk_score=0.0,
                    verification_required=False,
                ),
                "malformed filesystem action",
            )
        return RepairProposal(
            AgentAction(
                "say",
                {"text": f"Action rejected by verifier: {verification.issues}"},
                risk_score=0.0,
                verification_required=False,
            ),
            "generic verifier rejection",
        )
