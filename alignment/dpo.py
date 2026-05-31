from __future__ import annotations

import math

from alignment.preferences import PreferenceExample


def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-x))


class DPOObjective:
    def loss_from_logps(self, chosen_logp: float, rejected_logp: float, ref_chosen_logp: float, ref_rejected_logp: float, beta: float = 0.1) -> float:
        margin = beta * ((chosen_logp - rejected_logp) - (ref_chosen_logp - ref_rejected_logp))
        return -math.log(sigmoid(margin) + 1e-8)

    def score_example(self, example: PreferenceExample) -> dict:
        return {"prompt": example.prompt, "chosen_len": len(example.chosen), "rejected_len": len(example.rejected)}

