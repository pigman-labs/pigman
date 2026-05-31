# Tools

The `tools/` package is the local execution boundary for the agent. It wraps
side effects in structured results so planning, verification, memory, and
runtime layers can reason about what happened and how to roll it back.

## What Is Real

- Shell execution with timeout handling and command classification.
- Filesystem read/write/list/diff with structured write metadata.
- Patch replacement with rollback records.
- Rollback manager for file writes and text replacements.
- HTTP request wrapper using stdlib `urllib`.
- Browser action schema-compatible stub.
- Tool registry describing available operations.
- `ToolExecutor` routing for shell, filesystem, patch, HTTP, browser, memory,
  text, and fallback no-op actions.
- Tool eval covering diff, shell, safety classification, patch rollback, and
  executor rollback metadata.

## Files

- `executor.py`: central dispatcher from decoded tool calls to execution result.
- `results.py`: `ToolResult` and `RollbackRecord`.
- `safety.py`: command classifier.
- `rollback.py`: rollback application.
- `registry.py`: tool metadata registry.
- `shell.py`: subprocess execution.
- `filesystem.py`: file operations.
- `patch.py`: text patching.
- `http_api.py`: stdlib HTTP client.
- `browser.py`: browser action schema stub.

## Safety Model

The command classifier blocks clearly destructive commands before subprocess
execution. Unknown commands are marked as requiring policy review, while known
test/read/build commands are allowed locally. This is not a full sandbox, but it
is now a concrete safety gate that verifiers and the multi-agent runtime can
build on.

## Remaining Gaps

- OS-level sandboxing and resource isolation.
- Network allowlists and request provenance.
- Real browser automation backend.
- Multi-file unified-diff patch parser.
- Capability-scoped credentials and secrets redaction.
