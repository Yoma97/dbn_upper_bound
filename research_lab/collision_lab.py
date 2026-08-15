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
PROGRAM_PATH = ROOT / "knowledge" / "unified_collision_geometry_program.md"
SOURCE_REGISTRY_PATH = ROOT / "knowledge" / "source_registry.yaml"
DEFAULT_MODEL = os.getenv("OPENAI_DEFAULT_MODEL", "gpt-5.6-sol")

PRIMARY_KEYS = [
    "collision_unifier",
    "regularization_architect",
    "phase_current_analyst",
    "gap_trace_analyst",
    "collision_flux_analyst",
]

BACKUP_KEYS = ["arithmetic_separator_specialist"]

CERT_KEYS = [
    "proof_architect",
    "destroyer",
    "equivalence_auditor",
    "mathematical_legitimacy_auditor",
    "independent_referee",
]

WEB_ENABLED_KEYS = {"frontier_curator", "novelty_auditor"}

DEFAULT_TARGET = """
FOCUSED MODE. Do not open unrelated RH directions.

Primary program: determine whether discriminant, inverse-square gap trace,
phase/transversality current, and topological collision charge for finite
real-rooted heat polynomials can be lifted to a single canonical relative
collision geometry for the Riemann de Bruijn--Newman heat family.

The goal is NOT to prove RH in this run. The goal is to construct correct new
mathematics or rigorously show why the proposed unification fails.

Only after well-definedness, collision locality, cutoff independence, finite
prototype recovery, and an evolution identity are established may any agent ask
for a Riemann-specific no-collision law.

Independent backup: localized arithmetic separator. Keep it logically separate
from the collision program and flag disguised Weil/Li equivalence immediately.
""".strip()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def ensure_memory() -> None:
    MEMORY.mkdir(parents=True, exist_ok=True)
    for name in [
        "collision_frontier_audits",
        "collision_ideas",
        "collision_candidates",
        "collision_certification",
        "collision_refuted",
        "collision_runs",
    ]:
        p = MEMORY / f"{name}.jsonl"
        if not p.exists():
            p.touch()


