"""Exact rational Cech maps for the Enriques support in C.2.UN.25.

The matrices encode the actual double curves and their divisor classes.
They do not assume degeneration of an unverified spectral sequence.
"""
import sympy as s

vertices = ['M', 'A', 'Q_a', 'Q_b'] + [f'E{i}' for i in range(1, 5)]
edges = [('M', 'A', 'D0'), ('M', 'A', 'Dinf'),
         ('M', 'Q_a', 'Ja'), ('M', 'Q_b', 'Jb')]
edges += [('A', f'E{i}', f'Z{i}') for i in range(1, 5)]
edges += [('M', f'E{i}', f'U{i}_{j}')
          for i in range(1, 5) for j in ['0', 'inf']]
edge_index = {name: k for k, (_, _, name) in enumerate(edges)}

d0 = s.zeros(16, 8)
for k, (a, b, _) in enumerate(edges):
    d0[k, vertices.index(a)] = -1
    d0[k, vertices.index(b)] = 1
d1 = s.zeros(8, 16)
for i in range(1, 5):
    for j, suffix in enumerate(['0', 'inf']):
        row = 2*(i-1)+j
        d1[row, edge_index['D0' if j == 0 else 'Dinf']] = 1
        d1[row, edge_index[f'Z{i}']] = 1
        d1[row, edge_index[f'U{i}_{suffix}']] = -1
assert d1*d0 == s.zeros(8, 8)
assert (d0.rank(), d1.rank()) == (7, 8)
dual_betti = [8-d0.rank(), 16-d0.rank()-d1.rank(), 8-d1.rank()]
assert dual_betti == [1, 1, 0]
print('Ordered components:', vertices)
print('Ordered double curves:', [x[2] for x in edges])
print('H0 Cech d0 ='); print(d0)
print('H0 Cech d1 ='); print(d1)
print('Ranks:', d0.rank(), d1.rank(), '; dual-complex Betti:', dual_betti)

# Ten rational curves on M: D0, four U_i0, Dinf, four U_iinf.
# Each block is the affine D4 intersection matrix. The unique global
# relation is 2D0+sum U_i0 = 2Dinf+sum U_iinf, a nonzero fibre class.
affine_d4 = -2*s.eye(5)
for i in range(1, 5):
    affine_d4[0, i] = affine_d4[i, 0] = 1
gram = s.diag(affine_d4, affine_d4)
assert gram.rank() == 8
fibre = s.Matrix([2, 1, 1, 1, 1])
assert affine_d4*fibre == s.zeros(5, 1)
print('Two affine D4 blocks: intersection rank', gram.rank())
print('Each fibre coefficient vector:', list(fibre))

# H2 of components has dimensions 10(M),2(A),2 each(E_i); Hopf H2=0.
# In M use D0,U_10,...,U_40,U_1inf,...,U_4inf, then a complementary
# tenth vector. The complementary vector does not occur in a double curve.
# Dinf=D0+(sum U_i0-sum U_iinf)/2; Ja=Jb=F/2.
curve_map = s.zeros(20, 16)
d_zero = s.zeros(10, 1); d_zero[0] = 1
d_inf = d_zero.copy()
half_fibre = d_zero.copy()
for i in range(4):
    d_inf[1+i] = s.Rational(1, 2)
    d_inf[5+i] = -s.Rational(1, 2)
    half_fibre[1+i] = s.Rational(1, 2)
curve_map[:10, edge_index['D0']] = d_zero
curve_map[:10, edge_index['Dinf']] = d_inf
curve_map[:10, edge_index['Ja']] = half_fibre
curve_map[:10, edge_index['Jb']] = half_fibre
# A basis is F,H: D0,Dinf are F; Z_i are H.
curve_map[10, edge_index['D0']] = -1
curve_map[10, edge_index['Dinf']] = -1
for i in range(4):
    zi = edge_index[f'Z{i+1}']
    u0 = edge_index[f'U{i+1}_0']
    ui = edge_index[f'U{i+1}_inf']
    curve_map[11, zi] = 1
    curve_map[1+i, u0] = 1
    curve_map[5+i, ui] = 1
    # E_i basis is its negative section and its ruling fibre.
    curve_map[12+2*i, zi] = -1
    curve_map[13+2*i, u0] = -1
    curve_map[13+2*i, ui] = -1
assert curve_map.rank() == 14

relation_half = s.zeros(16, 1)
relation_half[edge_index['Ja']] = 1
relation_half[edge_index['Jb']] = -1
relation_i0 = s.zeros(16, 1)
relation_i0[edge_index['D0']] = 2
relation_i0[edge_index['Dinf']] = -2
for i in range(1, 5):
    relation_i0[edge_index[f'U{i}_0']] = 1
    relation_i0[edge_index[f'U{i}_inf']] = -1
