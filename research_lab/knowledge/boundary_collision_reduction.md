# Boundary-collision reduction for the de Bruijn-Newman constant

**Status:** PROVED reduction from established positive-time asymptotics. **Circularity status:** RH-equivalent final reduction, not independent progress by itself. **RH status: OPEN.**

Let `H_t` be the de Bruijn-Newman heat family. Use the unconditional D.H.J. Polymath large-`x` zero theorem: for every `0<t<=1/2`, all sufficiently large real-part zeros are real and simple, with a threshold of the form `x>=exp(C/t)`.

## Proposition

If `Lambda>0`, then `H_Lambda` has a multiple real zero at finite height.

Consequently, if one independently proves

\[
(H_t(x),H_t'(x))\ne(0,0)
\qquad
(0<t\le1/2,\ x\in\mathbb R),
\]

then `Lambda<=0`. Together with Rodgers--Tao `Lambda>=0`, this yields `Lambda=0` and hence RH.

## Proof sketch with dependencies exposed

Assume `Lambda>0`. Since the known unconditional upper bound gives `Lambda<1/2`, choose `t_n<Lambda` with `t_n->Lambda` and `t_n>=Lambda/2`. By definition of `Lambda`, each `H_{t_n}` has a nonreal zero `z_n`.

The positive-time Polymath large-`x` theorem is uniform for `t_n>=Lambda/2`, so nonreal zeros cannot escape through `|Re z|->infinity`. The standard de Bruijn strip control bounds their imaginary parts on the compact time interval. Hence, after taking a subsequence, `z_n->z_*` in a fixed compact set.

Local uniform convergence in `(t,z)` gives `H_Lambda(z_*)=0`. At `t=Lambda` all zeros are real, so `z_*=x_*` is real. Since `z_n` and its distinct conjugate both converge to `x_*`, Rouche/argument principle on a small disk forces multiplicity at least two at `x_*`.

Thus

\[
H_\Lambda(x_*)=H_\Lambda'(x_*)=0.
\]

## Circularity audit

The proof uses only Newman's transition property, the unconditional positive-time large-`x` theorem, real-entire conjugation symmetry, compactness, and Rouche/argument principle. It does not assume RH or `Lambda<=0`.

However, the universal statement "no positive-time multiple real zero" is, after this reduction and Rodgers--Tao, strong enough to prove RH. It must therefore be obtained from an independently certified mechanism rather than inserted as an axiom.
