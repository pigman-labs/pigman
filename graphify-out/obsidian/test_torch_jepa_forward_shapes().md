---
source_file: "tests/unit/test_torch_backend.py"
type: "code"
community: "activations_l2_normalize, activations_tanh, activations_tanh_grad"
location: "L12"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/activations_l2_normalize,_activations_tanh,_activations_tanh_grad
---

# test_torch_jepa_forward_shapes()

## Connections
- [[.batch()]] - `calls` [INFERRED]
- [[SyntheticWorldDataset]] - `calls` [INFERRED]
- [[TorchJEPAModel]] - `calls` [INFERRED]
- [[TorchModelConfig]] - `calls` [INFERRED]
- [[test_torch_backend.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/activations_l2_normalize,_activations_tanh,_activations_tanh_grad