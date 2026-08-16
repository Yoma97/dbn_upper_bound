# Round 80 — Current de Bruijn–Newman upper bounds and singular-wedge update

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Purpose:** correct Round 79's published-input cutoff and distinguish peer-reviewed bounds from newer certified-record packages.

---

## 1. Peer-reviewed published upper bound is `Lambda <= 0.20`

Platt–Trudgian, *The Riemann hypothesis is true up to 3 x 10^12* (Bull. London Math. Soc. 53 (2021), 792–797; arXiv:2004.09765), prove rigorously by interval arithmetic that RH holds up to

\[
T=3{,}000{,}175{,}332{,}800.
\]

Their Section 3.4 explicitly applies the Polymath15 criterion and states:

\[
\boxed{\Lambda\le0.20.}
\]

This is Corollary 2 of their paper, not merely an inference made later by the present project.

Therefore Round 79's unrestricted cutoff `0.22` is superseded.

If one admits standard peer-reviewed unconditional computational results, then Craven–Csordas strict heat smoothing gives

\[
\boxed{t>0.20\Longrightarrow H_t\text{ has only simple real zeros}.}
\]

The proof is: choose `Lambda<s<t`; then `H_s in LP` has order one and

\[
H_t=e^{-(t-s)D^2}H_s,
\]

so the strict heat-smoothing theorem yields simple real zeros.

---

## 2. Newer 2026 certified-record bounds

The Tao/Ivanisvili/Davis *Optimization Problems in Mathematics* database currently records two 2026 certificate-package improvements:

\[
\Lambda\le0.1965
\]

and

\[
\boxed{\Lambda\le3/16=0.1875.}
\]

The `0.1875` entry was added by merged pull request `teorth/optimizationproblems#126` on 2026-07-17.

The PR states that the certificate instantiates Polymath15 Theorem 1.2 at

\[
X=6000000185827,
\quad t_0=1680/10^4,
\quad y_0^2=39/1000,
\]

so that

\[
t_0+y_0^2/2=3/16.
\]

Its only RH-height input is the Platt–Trudgian theorem, with exact inequality

\[
X/2=3000000092913.5
\le3000175332800.
\]

The submission claims a self-contained certificate bundle, exact-rational / outward-rounded assembly checking, a 58-check primary verifier, a zero-shared-code second line with 76 checks, and a live independent tail re-proof. The result is explicitly disclosed as fully AI-derived.

The earlier `0.1965` result was added by merged PR `#101` and similarly supplies independent certificate lines.

### Status classification

These must be distinguished from peer-reviewed literature:

- `PEER_REVIEWED_PUBLISHED_BOUND = 0.20`;
- `CERTIFIED_RECORD_DATABASE_BOUND = 0.1875`;
- `INDEPENDENT_PROJECT_REPLAY_OF_0.1875 = NOT_YET_DONE`;
- `REFEREE_VERIFIED_0.1875 = NOT ESTABLISHED BY OUR AUDIT`.

Merging into the Tao-maintained optimization database is meaningful external evidence that the record is considered worthy of tracking, but it is **not itself a substitute for replaying the certificate bundle or journal peer review**. No visible PR discussion/review comments were present in the connector audit of PR #126.

Thus the project should not silently call `0.1875` a peer-reviewed theorem. It is best described as a current certified-record upper bound pending our independent replay.

---

## 3. Strict-track effect

Both `0.20` and `0.1875` depend on finite-height RH verification.

The user's strict proof policy forbids such verification anywhere in the dependency closure. Hence neither number is admissible as the time cutoff on Track S.

Therefore:

\[
\boxed{\text{Track S does not change.}}
\]

The current strict collision certificate remains

\[
\boxed{\lambda\ge6.85\quad(0<t\le1/2)}
\]

from Round 78.

The certified-record improvements are nevertheless highly useful for:

1. understanding the unrestricted state of the art;
2. removing positive-time regions on Track U;
3. comparing our collision certificate against Polymath-style barrier methods;
4. mining the 2026 certificate machinery for reusable interval / tiling ideas.

---

## 4. Unrestricted-track reduction is now sharper

### Peer-reviewed unrestricted track

\[
t>0.20
\quad\Longrightarrow\quad
\text{simple real zeros by strict heat smoothing}.
\]

### Certified-record unrestricted track

If the 2026 `0.1875` certificate package is independently replayed and accepted as an input, then

\[
\boxed{t>0.1875\Longrightarrow\text{simple real zeros}.}
\]

