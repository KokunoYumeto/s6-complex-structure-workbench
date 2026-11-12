"""Exact rational channels and bounded full-box incidence for the true band."""
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import json

vacuum = F(-1, 3)
repeated = F(1, 5)
disjoint = F(1, 3)
adjacent = F(1, 4)/F(3, 2) + F(3, 4)/F(7, 2)
assert adjacent == F(8, 21)
assert -vacuum-disjoint == 0
assert -vacuum-adjacent == -F(1, 21)
assert F(3, 4)*F(4, 3) == 1
assert F(3, 64)*2*F(4, 3) == F(1, 8)
assert F(4, 3)/(1-F(1, 8)) == F(32, 21)
assert F(1, 8)/(1-F(1, 8)) == F(1, 7)
assert 1/(1-F(1, 7)) == F(7, 6)
assert F(7, 6)*F(3, 4)**2*F(32, 21) == 1
assert (1+F(3, 4))/(1-F(1, 4)) == F(7, 3)


def shift(n, i):
    out = list(n)
    out[i] += 1
    return tuple(out)


rows = []
for L in (2, 3, 4, 5):
    vertices = list(product(range(-L, L+1), repeat=3))
    edges = [(n, i) for n in vertices for i in range(3) if n[i] < L]
    stars = {e: [] for e in edges}
    supports = []
    for n in vertices:
        for i, j in combinations(range(3), 2):
            if n[i] == L or n[j] == L:
                continue
            support = frozenset(((n, i), (shift(n, i), j),
                                 (shift(n, j), i), (n, j)))
            p = len(supports)
            supports.append(support)
            for e in support:
                stars[e].append(p)
    M = len(supports)
    assert M == 3*(2*L)**2*(2*L+1)
    assert len(edges) == 3*(2*L)*(2*L+1)**2
    neighbors = [set() for _ in range(M)]
    for incident in stars.values():
        for p, q in combinations(incident, 2):
            assert q not in neighbors[p]
            neighbors[p].add(q)
            neighbors[q].add(p)
    degrees = [len(x) for x in neighbors]
    assert max(degrees) == 12 and min(degrees) < 12
    assert sum(degrees) == 288*L**3-24*L
    assert sum(len(ps)*(len(ps)-1) for ps in stars.values()) == sum(degrees)
    for p, support in enumerate(supports):
        d = degrees[p]
        assert d == sum(len(stars[e])-1 for e in support)
        actual_cluster_diagonal = -vacuum-repeated-(M-1-d)*disjoint-d*adjacent
        excitation_diagonal = actual_cluster_diagonal+F(M, 3)
        assert actual_cluster_diagonal == F(7, 15)-F(M, 3)-F(d, 21)
        assert excitation_diagonal == F(7, 15)-F(d, 21)
    reached = {0}
    pending = [0]
    while pending:
        p = pending.pop()
        for q in neighbors[p]-reached:
            reached.add(q)
            pending.append(q)
    assert len(reached) == M
    lower_q = F(2*sum(degrees), M)
    assert lower_q == F(48*L*L-4, L*(2*L+1))
    assert F(24)-lower_q == F(4*(6*L+1), L*(2*L+1))
    assert F(7, 15)-F(24, 21) == -F(71, 105)

    parity_count = None
    if L == 2:
        seen = set()
        for p, q in combinations(range(M), 2):
            overlap = supports[p] & supports[q]
            assert len(overlap) in (0, 1)
            parity = supports[p] ^ supports[q]
            assert len(parity) == (6 if overlap else 8)
            assert parity not in seen
            seen.add(parity)
            coefficient = -vacuum-(adjacent if overlap else disjoint)
            assert coefficient == (-F(1, 21) if q in neighbors[p] else 0)
        parity_count = len(seen)
        assert parity_count == M*(M-1)//2
    rows.append({
        "L": L, "links": len(edges), "faces": M,
        "adjacent_pairs": sum(degrees)//2,
        "total_degree": sum(degrees),
        "min_degree": min(degrees), "max_degree": max(degrees),
        "connected": len(reached) == M,
        "all_distinct_pair_parity_supports_checked": parity_count,
        "signless_eigenvalue_lower_bound": str(lower_q),
    })

root = Path(__file__).resolve().parent
proof = root / "first_excitation_band_independent.md"
raw = proof.read_bytes()
receipt = {
    "status": "PASS",
    "proof": proof.name,
    "proof_bytes": len(raw),
    "proof_sha256": sha256(raw).hexdigest(),
    "virtual_resolvent_channels": {
        "vacuum": str(vacuum), "repeated_face": str(repeated),
        "disjoint_pair": str(disjoint), "adjacent_pair": str(adjacent)
    },
    "excitation_diagonal": "7/15 - d_p/21",
    "excitation_offdiagonal": "-1/21 if adjacent, zero otherwise",
    "finite_volume_degree_sum": "288 L^3 - 24 L",
    "coefficient_limit": "-71/105",
    "explicit_even_remainder": "(7/3) (64 M/3)^4 kappa xi^4 for |xi| <= 3/(128 M)",
    "boxes": rows,
    "scope": "Exact finite rational/incidence checks, not an interacting-vacuum simulation or continuum limit."
}
(root / "FIRST_EXCITATION_BAND_INDEPENDENT_CHECKS.json").write_text(
    json.dumps(receipt, indent=2)+"\n", encoding="utf-8")
print(json.dumps(receipt, indent=2))
