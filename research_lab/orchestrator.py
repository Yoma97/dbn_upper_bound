from __future__ import annotations

import argparse
import asyncio
import json
import os
from pathlib import Path
from typing import Dict, List

from agents import Agent, RunConfig, Runner

from agents import AGENTS, render_agent_prompt


ROOT = Path(__file__).resolve().parent
MEMORY = ROOT / "memory"
CONSTITUTION_PATH = ROOT / "prompts" / "constitution.md"
DEFAULT_MODEL = os.getenv("OPENAI_DEFAULT_MODEL", "gpt-5.6-sol")

INVENTION_KEYS = [
    "obstruction_analyst",
    "object_inventor",
    "identity_invariant_hunter",
    "bridge_builder",
    "definition_inventor",
]

CERTIFICATION_KEYS = [
    "proof_architect",
    "destroyer",
    "equivalence_auditor",
    "independent_referee",
]

GENERALIZATION_KEYS = [
    "abstraction_agent",
    "transfer_agent",
    "novelty_auditor",
]

DEFAULT_TARGET = """
We are studying the de Bruijn-Newman heat-flow route to RH. The current program
has a partially controlled regime but retains an unresolved low-shoulder /
transversality obstruction. Do not merely improve constants. Seek the weakest
new structural theorem, exact identity, invariant, monotonicity principle,
non-collision mechanism, or abstract entire-function theorem that could remove
this obstruction without assuming RH or an equivalent hidden statement.

A useful proposal must state exactly how it would imply the missing
transversality/non-multiple-zero conclusion and why the proposed theorem could
plausibly be proved from established mathematics plus genuinely new lemmas.
""".strip()


def load_constitution() -> str:
    return CONSTITUTION_PATH.read_text(encoding="utf-8")


def ensure_memory() -> None:
    MEMORY.mkdir(parents=True, exist_ok=True)
    for name in ["ideas", "candidates", "theorems", "refuted", "dead_ends", "runs"]:
        path = MEMORY / f"{name}.jsonl"
        if not path.exists():
            path.touch()


def append_jsonl(name: str, payload: Dict) -> None:
    ensure_memory()
    with (MEMORY / f"{name}.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(payload, ensure_ascii=False) + "\n")


def make_agent(key: str, target: str, constitution: str) -> Agent:
    spec = AGENTS[key]
    return Agent(
        name=spec.name,
        instructions=render_agent_prompt(key, constitution, target),
        model=DEFAULT_MODEL,
    )


async def run_one(key: str, task: str, target: str, constitution: str) -> Dict:
    agent = make_agent(key, target, constitution)
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


async def independent_invention_round(target: str, constitution: str) -> List[Dict]:
    task = """
Work independently. Do not assume access to other agents' proposals. Produce
up to four genuinely distinct candidate mechanisms. At least one should attempt
an exact identity/invariant-style route rather than a refined estimate. Freeze
each candidate with a precise statement, hypotheses, proof plan, failure modes,
and the exact implication that would close the current target. Do not call any
proposal a theorem.
""".strip()
    results = await asyncio.gather(
        *(run_one(key, task, target, constitution) for key in INVENTION_KEYS)
    )
    for item in results:
        append_jsonl("ideas", item)
    return results


async def synthesize_candidates(target: str, constitution: str, inventions: List[Dict]) -> Dict:
    transcript = "\n\n".join(
        f"### {x['agent_name']}\n{x['output']}" for x in inventions
    )
    task = f"""
You are the synthesis stage. Compare the independently frozen proposals below.
Do NOT reward agreement or verbosity. Select at most five candidates that are
most structurally novel, falsifiable, non-circular, and plausibly provable.
Merge two proposals only if the mathematical mechanism is genuinely the same.
For each selected candidate output a frozen statement and a list of exact proof
obligations. Explicitly reject proposals that only rename RH, improve a constant
without crossing a logical threshold, or depend on numerical evidence.

INDEPENDENT PROPOSALS:
{transcript}
""".strip()
    result = await run_one("proof_architect", task, target, constitution)
    append_jsonl("candidates", result)
    return result


async def certification_round(target: str, constitution: str, candidate_bundle: Dict) -> List[Dict]:
    frozen = candidate_bundle["output"]
    tasks = {
        "proof_architect": "Attempt a complete dependency-explicit proof of each frozen candidate. Mark every missing implication as GAP.",
        "destroyer": "Attack each frozen candidate. Search for countermodels, perturbations, limiting-regime failures, multiplicity issues, and hidden nonuniformity. Refute whenever possible.",
        "equivalence_auditor": "Audit each frozen candidate for hidden RH dependence, equivalence to RH, circular reasoning, or a hypothesis as hard as the target.",
        "independent_referee": "Act as a fresh hostile expert referee. You are given only the frozen candidate bundle below. Determine which claims, if any, are fully proved. Do not infer missing arguments from author intent.",
    }

    async def certify(key: str) -> Dict:
        prompt = f"{tasks[key]}\n\nFROZEN CANDIDATE BUNDLE:\n{frozen}"
        return await run_one(key, prompt, target, constitution)

    results = await asyncio.gather(*(certify(k) for k in CERTIFICATION_KEYS))
    for item in results:
        append_jsonl("runs", item)
    return results


async def generalization_round(target: str, constitution: str, candidate_bundle: Dict, certification: List[Dict]) -> List[Dict]:
    cert_text = "\n\n".join(f"### {x['agent_name']}\n{x['output']}" for x in certification)
    frozen = candidate_bundle["output"]
    task_base = f"""
Only analyze candidates that genuinely survive the certification evidence.
Do not treat a proof draft with a GAP as a theorem.

FROZEN CANDIDATES:\n{frozen}\n\nCERTIFICATION REPORTS:\n{cert_text}
""".strip()

    tasks = {
        "abstraction_agent": task_base + "\n\nFind the weakest natural abstract setting in which any surviving result remains rigorously true.",
        "transfer_agent": task_base + "\n\nSeek rigorous non-Riemann applications or independent consequences of any surviving structure.",
        "novelty_auditor": task_base + "\n\nTry to show that any surviving object/theorem is already known, equivalent to a known theorem, or a disguised special case. Be aggressive and specific.",
    }

    results = await asyncio.gather(
        *(run_one(k, tasks[k], target, constitution) for k in GENERALIZATION_KEYS)
    )
    for item in results:
        append_jsonl("runs", item)
    return results


async def run_lab(target: str) -> None:
    ensure_memory()
    constitution = load_constitution()

    inventions = await independent_invention_round(target, constitution)
    bundle = await synthesize_candidates(target, constitution, inventions)
    certification = await certification_round(target, constitution, bundle)
    generalization = await generalization_round(target, constitution, bundle, certification)

    report = {
        "target": target,
        "model": DEFAULT_MODEL,
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
    parser.add_argument("--target", default=DEFAULT_TARGET, help="Precise obstruction to attack")
    args = parser.parse_args()
    asyncio.run(run_lab(args.target))


if __name__ == "__main__":
    main()