This improves the compact positive-time interval but does **not** change the asymptotic nature of the problem as the target tends to zero.

For any fixed `epsilon>0`, Polymath Theorem 1.5 still makes the large-`x` tail finite/effective on `t>=epsilon`; the only noncompact limit is still

\[
\boxed{t\to0^+,\qquad x=4\pi e^{\lambda/t},\qquad\lambda=O(1).}
\]

---

## 5. Focused literature search for the singular wedge

Searches were run specifically for combinations of:

- de Bruijn–Newman + `t log x`;
- positive-time uniform asymptotics;
- `x = exp(C/t)`;
- small-`t` saddle asymptotics;
- simple zeros / positive-time zero asymptotics;
- literature from 2020–2026.

The search recovered Polymath Theorem 1.3 / Theorem 1.5, Ki–Kim–Lee, Rodgers–Tao, Dobner, Newman–Wu, and unrelated/generalized heat-flow papers. It did **not** locate a later primary-source theorem that directly provides a uniform collision-exclusion or joint `(H_t,H_t')` asymptotic in the double scaling

\[
t\to0^+,
\qquad
\lambda=t\log(x/4\pi)\in K
\]

for a fixed compact `K`.

This is a negative literature-search result, not a proof of absence. The proper statement is:

> No such theorem was found in the focused search performed through 2026-08-16.

Consequently the singular wedge remains a credible genuine research frontier.

---

## 6. What should be mined from the 2026 `0.1875` certificate

Even though it cannot enter Track S because of its RH-height dependency, its *internal techniques* may be reusable if they are logically separable from that dependency.

The PR describes several potentially useful devices:

1. **window tiling in the Riemann–Siegel cutoff** rather than one monolithic sweep;
2. a split at a certified overlapping cutoff;
3. mollified finite-window lower bounds;
4. a cutoff-descent analytic tail certificate;
5. exact-rational assembly gates;
6. zero-shared-code second-line verification;
7. AST/file-read auditing of supposedly independent verifiers.

These are verification-engineering ideas, not RH assumptions. They should be inspected for transfer into the strict low-shoulder code.

The immediate action is therefore to replay / inspect the `0.1875` bundle and extract only lemmas whose proof does not use finite-height RH.

---

## 7. Revised research priorities

### P0 — literature/certificate mining

Independently replay the `0.1875` bundle and classify every certificate leg as:

- RH-height dependent;
- pure Polymath analytic machinery;
- pure interval/tiling infrastructure;
- reusable on Track S.

### P1 — singular-wedge theorem SW-1

Derive a **uniform joint asymptotic** from Polymath Theorem 1.3 in

\[
x=4\pi e^{\lambda/t},
\qquad t\to0^+,
\]

for both normalized value and derivative, with explicit uniform remainder.

### P2 — limiting transversality SW-2

Identify the limiting joint Dirichlet model and prove that its value and derivative cannot vanish simultaneously on the desired lambda interval.

### P3 — certified perturbation

Use validated computation only after SW-1/SW-2 reduce the singular wedge to a compact perturbation problem.

### P4 — resume numerical threshold lowering only if it informs SW-1/SW-2

The `6.83` diagnostics remain useful, but blind continuation of `6.85 -> 6.83 -> ...` is no longer the highest-value activity.

---

## 8. Current status table

| Item | Current status |
|---|---|
| `Lambda >= 0` | PROVED (Rodgers–Tao) |
| `Lambda <= 0.20` | PEER-REVIEWED / PUBLISHED / UNCONDITIONAL |
| `Lambda <= 0.1875` | CERTIFIED-RECORD PACKAGE; merged into Tao-maintained database; independent project replay pending |
| Track-S use of `0.20` or `0.1875` | FORBIDDEN by finite-height-RH dependency rule |
| KKL fixed-positive-time eventual real/simple zeros | PROVED, nonuniform in `t` for our purpose |
| Polymath `x >= exp(C/t)` far-tail control | PROVED, effective |
| uniform bounded-`lambda` joint asymptotic | NOT FOUND IN LITERATURE; OPEN PROJECT TARGET |
| strict project collision-free shoulder | `lambda >= 6.85`, internally 512/768-bit certified |
| RH | OPEN |

---

## 9. Circularity audit

No new strict-track theorem is claimed from the `0.1875` record. Its Platt–Trudgian RH-height input is explicitly quarantined on Track U.

The proposed reuse is limited to analytic or verification sublemmas whose dependency graphs can be independently shown not to require the RH-height input.

**RH remains OPEN.**
