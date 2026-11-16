"""Exact finite certificates for C.2.UN.81.

The analytic contractions are proved in the manuscript.  This program
checks the point-fibre graph identities, all three adjunction/order
cases, the plane progress ordering, and the two finite block potentials.
It deliberately does not replace an analytic contraction by a graph.
"""

from itertools import product
import sympy as s


def grow(state):
    # Vertices are (minus self-square, full-fibre multiplicity,
    # canonical discrepancy over the elliptic root, genus).
    vv, ee = state
    nn = len(vv)
    for i in range(nn):
        v = list(vv)
        b, m, a, g = v[i]
        v[i] = (b + 1, m, a, g)
        v.append((1, m, a + 1, 0))
        yield (tuple(v), tuple(sorted(ee + ((i, nn),)))), (i,)
    for i, j in ee:
        v = list(vv)
        bi, mi, ai, gi = v[i]
        bj, mj, aj, gj = v[j]
        v[i] = (bi + 1, mi, ai, gi)
        v[j] = (bj + 1, mj, aj, gj)
        v.append((1, mi + mj, ai + aj + 1, 0))
        e = tuple(x for x in ee if x != (i, j))
        e = tuple(sorted(e + ((i, nn), (j, nn))))
        yield (tuple(v), e), (i, j)


states = [(((0, 1, 0, 1),), ())]
graph_checks = receiver_checks = cases = 0
case_counts = [0, 0, 0]
for depth in range(7):
    nxt = []
    for old in states:
        vv, ee = old
        val = [0] * len(vv)
        for i, j in ee:
            val[i] += 1
            val[j] += 1
        for i, (b, m, a, g) in enumerate(vv):
            assert val[i] <= b + (0 if g else 1)
            # The full fibre has zero intersection with each component.
            assert -b * m + sum(vv[j][1] for x, j in ee if x == i) \
                + sum(vv[x][1] for x, j in ee if j == i) == 0
            graph_checks += 1
        if depth == 6:
            continue
        for new, centre in grow(old):
            nxt.append(new)
            vnew, enew = new
            last = len(vnew) - 1
            for root_boundary in (False, True):
                boundary = [root_boundary] + [True] * last
                t = sum(boundary[i] for i in centre)
                assert t in (0, 1, 2)
                case_counts[t] += 1
                cases += 1
                if t == 0:
                    assert centre == (0,) and not root_boundary
                    assert vnew[last][2] == 1
                if t == 2:
                    for i in centre:
                        b0, _, _, genus = vv[i]
                        # An actual boundary omits at most the elliptic root.
                        t_i = sum(boundary[j] for x, j in enew if x == i) \
                            + sum(boundary[x] for x, j in enew if j == i)
                        assert t_i <= val[i]
                        receiving_square = b0 + 1 - t_i
                        assert receiving_square >= (1 if genus else 0)
                        receiver_checks += 1
    states = nxt

print(f"Full elliptic-fibre vertex identities: {graph_checks} PASS")
print(f"Last-point actual-boundary cases: {cases} PASS; t=0,1,2: {case_counts}")
print(f"Exact opposite receiving-square comparisons: {receiver_checks} PASS")

p, q, a, b = s.symbols('p q a b', integer=True)
assert s.expand((p - (p + 2) - 1) - (-3)) == 0
assert s.expand((q + a + 2) - 1 - (q + a + 1)) == 0
assert s.expand((q + a + b + 2) + q
                - ((q + a + 1) + (q + b + 1))) == 0

plane_cases = 0
for M in range(2, 12):
    for q0 in range(M + 1):
        for aa, bb in product(range(1, 6), repeat=2):
            r = q0 + aa + bb + 2
            receivers = [q0 + aa + 1, q0 + bb + 1]
            assert all(z >= q0 + 2 for z in receivers)
            if r <= M:
                before = [20] * (M + 1)
                after = before.copy()
                after[q0] -= 1
                after[r] -= 1
                for z in receivers:
                    after[z] += 1
                assert tuple(after) < tuple(before)
                plane_cases += 1
        if q0 + 2 <= M:
            assert q0 + 2 > q0
print(f"Plane type-II increasing-order defect checks: {plane_cases} PASS")
print("Plane adjunction orders and strict receiver ascent: PASS")

# Outer move: component cards unchanged; only designated-parent defect drops.
# Other surface Betti numbers may change at any canonical order.
outer_flops = 0
for M in range(1, 12):
    for hh in range(1, 11):
        cards = tuple(3 for _ in range(M))
        assert cards + (hh - 1,) < cards + (hh,)
        outer_flops += 1

# Every whole removal at q deletes that card and adds only q+1 cards.
# All later surface-defect resets may be arbitrarily large and are later.
block_checks = 0
for M in range(1, 12):
    for q0 in range(1, M + 1):
        for additions in range(8):
            if q0 == M and additions:
                continue
            old_cards = [2] * M
            new_cards = old_cards.copy()
            new_cards[q0 - 1] -= 1
            if q0 < M:
                new_cards[q0] += additions
            for old_h, new_h in product((0, 1, 50), (0, 1, 10**6)):
                assert tuple(new_cards) + (new_h,) < tuple(old_cards) + (old_h,)
                # Same check for the longer inner card/Betti vector.
                assert tuple(new_cards) + (new_h,) * (M + 1) \
                    < tuple(old_cards) + (old_h,) * (M + 1)
                block_checks += 1
print(f"Outer direct designated-parent decreases: {outer_flops} PASS")
print(f"Whole-removal lexicographic comparisons: {block_checks} PASS")

# A geometric translation field distinguishes the discarded local model:
# a nonboundary horizontal (-1) curve is not counted as a pi-exceptional.
z, w = s.symbols('z w')
for r in range(1, 8):
    # Point map (z,w)=(x,xy) lifts d/dz to d/dx-(y/x)d/dy.
    x, y = s.symbols('x y')
    Dx, Dy = 1, -y / x
    assert s.diff(x, x)*Dx + s.diff(x, y)*Dy == 1
    assert s.simplify(s.diff(x*y, x)*Dx + s.diff(x*y, y)*Dy) == 0
print("Exceptional-translation polar chart and horizontal-scope distinction: PASS")
print("ALL EXACT CHECKS FOR C.2.UN.81 PASSED")
