# Round 48 — Height-adaptive modified Li amplification and the absolute-Euler-product disk barrier

**Date:** 2026-08-16

**RH status:** OPEN.

**Status labels:** PROVED / SOURCE-AUDITED / NO-GO / NEW TOOL TARGET / NOVELTY UNVERIFIED.

## 0. Executive verdict

The post-Round-47 priority is sparse-exception amplification. Modified Li coefficients provide a real amplification mechanism: by tuning the real Möbius parameter to the height of an off-line zero, one improves the natural amplification scale from `gamma^2/delta` to `gamma/delta`.

However, the apparent bonus that the corresponding derivative is evaluated at a point to the right of `Re s=1` does **not** give a free prime-side proof. A sharp conformal calculation shows that every Jensen disk whose reflected image stays entirely in the half-plane of absolute Euler-product convergence misses every non-trivial zero in the critical strip. Thus any successful modified-Li/Jensen closure must enter the critical strip or use information stronger than absolute Euler-product convergence.

This round therefore yields both:

1. a quantitatively optimized sparse-orbit amplifier;
2. an exact geometric no-go theorem explaining why absolute Euler-product control alone cannot close it.

---

## 1. Source normalization guard

For real `a<1/2`, define the modified Li coefficient

\[
\lambda(n,a)
:=\sum_{\rho}
\left[1-\left(\frac{\rho-a}{\rho+a-1}\right)^n\right],
\]

with the standard symmetric zero summation.

We use the normalization recorded in Mazhouda's Selberg-class treatment:

\[
\boxed{
\lambda(n,a)
=\frac1{(n-1)!}
\left.\frac{d^n}{ds^n}
\left[(s-a)^{n-1}\log\xi(s)\right]
\right|_{s=1-a}.
}
\]

This reduces at `a=0` exactly to the classical Li coefficient normalization.

**Source audit.** The arXiv version of Sekatskii's generalized criterion contains a displayed contour identity with an extra factor `n` in the derivative relation. Taken literally at `a=0`, that does not match the classical Li normalization. Mazhouda's later formula does match the classical case exactly. The project therefore uses the Mazhouda normalization and does not import the extra factor.

The positivity of all modified coefficients for fixed `a<1/2` remains RH-equivalent; it is not an independent input.

---

## 2. Height-adaptive Möbius factor

Write

\[
a=\frac12-h,\qquad h>0,
\]

and let a right-half off-line zero be

\[
\rho=\frac12+\delta+i\gamma,
\qquad 0<\delta<\frac12.
\]

Then

\[
Z_h(\rho)
:=\frac{\rho-a}{\rho+a-1}
=\frac{h+\delta+i\gamma}{-h+\delta+i\gamma}.
\]

Hence

\[
\boxed{
|Z_h(\rho)|^2
=\frac{(h+\delta)^2+\gamma^2}
{(h-\delta)^2+\gamma^2}>1.
}
\]

Put

\[
A(h):=\log|Z_h(\rho)|
=\frac12\log\frac{(h+\delta)^2+\gamma^2}
{(h-\delta)^2+\gamma^2}.
\]

Differentiation gives

\[
A'(h)
=\frac{2\delta(\delta^2+\gamma^2-h^2)}
{\big((h+\delta)^2+\gamma^2\big)
 \big((h-\delta)^2+\gamma^2\big)}.
\]

Therefore the unique maximum occurs at

\[
\boxed{h_*=\sqrt{\gamma^2+\delta^2}.}
\]

At this optimum,

\[
\boxed{
A(h_*)
=\frac12\log\frac{h_*+\delta}{h_*-\delta}
=\operatorname{artanh}\frac{\delta}{\sqrt{\gamma^2+\delta^2}}.
}
\]

For `delta=o(gamma)`,

\[
\boxed{
A(h_*)=\frac\delta\gamma+O\!\left(\frac{\delta^3}{\gamma^3}\right).
}
\]

Thus a single transformed zero has amplitude

\[
|Z_{h_*}(\rho)|^n
=\exp\!\left(
\frac{n\delta}{\gamma}+O\left(\frac{n\delta^3}{\gamma^3}\right)
\right).
\]

A natural order-one amplification therefore occurs at

\[
\boxed{n\asymp\gamma/\delta.}
\]

For comparison, standard Li corresponds to fixed `h=1/2` and gives

\[
\log|Z_{1/2}(\rho)|
=\frac{\delta}{\gamma^2+1/4}+O(\delta^3/\gamma^4),
\]

so its natural scale is `n asymp gamma^2/delta`.

**Conclusion:** the height-adaptive modified Li map gains one full factor of `gamma` in sparse-orbit amplification.

---

## 3. Conformal disk formulation

Let

\[
z=s-\frac12,
\qquad
w=\frac{s-a}{s+a-1}=\frac{z+h}{z-h}.
\]

Solving for `s`,

\[
\boxed{
s(w)=\frac12-h\frac{1+w}{1-w}.}
\]

