from __future__ import annotations

import argparse
import asyncio
import json
import os
from pathlib import Path
from typing import Dict, List

from agents import Agent, RunConfig, Runner, WebSearchTool

from roles import AGENTS, render_agent_prompt


ROOT = Path(__file__).resolve().parent
MEMORY = ROOT / "memory"
CONSTITUTION_PATH = ROOT / "prompts" / "constitution.md"
FRONTIER_PATH = ROOT / "knowledge" / "frontier_map.md"
CONSTRAINT_FRONTIER_PATH = ROOT / "knowledge" / "constraint_frontier.md"
INVENTION_CHARTER_PATH = ROOT / "knowledge" / "mathematical_invention_charter.md"
SOURCE_REGISTRY_PATH = ROOT / "knowledge" / "source_registry.yaml"
DEFAULT_MODEL = os.getenv("OPENAI_DEFAULT_MODEL", "gpt-5.6-sol")

INVENTION_KEYS = [
    "obstruction_analyst",
    "constraint_hunter",
    "violation_amplifier",
    "structural_mutator",
    "object_inventor",
    "identity_invariant_hunter",
    "bridge_builder",
    "definition_inventor",
    "theory_builder",
]

CERTIFICATION_KEYS = [
    "proof_architect",
    "destroyer",
    "equivalence_auditor",
    "mathematical_legitimacy_auditor",
    "exclusion_completeness_auditor",
    "independent_referee",
]

GENERALIZATION_KEYS = [
    "abstraction_agent",
    "transfer_agent",
    "novelty_auditor",
]

WEB_ENABLED_KEYS = {"frontier_curator", "novelty_auditor"}

DEFAULT_TARGET = """
Start from the dated external frontier map, not from any presumed project progress.
The laboratory has TWO simultaneous goals:

A. EXCLUSION-FIRST: find an independently provable law C that the genuine
   zeta/xi structure must satisfy and prove that every RH-false admissible
   configuration violates C.

B. CREATION-FIRST: invent genuinely new mathematical structures, operators,
   transforms, pairings, energies, positivity notions, propagation principles,
   or abstract theories that obey standard mathematical principles and make a
   missing RH-relevant theorem provable. New mathematics should have life beyond
   the Riemann problem whenever possible.

Give highest priority to:

0. complete no-go laws / positive separators with independently provable soundness;
1. sparse-exception amplification/rigidity;
2. new mathematical structures that reveal hidden positivity, self-adjointness,
   monotonicity, exact identities, or first-crossing impossibility;
3. unconditional horizontal-multiplicity or horizontally weighted pair bounds;
4. bridges from current zero-density estimates to horizontal pair information;
5. structural de Bruijn-Newman mechanisms independent of finite-height verification;
6. non-tautological long-mollifier/variational mechanisms;
7. new hyperbolicity/Laguerre propagation mechanisms reaching low-shift/high-degree regimes.

Do not merely improve a numerical constant. Do not restate an RH-equivalent
criterion unless there is a genuinely independent proof mechanism for it. Do not
reward symbolic novelty that is ill-defined, unnatural, overfit to computed zeros,
or incapable of supporting a nontrivial mathematical theorem.
""".strip()


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_constitution() -> str:
    return load_text(CONSTITUTION_PATH)


def build_research_context(target: str, live_delta: str = "") -> str:
    frontier = load_text(FRONTIER_PATH)
    constraint_frontier = load_text(CONSTRAINT_FRONTIER_PATH)
    invention_charter = load_text(INVENTION_CHARTER_PATH)
    registry = load_text(SOURCE_REGISTRY_PATH)
    delta_section = (
        f"\n\nLIVE FRONTIER AUDIT FOR THIS RUN:\n{live_delta}\n"
        if live_delta
        else ""
    )
    return (
        f"USER/ROUND TARGET:\n{target}\n\n"
        f"DATED EXTERNAL FRONTIER MAP:\n{frontier}\n\n"
        f"CONSTRAINT-FIRST / NO-GO FRONTIER:\n{constraint_frontier}\n\n"
        f"MATHEMATICAL INVENTION CHARTER:\n{invention_charter}\n\n"
        f"SOURCE PROVENANCE REGISTRY:\n{registry}"
        f"{delta_section}"
    )


