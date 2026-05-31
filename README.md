# JEPA World Agent

Research-grade scaffold for a JEPA-first world-model agent.

This repo intentionally keeps all packages at the repository root instead of using a `src/` layout.

## Architecture

See [JEPA_WORLD_MODEL_ARCHITECTURE.md](JEPA_WORLD_MODEL_ARCHITECTURE.md) for the full blueprint.

## Layout

```text
core/        shared types, config, registry, checkpoint helpers
data/        dataset schemas, trajectory records, collators
encoders/    modality encoders and cross-modal fusion
jepa/        context/target encoders, predictor, masking, losses
dynamics/    latent state, transitions, rollout, uncertainty
memory/      working, episodic, semantic, procedural, graph/vector memory
planner/     MPC, MCTS, beam, value/risk models
policies/    action policies for tools, code, browser, robots
decoders/    text, code, tool, browser, robot decoders
verifiers/   syntax, code, math, tool, safety, world-state verification
tools/       shell, filesystem, browser, API, simulator adapters
training/    loops, objectives, optimizers, distributed helpers
serving/     runtime, session, model/planner/memory servers
evals/       world-model, coding, browser, safety, calibration evals
state/       canonical action, belief, and goal schemas
world_model/ JEPA + dynamics composition
causal/      causal graphs and interventions
routing/     expert/tool/planner routing
orchestration/ top-level agent loops
interfaces/  Python/Rust/tool message schemas
simulators/  cheap rollout environments
storage/     trajectory logs and persistence adapters
telemetry/   tracing and metrics
security/    policy classification and permission gates
kernels/     Python fallbacks for hot kernels
runtime_rs/  Rust runtime crate
jepa_kernels_rs/ Rust math/kernel crate
memory_store_rs/ Rust memory service crate
tool_sandbox_rs/ Rust sandbox policy crate
configs/     YAML configuration files
scripts/     executable entrypoints
tests/       unit/integration/smoke tests
```

## Quick Start

```bash
env UV_CACHE_DIR=.uv-cache uv python install 3.12
env UV_CACHE_DIR=.uv-cache uv venv .venv-torch --python 3.12
env UV_CACHE_DIR=.uv-cache uv pip install --python .venv-torch/bin/python -e '.[dev]'
source .venv-torch/bin/activate
python -m scripts.serve_agent
python -m scripts.eval_agent
python -m scripts.eval_affect
python -m scripts.eval_multi_agent
python -m scripts.run_goal run python tests
python -m scripts.train_smoke
python -m scripts.train_neural --steps 250
python -m scripts.train_torch_jepa --steps 200
python -m scripts.train_torch_dynamics --steps 200
python -m scripts.train_joint_world_model --steps 100
python -m scripts.build_dataset
python -m scripts.verify_all
python benchmarks/agent_benchmark.py
cargo test
```

This is a scaffold, not a trained model release.

## Current End-to-End Slice

The repo now has a local executable agent loop:

```text
goal/text observation
  -> encoder registry
  -> deterministic latent embedding
  -> cross-modal fusion
  -> belief update
  -> memory retrieval
  -> JEPA/dynamics prediction
  -> planner router
  -> action policy
  -> decoder
  -> verifier ensemble
  -> tool executor
  -> causal graph update
  -> trajectory log
```

The NumPy backend remains deterministic and inspectable. The PyTorch backend is now the main trainable path.

## Trainable Neural Core

The repo includes a real NumPy JEPA training path:

```bash
python -m scripts.train_neural --steps 250
```

This trains an action-conditioned JEPA on a deterministic synthetic world and writes:

```text
artifacts/checkpoints/neural_jepa.npz
```

It is small, but it has actual weights, forward passes, manual backprop, EMA target encoder updates, checkpoint save/load, and evaluation.

## PyTorch Backend

The PyTorch backend adds:

```text
device selection: CPU/CUDA/MPS
autograd training
gradient clipping
checkpoint save/load
JSONL metrics
RMSNorm
residual MLP blocks
dropout
action-conditioned JEPA
EMA target encoder
MoE feed-forward layer
latent dynamics with uncertainty/value/risk heads
```

Docs:

```text
docs/MODEL_BACKENDS.md
docs/EVALS.md
docs/ROADMAP.md
docs/CHAT_AND_FRONTIER_GAPS.md
docs/GENERAL_INTELLIGENCE_ROADMAP.md
docs/MANU_INTEGRATION.md
docs/MASTER_PLAN.md
```

## Frontier Subsystems Added

These are local runnable versions of the frontier-lab categories:

```text
dataset_engine/    dataset manifests, quality scoring, dedup, JSONL streaming
distributed/       DDP/FSDP/ZeRO-style launch planning abstractions
multimodal_stack/  tiny Transformer + SSM multimodal fusion stack
alignment/         preference buffer and DPO-style objective helper
serving_api/       local HTTP serving wrapper around AgentRuntime
safety_frontier/   frontier-style safety case suite
affect/            MANU-style affect, intrinsic reward, salience, curriculum
multi_agent/       Coordinator, specialist agents, message bus, safety handoff
memory/            Episodic, semantic, procedural, vector, graph memory
tools/             Structured shell/filesystem/http/browser/patch execution
verifiers/         Structured safety, policy, tool, source, and state checks
```

## What Is Still Not Frontier-Scale

This is now a serious runnable research scaffold. It is still not OpenAI/Anthropic-scale: there is no massive data engine, distributed training stack, large multimodal model, RLHF/RLAIF pipeline, production serving layer, or industrial safety/eval operation.
