from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path

import torch
import torch.nn.functional as F

from torch_backend.config import TorchModelConfig, TorchTrainConfig
from torch_backend.device import seed_everything, select_device
from torch_backend.losses import uncertainty_loss
from torch_backend.world_model import TorchLatentDynamics


@dataclass(frozen=True)
class TorchDynamicsReport:
    initial_loss: float
    final_loss: float
    checkpoint: str
    metrics_path: str
    device: str


def train_dynamics_torch(train_cfg: TorchTrainConfig | None = None, model_cfg: TorchModelConfig | None = None) -> TorchDynamicsReport:
    train_cfg = train_cfg or TorchTrainConfig(checkpoint="artifacts/checkpoints/torch_dynamics.pt", metrics_path="artifacts/runs/torch_dynamics_metrics.jsonl")
    model_cfg = model_cfg or TorchModelConfig()
    seed_everything(train_cfg.seed)
    device = select_device(train_cfg.device)
    model = TorchLatentDynamics(model_cfg).to(device)
    optim = torch.optim.AdamW(model.parameters(), lr=train_cfg.lr, weight_decay=train_cfg.weight_decay)

    true_a = torch.randn(model_cfg.action_dim, model_cfg.latent_dim, device=device) * 0.4
    metrics_path = Path(train_cfg.metrics_path)
    metrics_path.parent.mkdir(parents=True, exist_ok=True)
    checkpoint = Path(train_cfg.checkpoint)
    checkpoint.parent.mkdir(parents=True, exist_ok=True)

    initial_loss = None
    final_loss = 0.0
    with metrics_path.open("w", encoding="utf-8") as metrics:
        for step in range(train_cfg.steps):
            state = F.normalize(torch.randn(train_cfg.batch_size, model_cfg.latent_dim, device=device), dim=-1)
            action = torch.randn(train_cfg.batch_size, model_cfg.action_dim, device=device)
            target_next = F.normalize(state + torch.tanh(action @ true_a) * 0.1, dim=-1)
            value_target = target_next.mean(dim=-1)
            risk_target = action.pow(2).mean(dim=-1).clamp(0, 1)

            output = model(state, action)
            state_loss = F.mse_loss(F.normalize(output["next_state"], dim=-1), target_next)
            value_loss = F.mse_loss(output["value"], value_target)
            risk_loss = F.mse_loss(torch.sigmoid(output["risk"]), risk_target)
            unc_loss = uncertainty_loss(output["uncertainty"], output["next_state"] - target_next)
            loss = state_loss + 0.2 * value_loss + 0.2 * risk_loss + 0.01 * unc_loss

            optim.zero_grad(set_to_none=True)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), train_cfg.grad_clip)
            optim.step()

            final_loss = float(loss.detach().cpu())
            if initial_loss is None:
                initial_loss = final_loss
            if step % train_cfg.log_every == 0 or step == train_cfg.steps - 1:
                metrics.write(json.dumps({"step": step, "loss": final_loss, "state_loss": float(state_loss.detach().cpu())}) + "\n")

    torch.save({"model": model.state_dict(), "model_cfg": asdict(model_cfg), "train_cfg": asdict(train_cfg)}, checkpoint)
    return TorchDynamicsReport(initial_loss or final_loss, final_loss, str(checkpoint), str(metrics_path), str(device))

