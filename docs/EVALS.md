# Evaluation Suite

Current eval groups:

```text
world_model:
  verifies the prediction path runs

agent:
  runs end-to-end tool-use scenarios

neural:
  evaluates saved NumPy JEPA checkpoints

planner:
  compares MPC, beam, MCTS, and CEM on synthetic control

memory:
  tests JSONL episodic and SQLite semantic persistence

tools:
  tests filesystem diff/patch-style utilities

verifiers:
  tests shell safety classification
```

Run:

```bash
python -m scripts.eval_agent
python -m scripts.eval_multi_agent

Memory retrieval and consolidation are included in:

```bash
python -m scripts.eval_agent
```

Tool execution coverage includes shell safety classification, patch rollback,
filesystem rollback metadata, and executor routing through `run_tool_eval`.

Verifier coverage includes shell safety, ensemble rejection, structured issue
generation, and repair hints through `run_verifier_eval`.
```

Outputs:

```text
artifacts/evals/latest.json
```

The current evals are smoke/regression evals, not frontier benchmarks. The next step is adding real task suites with baselines and ablations.
