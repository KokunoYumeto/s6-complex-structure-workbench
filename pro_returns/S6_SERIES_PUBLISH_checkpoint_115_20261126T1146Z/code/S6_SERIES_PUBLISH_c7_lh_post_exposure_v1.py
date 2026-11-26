#!/usr/bin/env python3
"""LH post-exposure auxiliary maps; no historical target code is imported."""
from collections import Counter
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path

from sympy import Matrix, ZZ, eye, symbols, zeros
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT / "agents/continuation7_iii_odd_weighted"
INPUT = ROOT / (
    "agents/continuation7_iii_weighted_catalogue/"
    "S6_SERIES_PUBLISH_III_02LD_fresh_exterior_data.json"
)
EXPECTED = "083818ab7e52eaa416fedca4f9676340f2adbd2a90798bc2eb1f14e7b5dbbecc"
raw = INPUT.read_bytes()
assert sha256(raw).hexdigest() == EXPECTED
data = json.loads(raw)
assert len(data["rows"]) == 172
PAIRS = list(combinations(range(4), 2))


def rows(A):
    assert all(x.is_Integer for x in A)
    return [[int(x) for x in row] for row in A.tolist()]


def egcd(a, b):
    r, s, u, v, x, y = int(a), int(b), 1, 0, 0, 1
    while s:
        q = r // s
        r, s, u, v, x, y = s, r-q*s, x, y, u-q*x, v-q*y
    if r < 0:
        r, u, v = -r, -u, -v
    assert u*a+v*b == r
    return r, u, v


def minor_section(E):
    """Euclidean sum of 2-by-2 adjugates, rather than a Smith section."""
    common = 0
    terms = []
    for pair in combinations(range(E.cols), 2):
        block = E[:, pair]
        determinant = int(block.det())
        common, u, v = egcd(common, determinant)
        terms = [(J, d, c*u) for J, d, c in terms]
        terms.append((pair, determinant, v))
        if common == 1:
            break
    assert common == 1
    R = zeros(E.cols, 2)
    kept = []
    for pair, determinant, c in terms:
        if not c:
            continue
        block = E[:, pair]
        adj = block.adjugate()
        for j, position in enumerate(pair):
            R[position, :] += c*adj[j, :]
        kept.append(dict(columns=list(pair), determinant=determinant,
                         bezout=c, adjugate=rows(adj)))
    assert sum(t["determinant"]*t["bezout"] for t in kept) == 1
    assert E*R == eye(2)
    return R, kept


def wedge(x, y):
    return Matrix([x[i]*y[j]-x[j]*y[i] for i, j in PAIRS])


def exterior(A):
    return Matrix([[A.extract(I, J).det() for J in PAIRS] for I in PAIRS])


D = symbols("D", integer=True, positive=True)
S = Matrix.diag(1, 1, 1, D)
delta = eye(4)[:, 2]
saved = []
counts = Counter()
exceptional = []
for row in data["rows"]:
    key = row["key"]
    returns = [Matrix(A) for A in row["monodromies"]]
    elliptic = [A[:2, :2] for A in returns]
    E = Matrix.hstack(*(B-eye(2) for B in elliptic))
    R, witnesses = minor_section(E)
    weighted = [S.inv()*A*S for A in returns]
    W = Matrix.hstack(*(exterior(A)-eye(6) for A in weighted))
    preimages = zeros(6*len(returns), 2)
    for j in range(2):
        for i, A in enumerate(weighted):
            z = Matrix([R[2*i, j], R[2*i+1, j], 0, 0])
            assert A*delta == delta
            assert exterior(A)*wedge(delta, z)-wedge(delta, z) == (
                wedge(delta, Matrix([*((elliptic[i]-eye(2))*z[:2, :]),
                                      0, 0]))
            )
            preimages[6*i:6*i+6, j] = wedge(delta, z)
        assert W*preimages[:, j] == wedge(delta, eye(4)[:, j])
    diag = smith_normal_form(E, domain=ZZ)
    assert [abs(int(diag[j, j])) for j in range(2)] == [1, 1]
    record = dict(key=key, elliptic_relations=rows(E),
                  image_section=rows(R), minor_witnesses=witnesses,
                  mixed_angular_preimages=rows(preimages))
    saved.append(record)
    counts[(key[0], key[1])] += 1
    if key[:2] == [46, "II"]:
        assert row["fibres"][1] == "II"
        II = elliptic[1]-eye(2)
        inverse = Matrix([[-1, -1], [1, 0]])
        assert II == Matrix([[0, 1], [-1, -1]])
        assert II*inverse == eye(2) and inverse*II == eye(2)
        words = Matrix([[1, -4], [1, -1]])
        word_pre = Matrix([[-2, 5], [1, -4]])
        assert II*word_pre == words and abs(int(words.det())) == 3
        quotient = Matrix([[1, -1]])
        assert all(int(x) % 3 == 0 for x in quotient*words)
        # Every kernel vector (x,y), x-y=3k, has the following inverse:
        x, y, k = symbols("x y k", integer=True)
        coeff = words.inv()*Matrix([y+3*k, y])
        assert coeff == Matrix([[-k+y], [-k]])
        exceptional.append(dict(key=key, return_difference=rows(II),
                                inverse=rows(inverse), words=rows(words),
                                word_preimages=rows(word_pre),
                                quotient=[1, -1], modulus=3))
