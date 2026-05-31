from __future__ import annotations


class TextDecoder:
    def decode(self, answer_latent: dict) -> str:
        return str(answer_latent.get("text", answer_latent))

