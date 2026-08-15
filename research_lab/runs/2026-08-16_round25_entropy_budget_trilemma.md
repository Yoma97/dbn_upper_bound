# Round 25 — Local entropy-budget trilemma at heat collisions

**Date:** 2026-08-16

**RH status:** OPEN.

**Status labels:** PROVED / STRUCTURAL OBSTRUCTION / CONDITIONAL APPLICATION / NOVELTY UNVERIFIED.

## 0. Executive verdict

Rounds 18 and 22 leave Program A with one missing gate: an independent one-sided finite entropy/coercive budget. This round shows that, for an isolated generic double heat collision, this gate has a rigid local form.

If a balance law retains a nonzero collision detector of size `1/g^2`, then because

\[
g(t)^2=8(t-t_c)+O((t-t_c)^2),
\]

the state functional itself must carry a logarithmic singularity. Conversely, any compensator that removes that logarithmic singularity necessarily contributes the opposite `1/(t-t_c)` term to the derivative and therefore cancels the leading detector.

Thus there is no free bounded pairwise entropy carrying an uncancelled nonintegrable collision bulk.

The resulting trilemma is:

1. **keep the detector:** the entropy diverges logarithmically, so collision exclusion requires an independent one-sided bound;
2. **cancel the logarithm:** the compensator cancels the leading `1/(t-t_c)` detector as well;
3. **move the singularity into another channel:** then the obstruction has merely been transferred to a nonintegrable flux/reference/remainder term.

This does not disprove Program A. It identifies exactly what an independent successful A-side theorem must supply.

---

## 1. Universal collision scale

Let `F(t,x)` be a nontrivial real-analytic solution of

\[
\partial_tF=-\partial_x^2F
\]

near an isolated generic double collision at `(t_c,c)`. On the real-simple side `t>t_c`, let

\[
x_-(t)<x_+(t),\qquad g(t):=x_+(t)-x_-(t),\qquad \tau:=t-t_c.
\]

Round 18 established

\[
\boxed{g^2=8\tau+O(\tau^2).}
\]

Hence

\[
\boxed{\frac1{g^2}=\frac1{8\tau}+O(1).}
\]

Also

\[
\dot g=\frac4g+O(g).
\]

All statements below use only this local normal form.

---

## 2. Abstract balance-law lemma — PROVED

Let `C(t)` be absolutely continuous on `(t_c,t_c+\varepsilon]`. Assume

\[
\boxed{
\dot C(t)=\sigma\frac{\alpha}{g(t)^2}+R(t),
}
\]

where

\[
\alpha>0,\qquad \sigma\in\{+1,-1\},\qquad R\in L^1(t_c,t_c+\varepsilon).
\]

Then

\[
\boxed{
C(t)=\sigma\frac{\alpha}{8}\log\tau+O(1)
\qquad(\tau\downarrow0).
}
\]

### Proof

Using `g^{-2}=(8\tau)^{-1}+O(1)`,

\[
\dot C(t)=\sigma\frac{\alpha}{8\tau}+L^1(t_c,t_c+\varepsilon),
\]

because the additional `O(1)` term is integrable. Integrating from a fixed positive `\tau_0` to `\tau` gives

\[
C(t)=\sigma\frac{\alpha}{8}\log\tau+O(1).
\]

No global information about `F` is used.

---

## 3. One-sided budget consequence — PROVED

The sign determines which finite budget would exclude collision.

If `\sigma=+1`, then

\[
C(t)\to-\infty.
\]

Therefore a collision is incompatible with any independently proved lower bound

\[
C(t)\ge -M.
\]

If `\sigma=-1`, then

\[
C(t)\to+\infty.
\]

Therefore a collision is incompatible with any independently proved upper bound

\[
C(t)\le M.
\]

The balance law itself supplies neither bound.

Thus

\[
\boxed{
\text{positive detector} + L^1\text{ errors}
\Longrightarrow
\text{logarithmically divergent state variable at collision}.
}
\]

