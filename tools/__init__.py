"""Tool adapters."""

from tools.browser import BrowserAction, BrowserTool
from tools.executor import ToolExecutor
from tools.filesystem import FilesystemTool
from tools.http_api import HttpApiTool, HttpResult
from tools.patch import PatchTool
from tools.registry import ToolRegistry, ToolSpec
from tools.results import RollbackRecord, ToolResult
from tools.rollback import RollbackManager
from tools.safety import CommandClassification, CommandClassifier
from tools.shell import ShellResult, ShellTool

__all__ = [
    "BrowserAction",
    "BrowserTool",
    "CommandClassification",
    "CommandClassifier",
    "FilesystemTool",
    "HttpApiTool",
    "HttpResult",
    "PatchTool",
    "RollbackManager",
    "RollbackRecord",
    "ShellResult",
    "ShellTool",
    "ToolExecutor",
    "ToolRegistry",
    "ToolResult",
    "ToolSpec",
]
