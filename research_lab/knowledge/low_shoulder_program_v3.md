# Low-Shoulder Program V3 — executable state after Round 74

**Date:** 2026-08-16  
**RH status:** OPEN.  
**Purpose:** Replace the now-stale V2 checklist by the actual proof state, the currently certified frontier, and explicit invention gates.

---

## 0. Logical target

The project uses the standard de Bruijn--Newman boundary-collision reduction already isolated in `boundary_collision_reduction.md`:

\[
(H_t(x),H_t'(x))\ne(0,0)
\quad\forall x\in\mathbb R,\ 0<t\le1/2
\]

combined with the classical upper-time real-rooted regime to force `Lambda<=0`. Together with the unconditional Rodgers--Tao theorem `Lambda>=0`, this would give `Lambda=0` and RH.

The universal no-collision statement is RH-strength and is never an allowed intermediate assumption.

---

## 1. Current proved shoulder frontier

The strongest project-certified unbounded-`x` statement is Round 73:

\[
\boxed{
0<t\le1/2,
\qquad
\lambda:=t\log\frac{|x|}{4\pi}\ge7.08
\Longrightarrow
(H_t(x),H_t'(x))\ne(0,0).
}
\]

Status:

- `INTERNALLY_PROVED`;
- `512/768-BIT CERTIFIED`;
- internal circularity audit passed;
- `REFEREE_VERIFIED: PENDING`;
- `NOVELTY_UNVERIFIED`;
- RH remains OPEN.

The old constants `10.52` and `7.10` are retained only as historical nested certificates.

---

## 2. What is no longer a target

The following V2 milestones have been completed.

### LS-A1 — exact-weight moment collapse

**INTERNALLY_PROVED, Round 64.**

Uniformly on compact `K subset (4,infinity)`, with explicit remainders,

\[
A_0(t,\lambda)\to
\zeta\!\left(\frac12+\frac\lambda4\right)-1,
\]

\[
A_1(t,\lambda)\to
-\zeta'\!\left(\frac12+\frac\lambda4\right).
\]

### LS-A2 — renormalized PSC limit

**INTERNALLY_PROVED, Round 65.**

\[
\boxed{
 t\mathcal T(t,\lambda)
\to
\frac\lambda2
\left[
2-\zeta\!\left(\frac12+\frac\lambda4\right)
\right].
}
\]

The normalization-ratio geometry was separately subjected to a hostile audit and corrected textually without weakening the theorem.

### Practical true-weight tails

**INTERNALLY_PROVED, Round 66.**

Finite exact heads plus convex-secant tails remove the impractical near-`q=1` constants from the numerical proof layer.

### LS-A3/LS-A4 — practical analytic + compact closure

**ACHIEVED quantitatively through Round 73.**

The project has successively certified `10.52`, `7.10`, and now `7.08` by explicit small-time bounds plus complete 512/768-bit box covers.

Thus the immediate project question is no longer whether true weights improve `10.52`; they demonstrably do.

---

## 3. Structural scales that must not be confused

### 3.1 Triangle-PSC small-time floor

Let `p_*` solve

\[
\zeta(p_*)=2.
\]

Then

\[
\lambda_*=4(p_*-1/2)=4.914588956\ldots
\]

is the asymptotic sign floor of the unchanged `n=1` triangle-envelope PSC:

\[
1-A_0\to2-\zeta\left(\frac12+\frac\lambda4\right).
\]

It is **not** a collision threshold and **not** a universal phase-slope floor.

### 3.2 Finite-time PSC-core frontier

The diagnostic at `lambda=7.06` shows that the first practical failure of the old PSC is instead concentrated near

\[
0.4909\lesssim t\le0.5,
\qquad
7.06\lesssim\lambda\lesssim7.0779.
\]

All terminal failures are `PSC_CORE`. They are not geometry, Polymath-error, or generic interval-width failures.

This is the active obstruction now.

### 3.3 APVC small-time floor

Round 74 introduces an `n=1` anchored phase-velocity certificate. Its fixed-lambda small-time floor is determined by

\[
\zeta(p_A)=1+\frac1{\sqrt2},
\]

hence

\[
\lambda_{\rm APVC,*}\approx5.7521220846.
\]

This is higher than `lambda_*`. Therefore APVC is a finite-time complement to the old PSC, not a replacement for it in the singular limit.

---

## 4. Current primary mechanism — hybrid PSC/APVC

Keep the old PSC as Gate 1.

At a hypothetical collision,

\[
|p|\le E_0,
\qquad
|p_x|\le E_1.
\]

Writing

\[
\frac p2=\cos\phi+
\sum_{n=2}^Na_n\cos(\phi-\tau\log n),
\]

gives the collision-conditioned anchor

\[
|\cos\phi|\le A_0+E_0/2.
\]

Thus, if `U=A0+E0/2<1`,

\[
|\sin\phi|\ge\sqrt{1-U^2}.
\]

Round 74 proves

\[
|p_x|
\ge2\left[
|\phi_x|\sqrt{1-U^2}-B_1
\right],
\]

where

\[
B_1=
\sum_{n=2}^Na_n
\sqrt{(\sigma_x\log n)^2+(
\phi_x-\tau_x\log n)^2}.
\]

In the shoulder geometry, if

\[
\Phi:=|\phi_x|\ge T\log N,
\qquad T:=-\tau_x>0,
\qquad T\ge\sigma_x,
\]

then

\[
\boxed{
B_1\le
\Phi A_0-(T-\sigma_x)A_1.
}
\]

This converts part of the old `A1` loss into a favorable term.

The current implementation strategy is therefore:

1. old PSC first;
2. if PSC fails, APVC with the **same** certified Polymath `E0,E1`;
3. subdivide only when neither gate certifies the whole box.

A deterministic source generator patches APVC into the already audited PSC verifier, so the error machinery is not duplicated.

---

## 5. Active threshold experiment

The current proof target is

\[
\boxed{C_{\rm target}=6.90.}
\]

This number is **not proved yet** at the time this V3 state is written.

Reasons for selecting it:

- pointwise high-precision diagnostics at `t=1/2` give a large positive APVC margin at `lambda=6.90`;
- the diagnostic APVC pointwise transition is near `6.819`, so `6.90` retains substantial slack;
- `6.90` is far enough below `7.08` to test that the new mechanism is materially stronger, not merely an interval tweak.

Promotion gate:

- complete finite cover of every required compact box;
- 512-bit pass;
- independent 768-bit pass;
- identical area/partition audit;
- no unresolved leaves;
- all APVC slope-sign gates explicit;
- a separate analytic small-time cover if the rectangular verifier does not naturally handle `t->0`.

Until these gates pass,

\[
C_{\rm project-proved}=7.08.
\]

---

## 6. Stop conditions for APVC

Do not push APVC indefinitely.

Classify a failed leaf as:

- `TYPE II`: interval width/rounding only;
- `TYPE III`: Polymath remainder dominates;
- `TYPE IV-A`: APVC value anchor `A0+E0/2<1` fails;
- `TYPE IV-B`: phase-velocity ordering `Phi>=T log N` fails;
- `TYPE IV-C`: APVC core margin tends to zero pointwise;
- `TYPE V`: cutoff/partition artifact;
- `TYPE VI`: unresolved.

If pointwise APVC core failure persists under shrinking boxes, stop subdividing and change the certificate.

---

## 7. Next invention if APVC reaches its finite-time floor

### 7.1 Exact joint phase-drift invariant

Retain

\[
J=\phi_x|S|^2+
\Im(\overline S S_x).
\]

For

\[
Z=e^{i\phi}S=X+iY,
\]

one has the exact identity

\[
J=X\,\Im Z_x-rac Y2p_x.
\]

Hence a true collision forces `J` into an explicit `E0,E1`-sized neighborhood of zero. A phase-sensitive exact-head/tail certificate for `J` is the next candidate if APVC is exhausted.

This route is more expensive because it retains complex phase correlations; it should not be deployed while the positive-weight APVC still has slack.

### 7.2 Existing full joint-jet certificate

The project already has a local exact finite-sum joint-jet criterion

\[
|p|^2+\rho^2|p_x|^2
>
E_0^2+M^2.
\]

It is rigorous and non-circular. Its drawback in the current `(t,lambda)` shoulder is rapid phase variation because `x=4pi exp(lambda/t)`. It is therefore a targeted local fallback, not the first global tiling mechanism.

---

## 8. Ultimate low-low shoulder

Even a successful APVC improvement does not remove the structural need for new mathematics below the old asymptotic floor

\[
\lambda_*\approx4.914588956.
\]

The long-horizon alternatives remain:

1. collision-conditioned phase/jet structure stronger than any scalar triangle envelope;
2. sparse-exception / explicit-formula amplification from Rounds 48--61;
3. genuinely new prime-side connected/factorization input if the collision-side program stalls.

Frozen/refuted routes remain frozen unless a new theorem changes their obstruction:

- raw theta diagonalization;
- finite reflected theta blocks;
- generic log-concavity/Poincare upper bounds;
- generalized Laguerre hierarchy as an assumed positivity input;
- global sign-change counting;
- global winding without a new zero-count input.

---

## 9. Bounded spatial core remains separate

The variable `lambda` is not an appropriate positive scale for `|x|<4pi` and related bounded regions. After the unbounded shoulder is compressed as far as the current methods permit, the bounded/core sector must be closed by a genuinely compact analytic/validated cover.

Finite verification there is legitimate because it is a compact-domain proof step; finite-height RH verification is never used as a substitute for the global theorem.

---

## 10. Current execution order

1. Finish the 512/768-bit hybrid PSC/APVC audit at `C_target=6.90`.
2. If it passes, promote the global project threshold and archive hashes/manifests.
3. Lower `C_target` adaptively until a **pointwise**, not interval-induced, APVC obstruction appears.
4. At that point switch to `J` / exact joint-jet only in the residual corner.
5. In parallel preserve Round-65 small-time PSC because it is asymptotically stronger than APVC.
6. Only after these finite-time mechanisms are exhausted return Track C prime-side all-orders to primary status.

The governing rule is now:

\[
\boxed{
\text{certify existing structure}
\to
\text{localize a genuine pointwise failure}
\to
\text{invent exactly one stronger certificate for that failure}.
}
\]
