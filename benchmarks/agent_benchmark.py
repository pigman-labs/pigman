from __future__ import annotations

from time import perf_counter

from serving.runtime import AgentRuntime


def run_benchmark(iterations: int = 5) -> dict:
    runtime = AgentRuntime()
    started = perf_counter()
    successes = 0
    for _ in range(iterations):
        result = runtime.step({"goal": "explain current architecture"})
        execution = result["execution"]
        successes += int(bool(execution and execution.success))
    elapsed = perf_counter() - started
    return {
        "iterations": iterations,
        "successes": successes,
        "seconds": round(elapsed, 6),
        "steps_per_second": round(iterations / elapsed, 3) if elapsed else float("inf"),
    }


if __name__ == "__main__":
    print(run_benchmark())
