---
source_file: "training/loops/train_torch_jepa.py"
type: "code"
community: "activations_l2_normalize, activations_tanh, activations_tanh_grad"
location: "L26"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/activations_l2_normalize,_activations_tanh,_activations_tanh_grad
---

# train_jepa_torch()

## Connections
- [[.backward()]] - `calls` [INFERRED]
- [[.batch()]] - `calls` [INFERRED]
- [[.save()]] - `calls` [INFERRED]
- [[.state_dict()]] - `calls` [INFERRED]
- [[.step()_4]] - `calls` [INFERRED]
- [[.write()]] - `calls` [INFERRED]
- [[.zero_grad()_1]] - `calls` [INFERRED]
- [[SyntheticWorldDataset]] - `calls` [INFERRED]
- [[TorchJEPAModel]] - `calls` [INFERRED]
- [[TorchModelConfig]] - `calls` [INFERRED]
- [[TorchTrainConfig]] - `calls` [INFERRED]
- [[TorchTrainReport]] - `calls` [EXTRACTED]
- [[cosine_mse_loss()]] - `calls` [INFERRED]
- [[main()_2]] - `calls` [INFERRED]
- [[main()_11]] - `calls` [INFERRED]
- [[seed_everything()]] - `calls` [INFERRED]
- [[select_device()]] - `calls` [INFERRED]
- [[test_torch_training_writes_checkpoints()]] - `calls` [INFERRED]
- [[train_joint_world_model()]] - `calls` [INFERRED]
- [[train_torch_jepa.py]] - `contains` [EXTRACTED]
- [[update_target()]] - `calls` [INFERRED]
- [[vicreg_loss()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/activations_l2_normalize,_activations_tanh,_activations_tanh_grad