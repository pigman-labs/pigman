from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class CommandClassification:
    category: str
    safe: bool
    requires_permission: bool = False
    reasons: list[str] = field(default_factory=list)


class CommandClassifier:
    READ_ONLY = {
        "pwd",
        "ls",
        "cat",
        "sed",
        "rg",
        "grep",
        "find",
        "python",
        "python3",
        "pytest",
        "cargo",
        "git",
        "echo",
        "sleep",
    }
    DESTRUCTIVE = {"rm", "rmdir", "shutdown", "reboot", "mkfs", "dd"}
    RISKY_PATTERNS = ("rm -rf", "git reset --hard", "drop table", "sudo", "chmod -r", "chown -r")

    def classify(self, command: list[str]) -> CommandClassification:
        if not command:
            return CommandClassification("invalid", False, reasons=["empty command"])
        executable = Path(str(command[0])).name
        joined = " ".join(str(part) for part in command).lower()
        reasons = [pattern for pattern in self.RISKY_PATTERNS if pattern in joined]
        if executable in self.DESTRUCTIVE:
            reasons.append(f"destructive executable: {executable}")
        if reasons:
            return CommandClassification("dangerous", False, True, reasons)
        if executable in self.READ_ONLY:
            category = "test" if executable in {"pytest", "cargo"} or "pytest" in joined else "read_or_build"
            return CommandClassification(category, True)
        return CommandClassification("unknown", True, True, ["unknown executable requires policy review"])
