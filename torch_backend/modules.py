from __future__ import annotations

import torch
from torch import nn
import torch.nn.functional as F


class RMSNorm(nn.Module):
    def __init__(self, dim: int, eps: float = 1e-6) -> None:
        super().__init__()
        self.eps = eps
        self.scale = nn.Parameter(torch.ones(dim))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        rms = x.pow(2).mean(dim=-1, keepdim=True).add(self.eps).sqrt()
        return self.scale * x / rms


class ResidualMLPBlock(nn.Module):
    def __init__(self, dim: int, hidden_dim: int, dropout: float) -> None:
        super().__init__()
        self.norm = RMSNorm(dim)
        self.net = nn.Sequential(
            nn.Linear(dim, hidden_dim),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, dim),
            nn.Dropout(dropout),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return x + self.net(self.norm(x))


class MoEFeedForward(nn.Module):
    def __init__(self, dim: int, hidden_dim: int, experts: int = 4, top_k: int = 2) -> None:
        super().__init__()
        self.experts = nn.ModuleList(
            [
                nn.Sequential(
                    nn.Linear(dim, hidden_dim),
                    nn.GELU(),
                    nn.Linear(hidden_dim, dim),
                )
                for _ in range(experts)
            ]
        )
        self.router = nn.Linear(dim, experts)
        self.top_k = top_k
        self.expert_count = experts

    def forward(self, x: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        logits = self.router(x)
        probs = F.softmax(logits, dim=-1)
        weights, indices = probs.topk(self.top_k, dim=-1)
        weights = weights / weights.sum(dim=-1, keepdim=True).clamp_min(1e-8)

        output = torch.zeros_like(x)
        for slot in range(self.top_k):
            slot_indices = indices[:, slot]
            slot_weights = weights[:, slot].unsqueeze(-1)
            for expert_index, expert in enumerate(self.experts):
                mask = slot_indices == expert_index
                if mask.any():
                    output[mask] += slot_weights[mask] * expert(x[mask])

        load = probs.mean(dim=0)
        load_balance = self.expert_count * torch.sum(load * load)
        return output, load_balance

