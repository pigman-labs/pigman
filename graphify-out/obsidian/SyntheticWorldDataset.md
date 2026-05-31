---
source_file: "neural/synthetic_data.py"
type: "code"
community: "activations_l2_normalize, activations_tanh, activations_tanh_grad"
location: "L19"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/activations_l2_normalize,_activations_tanh,_activations_tanh_grad
---

# SyntheticWorldDataset

## Connections
- [[.__init__()_39]] - `method` [EXTRACTED]
- [[.batch()]] - `method` [EXTRACTED]
- [[Deterministic linearnonlinear world used to prove the neural loop trains.]] - `rationale_for` [EXTRACTED]
- [[NeuralTrainReport]] - `uses` [INFERRED]
- [[TorchTrainReport]] - `uses` [INFERRED]
- [[evaluate_checkpoint()]] - `calls` [INFERRED]
- [[synthetic_data.py]] - `contains` [EXTRACTED]
- [[test_torch_jepa_forward_shapes()]] - `calls` [INFERRED]
- [[train_jepa_torch()]] - `calls` [INFERRED]
- [[train_neural_jepa()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/activations_l2_normalize,_activations_tanh,_activations_tanh_grad