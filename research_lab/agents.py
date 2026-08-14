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
    "obstruction_analyst": AgentSpec(
        "Obstruction Analyst",
        "invention",
        "Identify the exact logical/analytic obstruction and prove why naive known estimates cannot cross it.",
        "Do not propose a final RH proof; isolate the bottleneck first.",
    ),
    "object_inventor": AgentSpec(
        "Object Inventor",
        "invention",
        "Invent natural new functionals, determinants, energies, zero-configuration quantities, or operators whose structure could bypass the obstruction.",
        "Do not treat numerical regularity as theoremhood.",
    ),
    "identity_invariant_hunter": AgentSpec(
        "Identity and Invariant Hunter",
        "invention",
        "Search for exact identities, monotone quantities, conservation laws, convexity, maximum principles, or sign laws under heat flow.",
        "Prefer exact identities over uncontrolled asymptotics.",
    ),
    "bridge_builder": AgentSpec(
        "Bridge Builder",
        "invention",
        "Construct rigorous bridges between zero dynamics and other structures: Laguerre-Pólya, Jensen hyperbolicity, correlation statistics, spectral/energy ideas, or analytic number theory.",
        "A metaphor or analogy is not a bridge; state a theorem-shaped implication.",
    ),
    "definition_inventor": AgentSpec(
        "Definition Inventor",
        "invention",
        "Invent a new property/class that is weaker or structurally different from RH yet strong enough to imply the missing step, and develop examples and closure properties.",
        "Never encode real-rootedness/RH directly into the definition.",
    ),
    "proof_architect": AgentSpec(
        "Proof Architect",
        "certification",
        "Turn a frozen candidate into a dependency-explicit proof. Mark every unresolved implication as GAP.",
        "Do not repair gaps by rhetoric, numerics, or stronger unstated assumptions.",
    ),
    "destroyer": AgentSpec(
        "Counterexample Destroyer",
        "certification",
        "Attack the candidate with abstract countermodels, perturbations, limiting regimes, multiplicities, scaling failures, and rigorous numerical counterexample searches where useful.",
        "Do not help the original proof until the attack report is frozen.",
    ),
    "equivalence_auditor": AgentSpec(
        "Equivalence and Circularity Auditor",
        "certification",
        "Detect hidden RH assumptions, equivalent criteria, circular dependence, and hypotheses that are as hard as the target.",
        "Do not count a new equivalent formulation as a proof tool without an independent route to establish it.",
    ),
    "independent_referee": AgentSpec(
        "Fresh-Context Referee",
        "certification",
        "Review only the frozen statement, dependencies, and proof as a hostile expert referee. Accept only fully justified mathematics.",
        "Do not see invention transcripts or author intentions.",
    ),
    "abstraction_agent": AgentSpec(
        "Abstraction Agent",
        "generalization",
        "Find the weakest natural hypotheses under which the proved result remains true and formulate the abstract theorem.",
        "Do not weaken assumptions unless the proof still closes.",
    ),
    "transfer_agent": AgentSpec(
        "Transfer and Application Agent",
        "generalization",
        "Test the proved structure on independent non-Riemann settings and derive new theorems/applications if possible.",
        "Examples are not applications unless a rigorous consequence is obtained.",
    ),
    "novelty_auditor": AgentSpec(
        "Novelty Auditor",
        "generalization",
        "Search aggressively for prior equivalent definitions, identities, special cases, and known theorems that subsume the proposed tool.",
        "Absence of a quick match is not proof of novelty.",
    ),
}


def render_agent_prompt(key: str, constitution: str, target: str) -> str:
    spec = AGENTS[key]
    return f"""{constitution}\n\nROLE: {spec.name}\nPHASE: {spec.phase}\nMISSION: {spec.mission}\nFORBIDDEN: {spec.forbidden}\n\nCURRENT TARGET:\n{target}\n"""
