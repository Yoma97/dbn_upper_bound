# Round 73 — Global shoulder improvement to `lambda >= 6.19` using the unconditional `Lambda <= 0.22` reduction

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Truth status:** INTERNALLY_PROVED + 512/768-BIT DIRECTED-ROUNDING CERTIFIED.  
**Referee status:** NOT YET REFEREE_VERIFIED under the project's independent-reconstruction rule.  
**Novelty:** NOVELTY_UNVERIFIED.

---

## 1. Main theorem

Let

\[
\lambda=t\log\frac{|x|}{4\pi}.
\]

Then the project now has a complete internal proof/certificate of

\[
\boxed{
0<t\le\frac12,
\qquad
\lambda\ge6.19
\Longrightarrow
(H_t(x),H_t'(x))\neq(0,0).
}
\tag{73.1}
\]

Thus the internally certified positive-time collision-exclusion shoulder improves from `7.039` (and earlier `7.04`, `7.10`, `10.52`) to

\[
\boxed{C_{\rm project-proved}=6.19.}
\]

This is **not** a proof of RH. The lower shoulder and bounded spatial core remain open.

The key new idea is not a tighter finite-time envelope at `t=1/2`: it is the observation that the published unconditional bound

\[
\Lambda\le0.22
\]

removes every time `t>0.22` from the multiple-zero problem altogether.

---

## 2. Safe external input: the unconditional Polymath upper bound

D.H.J. Polymath proves unconditionally

\[
\boxed{\Lambda\le0.22.}
\tag{73.2}
\]

This is a Tier-A published input in the project source registry. It is much weaker than the target `Lambda<=0` and does not assume RH.

The proof below uses (73.2) only to eliminate the already-real-rooted interior `t>0.22`; the difficult interval `0<t<=0.22` is treated independently by PSC.

---

## 3. Interior simplicity lemma

### Lemma 73.2

For the de Bruijn--Newman heat family, if

\[
t_0>\Lambda,
\]

then every real zero of `H_{t_0}` is simple.

### Proof

Suppose instead that `H_{t_0}` has a real zero `c` of multiplicity `m>=2`. Write locally

\[
H_{t_0}(c+z)
=a z^m+O(z^{m+1}),
\qquad a\neq0.
\tag{73.3}
\]

The heat equation is

\[
\partial_tH_t=-\partial_z^2H_t.
\]

For `epsilon>0`, going backward from `t_0` gives

\[
H_{t_0-\epsilon}
=e^{+\epsilon\partial_z^2}H_{t_0}.
\]

Set `z=sqrt(epsilon) w`. Uniformly on compact `w`-sets,

\[
\frac{H_{t_0-\epsilon}(c+\sqrt\epsilon\,w)}
{a\epsilon^{m/2}}
=
P_m^-(w)+O(\sqrt\epsilon),
\tag{73.4}
\]

where

\[
P_m^-(w):=e^{+\partial_w^2}w^m.
\]

Let

\[
Q_m(w):=e^{-\partial_w^2}w^m.
\]

As established in the all-multiplicity collision analysis, `Q_m` is the monic Hermite collision polynomial and has `m` distinct real zeros. Directly from the coefficient formula,

\[
\boxed{P_m^-(w)=i^{-m}Q_m(iw).}
\tag{73.5}
\]

Hence the zeros of `P_m^-` are `-i` times the real zeros of `Q_m`. For every `m>=2`, at least one zero of `Q_m` is nonzero, so `P_m^-` has a genuinely nonreal zero.

Choose a small disk around such a nonreal simple zero, disjoint from the real axis. By (73.4) and Rouché/Hurwitz, for all sufficiently small `epsilon>0`, `H_{t_0-epsilon}` has a nonreal zero in that disk.

But if `t_0>Lambda`, choose `epsilon` so small that

\[
t_0-\epsilon>\Lambda.
\]

By the defining property of `Lambda`, all zeros of `H_{t_0-epsilon}` are real. Contradiction.

Therefore every zero at `t_0>Lambda` is simple. ∎

### Corollary 73.3

From (73.2),

\[
\boxed{
t>0.22\Longrightarrow(H_t(x),H_t'(x))\neq(0,0)
\quad\text{for every real }x.}
\tag{73.6}
\]

Thus a global positive-time collision-exclusion proof only needs to certify

\[
0<t\le0.22.
\]

The endpoint `t=0.22` is **not** discarded: if `Lambda=0.22`, it could in principle be a threshold collision, so PSC explicitly includes it.

---

## 4. New finite domain

For the new shoulder target it suffices to cover

\[
0<t\le0.22,
\qquad
6.19\le\lambda\le7.04.
\tag{73.7}
\]

The previously certified theorem `lambda>=7.04` handles the rest of the `t<=0.22` shoulder, while Corollary 73.3 handles **all** `lambda` for `t>0.22`.

At the worst geometric corner of (73.7),

\[
L=\log\frac{x}{4\pi}
=\frac\lambda t
\ge\frac{6.19}{0.22}
=\frac{619}{22}
=28.13636\ldots
\tag{73.8}
\]

and therefore

\[
x>2.08\times10^{13}.
\]

The Polymath approximation is extremely accurate here.

---

## 5. Global Polymath error audit

Fix

\[
\rho=0.1.
\]

On the Cauchy disks in (73.7), the cutoff-edge exponent has large enough slack to use

\[
\frac{b_n^t}{n^{\Re s_*}}
\le n^{-1.27},
\]

and after the worst `n^y`, `0<=y<=0.1`,

\[
n^y\frac{b_n^t}{n^{\Re s_*}}
\le n^{-1.17}.
\]

Indeed the asymptotic edge exponent is

\[
\frac12+\frac{6.19}{8}=1.27375,
\]

while all disk corrections at `x>2e13` are vastly smaller than the available `0.00375` slack.

Using only

\[
\zeta(s)\le1+\frac1{s-1},
\qquad s>1,
\]

the 512- and 768-bit directed-rounding endpoint audits independently certify

\[
Z_*\le11.606703703703705,
\]

\[
e_A+e_B
\le7.2420515225931095\times10^{-12},
\]

\[
e_{C,0}
\le1.6509274020979614\times10^{-8},
\]

\[
E_{\rm jump}
\le8.871220157240477\times10^{-8},
\]

and hence

\[
\boxed{
E_0
\le1.0522871764490697\times10^{-7}.
}
\tag{73.9}
\]

For the symmetric normalization, the same Schwarz-conjugation audit as before gives

\[
\left|\frac{B_t}{D_t}\right|
\le e^{0.026L}.
\]

At the endpoint

\[
e^{0.026L}\le2.0782900298006544.
\]

The three error channels times this ratio decrease for `L>=619/22`:

1. `e_A+e_B`: the exponential denominator contributes rate essentially `e^{-L}`; even the loose logarithmic derivative satisfies
   \[
   0.026+2/L-0.99<0;
   \]
2. `e_C0`: after normalization the main linear decay rate is at least
   \[
   \left(\frac14+\frac{6.19}{16}-0.026\right)L
   =0.610875L;
   \]
   the positive correction terms decrease with `L`;
3. the slow cutoff-jump channel behaves no worse than `N^{-1.17}` with `N` growing like `e^{L/2}`, leaving net rate
   \[
   1.17/2-0.026=0.559>0.
   \]

Thus the endpoint product controls the full region, and Cauchy gives

\[
\boxed{
E_1
\le2.1869579473011833\times10^{-6}.
}
\tag{73.10}
\]

The finite PSC grid deliberately uses the vastly weaker padded constants

\[
\boxed{E_0=10^{-3},\qquad E_1=0.02.}
\tag{73.11}
\]

This makes the final certificate insensitive to microscopic error-audit rounding.

Canonical files:

- `research_lab/certificates/low_shoulder/lambda619_error_audit.c`
- `research_lab/certificates/low_shoulder/lambda619_error_512.txt`
- `research_lab/certificates/low_shoulder/lambda619_error_768.txt`

Local source SHA256 used for the run:

`bc2ea71b968e26034f502744e9871aea416617cc128f4f97b98c8cf0983de1b6`.

---

## 6. True-weight finite-head / optimized-tail certificate

The real phase amplitudes are

\[
a_n=
\exp\left(
\frac t4(\log n)^2-\sigma\log n
\right).
\]

The new verifier uses

\[
K=2048.
\]

At the worst corner the Riemann--Siegel cutoff is already greater than `1.287e6`, so the entire finite head `2<=n<=K` is always present.

For a box

\[
t\in[t_a,t_b],
\qquad
\lambda\in[\lambda_a,\lambda_b],
\]

write `u=log n` and use

\[
\sigma\ge\frac12+\frac\lambda4-10^{-10}.
\]

From the moving-cutoff constraint and `n>=K`, the verifier uses the safe padded implication

\[
\lambda\ge\max(\lambda_a,2tu)-2\times10^{-6}.
\tag{73.12}
\]

With

\[
\eta=\frac{2\times10^{-6}}4+10^{-10},
\]

the optimized tail exponent is bounded by the same three branches previously proved:

\[
h_1(u)=
\frac{t_b}{4}u^2-
\left(\frac12+\frac{\lambda_a}{4}-\eta\right)u,
\qquad
u\le u_1:=\frac{\lambda_a}{2t_b},
\]

\[
h_2(u)=
-\left(\frac12+\frac{\lambda_a}{8}-\eta\right)u,
\qquad
u_1\le u\le u_2:=\frac{\lambda_a}{2t_a},
\]

and, for `t_a>0`,

\[
h_3(u)=
-\frac12u-\frac{t_a}{4}u^2+\eta u,
\qquad
u_2\le u\le
u_3:=\frac{\lambda_b+2\times10^{-6}}{2t_a}.
\]

For the first time box `t_a=0`, the `h_2` branch continues to infinity.

The counting-measure exponent in the first branch is convex, so its secant gives a rigorous integral upper bound. The second branch is integrated exactly. The third branch is decreasing at `u_2` because

\[
\frac12+\eta-\frac{\lambda_a}{4}<0,
\]

and is bounded by its left endpoint times the segment length. The logarithmic moment is handled in parallel.

No oscillatory cancellation is used.

---

## 7. Exact finite partition

The time interval `[0,0.22]` is partitioned into exactly 32 boxes:

- `[0,0.18]`: 18 boxes of width `0.01`;
- `[0.18,0.21]`: 6 boxes of width `0.005`;
- `[0.21,0.218]`: 4 boxes of width `0.002`;
- `[0.218,0.22]`: 4 boxes of width `0.0005`.

The lambda interval `[6.19,7.04]` is partitioned into exactly 85 boxes of width `0.01`.

Thus the full rectangle (73.7) consists of

\[
\boxed{32\times85=2720\text{ boxes}.}
\]

All endpoints are rational numbers constructed inside MPFR; no binary floating-point endpoint is used in an acceptance decision.

---

## 8. 512-bit result

The monolithic 512-bit run certifies all 2720 boxes:

```text
PSC lambda [6.19,7.04] t<=0.22 PREC=512 ibox=[0,32) boxes=2720 fail=0
minimum_margin_lower=0.049218384939129022
worst_t=[0.219500,0.220000] lambda=[6.1900,6.2000]
A0_upper=0.82853202750245358 A1_upper=2.3383369555918039
GRID_RESULT pass=1
```

Thus even after padding the analytic errors upward by roughly four orders of magnitude, the weakest box retains

\[
\boxed{0.049218384939129022>0.}
\tag{73.13}
\]

of directed lower PSC margin.

---

## 9. 768-bit independent precision rerun

The same source was compiled at 768 bits and run in four disjoint time-index chunks:

- `[0,8)`: 680 boxes, `fail=0`, minimum margin `12.456560911890461`;
- `[8,16)`: 680 boxes, `fail=0`, minimum margin `3.0034496597067775`;
- `[16,24)`: 680 boxes, `fail=0`, minimum margin `0.30040464591597071`;
- `[24,32)`: 680 boxes, `fail=0`, minimum margin `0.049218384939129022`.

The chunks are disjoint and exhaust all 32 time boxes, hence all 2720 rectangles. The global weakest box and margin agree with the 512-bit run.

Canonical files:

- `research_lab/certificates/low_shoulder/convex_tail_psc_lambda619_mpfr.c`
- `research_lab/certificates/low_shoulder/convex_tail_psc_lambda619_512.txt`
- `research_lab/certificates/low_shoulder/convex_tail_psc_lambda619_768_chunks.txt`

Local source SHA256 used for both precision builds:

`2f3baa98f8c8e289fe6ee7aa270196c2fc4757a8230378c2a6ca861c4164f040`.

---

## 10. Proof cover for Theorem 73.1

The domain is the union of three pieces.

### A. `0<t<=0.22`, `6.19<=lambda<=7.04`

Certified by Sections 5--9.

### B. `0<t<=0.22`, `lambda>=7.04`

Covered by the already certified `lambda>=7.04` shoulder theorem.

### C. `0.22<t<=1/2`, all real `x`

Covered by Corollary 73.3 from the unconditional input `Lambda<=0.22`.

The union proves (73.1).

---

## 11. Circularity audit

The new logical input `Lambda<=0.22` deserves explicit scrutiny.

It is **not** an assumption equivalent to RH. It is an unconditional published upper bound, already much weaker than the desired conclusion `Lambda<=0`. Using a known coarse upper bound to remove the interval strictly above it does not assume the target.

The dependency graph is

`unconditional Polymath Lambda<=0.22`

`+ local heat-collision Hermite splitting`

`-> no multiple zeros for t>0.22`

and independently

`unconditional Polymath effective approximation`

`+ phase-slope transversality`

`+ positive true-weight envelope`

`+ directed-rounding finite arithmetic`

`-> no multiple zeros for 0<t<=0.22, lambda>=6.19`.

Not used:

- RH;
- `Lambda<=0` or `Lambda=0`;
- global real-rootedness at any `t<=0.22`;
- zero-spacing lower bounds;
- pair correlation/GUE;
- generalized Laguerre positivity;
- Rodgers--Tao negative-time estimates derived under a `Lambda<0` contradiction setup.

The Polymath proof of `Lambda<=0.22` contains finite certified numerical ingredients, but that theorem is itself unconditional; finite verification is not being promoted to full RH.

**Circularity verdict:** PASS internally.

---

## 12. Interpretation and next obstruction

The previous finite-time obstruction near `t=1/2`, which pinned the plain PSC near `lambda≈7.04`, is no longer relevant once (73.2) is used. The new weakest point has moved exactly to the new terminal time

\[
t=0.22.
\]

This confirms that the correct next optimization problem is now the PSC boundary at `t=0.22`, not `t=1/2`.

A non-rigorous direct-moment diagnostic places the true pointwise PSC transition near `lambda≈6.1`, while the present `K=2048` box envelope is certified at `6.19`. Therefore some additional constant improvement is still available by enlarging the exact head/refining the terminal boxes, but this is now a secondary quantitative task.

The more important structural frontier remains the fixed-lambda small-time triangle floor

\[
\lambda_*=4.914588956\ldots,
\]

and ultimately the region below it, where a changed certificate is required.

RH remains OPEN.
