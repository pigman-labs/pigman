# Master Plan

## Purpose

This document is the single source of truth for the project.

The repo has grown across several directions:

```text
JEPA/world models
PyTorch/NumPy neural backends
tool-using agents
memory
planners
verifiers
frontier-style dataset/training/eval scaffolds
MANU affect/intrinsic motivation
general-intelligence roadmap
multi-agent network
chat interface
```

The purpose of this plan is to make the project coherent again.

## North Star

Build a research-grade, open-ended, multi-agent world-model system.

The target architecture:

```text
chat/language interface
  -> coordinator agent
  -> specialist agent network
  -> shared world model
  -> planners
  -> tools
  -> verifiers
  -> memory
  -> affect/intrinsic motivation
  -> curriculum engine
  -> continual learning
  -> eval/safety gates
```

The core loop:

```text
observe
  -> encode state
  -> predict outcomes
  -> update affect/intrinsic reward
  -> plan
  -> verify
  -> act
  -> observe result
  -> update memory
  -> learn from trace
  -> generate harder tasks
```

## What This Is

This project is:

```text
a research platform for agentic world-model intelligence
```

It is not:

```text
a ChatGPT clone
a finished AGI
a production AI assistant
a frontier foundation model
```

The serious thesis:

```text
General intelligence needs more than chat.
It needs language + world modeling + planning + memory + tools + verification + intrinsic motivation + continual learning.
```

## System Layers

### 1. Language / Chat Interface

Purpose:

```text
turn user language into structured goals
turn evidence/plans/results into natural responses
ask clarifying questions
```

Near-term:

```text
use external LLM or simple templates
```

Long-term:

```text
train latent-state-to-text decoder
```

Important doc:

```text
docs/CHAT_AND_FRONTIER_GAPS.md
```

### 2. Multi-Agent Network

Purpose:

```text
divide cognition into specialized roles
```

Agents:

```text
CoordinatorAgent
WorldModelAgent
PlannerAgent
CodeAgent
BrowserAgent
ToolAgent
MemoryAgent
VerifierAgent
CurriculumAgent
ResearchAgent
SafetyGovernor
AffectAgent
```

First implementation should be in-process:

```text
multi_agent/
  messages.py
  bus.py
  base.py
  coordinator.py
  world_model_agent.py
  planner_agent.py
  code_agent.py
  verifier_agent.py
  memory_agent.py
  safety_governor.py
```

Do not start with distributed microservices. Start with a local message bus.

### 3. World Model

Purpose:

```text
predict hidden/future state
predict action outcomes
estimate uncertainty
support planning rollouts
```

Current components:

```text
neural/
torch_backend/
world_model/
dynamics/
jepa/
```

Training targets:

```text
state + action -> next_state
state + goal -> useful action
patch + repo state -> test result
browser state + action -> next page state
tool trace + goal -> next tool/result
```

### 4. Planning

Purpose:

```text
choose action sequences using world-model rollouts and verifier feedback
```

Planner types:

```text
MPC
beam search
MCTS
CEM
hierarchical planning
rule baseline
learned planner
```

Current components:

```text
planner/
```

Planner rule:

```text
plan several steps, execute one or few, observe, replan
```

### 5. Tools

Purpose:

```text
let agents act in the world
```

Tools:

```text
filesystem
shell
HTTP/API
browser stub
patch tool
future database tool
future real browser tool
future simulator tool
```

Current components:

```text
tools/
tool_sandbox_rs/
```

Rule:

```text
every tool call must be schema-validated, logged, risk-classified, timeout-bounded, and verifier-compatible
```

### 6. Verifiers

Purpose:

```text
ground model beliefs in reality
```

Verifiers:

```text
Python compile
pytest
cargo test
shell safety
filesystem write safety
source/provenance
world-state consistency
frontier safety cases
future proof checkers
future SMT solvers
future browser state validators
```

Current components:

```text
verifiers/
safety_frontier/
```

Rule:

