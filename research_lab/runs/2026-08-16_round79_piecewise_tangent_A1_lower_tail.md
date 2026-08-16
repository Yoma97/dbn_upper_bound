# Round 79 — Piecewise-tangent lower tail for the favorable `A1` moment

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Truth status:** INTERNALLY_PROVED.  
**Novelty:** NOVELTY_UNVERIFIED.  
**Role:** Replaces the `O(K)` large favorable APVC head by a small exact head plus a rigorous closed-form lower tail. This is intended for the near-frontier secant-APVC regime.

---

## 1. Problem

Round 74/75 turns part of

\[
A_1=\sum_{n=2}^N a_n\log n
\]

into a **favorable lower-bound term**. The first implementation therefore used a directed finite head

\[
A_{1,L}^{(K)}
=
\sum_{n=2}^K a_{n,L}\log n.
\]

Near `t=1/2`, `lambda≈6.8`, the cutoff is only of order `10^3`, so a large choice such as `K=900` is possible but computationally expensive inside a heavily subdivided 512/768-bit box proof.

The positive heat exponent has extra structure that gives a nearly sharp lower tail in closed form.

---

## 2. Box lower amplitude

Consider a parameter box on which

\[
t\ge t_-,
\qquad
\sigma\le\sigma_+.
\]

Since

\[
a_n
=
\exp\left(\frac t4\log^2n-\sigma\log n\right),
\]

we have for every `n>=2`

\[
\boxed{
a_n\ge
f_-(n):=
\exp\left(
\frac{t_-}{4}\log^2n-\sigma_+\log n
\right).
}
\tag{79.1}
\]

Let `M` be any integer guaranteed to satisfy

\[
M\le N
\]

throughout the whole box.

Then for every `K<M`,

\[
A_1
\ge
\sum_{n=2}^K f_-(n)\log n
+
\sum_{n=K+1}^M f_-(n)\log n.
\tag{79.2}
\]

The first sum is a small directed finite head. We now bound the second sum from below without enumerating it.

---

## 3. Decreasing-sum to integral lower bound

Put

\[
h(u)=
(\log u)
\exp\left(
\frac{t_-}{4}\log^2u-\sigma_+\log u
\right).
\tag{79.3}
\]

Writing `v=log u`,

\[
\frac{d}{dv}\log h(e^v)
=
\frac1v+rac{t_-}{2}v-\sigma_+.
\tag{79.4}
\]

Assume

\[
\boxed{
\frac1v+rac{t_-}{2}v-\sigma_+<0
\quad
\text{for }
\log(K+1)\le v\le\log(M+1).
}
\tag{79.5}
\]

Then `h` is decreasing throughout the tail. Hence, for every integer `n`,

\[
h(n)\ge\int_n^{n+1}h(u)\,du,
\]

and therefore

\[
\boxed{
\sum_{n=K+1}^M h(n)
\ge
\int_{K+1}^{M+1}h(u)\,du.
}
\tag{79.6}
\]

---

## 4. Convex quadratic after logarithmic coordinates

With `u=e^v`, `du=e^v dv`, the integral becomes

\[
\int_{v_0}^{v_1}v e^{g(v)}\,dv,
\tag{79.7}
\]

where

\[
v_0=\log(K+1),
\qquad
v_1=\log(M+1),
\]

and

\[
\boxed{
g(v)=av^2-bv,
\qquad
a=\frac{t_-}{4},
\qquad b=\sigma_+-1.}
\tag{79.8}
\]

The key fact is

\[
g''(v)=2a=\frac{t_-}{2}>0.
\]

For any tangent point `r`,

\[
\ell_r(v)=g(r)+g'(r)(v-r)
=(2ar-b)v-ar^2.
\tag{79.9}
\]

Because `g` is quadratic, the tangent defect is **exactly**

\[
\boxed{
g(v)-\ell_r(v)=a(v-r)^2.}
\tag{79.10}
\]

In particular,

\[
e^{g(v)}\ge e^{\ell_r(v)}.
\]

---

## 5. Closed-form one-segment lower tail

For an interval `[A,B] subset [v0,v1]`, choose any `r in [A,B]` and set

\[
m=2ar-b.
\]

Then

\[
\int_A^B v e^{g(v)}\,dv
\ge
 e^{-ar^2}
\int_A^B v e^{mv}\,dv.
\tag{79.11}
\]

For `m!=0`, define

\[
\mathfrak L_1(m;A,B)
=
\frac{e^{mB}(mB-1)-e^{mA}(mA-1)}{m^2}.
\tag{79.12}
\]

