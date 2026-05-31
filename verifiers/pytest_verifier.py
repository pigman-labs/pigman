from __future__ import annotations

import sys

from tools.shell import ShellTool
from verifiers.base import Severity, VerificationResult


class PytestVerifier:
    def __init__(self, timeout: int = 120) -> None:
        self.shell = ShellTool()
        self.timeout = timeout

    def check(self, args: list[str] | None = None) -> VerificationResult:
        command = [sys.executable, "-m", "pytest", *(args or [])]
        result = self.shell.run(command, timeout=self.timeout)
        if result.returncode == 0:
            return VerificationResult.pass_("pytest")
        return VerificationResult.fail(
            "pytest_failed",
            "pytest returned non-zero status",
            Severity.ERROR,
            "inspect pytest output and fix failing tests",
            verifier="pytest",
            evidence={"returncode": result.returncode, "stdout_tail": result.stdout[-2000:], "stderr_tail": result.stderr[-2000:]},
        )