```text
neural confidence is not enough
```

### 7. Memory

Purpose:

```text
make experience reusable
```

Memory types:

```text
working memory
episodic memory
semantic memory
procedural memory
vector memory
graph memory
affect-weighted salient memory
```

Current components:

```text
memory/
memory_store_rs/
storage/
```

Memory record should include:

```text
state
goal
action
prediction
actual outcome
verifier result
affect state
surprise
curiosity
trust update
skill extraction
```

### 8. MANU Affect / Intrinsic Motivation

Purpose:

```text
drive exploration, salience, curriculum, risk sensitivity, and strategy switching
```

MANU vector:

```text
H  happiness
C  curiosity
G  greed
F  fear
A  anger / goal blockage pressure
Tr trust
Bo boredom
Su surprise
Lo bond / long-term preference association
Fr frustration
```

Important framing:

```text
computational affect, not literal consciousness
```

Proposed components:

```text
affect/
  state.py
  dynamics.py
  intrinsic_reward.py
  trust.py
  salience.py
  curriculum.py
```

Important doc:

```text
docs/MANU_INTEGRATION.md
```

### 9. Dataset Engine

Purpose:

```text
turn real experience and public datasets into training traces
```

Current components:

```text
dataset_engine/
```

Dataset targets:

```text
WebWorldData
Mind2Web
SWE-bench / SWE-smith
TOUCAN
Open X-Embodiment
D2E
code repos
tool traces
browser traces
generated curricula
```

Trace schema:

```text
observation
state
goal
action
next_observation
reward
verifier_result
uncertainty
memory_update
affect_state
```

### 10. Training Infrastructure

Purpose:

```text
train models from traces
```

Current components:

```text
training/
torch_backend/
distributed/
```

Backends:

```text
NumPy reference backend
PyTorch real backend
future distributed backend
```

Training loops:

```text
train_neural_jepa
train_torch_jepa
train_torch_dynamics
train_joint_world_model
future train_policy
future train_value_risk
future train_affect
future train_text_decoder
```

### 11. Alignment / Preference Learning

Purpose:

```text
make behavior safer and more preference-aligned
```

Current components:

```text
alignment/
```

Near-term:

```text
preference buffer
DPO-style objective helper
safe vs unsafe action preference pairs
tool-use preference pairs
```

Long-term:

```text
RLAIF
human feedback
reward model
policy optimization
red-team feedback
```

### 12. Serving / Runtime

Purpose:

```text
make the system usable
```

Current components:

```text
serving/
serving_api/
orchestration/
scripts/
```

Near-term surfaces:

```text
CLI
local HTTP API
GitHub bot later
browser tool later
```

Runtime must support:

```text
trace IDs
timeouts
retries
rollback hooks
telemetry
session save/load
safety gates
```

### 13. Evals

Purpose:

```text
measure whether capability improves
```

Current components:

```text
evals/
benchmarks/
safety_frontier/
tests/
```

Eval categories:

```text
world model prediction
planner synthetic control
tool-use
memory retrieval
verifier safety
agent end-to-end
frontier safety smoke
future code repair
future browser workflows
future multi-environment transfer
```

Rule:

```text
no model/checkpoint promotion without eval gates
```

## Repo Organization Target

Keep root-level packages.

Do not move everything into `src/`.

Current / planned top-level modules:

```text
affect/
alignment/
benchmarks/
causal/
configs/
core/
data/
dataset_engine/
decoders/
distributed/
docs/
dynamics/
encoders/
envs/
evals/
interfaces/
jepa/
kernels/
memory/
multi_agent/
multimodal_stack/
neural/
orchestration/
planner/
policies/
routing/
safety_frontier/
security/
serving/
serving_api/
simulators/
state/
storage/
telemetry/
tools/
torch_backend/
training/
verifiers/
world_model/
```

Rust crates:

```text
runtime_rs/
jepa_kernels_rs/
memory_store_rs/
tool_sandbox_rs/
```

## Build Order

