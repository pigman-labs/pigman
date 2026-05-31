# Verifiers

The `verifiers/` package is the policy and correctness gate between planning
and execution. It now returns structured issues with severity, repair hints, and
evidence while preserving the older `approved/issues` API.

## What Is Real

- Structured `VerificationIssue` with severity and repair hint.
- Mergeable `VerificationResult`.
- Shell safety verifier backed by command classification.
- Tool verifier for shell, filesystem, patch, and HTTP schemas.
- Filesystem write verifier with allowed-root checks and size limits.
- Risk policy verifier for auto-execution thresholds.
- Source provenance verifier.
- World-state consistency verifier.
- Pytest and Cargo verifier wrappers.
- Ensemble verifier that merges safety, policy, and tool checks.

## Files

- `base.py`: result and issue schema.
- `ensemble.py`: aggregate verifier.
- `tool.py`: tool-call schema and safety validation.
- `shell.py`: command safety validation.
- `filesystem.py`: write-path and size validation.
- `policy.py`: risk threshold policy.
- `source.py`: provenance checks.
- `world_state.py`: belief-state consistency checks.
- `pytest_verifier.py`: pytest wrapper.
- `rust.py`: cargo test/build wrapper.
- `code.py`: compile/pytest project verifier.

## Policy Shape

Verifiers do not execute tools. They only inspect intended actions, decoded tool
calls, source metadata, and state. Execution remains in `tools/`; verification
returns enough structure for the planner or repair policy to choose a safer next
action.

## Remaining Gaps

- Capability-scoped permission prompts.
- Full data exfiltration and secret scanning.
- Network allowlists and provenance trust scoring.
- Formal policy language.
- Sandboxed execution proofs from the OS or container layer.