For `m=0`, use the continuous value

\[
\mathfrak L_1(0;A,B)=\frac{B^2-A^2}{2}.
\tag{79.13}
\]

Thus

\[
\boxed{
\int_A^B v e^{g(v)}\,dv
\ge
 e^{-ar^2}\mathfrak L_1(m;A,B).
}
\tag{79.14}
\]

---

## 6. Piecewise-midpoint tangent theorem

Partition

\[
v_0=v^{(0)}<v^{(1)}<\cdots<v^{(J)}=v_1.
\]

On segment `j` choose the midpoint

\[
r_j=\frac{v^{(j)}+v^{(j+1)}}2.
\]

Set

\[
m_j=2ar_j-b.
\]

Combining (79.2), (79.6), and (79.14) gives:

### Theorem 79.1 — favorable `A1` lower certificate

Under (79.5),

\[
\boxed{
A_1
\ge
A_{1,L}^{\rm head}(K)
+
\sum_{j=0}^{J-1}
 e^{-ar_j^2}
\mathfrak L_1
\left(
 m_j;
 v^{(j)},v^{(j+1)}
\right),
}
\tag{79.15}
\]

where

\[
A_{1,L}^{\rm head}(K)
=
\sum_{n=2}^K
f_-(n)\log n.
\tag{79.16}
\]

Every term is positive and evaluable by directed rounding in `O(K+J)` operations, independently of the magnitude of the guaranteed cutoff `M`.

---

## 7. Quantified tangent loss

On a segment of logarithmic width

\[
\Delta_j=v^{(j+1)}-v^{(j)},
\]

the midpoint satisfies

\[
|v-r_j|\le\Delta_j/2.
\]

By the exact defect (79.10),

\[
0\le g(v)-\ell_{r_j}(v)
\le
\frac{a\Delta_j^2}{4}.
\]

Therefore the tangent exponential retains at least the fraction

\[
\boxed{
\exp\left(-\frac{a\Delta_j^2}{4}ight)
}
\tag{79.17}
\]

of the continuous lower-amplitude integrand on that segment.

For equal logarithmic segments, the worst tangent loss therefore decays quadratically in `1/J` without requiring any higher derivative bound; it is exact for the quadratic heat exponent.

---

## 8. Near-frontier efficiency diagnostic — not part of the proof

At the representative point

\[
t=1/2,
\qquad
\lambda=6.82,
\]

and with a guaranteed tail ending near `M=900`, ordinary high-precision evaluation gives the following approximate recovery fractions relative to the direct positive sum through `M`:

- `K=64`, `J=4`: about `99.71%`;
- `K=64`, `J=8`: about `99.87%`;
- `K=128`, `J=4`: about `99.87%`;
- `K=128`, `J=8`: about `99.94%`.

These percentages are **diagnostic only**. They demonstrate why the theorem is useful computationally but are not used as proof constants.

---

## 9. Why this matters mathematically

The old implementation faced a false tradeoff:

- small `K`: fast but loses the favorable `A1` term;
- large `K`: sharp but expensive in every subdivision box.

Round 79 removes this tradeoff. It uses only positivity, monotonicity, and the exact quadratic structure of the heat weight.

This is especially important near the finite-time APVC frontier, where margins are small enough that losing even a few percent of `A1` can force unnecessary subdivision or imitate a pointwise obstruction.

---

## 10. Circularity audit

Inputs:

- exact positive heat amplitudes;
- box inequalities `t>=t_-`, `sigma<=sigma_+`;
- a guaranteed integer cutoff lower bound `M<=N`;
- monotonicity condition (79.5);
- convexity of a quadratic and the decreasing integral comparison.

Not used:

- RH;
- any bound on `Lambda`;
- finite-height RH verification;
- zero locations or gaps;
- oscillatory cancellation;
- GUE/pair correlation;
- Laguerre--Polya membership.

No desired collision-exclusion conclusion is assumed.

---

## 11. Implementation target

For the next frontier (`lambda≈6.82`), implement:

1. a small directed head, initially `K=64` or `128`;
2. a certified integer `M` below the minimum cutoff in each box;
3. 4--8 equal logarithmic tangent segments;
4. directed evaluation of (79.15), with a Taylor branch if a segment slope `m_j` straddles zero;
5. use the resulting lower bound wherever Round-75 secant APVC requires `A1_L`.

This should reduce proof cost by an order of magnitude while preserving essentially all of the favorable moment.
