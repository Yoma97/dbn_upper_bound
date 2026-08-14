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
SOURCE_REGISTRY_PATH = ROOT / "knowledge" / "source_registry.yaml"
DEFAULT_MODEL = os.getenv("OPENAI_DEFAULT_MODEL", "gpt-5.6-sol")

INVENTION_KEYS = [
    "obstruction_analyst",
    "constraint_hunter",
    "violation_amplifier",
    "object_inventor",
    "identity_invariant_hunter",
    "bridge_builder",
    "definition_inventor",
]

CERTIFICATION_KEYS = [
    "proof_architect",
    "destroyer",
    "equivalence_auditor",
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
Seek the weakest genuinely new and plausibly provable intermediate theorem that
advances the Riemann Hypothesis beyond the strongest currently established
frontier. Give especially high priority to EXCLUSION-FIRST mechanisms:

0. find an independently provable no-go law C that the genuine zeta/xi structure
   must satisfy, together with a complete theorem that every RH-false admissible
   zero configuration violates C;
1. sparse-exception amplification/rigidity: one off-line zero must create a
   detectable sign, growth, spectral, correlation, moment, heat-flow, or
   prime-side defect that cannot be cancelled or hidden;
2. unconditional horizontal-multiplicity or horizontally weighted pair bounds;
3. a bridge from current zero-density estimates to pair-correlation horizontal information;
4. a structural de Bruijn-Newman mechanism independent of finite-height verification;
5. a non-tautological long-mollifier/variational mechanism;
6. a new hyperbolicity/Laguerre propagation theorem that reaches low-shift/high-degree territory.

Do not merely improve a numerical constant. Do not restate an RH-equivalent
criterion as the proposed advance unless you also provide a genuinely independent
route to prove the criterion. A high-value result should have independent
mathematical content and, ideally, applications beyond the Riemann xi-function.
""".strip()


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_constitution() -> str:
    return load_text(CONSTITUTION_PATH)


def build_research_context(target: str, live_delta: str = "") -> str:
    frontier = load_text(FRONTIER_PATH)
    registry = load_text(SOURCE_REGISTRY_PATH)
    delta_section = (
        f"\n\nLIVE FRONTIER AUDIT FOR THIS RUN:\n{live_delta}\n"
        if live_delta
        else ""
    )
    return (
        f"USER/ROUND TARGET:\n{target}\n\n"
        f"DATED EXTERNAL FRONTIER MAP:\n{frontier}\n\n"
        f"SOURCE PROVENANCE REGISTRY:\n{registry}"
        f"{delta_section}"
    )


def ensure_memory() -> None:
    MEMORY.mkdir(parents=True, exist_ok=True)
    for name in ["frontier_audits", "ideas", "candidates", "theorems", "refuted", "dead_ends", "runs"]:
        path = MEMORY / f"{name}.jsonl"
        if not path.exists():
            path.touch()


def append_jsonl(name: str, payload: Dict) -> None:
    ensure_memory()
    with (MEMORY / f"{name}.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(payload, ensure_ascii=False) + "\n")


def make_agent(key: str, research_context: str, constitution: str) -> Agent:
    spec = AGENTS[key]
    tools = []
    if key in WEB_ENABLED_KEYS:
        tools = [WebSearchTool(search_context_size="high")]
    return Agent(
        name=spec.name,
        instructions=render_agent_prompt(key, constitution, research_context),
        model=DEFAULT_MODEL,
        tools=tools,
    )


async def run_one(key: str, task: str, research_context: str, constitution: str) -> Dict:
    agent = make_agent(key, research_context, constitution)
    result = await Runner.run(
        agent,
        task,
        run_config=RunConfig(model=DEFAULT_MODEL),
    )
    return {
        "agent_key": key,
        "agent_name": AGENTS[key].name,
        "phase": AGENTS[key].phase,
        "output": result.final_output,
    }


async def live_frontier_audit(target: str, constitution: str) -> Dict:
    baseline_context = build_research_context(target)
    task = """
Audit the dated frontier against the live literature before any invention begins.
Search primarily official sources, journal pages, arXiv records/full text, and
author-maintained research sources. Focus on results that could materially change
a KNOWN claim, a LIMITATION, a MISSING-THEOREM target, or an exclusion/positivity
mechanism relevant to the constraint-first program.

For every possible update:
1. give title/authors/date/source;
2. state the exact theorem and hypotheses, not a headline paraphrase;
3. classify source tier A/B/C/D using the registry rules;
4. say whether it CONFIRMS, SUPERSEDES, NARROWS, or DOES NOT CHANGE the baseline;
5. distinguish a proof, conditional theorem, computational certificate, and claimed proof;
6. reject extraordinary RH claims that lack community/official validation as theorem premises.

Return a concise delta. If no verified material change is found, say so explicitly.
Do not invent new mathematics in this stage.
""".strip()
    result = await run_one("frontier_curator", task, baseline_context, constitution)
    append_jsonl("frontier_audits", result)
    return result


async def independent_invention_round(research_context: str, constitution: str) -> List[Dict]:
    task = """
Work independently. Do not assume access to other agents' proposals.

First select one or two exact frontier obstructions from the supplied dated map
and live audit. Then produce up to four genuinely distinct candidate mechanisms.
Constraint-first proposals must separate SOUNDNESS (why the true zeta/xi object
obeys the law independently of RH) from EXCLUSION COMPLETENESS (why every
RH-false admissible configuration violates it). Violation-amplification proposals
must begin from the weakest false scenario, such as one off-line zero plus forced
symmetry partners, and prove how it becomes detectable despite cancellation and
sparsity.

Across your proposals, favor cross-frontier bridges and exact identities,
invariants, propagation laws, rigidity theorems, positivity/definiteness laws,
moment constraints, trace/operator inequalities, or new structural statistics
rather than refined estimates.

For every proposal:
- quote the exact strongest known input from the frontier map/live audit;
- state the current limitation;
- state a precise new intermediate theorem;
- give the implication chain showing what it would improve;
- explain why it is not merely RH/PCC/ES/theta=infinity/LP/Li/Weil positivity in disguise;
- if it is an endpoint-equivalent criterion, provide the independent lower-level mechanism intended to prove it;
- list all false configurations the proposal excludes and any that may survive;
- give the fastest way to falsify it;
- identify which source tiers it depends on.

Freeze each candidate. Do not call any proposal a theorem.
""".strip()
    results = await asyncio.gather(
        *(run_one(key, task, research_context, constitution) for key in INVENTION_KEYS)
    )
    for item in results:
        append_jsonl("ideas", item)
    return results


async def synthesize_candidates(research_context: str, constitution: str, inventions: List[Dict]) -> Dict:
    transcript = "\n\n".join(
        f"### {x['agent_name']}\n{x['output']}" for x in inventions
    )
    task = f"""
You are the synthesis stage. Compare the independently frozen proposals below.
Do NOT reward agreement, grandiosity, or verbosity. Select at most five
candidates using this order of preference:

1. supplies an independently provable constraint/no-go law with a credible path to COMPLETE exclusion of all RH-false configurations;
2. amplifies a sparse/local off-line defect into an unavoidable observable contradiction;
3. closes a precisely documented frontier obstruction;
4. has hypotheses strictly weaker/different from an RH-equivalent endpoint;
5. creates a rigorous bridge between established partial theories;
6. is falsifiable and plausibly provable with current inputs plus a genuinely new lemma;
7. has potential independent mathematical value beyond RH.

For a constraint candidate, freeze separate obligations for SOUNDNESS and
EXCLUSION COMPLETENESS. For an amplifier, freeze the minimal-false configuration,
the amplification lemma, cancellation control, and the established observable
that should contradict it.

For each selected candidate output a frozen statement and an explicit dependency
graph. Reject proposals that merely rename RH, assume PCC/ES, assume every zero
lies in a 1/log(T) box, assume unrestricted theta=infinity, ask directly for all
Jensen hyperbolicities, merely restate Li/Weil positivity without an independent
proof mechanism, improve a constant without a logical threshold, or rely on
numerical evidence. Merge proposals only if their mechanisms are genuinely the same.

INDEPENDENT PROPOSALS:
{transcript}
""".strip()
    result = await run_one("proof_architect", task, research_context, constitution)
    append_jsonl("candidates", result)
    return result


async def certification_round(research_context: str, constitution: str, candidate_bundle: Dict) -> List[Dict]:
    frozen = candidate_bundle["output"]
    tasks = {
        "proof_architect": "Attempt a complete dependency-explicit proof of each frozen candidate from allowed frontier inputs. For no-go candidates prove SOUNDNESS and EXCLUSION COMPLETENESS separately. Mark every missing implication as GAP. Do not silently upgrade source tiers.",
        "destroyer": "Attack each frozen candidate with abstract countermodels, perturbations, limiting regimes, sparse exceptional zero configurations, multiplicity issues, cancellation mechanisms, hidden nonuniformity, and rigorous numerical counterexample searches where useful. Refute whenever possible.",
        "equivalence_auditor": "Audit each frozen candidate for hidden RH/PCC/ES/theta=infinity dependence, equivalence to Li/Weil/Laguerre or another endpoint criterion without an independent proof route, circular reasoning, or a hypothesis as hard as the target. Trace every dependency to the source registry.",
        "exclusion_completeness_auditor": "Audit every proposed constraint/no-go theorem for COMPLETE exclusion. Construct the strongest surviving RH-false configuration compatible with the claimed law. Check functional-equation/conjugation partners, multiplicity, cancellation among several off-line zeros, arbitrarily sparse exceptions, zeros arbitrarily close to the line, and high-height nonuniformity. If any false configuration survives, mark the exclusion incomplete and state it explicitly.",
        "independent_referee": "Act as a fresh hostile expert referee. You are given only the frozen candidate bundle, the dated frontier, live audit, and permitted sources. Determine which claims, if any, are fully proved. A constraint route passes only if both soundness and complete exclusion are proved. Do not infer missing arguments from author intent.",
    }

    async def certify(key: str) -> Dict:
        prompt = f"{tasks[key]}\n\nFROZEN CANDIDATE BUNDLE:\n{frozen}"
        return await run_one(key, prompt, research_context, constitution)

    results = await asyncio.gather(*(certify(k) for k in CERTIFICATION_KEYS))
    for item in results:
        append_jsonl("runs", item)
    return results


async def generalization_round(research_context: str, constitution: str, candidate_bundle: Dict, certification: List[Dict]) -> List[Dict]:
    cert_text = "\n\n".join(f"### {x['agent_name']}\n{x['output']}" for x in certification)
    frozen = candidate_bundle["output"]
    task_base = f"""
Only analyze candidates that genuinely survive the certification evidence.
Do not treat a proof draft with a GAP as a theorem. Distinguish a proved lemma
from a conjectural bridge and from a merely numerically supported statement.
For a no-go law, require proved soundness plus proved exclusion completeness.

FROZEN CANDIDATES:\n{frozen}\n\nCERTIFICATION REPORTS:\n{cert_text}
""".strip()

    tasks = {
        "abstraction_agent": task_base + "\n\nFind the weakest natural abstract setting in which any surviving result remains rigorously true. Seek a general no-go/positivity/rigidity theorem that applies beyond xi/RH.",
        "transfer_agent": task_base + "\n\nSeek rigorous non-Riemann applications or independent consequences. An example without a proved consequence does not count as transfer.",
        "novelty_auditor": task_base + "\n\nUse live web search as needed to try aggressively to show that any surviving object/theorem is already known, equivalent to a known theorem, or a disguised special case. In particular compare with Weil positivity, Li/Bombieri-Lagarias criteria, de Branges/Suzuki moment and operator formulations, and function-field positivity mechanisms. Prefer primary sources. Report search scope and uncertainty.",
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
    generalization = await generalization_round(research_context, constitution, bundle, certification)

    report = {
        "target": target,
        "frontier_as_of": "2026-08-14",
        "model": DEFAULT_MODEL,
        "live_frontier_audit": frontier_audit,
        "inventions": inventions,
        "candidate_bundle": bundle,
        "certification": certification,
        "generalization": generalization,
        "warning": "No output is automatically a theorem. Human/formal promotion gates remain mandatory.",
    }
    append_jsonl("runs", {"final_report": report})
    print(json.dumps(report, ensure_ascii=False, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the Riemann Mathematical Invention Lab")
    parser.add_argument("--target", default=DEFAULT_TARGET, help="Optional precise obstruction; default uses the full dated frontier portfolio")
    args = parser.parse_args()
    asyncio.run(run_lab(args.target))


if __name__ == "__main__":
    main()
