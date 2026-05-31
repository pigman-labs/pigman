from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PreferenceExample:
    prompt: str
    chosen: str
    rejected: str
    source: str = "synthetic"


class PreferenceBuffer:
    def __init__(self) -> None:
        self.examples: list[PreferenceExample] = []

    def add(self, example: PreferenceExample) -> None:
        self.examples.append(example)

    def synthetic_from_scores(self, prompt: str, candidates: list[tuple[str, float]]) -> PreferenceExample:
        ranked = sorted(candidates, key=lambda item: item[1], reverse=True)
        example = PreferenceExample(prompt=prompt, chosen=ranked[0][0], rejected=ranked[-1][0])
        self.add(example)
        return example

