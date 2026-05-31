from __future__ import annotations

from verifiers.base import VerificationResult
from tools.safety import CommandClassifier


class ShellSafetyVerifier:
    def __init__(self) -> None:
        self.classifier = CommandClassifier()

    def check_command(self, command: list[str]) -> VerificationResult:
        classification = self.classifier.classify(command)
        if not classification.safe:
            return VerificationResult.fail(
                "unsafe_shell_command",
                "; ".join(classification.reasons) or "unsafe shell command",
                requires_permission=classification.requires_permission,
                verifier="shell_safety",
                evidence={"command": command, "classification": classification.__dict__},
            )
        joined = " ".join(command).lower()
        dangerous = ["rm -rf", "git reset --hard", "drop table", "shutdown"]
        for item in dangerous:
            if item in joined:
                return VerificationResult.fail(
                    "dangerous_shell_pattern",
                    f"dangerous shell pattern: {item}",
                    requires_permission=True,
                    verifier="shell_safety",
                    evidence={"command": command, "pattern": item},
                )
        return VerificationResult.pass_("shell_safety")
