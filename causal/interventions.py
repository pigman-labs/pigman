from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Intervention:
    variable: str
    value: object
    expected_effect: str

