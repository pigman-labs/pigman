---
source_file: "torch_backend/world_model.py"
type: "code"
community: "activations_l2_normalize, activations_tanh, activations_tanh_grad"
location: "L26"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/activations_l2_normalize,_activations_tanh,_activations_tanh_grad
---

# TorchJEPAModel

## Connections
- [[.__init__()_10]] - `method` [EXTRACTED]
- [[.forward()_4]] - `method` [EXTRACTED]
- [[MoEFeedForward]] - `uses` [INFERRED]
- [[RMSNorm]] - `uses` [INFERRED]
- [[ResidualMLPBlock]] - `uses` [INFERRED]
- [[TorchModelConfig]] - `uses` [INFERRED]
- [[TorchTrainReport]] - `uses` [INFERRED]
- [[test_torch_jepa_forward_shapes()]] - `calls` [INFERRED]
- [[train_jepa_torch()]] - `calls` [INFERRED]
- [[world_model.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/activations_l2_normalize,_activations_tanh,_activations_tanh_grad