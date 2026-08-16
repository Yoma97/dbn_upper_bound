# Round 87 — The `lambda = 2` core barrier and the next admissible joint-core target

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Status:** PROVED STRUCTURAL NO-GO for the present positive-zeta-amplitude core; NEW TOOL TARGET IDENTIFIED.  
**Strict-program admissibility:** PASSED.  
**Novelty:** NOVELTY_UNVERIFIED.

---

## 1. Context

Round 86 proves, using published piecewise logarithmic exponential-sum bounds, that for every `epsilon>0` there is `t_epsilon>0` such that

\[
0<t\le t_\varepsilon,
\qquad
\lambda\ge C_{\beta,\mathrm{pub}}+\varepsilon,
\qquad
C_{\beta,\mathrm{pub}}=2.540788014091779\ldots,
\]

implies

\[
(H_t(x),H_t'(x))\ne(0,0).
\]

The exponential-sum part of the architecture can in principle improve further.  However, the *core* of Rounds 82--86 is anchored by

\[
S_t^{\rm core}
=
\zeta(p+i\tau)+o(1),
\qquad
p=\frac12+\frac\lambda4,
\]

followed by the positive Euler-product lower bound

\[
|\zeta(p+i\tau)|\ge\frac{\zeta(2p)}{\zeta(p)}>0,
\qquad p>1.
\]

This mechanism has an exact structural boundary at

\[
\boxed{\lambda=2.}
\]

because `p=1` there.

---

## 2. Why the Euler-product anchor cannot simply be continued below 2

Fix

\[
0<\lambda_0<2,
\qquad
p_0=\frac12+\frac{\lambda_0}{4}\in\left(\frac12,1\right).
\]

Suppose one tried to continue the current argument by proving a positive constant `c(lambda_0)>0` for which

\[
\left|
\zeta(p_0+i\tau(t,\lambda_0))
\right|
\ge c(\lambda_0)
\tag{87.1}
\]

for every sufficiently small positive `t`, where `tau(t,lambda)` is the exact real-axis Polymath saddle phase.

The exact formula is

\[
\tau(t,x)
=-\frac x2+\frac t2B(x),
\]

with

\[
B(x)=\frac{3x}{1+x^2}-\frac12\arctan x,
\]

and

\[
x(t)=4\pi e^{\lambda_0/t}.
\]

Hence

\[
-\tau(t,\lambda_0)
=2\pi e^{\lambda_0/t}+O(t).
\tag{87.2}
\]

As `t` decreases continuously to zero, the right side is continuous and tends to `+infinity`; its derivative is eventually strictly negative in `t`.  Consequently the map

\[
t\longmapsto -\tau(t,\lambda_0)
\]

contains an interval `(T_0,infinity)` in its range.

Therefore (87.1) would imply

\[
\boxed{
|\zeta(p_0+iT)|\ge c(\lambda_0)
\quad\text{for every sufficiently large }T.
}
\tag{87.3}

In particular the vertical line `Re s=p_0` would contain no sufficiently high zero of zeta.

If such a mechanism were established uniformly for every `lambda_0 in (0,2)`, then every vertical line

\[
\frac12<\Re s<1
\]

would be eventually zero-free.  After a compact finite-height verification this would amount to the desired critical-strip zero exclusion itself.

Thus below `lambda=2`, a **uniform positive lower bound for the individual zeta core is not an innocent analytic estimate**.  It is precisely the kind of hidden RH-strength assertion the project must not smuggle into the proof.

This does not prove that no special lower bound on one isolated vertical line can ever be proved.  It proves that the present all-lambda program cannot cross `2` by merely replacing the Euler-product lower bound with an unexplained positive zeta lower bound.

---

## 3. The same warning applies to a naive `zeta + zeta'` norm

One might try to replace the amplitude anchor by

\[
|\zeta(p+iT)|+|\zeta'(p+iT)|.
\]

This does not solve the structural problem automatically.

At a multiple zero of zeta both terms vanish.  Excluding simultaneous vanishing throughout the strip would require an independent theorem ruling out multiple zeta zeros there.  No such unconditional theorem is available, and importing it would replace the original problem by another major open problem.

Even at simple zeros, a uniform positive lower bound for the above norm would require quantitative lower control on `|zeta'|` at all zeros on a fixed vertical line, which is also not available.

Therefore the next core mechanism must **not** be based on a pointwise positive norm of zeta and finitely many derivatives alone.

---

## 4. What survives below 2

The oscillatory-tail machinery of Rounds 84--86 remains valuable.  The obstruction is localized entirely to the low-index core.

The exact heat sum can still be split as

\[
S_t=S_t^{\rm core}+S_t^{\rm tail}.
\]

For sufficiently good exponential-sum input, the tail may be exponentially small even for `lambda` below 2.  What fails is the replacement

\[
S_t^{\rm core}
\rightsquigarrow
\zeta(p+i\tau)
\]

followed by a **positive amplitude lower bound**.

Hence the next invention should preserve the core together with the reflected saddle/collision constraint rather than trying to certify the core separately.

---

## 5. Admissible next object: a joint reflected-core determinant

On the real axis the normalized Polymath main term has the reflected form

\[
p_t(x)=2\Re(e^{i\phi}S_t).
\]

Its derivative is

\[
\frac{p_t'(x)}2
=-\phi_x\Im(e^{i\phi}S_t)
+\Re(e^{i\phi}S_{t,x}).
\]

The current Euler-product method first lower-bounds `|S_t|`, uses the value equation to force most of that amplitude into the imaginary direction, and then obtains transversality.

Below `lambda=2` this order of operations must be changed.

Define the phase-invariant joint quantity

\[
\boxed{
\mathfrak D_t
:=
\Im\bigl(\overline{S_t}S_{t,x}\bigr)
+\phi_x|S_t|^2.
}
\tag{87.4}
\]

This is the invariant already encountered in the earlier `J`-route.  If

\[
Z=e^{i\phi}S_t=X+iY,
\]

then

\[
\mathfrak D_t
=
X\,\Im Z_x-\frac{Y}{2}p_t'(x).
\tag{87.5}
\]

Therefore a genuine collision, together with the Polymath value/derivative error bounds, forces

\[
|\mathfrak D_t|
\le
\frac{E_0}{2}
\bigl(|\phi_x||S_t|+|S_{t,x}|\bigr)
+
\frac{E_1}{2}|S_t|.
\tag{87.6}
\]

Unlike the Euler-product amplitude anchor, `D_t` can in principle remain large because of **relative phase/derivative structure even when `S_t` itself is small**.

This is therefore the smallest admissible core object presently known that could cross `lambda=2` without assuming zeta nonvanishing.

---

## 6. Limiting core representation needed for `D_t`

The next theorem target is not

\[
S_t\to\zeta(p+i\tau)
\]

with a lower bound for the right side.

It is a **joint asymptotic representation** for

\[
(S_t,S_{t,x})
\]

(or equivalently `(S_t,T_t)`) in which `mathfrak D_t` has a directly analyzable arithmetic form.

Since

\[
S_{t,x}
=-(\sigma_x+i\tau_x)T_t,
\qquad
T_t=\sum a_n\log n\,e^{-i\tau\log n},
\]

we have

\[
\Im(\overline S S_x)
=
-\sigma_x\Im(\overline S T)
-\tau_x\Re(\overline S T).
\tag{87.7}
\]

Thus

\[
\boxed{
\mathfrak D_t
=
\phi_x|S|^2
-\sigma_x\Im(\overline S T)
-\tau_x\Re(\overline S T).
}
\tag{87.8}
\]

The new core problem is therefore a **Hermitian quadratic form in the two Dirichlet polynomials `(S,T)`**, not a pointwise lower bound for zeta.

This distinction is fundamental.

---

## 7. Immediate research questions

The following questions now replace “find a better zeta lower bound”.

1. Can the Hermitian form (87.8), after scaling by `t`, be rewritten as a positive or sign-controlled weighted double sum?
2. Do the diagonal terms have a definite sign and dominate the off-diagonal terms after the piecewise-beta tail has been removed?
3. Can the reflected functional equation pair the dangerous off-diagonal terms into a controllable real kernel?
4. Does collision conditioning add a second orthogonality relation that removes the potentially negative rank-one direction?
5. Is any proposed positivity equivalent to Weil/Li/Laguerre--Polya positivity?  If yes, reject it immediately as circular.

---

## 8. Relation to the earlier prime-side program

Rounds 48--61 found that generic quadratic/Gram positivity loses diagonal control because neighboring zero vectors are highly correlated, while higher cumulants require genuinely new prime correlations.

The present object (87.8) is different: it arises **inside the explicit Riemann--Siegel half-sum before passing to a zero-spectral Gram representation**.  Therefore it deserves a separate audit before the old prime-side no-go results are imported.

However, if (87.8) reduces after expansion to an uncontrolled shifted-prime/Dirichlet correlation of exactly the type isolated in Rounds 54--61, the route must be declared structurally blocked rather than renamed.

---

## 9. Program decision

The singular-wedge program is now split as follows.

### Literature/exponential-sum zone

\[
\lambda>C_{\beta,\mathrm{pub}}
=2.540788014091779\ldots
\]

is closed for sufficiently small positive time by Round 86.

Improving the beta envelope may lower this number somewhat, but cannot by itself solve the core barrier at 2.

### Core-transition zone

\[
2<\lambda\le2.540788\ldots
\]

remains primarily an exponential-sum optimization problem; current-preprint beta bounds already give a small improvement and future bounds may reduce it further.

### New-invention zone

\[
\boxed{0<\lambda\le2.}
\]

requires a core mechanism that tolerates zeros of zeta in the strip.  The first target is the joint Hermitian determinant/invariant (87.8), not a positive zeta-amplitude estimate.

---

## 10. Circularity audit

The no-go statement uses only the explicit phase map and the logical implication of a uniform positive zeta lower bound.  It assumes neither RH nor its negation.

The proposed invariant is an identity, not a positivity assumption.

No claim is made that `mathfrak D_t` is positive or nonzero.  Proving such a statement is the next open task and must undergo a Weil/Li/Laguerre circularity audit.

**RH remains OPEN.**
