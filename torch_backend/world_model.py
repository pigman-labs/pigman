from __future__ import annotations

from copy import deepcopy

import torch
from torch import nn
import torch.nn.functional as F

from torch_backend.config import TorchModelConfig
from torch_backend.modules import MoEFeedForward, RMSNorm, ResidualMLPBlock


class TorchEncoder(nn.Module):
    def __init__(self, input_dim: int, latent_dim: int, hidden_dim: int, depth: int, dropout: float) -> None:
        super().__init__()
        self.input = nn.Linear(input_dim, latent_dim)
        self.blocks = nn.Sequential(
            *[ResidualMLPBlock(latent_dim, hidden_dim, dropout) for _ in range(depth)]
        )
        self.norm = RMSNorm(latent_dim)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return F.normalize(self.norm(self.blocks(self.input(x))), dim=-1)


class TorchJEPAModel(nn.Module):
    def __init__(self, cfg: TorchModelConfig) -> None:
        super().__init__()
        self.cfg = cfg
        self.context_encoder = TorchEncoder(cfg.input_dim, cfg.latent_dim, cfg.hidden_dim, cfg.depth, cfg.dropout)
        self.target_encoder = deepcopy(self.context_encoder)
        for param in self.target_encoder.parameters():
            param.requires_grad_(False)
        self.action = nn.Linear(cfg.action_dim, cfg.latent_dim)
        self.predictor_blocks = nn.ModuleList(
            [ResidualMLPBlock(cfg.latent_dim, cfg.hidden_dim, cfg.dropout) for _ in range(cfg.depth)]
        )
        self.moe = MoEFeedForward(cfg.latent_dim, cfg.hidden_dim, cfg.moe_experts, cfg.moe_top_k)
        self.out = nn.Sequential(RMSNorm(cfg.latent_dim), nn.Linear(cfg.latent_dim, cfg.latent_dim))

    @torch.no_grad()
    def update_target(self, tau: float) -> None:
        for target, source in zip(self.target_encoder.parameters(), self.context_encoder.parameters()):
            target.data.mul_(tau).add_(source.data, alpha=1.0 - tau)

    def forward(self, context: torch.Tensor, action: torch.Tensor, target: torch.Tensor) -> dict[str, torch.Tensor]:
        z_context = self.context_encoder(context)
        with torch.no_grad():
            z_target = self.target_encoder(target)
        hidden = z_context + self.action(action)
        for block in self.predictor_blocks:
            hidden = block(hidden)
        moe_out, load_balance = self.moe(hidden)
        pred = F.normalize(self.out(hidden + moe_out), dim=-1)
        return {
            "prediction": pred,
            "target": z_target,
            "context": z_context,
            "moe_load_balance": load_balance,
        }


class TorchLatentDynamics(nn.Module):
    def __init__(self, cfg: TorchModelConfig) -> None:
        super().__init__()
        dim = cfg.latent_dim + cfg.action_dim
        self.trunk = nn.Sequential(
            nn.Linear(dim, cfg.hidden_dim),
            nn.GELU(),
            ResidualMLPBlock(cfg.hidden_dim, cfg.hidden_dim * 2, cfg.dropout),
            ResidualMLPBlock(cfg.hidden_dim, cfg.hidden_dim * 2, cfg.dropout),
        )
        self.delta = nn.Linear(cfg.hidden_dim, cfg.latent_dim)
        self.uncertainty = nn.Linear(cfg.hidden_dim, cfg.latent_dim)
        self.value = nn.Linear(cfg.hidden_dim, 1)
        self.risk = nn.Linear(cfg.hidden_dim, 1)

    def forward(self, state: torch.Tensor, action: torch.Tensor) -> dict[str, torch.Tensor]:
        hidden = self.trunk(torch.cat([state, action], dim=-1))
        delta = self.delta(hidden)
        return {
            "next_state": state + delta,
            "delta": delta,
            "uncertainty": self.uncertainty(hidden),
            "value": self.value(hidden).squeeze(-1),
            "risk": self.risk(hidden).squeeze(-1),
        }
