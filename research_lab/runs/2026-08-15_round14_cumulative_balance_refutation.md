# Round 14 — Rigorous refutation of the cumulative-balance lemma

**Date:** 2026-08-15

**RH status:** OPEN.

---

## 1. Starting identity from Round 13

Let

\[
\psi_t(u)=e^{tu^2}\Phi(u),\qquad
w_t(u)=u\psi_t(u),
\]

\[
q(u)=-\frac{\Phi'(u)}{u\Phi(u)}.
\]

From the established strict concavity of \(r\mapsto\log\Phi(\sqrt r)\),

\[
q'(u)>0\qquad(u>0).
\]

Define

\[
S_0(t,x)=\int_0^\infty w_t(u)\sin(xu)\,du=-H_t'(x),
\]

and the cumulative balance

\[
M_{t,x}(v)=\int_0^v w_t(u)\sin(xu)\,du.
\]

When \(H_t'(x)=0\), one has \(M_{t,x}(\infty)=0\). Round 13 also proved

\[
\int_0^\infty q(u)w_t(u)\sin(xu)\,du
=xH_t(x)-2tH_t'(x).
\]

Therefore at every positive critical point \(x>0\) of \(H_t\),

\[
\boxed{
xH_t(x)=-\int_0^\infty q'(u)M_{t,x}(u)\,du.
}
\]

The boundary term vanishes because of the super-exponential decay of the Riemann kernel and its derivatives.

---

## 2. The Round-13 candidate is false

Round 13 proposed the candidate statement

\[
H_t'(x)=0\quad\Longrightarrow\quad M_{t,x}(v)\ge0\ \forall v\ge0.
\]

### Proposition 14.1

**REFUTED (rigorously).** The statement above is false even in the fully real-rooted regime.

### Proof

Take \(t=1/2\). By de Bruijn, \(H_{1/2}\) has only real zeros. Moreover a multiple real zero at time \(t_0\) must satisfy \(t_0\le\Lambda\), while the established upper bound has \(\Lambda<1/2\); hence all zeros of \(H_{1/2}\) are simple.

Polymath's high-height theorem supplies infinitely many such real simple zeros. Between consecutive simple real zeros, the sign of \(H_{1/2}\) alternates. Hence there are infinitely many intervals on which \(H_{1/2}>0\). On each such bounded interval with zero endpoints, Rolle's theorem gives a point \(x_*>0\) with

\[
H_{1/2}'(x_*)=0,\qquad H_{1/2}(x_*)>0.
\]

At this point the exact identity above gives

\[
\int_0^\infty q'(u)M_{1/2,x_*}(u)\,du
=-x_*H_{1/2}(x_*)<0.
\]

Since \(q'(u)>0\), it is impossible that \(M_{1/2,x_*}(u)\ge0\) for every \(u\). Therefore

\[
\exists v>0:\quad M_{1/2,x_*}(v)<0.
\]

This contradicts the proposed cumulative-balance lemma. ∎

### Interpretation

The overshoot discovered in Round 13 is not exceptional to collisions. Ordinary critical points in the known real-rooted regime already exhibit negative cumulative balance. Thus **the mere existence of an overshoot carries too little information to detect collision**.

---

## 3. What survives exactly

At a critical point \(H_t'(x)=0\), define the weighted overshoot functional

\[
\mathcal O_t(x)
:=-\int_0^\infty q'(u)M_{t,x}(u)\,du.
\]

Then the previous identity is

\[
\boxed{\mathcal O_t(x)=xH_t(x)\qquad(H_t'(x)=0).}
\]

Therefore a collision is exactly a critical point with

\[
\mathcal O_t(x)=0.
\]

This formulation is exact but, quantified over all \(t>0\), is RH-equivalent through the positive-threshold collision theorem. It is not an independent no-go theorem.

The useful structural information is more limited:

- \(q'(u)>0\) is independently established from the Riemann kernel;
- \(q\) is independent of heat time;
- the heat dependence is entirely in the exponentially tilted positive weight \(w_t\);
- collision asks for exact cancellation of a strictly positive \(q'\)-weighted cumulative oscillatory balance.

---

## 4. Sharpened C6 target

The next target must **not** impose one sign on \(M\). Instead it should prove non-vanishing of the weighted balance at critical points by a structural sign-regularity or variation-diminishing argument.

A precise form is:

### CANDIDATE 14-A — weighted critical transversality

Find an independently provable index/sign rule \(\sigma(t,x)\in\{\pm1\}\), determined from the Riemann kernel or from a finite oscillation index and not from the unknown sign of \(H_t(x)\), such that whenever

\[
H_t'(x)=0,\quad t>0,\ x>0,
\]

one has

\[
\boxed{
\sigma(t,x)\int_0^\infty q'(u)M_{t,x}(u)\,du>0.
}
\]

This would prohibit a common zero of \(H_t,H_t'\).

### Mandatory anti-circularity test

A proposed \(\sigma\) is rejected if defining or proving its sign already assumes:

- real-rootedness of \(H_t\);
- interlacing of zeros of \(H_t\) and \(H_t'\);
- the sign of \(H_t\) between unknown zeros;
- \(L_1>0\) for all real x;
- any all-n generalized Laguerre/positive-definite-kernel criterion.

---

## 5. Half-wave decomposition for the next attack

For a fixed \(x>0\), partition \((0,\infty)\) into sine half-waves

\[
I_n=\left[\frac{n\pi}{x},\frac{(n+1)\pi}{x}\right],\qquad n=0,1,2,\dots.
\]

Define positive masses

\[
a_n(t,x)=\int_{I_n}w_t(u)|\sin(xu)|\,du,
\]

\[
b_n(t,x)=\int_{I_n}q(u)w_t(u)|\sin(xu)|\,du.
\]

Then

\[
S_0(t,x)=\sum_{n\ge0}(-1)^n a_n,
\qquad
S_1(t,x)=\sum_{n\ge0}(-1)^n b_n.
\]

Since q is strictly increasing and the intervals are ordered,

\[
\boxed{
\frac{b_{n+1}}{a_{n+1}}>\frac{b_n}{a_n}
}
\]

whenever the masses are nonzero: the weighted average of q over a later half-wave is strictly larger than over an earlier half-wave.

This is a genuine monotone-likelihood-ratio structure.

However it is **not yet enough**: an alternating sequence can have zero unweighted sum and zero increasing-ratio weighted sum if its partial alternating sums change sign. Therefore any successful theorem must add a nontrivial constraint on the half-wave mass sequence \((a_n)\) coming from the special Riemann density

\[
w_t(u)=u e^{tu^2}\Phi(u).
\]

The next legitimate mathematical question is therefore:

> What exact discrete shape property (strict log-concavity, ratio monotonicity of suitable grouped half-wave masses, or a stronger sign-regular determinant) does the Riemann kernel force on \((a_n(t,x))\), and is that property strong enough to make the two alternating sums unable to vanish simultaneously?

This is narrower and more falsifiable than a generic `prove L1>0` request.

---

## 6. Status

- Round-13 cumulative nonnegative-balance lemma: **REFUTED**.
- Monotonicity \(q'(u)>0\): **PROVED**.
- Exact weighted critical identity: **PROVED**.
- Half-wave average ratios \(b_n/a_n\) strictly increasing: **PROVED**.
- A sufficient shape theorem for the half-wave masses \(a_n\): **OPEN**.
- Independent C6 no-collision mechanism: **OPEN**.
- RH: **OPEN**.
- Novelty: **UNVERIFIED**.
