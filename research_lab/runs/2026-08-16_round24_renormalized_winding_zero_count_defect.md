# Round 24 — Polymath-style winding renormalization reduces exactly to zero-count defect

**Date:** 2026-08-16

**RH status:** OPEN.

**Status:** PROVED identity / STRUCTURAL BARRIER / NOVELTY UNVERIFIED.

## 0. Purpose

Round 23 proved that horizontal winding of

\[
W_t(x)=H_t(x)+iH_t'(x)
\]

is a real-zero counting observable. A possible escape for Program B was to renormalize the large-`X` winding by subtracting the explicit Polymath asymptotic counting phase `g(X,t)` and the explicit endpoint phase. This round shows that this does not create a new invariant: the renormalized quantity is exactly the real-zero counting defect.

---

## 1. Exact positive-half zero-count formula

For fixed real `t`, assume `H_t` has only simple real zeros in `[-X,X]` and `H_t(X) != 0`. Since `H_t` is even and `H_t(0)>0`, let

\[
N_t^+(X)=\#\{x\in(0,X):H_t(x)=0\}.
\]

Round 23 gives

\[
\Delta_{-X}^{X}\arg W_t
=2\arctan\frac{H_t'(X)}{H_t(X)}-2\pi N_t^+(X).
\]

Therefore

\[
\boxed{
\frac1{2\pi}\Delta_{-X}^{X}\arg W_t
=\frac1\pi\arctan\frac{H_t'(X)}{H_t(X)}-N_t^+(X).
}
\]

This is exact and uses neither RH nor a Laguerre sign condition.

---

## 2. Renormalization by the Polymath counting phase

Let `g(X,t)` denote any explicit smooth leading counting function used to approximate the positive real-zero count in the Polymath asymptotic regime. Define the natural renormalized winding

\[
\mathfrak W_t(X)
:=
\frac1{2\pi}\Delta_{-X}^{X}\arg W_t
+g(X,t)
-\frac1\pi\arctan\frac{H_t'(X)}{H_t(X)}.
\]

Then identically

\[
\boxed{
\mathfrak W_t(X)=g(X,t)-N_t^+(X).
}
\]

Thus the most natural large-`X` phase renormalization leaves exactly the zero-count discrepancy.

---

## 3. Consequences for currently available Polymath estimates

A statement of the form

\[
N_t(X)=g(X,t)+O(\log X)
\]

only yields

\[
\mathfrak W_t(X)=O(\log X).
\]

This is far too coarse to determine an integer Brouwer degree or to show that the renormalized winding is independent of time.

Even a much sharper zero-location theorem of the schematic form

\[
g(x_j(t),t)=j+o(1)
\]

would merely make `g-N` a bounded sawtooth/rounding defect. It does not provide a new conservation law unless one proves that this defect is time-invariant through the region where the real-zero census is unknown.

---

## 4. Moving spatial boundary does not remove the obstruction

One might choose `X=X(t)` so that

\[
g(X(t),t)=\text{constant}
\]

and thereby follow the macroscopic drift of the high zeros. This is useful for controlling root transport through the spatial boundary.

However the exact identity then gives

\[
\mathfrak W_t(X(t))
=\text{constant}-N_t^+(X(t)).
\]

Hence time variation of the renormalized winding is still exactly the change in the number of real zeros inside the moving boundary.

Therefore a characteristic/moving-boundary normalization removes bulk transport but not collision spectral flow.

---

## 5. Relation to Program B

Program B asks for an independently computable degree/winding budget. Rounds 23--24 show:

\[
\boxed{
\text{raw winding} = \text{endpoint phase} - \text{real-zero count},
}
\]

and

\[
\boxed{
\text{Polymath-renormalized winding} = \text{explicit count model} - \text{actual real-zero count}.
}
\]

Thus positive-time high-`X` asymptotics can control the spatial boundary and subtract the macroscopic drift, but they do not determine the missing lower time-face census.

To restore B as an independent route one needs a genuinely new boundary observable not algebraically reducible to real-zero count, or an arithmetic/analytic theorem that fixes the count defect without assuming real-rootedness/no-collision.

---

## 6. Circularity test

Any proof of

\[
\mathfrak W_{t_+}(X)-\mathfrak W_{t_-}(X)=0
\]

that proceeds by showing

\[
N_{t_+}^+(X)=N_{t_-}^+(X)
\]

is simply the no-collision statement in counting form.

Likewise any proof based on global `L_1>=0`, Hermite--Biehler orientation, or an assumed lower-gap bound is not independent.

---

## 7. Verdict

The next step proposed before Round 23 — a full global boundary winding computation using only high-`X` Polymath asymptotics — is **not sufficient as stated**.

The high-`X` asymptotic component is useful for the spatial faces, but the horizontal time-face remainder is exactly the unknown real-zero count defect.

Therefore:

\[
\boxed{A\gtrsim B\gg C}
\]

remains the justified ranking until an independent boundary observable for B is found.

**RH remains OPEN.**
