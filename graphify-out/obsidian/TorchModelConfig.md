---
source_file: "torch_backend/config.py"
type: "code"
community: "activations_l2_normalize, activations_tanh, activations_tanh_grad"
location: "L7"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/activations_l2_normalize,_activations_tanh,_activations_tanh_grad
---

# TorchModelConfig

## Connections
- [[JointWorldModelReport]] - `uses` [INFERRED]
- [[TorchDynamicsReport]] - `uses` [INFERRED]
- [[TorchEncoder]] - `uses` [INFERRED]
- [[TorchJEPAModel]] - `uses` [INFERRED]
- [[TorchLatentDynamics]] - `uses` [INFERRED]
- [[TorchTrainReport]] - `uses` [INFERRED]
- [[config.py_1]] - `contains` [EXTRACTED]
- [[main()_11]] - `calls` [INFERRED]
- [[test_torch_dynamics_forward_shapes()]] - `calls` [INFERRED]
- [[test_torch_jepa_forward_shapes()]] - `calls` [INFERRED]
- [[test_torch_training_writes_checkpoints()]] - `calls` [INFERRED]
- [[train_dynamics_torch()]] - `calls` [INFERRED]
- [[train_jepa_torch()]] - `calls` [INFERRED]
- [[train_joint_world_model()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/activations_l2_normalize,_activations_tanh,_activations_tanh_grad