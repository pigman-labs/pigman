from __future__ import annotations

from time import time

from core.ids import event_id
from data.schemas import ActionRecord, ExecutionResult, Observation
from decoders.tool_decoder import ToolCall
from memory.retrieval import MemorySystem
from tools.browser import BrowserAction, BrowserTool
from tools.filesystem import FilesystemTool
from tools.http_api import HttpApiTool
from tools.patch import PatchTool
from tools.registry import ToolRegistry
from tools.shell import ShellTool


class ToolExecutor:
    def __init__(self, memory: MemorySystem | None = None) -> None:
        self.shell = ShellTool()
        self.filesystem = FilesystemTool()
        self.patch = PatchTool()
        self.http = HttpApiTool()
        self.browser = BrowserTool()
        self.registry = ToolRegistry.default()
        self.memory = memory or MemorySystem()

    def execute(self, call: ToolCall, action: ActionRecord) -> ExecutionResult:
        if call.name == "shell":
            structured = self.shell.run_structured(
                [str(item) for item in call.args["command"]],
                timeout=int(call.args.get("timeout", 30)),
            )
            observation = Observation(
                id=event_id("obs"),
                timestamp=time(),
                source="shell",
                raw_ref=str({"command": structured.data["command"], "exit_code": structured.data["returncode"]}),
                metadata=structured.to_metadata(),
            )
            return ExecutionResult(action, structured.ok, observation, structured.stdout, structured.stderr, structured.to_metadata())

        if call.name == "filesystem":
            path = str(call.args["path"])
            content = str(call.args.get("content", ""))
            structured = self.filesystem.write_structured(path, content)
            observation = Observation(
                id=event_id("obs"),
                timestamp=time(),
                source="file",
                raw_ref=path,
                metadata=structured.to_metadata(),
            )
            return ExecutionResult(action, True, observation, metadata=structured.to_metadata())

        if call.name == "patch":
            structured = self.patch.apply_replace_structured(
                str(call.args["path"]),
                str(call.args["old"]),
                str(call.args["new"]),
            )
            observation = Observation(
                id=event_id("obs"),
                timestamp=time(),
                source="file",
                raw_ref=str(call.args["path"]),
                metadata=structured.to_metadata(),
            )
            return ExecutionResult(action, structured.ok, observation, structured.stdout, structured.stderr, structured.to_metadata())

        if call.name == "http":
            body = call.args.get("body")
            if isinstance(body, str):
                body = body.encode("utf-8")
            structured = self.http.request_structured(
                str(call.args["url"]),
                str(call.args.get("method", "GET")),
                body,
                int(call.args.get("timeout", 10)),
            )
            observation = Observation(
                id=event_id("obs"),
                timestamp=time(),
                source="api",
                raw_ref=str(call.args["url"]),
                metadata=structured.to_metadata(),
            )
            return ExecutionResult(action, structured.ok, observation, structured.stdout, structured.stderr, structured.to_metadata())

        if call.name == "browser":
            structured = self.browser.execute_structured(
                BrowserAction(
                    type=str(call.args.get("type", "navigate")),
                    selector=call.args.get("selector"),
                    text=call.args.get("text"),
                    url=call.args.get("url"),
                )
            )
            observation = Observation(
                id=event_id("obs"),
                timestamp=time(),
                source="browser",
                raw_ref=str(structured.data),
                metadata=structured.to_metadata(),
            )
            return ExecutionResult(action, structured.ok, observation, structured.stdout, structured.stderr, structured.to_metadata())

        if call.name == "memory":
            query = str(call.args.get("query", ""))
            bundle = self.memory.retrieve(query)
            observation = Observation(
                id=event_id("obs"),
                timestamp=time(),
                source="api",
                raw_ref=str(bundle),
                metadata={"memory_hits": len(bundle.vector_hits)},
            )
            return ExecutionResult(action, True, observation, stdout=str(bundle))

        if call.name == "text":
            text = str(call.args.get("text", ""))
            observation = Observation(
                id=event_id("obs"),
                timestamp=time(),
                source="user_text",
                raw_ref=text,
                metadata={"emitted": True},
            )
            return ExecutionResult(action, True, observation, stdout=text)

        observation = Observation(
            id=event_id("obs"),
            timestamp=time(),
            source="simulator",
            raw_ref=f"noop:{call.name}",
        )
        return ExecutionResult(action, True, observation, stdout=f"noop:{call.name}")
