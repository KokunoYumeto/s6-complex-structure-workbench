#!/usr/bin/env python3
"""Exact coherent incidence and dual residue maps for reduced Hopf supports."""
from sympy import Matrix, Rational, symbols, factor


def incidence(vertices, edges, left, right):
    rows = []
    for (a, b), x, y in zip(edges, left, right):
        row = [0] * vertices
        row[a], row[b] = x, -y
        rows.append(row)
    return Matrix(rows)


def ordinary(vertices, edges):
    return incidence(vertices, edges, [1] * len(edges), [1] * len(edges))


# A genuine branched unicycle: a triangle, a two-step tail, and another leaf.
edges = [(0, 1), (1, 2), (2, 0), (1, 3), (3, 4), (2, 5)]
vertices = 6
values = [Rational(2), Rational(3), Rational(5), Rational(7), Rational(11),
          Rational(13)]
left = [Rational(17 + j) for j in range(len(edges))]
right = [left[j] * values[a] / values[b] for j, (a, b) in enumerate(edges)]
d0, d1 = ordinary(vertices, edges), incidence(vertices, edges, left, right)
assert d0.rank() == d1.rank() == vertices - 1
assert d1 * Matrix(values) == Matrix.zeros(len(edges), 1)
residue = d1.T.nullspace()[0]
assert all(residue[j] != 0 for j in range(3))
assert all(residue[j] == 0 for j in range(3, len(edges)))
h0 = vertices - d0.rank()
h1 = len(edges) - d0.rank() + vertices - d1.rank()
h2 = len(edges) - d1.rank()
assert (h0, h1, h2) == (1, 2, 1)
print("BRANCHED UNICYCLE")
print("edges =", edges)
print("actual restriction matrix =", d1.tolist())
print("ranks(d0,d1) =", (d0.rank(), d1.rank()))
print("coherent dimensions =", (h0, h1, h2))
print("dual residue vector =", list(residue))
print("tree residues vanish exactly; cycle residues are all nonzero")

# Change the one surviving holonomy, retaining every coefficient nonzero.
bad_right = right[:]
bad_right[2] *= 2
bad = incidence(vertices, edges, left, bad_right)
assert bad.rank() == vertices
assert len(edges) - bad.rank() == 0
print("NONTRIVIAL CYCLE HOLONOMY: rank =", bad.rank(), "; h2 = 0")

# Symbolic actual two-component/two-curve map, with arbitrary restrictions.
a, b, c, d = symbols("a b c d", nonzero=True)
two = Matrix([[a, -b], [c, -d]])
assert factor(two.det()) == -a*d + b*c
print("TWO COMPONENTS: determinant =", factor(two.det()),
      "; vanishes precisely when (a/b)*(d/c)=1")

# The same maps on cycles of arbitrary tested length, with irregular tails.
checked = 0
for cycle in range(2, 9):
    for tail in range(0, 5):
        e = ([(0, 1), (1, 0)] if cycle == 2 else
             [(j, (j + 1) % cycle) for j in range(cycle)])
        for j in range(tail):
            e.append((0 if j == 0 else cycle + j - 1, cycle + j))
        n = cycle + tail
        val = [Rational(j + 2, j + 3) for j in range(n)]
        le = [Rational(2*j + 3, j + 2) for j in range(len(e))]
        ri = [le[j] * val[x] / val[y] for j, (x, y) in enumerate(e)]
        mat = incidence(n, e, le, ri)
        assert mat.rank() == n - 1
        dual = mat.T.nullspace()
        assert len(dual) == 1
        assert all(dual[0][j] != 0 for j in range(cycle))
        assert all(dual[0][j] == 0 for j in range(cycle, len(e)))
        # Remove the closing cycle edge: the actual weighted tree map is onto.
        tree_rows = [j for j in range(len(e)) if j != cycle - 1]
        tree = mat[tree_rows, :]
        assert tree.rank() == n - 1
        checked += 1
print("EXACT CYCLE/TAIL AND TREE CASES PASSED =", checked)
print("ALL CHECKS PASSED")
