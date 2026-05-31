from __future__ import annotations

from dataclasses import dataclass, field
from time import time


@dataclass(frozen=True)
class Event:
    name: str
    payload: dict = field(default_factory=dict)
    timestamp: float = field(default_factory=time)

