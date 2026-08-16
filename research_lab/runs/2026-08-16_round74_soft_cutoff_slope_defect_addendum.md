# Round 74 addendum — soft cutoff-slope defect for APVC

**Status:** INTERNALLY_PROVED strengthening.  
**RH status:** OPEN.

Round 74 first stated a convenient sufficient hypothesis

\[
\Phi\ge T\log N,
\qquad
\Phi=|\phi_x|,
\quad T=-\tau_x>0,
\]

in order to write `|Phi-T log n|=Phi-T log n` for every `n<=N`.
This hard ordering is unnecessary and is numerically undesirable because the highest cutoff term naturally lies extremely close to the phase-slope balance point.

Define instead

\[
\boxed{
\delta_N:=(T\log N-\Phi)_+.
}
\tag{A1}
\]

For every `n<=N`, put `ell=log n`. Since

\[
T\ell-\Phi\le T\log N-\Phi\le\delta_N,
\]

we have in both sign cases

\[
\boxed{
|\Phi-T\ell|
\le
\Phi-T\ell+2\delta_N.
}
\tag{A2}
\]

Indeed, when `Phi-T ell>=0` this is immediate; when it is negative, the right side minus the left side equals

\[
2(\delta_N-(T\ell-\Phi))\ge0.
\]

Consequently, if `T>=sigma_x>=0`,

\[
\begin{aligned}
\omega_n
&=\sqrt{(\sigma_x\ell)^2+(\Phi-T\ell)^2}\\
&\le \sigma_x\ell+|\Phi-T\ell|\\
&\le
\Phi+2\delta_N-(T-\sigma_x)\ell.
\end{aligned}
\]

Summing against the positive amplitudes gives the strengthened phase-free tail bound

\[
\boxed{
B_1
\le
(\Phi+2\delta_N)A_0-(T-\sigma_x)A_1.
}
\tag{A3}
\]

Thus the hard hypothesis `Phi>=T log N` can be removed from APVC. A sufficient collision-exclusion inequality is

\[
\boxed{
2\left[
\Phi\sqrt{1-(A_0+E_0/2)^2}
-(\Phi+2\delta_N)A_0
+(T-\sigma_x)A_1
\right]>E_1,
}
\tag{A4}
\]

provided `A0+E0/2<1` and `T>=sigma_x`.

For an interval box, it is enough to use

\[
\delta_N\le
\delta_U:=
\max\{T_U\log N_U-\Phi_L,0\},
\]

and therefore

\[
B_1
\le
(\Phi_U+2\delta_U)A_{0,U}
-c_LA_{1,L},
\qquad
c_L:=T_L-\sigma_{x,U}>0.
\tag{A5}
\]

This formulation is robust under cutoff jumps and removes the need to subdivide merely to prove a tiny strict ordering between the outer phase speed and the final term's phase speed.

**Circularity:** unchanged from Round 74. The addendum uses only an elementary absolute-value inequality and positive weighted sums; no zero information is imported.
