from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path

import torch
import torch.nn.functional as F

from neural.synthetic_data import SyntheticWorldDataset
from torch_backend.config import TorchModelConfig, TorchTrainConfig
from torch_backend.device import seed_everything, select_device
from torch_backend.losses import cosine_mse_loss, vicreg_loss
from torch_backend.world_model import TorchJEPAModel


@dataclass(frozen=True)
class TorchTrainReport:
    initial_loss: float
    final_loss: float
    checkpoint: str
    metrics_path: str
    device: str


def train_jepa_torch(train_cfg: TorchTrainConfig | None = None, model_cfg: TorchModelConfig | None = None) -> TorchTrainReport:
    train_cfg = train_cfg or TorchTrainConfig()
    model_cfg = model_cfg or TorchModelConfig()
    seed_everything(train_cfg.seed)
    device = select_device(train_cfg.device)
    dataset = SyntheticWorldDataset(model_cfg.input_dim, model_cfg.action_dim, seed=train_cfg.seed)
    model = TorchJEPAModel(model_cfg).to(device)
    optim = torch.optim.AdamW(model.parameters(), lr=train_cfg.lr, weight_decay=train_cfg.weight_decay)

    metrics_path = Path(train_cfg.metrics_path)
    metrics_path.parent.mkdir(parents=True, exist_ok=True)
    checkpoint = Path(train_cfg.checkpoint)
    checkpoint.parent.mkdir(parents=True, exist_ok=True)

    initial_loss = None
    final_loss = 0.0
    with metrics_path.open("w", encoding="utf-8") as metrics:
        for step in range(train_cfg.steps):
            batch = dataset.batch(train_cfg.batch_size)
            context = torch.tensor(batch.context, dtype=torch.float32, device=device)
            action = torch.tensor(batch.action, dtype=torch.float32, device=device)
            target = torch.tensor(batch.target, dtype=torch.float32, device=device)

            output = model(context, action, target)
            pred_loss = cosine_mse_loss(output["prediction"], output["target"])
            reg_loss = vicreg_loss(output["context"])
            load_loss = output["moe_load_balance"]
            loss = pred_loss + 0.02 * reg_loss + 0.01 * load_loss

            optim.zero_grad(set_to_none=True)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), train_cfg.grad_clip)
            optim.step()
            model.update_target(train_cfg.ema_tau)

            final_loss = float(loss.detach().cpu())
            if initial_loss is None:
                initial_loss = final_loss
            if step % train_cfg.log_every == 0 or step == train_cfg.steps - 1:
                metrics.write(json.dumps({"step": step, "loss": final_loss, "pred_loss": float(pred_loss.detach().cpu())}) + "\n")

    torch.save({"model": model.state_dict(), "model_cfg": asdict(model_cfg), "train_cfg": asdict(train_cfg)}, checkpoint)
    return TorchTrainReport(initial_loss or final_loss, final_loss, str(checkpoint), str(metrics_path), str(device))