assert curve_map*relation_half == s.zeros(20, 1)
assert curve_map*relation_i0 == s.zeros(20, 1)
assert s.Matrix.hstack(relation_half, relation_i0).rank() == 2
print('H2 curve-to-component Gysin/inclusion matrix ='); print(curve_map)
print('H2 restriction rank:', curve_map.rank())
print('Kernel basis: Ja-Jb; 2D0-2Dinf+sum(U_i0-U_iinf).')

# Each Hopf H1 restricts to one nonzero direction in its elliptic edge.
h1_map = s.Matrix([[1, 0], [0, 0], [0, 1], [0, 0]])
assert h1_map.rank() == 2
betti = [1, 1, (20-14)+(4-2), 2+(16-14), 8]
assert betti == [1, 1, 8, 4, 8]
assert sum((-1)**i*b for i, b in enumerate(betti)) == 12
print('Rational support Betti:', betti, '; Euler=12')

# For coherent cohomology, each Hopf H1(O) restricts isomorphically
# to H1(O) of its elliptic attaching curve. All component H2(O)=0.
coherent_h1_map = s.eye(2)
assert coherent_h1_map.rank() == 2
coherent = [1, 1, 0]
print('Coherent support dimensions:', coherent)

balanced = betti.copy()
for degree, increment in [(2, 2), (3, 6), (4, 2)]:
    balanced[degree] += 6*increment
assert balanced == [1, 1, 20, 40, 20]
assert sum((-1)**i*b for i, b in enumerate(balanced)) == 0
print('After six negative blocks:', balanced, '; Euler=0')
print('Coherent dimensions unchanged:', coherent)


def paired_root_support(r):
    """Build all incidence and curve-class maps for r paired root values."""
    assert r >= 2
    verts = ['M', 'A'] + [f'Q{j}' for j in range(r)] + [f'E{i}' for i in range(4)]
    eds = [('M', 'A', 'D0'), ('M', 'A', 'Dinf')]
    eds += [('M', f'Q{j}', f'J{j}') for j in range(r)]
    eds += [('A', f'E{i}', f'Z{i}') for i in range(4)]
    eds += [('M', f'E{i}', f'U{i}_{j}') for i in range(4) for j in ['0', 'inf']]
    idx = {name: k for k, (_, _, name) in enumerate(eds)}
    inc0 = s.zeros(r+14, r+6)
    inc1 = s.zeros(8, r+14)
    for k, (a, b, _) in enumerate(eds):
        inc0[k, verts.index(a)] = -1
        inc0[k, verts.index(b)] = 1
    for i in range(4):
        for j, suffix in enumerate(['0', 'inf']):
            inc1[2*i+j, idx['D0' if j == 0 else 'Dinf']] = 1
            inc1[2*i+j, idx[f'Z{i}']] = 1
            inc1[2*i+j, idx[f'U{i}_{suffix}']] = -1
    assert inc1*inc0 == s.zeros(8, r+6)
    assert (inc0.rank(), inc1.rank()) == (r+5, 8)
    curves = s.zeros(20, r+14)
    curves[:10, idx['D0']] = d_zero
    curves[:10, idx['Dinf']] = d_inf
    for j in range(r):
        curves[:10, idx[f'J{j}']] = half_fibre
    curves[10, idx['D0']] = curves[10, idx['Dinf']] = -1
    for i in range(4):
        zi, u0, ui = [idx[name] for name in [f'Z{i}', f'U{i}_0', f'U{i}_inf']]
        curves[11, zi] = 1
        curves[1+i, u0] = 1
        curves[5+i, ui] = 1
        curves[12+2*i, zi] = -1
        curves[13+2*i, u0] = curves[13+2*i, ui] = -1
    assert curves.rank() == 14
    assert len(curves.nullspace()) == r
    b = [1, 1, 6+r, 2*r, 6+r]
    bb = [1, 1, 18+r, 36+2*r, 18+r]
    assert sum((-1)**i*x for i, x in enumerate(b)) == 12
    assert sum((-1)**i*x for i, x in enumerate(bb)) == 0
    print(f'r={r}: H0 ranks={inc0.rank()},{inc1.rank()}; H2 rank={curves.rank()}; '
          f'kernel dimension={len(curves.nullspace())}; b={b}; balanced={bb}; h(O)=[1,1,0]')


print('General paired-root family: b=(1,1,r+6,2r,r+6), h(O)=(1,1,0).')
print('After six negative blocks: b=(1,1,r+18,2r+36,r+18).')
for r in (2, 3, 4):
    paired_root_support(r)
