from __future__ import annotations

from decoders.tool_decoder import ToolCall
from verifiers.base import VerificationResult
from verifiers.filesystem import FilesystemWriteVerifier
from verifiers.shell import ShellSafetyVerifier


class ToolVerifier:
    def __init__(self) -> None:
        self.shell = ShellSafetyVerifier()
        self.filesystem = FilesystemWriteVerifier()

    def check(self, call: ToolCall) -> VerificationResult:
        if call.name == "shell":
            command = call.args.get("command")
            if not isinstance(command, list) or not command:
                return VerificationResult.fail(
                    "malformed_shell_command",
                    "shell command must be a non-empty list",
                    repair_hint="provide command as argv list",
                    verifier="tool",
                )
            shell_result = self.shell.check_command([str(item) for item in command])
            if not shell_result.approved:
                return shell_result
        if call.name == "filesystem":
            if "path" not in call.args:
                return VerificationResult.fail(
                    "missing_filesystem_path",
                    "filesystem call requires path",
                    repair_hint="include a path field",
                    verifier="tool",
                )
            return self.filesystem.check_payload(str(call.args["path"]), str(call.args.get("content", "")))
        if call.name == "patch":
            for key in ("path", "old", "new"):
                if key not in call.args:
                    return VerificationResult.fail(
                        "malformed_patch_call",
                        f"patch call requires {key}",
                        repair_hint="include path, old, and new fields",
                        verifier="tool",
                    )
            return self.filesystem.check_path(str(call.args["path"]))
        if call.name == "http":
            url = str(call.args.get("url", ""))
            if not (url.startswith("http://") or url.startswith("https://")):
                return VerificationResult.fail(
                    "invalid_http_url",
                    "http tool requires http:// or https:// URL",
                    repair_hint="provide an absolute HTTP URL",
                    verifier="tool",
                )
        return VerificationResult.pass_("tool")
