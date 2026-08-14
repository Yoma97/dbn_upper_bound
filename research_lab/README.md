# Mathematical Invention Lab for the Riemann Hypothesis

This directory is an experimental multi-agent research layer. It does **not** modify or replace the original de Bruijn–Newman code.

## Research objective

The lab is not optimized for numerical approximation or for repeatedly combining known methods. Its primary objective is to invent, test, prove, generalize, and certify genuinely new mathematical objects, identities, invariants, lemmas, and theorems that could close a precise obstruction on a route to RH.

The first target is the unresolved low-shoulder / transversality obstruction in the current de Bruijn–Newman heat-flow program. The orchestrator may change the target only when it records a precise reason.

## Non-negotiable rules

1. Numerical evidence is never a proof.
2. Arb/interval arithmetic may REFUTE a claim, rigorously certify a finite subproblem, or provide evidence; it may never promote a claim to THEOREM by itself.
3. A result cannot be promoted to THEOREM unless a complete proof is supplied and survives independent reconstruction and adversarial review.
4. A result cannot be promoted to NEW_TOOL unless it is abstracted beyond the Riemann-specific setting and has at least one mathematically independent application or a rigorous general theorem explaining its scope.
5. Every proof dependency must be explicit. Hidden use of RH, an equivalent conjecture, or the desired conclusion invalidates the proof.
6. Failed ideas are permanent research assets. They are recorded so future agents do not rediscover the same dead end without a materially new hypothesis or mechanism.
7. Inventors work independently during the first round. Cross-pollination occurs only after independent proposals are frozen.

## Pipeline

```text
TARGET / OBSTRUCTION
       |
       v
INDEPENDENT INVENTION
  - Obstruction Analyst
  - Object Inventor
  - Identity / Invariant Hunter
  - Bridge Builder
  - Definition Inventor
       |
       v
CANDIDATE SYNTHESIS
       |
       v
CERTIFICATION
  - Proof Architect
  - Counterexample Destroyer
  - Equivalence / Circularity Auditor
  - Independent Referee
       |
       v
GENERALIZATION
  - Abstraction Agent
  - Transfer / Application Agent
  - Novelty Auditor
       |
       v
CANDIDATE -> PROPOSITION -> THEOREM -> NEW_TOOL
```

## Status ladder

- `IDEA`: informal mechanism or object.
- `CANDIDATE`: precise statement with hypotheses and claimed consequence.
- `SUPPORTED`: non-proof evidence exists.
- `REFUTED`: counterexample or logical failure found.
- `PROPOSITION`: proof draft exists but has not passed all gates.
- `THEOREM`: complete proof has passed proof reconstruction, circularity audit, and adversarial review.
- `NEW_TOOL`: theorem/structure is abstracted, nontrivial beyond RH, and demonstrates transfer value.

## Directory layout

```text
research_lab/
  README.md
  requirements.txt
  config.yaml
  schemas.py
  agents.py
  orchestrator.py
  prompts/
    constitution.md
  memory/
    ideas.jsonl
    candidates.jsonl
    theorems.jsonl
    refuted.jsonl
    dead_ends.jsonl
```

## First research mission

The initial orchestrator prompt is deliberately not simply `Prove RH`.

It asks for the weakest new structural theorem that would eliminate the currently unresolved low-shoulder obstruction without hiding RH in its hypotheses, with special preference for:

- a new monotone or conserved functional under the heat flow;
- a structural non-collision principle;
- an exact identity replacing a fragile asymptotic inequality;
- a new bridge between zero dynamics and real-entire-function / correlation structure;
- a general theorem whose Riemann application is a corollary.

A proposed theorem is valuable only if it comes with a plausible route to proof and survives the certification pipeline.
