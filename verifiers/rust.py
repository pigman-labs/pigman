from __future__ import annotations

from tools.shell import ShellTool
from verifiers.base import Severity, VerificationResult


class CargoVerifier:
    def __init__(self, timeout: int = 120) -> None:
        self.shell = ShellTool()
        self.timeout = timeout

    def test(self) -> VerificationResult:
        return self._run(["cargo", "test"], "cargo_test")

    def build(self) -> VerificationResult:
        return self._run(["cargo", "build", "--workspace"], "cargo_build")

    def _run(self, command: list[str], verifier: str) -> VerificationResult:
        result = self.shell.run(command, timeout=self.timeout)
        if result.returncode == 0:
            return VerificationResult.pass_(verifier)
        return VerificationResult.fail(
            f"{verifier}_failed",
            f"{' '.join(command)} returned non-zero status",
            Severity.ERROR,
            "inspect cargo output and fix Rust build/test errors",
            verifier=verifier,
            evidence={"returncode": result.returncode, "stdout_tail": result.stdout[-2000:], "stderr_tail": result.stderr[-2000:]},
        )
