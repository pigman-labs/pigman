---
source_file: "neural/jepa_model.py"
type: "rationale"
community: "activations_l2_normalize, activations_tanh, activations_tanh_grad"
location: "L25"
tags:
  - graphify/rationale
  - graphify/INFERRED
  - community/activations_l2_normalize,_activations_tanh,_activations_tanh_grad
---

# Small but real action-conditioned JEPA trained with manual backprop.

## Connections
- [[Linear]] - `uses` [INFERRED]
- [[OptimizerConfig]] - `uses` [INFERRED]
- [[TrainableJEPA]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/INFERRED #community/activations_l2_normalize,_activations_tanh,_activations_tanh_grad