The critical line `Re s=1/2` maps to `|w|=1`; the left half-plane maps to the unit disk.

Using the functional equation `xi(s)=xi(1-s)`, the reflected point is

\[
\boxed{
1-s(w)=\frac12+h\frac{1+w}{1-w}.}
\]

For `|w|=r<1`,

\[
\Re\frac{1+w}{1-w}
=\frac{1-r^2}{|1-w|^2}.
\]

Its minimum on the circle is attained at `w=-r`, hence

\[
\boxed{
\min_{|w|=r}\Re(1-s(w))
=\frac12+h\frac{1-r}{1+r}.}
\]

Therefore the entire reflected circle lies in the half-plane of absolute Euler-product convergence `Re s>1` only if

\[
\boxed{
r<r_{\rm abs}(h):=\frac{2h-1}{2h+1}}
\]

(which requires `h>1/2`).

---

## 4. Exact Euler-disk exclusion theorem

Consider a left-half non-trivial zero

\[
\rho_-=\frac12-\delta+i\gamma,
\qquad 0<\delta<\frac12.
\]

Its disk coordinate satisfies

\[
\boxed{
|w(\rho_-)|^2
=\frac{(h-\delta)^2+\gamma^2}
{(h+\delta)^2+\gamma^2}.}
\]

### Theorem 48.1 — absolute Euler-product disks miss every non-trivial off-line zero

For every `h>1/2`, every `0<delta<1/2`, and every real `gamma`,

\[
\boxed{
|w(\rho_-)|
>
\frac{2h-1}{2h+1}=r_{\rm abs}(h).
}
\]

Hence no Jensen circle whose reflected image is wholly contained in `Re s>1` can enclose a non-trivial zero in the critical strip.

### Proof

After squaring and clearing positive denominators, the desired inequality is equivalent to positivity of

\[
D:=ig((h-\delta)^2+\gamma^2\big)(2h+1)^2
-ig((h+\delta)^2+\gamma^2\big)(2h-1)^2.
\]

Direct expansion yields

\[
\boxed{
D=4h\left[(1-2\delta)(2h^2-\delta)+2\gamma^2\right].}
\]

Since `h>1/2` and `0<delta<1/2`, both

\[
1-2\delta>0,
\qquad
2h^2-\delta>0,
\]

and therefore `D>0`. This proves the claim. ∎

---

## 5. Interpretation

The derivative point of the modified Li coefficient is

\[
1-a=\frac12+h.
\]

Choosing `h~gamma` indeed moves that point far into `Re s>1`, where the Euler product is absolutely convergent. But the `n`-th derivative / Jensen coefficient probes a full conformal disk whose boundary approaches the critical line. The disk must leave the absolute-convergence half-plane before it can see any non-trivial off-line zero.

Thus

\[
\boxed{
\text{large real derivative center}
\not\Rightarrow
\text{prime-side closure from absolute convergence}.}
\]

The obstruction is geometric, not a failure of a particular estimate.

---

## 6. Sparse-exception significance

The useful part survives:

\[
\boxed{
\text{height-adaptive modified Li amplification scale}
\sim\gamma/\delta.}
\]

This is substantially stronger than standard Li's `gamma^2/delta` scale.

But to turn this into a proof mechanism one needs an independent control on the corresponding high-order coefficient after the conformal disk has entered the critical strip.

Absolute Euler-product control cannot supply that theorem.

Zero-density information alone is also not automatically sufficient: the target is a single sparse orbit, so a density estimate can allow precisely the exceptional zero one is trying to exclude.

---

## 7. New-tool gate exposed by Round 48

A successful modified-Li route now requires at least one genuinely new ingredient of one of the following types:

1. **critical-strip coefficient control:** a uniform bound/sign theorem for height-adaptive modified Li coefficients with `h~gamma`, `n~gamma/delta`, obtained without RH;
2. **nonlinear phase-removal:** an averaged or quadratic transform that preserves explicit-formula computability while removing the Diophantine phase problem of individual powers `Z_h(rho)^n`;
3. **sparse-exception explicit formula:** a test family whose response to one off-line quartet grows faster than the independently controlled prime-side norm/error;
4. **new conformal/Hardy-space inequality:** control of the Jensen integral after the disk enters `1/2<Re s<1`, from arithmetic input strictly weaker than zero-freeness of that region.

Any proposed theorem that simply asserts all modified Li coefficients are nonnegative is rejected as RH-equivalent packaging.

---

## 8. Program decision

- Height-adaptive modified Li amplification: **PROVED and potentially useful as a detector**.
- Absolute-Euler-product closure: **REFUTED by Theorem 48.1**.
- Standard fixed-parameter Li as sparse amplifier: **quantitatively inferior**.
- Immediate next target: test whether pair-correlation / equal-ordinate statistics can provide the missing phase-insensitive amplification, and prove a no-go if a single orbit remains only `O(1)` against known errors.

**No proof of RH is claimed. Novelty of the optimized packaging and disk-barrier theorem is unverified.**