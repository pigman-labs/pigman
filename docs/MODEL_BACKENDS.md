# Model Backends

## NumPy Backend

The NumPy backend is a reference implementation:

- deterministic
- small
- easy to inspect
- manual backprop
- `.npz` checkpoints

Main files:

```text
neural/jepa_model.py
neural/dynamics_model.py
training/loops/train_neural_jepa.py
```

Use it when debugging architecture logic without GPU or PyTorch.

## PyTorch Backend

The PyTorch backend is the serious training path:

- autograd
- device selection: CPU, CUDA, MPS
- residual MLP blocks
- RMSNorm
- dropout
- action-conditioned JEPA
- EMA target encoder
- MoE feed-forward block
- trainable latent dynamics model with uncertainty/value/risk heads
- `.pt` checkpoints
- JSONL metrics

Main files:

```text
torch_backend/
training/loops/train_torch_jepa.py
training/loops/train_torch_dynamics.py
training/loops/train_joint_world_model.py
```

Commands:

```bash
python -m scripts.train_torch_jepa --steps 200
python -m scripts.train_torch_dynamics --steps 200
python -m scripts.train_joint_world_model --steps 100
```

## Current Boundary

This is now a real trainable research backend, but it is still small-scale. It does not yet include distributed training, real multimodal datasets, large Transformer stacks, or production inference serving.

