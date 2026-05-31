# Multi-Agent Runtime

The `multi_agent/` package is the project-level control layer that coordinates the
world model, planner, safety checks, verifiers, tools, memory, and affect engine
through a shared trace.

## What Is Real

- Priority message bus with trace history.
- Typed blackboard implementation with write history while preserving dict-like
  compatibility with the rest of the repo.
- Per-agent budget accounting for step count and cumulative risk.
- Coordinator agent that fans out a task to specialists and merges their outputs.
- Specialist agents for memory, world modeling, planning, safety, verification,
  tool execution, and affect updates.
- Shared-state handoff between agents, so each subsystem can consume concrete
  outputs from earlier specialists.
- Safety gate honored by tool execution, not just recorded as metadata.
- Debate-style ranking and merge protocol for specialist results.
- Repair proposals for verifier-rejected actions.
- JSONL trace logging in `artifacts/runs/multi_agent_trace.jsonl`.
- End-to-end smoke eval through `python -m scripts.eval_multi_agent`.

## Runtime Flow

```text
user goal
  -> coordinator
  -> memory_agent
  -> world_model_agent
  -> planner_agent
  -> safety_governor
  -> verifier_agent
  -> tool_agent
  -> affect_agent
  -> coordinator merge
```

The current implementation is deterministic and local. It does not spawn
independent OS processes or call external LLMs. That is intentional for testable
research iteration: each specialist is a composable Python object with a small
typed message boundary.

## Files

- `messages.py`: message, task, priority, and result dataclasses.
- `bus.py`: priority queue bus with trace history.
- `base.py`: common agent context and tick loop.
- `blackboard.py`: shared-state store with update history.
- `budgets.py`: per-agent execution and risk budgets.
- `specialists.py`: concrete subsystem agents.
- `coordinator.py`: fan-out, aggregation, and vote merge.
- `protocols.py`: ranking and merge policies.
- `repair.py`: verifier rejection repair proposals.
- `trace.py`: JSONL runtime trace recording.
- `runtime.py`: runnable orchestration entry point.

## Near-Term Upgrades

- Replace the shared dictionary with a typed blackboard schema.
- Add async execution and cancellation for long-running specialist calls.
- Add per-agent budgets, retries, and timeout policies.
- Add learned specialist selection instead of always calling every specialist.
- Add richer cross-agent debate rounds where verifier and planner can repair
  rejected actions before tool execution.
