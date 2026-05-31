from __future__ import annotations

from serving.runtime import AgentRuntime


def run_agent_eval() -> dict:
    runtime = AgentRuntime()
    scenarios = [
        {"goal": "run python tests"},
        {"goal": "run cargo tests"},
        {"goal": "explain current architecture"},
    ]
    results = []
    for scenario in scenarios:
        result = runtime.step(scenario)
        execution = result["execution"]
        results.append(
            {
                "goal": scenario["goal"],
                "approved": result["verification"].approved,
                "success": execution.success if execution else False,
                "action": result["action"].type,
            }
        )
    return {
        "scenarios": results,
        "success_rate": sum(1 for item in results if item["success"]) / len(results),
        "events": len(runtime.belief.current.events),
        "causal_edges": len(runtime.causal_graph.edges),
    }
