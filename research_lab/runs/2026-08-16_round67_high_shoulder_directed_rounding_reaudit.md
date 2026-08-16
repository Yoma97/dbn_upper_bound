# Round 67 — Hostile directed-rounding re-audit of the lambda=10.52 theorem

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Final theorem status:** PROJECT-PROVED after corrected 512/768-bit rerun.  
**Novelty:** not at issue; this round is a proof-hygiene audit.

---

## 1. Object under attack

The project theorem under review is

\[
0<t\le\frac12,
\qquad
\lambda=t\log\frac{|x|}{4\pi}\ge10.52
\Longrightarrow
(H_t(x),H_t'(x))\neq(0,0).
\tag{67.1}
\]

The analytic proof uses the unconditional Polymath Theorem 1.3 / Corollary 6.5 plus the phase-slope transversality certificate.

The purpose of this round is not to improve the constant. It is to attack the finite directed-rounding layer itself.

---

## 2. Defects found in the first imported scalar artifact

The first scalar MPFR file was numerically extremely high precision, but two operations did not literally respect the direction asserted by their labels.

### Defect A — pi direction in `x0 lower`

The code constructed

\[
x_0=4\pi e^{21.04}
\]

using `pi` rounded upward while printing the result as `x0 lower`.

For a lower bound on `x0`, every positive multiplicative factor must be enclosed downward. Therefore this was a formal proof-artifact defect.

### Defect B — log direction in the jump exponent

For

\[
N^{-p}=e^{-p\log N},
\]

the old code reused `log N` rounded upward in a context where a lower enclosure of `p log N` is required before negation to obtain an upper exponent.

Again, the numerical difference was at MPFR-ulp scale, but the directional logic was not literal.

---

## 3. Defect found in the first imported Dirichlet-moment helper

The old positive-moment verifier computed `log n` upward and then multiplied by a downward enclosure of `p`, treating the result as if it were automatically a downward enclosure of `p log n`.

For positive quantities, multiplying one lower and one upper enclosure does not in general give the required lower product. Therefore the upper bound for

\[
n^{-p}=e^{-p\log n}
\]

was not formally certified by that implementation.

This defect also occurred far below the displayed decimal precision, but a proof certificate is judged by direction correctness, not by the expectation that the error is tiny.

---

## 4. Corrected scalar implementation

The canonical source is now

`research_lab/certificates/high_shoulder/high_shoulder_lambda1052_audit.c`.

It uses separate variables

- `piL, piU`;
- `Llo, Lhi`;
- `rhoL, rhoU`;
- `lnNlo, lnNhi`;
- `pL`.

The monotonicity of each formula determines which endpoint is used.

Examples:

1. `x0 lower` uses `piL` and `Llo`.
2. the denominator `x0-rho-6.66` uses lower `x0` and upper subtracted quantities.
3. `eAB` uses upper `L^2` and lower denominator.
4. the negative main exponent in `eC0` uses lower positive coefficient and lower `L` before negation.
5. the jump factor `N^{-p}` uses downward `log N` and downward `p`; the factor `N^rho` uses upward `log N` and upward `rho`.
6. the Cauchy division by `rho` uses `rhoL` for an upper quotient.

The positive moment constants are deliberately padded upward to

\[
A_0\le0.861634073,
\qquad
A_1\le1.44477381.
\tag{67.2}
\]

---

## 5. Corrected positive-moment implementation

The canonical source is now

`research_lab/certificates/high_shoulder/dirichlet_tail_moments_mpfr_512.c`.

For each positive integer `n`, it computes

\[
\log n\in[\ell_-,\ell_+]
\]

with separate directed calls. Then

\[
p_-\ell_-
\le p\log n,
\]

so

\[
-p\log n
\le -p_-\ell_-,
\]

and exponentiation upward yields a valid upper bound for `n^{-p}`.

For the logarithmic moment, this weight upper bound is multiplied by `ell_+`.

The integral tail also tracks the sign of `1-p<0`: the upper exponent `(1-p) log M` uses the upper coefficient `1-p_-` and the lower positive logarithm.

---

## 6. Fresh 512/768-bit reruns

The corrected moment verifier was compiled independently at 512 and 768 bits and run with

\[
p=1.814,
\qquad M=100000.
\]

Both return

\[
\boxed{
A_0\le0.86163407260348712,
\qquad
A_1\le1.4447738087713327.
}
\tag{67.3}
\]

which validates the padded values (67.2).

The corrected scalar theorem audit was then compiled and rerun at both precisions.

Both return the same outward-projected values

\[
E_0\le2.7089645820749954\times10^{-8},
\]

\[
E_1\le4.6814434358897312\times10^{-7},
\]

\[
Y\ge0.13836592699999933,
\]

\[
\text{PSC lower side}
\ge0.0051788758799930388,
\]

and therefore

\[
\boxed{
\text{final contradiction margin}
\ge0.0051784077356494497>0.
}
\tag{67.4}
\]

Both runs end with

`AUDIT_RESULT pass=1`.

---

## 7. Effect on the theorem

The first imported finite artifacts are **superseded** and must not be cited as canonical proof executables.

However, the mathematical theorem (67.1) survives the hostile audit with essentially unchanged slack. The corrected artifacts provide a literal directed-rounding certificate.

Therefore

\[
\boxed{C_{\rm proved}=10.52}
\]

is restored/retained.

The correction changes proof hygiene, not the theorem constant.

---

## 8. Independent diagnostic remains stronger

The separate actual-weight boundary interval regression at

\[
t=1/2,
\qquad
x\approx4\pi e^{21.04}
\]

still gives

\[
A_0\le0.20955042280644084,
\quad
A_1\le0.22794011633558037,
\]

with phase margin

\[
\ge8.0875893307159448.
\]

It is not needed to repair the theorem, but it remains the quantitative evidence that the global edge-power majorant is the major source of slack.

---

## 9. Circularity audit

The corrected re-audit uses only

- unconditional Polymath Theorem 1.3 / Corollary 6.5;
- elementary positive-series inequalities;
- Cauchy's estimate;
- phase-slope transversality algebra;
- MPFR directed rounding.

Not used:

- RH;
- `Lambda<=0` or `Lambda=0`;
- finite-height RH verification;
- all-real zeros of `H_0`;
- GUE/pair correlation;
- Rodgers--Tao negative-time estimates;
- a zero-motion ODE requiring prior simplicity.

Thus the corrected theorem is non-circular.

---

## 10. Reproducibility hashes

The exact local files compiled and rerun before commit had SHA256:

- scalar source: `f803397faa88e440783e1bd337ec12e2e9556059c1a2fe651b86cf61d304aabe`
- scalar 512 output: `de8a5eb160fa9bc6bc973a95bfa6d276cca9bdb50c660e0d91c384e03d5b0ced`
- scalar 768 output: `337d00903510f79a3b78b9d8f731b8360452e06498361b4a6a904b15c42da843`
- moment source: `f4bf65388b01c6544f5d87b93f13d3f46cf8f4a353c97fff495e32a1c698e1ef`
- moment 512 output: `e1be5739f4eb68d1dd5b0289d5ca82831781b1907123fe78357b1ec6d4fe1e64`
- moment 768 output: `7ebfd97247829a73eeeb49d2e2429508ca2a10d09647a90435f94f95375ac46d`

---

## 11. Research consequence

The high-shoulder foundation is now cleaner than before the attack. The next threshold-improvement work should use Round 66's exact-head / convex-secant true-weight tail rather than shaving constants from the repaired `n^-1.814` proof.

The exploratory target `lambda=7.10` remains **UNPROVED** until a complete 512/768-bit global `(t,lambda)` cover is produced.
