#!/usr/bin/env python3
"""Exact-rational audit for Round 86's published-beta singular-wedge threshold.

This script contains no floating-point arithmetic.  It checks the finite
piecewise-linear published beta envelope used in Round 86, proves that the
weighted tail-rate quadratic is non-positive at every endpoint at the claimed
threshold, and checks that the unique binding kink is the Sargos/Huxley
intersection.

The analytic source statements for the pieces are recorded in Round 86 and
source_registry.yaml.  This verifier audits the *assembly arithmetic* once
those source inequalities are admitted.
"""
from fractions import Fraction as Q

# Published Sargos exponent pair (1959/21656, 16135/21656).
kS = Q(1959,21656)
lS = Q(16135,21656)
bS = lS-kS

# Published Huxley table-19.2 line beta <= (569+1053 alpha)/2800.
AH = Q(569,2800)
BH = Q(1053,2800)

# Their exact intersection.
alpha_star = (AH-kS)/(bS-BH)
assert alpha_star == Q(854633,2111129)

beta_star = kS+bS*alpha_star
assert beta_star == Q(6003317,16889032)

# Solve h_C(alpha_star)=0, where
# h_C(alpha)=C/4*(alpha^2-alpha)-alpha/2+B(alpha).
C = 4*(beta_star-alpha_star/2)/(alpha_star*(1-alpha_star))
assert C == Q(1818938190755,715895297312)

# The core-tail transition alpha=1-2/lambda at lambda=C.
alpha_min = 1-Q(2,1)/C
assert Q(0) < alpha_min < Q(2848,12173)

# Piecewise *published* beta envelope used in the proof.
# Entries are [left,right], intercept A, slope B, label.
# The Huxley-table rows are those recorded in ANTEDB Theorem 4.16/Table 4.3;
# the Bourgain rows come from Bourgain 2017 Eq. (3.18); the Sargos pair is
# a global exponent-pair line.  We deliberately do NOT use the new
# Trudgian--Yang pair (18/199,593/796) here.
segments = [
    (alpha_min, Q(2848,12173), Q(13,414), Q(346,414), "A2 Bourgain"),
    (Q(2848,12173), Q(161,646), Q(13,318), Q(253,318), "Huxley 17.1"),
    (Q(161,646), Q(19,74), Q(11,492), Q(107,123), "Huxley 17.1"),
    (Q(19,74), Q(199,716), Q(89,2706), Q(2243,2706), "Huxley 17.1"),
    (Q(199,716), Q(967,3428), Q(29,600), Q(58,75), "Huxley 17.1"),
    (Q(967,3428), Q(120,419), Q(49,1614), Q(1351,1614), "Huxley 17.1"),
    (Q(120,419), Q(1328,4447), Q(1,66), Q(235,264), "Huxley 17.1"),
    (Q(1328,4447), Q(104,343), Q(13,194), Q(139,194), "A Bourgain"),
    (Q(104,343), Q(87,275), Q(13,146), Q(47,73), "Huxley 17.1"),
    (Q(87,275), Q(423,1295), Q(11,244), Q(191,244), "Huxley 17.1"),
    (Q(423,1295), Q(227,601), Q(89,1282), Q(454,641), "Huxley 17.1"),
    (Q(227,601), Q(12,31), Q(29,280), Q(173,280), "Huxley 17.1"),
    (Q(12,31), Q(1508,3825), Q(1,32), Q(103,128), "Huxley 17.1"),
    (Q(1508,3825), alpha_star, kS, bS, "Sargos exponent pair"),
    (alpha_star, Q(143,349), AH, BH, "Huxley 19.2"),
    (Q(143,349), Q(263,638), Q(491,5530), Q(1812,2765), "Huxley 19.2"),
    (Q(263,638), Q(1673,4038), Q(113,1345), Q(897,1345), "Huxley 19.2"),
    (Q(1673,4038), Q(5,12), Q(2,9), Q(1,3), "Bourgain 2017 I"),
    (Q(5,12), Q(3,7), Q(1,12), Q(2,3), "Bourgain 2017 II"),
    (Q(3,7), Q(1,2), Q(13,84), Q(1,2), "Bourgain 2017 III"),
]

def h(alpha,A,B):
    return C*Q(1,4)*(alpha*alpha-alpha)-alpha*Q(1,2)+A+B*alpha

# Exact contiguous cover.
assert segments[0][0] == alpha_min
assert segments[-1][1] == Q(1,2)
for i in range(len(segments)-1):
    assert segments[i][1] == segments[i+1][0], (i,segments[i][1],segments[i+1][0])

# On each segment h is convex (h''=C/2>0), so endpoint checks suffice.
binding=[]
for lo,hi,A,B,label in segments:
    hlo=h(lo,A,B)
    hhi=h(hi,A,B)
    assert hlo <= 0, (label,"left",hlo)
    assert hhi <= 0, (label,"right",hhi)
    if hlo == 0: binding.append((label,"left",lo))
    if hhi == 0: binding.append((label,"right",hi))

# Exactly the two adjacent descriptions of the same kink bind.
assert binding == [
    ("Sargos exponent pair","right",alpha_star),
    ("Huxley 19.2","left",alpha_star),
]

# The two source lines agree exactly at the kink.
assert kS+bS*alpha_star == AH+BH*alpha_star

print("ROUND86_RATIONAL_AUDIT pass=1")
print("alpha_star =", alpha_star, "=", float(alpha_star))
print("beta_star  =", beta_star, "=", float(beta_star))
print("C_beta_pub =", C, "=", float(C))
print("alpha_min  =", alpha_min, "=", float(alpha_min))
print("segments   =", len(segments))
