from __future__ import annotations

import hashlib
from math import sqrt


def l2_norm(values: list[float]) -> float:
    return sqrt(sum(value * value for value in values))


def normalize(values: list[float]) -> list[float]:
    norm = l2_norm(values)
    if norm == 0:
        return values
    return [value / norm for value in values]


def stable_hash_embedding(text: str, dim: int = 64) -> list[float]:
    """Small deterministic embedding fallback for local end-to-end tests."""
    if dim <= 0:
        raise ValueError("dim must be positive")

    buckets = [0.0 for _ in range(dim)]
    tokens = text.lower().split() or [text.lower()]
    for token in tokens:
        digest = hashlib.blake2b(token.encode("utf-8"), digest_size=16).digest()
        index = int.from_bytes(digest[:4], "big") % dim
        sign = 1.0 if digest[4] % 2 == 0 else -1.0
        buckets[index] += sign
    return normalize(buckets)


def cosine_similarity(a: list[float], b: list[float]) -> float:
    if len(a) != len(b):
        raise ValueError("Vectors must have the same length")
    denom = l2_norm(a) * l2_norm(b)
    if denom == 0:
        return 0.0
    return sum(x * y for x, y in zip(a, b, strict=True)) / denom
