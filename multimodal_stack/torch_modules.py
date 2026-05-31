from __future__ import annotations

import torch
from torch import nn

from torch_backend.modules import RMSNorm, ResidualMLPBlock


class ModalityAdapter(nn.Module):
    def __init__(self, input_dim: int, latent_dim: int) -> None:
        super().__init__()
        self.proj = nn.Linear(input_dim, latent_dim)
        self.norm = RMSNorm(latent_dim)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.norm(self.proj(x))


class TinySSMBlock(nn.Module):
    def __init__(self, dim: int) -> None:
        super().__init__()
        self.gate = nn.Linear(dim, dim)
        self.mix = nn.Linear(dim, dim)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        state = torch.cumsum(torch.tanh(self.mix(x)), dim=1)
        return x + torch.sigmoid(self.gate(x)) * state / max(1, x.shape[1])


class MultimodalWorldStack(nn.Module):
    def __init__(self, text_dim: int = 32, vision_dim: int = 48, tool_dim: int = 16, latent_dim: int = 64, depth: int = 2) -> None:
        super().__init__()
        self.text = ModalityAdapter(text_dim, latent_dim)
        self.vision = ModalityAdapter(vision_dim, latent_dim)
        self.tool = ModalityAdapter(tool_dim, latent_dim)
        encoder_layer = nn.TransformerEncoderLayer(latent_dim, nhead=4, dim_feedforward=latent_dim * 4, batch_first=True)
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=depth)
        self.ssm = TinySSMBlock(latent_dim)
        self.head = nn.Sequential(ResidualMLPBlock(latent_dim, latent_dim * 2, 0.05), RMSNorm(latent_dim))

    def forward(self, text: torch.Tensor, vision: torch.Tensor, tool: torch.Tensor) -> torch.Tensor:
        tokens = torch.stack([self.text(text), self.vision(vision), self.tool(tool)], dim=1)
        hidden = self.ssm(self.transformer(tokens))
        return self.head(hidden.mean(dim=1))

