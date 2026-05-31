from pathlib import Path

from evals.memory_eval import run_memory_eval
from evals.planner_eval import run_planner_eval
from evals.tool_eval import run_tool_eval
from memory.persistent import JsonlEpisodicStore, SqliteMemoryStore
from tools.filesystem import FilesystemTool
from tools.patch import PatchTool
from verifiers.shell import ShellSafetyVerifier


def test_planner_eval_selects_best_action() -> None:
    result = run_planner_eval()
    assert result["mpc"] == "best"
    assert result["beam"] == "best"


def test_persistent_memory(tmp_path: Path) -> None:
    episodes = JsonlEpisodicStore(str(tmp_path / "episodes.jsonl"))
    db = SqliteMemoryStore(str(tmp_path / "memory.sqlite3"))
    episodes.append({"ok": True})
    db.upsert_fact("alpha", "beta", 0.9)
    assert episodes.read_recent()[0]["ok"] is True
    assert db.facts("alpha")[0].value == "beta"


def test_tool_and_patch(tmp_path: Path) -> None:
    target = tmp_path / "file.txt"
    target.write_text("hello\n", encoding="utf-8")
    patch = PatchTool().apply_replace(str(target), "hello", "world")
    assert patch["ok"]
    assert "world" in target.read_text(encoding="utf-8")
    assert "-a" in FilesystemTool().diff_text("a\n", "b\n")
    assert run_tool_eval()["diff_has_plus"]


def test_shell_safety() -> None:
    verifier = ShellSafetyVerifier()
    assert verifier.check_command(["python", "-m", "pytest"]).approved
    assert not verifier.check_command(["rm", "-rf", "/"]).approved


def test_memory_eval(tmp_path: Path) -> None:
    result = run_memory_eval(str(tmp_path))
    assert result["episodes"] >= 2
    assert result["facts"] >= 1
    assert result["vector_hits"] >= 1
    assert result["graph_hits"] >= 1
