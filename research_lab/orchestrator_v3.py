from __future__ import annotations

import argparse
import asyncio
import json
import os
from pathlib import Path
from typing import Dict, List

from agents import Agent, RunConfig, Runner, WebSearchTool

from arb_verification import (
    ArbCapability,
    ArbJob,
    NumericalRole,
    append_job,
    universal_claim_warning,
)
from model_policy import model_settings_for
from roles import AGENTS, render_agent_prompt
from structured_outputs import AuditReport, ClaimCard, ResearchReport


ROOT = Path(__file__).resolve().parent
MEMORY = ROOT / "memory_v3"
DEFAULT_MODEL = os.getenv("OPENAI_DEFAULT_MODEL", "gpt-5.6-sol")

CONSTITUTION = ROOT / "prompts" / "constitution.md"
FRONTIER = ROOT / "knowledge" / "frontier_map.md"
CONSTRAINTS = ROOT / "knowledge" / "constraint_frontier.md"
INVENTION = ROOT / "knowledge" / "mathematical_invention_charter.md"
SOURCES = ROOT / "knowledge" / "source_registry.yaml"
HYGIENE = ROOT / "knowledge" / "research_hygiene_protocol.md"
CONVENTIONS = ROOT / "knowledge" / "convention_lock.md"
ARB_PROTOCOL = ROOT / "knowledge" / "arb_verification_protocol.md"

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


def ensure_memory() -> None:
    MEMORY.mkdir(parents=True, exist_ok=True)
    for name in [
        "frontier",
        "inventions",
        "frozen_candidates",
        "audits",
        "arb_gate_results",
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


def build_context(target: str, frontier_delta: str = "") -> str:
    sections = [
        f"ROUND TARGET:\n{target}",
        f"MATHEMATICAL RESEARCH CONSTITUTION:\n{read(CONSTITUTION)}",
        f"STRICT RESEARCH HYGIENE PROTOCOL:\n{read(HYGIENE)}",
        f"CANONICAL CONVENTION LOCK:\n{read(CONVENTIONS)}",
        f"RIGOROUS ARB VERIFICATION PROTOCOL:\n{read(ARB_PROTOCOL)}",
        f"DATED FRONTIER MAP:\n{read(FRONTIER)}",
        f"CONSTRAINT FRONTIER:\n{read(CONSTRAINTS)}",
        f"MATHEMATICAL INVENTION CHARTER:\n{read(INVENTION)}",
        f"SOURCE REGISTRY:\n{read(SOURCES)}",
    ]
    if frontier_delta:
        sections.append(f"LIVE FRONTIER DELTA:\n{frontier_delta}")
    return "\n\n".join(sections)


def enforce_claim_hygiene(claim: ClaimCard) -> ClaimCard:
    if claim.unresolved_gaps:
        claim.truth_label = "CANDIDATE"

    if any(dep.conjectural for dep in claim.strongest_known_input):
        claim.truth_label = "CANDIDATE"
        marker = "Conjectural imported dependency present"
        if marker not in claim.unresolved_gaps:
            claim.unresolved_gaps.append(marker)

    # One-New-Lemma Rule: routes with multiple independent gaps are diagnostic,
    # not the next proof target.
    if len(claim.unresolved_gaps) > 1:
        claim.relevance_label = "DIAGNOSTIC_TOOL"

    if claim.truth_label == "PROVED" and claim.novelty_label == "NOT_ASSESSED":
        claim.novelty_label = "NOVELTY_UNVERIFIED"

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
        model_settings=model_settings_for(key),
        tools=tools,
        output_type=output_type,
    )


async def run_research_agent(key: str, task: str, ctx: str) -> ResearchReport:
    agent = make_role_agent(key, ctx, ResearchReport)
    result = await Runner.run(
        agent,
        task,
        run_config=RunConfig(model=DEFAULT_MODEL, workflow_name=f"RH-Lab-v3/{key}"),
    )
    return enforce_report_hygiene(result.final_output)


async def run_audit_agent(key: str, task: str, ctx: str) -> AuditReport:
    agent = make_role_agent(key, ctx, AuditReport)
    result = await Runner.run(
        agent,
        task,
        run_config=RunConfig(model=DEFAULT_MODEL, workflow_name=f"RH-Lab-v3/{key}"),
    )
    return result.final_output


