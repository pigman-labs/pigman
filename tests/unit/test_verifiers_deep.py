from __future__ import annotations

from decoders.tool_decoder import ToolCall
from dynamics.latent_state import LatentState
from evals.verifier_eval import run_verifier_eval
from state.action import AgentAction
from verifiers.base import Severity, VerificationResult
from verifiers.ensemble import VerifierEnsemble
from verifiers.filesystem import FilesystemWriteVerifier
from verifiers.policy import PolicyVerifier, RiskPolicy
from verifiers.shell import ShellSafetyVerifier
from verifiers.source import SourceProvenanceVerifier
from verifiers.tool import ToolVerifier
from verifiers.world_state import WorldStateVerifier


def test_verification_result_preserves_structured_issue() -> None:
    result = VerificationResult.fail(
        "x",
        "broken",
        Severity.CRITICAL,
        "fix it",
        requires_permission=True,
        verifier="test",
    )

    assert not result.approved
    assert result.requires_permission
    assert result.structured_issues[0].severity == Severity.CRITICAL
    assert result.as_dict()["structured_issues"][0]["repair_hint"] == "fix it"


def test_policy_verifier_blocks_high_risk_and_warns_medium_risk() -> None:
    verifier = PolicyVerifier(RiskPolicy(max_auto_risk=0.8, max_safe_risk=0.4))

    blocked = verifier.check(AgentAction("run_shell", {}, risk_score=0.95))
    warning = verifier.check(AgentAction("run_shell", {}, risk_score=0.5))

    assert not blocked.approved
    assert blocked.requires_permission
    assert warning.approved
    assert warning.structured_issues[0].severity == Severity.WARNING


def test_filesystem_write_verifier_blocks_outside_roots() -> None:
    verifier = FilesystemWriteVerifier(allowed_roots=("artifacts",))

    assert verifier.check_path("artifacts/x.txt").approved
    blocked = verifier.check_path("/tmp/outside.txt")
    assert not blocked.approved
    assert blocked.requires_permission


def test_shell_safety_uses_command_classifier() -> None:
    verifier = ShellSafetyVerifier()

    assert verifier.check_command(["echo", "ok"]).approved
    blocked = verifier.check_command(["rm", "-rf", "/"])
    assert not blocked.approved
    assert blocked.structured_issues


def test_tool_verifier_validates_shell_filesystem_patch_and_http() -> None:
    verifier = ToolVerifier()

    assert verifier.check(ToolCall("shell", {"command": ["echo", "ok"]})).approved
    assert not verifier.check(ToolCall("shell", {"command": []})).approved
    assert verifier.check(ToolCall("filesystem", {"path": "artifacts/tool.txt", "content": "x"})).approved
    assert not verifier.check(ToolCall("patch", {"path": "artifacts/tool.txt"})).approved
    assert not verifier.check(ToolCall("http", {"url": "ftp://example.com"})).approved


def test_ensemble_merges_policy_safety_and_tool_findings() -> None:
    result = VerifierEnsemble().check(
        AgentAction("run_shell", {"command": ["rm", "-rf", "/"]}, risk_score=0.95),
        ToolCall("shell", {"command": ["rm", "-rf", "/"]}),
    )

    assert not result.approved
    assert result.requires_permission
    assert len(result.structured_issues) >= 2


def test_source_and_world_state_verifiers_return_repair_hints() -> None:
    source = SourceProvenanceVerifier().check({})
    state = LatentState()
    world = WorldStateVerifier().check(state)

    assert not source.approved
    assert "provenance" in source.issues[0]
    assert not world.approved
    assert world.structured_issues[0].repair_hint


def test_verifier_eval_exercises_ensemble() -> None:
    result = run_verifier_eval()

    assert result["safe"]
    assert result["unsafe_blocked"]
    assert result["ensemble_safe"]
    assert result["ensemble_rejected"]
    assert result["structured_issues"] >= 1
