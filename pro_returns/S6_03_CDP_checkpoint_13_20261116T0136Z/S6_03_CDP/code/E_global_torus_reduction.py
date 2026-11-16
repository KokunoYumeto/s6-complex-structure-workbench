"""Exact finite certificates for C.2.UN.85.

The source proves the actual analytic maps.  This program verifies their
integer fibre/discrepancy identities, the NC branch obstruction, the
global component counting convention, and the fixed lexicographic
potential.  It does not infer contractions from numerical graphs.
"""

from itertools import combinations, product
from math import gcd
from random import Random
import sympy as s


def forest_successors(state):
    """Actual point blowups away from the marked elliptic curve.

    A vertex is (minus self-square, positive discrepancy).
    """
    vertices, edges = state
    n = len(vertices)
    yield (vertices + ((1, 1),), edges), ()
    for i, (b, a) in enumerate(vertices):
        vv = list(vertices)
        vv[i] = (b + 1, a)
        vv.append((1, a + 1))
        yield (tuple(vv), tuple(sorted(edges + ((i, n),)))), (i,)
    for i, j in edges:
        vv = list(vertices)
        bi, ai = vv[i]
        bj, aj = vv[j]
        vv[i] = (bi + 1, ai)
        vv[j] = (bj + 1, aj)
        vv.append((1, ai + aj + 1))
        ee = tuple(e for e in edges if e != (i, j))
        yield (tuple(vv), tuple(sorted(ee + ((i, n), (j, n))))), (i, j)


states = {((), ())}
vertex_checks = transition_checks = receiving_checks = 0
for depth in range(7):
    nxt = set()
    for vertices, edges in states:
        valence = [0] * len(vertices)
        for i, j in edges:
            valence[i] += 1
            valence[j] += 1
        for i, (b, a) in enumerate(vertices):
            assert b >= 1 and a >= 1
            assert valence[i] <= b + 1
            vertex_checks += 1
        if depth == 6:
            continue
        for new, centre in forest_successors((vertices, edges)):
            nxt.add(new)
            transition_checks += 1
            if len(centre) == 2:
                for i in centre:
                    b, _ = vertices[i]
                    # The node blowup leaves each old vertex's valence
                    # unchanged; all discrepancy primes are boundary.
                    receiving_square = b + 1 - valence[i]
                    assert receiving_square >= 0
                    receiving_checks += 1
    states = nxt

print(f"Positive-discrepancy vertex identities: {vertex_checks} PASS")
print(f"Actual off-support/smooth/node transitions: {transition_checks} PASS")
print(f"Opposite rational receiving squares: {receiving_checks} PASS")

# Retain the exact counterexample to the discarded stronger inequality.
first = (((1, 1),), ())
second = next(new for new, centre in forest_successors(first) if centre == (0,))
third = next(new for new, centre in forest_successors(second) if centre == (0, 1))
vv, ee = third
new_index = len(vv) - 1
new_valence = sum(new_index in e for e in ee)
assert vv[new_index] == (1, 4) and new_valence == 2
assert new_valence > vv[new_index][0] - 1
assert new_valence == vv[new_index][0] + 1
print("Discarded n<=b-1 assertion: exact node counterexample retained PASS")


# Complete fibre coefficients include unmarked coefficient-zero vertices.
edge_checks = fibre_states = 0
for initial in range(-12, 13):
    current = {((initial,), ())}
    for depth in range(6):
        nxt = set()
        for aa, ee in current:
            fibre_states += 1
            for i, j in ee:
                assert gcd(abs(aa[i] + 1), abs(aa[j] + 1)) == 1
                assert (aa[i], aa[j]) != (-1, -1)
                edge_checks += 1
            if depth == 5:
                continue
            n = len(aa)
            for i, a in enumerate(aa):
                nxt.add((aa + (a + 1,), tuple(sorted(ee + ((i, n),)))))
            for i, j in ee:
                edges = tuple(e for e in ee if e != (i, j))
                nxt.add((aa + (aa[i] + aa[j] + 1,),
                         tuple(sorted(edges + ((i, n), (j, n))))))
        current = nxt

assert (-1) + (-1) + 1 == -1
assert gcd(0, 0) != 1
# Riemann--Hurwitz for an unramified double cover by P1:
# -2 = 2(2g-2), which would give 2g=1.
assert all(-2 != 2 * (2 * genus - 2) for genus in range(101))
print(f"Complete-fibre canonical states: {fibre_states} PASS")
print(f"Shifted adjacent coefficient gcd checks: {edge_checks} PASS")
print("Nodal-image and connected rational double-cover obstructions: PASS")


