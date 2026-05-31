# MANU Integration

## Purpose

This document integrates the ideas from `~/projects/manu/README.md` into this repo's JEPA/world-model agent architecture.

MANU's core thesis:

```text
intelligence without affect is brittle
```

This repo's current thesis:

```text
general agents need world modeling + planning + memory + tools + verifiers + continual learning
```

The integration:

```text
MANU affect system
  -> intrinsic motivation
  -> curriculum pressure
  -> exploration policy
  -> memory salience
  -> uncertainty-aware self-correction

JEPA/world model
  -> state prediction
  -> action-conditioned dynamics
  -> surprise/error signals
  -> planning rollouts
  -> verifier-grounded learning
```

Together:

```text
observe
  -> predict
  -> measure surprise / progress / risk / frustration
  -> update affect
  -> shape intrinsic reward
  -> choose action
  -> verify outcome
  -> consolidate memory
  -> generate next curriculum step
```

## High-Level Architecture

```text
Environment
  -> observations
  -> encoders
  -> fused latent state
  -> JEPA/world model prediction
  -> prediction error / uncertainty / verifier result
  -> MANU affect update
  -> intrinsic reward
  -> planner/action policy
  -> tools/verifiers
  -> memory + dataset engine
  -> continual learning
```

MANU should not replace the world model. It should wrap the world model with motivational dynamics.

## MANU State Vector

MANU defines:

```text
Psi(t) = [H, C, G, F, A, Tr, Bo, Su, Lo, Fr]
```

Where:

```text
H  = happiness
C  = curiosity
G  = greed
F  = fear
A  = anger
Tr = trust
Bo = boredom
Su = surprise
Lo = love / bond
Fr = frustration
```

In this repo, this should become:

```text
affect/
  state.py
  dynamics.py
  intrinsic_reward.py
  salience.py
  curriculum.py
  trust.py
```

The affect state should be attached to the agent belief state:

```text
BeliefState:
  latent world state
  hypotheses
  unresolved questions
  affect state
  uncertainty
  memory salience
```

## Mapping MANU To Current Repo

| MANU concept | Current repo subsystem | Integration |
|---|---|---|
| World model surprise | `world_model/`, `torch_backend/` | prediction error updates surprise |
| Curiosity | `training/`, `planner/` | learning-progress reward drives exploration |
| Fear | `verifiers/`, `security/`, `tools/` | risk model suppresses unsafe actions |
| Boredom | `memory/`, `dataset_engine/` | low novelty triggers curriculum generation |
| Trust | `memory/`, `tools/`, `verifiers/` | track reliability of tools, users, sources |
| Frustration | `planner/`, `evals/` | repeated failure triggers strategy change |
| Happiness | `evals/`, `verifiers/` | positive verifier surprises reinforce behavior |
| Anger | `planner/` | goal blockage signal, not literal aggression |
| Greed | `planner/risk_model.py` | immediate reward pressure vs delayed reward |
| Love / bond | `memory/semantic_memory.py` | long-term user/entity affinity and preference |

## Data Flow

```text
1. Agent observes environment.

2. Encoders produce latent observation.

3. World model predicts next latent state.

4. Environment/tool/verifier returns actual next state.

5. System computes:
   prediction_error
   reward_prediction_error
   uncertainty
   novelty
   verifier_success
   risk
   repeated_failure_count
   source/tool reliability

6. MANU affect dynamics update Psi(t).

7. Intrinsic reward is computed from Psi(t).

8. Planner receives:
   extrinsic goal
   intrinsic reward
   risk pressure
   curiosity pressure
   frustration pressure
   trust scores

9. Planner chooses action.

10. Memory stores:
   trace
   affect state
   surprise
   outcome
   reusable skill
```

## Affect Update Signals

### Surprise

Source:

```text
world model prediction error
```

Implementation:

```text
Su(t) = normalized_distance(predicted_latent, observed_latent)
```

