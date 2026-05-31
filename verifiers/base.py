from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class Severity(str, Enum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


@dataclass(frozen=True)
class VerificationIssue:
    code: str
    message: str
    severity: Severity = Severity.ERROR
    repair_hint: str = ""
    evidence: dict = field(default_factory=dict)


@dataclass(frozen=True)
class VerificationResult:
    approved: bool
    issues: list[str] = field(default_factory=list)
    requires_permission: bool = False
    requires_repair: bool = False
    structured_issues: list[VerificationIssue] = field(default_factory=list)
    verifier: str = ""
    confidence: float = 1.0

    @classmethod
    def pass_(cls, verifier: str = "", confidence: float = 1.0) -> "VerificationResult":
        return cls(True, verifier=verifier, confidence=confidence)

    @classmethod
    def fail(
        cls,
        code: str,
        message: str,
        severity: Severity = Severity.ERROR,
        repair_hint: str = "",
        requires_permission: bool = False,
        requires_repair: bool = True,
        verifier: str = "",
        evidence: dict | None = None,
    ) -> "VerificationResult":
        issue = VerificationIssue(code, message, severity, repair_hint, evidence or {})
        return cls(
            False,
            [message],
            requires_permission,
            requires_repair,
            [issue],
            verifier=verifier,
            confidence=1.0,
        )

    def merge(self, other: "VerificationResult") -> "VerificationResult":
        return VerificationResult(
            approved=self.approved and other.approved,
            issues=[*self.issues, *other.issues],
            requires_permission=self.requires_permission or other.requires_permission,
            requires_repair=self.requires_repair or other.requires_repair,
            structured_issues=[*self.structured_issues, *other.structured_issues],
            verifier="+".join(filter(None, [self.verifier, other.verifier])),
            confidence=min(self.confidence, other.confidence),
        )

    def as_dict(self) -> dict:
        return {
            "approved": self.approved,
            "issues": self.issues,
            "requires_permission": self.requires_permission,
            "requires_repair": self.requires_repair,
            "structured_issues": [
                {
                    "code": issue.code,
                    "message": issue.message,
                    "severity": issue.severity.value,
                    "repair_hint": issue.repair_hint,
                    "evidence": issue.evidence,
                }
                for issue in self.structured_issues
            ],
            "verifier": self.verifier,
            "confidence": self.confidence,
        }
