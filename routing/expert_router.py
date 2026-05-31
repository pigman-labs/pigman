from __future__ import annotations


class ExpertRouter:
    def __init__(self, experts: list[str], top_k: int = 2) -> None:
        self.experts = experts
        self.top_k = top_k

    def route(self, domain: str) -> list[str]:
        matching = [expert for expert in self.experts if domain in expert]
        return (matching or self.experts)[: self.top_k]

