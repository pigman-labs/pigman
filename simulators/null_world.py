from __future__ import annotations


class NullWorld:
    def step(self, action: dict) -> dict:
        return {"observation": {"echo": action}, "done": False}

