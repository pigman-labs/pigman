# General Intelligence Roadmap

## Core Point

This repo does not become general intelligence by scaling one small model or one dataset.

To move toward general intelligence, it must become an **open-ended learning system**:

```text
experience
  -> world model update
  -> skill acquisition
  -> self-evaluation
  -> curriculum generation
  -> safer/better action
  -> more experience
```

The system should not only answer questions. It should learn from acting in many environments.

## Target Architecture

```text
many environments
  -> unified experience schema
  -> multimodal perception
  -> latent world model
  -> planner
  -> memory
  -> skill library
  -> language interface
  -> tools/verifiers
  -> curriculum engine
  -> continual learning loop
  -> safety/eval gates
```

The key loop:

```text
observe
  -> infer state
  -> predict possible futures
  -> choose action
  -> execute
  -> verify result
  -> update belief
  -> learn from trace
```

## 1. Many Environments

General intelligence requires breadth.

The agent should train and evaluate across:

```text
code repos
web tasks
games
simulated robotics
math/proof systems
science simulators
documents
spreadsheets
APIs
dialogue/social environments
planning tasks
visual reasoning tasks
tool-use workflows
```

The next repo-level addition should be:

```text
envs/
  code_env
  web_env
  gridworld_env
  math_env
  document_env
  api_env
  game_env
```

Each environment should expose the same interface:

```text
reset()
observe()
available_actions()
step(action)
verify()
score()
```

## 2. Unified Experience Format

Every domain should become the same kind of training trace:

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
```

This matters because the agent must learn cross-domain structure:

```text
state + action -> next_state
goal + state -> useful action
failed prediction -> belief update
successful trajectory -> reusable skill
```

## 3. General World Model

The world model should learn:

```text
what is true now
what entities exist
what actions are possible
what happens next
what matters for the goal
what is hidden or uncertain
which outcomes are risky
```

Training targets:

```text
masked latent prediction
future latent prediction
action-conditioned transition prediction
reward/verifier prediction
uncertainty calibration
entity/relation prediction
skill outcome prediction
```

The world model should not only model text. It should model:

```text
language
code
screens
documents
tables
graphs
tool results
environment states
actions
```

## 4. Language Layer

General intelligence needs language, but language does not need to be the only thinking substrate.

Best near-term design:

```text
LLM or chat decoder:
  understands user intent
  explains results
  asks questions
  writes natural responses

world-model agent:
  tracks state
  predicts outcomes
  plans actions
  uses tools
  verifies results
```

Longer-term design:

```text
latent state + evidence + plan -> trained language decoder -> response
```

Language should be the interface, not the entire cognition engine.

## 5. Skill Library

The system should convert solved tasks into reusable skills.

Process:

```text
solve task
  -> compress trajectory
  -> extract reusable procedure
  -> store skill
  -> retrieve skill later
  -> improve skill with repeated use
```

Skill record:

```text
name
trigger conditions
preconditions
action sequence
expected effects
failure modes
verification method
examples
```

A generally intelligent agent should get better at new tasks because old skills transfer.

## 6. Open-Ended Curriculum

The system needs tasks just beyond its current ability.

Curriculum rule:

```text
too easy -> little learning
too hard -> noise
slightly hard -> growth
```

Curriculum engine should:

```text
measure current ability
generate new tasks
mutate existing tasks
combine skills
increase horizon length
add distractors
add hidden variables
test transfer
```

Examples:

```text
fix one-file bug
  -> fix multi-file bug
  -> fix flaky test
  -> fix bug with unclear error
  -> fix bug requiring API understanding

click simple website
  -> fill form
  -> recover from bad navigation
  -> complete multi-page workflow
```

## 7. Self-Correction Under Uncertainty

The agent must know when it might be wrong.

Runtime behavior:

```text
predict outcome
  -> estimate uncertainty
  -> act if safe
  -> run probe if uncertain
  -> ask user if needed
  -> observe mismatch
  -> update belief
  -> repair plan
  -> remember failure
```

Required components:

```text
uncertainty head
OOD detector
calibration loss
surprise score
failure memory
repair planner
rollback system
```

This is essential for autonomy.

## 8. Continual Learning Without Collapse

Naive online learning will destroy capabilities.

Use a safe learning loop:

```text
new trace
  -> verifier labels outcome
  -> memory stores trace
  -> consolidation extracts facts/procedures
  -> replay buffer updates
  -> adapter fine-tune
  -> regression eval
  -> promote checkpoint only if better
