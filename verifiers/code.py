from __future__ import annotations

from tools.shell import ShellTool
from verifiers.base import VerificationResult
import sys


class CodeVerifier:
    def __init__(self) -> None:
        self.shell = ShellTool()

    def pytest(self) -> VerificationResult:
        result = self.shell.run([sys.executable, "-m", "pytest"])
        return VerificationResult(
            approved=result.returncode == 0,
            issues=[] if result.returncode == 0 else [result.stdout[-1000:] + result.stderr[-1000:]],
            requires_repair=result.returncode != 0,
            verifier="pytest",
        )

    def compile_python(self) -> VerificationResult:
        packages = [
            "core",
            "data",
            "encoders",
            "jepa",
            "dynamics",
            "memory",
            "planner",
            "policies",
            "decoders",
            "verifiers",
            "tools",
            "training",
            "serving",
            "evals",
            "state",
            "world_model",
            "causal",
            "routing",
            "orchestration",
            "interfaces",
            "simulators",
            "storage",
            "telemetry",
            "security",
            "kernels",
            "scripts",
        ]
        result = self.shell.run([sys.executable, "-m", "compileall", *packages])
        return VerificationResult(
            approved=result.returncode == 0,
            issues=[] if result.returncode == 0 else [result.stdout[-1000:] + result.stderr[-1000:]],
            requires_repair=result.returncode != 0,
            verifier="compile_python",
        )
