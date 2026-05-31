from __future__ import annotations

from hashlib import blake2b
from time import time_ns


def stable_id(prefix: str, payload: str) -> str:
    digest = blake2b(payload.encode("utf-8"), digest_size=8).hexdigest()
    return f"{prefix}_{digest}"


def event_id(prefix: str) -> str:
    return stable_id(prefix, str(time_ns()))
