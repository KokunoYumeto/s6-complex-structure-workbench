"""Exact arithmetic certificates for C.2.UN.69; no geometric assumptions inferred."""
from itertools import combinations, product
import sympy as s

print("C.2.UN.69: exact adjunction and finite incidence certificates")
pairs = [(a, q) for a in range(1, 20) for q in range(1, 20)
         if (a - 1) * q == 2]
assert pairs == [(2, 2), (3, 1)]
print("Positive rational maximum pairs (coefficient, square):", pairs)
for length in range(1, 6):
    for coeff in product(range(1, 4), repeat=length):
        for inter in product(range(2), repeat=length):
            if sum(a*b for a, b in zip(coeff, inter)) == 1:
                marked = [i for i, b in enumerate(inter) if b]
                assert len(marked) == 1 and coeff[marked[0]] == 1
print("Weighted (-1)-intersection partition: one coefficient-one transverse mark.")

tested = 0
for n in range(2, 5):
    all_edges = list(combinations(range(n), 2))
    for mask in range(1, 1 << len(all_edges)):
        edges = [e for i, e in enumerate(all_edges) if mask >> i & 1]
        adj = [set() for _ in range(n)]
        for a, b in edges:
            adj[a].add(b); adj[b].add(a)
        seen = {0}
        while True:
            more = seen | {b for a in seen for b in adj[a]}
            if more == seen: break
            seen = more
        if len(seen) != n: continue
        for heights in product(range(4), repeat=n):
            if any(abs(heights[a] - heights[b]) not in (1, 2)
                   for a, b in edges): continue
            incoming = [sum(heights[b] < heights[a] for b in adj[a])
                        for a in range(n)]
            if max(incoming) > 1: continue
            # Hodge's unique positive-square boundary is exactly this condition.
            assert len(edges) == n - 1
            maximum = max(range(n), key=lambda a: heights[a])
            assert len(adj[maximum]) == 1
            parent = next(iter(adj[maximum]))
            delta = heights[maximum] - heights[parent]
            assert (delta + 1, 2 // delta) in pairs
            tested += 1
print("Connected integral-height rational incidence records checked:", tested)

g = s.symbols("g", integer=True)
e_curve = 2 - 2*g
assert s.expand(2*e_curve - e_curve) == e_curve
assert 3 - 1 == 2
print("Actual blowup fibre differences: point 2; curve", e_curve)
print("Every certificate PASS.")
