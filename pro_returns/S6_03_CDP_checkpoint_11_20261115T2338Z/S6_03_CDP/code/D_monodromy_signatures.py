#!/usr/bin/env python3
"""Exact rank-four cyclotomic monodromy and A'Campo signatures.

All matrices, determinants, exterior powers, Mobius inversions and zeta
identities are over Z or Q(t). No numerical roots are used. The output
enumerates all monodromy signatures and checks the exceptional explicit
torus automorphisms used in the geometric realization proof.
"""
from __future__ import annotations

import csv
import itertools
import json
import math
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[1]
x, t = s.symbols("x t")
orders = [1, 2, 3, 4, 5, 6, 8, 10, 12]
degree = {n: int(s.totient(n)) for n in orders}


def products(left, start=0, factors=()):
    if left == 0:
        yield factors
        return
    for i in range(start, len(orders)):
        n = orders[i]
        if degree[n] <= left:
            yield from products(left-degree[n], i, factors+(n,))


def exterior(matrix, q):
    if q == 0:
        return s.ones(1)
    subsets = list(itertools.combinations(range(matrix.rows), q))
    return s.Matrix([[matrix.extract(I, J).det() for J in subsets]
                     for I in subsets])


def phi_text(factors, latex=False):
    bits = []
    for n in sorted(set(factors)):
        e = factors.count(n)
        if latex:
            bits.append(r"\Phi_{%d}" % n + ("^{%d}" % e if e > 1 else ""))
        else:
            bits.append("Phi_%d" % n + ("^%d" % e if e > 1 else ""))
    return ("" if latex else " ").join(bits)


rows = []
all_positive_traces = set()
for factors in products(4):
    blocks = [s.Matrix.companion(s.Poly(s.cyclotomic_poly(n, x), x))
              for n in factors]
    T = s.diag(*blocks)
    if T.det() != 1:
        continue
    M = math.lcm(*factors)
    assert T**M == s.eye(4)
    L = {k: int((s.eye(4)-T**k).det()) for k in range(1, 8*M+1)}
    assert all(v >= 0 for v in L.values())
    all_positive_traces.update(v for v in L.values() if v)
    signature = {}
    for n in range(1, 8*M+1):
        numerator = sum(int(s.mobius(n//d))*L[d] for d in s.divisors(n))
        assert numerator % n == 0
        a = numerator//n
        if a:
            assert M % n == 0
            signature[n] = a
    zeta = s.Integer(1)
    for q in range(5):
        W = exterior(T, q)
        det = (s.eye(W.rows)-t*W).det()
        zeta *= det**((-1)**(q+1))
    euler_product = s.prod((1-t**n)**(-a) for n, a in signature.items())
    assert s.cancel(zeta-euler_product) == 0
    assert sum(n*a for n, a in signature.items()) == 0
    if 1 in factors:
        assert signature == {}
    else:
        assert signature.get(1, 0) == L[1] > 0
    rows.append({"factors": factors, "polynomial": phi_text(factors),
                 "order": M, "signature": signature,
                 "L1": L[1], "period": [L[k] for k in range(1, M+1)]})

rows.sort(key=lambda r: (1 not in r["factors"], r["order"], r["factors"]))
assert len(rows) == 19
assert sum(not r["signature"] for r in rows) == 5
assert sorted(all_positive_traces) == [1, 2, 3, 4, 5, 6, 8, 9, 12, 16]
assert sorted(set(r["order"] for r in rows)) == [1, 2, 3, 4, 5, 6, 8, 10, 12]

# Integral lattice actions on E_i^2, in real block coordinates.
J = s.Matrix([[0, -1], [1, 0]])
O = s.zeros(2)
I = s.eye(2)
G8 = s.BlockMatrix([[O, J], [I, O]]).as_explicit()
G12 = s.BlockMatrix([[O, I], [I, J]]).as_explicit()
for n, G in [(8, G8), (12, G12)]:
    assert G.det() == 1
    assert G.charpoly(x).as_expr() == s.cyclotomic_poly(n, x)
    assert G**n == s.eye(4)
    assert all(G**d != s.eye(4) for d in s.divisors(n) if d < n)
assert G8**2 == s.diag(J, J)
assert s.Poly(s.cyclotomic_poly(5, -x), x) == s.Poly(s.cyclotomic_poly(10, x), x)
assert {j % 5 for j in [1, 2, -1, -2]} == {1, 2, 3, 4}
assert {(5+2*j) % 10 for j in [1, 2, -1, -2]} == {1, 3, 7, 9}

with (ROOT/"records/D_monodromy_signatures.csv").open("w", newline="") as out:
    writer = csv.writer(out)
    writer.writerow(["characteristic_polynomial", "semisimple_order",
                     "nonzero_a_n", "L1", "one_period_Lk"])
    for r in rows:
        writer.writerow([r["polynomial"], r["order"],
                         "; ".join(f"a_{n}={a}" for n,a in r["signature"].items()),
                         r["L1"], "; ".join(map(str, r["period"]))])

lines = [r"\begin{center}", r"\small",
         r"\begin{tabular}{ccl}",
         r"$P_T$ & $M$ & Nonzero $a_n$\\\hline"]
for r in rows:
    sig = (r",\quad ".join("a_{%d}=%d" % (n, a)
                            for n, a in r["signature"].items())
           or r"\text{all zero}")
    lines.append("$%s$ & %d & $%s$ \\\\" %
                 (phi_text(r["factors"], True), r["order"], sig))
lines += [r"\end{tabular}", r"\end{center}", ""]
(ROOT/"records/D_monodromy_signatures_table.tex").write_text("\n".join(lines))

print("Exact cyclotomic rank-four orientation-preserving cases:", len(rows))
print("Zero-signature cases:", sum(not r["signature"] for r in rows))
print("Semisimple orders:", sorted(set(r["order"] for r in rows)))
print("Positive Lefschetz values:", sorted(all_positive_traces))
print("All exterior-power zeta identities and Mobius coefficients verified.")
print("Explicit E_i^2 automorphisms have exact orders 8,12 and polynomials Phi_8,Phi_12.")
print("Genus-two Jacobian eigenvalues and its negative give Phi_5 and Phi_10.")
print(json.dumps(rows, indent=2))
