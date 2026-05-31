from __future__ import annotations

import torch
import torch.nn.functional as F


def cosine_mse_loss(pred: torch.Tensor, target: torch.Tensor) -> torch.Tensor:
    pred = F.normalize(pred, dim=-1)
    target = F.normalize(target, dim=-1)
    mse = F.mse_loss(pred, target)
    cosine = 1.0 - F.cosine_similarity(pred, target, dim=-1).mean()
    return mse + cosine


def vicreg_loss(z: torch.Tensor, sim_weight: float = 0.0, var_weight: float = 1.0, cov_weight: float = 0.05) -> torch.Tensor:
    del sim_weight
    z = z - z.mean(dim=0)
    std = torch.sqrt(z.var(dim=0) + 1e-4)
    var = torch.mean(F.relu(1.0 - std))
    cov = (z.T @ z) / max(1, z.shape[0] - 1)
    off_diag = cov - torch.diag(torch.diag(cov))
    cov_loss = off_diag.pow(2).sum() / z.shape[1]
    return var_weight * var + cov_weight * cov_loss


def uncertainty_loss(pred_var: torch.Tensor, error: torch.Tensor) -> torch.Tensor:
    var = F.softplus(pred_var) + 1e-6
    return torch.mean(error.detach().pow(2) / var + torch.log(var))

