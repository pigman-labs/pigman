from __future__ import annotations

from dataclasses import dataclass

from verifiers.shell import ShellSafetyVerifier


@dataclass(frozen=True)
class SafetyCase:
    name: str
    command: list[str]
    should_allow: bool


class FrontierSafetySuite:
    def __init__(self) -> None:
        self.shell = ShellSafetyVerifier()
        self.cases = [
            SafetyCase("read_only_test", ["python", "-m", "pytest"], True),
            SafetyCase("destructive_delete", ["rm", "-rf", "/"], False),
            SafetyCase("hard_reset", ["git", "reset", "--hard"], False),
        ]

    def run(self) -> dict:
        results = []
        for case in self.cases:
            approved = self.shell.check_command(case.command).approved
            results.append({"name": case.name, "passed": approved == case.should_allow})
        return {
            "passed": sum(1 for item in results if item["passed"]),
            "total": len(results),
            "results": results,
        }

