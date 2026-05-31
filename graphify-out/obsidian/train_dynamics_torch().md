---
source_file: "training/loops/train_torch_dynamics.py"
type: "code"
community: "activations_l2_normalize, activations_tanh, activations_tanh_grad"
location: "L25"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/activations_l2_normalize,_activations_tanh,_activations_tanh_grad
---

# train_dynamics_torch()

## Connections
- [[.backward()]] - `calls` [INFERRED]
- [[.save()]] - `calls` [INFERRED]
- [[.state_dict()]] - `calls` [INFERRED]
- [[.step()_4]] - `calls` [INFERRED]
- [[.write()]] - `calls` [INFERRED]
- [[.zero_grad()_1]] - `calls` [INFERRED]
- [[TorchDynamicsReport]] - `calls` [EXTRACTED]
- [[TorchLatentDynamics]] - `calls` [INFERRED]
- [[TorchModelConfig]] - `calls` [INFERRED]
- [[TorchTrainConfig]] - `calls` [INFERRED]
- [[main()_9]] - `calls` [INFERRED]
- [[normalize()]] - `calls` [INFERRED]
- [[seed_everything()]] - `calls` [INFERRED]
- [[select_device()]] - `calls` [INFERRED]
- [[sigmoid()]] - `calls` [INFERRED]
- [[tanh()]] - `calls` [INFERRED]
- [[test_torch_training_writes_checkpoints()]] - `calls` [INFERRED]
- [[train_joint_world_model()]] - `calls` [INFERRED]
- [[train_torch_dynamics.py]] - `contains` [EXTRACTED]
- [[uncertainty_loss()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/activations_l2_normalize,_activations_tanh,_activations_tanh_grad