def queue_arb_requests(report: ResearchReport, origin: str) -> List[dict]:
    results: List[dict] = []
    for claim in report.claims:
        for req in claim.numerical_requests:
            try:
                capability = ArbCapability(req.capability)
            except ValueError:
                payload = {
                    "origin": origin,
                    "claim": claim.title,
                    "status": "ARB_CAPABILITY_UNKNOWN",
                    "capability": req.capability,
                    "reason": "Capability is not present in the strict Arb capability registry.",
                }
                dump_jsonl("arb_gate_results", payload)
                results.append(payload)
                continue

            job = ArbJob(
                title=f"{claim.title}: {req.mathematical_quantity}",
                role=NumericalRole(req.role),
                capability=capability,
                mathematical_quantity=req.mathematical_quantity,
                inputs=req.inputs,
                certified_domain=req.certified_domain,
                analytic_reduction=req.analytic_reduction,
                logically_necessary=req.logically_necessary,
            )
            gate = append_job(MEMORY, job)
            payload = {
                "origin": origin,
                "claim": claim.title,
                "job_id": job.job_id,
                "status": gate.status,
                "runnable_now": gate.runnable_now,
                "reason": gate.reason,
            }
            dump_jsonl("arb_gate_results", payload)
            results.append(payload)
    return results


async def frontier_audit(target: str) -> ResearchReport:
    ctx = build_context(target)
    task = """
Audit current primary/official literature only. Report material frontier changes.
Do not invent mathematics. Distinguish theorem, conditional theorem, preprint,
computation and claimed proof. State exact hypotheses, source tier and conventions.
""".strip()
    report = await run_research_agent("frontier_curator", task, ctx)
    dump_jsonl("frontier", report.model_dump())
    return report


async def invention_round(ctx: str) -> List[ResearchReport]:
    task = f"""
Work blind and independently. Produce at most THREE atomic claims. Use the
One-New-Lemma Rule: a live route may contain at most one genuinely new unproved
lemma. State quantifiers, domains, conventions, assumption ledger, dependency
edges, edge cases and fastest falsification test.

Numerical work follows this rule exactly:
{universal_claim_warning()}

If computation would help, fill `numerical_requests`; do not pretend an unavailable
Arb capability exists and do not replace a missing rigorous capability with ordinary
floating point for certification.

Prefer a small theorem that can actually be proved to a long RH-shaped chain.
If you invent a new object, target one structural theorem meaningful outside RH.
""".strip()
    reports = await asyncio.gather(
        *(run_research_agent(key, task, ctx) for key in INVENTION_KEYS)
    )
    for report in reports:
        dump_jsonl("inventions", report.model_dump())
        queue_arb_requests(report, "invention")
    return reports


def candidate_public_view(claim: ClaimCard) -> Dict:
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
    all_claims = [c.model_dump() for report in reports for c in report.claims]
    agent = Agent(
        name="Strict Synthesis Judge",
        instructions=(read(CONSTITUTION) + "\n\n" + read(HYGIENE) + "\n\n" + read(CONVENTIONS) + "\n\n" + ctx),
        model=DEFAULT_MODEL,
        model_settings=model_settings_for("synthesis"),
        output_type=ResearchReport,
    )
    task = f"""
Select at most FOUR candidates.
Hard rules: atomic statement; at most one new unproved lemma; reject multi-gap
chains; reject hidden RH-equivalent endpoints without independent machinery;
prefer claims surviving toy, parity, multiplicity, endpoint and convention checks;
correctness does not imply novelty. Preserve one reusable mathematical structure
if legitimate.

PROPOSALS:\n{json.dumps(all_claims, ensure_ascii=False)}
""".strip()
    result = await Runner.run(
        agent,
        task,
        run_config=RunConfig(model=DEFAULT_MODEL, workflow_name="RH-Lab-v3/synthesis"),
    )
    report = enforce_report_hygiene(result.final_output)
    dump_jsonl("frozen_candidates", report.model_dump())
    queue_arb_requests(report, "synthesis")
    return report