assert len(exceptional) == 2
for profile, count in sorted(counts.items()):
    print("PASS elliptic profile", profile, "natural rows", count,
          "full image Z^2; exact minor sections and all-D angular preimages")

# The original even-factor auxiliary is checked on one actual natural row.
target = next(r for r in data["rows"] if r["key"] == [43, "default", 2, 1, 2])
S2 = Matrix.diag(1, 1, 1, 2)
returns2 = [S2.inv()*Matrix(A)*S2 for A in target["monodromies"]]
W2 = Matrix.hstack(*(exterior(A)-eye(6) for A in returns2))
basis = eye(6)
expected_image = Matrix.hstack(basis[:, 1], basis[:, 3], basis[:, 2],
                              basis[:, 4], 2*basis[:, 0]+2*basis[:, 5])
assert hermite_normal_form(W2) == hermite_normal_form(expected_image)
tau = basis[:, 0]+basis[:, 5]
free = Matrix([[1, 0, 0, 0, 0, -1]])
torsion = Matrix([[0, 0, 0, 0, 0, 1]])
assert free*W2 == zeros(1, W2.cols)
assert all(int(x) % 2 == 0 for x in torsion*W2)
assert free*tau == zeros(1, 1) and torsion*tau == Matrix([[1]])
assert 2*tau == expected_image[:, 4]
graph = Matrix.hstack(*(A-eye(4) for A in returns2[:-1]))
edge = zeros(graph.cols, 1)
edge[2] = 1
assert graph*edge == zeros(4, 1)
assert edge[2] == 1
even = dict(key=target["key"], weight=2, return_relations=rows(W2),
            image_basis=rows(expected_image), free_coordinate=rows(free),
            torsion_coordinate=rows(torsion), torsion_modulus=2,
            tau=rows(tau), primitive_normal_edge=rows(edge))
print("PASS both OS46/II rows: exact II inverse, index-three word inclusion, quotient inverse")
print("PASS OS43/default a=2 b=1 site=2 D=2: tau has exact order 2; primitive delta edge")

# This checks the explicit half and inverse on every residue of the sampled odd groups.
# The unbounded proof is the modular identity 2*((g+1)//2)=1 modulo g.
half_checks = 0
for g in (1, 3, 5, 7, 15, 45, 105):
    h = (g+1)//2
    for c in range(g):
        assert (2*h*c-c) % g == 0
        for shift in range(g):
            assert ((c+shift)-h*(2*(c+shift)) - (c-h*2*c)) % g == 0
            half_checks += 1
print("PASS odd-half inverse and lift-independence residue equations:", half_checks)

out = LANE / "S6_SERIES_PUBLISH_III_02LH_post_exposure_data.json"
payload = dict(
    scope="Post-exposure auxiliary verification; no historical execution or extra blind credit.",
    input_sha256=EXPECTED, rows=saved, exceptions=exceptional, even_example=even,
    odd_half_checks=half_checks,
)
out.write_text(json.dumps(payload, indent=2)+"\n", encoding="utf-8", newline="\n")
loaded = json.loads(out.read_text())
assert loaded == payload
for r in loaded["rows"]:
    assert Matrix(r["elliptic_relations"])*Matrix(r["image_section"]) == eye(2)
assert len(loaded["rows"]) == 172
print("PASS complete saved JSON reread and 172 image-section equations")
print("DATA_SHA256", sha256(out.read_bytes()).hexdigest())
print("PASS all post-exposure auxiliary calculations complete")
