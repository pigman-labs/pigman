from __future__ import annotations

from pathlib import Path

from data.schemas import ActionRecord
from decoders.tool_decoder import ToolCall
from evals.tool_eval import run_tool_eval
from tools.browser import BrowserAction, BrowserTool
from tools.executor import ToolExecutor
from tools.filesystem import FilesystemTool
from tools.patch import PatchTool
from tools.registry import ToolRegistry
from tools.rollback import RollbackManager
from tools.safety import CommandClassifier
from tools.shell import ShellTool


def test_command_classifier_blocks_destructive_patterns() -> None:
    classifier = CommandClassifier()

    assert classifier.classify(["python", "-m", "pytest"]).safe
    blocked = classifier.classify(["rm", "-rf", "/"])
    assert not blocked.safe
    assert blocked.requires_permission


def test_shell_tool_returns_structured_timeout() -> None:
    result = ShellTool().run_structured(["sleep", "2"], timeout=1)

    assert not result.ok
    assert result.data["returncode"] == 124
    assert result.data["timed_out"] is True


def test_filesystem_structured_write_and_rollback(tmp_path: Path) -> None:
    target = tmp_path / "note.txt"
    target.write_text("before", encoding="utf-8")

    result = FilesystemTool().write_structured(str(target), "after")
    rollback = RollbackManager().apply(result.rollback)

    assert result.ok
    assert result.rollback.before == "before"
    assert rollback["ok"]
    assert target.read_text(encoding="utf-8") == "before"


def test_patch_structured_replace_and_rollback(tmp_path: Path) -> None:
    target = tmp_path / "note.txt"
    target.write_text("hello world", encoding="utf-8")

    result = PatchTool().apply_replace_structured(str(target), "world", "agent")
    rollback = RollbackManager().apply(result.rollback)

    assert result.ok
    assert target.read_text(encoding="utf-8") == "hello world"
    assert rollback["ok"]


def test_browser_stub_returns_tool_result() -> None:
    result = BrowserTool().execute_structured(BrowserAction("navigate", url="http://localhost"))

    assert result.ok
    assert result.tool == "browser"
    assert result.data["action"]["url"] == "http://localhost"


def test_tool_registry_lists_default_tools() -> None:
    registry = ToolRegistry.default()
    names = {spec.name for spec in registry.list()}

    assert {"shell", "filesystem", "patch", "http", "browser"}.issubset(names)


def test_executor_routes_patch_and_filesystem(tmp_path: Path) -> None:
    target = tmp_path / "note.txt"
    target.write_text("alpha", encoding="utf-8")
    executor = ToolExecutor()
    action = ActionRecord("edit_file", {"path": str(target)}, True, 0.1)

    patch = executor.execute(ToolCall("patch", {"path": str(target), "old": "alpha", "new": "beta"}), action)
    write = executor.execute(ToolCall("filesystem", {"path": str(target), "content": "gamma"}), action)

    assert patch.success
    assert patch.metadata["rollback"] is not None
    assert write.success
    assert write.metadata["rollback"] is not None


def test_tool_eval_exercises_safety_patch_shell_and_executor() -> None:
    result = run_tool_eval()

    assert result["shell_ok"]
    assert result["dangerous_blocked"]
    assert result["patch_ok"]
    assert result["rollback_ok"]
    assert result["executor_ok"]
