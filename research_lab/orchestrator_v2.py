from __future__ import annotations

import argparse
import asyncio
import json
import os
from pathlib import Path
from typing import Dict, List

from agents import Agent, RunConfig, Runner, WebSearchTool

from roles import AGENTS, render_agent_prompt
from structured_outputs import AuditReport, ClaimCard, ResearchReport


ROOT = Path(__file__).resolve().parent
MEMORY = ROOT / "memory_v2"
DEFAULT_MODEL = os.getenv("OPENAI_DEFAULT_MODEL", "gpt-5.6-sol")

CONSTITUTION = ROOT / "prompts" / "constitution.md"
FRONTIER = ROOT / "knowledge" / "frontier_map.md"
CONSTRAINTS = ROOT / "knowledge" / "constraint_frontier.md"
INVENTION = ROOT / "knowledge" / "mathematical_invention_charter.md"
SOURCES = ROOT / "knowledge" / "source_registry.yaml"
HYGIENE = ROOT / "knowledge" / "research_hygiene_protocol.md"
CONVENTIONS = ROOT / "knowledge" / "convention_lock.md"

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

AUDIT_KEYS = [
    "destroyer",
    "equivalence_auditor",
    "mathematical_legitimacy_auditor",
    "exclusion_completeness_auditor",
    "independent_referee",
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def context(target: str, frontier_delta: str = "") -> str:
    return "\n\n".join(
        [
            f"ROUND TARGET:\n{target}",
            f"MATHEMATICAL RESEARCH CONSTITUTION:\n{read(CONSTITUTION)}",
            f"STRICT RESEARCH HYGIENE PROTOCOL:\n{read(HYGIENE)}",
            f"CANONICAL CONVENTION LOCK:\n{read(CONVENTIONS)}",
            f"DATED FRONTIER MAP:\n{read(FRONTIER)}",
            f"CONSTRAINT FRONTIER:\n{read(CONSTRAINTS)}",
            f"MATHEMATICAL INVENTION CHARTER:\n{read(INVENTION)}",
            f"SOURCE REGISTRY:\n{read(SOURCES)}",
            f"LIVE FRONTIER DELTA:\n{frontier_delta}" if frontier_delta else "",
        ]
    )


def ensure_memory() -> None:
    MEMORY.mkdir(parents=True, exist_ok=True)
    for name in [
        "frontier",
        "inventions",
        "frozen_candidates",
        "audits",
        "reconstructions",
        "refuted",
        "survivors",
    ]:
        p = MEMORY / f"{name}.jsonl"
        if not p.exists():
            p.touch()


def dump_jsonl(name: str, payload: Dict) -> None:
    ensure_memory()
    with (MEMORY / f"{name}.jsonl").open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(payload, ensure_ascii=False) + "\n")


def normalize_output(obj):
    if hasattr(obj, "model_dump"):
        return obj.model_dump()
    return obj


def enforce_claim_hygiene(claim: ClaimCard) -> ClaimCard:
    # A model cannot self-promote a gapped statement to PROVED.
    if claim.unresolved_gaps:
        claim.truth_label = "CANDIDATE"

    # Any conjectural imported dependency creates a gap.
    if any(dep.conjectural for dep in claim.strongest_known_input):
        claim.truth_label = "CANDIDATE"
        marker = "Conjectural imported dependency present"
        if marker not in claim.unresolved_gaps:
            claim.unresolved_gaps.append(marker)

    # One-New-Lemma Rule: a multi-gap route cannot be treated as the next target.
    if len(claim.unresolved_gaps) > 1:
        claim.relevance_label = "DIAGNOSTIC_TOOL"

    # Correctness never implies novelty.
    if claim.truth_label == "PROVED" and claim.novelty_label == "NOT_ASSESSED":
        claim.novelty_label = "NOVELTY_UNVERIFIED"

    # A bare reformulation cannot be called a frontier advance.
    if claim.relevance_label == "REFORMULATION_ONLY":
        claim.truth_label = claim.truth_label

    return claim


def enforce_report_hygiene(report: ResearchReport) -> ResearchReport:
    report.claims = [enforce_claim_hygiene(c) for c in report.claims]
    return report


