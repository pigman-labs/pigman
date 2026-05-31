---
source_file: "neural/jepa_model.py"
type: "code"
community: "activations_l2_normalize, activations_tanh, activations_tanh_grad"
location: "L24"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/activations_l2_normalize,_activations_tanh,_activations_tanh_grad
---

# TrainableJEPA

## Connections
- [[.__init__()_38]] - `method` [EXTRACTED]
- [[.__init__()_37]] - `calls` [INFERRED]
- [[._copy_context_to_target()]] - `method` [EXTRACTED]
- [[.ema_target()]] - `method` [EXTRACTED]
- [[.encode_context()]] - `method` [EXTRACTED]
- [[.encode_target()]] - `method` [EXTRACTED]
- [[.load()]] - `method` [EXTRACTED]
- [[.predict()_1]] - `method` [EXTRACTED]
- [[.save()]] - `method` [EXTRACTED]
- [[.step()_3]] - `method` [EXTRACTED]
- [[.train_step()_1]] - `method` [EXTRACTED]
- [[.zero_grad()]] - `method` [EXTRACTED]
- [[Linear]] - `uses` [INFERRED]
- [[NeuralTrainReport]] - `uses` [INFERRED]
- [[NeuralWorldModelAdapter]] - `uses` [INFERRED]
- [[OptimizerConfig]] - `uses` [INFERRED]
- [[Small but real action-conditioned JEPA trained with manual backprop.]] - `rationale_for` [EXTRACTED]
- [[evaluate_checkpoint()]] - `calls` [INFERRED]
- [[jepa_model.py]] - `contains` [EXTRACTED]
- [[train_neural_jepa()]] - `calls` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/activations_l2_normalize,_activations_tanh,_activations_tanh_grad