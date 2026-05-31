from __future__ import annotations

from pathlib import Path

import numpy as np


def save_npz(path: str, **arrays) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    np.savez(target, **arrays)


def load_npz(path: str) -> dict:
    loaded = np.load(path)
    return {key: loaded[key] for key in loaded.files}

