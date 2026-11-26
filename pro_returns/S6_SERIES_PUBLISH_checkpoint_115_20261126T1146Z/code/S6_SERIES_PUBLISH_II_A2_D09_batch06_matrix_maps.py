"""Post-reading exact preservation of the XD matrix dump and GE/DF bases.

This is an editorial comparison, written after the original proofs and historical
programs were read. It earns no independent derivation credit. Historical
producers are not imported or executed. Downloads remain outside current.
"""
from pathlib import Path
from itertools import combinations
import hashlib
import json
import re
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / 'agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_D09_D04_batch06_working'
TEMP = ROOT.parents[1] / 'S6_SERIES_PUBLISH_A_primary_temp/D09_batch06'
I = s.eye(4)
e = list(I.columnspace())
pairs = list(combinations(range(4), 2))

def wedge(v, w):
    return s.Matrix([v[a]*w[b]-v[b]*w[a] for a, b in pairs])

def exterior(A):
    return s.Matrix.hstack(*(wedge(A[:, a], A[:, b]) for a, b in pairs))

def smith(A):
    D = smith_normal_form(A, domain=s.ZZ)
    return [abs(int(D[i, i])) for i in range(min(D.shape)) if D[i, i]]

markings = [s.Matrix.hstack(e[2], e[3], e[0], e[1]),
            s.Matrix.hstack(e[1]+e[3], -e[0]-e[2], e[2], e[3]),
            s.Matrix.hstack(e[0]+e[3], e[1]-e[2], e[2], e[3])]
R1 = [A.inv()[1:, :] for A in markings]
R2 = [exterior(A.inv())[1:, :] for A in markings]
meridians = [s.Matrix([1, 0]), s.Matrix([0, 1]), s.Matrix([-1, -1])]
clutches = [e[0], s.zeros(4, 1), s.zeros(4, 1)]

def mv_maps(local1, local2):
    F1, F2 = s.zeros(15, 15), s.zeros(29, 30)
    for i in range(3):
        F1[:4, 5*i:5*i+4] = I
        F1[:4, 5*i+4] = clutches[i]
        F1[4:6, 5*i+4] = meridians[i]
        F1[6+3*i:9+3*i, 5*i:5*i+4] = -local1[i]
        F2[:6, 10*i:10*i+6] = s.eye(6)
        F2[14+5*i:19+5*i, 10*i:10*i+6] = -local2[i]
        for j in range(4):
            F2[:6, 10*i+6+j] = wedge(e[j], clutches[i])
            F2[6+j, 10*i+6+j] = meridians[i][0]
            F2[10+j, 10*i+6+j] = meridians[i][1]
    return F1, F2

F1, F2 = mv_maps(R1, R2)
F0 = s.Matrix([[1, 1, 1], [-1, 0, 0], [0, -1, 0], [0, 0, -1]])
d1, d2, d3, d4 = s.zeros(1, 4), s.zeros(4, 7), s.zeros(7, 6), s.zeros(6, 2)
d2[0, 6], d3[0, 4] = 1, 1
classes = [wedge(A[:, 0], A[:, 1]) for A in markings]
H1 = s.Matrix.hstack(e[0], *(A[:, 0] for A in markings))
H2 = s.Matrix.hstack(*(wedge(e[0], e[j]) for j in range(1, 4)), *classes)
generated = {'local_d1': d1, 'local_d2': d2, 'local_d3': d3, 'local_d4': d4,
             'MV_F0': F0, 'MV_F1': F1, 'MV_F2': F2,
             'H1_reduced_relation_matrix': H1, 'H2_reduced_relation_matrix': H2}
generated.update({f'S_{i+1}': A for i, A in enumerate(markings)})
generated.update({f'R1_{i+1}': A for i, A in enumerate(R1)})
generated.update({f'R2_{i+1}': A for i, A in enumerate(R2)})
assert len(generated) == 18

original = (WORK / 'S6_SERIES_PUBLISH_II_A2_02XD_following_before.tex').read_text()
parsed = {}
renames = {r'\partial_' + str(i): 'local_d' + str(i) for i in range(1, 5)}
renames.update({'F_' + str(i): 'MV_F' + str(i) for i in range(3)})
renames.update({'R_{H_1}': 'H1_reduced_relation_matrix', 'R_{H_2}': 'H2_reduced_relation_matrix'})
for i in range(1, 4):
    renames[f'R_{{1,{i}}}'] = f'R1_{i}'
    renames[f'R_{{2,{i}}}'] = f'R2_{i}'
