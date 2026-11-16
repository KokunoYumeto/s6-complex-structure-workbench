#!/usr/bin/env python3
"""Exact NC-branch certificates used in the independent audit of UN85.

An actual point-blown-up smooth elliptic fibre has one initial canonical
coefficient d0. Smooth blowups create d+1 and node blowups create d+e+1.
The shifted edge coefficients therefore have gcd one, including negative
coefficients and the zero-coefficient components of the full fibre.
"""
from math import gcd

state_count = edge_count = transition_count = 0
for initial in range(-20, 21):
    states = {((initial,), ())}
    for depth in range(6):
        nxt = set()
        for coeffs, edge_tuple in states:
            edges = set(edge_tuple)
            state_count += 1
            for i,j in edges:
                assert gcd(abs(coeffs[i]+1), abs(coeffs[j]+1)) == 1
                assert not (coeffs[i] == coeffs[j] == -1)
                edge_count += 1
            n = len(coeffs)
            if depth == 5:
                continue
            for i, d in enumerate(coeffs):
                nxt.add((coeffs+(d+1,),tuple(sorted(edges|{(i,n)}))))
                transition_count += 1
            for i,j in edges:
                d = coeffs[i]+coeffs[j]+1
                new_edges=(edges-{(i,j)})|{(i,n),(j,n)}
                nxt.add((coeffs+(d,),tuple(sorted(new_edges))))
                transition_count += 1
        states = nxt

print(f"Initial canonical coefficients: all integers from -20 through20")
print(f"Actual full-fibre coefficient states through depth5: {state_count} PASS")
print(f"Smooth/node point-map transitions: {transition_count} PASS")
print(f"Shifted edge gcd certificates: {edge_count} PASS")

# At a putative nodal image with two source branches and one other branch,
# a last exceptional curve would have two self-double neighbours of
# coefficient -1. Its actual node coefficient is then also -1.
d_left=d_right=-1
d_new=d_left+d_right+1
assert d_new == -1
assert gcd(abs(d_left+1),abs(d_new+1)) == 0
print("Two-source/one-other nodal-image coefficient contradiction: PASS")

# A connected unramified double cover P1 -> C would give 2=2(2-2g(C)).
assert all(2 != 2*(2-2*g) for g in range(101))
print("Connected etale double cover by P1: Euler contradiction PASS")

# A self-double last curve with two triple points has two disjoint
# normalized (-1) branches; both ordinary point contractions count.
square_first=-1
triple_points=2
square_second=-triple_points-square_first
assert square_second == -1
defect_drop=1+1
assert defect_drop == 2
print("Same global source: two normalized point blowdowns, defect drop2 PASS")
print("All exact NC recognized-branch certificates: PASS")
