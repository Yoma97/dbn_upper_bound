#!/usr/bin/env python3
"""Generate the hostile-audited K=2048 PSC verifier on 6.19 <= lambda <= 7.08.

This is a deterministic textual extension of the committed canonical
convex_tail_psc_lambda619_mpfr.c.  It changes only the number of 0.01-wide
lambda boxes from 85 to 89, the printed box count, and the diagnostic label.
The mathematical inequalities and all directed-rounding operations are
unchanged.
"""
from pathlib import Path

src = Path(__file__).with_name("convex_tail_psc_lambda619_mpfr.c")
out = Path(__file__).with_name("convex_tail_psc_lambda619_to708_mpfr.c")

s = src.read_text()
replacements = [
    ("for(int j=0;j<85;j++)", "for(int j=0;j<89;j++)"),
    ("(IHI-ILO)*85", "(IHI-ILO)*89"),
    ("lambda [6.19,7.04]", "lambda [6.19,7.08]"),
]
for old, new in replacements:
    if s.count(old) != 1:
        raise SystemExit(f"expected exactly one occurrence of {old!r}, found {s.count(old)}")
    s = s.replace(old, new)

out.write_text(s)
print(out)
