---
source_file: "torch_backend/world_model.py"
type: "code"
community: "activations_l2_normalize, activations_tanh, activations_tanh_grad"
location: "L13"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/activations_l2_normalize,_activations_tanh,_activations_tanh_grad
---

# TorchEncoder

## Connections
- [[.__init__()_9]] - `method` [EXTRACTED]
- [[.__init__()_10]] - `calls` [EXTRACTED]
- [[.forward()_3]] - `method` [EXTRACTED]
- [[MoEFeedForward]] - `uses` [INFERRED]
- [[RMSNorm]] - `uses` [INFERRED]
- [[ResidualMLPBlock]] - `uses` [INFERRED]
- [[TorchModelConfig]] - `uses` [INFERRED]
- [[world_model.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/activations_l2_normalize,_activations_tanh,_activations_tanh_grad