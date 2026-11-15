"""Exact integral Wang maps and quotient cohomology for C.2.UN.21.

The input actions are realized by the geometric cycles in C.SK.8:
two invariant lifted base surfaces and two negative circle tori.
This script checks their Smith maps, not the existence of those cycles.
"""
import itertools
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def wang(signs):
    """Homology of the mapping torus of integral diagonal involutions."""
    free = []
    torsion = []
    for k in range(len(signs) + 1):
        current = signs[k] if k < len(signs) else []
        previous = signs[k - 1] if k else []
        matrix = s.diag(*[x - 1 for x in current]) if current else s.zeros(0)
        smith = smith_normal_form(matrix, domain=ZZ)
        diagonal = [abs(int(smith[i, i])) for i in range(len(current))]
        cokernel_free = diagonal.count(0)
        kernel_previous = previous.count(1)
        free.append(cokernel_free + kernel_previous)
        torsion.append([x for x in diagonal if x > 1])
        print("Wang H", k, "map diagonal=", [x-1 for x in current],
              "Smith=", diagonal, "free=", free[-1],
              "torsion=", torsion[-1])
    # UCT: the torsion of H^k is that of H_{k-1}.
    cohomology_torsion = [[]] + torsion[:-1]
    return free, torsion, cohomology_torsion


m5 = [[1], [-1, -1], [1, 1, -1, -1],
      [1, 1, -1, -1], [-1, -1], [1]]
assert list(map(len, m5)) == [1, 2, 4, 4, 2, 1]
print("Compact Y from the M5 mapping torus:")
by, hy_tor, cy_tor = wang(m5)
assert by == [1, 1, 2, 4, 2, 1, 1]
assert hy_tor == [[], [2, 2], [2, 2], [2, 2], [2, 2], [], []]
assert cy_tor == [[], [], [2, 2], [2, 2], [2, 2], [2, 2], []]

m3 = [[1], [-1, -1], [-1, -1], [1]]
print("\nSecondary Kodaira P from the M3 mapping torus:")
bp, hp_tor, cp_tor = wang(m3)
assert bp == [1, 1, 0, 1, 1]
assert hp_tor == [[], [2, 2], [2, 2], [], []]
assert cp_tor == [[], [], [2, 2], [2, 2], []]

# Cohomological Mayer--Vietoris, P union Q along J:
bq = [1, 1, 0, 1, 1]
bj = [1, 2, 1, 0, 0]
restriction_rank = [1, 1, 0, 0, 0]
bs = [bp[k] + bq[k] - restriction_rank[k]
      + (bj[k-1]-restriction_rank[k-1] if k else 0)
      for k in range(5)]
assert bs == [1, 1, 1, 3, 2]
print("\nReduced support rational ranks:", bs)
print("Restriction ranks P+Q -> J:", restriction_rank)

# The invariant Seifert-surface mapping torus proves the integral
# H2(J)->H2(P) restriction is zero, including its torsion target.
# In H1, allow every possible torsion choice for the radial lift.
for e1, e2 in itertools.product([0, 1], repeat=2):
    # Generators p, t1, t2, q; relations 2t1,2t2,p+e1t1+e2t2-q.
    relations = s.Matrix([[0, 2, 0, 0], [0, 0, 2, 0],
                          [1, e1, e2, -1]])
    smith = smith_normal_form(relations, domain=ZZ)
    diagonal = [abs(int(smith[i,i])) for i in range(3)]
    assert diagonal == [1, 2, 2]
hs_tor = [[], [2, 2], [2, 2], [], []]
cs_tor = [[]] + hs_tor[:-1]
assert cs_tor == [[], [], [2, 2], [2, 2], []]
print("Integral support homology torsion:", hs_tor)
print("Integral support cohomology torsion:", cs_tor)
print("Every radial torsion lift has the same primitive Smith quotient.")

# At infinity, inversion on the first E and translation on the second:
real_h1_signs = [-1, -1, 1, 1]
bb = [sum(s.prod(real_h1_signs[i] for i in subset) == 1
          for subset in itertools.combinations(range(4), k))
      for k in range(5)]
assert bb == [1, 2, 2, 2, 1]
print("Bielliptic B rational ranks:", bb)
print("\nBielliptic B via T(-1_E) times a circle:")
b3, h3_tor, c3_tor = wang([[1], [-1, -1], [1]])
bb_from_wang = [b3[k] if k < len(b3) else 0 for k in range(5)]
bb_tor = [h3_tor[k].copy() if k < len(h3_tor) else [] for k in range(5)]
for k in range(1, 5):
    bb_from_wang[k] += b3[k-1]
    bb_tor[k] += h3_tor[k-1]
assert bb_from_wang == bb
assert [[]] + bb_tor[:-1] == [[], [], [2, 2], [2, 2], []]
print("B cohomology torsion:", [[]] + bb_tor[:-1])

# Coherent reduced central union:
hop = [1, 1, 0]
hoq = [1, 1, 0]
hoj = [1, 1, 0]
coherent_rank = [1, 1, 0]
hos = [hop[k]+hoq[k]-coherent_rank[k]
       + (hoj[k-1]-coherent_rank[k-1] if k else 0)
       for k in range(3)]
assert hos == [1, 1, 0]

# Original reduced fibre upstairs has h(O)=(1,2,1).
# On C[t]/(t^2)e, g(t)=-t and g(e)=epsilon e.
coherent_central_signs = [[1], [-1, 1], [-1]]
full_fibre_invariants = [
    sum(int(epsilon == 1)+int(-epsilon == 1) for epsilon in row)
    for row in coherent_central_signs]
assert full_fibre_invariants == [1, 2, 1]
print("Reduced support h(O):", hos)
print("Full doubled fibre h(O):", full_fibre_invariants)
print("Each signed C[t]/t^2 summand has exactly one invariant basis vector.")

# Leray signs over V, H^q(O_V)=(C,C,0), with (-1) on H^1.
# The global elliptic R^1(O) frame is invariant.
ho_y_signs = [[1], [-1, 1], [-1], []]
ho_y = [row.count(1) for row in ho_y_signs]
assert ho_y == [1, 1, 0, 0]
print("Compact Y h(O):", ho_y)

euler = lambda b: sum((-1)**k * x for k, x in enumerate(b))
assert all(euler(b) == 0 for b in [by, bp, bq, bj[:3], bs, bb])
assert all((-1)**k*by[k] == (-1)**(6-k)*by[6-k]
           for k in range(7))
print("All Euler numbers vanish; all Smith and invariant checks passed.")
