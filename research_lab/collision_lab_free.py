from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MEMORY = ROOT / "memory"
PROGRAM = ROOT / "knowledge" / "unified_collision_geometry_program.md"
FRONTIER = ROOT / "knowledge" / "frontier_map.md"
MODEL = os.getenv("GITHUB_MODELS_MODEL", "openai/gpt-4.1-mini")
ENDPOINT = "https://models.github.ai/inference/chat/completions"
TOKEN = os.environ["GITHUB_TOKEN"]

PRIMARY = {
    "collision_unifier": "Re-derive the finite heat-polynomial unification of discriminant, inverse-square gap trace, phase/Laguerre current, and topological collision index. State exact identities, hypotheses, and the first obstruction to infinite-dimensional lifting.",
    "regularization_architect": "Attempt a canonical relative/regularized collision functional for the Riemann de Bruijn-Newman heat family. Prioritize collision locality, cutoff independence, and Hadamard compatibility. If impossible, give a precise obstruction or counterexample.",
    "phase_current_analyst": "Analyze phase/transversality currents without merely renaming L1. Seek a kernel-side weighted-integrated sign mechanism special enough to be independently testable. Reject circular formulations.",
    "gap_trace_analyst": "Construct or refute a cutoff-independent regularized inverse-square gap trace linked to a logarithmic derivative of a relative collision functional. Audit tail-core cancellation rigorously.",
    "collision_flux_analyst": "Develop the topological collision-charge picture. Derive the correct continuity/source equation for (H,H') zeros under backward heat flow. Determine what extra Riemann-kernel input would be needed for a no-creation law.",
}

AUDITS = {
    "destroyer": "Attack the synthesized candidate with finite heat-polynomial counterexamples, multiplicity, tail perturbations, renormalization dependence, and generic entire-function countermodels. Return REFUTED if one decisive counterexample survives.",
    "circularity_auditor": "Audit for hidden RH, Laguerre-Polya, Weil/Li, de Bruijn-Newman endpoint, or real-rootedness assumptions. Separate genuinely independent hypotheses from equivalent restatements.",
    "legitimacy_auditor": "Audit well-definedness, domains, convergence, normalization dependence, collision locality, cutoff independence, and whether each claimed identity survives the finite-model limit.",
}


def read(path: Path, cap: int = 22000) -> str:
    text = path.read_text(encoding="utf-8")
    return text[:cap]


def call_model(system: str, user: str, max_tokens: int = 2400) -> str:
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "temperature": 0.2,
        "max_tokens": max_tokens,
    }
    req = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            data = json.loads(r.read().decode("utf-8"))
        return data["choices"][0]["message"]["content"]
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub Models request failed: HTTP {e.code}: {body}") from e


def append_jsonl(name: str, obj: dict) -> None:
    MEMORY.mkdir(parents=True, exist_ok=True)
    with (MEMORY / name).open("a", encoding="utf-8") as f:
        f.write(json.dumps(obj, ensure_ascii=False) + "\n")


def main() -> None:
    program = read(PROGRAM)
    frontier = read(FRONTIER, cap=12000)
    constitution = (
        "You are doing hostile, professor-level mathematical research on an open problem. "
        "Never claim RH is proved. Distinguish PROVED, CONDITIONAL, CANDIDATE, REFUTED. "
        "Do not invent convergence, positivity, or regularization facts. Every new object must have a domain, normalization, and fastest falsification test."
    )
    context = f"UNIFIED COLLISION GEOMETRY PROGRAM:\n{program}\n\nFRONTIER EXCERPT:\n{frontier}"

    primary_results = []
    for key, task in PRIMARY.items():
        out = call_model(constitution, context + "\n\nYOUR ROLE:\n" + task)
        item = {"agent": key, "model": MODEL, "output": out}
        primary_results.append(item)
        append_jsonl("collision_free_ideas.jsonl", item)
        time.sleep(4)

    synthesis_prompt = (
        context
        + "\n\nFROZEN INDEPENDENT REPORTS:\n"
        + "\n\n".join(f"## {x['agent']}\n{x['output']}" for x in primary_results)
        + "\n\nSynthesize at most TWO candidates. Require a concrete mathematical object, exact first identity, unresolved gap, and fastest falsification. "
          "Do not reward verbal unification. If nothing passes, say NO SURVIVING CANDIDATE."
    )
    synthesis = call_model(constitution, synthesis_prompt, max_tokens=3000)
    append_jsonl("collision_free_candidates.jsonl", {"agent": "synthesizer", "model": MODEL, "output": synthesis})
    time.sleep(4)

    audit_results = []
    for key, task in AUDITS.items():
        out = call_model(
            constitution,
            context + "\n\nFROZEN SYNTHESIS:\n" + synthesis + "\n\nAUDIT ROLE:\n" + task,
            max_tokens=2200,
        )
        item = {"agent": key, "model": MODEL, "output": out}
        audit_results.append(item)
        append_jsonl("collision_free_audits.jsonl", item)
        time.sleep(4)

    final_prompt = (
        context
        + "\n\nSYNTHESIS:\n" + synthesis
        + "\n\nAUDITS:\n"
        + "\n\n".join(f"## {x['agent']}\n{x['output']}" for x in audit_results)
        + "\n\nReturn a final research verdict with exactly these sections: PROVED TOOLS, REFUTED IDEAS, SURVIVING CANDIDATE, SMALLEST NEXT LEMMA, CIRCULARITY STATUS, RH STATUS. "
          "If any gate fails, explicitly downgrade the candidate."
    )
    verdict = call_model(constitution, final_prompt, max_tokens=3000)
    report = {
        "mode": "FREE_ONLY_GITHUB_MODELS",
        "model": MODEL,
        "primary": primary_results,
        "synthesis": synthesis,
        "audits": audit_results,
        "verdict": verdict,
    }
    Path("collision_lab_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()