Use:

```text
spike curiosity
trigger belief update
mark memory as salient
increase dataset sampling priority
```

### Curiosity

Source:

```text
learning progress
```

Implementation:

```text
C(t) = previous_prediction_loss - current_prediction_loss
```

or:

```text
C(t) = expected_information_gain(action)
```

Use:

```text
choose probes
generate curriculum tasks
prioritize uncertain-but-safe states
```

### Fear

Source:

```text
risk model
safety verifier
tool permission level
uncertainty
irreversibility
```

Implementation:

```text
F(t) = P(threat | state, action) * magnitude * (1 - coping_capacity)
```

Use:

```text
suppress dangerous actions
prefer reversible probes
ask user for permission
increase verifier strength
```

### Boredom

Source:

```text
low novelty
low prediction error
low learning progress
repeated states
```

Implementation:

```text
Bo(t) = 1 - normalized_entropy(recent_state_distribution)
```

Use:

```text
increase exploration
generate harder tasks
switch environments
seek new skills
```

### Frustration

Source:

```text
repeated failed attempts on same goal
```

Implementation:

```text
Fr(t) = attempts * (1 - success_rate) * goal_importance
```

Use:

```text
force strategy change
retrieve alternate skills
ask for help
lower confidence in current plan
```

### Trust

Source:

```text
tool reliability
source reliability
user consistency
verifier accuracy
memory provenance
```

Implementation:

```text
Tr(entity) = competence + benevolence + integrity - risk
```

Use:

```text
weight retrieved memories
choose tools
trust or verify source claims
decide autonomy level
```

### Happiness

Source:

```text
positive reward prediction error
unexpected verifier success
goal progress
```

Use:

```text
reinforce successful strategies
increase trust in skill
increase willingness to continue current path
```

### Greed

Source:

```text
near-term reward opportunity
```

Use carefully:

```text
prefer quick wins when safe
avoid over-optimizing short-term reward
balance with risk and long-horizon value
```

### Anger

In this repo, anger should be treated as:

```text
goal blockage pressure
```

Not:

```text
hostility
aggressive behavior
unsafe escalation
```

Use:

```text
detect blocked goals
increase replanning urgency
trigger obstacle analysis
```

### Love / Bond

In this repo, love/bond should be implemented as:

```text
long-term positive association with user/entity/source
```

Use:

```text
personalization
preference memory
trust calibration
continuity
```

Do not implement this as emotional dependency or manipulative attachment.

## Intrinsic Reward

MANU proposes:

```text
r_int(t) =
  lambda_C  * C(t)
  + lambda_H  * H(t)
  - lambda_F  * F(t)
  - lambda_Bo * Bo(t)
  - lambda_Fr * Fr(t)
  - lambda_A  * A(t)
  + lambda_Su * Su(t) * (1 - F(t))
```

In this repo, that becomes:

```text
intrinsic_reward =
  curiosity_reward
  + verifier_success_reward
  + safe_surprise_reward
  - risk_penalty
  - boredom_penalty
  - repeated_failure_penalty
  - goal_blockage_penalty
```

Planner score:

```text
score(action) =
  extrinsic_goal_value
  + intrinsic_reward
  - risk_penalty
  - uncertainty_penalty
  - tool_cost
```

## Memory Integration

Every stored trace should include:

```text
observation
action
prediction
actual_outcome
verifier_result
affect_state_before
affect_state_after
intrinsic_reward
surprise
curiosity
frustration
trust_updates
```

Memory salience should be increased by:

```text
high surprise
high learning progress
high verifier impact
high emotional delta
repeated failure
major success
```

This makes memory less like a passive log and more like biologically inspired episodic salience.

## Curriculum Integration

MANU's boredom and curiosity should feed a curriculum engine.

Curriculum policy:

```text
if boredom high:
  increase novelty or difficulty

if curiosity high:
  continue local exploration

if fear high:
  reduce risk and use safer probes

if frustration high:
  switch strategy or retrieve help

if happiness/trust high:
  consolidate skill and increase confidence
```