async def adversarial_audits(ctx: str, bundle: ResearchReport) -> List[AuditReport]:
    frozen = [candidate_public_view(c) for c in bundle.claims]
    frozen_text = json.dumps(frozen, ensure_ascii=False)
    tasks = {
        "destroyer": "Attack first: smallest counterexample, parity/multiplicity, endpoints, scaling, perturbations and nonuniform limits. Never repair the frozen statement.",
        "equivalence_auditor": "Trace logical strength and reject disguised RH/PCC/ES/Li/Weil/LP/Lambda=0/full-Jensen/unrestricted-mollifier endpoints.",
        "mathematical_legitimacy_auditor": "Audit domains, convergence, symmetries, conventions, operator domains, branches and every infinite manipulation.",
        "exclusion_completeness_auditor": "For no-go laws construct the strongest RH-false configuration that can survive. One survivor means failure or repair.",
        "independent_referee": "Hostile review of the frozen statement and allowed dependencies only. Do not infer a proof from intent.",
    }

    async def run(key: str) -> AuditReport:
        return await run_audit_agent(key, tasks[key] + "\n\nFROZEN CLAIMS:\n" + frozen_text, ctx)

    audits = await asyncio.gather(*(run(k) for k in AUDIT_KEYS))
    for audit in audits:
        dump_jsonl("audits", audit.model_dump())
    return audits


def make_reconstructor(name: str, ctx: str) -> Agent:
    instructions = f"""
{read(CONSTITUTION)}

{read(HYGIENE)}

{read(CONVENTIONS)}

{read(ARB_PROTOCOL)}

{ctx}

ROLE: Independent Proof Reconstructor.
You see only the frozen statement, definitions, conventions and allowed established
dependencies. You never see the author's proof. Reconstruct from scratch or return
exact GAPs. A second new lemma may not be invented to rescue the first.
""".strip()
    return Agent(
        name=name,
        instructions=instructions,
        model=DEFAULT_MODEL,
        model_settings=model_settings_for("proof_reconstructor"),
        output_type=ResearchReport,
    )


async def reconstruct_twice(ctx: str, bundle: ResearchReport) -> List[ResearchReport]:
    frozen = [candidate_public_view(c) for c in bundle.claims]
    task = (
        "Attempt independent proofs from scratch. If a proof does not close, keep "
        "truth_label=CANDIDATE and list every GAP. Do not use numerical evidence as "
        "an infinite proof.\n\nFROZEN CLAIMS:\n" + json.dumps(frozen, ensure_ascii=False)
    )
    a1 = make_reconstructor("Independent Reconstructor A", ctx)
    a2 = make_reconstructor("Independent Reconstructor B", ctx)
    r1, r2 = await asyncio.gather(
        Runner.run(a1, task, run_config=RunConfig(model=DEFAULT_MODEL, workflow_name="RH-Lab-v3/reconstruct-A")),
        Runner.run(a2, task, run_config=RunConfig(model=DEFAULT_MODEL, workflow_name="RH-Lab-v3/reconstruct-B")),
    )
    reports = [enforce_report_hygiene(r1.final_output), enforce_report_hygiene(r2.final_output)]
    for report in reports:
        dump_jsonl("reconstructions", report.model_dump())
        queue_arb_requests(report, "reconstruction")
    return reports


async def run_lab(target: str) -> None:
    ensure_memory()
    frontier = await frontier_audit(target)
    ctx = build_context(target, frontier.summary)
    inventions = await invention_round(ctx)
    bundle = await synthesis(ctx, inventions)

    # Falsification precedes proof reconstruction.
    audits = await adversarial_audits(ctx, bundle)
    reconstructions = await reconstruct_twice(ctx, bundle)

    print("=== STRICT RH LAB V3 ===")
    print(json.dumps({
        "frontier": frontier.model_dump(),
        "frozen_candidates": bundle.model_dump(),
        "audits": [a.model_dump() for a in audits],
        "independent_reconstructions": [r.model_dump() for r in reconstructions],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Strict multi-agent RH research lab v3")
    parser.add_argument(
        "--target",
        default=(
            "Identify exactly one smallest non-circular theorem or genuinely new "
            "mathematical structure that advances the current verified RH frontier; "
            "prove or refute it before building beyond it."
        ),
    )
    args = parser.parse_args()
    asyncio.run(run_lab(args.target))
