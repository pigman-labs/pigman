from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory

from decoders.tool_decoder import ToolCall
from data.schemas import ActionRecord
from tools.filesystem import FilesystemTool
from tools.patch import PatchTool
from tools.rollback import RollbackManager
from tools.safety import CommandClassifier
from tools.shell import ShellTool
from tools.executor import ToolExecutor


def run_tool_eval() -> dict:
    fs = FilesystemTool()
    diff = fs.diff_text("a\n", "b\n")
    shell = ShellTool().run_structured(["echo", "ok"], timeout=5)
    dangerous = CommandClassifier().classify(["rm", "-rf", "/"])
    with TemporaryDirectory() as tmp:
        target = Path(tmp) / "file.txt"
        target.write_text("alpha\n", encoding="utf-8")
        patch = PatchTool().apply_replace_structured(str(target), "alpha", "beta")
        rollback = RollbackManager().apply(patch.rollback) if patch.rollback else {"ok": False}
        executor = ToolExecutor().execute(
            ToolCall("filesystem", {"path": str(target), "content": "gamma\n"}),
            ActionRecord("edit_file", {"path": str(target)}, True, 0.1),
        )
    return {
        "diff_has_minus": "-a" in diff,
        "diff_has_plus": "+b" in diff,
        "shell_ok": shell.ok,
        "dangerous_blocked": not dangerous.safe,
        "patch_ok": patch.ok,
        "rollback_ok": rollback["ok"],
        "executor_ok": executor.success,
        "executor_has_rollback": executor.metadata.get("rollback") is not None,
    }
