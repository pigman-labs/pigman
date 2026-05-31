---
source_file: "torch_backend/world_model.py"
type: "code"
community: "activations_l2_normalize, activations_tanh, activations_tanh_grad"
location: "L63"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/activations_l2_normalize,_activations_tanh,_activations_tanh_grad
---

# TorchLatentDynamics

## Connections
- [[.__init__()_11]] - `method` [EXTRACTED]
- [[.forward()_5]] - `method` [EXTRACTED]
- [[MoEFeedForward]] - `uses` [INFERRED]
- [[RMSNorm]] - `uses` [INFERRED]
- [[ResidualMLPBlock]] - `uses` [INFERRED]
- [[TorchDynamicsReport]] - `uses` [INFERRED]
- [[TorchModelConfig]] - `uses` [INFERRED]
- [[test_torch_dynamics_forward_shapes()]] - `calls` [INFERRED]
- [[train_dynamics_torch()]] - `calls` [INFERRED]
- [[world_model.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/activations_l2_normalize,_activations_tanh,_activations_tanh_grad