def ensure_memory() -> None:
    MEMORY.mkdir(parents=True, exist_ok=True)
    for name in [
        "frontier_audits",
        "ideas",
        "theory_cards",
        "candidates",
        "theorems",
        "refuted",
        "dead_ends",
        "runs",
    ]:
        path = MEMORY / f"{name}.jsonl"
        if not path.exists():
            path.touch()


def append_jsonl(name: str, payload: Dict) -> None:
    ensure_memory()
    with (MEMORY / f"{name}.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(payload, ensure_ascii=False) + "\n")


def make_agent(key: str, research_context: str, constitution: str) -> Agent:
    spec = AGENTS[key]
    tools = [WebSearchTool(search_context_size="high")] if key in WEB_ENABLED_KEYS else []
    return Agent(
        name=spec.name,
        instructions=render_agent_prompt(key, constitution, research_context),
        model=DEFAULT_MODEL,
        tools=tools,
    )


async def run_one(key: str, task: str, research_context: str, constitution: str) -> Dict:
    agent = make_agent(key, research_context, constitution)
    result = await Runner.run(agent, task, run_config=RunConfig(model=DEFAULT_MODEL))
    return {
        "agent_key": key,
        "agent_name": AGENTS[key].name,
        "phase": AGENTS[key].phase,
        "output": result.final_output,
    }


async def live_frontier_audit(target: str, constitution: str) -> Dict:
    baseline_context = build_research_context(target)
    task = """
Audit the dated frontier against the live literature before invention begins.
Search primarily official sources, journal pages, arXiv full records/text, and
author-maintained research sources. Report only material deltas affecting a
KNOWN claim, limitation, missing theorem, positivity/no-go mechanism, or relevant
new mathematical structure.

For every possible update:
1. give title/authors/date/source;
2. state the exact theorem and hypotheses;
3. classify source tier A/B/C/D using the registry;
4. say CONFIRMS, SUPERSEDES, NARROWS, or DOES NOT CHANGE;
5. distinguish proof, conditional theorem, computation, and claimed proof;
6. never promote extraordinary RH claims without independent validation.

Do not invent mathematics in this stage.
""".strip()
    result = await run_one("frontier_curator", task, baseline_context, constitution)
    append_jsonl("frontier_audits", result)
    return result


async def independent_invention_round(research_context: str, constitution: str) -> List[Dict]:
    common = """
Work independently. Do not assume access to other agents' proposals.

Select one or two exact frontier obstructions. Produce up to four distinct
candidate mechanisms. Work in BOTH research modes where appropriate:

EXCLUSION MODE:
- separate SOUNDNESS from EXCLUSION COMPLETENESS;
- begin violation amplification from the weakest RH-false configuration;
- control cancellation, multiplicity, sparse exceptions, small displacement,
  high height, and all relevant uniformity issues.

CREATION MODE:
- you are explicitly encouraged to invent genuinely new mathematics;
- do not limit yourself to recombining named existing techniques;
- use disciplined structural operations from the Mathematical Invention Charter:
  lifting, dualization, deformation, polarization, localization/globalization,
  renormalization, completion, factorization, interpolation, or obstruction
  classification;
- a genuinely new object must come with a THEORY CARD: formal definition,
  domain/codomain, well-definedness obligations, symmetries/transformation laws,
  examples/non-examples, first exact identity, first nontrivial lemma target,
  relation to known structures, RH mechanism, and a non-RH application target.

Across proposals favor exact identities, new pairings/operators/kernels/measures,
positive representations, invariants, propagation laws, rigidity theorems,
first-crossing obstructions, or new structural statistics over constant tuning.

For every proposal state:
- strongest known input and source tier;
- exact current obstruction;
- precise new statement/object;
- why it is not RH/PCC/ES/theta-infinity/LP/Li/Weil in disguise;
- exact implication chain;
- fastest falsification route;
- surviving false configurations or mathematical edge cases;
- what would make the invention useful outside RH.

Freeze each proposal. Never self-promote to THEOREM.
""".strip()
    results = await asyncio.gather(
        *(run_one(key, common, research_context, constitution) for key in INVENTION_KEYS)
    )
    for item in results:
        append_jsonl("ideas", item)
        if item["agent_key"] in {"structural_mutator", "object_inventor", "definition_inventor", "theory_builder"}:
            append_jsonl("theory_cards", item)
    return results


async def synthesize_candidates(
    research_context: str,
    constitution: str,
    inventions: List[Dict],
) -> Dict:
    transcript = "\n\n".join(f"### {x['agent_name']}\n{x['output']}" for x in inventions)
    task = f"""
You are the synthesis stage. Compare the independently frozen proposals below.
Do not reward agreement, grandiosity, or verbosity. Select at most SIX candidates.

Rank primarily by:
1. complete no-go law with independently provable soundness;
2. sparse/local violation amplified into an unavoidable contradiction;
3. genuinely new mathematical structure with a credible first theorem;
4. exact closure of a documented frontier obstruction;
5. hypotheses genuinely weaker/different from RH-equivalent endpoints;
6. rigorous bridge between established partial theories;
7. falsifiability and proof accessibility;
8. mathematical life beyond RH.

PORTFOLIO RULE: if at least one structurally new candidate passes basic
well-definedness/noncircularity screening, preserve at least one such candidate
in the final portfolio even if a more conservative candidate looks closer to an
immediate RH consequence. The laboratory is optimizing for both RH progress and
new reusable mathematics.

For every structurally new candidate freeze its THEORY CARD and list separate
proof obligations for well-definedness, first structural identity, first
nontrivial theorem, RH relevance, and independent transfer.

For no-go candidates freeze SOUNDNESS and EXCLUSION COMPLETENESS separately.
Reject symbolic novelty that is ill-defined, arbitrary-coordinate dependent,
overfit to finite data, numerically justified, or merely a renamed known
criterion. Reject direct assumptions of PCC/ES, unrestricted theta=infinity,
all-zero narrow boxes, all Jensen hyperbolicities, or bare Li/Weil positivity.

Output explicit dependency graphs.

INDEPENDENT PROPOSALS:
{transcript}
""".strip()
    result = await run_one("proof_architect", task, research_context, constitution)
    append_jsonl("candidates", result)
    return result


async def certification_round(
    research_context: str,
    constitution: str,
    candidate_bundle: Dict,
) -> List[Dict]:
    frozen = candidate_bundle["output"]
    tasks = {
        "proof_architect": (
            "Attempt dependency-explicit proofs from allowed frontier inputs. For "
            "new structures first prove well-definedness and at least one structural "
            "law before using the object for RH. For no-go routes prove SOUNDNESS and "
            "EXCLUSION COMPLETENESS separately. Mark every missing implication GAP."
        ),
        "destroyer": (
            "Attack every candidate with abstract countermodels, perturbations, edge "
            "cases, sparse exceptions, multiplicity, cancellation, scaling, singular "
            "limits, and rigorous numerical falsification where useful. Numerics may "
            "refute but never certify an infinite theorem."
        ),
        "equivalence_auditor": (
            "Audit for hidden RH/PCC/ES/theta-infinity dependence, disguised Li/Weil/"
            "Laguerre endpoints, circular definitions, and hypotheses as hard as the "
            "target. Trace dependencies to the registry."
        ),
        "mathematical_legitimacy_auditor": (
            "Audit every invented object/theory using the Mathematical Invention "
            "Charter: well-definedness, convergence, domains, choice-independence, "
            "symmetry, naturality, scaling, limits, existence, nontriviality, known-case "
            "recovery, operator/measure legitimacy, and RH-specific overfitting. Return "
            "REJECT, REPAIR, or LEGITIMATE-CANDIDATE with exact reasons."
        ),
        "exclusion_completeness_auditor": (
            "For every constraint/no-go candidate construct the strongest RH-false "
            "configuration compatible with it. Check all symmetry partners, "
            "multiplicity, cancellation, arbitrarily sparse exceptions, zeros "
            "arbitrarily close to the line, and high-height nonuniformity. One survivor "
            "means exclusion is incomplete."
        ),
        "independent_referee": (
            "Fresh hostile expert review using only frozen definitions, statements, "
            "dependencies, frontier and permitted sources. Do not infer missing steps. "
            "A new mathematical structure is accepted only after its definitions and "
            "central claimed theorem are logically sound; RH relevance is a separate "
            "question."
        ),
    }

    async def certify(key: str) -> Dict:
        return await run_one(
            key,
            f"{tasks[key]}\n\nFROZEN CANDIDATE BUNDLE:\n{frozen}",
            research_context,
            constitution,
        )

    results = await asyncio.gather(*(certify(k) for k in CERTIFICATION_KEYS))
    for item in results:
        append_jsonl("runs", item)
    return results


async def generalization_round(
    research_context: str,
    constitution: str,
    candidate_bundle: Dict,
    certification: List[Dict],
) -> List[Dict]:
    cert_text = "\n\n".join(f"### {x['agent_name']}\n{x['output']}" for x in certification)
    frozen = candidate_bundle["output"]
    task_base = f"""
Only analyze candidates that genuinely survive certification. A proof draft with
a GAP is not a theorem. A newly invented object must pass mathematical legitimacy
before it is generalized. A no-go law requires proved soundness plus exclusion
completeness.

FROZEN CANDIDATES:\n{frozen}\n\nCERTIFICATION REPORTS:\n{cert_text}
""".strip()

    tasks = {
        "abstraction_agent": task_base + (
            "\n\nFind the weakest natural abstract setting in which each surviving result "
            "remains true. Develop reusable theorem statements beyond xi/RH."
        ),
        "transfer_agent": task_base + (
            "\n\nSeek at least one rigorous non-RH consequence/application for each "
            "surviving new structure. An example without a theorem does not count."
        ),
        "novelty_auditor": task_base + (
            "\n\nUse live search to try aggressively to identify the candidate as known, "
            "equivalent, or a disguised special case. Compare with relevant entire-"
            "function, operator, moment, positivity, de Branges, Weil/Li, Laguerre, "
            "spectral, heat-flow, and analytic-number-theory literature. Report scope "
            "and uncertainty honestly."
        ),
    }

    results = await asyncio.gather(
        *(run_one(k, tasks[k], research_context, constitution) for k in GENERALIZATION_KEYS)
    )
    for item in results:
        append_jsonl("runs", item)
    return results


async def run_lab(target: str) -> None:
    ensure_memory()
    constitution = load_constitution()

    frontier_audit = await live_frontier_audit(target, constitution)
    research_context = build_research_context(target, frontier_audit["output"])

    inventions = await independent_invention_round(research_context, constitution)
    bundle = await synthesize_candidates(research_context, constitution, inventions)
    certification = await certification_round(research_context, constitution, bundle)
    generalization = await generalization_round(
        research_context, constitution, bundle, certification
    )

    report = {
        "target": target,
        "frontier_as_of": "2026-08-14",
        "model": DEFAULT_MODEL,
        "live_frontier_audit": frontier_audit,
        "inventions": inventions,
        "candidate_bundle": bundle,
        "certification": certification,
        "generalization": generalization,
        "warning": (
            "No output is automatically a theorem. New mathematics and RH claims "
            "must pass independent proof, legitimacy, circularity, adversarial, "
            "generalization, and novelty gates."
        ),
    }
    append_jsonl("runs", {"final_report": report})
    print(json.dumps(report, ensure_ascii=False, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the Riemann Mathematical Invention Lab")
    parser.add_argument(
        "--target",
        default=DEFAULT_TARGET,
        help="Optional precise obstruction; default uses the full frontier portfolio",
    )
    args = parser.parse_args()
    asyncio.run(run_lab(args.target))


if __name__ == "__main__":
    main()
