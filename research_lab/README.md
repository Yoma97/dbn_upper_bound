# Mathematical Invention Lab for the Riemann Hypothesis

This directory is an experimental multi-agent research layer. It does **not** modify or replace the original de Bruijn–Newman code.

## Current default

Use:

```bash
python research_lab/orchestrator_v3.py
```

`orchestrator_v3.py` is the strict workflow. The older `orchestrator.py` and `orchestrator_v2.py` are retained only as development history.

V3 adds:

- role-specific GPT-5.6 Sol reasoning effort (`high/xhigh/max`);
- structured Pydantic claim/audit outputs;
- frozen atomic claims;
- One-New-Lemma Rule and zero-gap theorem promotion;
- falsification before proof reconstruction;
- two independent proof reconstructors that never see the author's proof;
- a canonical convention lock;
- explicit separation of correctness, novelty and RH relevance;
- structured numerical-verification requests;
- a strict Arb capability gate that refuses silent fallback to ordinary floating point.

## Research objective

The lab assumes **no private mathematical progress**. It starts from a dated map of the strongest externally supported RH frontiers, audits that map against live primary literature at the beginning of each run, and then tries to invent, prove, destroy, generalize, and certify genuinely new intermediate mathematics.

The goal is not to keep improving numerical constants or repeatedly restate criteria equivalent to RH. Preference is given to the **smallest single non-circular missing theorem** or a genuinely new reusable mathematical structure that removes one documented obstruction.

## Baseline and governance files

- `knowledge/frontier_map.md` — dated KNOWN / LIMITATION / MISSING-THEOREM map.
- `knowledge/source_registry.yaml` — source tiers A/B/C/D and provenance rules.
- `prompts/constitution.md` — epistemic, anti-circularity and invention rules.
- `knowledge/mathematical_invention_charter.md` — rules for creating legitimate new mathematics.
- `knowledge/research_hygiene_protocol.md` — atomic claims, dependency DAGs, independent reconstruction and dead-end rules.
- `knowledge/convention_lock.md` — canonical xi/H_t/Fourier/Laguerre normalization.
- `knowledge/arb_verification_protocol.md` — rigorous numerical evidence classes and allowed roles.
- `model_policy.py` — role-specific reasoning policy.
- `structured_outputs.py` — mandatory structured claim/audit schemas.
- `arb_verification.py` — capability registry and rigorous numerical-job gate.

## Source trust policy

- **Tier A:** published/accepted mathematics or official status.
- **Tier B:** serious current preprint; usable as frontier input but crucial dependencies must be reconstructed.
- **Tier C:** very recent/unreviewed preprint or certificate package; idea mining only until independently audited.
- **Tier D:** unverified/unclear-provenance/extraordinary RH claim; never a theorem premise.

A recent upload date is not evidence of mathematical validity.

## Non-negotiable rules

1. Numerical evidence is never an infinite proof.
2. A live implication chain may contain at most **one genuinely new unproved lemma**. Multi-gap chains are diagnostic only.
3. Arb may refute a universal claim with one rigorous counterexample, certify a finite subproblem, or participate in a theorem only after an independently proved analytic reduction to finitely many cases.
4. Missing Arb capability must be reported as `ARB_CAPABILITY_MISSING`; ordinary floating point may not silently substitute for certification.
5. A theorem cannot be promoted unless it has no unresolved gap and survives two independent proof reconstructions, hostile counterexample attack, dependency/circularity audit, convention audit and fresh-context referee review.
6. Correctness, novelty and RH relevance are separate labels.
7. Hidden use of RH, PCC, Essential Simplicity, unrestricted theta=infinity mollification, narrow-box assumptions or endpoint-equivalent criteria invalidates an alleged unconditional proof.
8. `100% of zeros on the critical line asymptotically` is not RH; a sparse exceptional set may remain.
9. Failed ideas are permanent research assets. A repaired claim receives a new identity and must state the exact mathematical delta.
10. Inventors work independently before proposals are frozen.

## Strict V3 pipeline

```text
DATED FRONTIER + LIVE PRIMARY-SOURCE AUDIT
                 |
                 v
BLIND INDEPENDENT INVENTION
  high/xhigh reasoning
  <= 3 atomic claims per role
                 |
                 v
STRICT SYNTHESIS
  one-new-lemma / multi-gap rejection
                 |
                 v
FROZEN CLAIM
                 |
                 +--------------------------+
                 |                          |
                 v                          v
ADVERSARIAL AUDITS                    ARB JOB GATE
  Destroyer                           rigorous capabilities only
  Equivalence auditor                no float fallback
  Legitimacy auditor
  Exclusion-completeness auditor
  Fresh referee
  max reasoning
                 |
                 v
TWO BLIND PROOF RECONSTRUCTIONS
  author proof hidden
  max reasoning
                 |
                 v
ONLY THEN: promotion/generalization/novelty audit
```

## Arb status

The currently exposed Arb_Riemann_Lab surface is limited to:

- rigorous `sqrt` enclosure;
- rigorous `zeta(s)` enclosure;
- rigorous indexed zeta-zero enclosure.

The program is prepared for, but does **not pretend to already have**, future endpoints for `xi`, derivatives, `H_t`, Laguerre expressions, interval integration/extrema, interval matrix inertia and interval-Newton isolation. The required contract is documented in `knowledge/arb_verification_protocol.md`.

## Status discipline

A result may be mathematically correct while novelty remains unverified. Likewise, an RH-equivalent reformulation may be correct but still be classified only as `REFORMULATION_ONLY` or `DIAGNOSTIC_TOOL`. New mathematics is promoted only after rigorous proof, independent reconstruction, adversarial survival, abstraction and non-RH transfer.