def make_role_agent(key: str, ctx: str, output_type):
    spec = AGENTS[key]
    tools = [WebSearchTool(search_context_size="high")] if key in {
        "frontier_curator",
        "novelty_auditor",
    } else []
    return Agent(
        name=spec.name,
        instructions=render_agent_prompt(key, read(CONSTITUTION), ctx),
        model=DEFAULT_MODEL,
        tools=tools,
        output_type=output_type,
    )


async def run_research_agent(key: str, task: str, ctx: str) -> ResearchReport:
    agent = make_role_agent(key, ctx, ResearchReport)
    result = await Runner.run(
        agent,
        task,
        run_config=RunConfig(model=DEFAULT_MODEL, workflow_name=f"RH-Lab-v2/{key}"),
    )
    report = enforce_report_hygiene(result.final_output)
    return report


async def run_audit_agent(key: str, task: str, ctx: str) -> AuditReport:
    agent = make_role_agent(key, ctx, AuditReport)
    result = await Runner.run(
        agent,
        task,
        run_config=RunConfig(model=DEFAULT_MODEL, workflow_name=f"RH-Lab-v2/{key}"),
    )
    return result.final_output


async def frontier_audit(target: str) -> ResearchReport:
    ctx = context(target)
    task = """
Audit only primary/official current literature. Report material changes to the
frontier. Do not invent mathematics. Distinguish theorem, conditional theorem,
preprint, computation, and claimed proof. Every imported result must list exact
hypotheses and source tier.
""".strip()
    report = await run_research_agent("frontier_curator", task, ctx)
    dump_jsonl("frontier", report.model_dump())
    return report


async def invention_round(ctx: str) -> List[ResearchReport]:
    task = """
Work blind and independently. Produce at most THREE atomic claims. Before any
long proof attempt, run the fastest conceptual counterexample tests mentally.
Obey the One-New-Lemma Rule: do not build a chain containing two independent new
unproved lemmas. Separate correctness, novelty and RH relevance. Every candidate
must have explicit quantifiers, domains, conventions, assumption ledger,
dependency edges, edge-case tests, and the fastest falsification route.

Prefer a small theorem that can actually be proved over an impressive RH-shaped
conjectural chain. If you invent a new object, prove or target one structural law
that also makes sense outside RH.
""".strip()
    reports = await asyncio.gather(
        *(run_research_agent(key, task, ctx) for key in INVENTION_KEYS)
    )
    for report in reports:
        dump_jsonl("inventions", report.model_dump())
    return reports


def candidate_public_view(claim: ClaimCard) -> Dict:
    """What auditors/reconstructors are allowed to see after freeze."""
    return {
        "title": claim.title,
        "statement": claim.statement,
        "quantifiers_and_domains": claim.quantifiers_and_domains,
        "hypotheses": claim.hypotheses,
        "conventions_used": claim.conventions_used,
        "allowed_dependencies": [d.model_dump() for d in claim.strongest_known_input],
        "dependency_edges": claim.dependency_edges,
    }


async def synthesis(ctx: str, reports: List[ResearchReport]) -> ResearchReport:
    all_claims = []
    for report in reports:
        all_claims.extend(c.model_dump() for c in report.claims)

    synth = Agent(
        name="Strict Synthesis Judge",
        instructions=(
            read(CONSTITUTION)
            + "\n\n"
            + read(HYGIENE)
            + "\n\n"
            + read(CONVENTIONS)
            + "\n\n"
            + ctx
        ),
        model=DEFAULT_MODEL,
        output_type=ResearchReport,
    )
    task = f"""
Select at most FOUR candidates from the frozen proposals below.

Hard rules:
- one atomic statement per claim;
- at most one genuinely new unproved lemma in the route;
- reject multi-gap chains;
- reject hidden RH-equivalent endpoints without independent machinery;
- prefer candidates already surviving toy/collision/endpoint checks;
- do not infer novelty from correctness;
- preserve one genuinely reusable mathematical structure if it passes legitimacy.

PROPOSALS:\n{json.dumps(all_claims, ensure_ascii=False)}
""".strip()
    result = await Runner.run(
        synth,
        task,
        run_config=RunConfig(model=DEFAULT_MODEL, workflow_name="RH-Lab-v2/synthesis"),
    )
    report = enforce_report_hygiene(result.final_output)
    dump_jsonl("frozen_candidates", report.model_dump())
    return report


