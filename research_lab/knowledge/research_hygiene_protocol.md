# Strict Research Hygiene Protocol v2

These rules are mandatory for every research round.

## 1. Atomic Claim Rule
One claim card = one mathematically atomic statement. Do not bundle several new lemmas into one candidate.

Every statement must expose:
- all quantifiers;
- domain/codomain;
- parameter ranges;
- regularity assumptions;
- normalization/convention;
- exact conclusion.

Ambiguous phrases such as “for large x”, “small t”, “controlled”, “generic”, “typically”, or “negligible” are forbidden unless quantified.

## 2. One-New-Lemma Rule
A live proof route may contain at most one genuinely new unproved mathematical lemma at a time.

If

    known => NEW_A => NEW_B => target,

then NEW_B may not be researched as though NEW_A were available. Prove or refute NEW_A first.

This rule prevents fake progress produced by stacking several plausible conjectures.

## 3. Zero-Gap Rule
A result may be marked INTERNALLY_PROVED only if unresolved_gaps is empty.

A phrase such as “it remains to justify...” means the result is not proved.

## 4. Correctness, Novelty, and Relevance Are Separate Axes
Never use one label to represent all three.

A claim may be:
- mathematically correct but already known;
- new-looking but unproved;
- correct and new but irrelevant to RH;
- equivalent to RH but diagnostically useful;
- a genuine intermediate theorem.

Never call a claim “new theorem” before both correctness and literature novelty have been independently audited.

## 5. Frozen-Claim Rule
Before certification, freeze:
- statement;
- definitions;
- hypotheses;
- conventions;
- allowed dependencies.

Verifiers audit the frozen object. They may not silently strengthen hypotheses or change definitions.

A repaired claim receives a new claim_id and a `repair_delta_from_parent` explaining exactly what changed mathematically.

## 6. Independent Reconstruction Rule
For theorem-level promotion require two independent proof reconstructions.

Each reconstructor receives only:
- frozen statement;
- definitions;
- conventions;
- allowed established dependencies.

They do NOT receive the author's proof text or invention transcript.

Agreement between the two reconstructions is evidence of reproducibility; disagreement blocks promotion.

## 7. Assumption Ledger
Every proof card lists every non-elementary assumption/dependency and marks it as:
- established theorem with source and exact hypotheses;
- proved earlier in this project;
- computational finite certificate;
- conjectural/unproved.

Any conjectural item in a proof chain is a GAP.

## 8. Dependency DAG
Represent each implication as an edge.

No edge may be labelled merely “standard”, “clearly”, “similarly”, or “by known theory” if it carries substantive content.

For each edge record the exact theorem/identity used.

## 9. Endpoint-Strength Audit
For every proposed missing theorem T, ask:
- Does T imply RH almost immediately?
- Is T known to be equivalent to RH, Li positivity, Weil positivity, LP membership, Lambda=0, full Jensen hyperbolicity, PCC/ES, or unrestricted mollifier strength?
- Does its negation encode an off-line zero directly?

If yes, mark `REFORMULATION_ONLY` unless an independent proof mechanism for T is supplied.

## 10. Edge-Case Matrix
Before proof development, attack every claim on the smallest relevant models:
- degree 2, 3, 4 polynomial heat flows;
- even and odd multiple-zero collisions;
- Gaussian and Hermite models;
- real-rooted and non-real-rooted entire/polynomial examples;
- symmetry-preserving fake-xi models;
- t -> 0 and first-crossing limits;
- high-height / x -> infinity limits;
- endpoint parameters;
- sparse exceptions;
- cancellation among symmetry partners;
- rescaling and normalization changes.

A counterexample kills or repairs the claim before long proof attempts begin.

## 11. Exact-vs-Asymptotic Separation
Do not mix exact identities with asymptotic approximations in the same equality chain.

Every approximation must carry an explicit remainder and uniformity regime.

## 12. Convention Lock
Use `knowledge/convention_lock.md`. Any departure requires an explicit conversion map checked algebraically.

## 13. Numerical Role
Numerics may:
- falsify conjectures;
- discover patterns;
- certify finite subproblems rigorously;
- independently sanity-check identities.

Numerics may not:
- prove an infinite/global statement by sampling;
- replace a uniform tail estimate;
- promote a claim to theorem status.

## 14. Source Discipline
For each imported theorem store:
- authors/title;
- exact theorem or proposition identifier if available;
- precise hypotheses used;
- publication/preprint status and date;
- source tier.

Use primary sources whenever possible. Recent preprints may inspire research, but crucial imported lemmas must be reconstructed before theorem promotion.

## 15. Failure Memory
Every refuted route is stored with:
- frozen statement;
- exact counterexample or failed edge;
- conditions under which it might be repairable.

Agents may not reopen it without a material mathematical delta.

## 16. Minimal Missing Theorem Rule
After every round ask:

> What is the smallest single new theorem that remains between established mathematics and the next certified frontier advance?

Prefer proving that theorem over constructing a longer RH-shaped chain.

## 17. Generality Test
A genuinely new mathematical tool should be defined on a natural class broader than xi whenever possible and should support at least one theorem not equivalent to RH.

If xi-specific arithmetic structure is essential, state exactly why.

## 18. Language Discipline
Use only these epistemic labels:
- `PROVED`: complete proof with zero gaps in the current logical system;
- `KNOWN`: established in cited literature;
- `CANDIDATE`: precise but unproved;
- `CONJECTURE`: evidence/heuristic only;
- `REFUTED`: explicit failure/counterexample;
- `NOVELTY_UNVERIFIED`: correctness may be established but literature novelty is not.

Never use “essentially proved”, “almost theorem”, or “verified” ambiguously.
