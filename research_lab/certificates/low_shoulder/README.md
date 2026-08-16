# Low-shoulder certificate bundle

This directory contains the finite proof layer used by Round 71 for

\[
0<t\le1/2,
\qquad
\lambda=t\log(|x|/(4\pi))\ge7.10.
\]

The small-time part `0<t<=0.01` is analytic (Round 70); the finite rectangle `0.01<=t<=0.5`, `7.10<=lambda<=10.52` is covered by the rectangular MPFR certificate; `lambda>=10.52` uses the separately corrected high-shoulder bundle.

## Canonical sources

- `small_time_lambda710_audit.c`
- `convex_tail_psc_box_mpfr.c`
- `adaptive_psc_lambda_tiler.py`

The exact local sources compiled for the canonical runs had SHA256:

- small-time scalar audit source: `d40819ac2d84e41af8542732930ad5fd43a861ba0d1d22f63897e73d211cd93f`
- rectangular PSC source: `87072c1b7e5beacdb7242019c85686c601a05a53591effe6b0997f8b748cdb1f`
- adaptive tiler source: `4a32038e85834bf303df198d06d251a42c49c3df760e4e154fff7026b5a6ed2c`

## Build

With MPFR and GMP installed, compile the same C source at two precisions, for example

```bash
cc -O2 -Wall -Wextra -DPREC=512 convex_tail_psc_box_mpfr.c -lmpfr -lgmp -o psc_box_512
cc -O2 -Wall -Wextra -DPREC=768 convex_tail_psc_box_mpfr.c -lmpfr -lgmp -o psc_box_768

cc -O2 -Wall -Wextra -DPREC=512 small_time_lambda710_audit.c -lmpfr -lgmp -o small_512
cc -O2 -Wall -Wextra -DPREC=768 small_time_lambda710_audit.c -lmpfr -lgmp -o small_768
```

The audit container used the versioned runtime library path because the unversioned development symlink was absent; that does not change arithmetic semantics.

## Small-time scalar rerun

Both precisions return `AUDIT_RESULT pass=1` with outward-projected PSC margin

`96.25440729041982`.

Canonical outputs:

- `small_time_lambda710_audit_512.txt`
- `small_time_lambda710_audit_768.txt`

## Finite rectangle rerun

Run

```bash
python adaptive_psc_lambda_tiler.py ./psc_box_512 0.01 0.5 7.10 10.52 9 128 run512 24
python adaptive_psc_lambda_tiler.py ./psc_box_768 0.01 0.5 7.10 10.52 9 128 run768 24
```

Both canonical runs produced:

- `7219` certified terminal leaves;
- `0` unresolved leaves;
- exact certified area `1.6758`, equal to the root rectangle area;
- minimum outward-projected leaf margin `0.018395736848899086`;
- identical projected certified-leaf SHA256  
  `e95a62f0555efa04b9156363c1c986587da90b715113f02ec97dc91f134dc104`.

The full 2.4 MB leaf CSV is deterministic output of the committed tiler and is represented compactly by `lambda710_tiling_manifest.json`. The manifest expands to all 262144 cells of the depth-9 grid exactly once, with no missing or overlapping cell.

Canonical summaries:

- `lambda710_tiling_512_summary.json`
- `lambda710_tiling_768_summary.json`
- `lambda710_tiling_manifest.json`

## Weakest leaf regression

The smallest projected margin occurs on

\[
t\in[0.47703125,0.4846875],
\qquad
\lambda\in[7.10,7.1534375].
\]

Both precision reruns give

`margin_lower = 0.018395736848899086`.

Files:

- `lambda710_worst_leaf_512.txt`
- `lambda710_worst_leaf_768.txt`

## Mathematical dependency

The executable implements the analytic box theorems of Rounds 68--69, including the Round-69 absolute-log correction. The proof inputs are the unconditional D.H.J. Polymath effective Riemann--Siegel bounds, the phase-slope transversality algebra, convex/integral positive-tail estimates, Schwarz symmetry, and Cauchy's estimate.

No RH, `Lambda<=0`, finite-height RH verification, pair-correlation/GUE input, zero-spacing hypothesis, or Laguerre--Polya assumption is used.

## Status

The `7.10` theorem is `INTERNALLY_PROVED + 512/768-BIT CERTIFIED`, but remains `NOT YET REFEREE_VERIFIED` under the project's independent-reconstruction policy. Novelty is unverified. RH remains open.