async def adversarial_audits(ctx: str, bundle: ResearchReport) -> List[AuditReport]:
    frozen = [candidate_public_view(c) for c in bundle.claims]
    task_base = json.dumps(frozen, ensure_ascii=False)

    tasks = {
        "destroyer": "Attack the frozen statements. Search first for the smallest counterexample, endpoint failure, parity/multiplicity failure, scaling failure, and nonuniform limit. Do not repair the claims.",
        "equivalence_auditor": "Determine whether any frozen statement is RH/PCC/ES/Li/Weil/LP/Lambda=0/full-Jensen/unrestricted-mollifier strength in disguise. Trace exact logical strength.",
        "mathematical_legitimacy_auditor": "Audit definitions, convergence, domains, symmetries, normalization, Fourier/time conventions, operator domains, and every infinite manipulation.",
        "exclusion_completeness_auditor": "For no-go claims, construct the strongest false-RH configuration that might survive. One survivor means FAIL or REPAIR.",
        "independent_referee": "Hostile referee review of statement and allowed dependencies only. Do not infer a proof from author intent.",
    }

    async def run(key: str):
        return await run_audit_agent(
            key,
            tasks[key] + "\n\nFROZEN CLAIMS:\n" + task_base,
            ctx,
        )

    audits = await asyncio.gather(*(run(k) for k in AUDIT_KEYS))
    for audit in audits:
        dump_jsonl("audits", audit.model_dump())
    return audits


def make_reconstructor(name: str, ctx: str) -> Agent:
    instructions = f"""
{read(CONSTITUTION)}

{read(HYGIENE)}

{read(CONVENTIONS)}

{ctx}

ROLE: Independent Proof Reconstructor
You receive only frozen statements, definitions, conventions, and allowed
established dependencies. You never see the author's proof. Reconstruct a proof
from scratch or return exact GAPs. Do not use numerical evidence as a global proof.
""".strip()
    return Agent(
        name=name,
        instructions=instructions,
        model=DEFAULT_MODEL,
        output_type=ResearchReport,
    )


async def reconstruct_twice(ctx: str, bundle: ResearchReport) -> List[ResearchReport]:
    frozen = [candidate_public_view(c) for c in bundle.claims]
    task = """
Attempt a proof from scratch for each frozen claim. If a proof cannot be closed,
leave truth_label=CANDIDATE and list every GAP. Do not create a second new lemma
to rescue the first. The objective is reproducibility, not persuasion.

FROZEN CLAIMS:
""" + json.dumps(frozen, ensure_ascii=False)

    a1 = make_reconstructor("Independent Reconstructor A", ctx)
    a2 = make_reconstructor("Independent Reconstructor B", ctx)
    r1, r2 = await asyncio.gather(
        Runner.run(a1, task, run_config=RunConfig(model=DEFAULT_MODEL, workflow_name="RH-Lab-v2/reconstruct-A")),
        Runner.run(a2, task, run_config=RunConfig(model=DEFAULT_MODEL, workflow_name="RH-Lab-v2/reconstruct-B")),
    )
    reports = [enforce_report_hygiene(r1.final_output), enforce_report_hygiene(r2.final_output)]
    for report in reports:
        dump_jsonl("reconstructions", report.model_dump())
    return reports


async def run_lab(target: str) -> None:
    ensure_memory()

    frontier = await frontier_audit(target)
    delta = frontier.summary
    ctx = context(target, delta)

    inventions = await invention_round(ctx)
    bundle = await synthesis(ctx, inventions)

    # Falsification and equivalence audits occur before proof reconstruction.
    audits = await adversarial_audits(ctx, bundle)

    # Reconstruct independently even if authors supplied proof-like material.
    reconstructions = await reconstruct_twice(ctx, bundle)

    print("=== STRICT RH LAB V2 ===")
    print(json.dumps({
        "frontier": frontier.model_dump(),
        "frozen_candidates": bundle.model_dump(),
        "audits": [a.model_dump() for a in audits],
        "independent_reconstructions": [r.model_dump() for r in reconstructions],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Strict multi-agent RH research lab v2")
    parser.add_argument("--target", default=(
        "Identify the smallest single non-circular theorem or genuinely new "
        "mathematical structure that advances the current verified RH frontier."
    ))
    args = parser.parse_args()
    asyncio.run(run_lab(args.target))
