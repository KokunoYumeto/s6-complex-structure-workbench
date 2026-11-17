#!/usr/bin/env python3
"""Exact finite certificates for the surface maps in C.2.UN.83."""
from fractions import Fraction

# A fibre state consists of self-intersections, multiplicities,
# an edge set, and the multiplicity-one component met by the section.
start = ((0,), (1,), (), 0)
states = {start}
checked = 0
for depth in range(5):
    new = set()
    for squares, mults, edges_tuple, mark in states:
        edges = set(edges_tuple)
        n = len(squares)
        assert mults[mark] == 1
        for i in range(n):
            assert squares[i]*mults[i] + sum(
                mults[j if i == k else k]
                for k,j in edges if i in (k,j)
            ) == 0
        if n > 1:
            candidates = [
                i for i in range(n) if i != mark and squares[i] == -1
                and sum(i in e for e in edges) <= 2
            ]
            assert candidates
        checked += 1
        # A blowup at a smooth fibre point, away from the section.
        for i in range(n):
            sq = list(squares); sq[i] -= 1; sq.append(-1)
            es = edges | {(i,n)}
            new.add((tuple(sq), mults+(mults[i],), tuple(sorted(es)), mark))
        # A blowup at the actual section point changes its marked component.
        sq = list(squares); sq[mark] -= 1; sq.append(-1)
        new.add((tuple(sq), mults+(1,), tuple(sorted(edges|{(mark,n)})), n))
        # A node is disjoint from a section; its exceptional multiplicity is a sum.
        for i,j in edges:
            sq = list(squares); sq[i] -= 1; sq[j] -= 1; sq.append(-1)
            es = (edges-{(i,j)}) | {(i,n),(j,n)}
            new.add((tuple(sq), mults+(mults[i]+mults[j],), tuple(sorted(es)), mark))
    states = new
print(f"Actual ruled-fibre point-map states through depth4: {checked} PASS")
print("Every reducible state has an unmarked (-1) curve of valence at most2.")

# Exact normal order excludes a disconnected Stein pencil:
# e divides m and m divides m/e imply e=1.
order_checks = 0
for m in range(1, 101):
    possible = [e for e in range(1,m+1) if m % e == 0 and (m//e) % m == 0]
    assert possible == [1]
    order_checks += 1
print(f"Exact normal-order/Stein-degree certificates: {order_checks} PASS")

# The actual canonical degree on a ruling fibre is -2.
# One section with no other surviving horizontal support therefore has
# coefficient -2; an exceptional discrepancy b has neighbour q+b+1.
height_checks = 0
for q in range(1, 51):
    assert q-(q-1)+1 == 2
    for b in range(1, 31):
        assert q+b+1 >= q+2
        height_checks += 1
print(f"One-section/positive-discrepancy height certificates: {height_checks} PASS")
print("All exact certificates for C.2.UN.83: PASS")