```

Needed mechanisms:

```text
replay buffers
frozen reference models
LoRA/adapters
elastic weight consolidation
eval gates
rollback checkpoints
shadow deployment
memory consolidation
```

Rule:

```text
never learn from production traces without verification and regression tests
```

## 9. Grounded Multimodal Perception

The agent needs perception grounded in real states.

Modalities:

```text
text
code
screenshots
DOM/accessibility trees
video
audio
robot state
documents
tables
graphs
tool outputs
```

Representation target:

```text
all modalities -> entity/relation/event/state latent graph
```

Examples:

```text
browser:
  screenshot + DOM + action -> next screenshot/DOM latent

robotics:
  video + proprioception + action -> future state latent

code:
  repo graph + patch -> test/verifier result latent
```

## 10. Safe Autonomous Tool Use

The agent must act through a tool gateway.

Tool gateway requirements:

```text
schema validation
permission classification
sandboxing
timeouts
resource limits
rollback plans
audit logs
provenance
network policy
filesystem policy
```

Risk levels:

```text
read-only:
  auto

local reversible write:
  auto or notify

network/prod/money/delete:
  ask permission

dangerous/illegal:
  block
```

Autonomy should increase only after eval performance proves reliability.

## 11. Deep Scientific, Math, And Code Ability

Do not rely only on neural confidence.

Use external verifiers:

```text
unit tests
typecheckers
linters
SMT solvers
proof assistants
computer algebra systems
simulators
symbolic math
static analyzers
numeric checks
```

For code:

```text
predict failing tests
localize bug
propose patch
run tests
repair
minimize diff
```

For math/science:

```text
generate derivation
verify with symbolic/numeric tools
cite assumptions
check dimensional consistency
simulate where possible
```

## 12. Strong Evaluation Across Unseen Tasks

The system needs evals that measure generalization, not memorization.

Eval tiers:

```text
unit smoke evals
synthetic control evals
held-out task suites
private contamination-resistant evals
long-horizon agent evals
adversarial evals
human-reviewed evals
cross-domain transfer evals
```

Track:

```text
success rate
steps to success
tool cost
recovery rate
hallucination rate
unsafe action rate
calibration
OOD detection
regression rate
transfer learning speed
```

No checkpoint should be promoted without eval gates.

## 13. Reliable Alignment And Safety Behavior

Safety must cover language and actions.

Needed:

```text
policy classifier
risk model
preference model
constitutional/rule checks
red-team dataset
misuse evals
prompt-injection evals
data-exfiltration evals
tool-abuse evals
```

Training:

```text
SFT on safe behavior
DPO/RLAIF on preference pairs
tool-risk prediction
refusal/redirect behavior
safe recovery behavior
```

Safety wrapper:

```text
language output checker
tool action checker
memory privacy checker
network/filesystem policy checker
```

## 14. Large-Scale Compute Infrastructure

Eventually required:

```text
multi-node training
FSDP
DeepSpeed ZeRO
tensor parallelism
pipeline parallelism
expert parallelism
checkpoint sharding
streaming dataset loaders
experiment tracking
GPU inference serving
batching
monitoring
canary deploys
cost tracking
```

But this should be earned with small-scale results.

Do not build expensive infrastructure before the system proves it can learn useful transferable skills.

## Practical Milestones

### Milestone 1: Code Environment

```text
repo state + patch -> test outcome
planner uses predictor to choose patch
beats rule baseline
```

### Milestone 2: Browser Environment

```text
page state + action -> next page state
planner uses world model for form/navigation tasks
beats rule baseline
```

### Milestone 3: Tool-Use Environment

```text
tool trace + goal -> best next tool
predicts failure risk
recovers from bad tool outputs
```

### Milestone 4: Multi-Environment Transfer

```text
same model trains across code + browser + tool tasks
skills transfer between domains
new tasks require fewer examples over time
```

### Milestone 5: Hybrid Chat Agent

```text
language layer handles conversation
world model handles state/action prediction
verifiers ground results
memory persists experience
```

### Milestone 6: Continual Learning

```text
store traces
verify outcomes
consolidate memory
fine-tune adapters
promote only through eval gates
```

## Real AGI Direction

The serious bet is:

```text
AGI-like behavior will not come from chat alone.
It needs language + world modeling + planning + memory + tools + verification + continual learning.
```

This repo should become a testbed for that thesis.

The first real AGI-relevant test:

```text
Can one agent loop learn across multiple environments,
transfer skills,
recover from mistakes,
and improve with experience without forgetting?
```

If yes, the project becomes scientifically interesting.

If no, it remains a useful but narrow agent framework.