Task generator should mutate tasks by:

```text
increasing horizon length
adding distractors
changing environment
requiring tool composition
introducing hidden variables
requiring memory
requiring transfer from prior skill
```

## Safety Constraints

MANU-style affect must be implemented as control signals, not anthropomorphic claims.

Rules:

```text
do not claim the system literally feels
do not optimize for emotional dependency
do not let anger/fear produce unsafe behavior
do not let love/bond manipulate users
do not let greed override safety
do not allow curiosity to bypass permissions
```

Safety wrapper:

```text
affect can modify planner scores
affect cannot bypass verifiers
affect cannot bypass tool permissions
affect cannot override policy constraints
```

## Proposed Code Layout

```text
affect/
  __init__.py
  state.py
  dynamics.py
  intrinsic_reward.py
  trust.py
  salience.py
  curriculum.py
  policy.py
  engine.py

tests/unit/test_affect.py
```

Implemented now:

```text
affect/state.py
  AffectState
  AffectInputs

affect/dynamics.py
  bounded MANU affect update

affect/intrinsic_reward.py
  intrinsic reward from affect state

affect/trust.py
  entity/tool/source trust ledger

affect/salience.py
  memory salience scoring

affect/curriculum.py
  curriculum decision policy

affect/policy.py
  affect-based action score modulation

affect/engine.py
  integrated affect update result

evals/affect_eval.py
scripts/eval_affect.py
tests/unit/test_affect.py
```

Future runtime integration:

```text
serving/runtime.py
  observe
  encode
  predict
  compute prediction error
  update affect
  compute intrinsic reward
  plan
  execute
  update memory with affect trace
```

Runtime integration is now active:

```text
AgentRuntime.step()
  -> computes affect inputs from prediction/verifier/tool result
  -> updates AffectEngine
  -> stores affect state in belief.global_state["affect"]
  -> stores intrinsic_reward and curriculum decision
  -> records affect_before/after and memory_salience in trajectory log
```

## Implementation Phases

### Phase 1: Deterministic Affect Engine

Add:

```text
AffectState dataclass
AffectInputs dataclass
AffectDynamics.update()
IntrinsicReward.compute()
```

Use simple bounded scalar updates.

### Phase 2: Runtime Hook

Update `AgentRuntime.step()`:

```text
prediction error -> surprise
verifier success -> happiness
tool risk -> fear
repeated failure -> frustration
low novelty -> boredom
```

Store affect state in trajectory logs.

### Phase 3: Planner Scoring

Modify planners to include:

```text
intrinsic reward
risk suppression
curiosity bonus
frustration strategy-switch penalty
trust weighting
```

### Phase 4: Curriculum Engine

Add:

```text
task difficulty estimator
novelty detector
task mutator
skill progression tracker
```

### Phase 5: Learned Affect Model

Train affect dynamics from traces:

```text
state/action/outcome -> affect delta
```

This should remain interpretable and safety-bounded.

## Relationship To General Intelligence Roadmap

MANU supplies the motivational layer for:

```text
open-ended curriculum
self-correction
continual learning
memory salience
exploration
trust calibration
safe autonomy
```

The JEPA/world-model system supplies:

```text
prediction
state tracking
planning
tool grounding
verifier feedback
```

The combination is AGI-relevant because it creates an agent that does not merely respond, but has internal pressure to:

```text
learn what it does not know
avoid unsafe states
remember important events
change strategy after failure
seek manageable novelty
consolidate useful skills
```

## Honest Framing

This is not consciousness.

This is not literal emotion.

This is a computational affect system:

```text
bounded internal control variables
used for motivation, memory salience, exploration, and safety-aware planning
```

That framing is important.

The goal is not to make the system "feel."

The goal is to make it learn and act more robustly by giving it structured internal drives.
