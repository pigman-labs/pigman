from __future__ import annotations

from serving.runtime import AgentRuntime


def main() -> None:
    runtime = AgentRuntime()
    result = runtime.step({"goal": "run python tests"})
    execution = result["execution"]
    print(
        {
            "action": result["action"].__dict__,
            "tool_call": result["tool_call"].__dict__,
            "approved": result["verification"].approved,
            "issues": result["verification"].issues,
            "success": execution.success if execution else False,
            "stdout": (execution.stdout[:500] if execution else ""),
        }
    )


if __name__ == "__main__":
    main()
