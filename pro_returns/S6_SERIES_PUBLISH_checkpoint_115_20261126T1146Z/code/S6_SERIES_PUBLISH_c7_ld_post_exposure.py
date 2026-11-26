#!/usr/bin/env python3
"""LD released-proof auxiliaries, computed anew without historical programs."""
from collections import Counter
from hashlib import sha256
from itertools import combinations
from math import gcd
from pathlib import Path
import json
import re

from sympy import Matrix, Symbol, ZZ, eye, zeros
from sympy.matrices.normalforms import smith_normal_form

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT / "agents/continuation7_iii_weighted_catalogue"
BASE = "S6_SERIES_PUBLISH_III_02LD_"
source = LANE / (BASE + "fresh_exterior_data.json")
assert sha256(source.read_bytes()).hexdigest() == "083818ab7e52eaa416fedca4f9676340f2adbd2a90798bc2eb1f14e7b5dbbecc"
rows = json.loads(source.read_text())["rows"]
wedges = list(combinations(range(4), 2))


def wedge(A):
    return Matrix([[A.extract(i, j).det() for j in wedges] for i in wedges])


def smith(A):
    S = smith_normal_form(A, domain=ZZ)
    return [abs(int(S[i, i])) for i in range(min(S.shape)) if S[i, i]]


def ints(A):
    assert all(x.q == 1 for x in A)
    return [[int(x) for x in row] for row in A.tolist()]


rankone = []
zero_weight = []
profile_counts = Counter()
for row in rows:
    os, profile, a, b, selected = row["key"]
    matrices = [Matrix(A) for A in row["monodromies"]]
    for i, (kind, A, component) in enumerate(zip(row["fibres"], matrices, row["components"])):
        if i + 1 == selected or not re.fullmatch(r"I\d+", kind):
            continue
        nu = int(kind[1:])
        M = A - eye(4)
        col = next(M[:, j] for j in range(4) if M[:, j] != zeros(4, 1))
        alpha = col / gcd(*(abs(int(x)) for x in col))
        if next(x for x in alpha if x) < 0:
            alpha = -alpha
        pivot = next(j for j in range(4) if alpha[j])
        beta = M[pivot, :] / alpha[pivot]
        assert alpha * beta == M and alpha[3] == 0
        assert all(x.q == 1 for x in beta)
        assert gcd(*(abs(int(x)) for x in alpha)) == 1
        assert gcd(*(abs(int(x)) for x in beta)) == 1
        q, kappa = component
        assert q == nu
        narrow = (a * kappa) % nu == 0
        vertical = gcd(*(abs(int(beta[j])) for j in range(3)))
        assert vertical == (nu if narrow else 1)
        if narrow:
            assert gcd(int(beta[3]), nu) == 1 and a % nu == 0
        # Literal cover factor: alpha is vertical, so S_D^{-1} alpha=alpha.
        D = Symbol("D", integer=True)
        SD = Matrix.diag(1, 1, 1, D)
        weighted = A.copy()
        weighted[:3, 3] = D * A[:3, 3]
        assert weighted - eye(4) == alpha * beta * SD
        rankone.append(dict(row=row["key"], site=i + 1, nu=nu, narrow=narrow,
                            alpha=ints(alpha), beta=ints(beta), vertical_content=vertical))
        profile_counts[os, profile] += 1

    zero = []
    for A in matrices[:-1]:
        A0 = A.copy()
        A0[:3, 3] = zeros(3, 1)
        zero.append(A0)
    G0 = Matrix.hstack(*(A - eye(4) for A in zero))
    E0 = Matrix.hstack(*(wedge(A) - eye(6) for A in zero))
    s1, s2 = smith(G0), smith(E0)
    assert s1 == [1, 1, a]
    assert s2 == [1, 1, 1, 1, a]
    zero_weight.append(dict(row=row["key"], degree_one=ints(G0), degree_two=ints(E0),
                            smith_one=s1, smith_two=s2))

assert len(rankone) == 436 and len(zero_weight) == 172
for (os, profile), count in sorted(profile_counts.items()):
    print("PROFILE", os, profile, "PRIMITIVE_RANK_ONE_FACTORS", count)
print("PASS 436 exact primitive alpha*beta factors; all literal D-column factor identities.")
print("PASS narrow vertical contents nu with gamma entry coprime to nu; all non-narrow contents one.")
print("PASS all 172 zero-weight degree-one Smith lists are [1,1,a].")
print("PASS all 172 zero-weight degree-two Smith lists are [1,1,1,1,a].")

D = Symbol("D", integer=True, positive=True)
T = eye(4)
T[0, 1], T[2, 3] = 1, D
W = wedge(T) - eye(6)
r1 = eye(6)[:, 1]
r2 = eye(6)[:, 2] + D * eye(6)[:, 3]
relations = Matrix.hstack(r1, r2)
preimages = Matrix.hstack(eye(6)[:, 3], eye(6)[:, 4] - D * eye(6)[:, 3])
Q = Matrix([[1, 0, 0, 0, 0, 0], [0, 0, -D, 1, 0, 0],
            [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]])
section = Matrix.hstack(*(eye(6)[:, i] for i in (0, 3, 4, 5)))
left = Matrix.vstack(eye(6)[1, :], eye(6)[2, :])
assert W * preimages == relations
assert Q * W == zeros(4, 6)
assert Q * section == eye(4)
assert left * relations == eye(2)
assert eye(6) - section * Q == relations * left
assert W == relations * left * W
print("PASS all-D cusp wedge quotient/section, relation preimages and complementary inverse identities.")

out = dict(scope="Post-exposure verification of every released LD finite-certificate auxiliary; no historical execution.",
           rankone=rankone, zero_weight=zero_weight,
           cusp=dict(wedges=wedges, quotient=str(Q), section=str(section),
                     relations=str(relations), preimages=str(preimages), left_inverse=str(left)))
(LANE / (BASE + "post_exposure_data.json")).write_text(json.dumps(out, indent=2) + "\n")
print("SCOPE complete new computations; frozen fresh inputs unchanged; no canonical/global mutations.")
