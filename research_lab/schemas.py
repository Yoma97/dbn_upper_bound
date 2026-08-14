from __future__ import annotations

from dataclasses import dataclass, asdict
from enum import Enum
from typing import List, Optional
import json
import uuid


class Status(str, Enum):
    IDEA = "IDEA"
    CANDIDATE = "CANDIDATE"
    SUPPORTED = "SUPPORTED"
    REFUTED = "REFUTED"
    PROPOSITION = "PROPOSITION"
    THEOREM = "THEOREM"
    NEW_TOOL = "NEW_TOOL"


@dataclass
class ResearchClaim:
    title: str
    statement: str
    hypotheses: List[str]
    mechanism: str
    target_connection: str
    proof_plan: List[str]
    known_dependencies: List[str]
    possible_failure_modes: List[str]
    status: Status = Status.IDEA
    claim_id: str = ""
    origin_agent: str = ""
    novelty_notes: str = ""
    proof_text: str = ""
    referee_notes: str = ""
    counterexample_notes: str = ""
    generalization_notes: str = ""

    def __post_init__(self) -> None:
        if not self.claim_id:
            self.claim_id = str(uuid.uuid4())

    def to_json(self) -> str:
        data = asdict(self)
        data["status"] = self.status.value
        return json.dumps(data, ensure_ascii=False)


@dataclass
class GateResult:
    gate: str
    passed: bool
    reason: str
    claim_id: str
    evidence: Optional[str] = None

    def to_json(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False)


def theorem_promotion_allowed(results: List[GateResult]) -> bool:
    required = {
        "independent_proof_reconstruction",
        "adversarial_referee",
        "circularity_audit",
        "counterexample_attack",
        "dependency_verification",
    }
    passed = {r.gate for r in results if r.passed}
    failed = {r.gate for r in results if not r.passed}
    return required.issubset(passed) and not (required & failed)


def new_tool_promotion_allowed(
    theorem_status: bool,
    abstract_definition: bool,
    scope_beyond_riemann: bool,
    transfer_value: bool,
    novelty_audit: bool,
) -> bool:
    return all(
        [
            theorem_status,
            abstract_definition,
            scope_beyond_riemann,
            transfer_value,
            novelty_audit,
        ]
    )
