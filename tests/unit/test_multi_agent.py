from __future__ import annotations

from data.schemas import Observation
from multi_agent.base import AgentContext
from multi_agent.blackboard import Blackboard
from multi_agent.budgets import AgentBudget, BudgetManager
from multi_agent.bus import MessageBus
from multi_agent.coordinator import CoordinatorAgent
from multi_agent.messages import AgentResult, Message, MessageType, Priority, TaskSpec
from multi_agent.protocols import DebateProtocol, MergeProtocol
from multi_agent.runtime import MultiAgentRuntime
from multi_agent.specialists import SafetyGovernor, ToolAgent
from state.action import AgentAction
from core.ids import event_id


def _message(recipient: str, priority: Priority = Priority.NORMAL) -> Message:
    return Message(
        sender="test",
        recipient=recipient,
        type=MessageType.TASK,
        payload={"goal": "test"},
        trace_id="trace-test",
        priority=priority,
    )


def test_message_bus_drains_by_priority() -> None:
    bus = MessageBus()
    bus.publish(_message("agent", Priority.LOW))
    bus.publish(_message("agent", Priority.CRITICAL))
    bus.publish(_message("agent", Priority.NORMAL))

    drained = bus.drain("agent")

    assert [message.priority for message in drained] == [
        Priority.CRITICAL,
        Priority.NORMAL,
        Priority.LOW,
    ]
    assert bus.pending("agent") == 0
    assert len(bus.history) == 3


def test_blackboard_tracks_write_history() -> None:
    board = Blackboard()
    board.put("belief", {"x": 1}, actor="world")
    board["belief"] = {"x": 2}

    assert board["belief"] == {"x": 2}
    assert len(board.events("belief")) == 2
    assert board.events("belief")[0].actor == "world"
    assert board.last_writer("belief") == "system"


def test_budget_manager_blocks_exhausted_agent() -> None:
    bus = MessageBus()
    budgets = BudgetManager()
    budgets.set("safety_governor", AgentBudget(max_steps=0))
    context = AgentContext(bus, budgets=budgets)
    bus.publish(_message("safety_governor"))

    result = SafetyGovernor().tick(context)[0]

    assert result.ok is False
    assert "budget exhausted" in result.summary


def test_coordinator_start_publishes_task_to_each_specialist() -> None:
    bus = MessageBus()
    context = AgentContext(bus)
    coordinator = CoordinatorAgent(["world", "planner"])
    obs = Observation(event_id("obs"), 0.0, "user_text", "hello")

    trace_id = coordinator.start(context, TaskSpec(goal="build"), obs)

    assert context.shared_state["observation"] == obs
    assert bus.pending("world") == 1
    assert bus.pending("planner") == 1
    assert all(message.trace_id == trace_id for message in bus.history)


def test_protocols_rank_and_merge_specialist_results() -> None:
    results = [
        AgentResult("planner", True, "good plan", confidence=0.8, risk=0.1),
        AgentResult("verifier", False, "blocked", confidence=0.4, risk=0.7),
    ]

    votes = DebateProtocol().rank(results)
    merged = MergeProtocol().merge(results)

    assert votes[0].agent == "planner"
    assert merged["ok"] is False
    assert merged["risk"] == 0.7
    assert "good plan" in merged["summaries"]


def test_safety_governor_blocks_high_risk_action_and_tool_honors_it() -> None:
    bus = MessageBus()
    context = AgentContext(bus)
    context.shared_state["action"] = AgentAction(
        "run_shell",
        {"command": ["python", "-c", "print('should not run')"]},
        risk_score=0.95,
    )
    context.shared_state["tool_call"] = type(
        "Call",
        (),
        {"name": "shell", "args": {"command": ["python", "-c", "print('should not run')"]}},
    )()

    bus.publish(_message("safety_governor"))
    safety_result = SafetyGovernor().tick(context)[0]
    bus.publish(_message("tool_agent"))
    tool_result = ToolAgent().tick(context)[0]

    assert safety_result.ok is False
    assert context.shared_state["safety_blocked"] is True
    assert tool_result.ok is False
    assert "blocked" in tool_result.summary
    assert "execution" not in context.shared_state


def test_multi_agent_runtime_executes_architecture_goal() -> None:
    result = MultiAgentRuntime().run("architecture digest for multi agent system")

    assert result.ok is True
    assert result.messages >= 8
    assert result.shared_state["execution"].success is True
    assert result.shared_state["verification"].approved is True
    assert result.shared_state["affect"].intrinsic_reward >= 0.0
    assert result.shared_state["coordinator_summary"]["ok"] is True
    assert result.agent_results["world_model_agent"]
    assert result.agent_results["tool_agent"]
