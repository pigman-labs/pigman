from __future__ import annotations

from pathlib import Path
import difflib
from time import time

from tools.results import RollbackRecord, ToolResult


class FilesystemTool:
    def read(self, path: str) -> str:
        return Path(path).read_text(encoding="utf-8", errors="replace")

    def write(self, path: str, content: str) -> None:
        target = Path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")

    def write_structured(self, path: str, content: str) -> ToolResult:
        started = time()
        target = Path(path)
        before = target.read_text(encoding="utf-8", errors="replace") if target.exists() else None
        self.write(path, content)
        ended = time()
        return ToolResult(
            ok=True,
            tool="filesystem",
            operation="write",
            data={"path": path, "bytes": len(content.encode("utf-8"))},
            rollback=RollbackRecord("file_write", path, before=before, after=content),
            started_at=started,
            ended_at=ended,
        )

    def list_files(self, root: str = ".") -> list[str]:
        return sorted(str(path) for path in Path(root).glob("**/*") if path.is_file())

    def read_structured(self, path: str) -> ToolResult:
        started = time()
        content = self.read(path)
        return ToolResult(
            ok=True,
            tool="filesystem",
            operation="read",
            stdout=content,
            data={"path": path, "bytes": len(content.encode("utf-8"))},
            started_at=started,
            ended_at=time(),
        )

    def list_structured(self, root: str = ".") -> ToolResult:
        started = time()
        files = self.list_files(root)
        return ToolResult(
            ok=True,
            tool="filesystem",
            operation="list",
            data={"root": root, "files": files, "count": len(files)},
            started_at=started,
            ended_at=time(),
        )

    def diff_text(self, before: str, after: str, fromfile: str = "before", tofile: str = "after") -> str:
        return "".join(
            difflib.unified_diff(
                before.splitlines(keepends=True),
                after.splitlines(keepends=True),
                fromfile=fromfile,
                tofile=tofile,
            )
        )
