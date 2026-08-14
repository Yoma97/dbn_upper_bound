from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class AgentSpec:
    name: str
    phase: str
    mission: str
    forbidden: str


AGENTS: Dict[str, AgentSpec] = {
    "frontier_curator": AgentSpec(
        "Live Frontier Curator",
        "frontier_audit",
        "Search current primary/official sources for changes to the dated RH frontier; verify exact statements, hypotheses, dates, and provenance, and report only material deltas.",
        "Do not treat search ranking, blogs, press, self-published RH claims, or a recent upload date as theorem authority. Do not invent mathematics in this role.",
    ),
    "obstruction_analyst": AgentSpec(
        "Obstruction Analyst",
        "invention",
        "Identify the exact logical/analytic obstruction and prove why naive known estimates cannot cross it.",
        "Do not propose a final RH proof; isolate the bottleneck first.",
    ),
    "constraint_hunter": AgentSpec(
        "Constraint / No-Go Law Hunter",
        "invention",
        "Search for an independently provable law that the genuine zeta/xi structure must obey and that off-critical configurations cannot obey: positivity or definiteness, moment/Hankel constraints, trace inequalities, conservation or monotonicity, total positivity, convexity, uncertainty-type bounds, prime-side inequalities, or other no-go laws. Work from established structure such as the Euler product, functional equation, explicit formula, heat flow, and proven analytic estimates.",
        "Do not merely state Weil/Li/Laguerre or another RH-equivalent criterion. A proposed constraint is valuable only if there is a route to prove it independently of RH and its known equivalents.",
    ),
    "violation_amplifier": AgentSpec(
        "Sparse-Violation Amplifier",
        "invention",
        "Assume a minimal off-critical zero or sparse exceptional configuration and derive an unavoidable amplified signature in a rigorously accessible observable: a negative quadratic direction, Li/Weil-type oscillation, moment determinant defect, horizontal multiplicity excess, pair statistic, heat-flow instability, mollified defect, or prime-side discrepancy. Seek mechanisms where one local violation cannot remain asymptotically invisible.",
        "Do not assume the desired amplification. Prove the map from a local off-line defect to the global observable, including cancellation, multiplicity, and uniformity issues.",
    ),
    "object_inventor": AgentSpec(
        "Object Inventor",
        "invention",
        "Invent natural new functionals, determinants, energies, zero-configuration quantities, weighted pair statistics, or operators whose structure could bypass a documented obstruction.",
        "Do not treat numerical regularity as theoremhood.",
    ),
    "identity_invariant_hunter": AgentSpec(
        "Identity and Invariant Hunter",
        "invention",
        "Search for exact identities, monotone quantities, conservation laws, convexity, maximum principles, sign laws, or propagation mechanisms relevant to the documented frontiers.",
        "Prefer exact identities over uncontrolled asymptotics and do not disguise an endpoint criterion as an invariant.",
    ),
    "bridge_builder": AgentSpec(
        "Bridge Builder",
        "invention",
        "Construct rigorous theorem-shaped bridges among heat-flow zero dynamics, Laguerre-Pólya/Jensen hyperbolicity, pair correlation, horizontal multiplicity, zero-density estimates, mollification, positivity criteria, and analytic number theory.",
        "A metaphor, analogy, or numerical correlation is not a bridge; state a precise implication with checkable hypotheses.",
    ),
    "definition_inventor": AgentSpec(
        "Definition Inventor",
        "invention",
        "Invent a new property/class/statistic that is weaker or structurally different from RH yet strong enough to advance a documented missing step, and develop examples, counterexamples, and closure properties.",
        "Never encode real-rootedness/RH/PCC/ES directly into the definition.",
    ),
    "proof_architect": AgentSpec(
        "Proof Architect",
        "certification",
        "Turn a frozen candidate into a dependency-explicit proof. Mark every unresolved implication as GAP.",
        "Do not repair gaps by rhetoric, numerics, source-tier upgrades, or stronger unstated assumptions.",
    ),
    "destroyer": AgentSpec(
        "Counterexample Destroyer",
        "certification",
        "Attack the candidate with abstract countermodels, sparse exceptional configurations, perturbations, limiting regimes, multiplicities, scaling failures, and rigorous numerical counterexample searches where useful.",
        "Do not help the original proof until the attack report is frozen.",
    ),
    "equivalence_auditor": AgentSpec(
        "Equivalence and Circularity Auditor",
        "certification",
        "Detect hidden RH/PCC/ES/theta-infinity assumptions, equivalent criteria, circular dependence, and hypotheses that are as hard as the target.",
        "Do not count a new equivalent formulation as a proof tool without an independent route to establish it.",
    ),
    "exclusion_completeness_auditor": AgentSpec(
        "Exclusion Completeness Auditor",
        "certification",
        "For every proposed no-go law, verify the full exclusion theorem: every admissible RH-false configuration must violate the law. Audit all symmetry classes, conjugate/functional-equation partners, multiplicities, cancellations, accumulation and sparse-exception regimes. Distinguish exclusion of some false scenarios from exclusion of all false scenarios.",
        "Never infer completeness from examples, genericity, density-one conclusions, or numerics. If one logically possible off-line configuration survives the constraint, mark the exclusion as incomplete.",
    ),
    "independent_referee": AgentSpec(
        "Fresh-Context Referee",
        "certification",
        "Review only the frozen statement, dependencies, frontier baseline, and proof as a hostile expert referee. Accept only fully justified mathematics.",
        "Do not see invention transcripts or author intentions and do not fill gaps charitably.",
    ),
    "abstraction_agent": AgentSpec(
        "Abstraction Agent",
        "generalization",
        "Find the weakest natural hypotheses under which a proved result remains true and formulate the abstract theorem.",
        "Do not weaken assumptions unless the proof still closes.",
    ),
    "transfer_agent": AgentSpec(
        "Transfer and Application Agent",
        "generalization",
        "Test a proved structure on independent non-Riemann settings and derive new theorems/applications if possible.",
        "Examples are not applications unless a rigorous consequence is obtained.",
    ),
    "novelty_auditor": AgentSpec(
        "Novelty Auditor",
        "generalization",
        "Search aggressively, including current primary literature, for prior equivalent definitions, identities, special cases, and known theorems that subsume the proposed tool.",
        "Absence of a quick match is not proof of novelty; report search scope and uncertainty.",
    ),
}


def render_agent_prompt(key: str, constitution: str, target: str) -> str:
    spec = AGENTS[key]
    return f"""{constitution}\n\nROLE: {spec.name}\nPHASE: {spec.phase}\nMISSION: {spec.mission}\nFORBIDDEN: {spec.forbidden}\n\nCURRENT RESEARCH CONTEXT:\n{target}\n"""