---

## 4. Exact application to the Round-18 relative log-Vandermonde — PROVED

Assume the colliding ordered pair has fixed symmetric pair weight `w>0`, locally constant on the collision cluster, and reference spacing `s\ne0` of the same orientation. Its ordered pair contribution to

\[
\mathscr C_w
=\sum_{j\ne k}w_{jk}\log\left|\frac{x_j-x_k}{\xi_j-\xi_k}\right|
\]

is

\[
2w\log\frac{g}{|s|}
=w\log g^2+O(1).
\]

Therefore

\[
\boxed{
\mathscr C_{w,\rm pair}
=w\log\tau+O(1)\to-\infty.
}
\]

The exact Round-18 `V`-bulk has ordered pair contribution

\[
\widetilde E^V_{w,\rm pair}
=\frac{2w}{g^2}+O(1)
=\frac{w}{4\tau}+O(1),
\]

so

\[
4\widetilde E^V_{w,\rm pair}
=\frac{w}{\tau}+O(1).
\]

Hence whenever the cutoff/reference channels are integrable at the collision, the abstract lemma recovers exactly

\[
\mathscr C_w=w\log\tau+O(1).
\]

Thus a lower bound on `\mathscr C_w` strong enough to exclude collision is not a consequence of the `V`-bulk/flux identity; it is the missing independent input.

---

## 5. Exact application to a locally constant Bregman window — PROVED

For a locally constant unit cutoff on the colliding pair, Round 17 uses

\[
L(r)=-\log r+r-1.
\]

The two ordered pair terms satisfy

\[
2L(g/|s|)
=-2\log g+O(1)
=-\log g^2+O(1).
\]

Therefore

\[
\boxed{
\mathcal C_{\rm Breg,pair}
=-\log\tau+O(1)\to+\infty.
}
\]

Correspondingly the force-square dissipation has leading size

\[
-\frac1\tau+O(1)
\]

when the cutoff is locally constant on the pair and the other channels are integrable.

So for the positive Bregman entropy the missing collision-excluding budget is an **upper** bound, not a lower bound.

This sign distinction must remain explicit.

---

## 6. Local equivalence with a gap bound — PROVED under bounded spectators

Suppose a collision-sensitive entropy has the local decomposition

\[
C(t)=\kappa\log g(t)+B(t),
\qquad \kappa\ne0,
\]

where the spectator term `B(t)` stays uniformly bounded near `t_c`.

Then a one-sided bound on `C` in the collision-excluding direction is quantitatively equivalent to a lower bound on `g`.

For example, if `\kappa<0` and

\[
C(t)\le M,\qquad |B(t)|\le M_0,
\]

then

\[
- |\kappa|\log g(t)\le M+M_0,
\]

hence

\[
\boxed{
g(t)\ge \exp\left(-\frac{M+M_0}{|\kappa|}\right).}
\]

The analogous statement holds for `\kappa>0` with a lower bound on `C`.

Therefore, **locally and with bounded noncolliding contributions, a finite one-sided logarithmic entropy budget is a lower-gap bound in another coordinate.**

This does not make such a bound circular if it is proved independently from Riemann-specific structure; it does show that one must audit any claimed entropy budget for hidden gap assumptions.

---

## 7. Compensation theorem — PROVED

Suppose

\[
C(t)=\sigma\frac{\alpha}{8}\log\tau+O(1)
\]

and introduce a compensator `Q(t)` such that

\[
\widehat C(t):=C(t)+Q(t)
\]

has a finite limit as `\tau\downarrow0`.

Then necessarily

\[
Q(t)=-\sigma\frac{\alpha}{8}\log\tau+O(1).
\]

If in addition `Q` is absolutely continuous and its bounded remainder has integrable derivative, then

\[
\boxed{
\dot Q(t)
=-\sigma\frac{\alpha}{8\tau}+L^1.
}
\]