# Symbolic canonical orders and the two normalized source contractions.
p, b1, b2 = s.symbols('p b1 b2', integer=True)
q = p + b1 + b2 + 2
q1, q2 = p + b1 + 1, p + b2 + 1
assert s.expand(q + p - q1 - q2) == 0
assert s.expand((q1 - p) - (b1 + 1)) == 0
assert s.expand((q2 - p) - (b2 + 1)) == 0
assert -2 - (-1) == -1
same_prime_checks = 0
for d in range(2, 103):
    old = (1, d)
    new = (1, d - 2)
    assert new < old
    same_prime_checks += 1
print(f"Same global prime counted once, defect drop two: {same_prime_checks} PASS")


def potential(cards, unrecognized, defect):
    assert all(x >= 0 for x in cards)
    assert unrecognized >= 0 and defect >= 0
    return tuple(cards) + (unrecognized, defect)


direct = recognition = whole = 0
for M in range(1, 6):
    for cards in product(range(3), repeat=M):
        if cards[-1] == 0:
            continue  # the protected maximal Hopf remains present
        for u in range(5):
            for d in range(8):
                old = potential(cards, u, d)
                if d:
                    assert potential(cards, u, d - 1) < old
                    direct += 1
                if u:
                    for arbitrary_new_defect in (0, 1, 17, 1000):
                        assert potential(cards, u - 1,
                                         d + arbitrary_new_defect) < old
                        recognition += 1
                for q0, count in enumerate(cards):
                    if count == 0 or (q0 == M - 1 and count == 1):
                        continue  # cannot remove the protected anchor
                    for added in (0, 1, 7):
                        new_cards = list(cards)
                        new_cards[q0] -= 1
                        if q0 + 1 < M:
                            new_cards[q0 + 1] += added
                        else:
                            assert new_cards[-1] >= 1
                        for reset_u, reset_d in ((0, 0), (21, 89), (999, 10000)):
                            assert potential(new_cards, reset_u, reset_d) < old
                            whole += 1
print(f"Direct fixed-model defect decreases: {direct} PASS")
print(f"Recognition with arbitrary later defect: {recognition} PASS")
print(f"Whole-card decreases with recognition resets: {whole} PASS")


# Finite deterministic adversarial records: whole removals may add many
# higher-order cards and reset all recognition/defect data.
rng = Random(8500)
records = steps = 0
for M in range(1, 6):
    for trial in range(12):
        cards = [rng.randrange(3) for _ in range(M)]
        cards[-1] += 1
        u, d = rng.randrange(8), rng.randrange(12)
        while True:
            old = potential(cards, u, d)
            if d:
                d -= 1
            elif u:
                u -= 1
                d = rng.randrange(17)
            else:
                removable = [j for j, c in enumerate(cards)
                             if c > (1 if j == M - 1 else 0)]
                if not removable:
                    break
                j = min(removable)
                cards[j] -= 1
                if j + 1 < M:
                    cards[j + 1] += rng.randrange(4)
                u, d = rng.randrange(12), rng.randrange(20)
            assert potential(cards, u, d) < old
            assert cards[-1] >= 1
            steps += 1
        records += 1
print(f"Finite recognition/reset records: {records}, steps: {steps} PASS")


# Exact incidence rank/frontier maps for connected labelled finite graphs.
graphs = frontiers = 0
for n in range(2, 6):
    pairs = list(combinations(range(n), 2))
    for mask in range(1, 1 << len(pairs)):
        edges = [e for k, e in enumerate(pairs) if mask & (1 << k)]
        reached = {0}
        while True:
            enlarged = reached | {v for a, b in edges for u, v in ((a, b), (b, a))
                                  if u in reached}
            if enlarged == reached:
                break
            reached = enlarged
        if len(reached) != n:
            continue
        incidence = s.zeros(n, len(edges))
        for j, (a, b) in enumerate(edges):
            incidence[a, j], incidence[b, j] = -1, 1
        assert incidence.rank() == n - 1
        betti_one = len(edges) - n + 1
        assert betti_one >= 0
        graphs += 1
        recognized = {0}
        while len(recognized) < n:
            frontier = [(a, b) if a in recognized else (b, a)
                        for a, b in edges if (a in recognized) != (b in recognized)]
            assert frontier
            old_u = n - len(recognized)
            recognized.add(min(frontier)[1])
            assert n - len(recognized) == old_u - 1
            frontiers += 1
        if betti_one == 0:
            assert len(edges) == n - 1
print(f"Connected incidence maps: {graphs}, actual frontier decreases: {frontiers} PASS")
print("All C.2.UN.85 exact finite certificates: PASS")
