from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal


ObservationSource = Literal[
    "user_text",
    "image",
    "video",
    "audio",
    "file",
    "browser",
    "shell",
    "api",
    "robot_sensor",
    "simulator",
]


@dataclass(frozen=True)
class Observation:
    id: str
    timestamp: float
    source: ObservationSource
    raw_ref: str
    metadata: dict = field(default_factory=dict)
    trust_level: float = 1.0
    privacy_level: str = "local"


@dataclass(frozen=True)
class EncodedObservation:
    observation: Observation
    modality: str
    vector: list[float]
    summary: str
    entities: list[dict] = field(default_factory=list)
    confidence: float = 1.0


@dataclass(frozen=True)
class ActionRecord:
    type: str
    payload: dict
    reversible: bool
    risk_score: float
    expected_effects: tuple[str, ...] = ()


@dataclass(frozen=True)
class ExecutionResult:
    action: ActionRecord
    success: bool
    observation: Observation
    stdout: str = ""
    stderr: str = ""
    metadata: dict = field(default_factory=dict)


@dataclass(frozen=True)
class TrajectoryStep:
    before: Observation
    action: ActionRecord
    after: Observation
    reward: float | None = None
    success: bool | None = None
