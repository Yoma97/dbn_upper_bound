from __future__ import annotations

from dataclasses import dataclass, asdict, field
from enum import Enum
from typing import List, Optional
import json
import uuid


class Status(str, Enum):
    """Legacy combined status. Prefer the orthogonal axes below."""
    IDEA = "IDEA"
    CANDIDATE = "CANDIDATE"
    SUPPORTED = "SUPPORTED"
    REFUTED = "REFUTED"
    PROPOSITION = "PROPOSITION"
    THEOREM = "THEOREM"
    NEW_TOOL = "NEW_TOOL"


class TruthStatus(str, Enum):
    IDEA = "IDEA"
    CANDIDATE = "CANDIDATE"
    INTERNALLY_PROVED = "INTERNALLY_PROVED"
    INDEPENDENTLY_RECONSTRUCTED = "INDEPENDENTLY_RECONSTRUCTED"
    REFEREE_VERIFIED = "REFEREE_VERIFIED"
    REFUTED = "REFUTED"


class NoveltyStatus(str, Enum):
    NOT_ASSESSED = "NOT_ASSESSED"
    NOVELTY_UNVERIFIED = "NOVELTY_UNVERIFIED"
    KNOWN_OR_SUBSUMED = "KNOWN_OR_SUBSUMED"
    PLAUSIBLY_NEW = "PLAUSIBLY_NEW"
    LITERATURE_AUDITED = "LITERATURE_AUDITED"


class RelevanceStatus(str, Enum):
    REFORMULATION_ONLY = "REFORMULATION_ONLY"
    DIAGNOSTIC_TOOL = "DIAGNOSTIC_TOOL"
    INTERMEDIATE_LEMMA = "INTERMEDIATE_LEMMA"
    FRONTIER_ADVANCE = "FRONTIER_ADVANCE"
    GENERAL_NEW_TOOL = "GENERAL_NEW_TOOL"


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

    # Hygiene fields: mandatory in serious candidates.
    quantifiers_and_domains: List[str] = field(default_factory=list)
    conventions_used: List[str] = field(default_factory=list)
    assumption_ledger: List[str] = field(default_factory=list)
    dependency_edges: List[str] = field(default_factory=list)
    proof_obligations: List[str] = field(default_factory=list)
    edge_cases_checked: List[str] = field(default_factory=list)
    falsification_tests: List[str] = field(default_factory=list)
    unresolved_gaps: List[str] = field(default_factory=list)
    repair_delta_from_parent: str = ""
    parent_claim_id: str = ""

    # Orthogonal epistemic axes.
    truth_status: TruthStatus = TruthStatus.IDEA
    novelty_status: NoveltyStatus = NoveltyStatus.NOT_ASSESSED
    relevance_status: RelevanceStatus = RelevanceStatus.DIAGNOSTIC_TOOL

    # Legacy compatibility only.
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
        data["truth_status"] = self.truth_status.value
        data["novelty_status"] = self.novelty_status.value
        data["relevance_status"] = self.relevance_status.value
        return json.dumps(data, ensure_ascii=False)

    def has_multiple_open_new_lemmas(self) -> bool:
        return len([g for g in self.unresolved_gaps if g.strip()]) > 1


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
        "independent_proof_reconstruction_1",
        "independent_proof_reconstruction_2",
        "adversarial_referee",
        "circularity_audit",
        "counterexample_attack",
        "dependency_verification",
        "convention_and_normalization_audit",
        "edge_case_audit",
        "zero_gap_check",
    }
    passed = {r.gate for r in results if r.passed}
    failed = {r.gate for r in results if not r.passed}
    return required.issubset(passed) and not (required & failed)


def new_tool_promotion_allowed(
    referee_verified_truth: bool,
    abstract_definition: bool,
    scope_beyond_riemann: bool,
    transfer_value: bool,
    novelty_audit: bool,
) -> bool:
    return all(
        [
            referee_verified_truth,
            abstract_definition,
            scope_beyond_riemann,
            transfer_value,
            novelty_audit,
        ]
    )
