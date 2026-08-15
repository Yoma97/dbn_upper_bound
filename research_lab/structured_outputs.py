from __future__ import annotations

from typing import List, Literal, Optional
from pydantic import BaseModel, Field


TruthLabel = Literal[
    "IDEA",
    "CANDIDATE",
    "PROVED",
    "KNOWN",
    "REFUTED",
]

NoveltyLabel = Literal[
    "NOT_ASSESSED",
    "NOVELTY_UNVERIFIED",
    "KNOWN_OR_SUBSUMED",
    "PLAUSIBLY_NEW",
    "LITERATURE_AUDITED",
]

RelevanceLabel = Literal[
    "REFORMULATION_ONLY",
    "DIAGNOSTIC_TOOL",
    "INTERMEDIATE_LEMMA",
    "FRONTIER_ADVANCE",
    "GENERAL_NEW_TOOL",
]


class SourceDependency(BaseModel):
    label: str
    source: str
    theorem_identifier: Optional[str] = None
    exact_hypotheses_used: List[str] = Field(default_factory=list)
    source_tier: Literal["A", "B", "C", "D", "PROJECT_PROVED", "FINITE_CERTIFICATE"]
    conjectural: bool = False


class ClaimCard(BaseModel):
    title: str
    statement: str
    quantifiers_and_domains: List[str]
    hypotheses: List[str]
    conventions_used: List[str]
    strongest_known_input: List[SourceDependency] = Field(default_factory=list)
    exact_current_obstruction: str
    mechanism: str
    implication_chain: List[str]
    assumption_ledger: List[str]
    dependency_edges: List[str]
    unresolved_gaps: List[str] = Field(default_factory=list)
    edge_cases_checked: List[str] = Field(default_factory=list)
    surviving_false_configurations: List[str] = Field(default_factory=list)
    falsification_tests: List[str]
    proof_plan: List[str]
    non_rh_application_target: Optional[str] = None
    why_not_rh_in_disguise: str
    truth_label: TruthLabel = "CANDIDATE"
    novelty_label: NoveltyLabel = "NOT_ASSESSED"
    relevance_label: RelevanceLabel = "DIAGNOSTIC_TOOL"
    parent_claim_id: Optional[str] = None
    repair_delta_from_parent: Optional[str] = None


class ResearchReport(BaseModel):
    role: str
    summary: str
    claims: List[ClaimCard] = Field(default_factory=list)
    rejected_or_refuted_ideas: List[str] = Field(default_factory=list)
    exact_gaps: List[str] = Field(default_factory=list)
    recommended_next_single_lemma: Optional[str] = None


class AuditFinding(BaseModel):
    claim_title: str
    verdict: Literal["PASS", "FAIL", "REPAIR", "INCONCLUSIVE"]
    exact_reason: str
    failed_dependency_edges: List[str] = Field(default_factory=list)
    hidden_assumptions: List[str] = Field(default_factory=list)
    counterexamples_or_edge_cases: List[str] = Field(default_factory=list)
    convention_issues: List[str] = Field(default_factory=list)


class AuditReport(BaseModel):
    role: str
    findings: List[AuditFinding]
    global_verdict: Literal["PASS", "FAIL", "REPAIR", "INCONCLUSIVE"]
    theorem_promotion_allowed: bool = False
    novelty_promotion_allowed: bool = False
    next_required_action: str