for name, body in re.findall(r'\\displaystyle\s+([^=]+)=\\begin\{pmatrix\}(.*?)\\end\{pmatrix\}', original, re.S):
    name = name.strip()
    rows = [[int(x.strip()) for x in row.split('&')] for row in body.strip().split(r'\\') if row.strip()]
    parsed[renames.get(name, name)] = s.Matrix(rows)
assert set(parsed) == set(generated)
historical = json.loads((TEMP / 'example_matrices.json').read_text())
assert set(historical) == set(generated)
for name, A in generated.items():
    assert A == parsed[name] == s.Matrix(historical[name]), name
    print('Exact old TeX / generating formula / historical output:', name, tuple(A.shape))
assert d1*d2 == s.zeros(1, 7)
assert d2*d3 == s.zeros(4, 6)
assert d3*d4 == s.zeros(7, 2)
assert (F1.det(), H1.det(), H2.det()) == (-1, -1, 1)
assert smith(F1) == [1]*15 and smith(F2) == [1]*29
print('XD determinants: F1=-1, RH1=-1, RH2=1; Smith factors: 15 and 29 units.')

# The GE proof uses first-unit-pivot quotient coordinates, not the local
# ordered product coordinates of XD. Give both exact maps and their inverses.
def quotient(v):
    p = next(i for i in range(v.rows) if abs(v[i]) == 1)
    Q = s.zeros(v.rows-1, v.rows)
    for k, j in enumerate(i for i in range(v.rows) if i != p):
        Q[k, j] = 1
        Q[k, p] = -v[j]/v[p]
    assert Q*v == s.zeros(v.rows-1, 1)
    return Q

Q1 = [quotient(A[:, 0]) for A in markings]
Q2 = [quotient(c) for c in classes]
change1 = [Q*A[:, 1:] for Q, A in zip(Q1, markings)]
change2 = [Q*exterior(A)[:, 1:] for Q, A in zip(Q2, markings)]
for degree, Cs, Rs, Qs in [(1, change1, R1, Q1), (2, change2, R2, Q2)]:
    for i, (C, R, Q) in enumerate(zip(Cs, Rs, Qs), 1):
        assert C*R == Q
        assert abs(C.det()) == 1
        assert C.inv()*Q == R
        print('GE <- XD local basis map', degree, i, 'C=', C.tolist(), 'inverse=', C.inv().tolist(), 'det=', C.det())
G1, G2 = mv_maps(Q1, Q2)
B1, B2 = s.diag(s.eye(6), *change1), s.diag(s.eye(14), *change2)
assert G1 == B1*F1 and G2 == B2*F2
assert G1.det() == 1 and B1.det() == -1
assert smith(G1) == [1]*15 and smith(G2) == [1]*29
print('GE matrices equal block-diagonal quotient changes times XD matrices; det(B1)=-1; det(G1)=+1.')

# Preserve the alternate invariant basis in UN36 and its exact congruence.
Q = s.zeros(6)
Q[0, 5] = Q[5, 0] = 1
Q[1, 4] = Q[4, 1] = -1
Q[2, 3] = Q[3, 2] = 1
f = [s.eye(6)[:, i] for i in range(6)]
for eps in [1, -1]:
    old = s.Matrix.hstack(f[0], f[1], -eps*f[2]+f[3], f[5])
    C = s.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, -eps], [0, 1, 0, 0]])
    new = s.Matrix.hstack(f[0], f[5], f[1], f[2]-eps*f[3])
    assert old*C == new
    expected = s.Matrix([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, -2*eps]])
    assert C.T*(old.T*Q*old)*C == new.T*Q*new == expected
    T = s.eye(4); T[0, 1] = 1; T[2, 3] = eps
    assert (exterior(T)-s.eye(6))*new == s.zeros(6, 4)
    assert (exterior(T)-s.eye(6)).rank() == 2
    print('UN36 epsilon=', eps, ': exact basis permutation/sign and Gram congruence hold.')
print('PASS: post-reading editorial matrix and basis preservation only; no independent proof event.')
