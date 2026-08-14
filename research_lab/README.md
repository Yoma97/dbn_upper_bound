# Mathematical Invention Lab for the Riemann Hypothesis

This directory is an experimental multi-agent research layer. It does **not** modify or replace the original de Bruijn–Newman code.

## Research objective

The lab assumes **no private mathematical progress**. It starts from a dated map of the strongest externally supported RH frontiers, audits that map against live primary literature at the beginning of each run, and then tries to invent, prove, destroy, generalize, and certify genuinely new intermediate mathematics.

The goal is not to keep improving numerical constants or to repeatedly restate criteria equivalent to RH. Preference is given to new bridge theorems that connect two existing partial theories and remove a documented obstruction.

## Baseline files

- `knowledge/frontier_map.md` — dated map of KNOWN / LIMITATION / MISSING-THEOREM targets.
- `knowledge/source_registry.yaml` — source tiers A/B/C/D and provenance rules.
- `prompts/constitution.md` — epistemic, anti-circularity, and invention rules.

The baseline currently covers:

- Levinson–Conrey mollification and the >5/12 critical-line record;
- unconditional pair correlation, horizontal multiplicity, PCC/Essential Simplicity;
- Guth–Maynard zero-density and Dirichlet-polynomial large-value estimates;
- de Bruijn–Newman heat flow and the Lambda bounds;
- Jensen-polynomial / Laguerre–Polya hyperbolicity, including the provisional August-2026 joint wedge;
- cross-frontier bridge targets, especially sparse-exception amplification.

## Source trust policy

- **Tier A:** published/accepted mathematics or official status.
- **Tier B:** serious current preprint; usable as frontier input but crucial dependencies must be reconstructed.
- **Tier C:** very recent/unreviewed preprint or certificate package; idea mining only until independently audited.
- **Tier D:** unverified/unclear-provenance/extraordinary RH claim; never a theorem premise.

A recent upload date is not evidence of mathematical validity.

## Non-negotiable rules

1. Numerical evidence is never a proof.
2. Arb/interval arithmetic may REFUTE a claim, rigorously certify a finite subproblem, or provide evidence; it may never promote a claim to THEOREM by itself.
3. A result cannot be promoted to THEOREM unless a complete proof is supplied and survives independent reconstruction, counterexample attack, dependency audit, and adversarial review.
4. A result cannot be promoted to NEW_TOOL unless it is abstracted beyond the Riemann-specific setting and has rigorous mathematical transfer value.
5. Hidden use of RH, PCC, Essential Simplicity, unrestricted theta=infinity mollification, a narrow-box hypothesis, or another endpoint-strength conjecture invalidates an alleged unconditional proof.
6. `100% of zeros on the line asymptotically` is not RH; a sparse exceptional set may remain.
7. Failed ideas are permanent research assets.
8. Inventors work independently during the first round. Cross-pollination occurs only after proposals are frozen.

## Pipeline

```text
DATED FRONTIER MAP
       |
       v
LIVE FRONTIER CURATOR + WEB SEARCH
  - primary/official sources first
  - output: verified delta only
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
  - Fresh-Context Referee
       |
       v
GENERALIZATION
  - Abstraction Agent
  - Transfer / Application Agent
  - Novelty Auditor (live literature search enabled)
       |
       v
CANDIDATE -> PROPOSITION -> THEOREM -> NEW_TOOL
```

## Current highest-priority invention targets

1. **Sparse-exception amplification / rigidity:** make a rare off-line zero leave a quantitatively unavoidable signature in a statistic that can be controlled.
2. **Horizontal multiplicity:** derive an unconditional bound of the Goldston–Suriajaya form with `C<2`, ideally approaching `C=1`, or invent a better horizontally sensitive statistic.
3. **Zero-density -> pair-correlation bridge:** convert current horizontal tail information into a useful near-pair/horizontal bound without assuming all zeros lie in a `1/log T` box.
4. **de Bruijn–Newman structural endpoint:** invent a non-tautological evolution/positivity mechanism that removes dependence on finite-height RH verification.
5. **Mollifier/variational bridge:** obtain genuinely new arithmetic control rather than merely assuming the theta=infinity endpoint.
6. **Jensen/Laguerre propagation:** reach the low-shift/high-degree frontier via a new propagation theorem, not by restating all Jensen hyperbolicities.

## Status ladder

- `IDEA`: informal mechanism or object.
- `CANDIDATE`: precise statement with hypotheses and claimed consequence.
- `SUPPORTED`: non-proof evidence exists.
- `REFUTED`: counterexample or logical failure found.
- `PROPOSITION`: proof draft exists but has not passed all gates.
- `THEOREM`: complete proof has passed proof reconstruction, circularity audit, counterexample attack, and adversarial review.
- `NEW_TOOL`: theorem/structure is abstracted, nontrivial beyond RH, and demonstrates rigorous transfer value.

## Directory layout

```text
research_lab/
  README.md
  requirements.txt
  config.yaml
  schemas.py
  roles.py
  orchestrator.py
  knowledge/
    frontier_map.md
    source_registry.yaml
  prompts/
    constitution.md
  memory/
    frontier_audits.jsonl
    ideas.jsonl
    candidates.jsonl
    theorems.jsonl
    refuted.jsonl
    dead_ends.jsonl
    runs.jsonl
```

The default orchestrator mission is deliberately not `Prove RH`. It asks for the weakest genuinely new intermediate theorem that improves a documented frontier without hiding the desired conclusion in its hypotheses.
