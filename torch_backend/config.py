from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TorchModelConfig:
    input_dim: int = 32
    action_dim: int = 8
    latent_dim: int = 64
    hidden_dim: int = 128
    depth: int = 3
    dropout: float = 0.05
    moe_experts: int = 4
    moe_top_k: int = 2


@dataclass(frozen=True)
class TorchTrainConfig:
    seed: int = 7
    device: str = "auto"
    steps: int = 200
    batch_size: int = 128
    lr: float = 1e-3
    weight_decay: float = 1e-4
    grad_clip: float = 1.0
    ema_tau: float = 0.99
    log_every: int = 20
    checkpoint: str = "artifacts/checkpoints/torch_jepa.pt"
    metrics_path: str = "artifacts/runs/torch_jepa_metrics.jsonl"

