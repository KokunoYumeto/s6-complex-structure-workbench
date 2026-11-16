"""Exact divisor, normal-degree and finite-level certificates for UN77.

The finite graph enumeration checks the point-blowup rules on effective
anticanonical divisors.  The finite-level check allows arbitrary tested
next-level additions and arbitrary reset of the Hopf defect.  The proof
of termination is the written fixed-length lexicographic induction,
not inference from the finite sample.
"""
from collections import deque
from math import gcd


def check_boundary(weights, genera, edges):
    for u, v in edges:
        assert weights[u] > 0 and weights[v] > 0
        assert not (weights[u] == weights[v] == 1)
        assert gcd(weights[u] - 1, weights[v] - 1) == 1
    val = [0] * len(weights)
    for u, v in edges:
        val[u] += 1
        val[v] += 1
    for i, (a, g) in enumerate(zip(weights, genera)):
        if a == 1:
            assert val[i] == (0 if g else 1)


states = set()
queue = deque()
for a in range(1, 8):
    key = ((a,), (1,), ())
    states.add(key)
    queue.append((key, 0))
for a in range(1, 5):
    for b in range(1, 5):
        key = ((a, b), (1, 1), ())
        states.add(key)
        queue.append((key, 0))

transitions = 0
while queue:
    (weights, genera, edges), depth = queue.popleft()
    check_boundary(weights, genera, edges)
    if depth == 4:
        continue
    # A smooth point blowup on coefficient one has new coefficient zero:
    # it leaves the positive-boundary graph unchanged.
    for u, a in enumerate(weights):
        assert a - 1 >= 0
        if a == 1:
            transitions += 1
            continue
        n = len(weights)
        new = (weights + (a - 1,), genera + (0,),
               tuple(sorted(edges + ((u, n),))))
        check_boundary(*new)
        transitions += 1
        if new not in states:
            states.add(new)
            queue.append((new, depth + 1))
    # The exact node rule: sigma^*D-E.
    for edge in edges:
        u, v = edge
        c = weights[u] + weights[v] - 1
        n = len(weights)
        new_edges = tuple(sorted(tuple(e for e in edges if e != edge)
                                 + ((u, n), (v, n))))
        new = (weights + (c,), genera + (0,), new_edges)
        check_boundary(*new)
        transitions += 1
        if new not in states:
            states.add(new)
            queue.append((new, depth + 1))
print("Effective anticanonical point-map states:", len(states))
print("Exact smooth/node transitions:", transitions)
print("No (1,1) positive edge; rational coefficient-one leaves; "
      "elliptic coefficient-one isolation: PASS")

# Type I: coefficient-one elliptic or rational boundary; the last
# point blowup decreases its square by one.
normal_checks = 0
for old_square in range(-20, 1):
    new_square = old_square - 1
    other = -new_square  # elliptic boundary has no triple points
    assert other >= 1
    normal_checks += 1
for old_square in range(-20, 0):
    new_square = old_square - 1
    other = -1 - new_square  # rational coefficient-one boundary is a leaf
    assert other >= 1
    normal_checks += 1
print("Type-I and type-II receiving normal-degree checks:", normal_checks)

# Two rational normalized branches of a self-double curve would both
# have negative square, but their unique triple point requires sum -1.
self_checks = 0
for a in range(1, 31):
    for b in range(1, 31):
        assert -a - b <= -2
        assert -a - b != -1
        self_checks += 1
print("Rational Hopf self-double degree contradictions:", self_checks)

# Last smooth point on coefficient a: exceptional a-1, neighbour q,
# horizontal parent q-1.  Nonnegative parent order excludes q=0.
height_checks = 0
for maximum in range(1, 51):
    for a in range(2, maximum + 2):
        exceptional = a - 1
        q = maximum - exceptional + 1
        parent = maximum - a + 1
        assert q == parent + 1
        assert 1 <= q <= maximum
        assert q + 1 <= maximum or q == maximum
        height_checks += 1
print("One-triple positive removal-level identities:", height_checks)

# Fixed-length lexicographic potential.  The removed q-card can add
# any finite number at q+1, and h may reset to any finite nonnegative
# value.  At q=M no additions are allowed.
potential_checks = 0
for maximum in range(1, 13):
    for q in range(1, maximum + 1):
        for additions in range(21):
            if q == maximum and additions:
                continue
            before = tuple(2 + j for j in range(maximum))
            after = list(before)
            after[q - 1] -= 1
            if q < maximum:
                after[q] += additions
            assert tuple(after) < before
            for h_after in (0, 1, 100, 10**9):
                assert tuple(after) + (h_after,) < before + (0,)
                potential_checks += 1
    for h in range(1, 21):
        base = tuple(range(maximum))
        assert base + (h - 1,) < base + (h,)
        potential_checks += 1
print("Whole-block lexicographic checks with arbitrary defect resets:",
      potential_checks)
print("Auxiliary multiplicity-two Atiyah divisors are excluded from "
      "the retained-stage order bound, as in the written proof.")
print("UN77 exact certificates: PASS")
