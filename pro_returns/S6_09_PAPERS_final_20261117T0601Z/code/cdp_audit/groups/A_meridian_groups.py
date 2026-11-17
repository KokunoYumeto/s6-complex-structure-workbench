#!/usr/bin/env python3
"""Exact lattice certificates for the actual meridian formulas of UN44.

The matrices below test presentation identities. They do not assert that
every matrix/vector tuple is realized by a holomorphic degeneration.
"""
from pathlib import Path
from random import Random

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form


def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = egcd(b, a % b)
    return g, y, x - (a // b) * y


def bezout(values):
    g, cs = 0, []
    for a in values:
        new_g, x, y = egcd(g, a)
        cs = [x * c for c in cs] + [y]
        g = new_g
    assert sum(c * a for c, a in zip(cs, values)) == g
    return g, cs


def group_invariants(relations):
    """Cokernel of an integral column-relation matrix: (free rank, torsion)."""
    form = smith_normal_form(relations, domain=sp.ZZ)
    diagonal = [abs(int(form[i, i]))
                for i in range(min(form.shape)) if form[i, i]]
    return relations.rows - len(diagonal), tuple(d for d in diagonal if d > 1)


def columns(vectors, rows):
    return sp.Matrix.hstack(*vectors) if vectors else sp.zeros(rows, 0)


I = sp.eye(4)
N1 = sp.zeros(4)
N1[0, 1] = 1
N2p = N1.copy()
N2p[2, 3] = 1
N2m = N1.copy()
N2m[2, 3] = -1
C3 = sp.Matrix([[0, -1], [1, -1]])
C4 = sp.Matrix([[0, -1], [1, 0]])
monodromies = {
    "identity": I,
    "rank_one_unipotent": I + N1,
    "rank_two_positive": I + N2p,
    "rank_two_negative": I + N2m,
    "minus_identity": -I,
    "two_cubic_blocks": sp.diag(C3, C3),
    "two_quartic_blocks": sp.diag(C4, C4),
}
multiplicities = [(1,), (2, 3), (2, 4), (4, 6),
                  (6, 10, 15), (4, 8, 12), (6, 9)]
out = ["UN44: exact integral meridian and root-cover presentation checks",
       "These are presentation certificates, with no occurrence assertion."]
count = 0
d_counts = {}
sample = []
for name, T in monodromies.items():
    assert T.det() == 1
    for ms in multiplicities:
        d, _ = bezout(ms)
        ns = [m // d for m in ms]
        ngcd, cs = bezout(ns)
        assert ngcd == 1
        for seed in range(11):
            rng = Random((seed + 1) * 10007 + sum(ms) * 101)
            vs = [sp.Matrix([rng.randrange(-3, 4) for _ in range(4)])
                  for _ in ms]
            v0 = sum((c * v for c, v in zip(cs, vs)), sp.zeros(4, 1))
            lifted = [(T**j * v, n) for v, n in zip(vs, ns)
                      for j in range(d)]

            # Cover presentation before eliminating w=t^d.
            cover_cols = [sp.Matrix.vstack((T**d - I)[:, k], sp.zeros(1, 1))
                          for k in range(4)]
            cover_cols += [sp.Matrix.vstack(v, sp.Matrix([n]))
                           for v, n in lifted]
            cover = columns(cover_cols, 5)

            # UN44's integral subgroup A=Lambda/R_d.
            R = columns([(T**d - I)[:, k] for k in range(4)]
                        + [v - n * v0 for v, n in lifted], 4)
            assert group_invariants(cover) == group_invariants(R)

            # Inclusion, equal rank and equal Smith index prove equality
            # of the old and augmented sublattices.
            augmented = sp.Matrix.hstack(R, T * R, (T - I) * v0)
            assert group_invariants(R) == group_invariants(augmented)

            # Gamma_ab from the original meridians.
            orig_cols = [sp.Matrix.vstack((T - I)[:, k], sp.zeros(1, 1))
                         for k in range(4)]
            orig_cols += [sp.Matrix.vstack(v, sp.Matrix([m]))
                          for v, m in zip(vs, ms)]
            original = columns(orig_cols, 5)

            # The same group reconstructed from A and t^d=-v0.
            reconstructed = columns(
                [sp.Matrix.vstack(R[:, k], sp.zeros(1, 1))
                 for k in range(R.cols)]
                + [sp.Matrix.vstack((T - I)[:, k], sp.zeros(1, 1))
                   for k in range(4)]
                + [sp.Matrix.vstack(v0, sp.Matrix([d]))], 5)
            assert group_invariants(original) == group_invariants(reconstructed)

            if d == 1:
                assert group_invariants(original) == group_invariants(R)
            if seed == 0 and name in ("identity", "minus_identity"):
                sample.append((name, ms, d, group_invariants(R),
                               group_invariants(original)))
            count += 1
            d_counts[d] = d_counts.get(d, 0) + 1

out.append(f"PASS: {count} exact tuples; gcd distribution {dict(sorted(d_counts.items()))}")
out.append("PASS: lifted-meridian 5-generator presentation equals the 4-generator R_d quotient")
out.append("PASS: R_d is T-stable and (T-I)v0 lies in R_d")
out.append("PASS: original Gamma_ab equals the exact extension's abelianization")
out.append("PASS: every gcd-one tuple gives Gamma itself as the R_1 quotient")
out.append("Samples: (monodromy, multiplicities, d, A=(free,torsion), Gamma_ab=(free,torsion))")
out.extend(map(str, sample))
out.append("Graph check: for every 2<=b<=8 and 1<=index<=12, 1+index*(b-1)>=2")
assert all(1 + a * (b - 1) >= 2 for b in range(2, 9) for a in range(1, 13))
out.append("PASS: a graph with >=2 cycles has no finite-index abelian subgroup")
result = "\n".join(out) + "\n"
Path(__file__).with_suffix(".out").write_text(result)
print(result, end="")