### Phase 0: Stabilize

Goal:

```text
make the repo coherent and consistently runnable
```

Tasks:

```text
keep README current
keep MASTER_PLAN current
run pytest/cargo test after changes
remove or ignore generated clutter
```

Done when:

```text
python -m pytest passes
python -m scripts.verify_all passes
cargo test passes
cargo build --workspace passes
```

### Phase 1: Multi-Agent Skeleton

Goal:

```text
add in-process agent network
```

Build:

```text
multi_agent/messages.py
multi_agent/bus.py
multi_agent/base.py
multi_agent/coordinator.py
multi_agent/world_model_agent.py
multi_agent/verifier_agent.py
multi_agent/memory_agent.py
multi_agent/safety_governor.py
```

Success:

```text
one user goal routes through coordinator -> specialist -> verifier -> memory
```

### Phase 2: Affect Engine

Goal:

```text
make MANU affect executable
```

Build:

```text
affect/state.py
affect/dynamics.py
affect/intrinsic_reward.py
affect/curriculum.py
```

Success:

```text
prediction error updates surprise
repeated failure updates frustration
risk updates fear
intrinsic reward modifies planner score
```

Status:

```text
implemented deterministic affect engine
integrated AgentRuntime trajectory logging
added affect eval and tests
remaining: feed affect score directly into planner candidate ranking
```

### Phase 3: Environment Gym

Goal:

```text
train/evaluate across multiple domains with one schema
```

Build:

```text
envs/base.py
envs/code_env.py
envs/web_env.py
envs/gridworld_env.py
envs/math_env.py
envs/tool_env.py
```

Success:

```text
same agent loop can run at least three environments
```

### Phase 4: Real Code-Repair Wedge

Goal:

```text
prove learned world model improves a real task
```

Build:

```text
SWE-bench-lite ingestion
repo snapshot schema
patch candidate generator
test-result predictor
planner integration
baseline comparison
```

Success:

```text
learned predictor improves patch selection vs baseline
```

### Phase 5: Browser/Tool Transfer

Goal:

```text
test cross-domain transfer
```

Build:

```text
browser trajectory ingestion
tool trace ingestion
shared state/action schema
cross-domain eval
```

Success:

```text
skills or representations transfer between code, web, and tools
```

### Phase 6: Continual Learning

Goal:

```text
learn from experience without forgetting
```

Build:

```text
trace replay buffer
adapter fine-tuning
checkpoint promotion gates
regression eval suite
rollback policy
```

Success:

```text
new traces improve target tasks without regressing old tasks
```

### Phase 7: Chat Product Shell

Goal:

```text
make the system usable through chat
```

Build:

```text
intent parser
response generator
evidence summarizer
clarification question policy
```

Near-term:

```text
external LLM or templates
```

Long-term:

```text
trained text decoder
```

## Success Metrics

Track:

```text
task success rate
steps to success
tool calls per success
wall-clock time
cost
prediction error
uncertainty calibration
unsafe action rate
recovery rate
memory retrieval accuracy
cross-domain transfer
regression rate
continual learning improvement
```

## What To Avoid

Do not do these yet:

```text
do not try to train a frontier foundation model
do not build massive distributed infra before a winning task
do not add random abstractions without tests
do not make anthropomorphic claims about MANU affect
do not let affect bypass safety
do not optimize for chat before world-model utility
do not expand domains before one wedge works
```

## Immediate Next Work

Highest-value next steps:

```text
1. Build multi_agent/ in-process network.
2. Build affect/ deterministic MANU engine.
3. Add envs/ with code, gridworld, and tool environments.
4. Connect affect state into AgentRuntime trajectory logs.
5. Add code-repair dataset schema and patch-success predictor.
6. Add baseline comparison report.
```

## Final Framing

The project should be organized around one question:

```text
Can a world-model agent with memory, tools, verifiers, intrinsic motivation,
and a multi-agent architecture learn transferable skills across environments?
```

Everything should serve that question.
