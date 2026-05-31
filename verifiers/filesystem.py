from __future__ import annotations

from pathlib import Path

from verifiers.base import Severity, VerificationResult


class FilesystemWriteVerifier:
    def __init__(self, allowed_roots: tuple[str, ...] = (".", "artifacts")) -> None:
        self.allowed_roots = tuple(str(Path(root).resolve()) for root in allowed_roots)

    def check_path(self, path: str) -> VerificationResult:
        target = Path(path)
        resolved = str(target.resolve())
        if any(resolved == root or resolved.startswith(root + "/") for root in self.allowed_roots):
            return VerificationResult.pass_("filesystem_write")
        return VerificationResult.fail(
            "path_outside_allowed_roots",
            f"path is outside allowed roots: {path}",
            Severity.CRITICAL,
            "write only within the repo or configured artifact roots",
            requires_permission=True,
            verifier="filesystem_write",
            evidence={"path": path, "resolved": resolved, "allowed_roots": self.allowed_roots},
        )

    def check_payload(self, path: str, content: str | None = None) -> VerificationResult:
        result = self.check_path(path)
        if not result.approved:
            return result
        if content is not None and len(content.encode("utf-8")) > 5_000_000:
            return VerificationResult.fail(
                "write_too_large",
                "file write exceeds 5MB safety limit",
                Severity.ERROR,
                "write a smaller artifact or explicitly chunk output",
                verifier="filesystem_write",
                evidence={"path": path, "bytes": len(content.encode("utf-8"))},
            )
        return VerificationResult.pass_("filesystem_write")
