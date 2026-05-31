---
source_file: "tests/unit/test_torch_backend.py"
type: "code"
community: "activations_l2_normalize, activations_tanh, activations_tanh_grad"
location: "L34"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/activations_l2_normalize,_activations_tanh,_activations_tanh_grad
---

# test_torch_training_writes_checkpoints()

## Connections
- [[TorchModelConfig]] - `calls` [INFERRED]
- [[TorchTrainConfig]] - `calls` [INFERRED]
- [[test_torch_backend.py]] - `contains` [EXTRACTED]
- [[train_dynamics_torch()]] - `calls` [INFERRED]
- [[train_jepa_torch()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/activations_l2_normalize,_activations_tanh,_activations_tanh_grad