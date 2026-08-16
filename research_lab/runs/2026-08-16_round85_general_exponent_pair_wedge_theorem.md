# Round 85 — General exponent-pair singular-wedge theorem

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Truth status:** INTERNALLY_PROVED, pending independent reconstruction.  
**Strict-program admissibility:** PASSED current direct/transitive audit.  
**Referee status:** PENDING.  
**Novelty:** NOVELTY_UNVERIFIED.

---

## 1. Main theorem

Let `(k,l)` be a limiting one-dimensional exponent pair in the following standard sense: for every `eta>0`, `(k+eta,l+eta)` is an exponent pair. Assume `l<1`.

Define

\[
\boxed{
C_{\rm EP}(k,\ell)
:=
\max\left\{
2,
\frac{2(1+k-\ell)}{1-\ell},
8(k+\ell)-4
\right\}.
}
\tag{85.1}
\]

Then for every `epsilon>0` there exists `t_epsilon>0` such that

\[
\boxed{
0<t\le t_\varepsilon,
\qquad
\lambda=t\log\frac{x}{4\pi}
\ge C_{\rm EP}(k,\ell)+\varepsilon
\Longrightarrow
(H_t(x),H_t'(x))\ne(0,0).
}
\tag{85.2}
\]

The theorem uses only:

- the analytic D.H.J. Polymath effective Riemann--Siegel approximation;
- the exponent-pair bound for the **individual logarithmic half-sum**;
- the Euler product in `Re s>1`;
- the collision-conditioned value/derivative argument already audited in Rounds 82 and 84.

It uses no RH, finite-height RH verification, bound for `Lambda`, pair correlation, zero-density theorem, or zeta subconvexity statement as a black box.

---

## 2. Exponent-pair normalization and our phase

Trudgian--Yang use the standard class `F(N,P,sigma,y,c)` and define `(k,l)` to be an exponent pair if

\[
\sum_{n\in I}e(f(n))
\ll
\left(\frac{y}{N^\sigma}\right)^kN^\ell,
\qquad y\ge N^\sigma,
\tag{85.3}
\]

uniformly for intervals `I subset [N,2N]` and admissible model phases.

For the de Bruijn--Newman half-sum put

\[
f(u)=\frac{|\tau|}{2\pi}\log u.
\]

Then

\[
f'(u)=\frac{|\tau|}{2\pi}u^{-1},
\]

so this phase lies **exactly** in the model class with

\[
\sigma=1,
\qquad
y=\frac{|\tau|}{2\pi},
\qquad c=0.
\]

In the singular wedge

\[
y=e^{\lambda/t+o(1)},
\]

while every relevant dyadic block has

\[
M\le N=e^{\lambda/(2t)+o(1)},
\]

so `y>=M` holds with enormous slack.

Hence, for every fixed `eta>0`,

\[
\boxed{
\sup_{M<V\le2M}
\left|
\sum_{M<n\le V}e^{-i\tau\log n}
\right|
\ll_{\eta}
\left(\frac{y}{M}\right)^{k+\eta}
M^{\ell+\eta}.
}
\tag{85.4}
\]

On exponential scale, if

\[
M=e^{u/t},
\]

this contributes the rate

\[
(k+\eta)\lambda+(\ell-k)u.
\tag{85.5}
\]

---

## 3. Core-tail split

As in Round 84, let

\[
p=\frac12+\frac\lambda4,
\qquad
S_t=\sum_{n\le N}a_ne^{-i\tau\log n},
\]

\[
a_n=
\exp\left(
\frac t4\log^2n-\sigma_*\log n
\right),
\qquad
\sigma_*=p+O(te^{-2\lambda/t}).
\]

Choose a small fixed split parameter `delta>0` and put

\[
u_0=\lambda-2-\delta,
\qquad
M_0=\lfloor e^{u_0/t}\rfloor.
\tag{85.6}
\]

The condition `lambda>2` ensures `u_0>0` once `delta` is sufficiently small.

For `n<=M0`,

\[
p-\frac{u_0}{4}
=1+\frac\delta4.
\tag{85.7}
\]

Therefore the exact Round-64 argument remains in a half-plane of absolute convergence and gives

\[
S_t^{\rm core}
=
\zeta(p+i\tau)+O(t)+O(e^{-c/t}),
\tag{85.8}
\]

and

\[
T_t^{\rm core}
:=
\sum_{n\le M_0}a_n\log n\,e^{-i\tau\log n}
=
-\zeta'(p+i\tau)+O(t)+O(e^{-c/t}),
\tag{85.9}
\]

uniformly on compact lambda intervals on which the split is admissible.

---

## 4. Exponent-pair tail rate

The heat-weight rate at

\[
M=e^{u/t}
\]

is

\[
W_\lambda(u)
=
\frac{u^2}{4}
-\left(\frac12+\frac\lambda4\right)u.
\tag{85.10}
\]

Combining Abel summation with (85.4), a dyadic tail block has exponential rate

\[
\boxed{
G_{k,\ell,\eta}(u)
=
W_\lambda(u)
+(k+\eta)\lambda
+(\ell-k)u.
}
\tag{85.11}
\]

The function `G` is convex in `u`. Thus on

\[
u_0\le u\le\lambda/2
\]

its maximum occurs at an endpoint.

### Lower endpoint

Let first `delta=eta=0`. At

\[
u=\lambda-2
\]

one obtains exactly

\[
G_{k,\ell,0}(\lambda-2)
=
\lambda(\ell-1)+2(1+k-\ell).
\tag{85.12}
\]

This is negative precisely when

\[
\boxed{
\lambda>
C_{\rm low}(k,\ell)
:=
\frac{2(1+k-\ell)}{1-\ell}.
}
\tag{85.13}
\]

### Moving cutoff

At

\[
u=\lambda/2
\]

one gets

\[
G_{k,\ell,0}(\lambda/2)
=
-\frac{\lambda^2}{16}
+\lambda\left(\frac{k+\ell}{2}-\frac14\right).
\tag{85.14}
\]

This is negative whenever

\[
\boxed{
\lambda>
C_{\rm cut}(k,\ell)
:=8(k+\ell)-4.
}
\tag{85.15}
\]

If the right side is negative, this endpoint imposes no additional positive restriction.

Therefore for every compact interval with lower endpoint strictly larger than

\[
\max\{2,C_{\rm low},C_{\rm cut}\},
\]

one may choose first `eta>0` and then `delta>0` small enough that **both endpoint rates remain uniformly negative**. Convexity then gives

\[
S_t^{\rm tail}=O(t^{-1}e^{-c/t})=o(1),
\]

\[
T_t^{\rm tail}=O(t^{-2}e^{-c/t})=o(1).
\tag{85.16}
\]

This proves the complex zeta envelope throughout the range in (85.1).

---

## 5. Polymath remainder and derivative audit

The Round-84 shrinking-radius argument applies unchanged.

Take

\[
\rho_t=t/100.
\]

On a compact lambda interval chosen sufficiently short that its upper endpoint is less than twice its lower endpoint, the exact Polymath equation (23) gives

\[
e_A+e_B=O(e^{-c/t}),
\]

because the entire logarithmic-square numerator is divided by `x-6.66` and the positive prefactor sum contributes at worst the Riemann--Siegel length `N=e^{\lambda/(2t)+o(1)}`.

Equation (24) gives the same exponential decay for `e_{C,0}`. The possible one-term cutoff jump is exponentially small. The symmetric-normalizer comparison costs only a bounded factor because

\[
\rho_t\log(x/4\pi)=O(1).
\]

Cauchy's estimate yields

\[
E_0=O(e^{-c/t}),
\qquad
E_1=O(t^{-1}e^{-c/t}),
\]

hence

\[
E_0\to0,
\qquad
tE_1\to0.
\tag{85.17}
\]

Longer lambda intervals are covered by finitely many overlapping short compact intervals and then spliced to Rounds 84, 82, and 81.

---

## 6. Collision transversality

The core-tail estimate gives

\[
S_t
=
\zeta(p+i\tau)+o(1),
\qquad
T_t
=
-\zeta'(p+i\tau)+o(1),
\tag{85.18}
\]

uniformly on the compact interval.

Since `lambda>2`,

\[
p=\frac12+\frac\lambda4>1.
\]

The Euler product therefore gives a uniform lower bound

\[
|\zeta(p+i\tau)|
\ge
\frac{\zeta(2p)}{\zeta(p)}
\ge m>0,
\tag{85.19}
\]

while absolute convergence gives

\[
|\zeta'(p+i\tau)|=O(1).
\]

At a hypothetical collision, with

\[
e^{i\phi}S_t=X+iY,
\]

the normalized value condition gives `|X|<=E0/2`, hence

\[
|Y|\ge m-o(1).
\]

The exact real-axis derivative formulas give

\[
t|\phi_x|\to\lambda/4,
\qquad
\sqrt{\sigma_x^2+\tau_x^2}\to1/2.
\]

Therefore the phase-slope contribution is of order `1/t`, while the logarithmic-moment correction is `O(1)` and the normalized derivative remainder is `o(1/t)`. Consequently the derivative cannot vanish simultaneously with the value for sufficiently small `t`.

This proves (85.2).

---

## 7. Bourgain corollary — canonical strict improvement

Bourgain's published Bombieri--Iwaniec/decoupling work yields the limiting exponent pair

\[
\left(
\frac{13}{84},
\frac{55}{84}
\right),
\]

in the standard `+eta` sense. Trudgian--Yang explicitly record the exponent-pair normalization and identify Bourgain's refinement as the last member of the family

\[
(\theta+\eta,1/2+\theta+\eta).
\]

For

\[
k=13/84,
\qquad
\ell=55/84,
\]

we obtain

\[
C_{\rm low}
=
\frac{84}{29}
=2.896551724137931\ldots,
\]

whereas

\[
C_{\rm cut}
=
\frac{52}{21}
=2.476190476190476\ldots.
\]

Hence

\[
\boxed{
C_{\rm EP}^{\rm Bourgain}
=
\frac{84}{29}.
}
\tag{85.20}
\]

Thus the canonical strict small-time theorem improves from Round 84's `3+epsilon` to

\[
\boxed{
\forall\varepsilon>0\ \exists t_\varepsilon>0:\quad
0<t\le t_\varepsilon,
\quad
\lambda\ge\frac{84}{29}+\varepsilon
\Longrightarrow
(H_t,H_t')\ne(0,0).
}
\tag{85.21}

This use of Bourgain is **not** the invalid Round-83 `16 theta` shortcut. Here the exponent-pair theorem controls the individual logarithmic half-sum itself, exactly the object required by the weighted tail estimate.

---

## 8. Published-pair convex-combination candidate near 2.70035

Trudgian--Yang record the published exponent pairs

\[
P_-=
\left(
\frac{1959}{21656},
\frac{16135}{21656}
\right)
\]

from Sargos (1995), and

\[
P_+=
\left(
\frac{516247}{6629696},
\frac{5080955}{6629696}
\right)
\]

from Huxley--Kolesnik (2001), in the standard `+eta` sense.

Their second coordinates lie on opposite sides of `3/4`. Convexity of exponent-pair bounds therefore gives a limiting pair with

\[
\ell_*=\frac34
\]

by taking weight

\[
w=
\frac{294204881}{382877065}
\]

on `P_-`. The resulting first coordinate is

\[
\boxed{
k_*
=
\frac{134074213}{1531508260}.
}
\tag{85.22}
\]

For every nontrivial pair, the two rate thresholds satisfy

\[
C_{\rm low}=C_{\rm cut}
\quad\Longleftrightarrow\quad
(4\ell-3)(k+\ell-1)=0.
\]

Since `k+l<1`, the balance occurs exactly at

\[
\ell=3/4.
\]

Therefore this convex combination gives

\[
\boxed{
C_*
=2+8k_*
=
\frac{1033902556}{382877065}
=2.700351236760551\ldots.
}
\tag{85.23}

**Status of (85.23): SOURCE-LINE AUDIT PENDING.**

The exact pair statements and their published provenance have been cross-checked against the Trudgian--Yang source table and bibliography, but the original paywalled Sargos/Huxley--Kolesnik theorem lines have not yet both been independently opened and transcribed inside this project. Accordingly (85.23) is not yet promoted to the canonical strict frontier.

The canonical proven small-time frontier of this round is (85.21).

---

## 9. Current-preprint frontier near 2.69745

Trudgian--Yang's Lemma 1.1 proves new exponent pairs including

\[
\left(\frac{18}{199},\frac{593}{796}\right),
\qquad
\left(\frac{2779}{38033},\frac{58699}{76066}\right).
\]

Their convex segment crosses `ell=3/4` at

\[
\left(\frac{202}{2317},\frac34\right),
\]

which would give

\[
\boxed{
C_{\rm TY}
=
\frac{6250}{2317}
=2.6974536037980146\ldots.
}
\tag{85.24}

This is a serious **current-preprint frontier candidate**, not a canonical theorem of the project yet. The improvement over (85.23) is very small, and independent reconstruction of the relevant Trudgian--Yang convex-hull derivation is required before promotion.

---

## 10. Architectural floor under the exponent-pair conjecture

If the exponent-pair conjecture were available, one could take the limiting pair

\[
(k,\ell)=(0,1/2).
\]

Then

\[
C_{\rm low}=2,
\qquad
C_{\rm cut}=0,
\]

and (85.1) gives

\[
C_{\rm EP}=2.
\]

Thus even ideal square-root cancellation in the tail would leave the present **Euler-product core** architecture with a natural floor at

\[
\boxed{\lambda=2.}
\]

because the core reference point

\[
p=1/2+\lambda/4
\]

reaches the boundary `Re s=1` there.

Therefore:

- the interval `2<lambda` is, in principle, an exponential-sum optimization problem;
- crossing `lambda=2` requires a new core reference/cancellation mechanism, not merely a better exponent pair.

---

## 11. Circularity audit

### Used

- D.H.J. Polymath analytic Theorem 1.3 and explicit errors;
- standard exponent-pair definition for model phases;
- Bourgain's unconditional exponent-pair input for the canonical corollary;
- Euler product only for `Re s>1`;
- fixed-cutoff collision-conditioned derivative argument.

### Not used

- RH;
- finite-height RH verification;
- any upper bound on `Lambda`;
- pair correlation/GUE;
- full-zeta subconvexity substituted for a half-sum;
- zero density;
- real-rootedness of `H_0`;
- Laguerre--Polya positivity as an input;
- Rodgers--Tao negative-time local equilibrium.

**RH remains OPEN.**
