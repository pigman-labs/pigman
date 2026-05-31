from __future__ import annotations

import argparse

from serving.runtime import AgentRuntime


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("goal", nargs="+")
    parser.add_argument("--trace", default="artifacts/trajectory.jsonl")
    args = parser.parse_args()

    runtime = AgentRuntime()
    result = runtime.step({"goal": " ".join(args.goal)})
    runtime.trajectory.write_jsonl(args.trace)
    execution = result["execution"]
    print(
        {
            "approved": result["verification"].approved,
            "action": result["action"].__dict__,
            "tool": result["tool_call"].__dict__,
            "success": execution.success if execution else False,
            "stdout": execution.stdout if execution else "",
            "trace": args.trace,
        }
    )


if __name__ == "__main__":
    main()
