from __future__ import annotations

import subprocess
import sys
from dataclasses import dataclass
from time import time

from tools.results import ToolResult
from tools.safety import CommandClassification, CommandClassifier


@dataclass(frozen=True)
class ShellResult:
    command: list[str]
    returncode: int
    stdout: str
    stderr: str
    timed_out: bool = False
    classification: CommandClassification | None = None


class ShellTool:
    def __init__(self, classifier: CommandClassifier | None = None) -> None:
        self.classifier = classifier or CommandClassifier()

    def classify(self, command: list[str]) -> CommandClassification:
        return self.classifier.classify(command)

    def run(self, command: list[str], timeout: int = 30) -> ShellResult:
        command = self._normalize_command(command)
        classification = self.classify(command)
        if not classification.safe:
            return ShellResult(command, 126, "", "; ".join(classification.reasons), False, classification)
        try:
            completed = subprocess.run(command, capture_output=True, text=True, timeout=timeout, check=False)
        except subprocess.TimeoutExpired as exc:
            return ShellResult(
                command,
                124,
                self._coerce_text(exc.stdout),
                self._coerce_text(exc.stderr) or "command timed out",
                True,
                classification,
            )
        except OSError as exc:
            return ShellResult(command, 127, "", f"{type(exc).__name__}: {exc}", False, classification)
        return ShellResult(command, completed.returncode, completed.stdout, completed.stderr, False, classification)

    def _normalize_command(self, command: list[str]) -> list[str]:
        if command and command[0] in {"python", "python3"}:
            return [sys.executable, *command[1:]]
        return command

    def _coerce_text(self, value: object) -> str:
        if value is None:
            return ""
        if isinstance(value, bytes):
            return value.decode("utf-8", errors="replace")
        return str(value)

    def run_structured(self, command: list[str], timeout: int = 30) -> ToolResult:
        started = time()
        result = self.run(command, timeout)
        ended = time()
        return ToolResult(
            ok=result.returncode == 0,
            tool="shell",
            operation="run",
            stdout=result.stdout,
            stderr=result.stderr,
            data={
                "command": result.command,
                "returncode": result.returncode,
                "timed_out": result.timed_out,
                "classification": None if result.classification is None else result.classification.__dict__,
            },
            started_at=started,
            ended_at=ended,
        )
