"""Bounded exact full-box checks for the independent local-energy proof."""
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import json


def shift(n, i):
    out = list(n)
    out[i] += 1
    return tuple(out)


def midpoint(edge, r):
    n, i = edge
    return Q(n[r]) + Q(int(i == r), 2)


norm_channel = Q(1, 4*9**2) + Q(3, 4*39**2)
energy_channel = Q(9, 2)*Q(1, 4*9**2) + Q(13, 2)*Q(3, 4*39**2)
assert norm_channel == Q(49, 13689)
assert energy_channel == Q(2, 117)
assert energy_channel/norm_channel == Q(234, 49)

# Linear coefficients in s=fp+fq and x=fe for the two exact channels.
assert Q(3)/Q(9, 2)-Q(1, 2) == Q(1, 6)
assert -Q(3, 2)/Q(9, 2) == -Q(1, 3)
assert Q(3)/Q(13, 2)-Q(1, 2) == -Q(1, 26)
assert Q(1, 2)/Q(13, 2) == Q(1, 13)
assert Q(2, 3)*Q(1, 6) == Q(1, 9)
assert Q(2, 3)*Q(1, 26) == Q(1, 39)

rows = []
for L in (2, 3, 4, 5):
    vertices = list(product(range(-L, L+1), repeat=3))
    edges = [(n, i) for n in vertices for i in range(3) if n[i] < L]
    stars = {e: [] for e in edges}
    faces = {}
    centers = {}
    for n in vertices:
        for i, j in combinations(range(3), 2):
            if n[i] == L or n[j] == L:
                continue
            key = (n, i, j)
            support = frozenset(((n, i), (shift(n, i), j),
                                 (shift(n, j), i), (n, j)))
            assert len(support) == 4
            faces[key] = support
            centers[key] = tuple(Q(n[r]) + Q(int(i == r)+int(j == r), 2)
                                 for r in range(3))
            for e in support:
                stars[e].append(key)
            for r in range(3):
                assert sum(midpoint(e, r) for e in support)/4 == centers[key][r]
    assert len(edges) == 3*(2*L)*(2*L+1)**2
    assert len(faces) == 3*(2*L)**2*(2*L+1)

    seen_pairs = set()
    parity_to_pair = {}
    delta_squares = [Q(0), Q(0), Q(0)]
    hinge_by_direction = [0, 0, 0]
    coplanar = 0
    for e, incident in stars.items():
        for p, q in combinations(incident, 2):
            pair = frozenset((p, q))
            assert pair not in seen_pairs
            seen_pairs.add(pair)
            assert faces[p] & faces[q] == {e}
            parity = faces[p] ^ faces[q]
            assert len(parity) == 6
            assert parity not in parity_to_pair
            parity_to_pair[parity] = pair
            planes_same = p[1:] == q[1:]
            if planes_same:
                coplanar += 1
            else:
                hinge_by_direction[e[1]] += 1
            for r in range(3):
                delta = centers[p][r] + centers[q][r] - 2*midpoint(e, r)
                if planes_same or e[1] == r:
                    assert delta == 0
                else:
                    assert abs(delta) == Q(1, 2)
                delta_squares[r] += delta**2
    assert hinge_by_direction == [32*L**3]*3
    assert delta_squares == [Q(16*L**3)]*3
    assert all(sum(c[r] for c in centers.values()) == 0 for r in range(3))
    rows.append({
        "L": L, "edges": len(edges), "faces": len(faces),
        "adjacent_unordered_pairs": len(seen_pairs),
        "distinct_six_edge_parity_supports": len(parity_to_pair),
        "hinged_pairs_by_shared_direction": hinge_by_direction,
        "coplanar_pairs": coplanar,
        "affine_delta_square_sums": [int(x) for x in delta_squares],
    })

root = Path(__file__).resolve().parent
proof = root / "local_energy_independent.md"
raw = proof.read_bytes()
receipt = {
    "status": "PASS",
    "proof": proof.name,
    "proof_bytes": len(raw),
    "proof_sha256": sha256(raw).hexdigest(),
    "norm_channel_factor": str(norm_channel),
    "energy_channel_factor": str(energy_channel),
    "leading_quotient_over_kappa": str(energy_channel/norm_channel),
    "boxes": rows,
    "scope": "Exact finite incidence and rational coefficients; no vacuum simulation or volume-limit assertion.",
}
(root / "LOCAL_ENERGY_INDEPENDENT_CHECKS.json").write_text(
    json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt, indent=2))
