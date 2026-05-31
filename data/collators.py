from __future__ import annotations

from collections.abc import Sequence
from typing import Any


def identity_collate(items: Sequence[Any]) -> list[Any]:
    return list(items)