def append_jsonl(name: str, payload: Dict) -> None:
    ensure_memory()
    with (MEMORY / f"{name}.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(payload, ensure_ascii=False) + "\n")


def build_context(target: str, live_delta: str = "") -> str:
    return (
        f"ROUND TARGET:\n{target}\n\n"
        f"UNIFIED COLLISION GEOMETRY PROGRAM:\n{read(PROGRAM_PATH)}\n\n"
        f"EXTERNAL FRONTIER MAP:\n{read(FRONTIER_PATH)}\n\n"
        f"SOURCE REGISTRY:\n{read(SOURCE_REGISTRY_PATH)}\n\n"
        f"LIVE LITERATURE DELTA:\n{live_delta if live_delta else 'Not yet audited.'}"
    )


def make_agent(key: str, context: str, constitution: str) -> Agent:
    tools = [WebSearchTool(search_context_size="high")] if key in WEB_ENABLED_KEYS else []
    return Agent(
        name=AGENTS[key].name,
        instructions=render_agent_prompt(key, constitution, context),
        model=DEFAULT_MODEL,
        tools=tools,
    )


async def run_one(key: str, task: str, context: str, constitution: str) -> Dict:
    result = await Runner.run(
        make_agent(key, context, constitution),
        task,
        run_config=RunConfig(model=DEFAULT_MODEL),
    )
    return {
        "agent_key": key,
        "agent_name": AGENTS[key].name,
        "phase": AGENTS[key].phase,
        "output": result.final_output,
    }


async def frontier_audit(target: str, constitution: str) -> Dict:
    context = build_context(target)
    task = """
Audit only literature that can directly bear on the focused program:
regularized discriminants/resultants of entire functions, zero-interaction
energies under backward heat flow, de Bruijn--Newman zero dynamics,
regularized pair traces/superzeta methods, phase/transversality currents,
topological collision indices, and localized Weil/Li separators.

For each relevant source give exact theorem, hypotheses, date, and source tier.
Most importantly, identify any theorem that already proves or refutes one of the
finite-to-infinite lifting steps. Do not broaden to unrelated RH approaches.
""".strip()
    out = await run_one("frontier_curator", task, context, constitution)
    append_jsonl("collision_frontier_audits", out)
    return out


async def invention_round(context: str, constitution: str) -> List[Dict]:
    common = """
This is a focused invention run. Stay inside the Unified Collision Geometry
Program. Reproduce the finite heat-polynomial prototype first; then address only
your assigned subproblem.

A candidate must state FORMAL DEFINITION, DOMAIN, FINITE RECOVERY,
WELL-DEFINEDNESS, COLLISION LOCALITY, CUTOFF/GAUGE DEPENDENCE, EVOLUTION LAW,
RELATION TO OTHER SHADOWS, FASTEST COUNTEREXAMPLE, CIRCULARITY RISK, and STATUS.

You are allowed and encouraged to conclude REFUTED. A rigorous impossibility
result is more valuable than a vague unified formula. Do not claim theoremhood.
""".strip()
    results = await asyncio.gather(
        *(run_one(k, common, context, constitution) for k in PRIMARY_KEYS + BACKUP_KEYS)
    )
    for item in results:
        append_jsonl("collision_ideas", item)
    return results


async def synthesis_round(context: str, constitution: str, ideas: List[Dict]) -> Dict:
    transcript = "\n\n".join(
        f"### {x['agent_name']}\n{x['output']}" for x in ideas
    )
    task = f"""
Synthesize the focused proposals below. Do not force unification.

Classify every proposed bridge as one of:
- EXACT FINITE IDENTITY,
- RIGOROUS INFINITE CONSTRUCTION,
- CONDITIONAL LIFT,
- CANDIDATE,
- REFUTED.

Preserve at most THREE primary candidates. A primary candidate survives only if
it passes basic definition/naturality screening and has a concrete proof
obligation smaller than RH. If discriminant/gap/current/topology do not unify,
state the maximal subset that does and why.

The arithmetic separator remains a separate backup and must never be used to
paper over a failure of collision regularization.

For each survivor freeze a precise theorem-shaped statement, assumptions,
dependency graph, and fastest destructive test.

PROPOSALS:\n{transcript}
""".strip()
    out = await run_one("proof_architect", task, context, constitution)
    append_jsonl("collision_candidates", out)
    return out


async def certification_round(context: str, constitution: str, bundle: Dict) -> List[Dict]:
    frozen = bundle["output"]
    tasks = {
        "proof_architect": "Attempt a full proof of every frozen finite or infinite claim. For regularized objects prove convergence/cutoff independence before using them. Mark each unresolved implication GAP.",
        "destroyer": "Destroy the frozen candidates using colliding heat polynomials, alternative cutoffs/enumerations, model entire functions with the same zero density but altered tails, higher-multiplicity collisions, and tail counterterms. Seek one decisive counterexample per candidate.",
        "equivalence_auditor": "Audit for hidden RH, Laguerre-Polya, Weil/Li positivity, Lambda<=0, or all-real-zero assumptions. Distinguish a new collision theorem from an endpoint-equivalent restatement.",
        "mathematical_legitimacy_auditor": "Audit definitions of regularized discriminants, resultants, finite-part gap traces, currents and charges for convergence, canonical normalization, choice independence, local collision sensitivity, domains and distributional legitimacy.",
        "independent_referee": "Fresh hostile referee: accept only statements whose finite prototype, regularization, collision locality, and evolution law are actually proved. Do not infer a missing theorem from the intended geometric picture.",
    }

    async def one(k: str) -> Dict:
        return await run_one(k, tasks[k] + f"\n\nFROZEN BUNDLE:\n{frozen}", context, constitution)

    out = await asyncio.gather(*(one(k) for k in CERT_KEYS))
    for item in out:
        append_jsonl("collision_certification", item)
    return out


async def novelty_round(context: str, constitution: str, bundle: Dict, cert: List[Dict]) -> Dict:
    cert_text = "\n\n".join(f"### {x['agent_name']}\n{x['output']}" for x in cert)
    task = f"""
Search current primary literature specifically for every surviving object or
identity. Compare with discriminants/resultants, zeta-regularized determinants,
superzeta functions, Calogero/heat-zero energies, Dyson/Vandermonde identities,
Krein spectral shift/relative determinants, argument-principle currents,
Poincare-Hopf/Brouwer degree collision counting, Rodgers--Tao Hamiltonians, and
Weil/Li/Bombieri--Lagarias separators.

Do not declare novelty from absence of a quick hit. Report closest prior art and
whether the survivor is genuinely new, a new synthesis, a special case, or known.

FROZEN BUNDLE:\n{bundle['output']}\n\nCERTIFICATION:\n{cert_text}
""".strip()
    out = await run_one("novelty_auditor", task, context, constitution)
    append_jsonl("collision_runs", out)
    return out


async def run_lab(target: str) -> None:
    ensure_memory()
    constitution = read(CONSTITUTION_PATH)
    audit = await frontier_audit(target, constitution)
    context = build_context(target, audit["output"])
    ideas = await invention_round(context, constitution)
    bundle = await synthesis_round(context, constitution, ideas)
    cert = await certification_round(context, constitution, bundle)
    novelty = await novelty_round(context, constitution, bundle, cert)
    report = {
        "mode": "unified_collision_geometry",
        "model": DEFAULT_MODEL,
        "target": target,
        "frontier_audit": audit,
        "ideas": ideas,
        "candidate_bundle": bundle,
        "certification": cert,
        "novelty": novelty,
        "warning": "This focused lab may establish new mathematics, refute the unification, or return gaps. It does not auto-promote any claim to an RH proof.",
    }
    append_jsonl("collision_runs", {"final_report": report})
    print(json.dumps(report, ensure_ascii=False, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(description="Focused Unified Collision Geometry research lab")
    parser.add_argument("--target", default=DEFAULT_TARGET)
    args = parser.parse_args()
    asyncio.run(run_lab(args.target))


if __name__ == "__main__":
    main()
