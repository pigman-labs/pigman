from __future__ import annotations

import json

from evals.multi_agent_eval import run_multi_agent_eval


def main() -> None:
    print(json.dumps(run_multi_agent_eval(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