Consequently

\[
\boxed{
\dot{\widehat C}(t)=L^1.
}
\]

Thus any regular compensation that makes the entropy finite cancels the leading nonintegrable collision detector in the derivative.

This is the precise no-free-lunch statement behind the entropy-budget obstruction.

---

## 8. Time-dependent smooth weights — PROVED extension

Let the colliding pair weight satisfy

\[
w(t)=w_c+O(\tau),\qquad w_c>0.
\]

Differentiating a weighted logarithmic pair term introduces

\[
\dot w(t)\log g(t)=O(|\log\tau|),
\]

which is integrable in time near `\tau=0`.

Therefore the leading `1/\tau` coefficient and the trilemma are unchanged for `C^1` time-dependent weights that remain positive at the collision.

A cutoff can avoid the theorem only by making the collision weight itself vanish sufficiently fast; but then it also turns off the collision detector and cannot exclude that collision by this channel.

---

## 9. Program-A trilemma

For any natural localized pairwise entropy whose balance near an isolated generic double collision has a nonzero inverse-square detector, exactly one of the following occurs.

### A1. Detector retained

\[
\dot C=\pm\frac{c}{\tau}+L^1,
\qquad c>0.
\]

Then

\[
C=\pm c\log\tau+O(1)
\]

and collision exclusion requires an independent one-sided finite budget.

### A2. State renormalized to remain finite

A compensator removes the logarithmic divergence, but its derivative removes the leading `1/\tau` detector as well.

### A3. Error channel is nonintegrable

If the state is claimed finite while the detector remains, then some flux/reference/remainder term must carry an opposing nonintegrable singularity. The obstruction has moved rather than disappeared.

Hence

\[
\boxed{
\text{bounded state}
+\text{uncancelled fixed-sign }1/\tau\text{ detector}
+L^1\text{ remainder}
\quad\text{cannot coexist at a collision}.}
\]

---

## 10. Consequence for the route ranking

Round 25 strengthens the interpretation of Round 18.

Program A remains structurally richer than Program B after the winding-count barrier, but its missing gate is now sharply classified:

\[
\boxed{A\gtrsim B\gg C.}
\]

A can advance only through a genuinely independent Riemann-specific one-sided bound, or through a new state variable whose collision sensitivity is not merely logarithmic pair separation with integrable errors.

A proposed budget derived from an assumed lower gap, global Laguerre positivity, all-real-zero membership, or a Rodgers--Tao estimate whose proof assumes `\Lambda<0` is not admissible for proving `\Lambda\le0`.

---

## 11. Immediate next test

The next non-circular A-side question is now narrower:

> Can the Fourier-kernel representation of `H_t`, unconditional positive-time Polymath asymptotics, or an entire-function quantity not reducible to pairwise logarithmic separation provide a one-sided bound on the localized entropy **without already implying a lower gap by assumption**?

A useful candidate must pass all three tests:

1. source-independent of RH / `\Lambda\le0` / all-real-zero assumptions;
2. finite in the collision model `z^2-2t` only if a genuinely Riemann-specific mechanism is used;
3. not obtained by compensating away the same `1/\tau` detector one seeks to exploit.

Program B should remain secondary unless a boundary observable is found that is not algebraically reducible to real-zero count defect.

---

## 12. Status

- abstract detector-to-logarithm lemma: **PROVED**;
- one-sided budget sign classification: **PROVED**;
- Round-18 relative log-Vandermonde application: **PROVED**;
- locally constant Bregman application: **PROVED**;
- local entropy-bound / lower-gap equivalence with bounded spectators: **PROVED**;
- compensation cancels leading detector: **PROVED**;
- smooth positive time-dependent weight extension: **PROVED**;
- existence of an independent Riemann-specific entropy budget: **OPEN**;
- RH: **OPEN**;
- novelty of this packaging: **UNVERIFIED**.
