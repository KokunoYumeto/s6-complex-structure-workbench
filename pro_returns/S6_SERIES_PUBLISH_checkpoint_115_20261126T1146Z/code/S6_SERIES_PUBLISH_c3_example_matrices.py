"""Compare every printed matrix with the defining maps before deleting duplicates."""
from pathlib import Path
import itertools
import re
import csv
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

ROOT = Path(__file__).resolve().parents[1]
text = (ROOT / 'S6_SERIES_PUBLISH_II.tex').read_text()
marker = 'The program \\texttt{code/part4/example\\_mayer\\_vietoris.py}'
if marker in text:
    start = text.index(marker)
    stop = text.index('\\begin{proposition}[Invariants of the compact torus fibration]', start)
    dump = text[start:stop]
else:
    with (ROOT / 'S6_SERIES_PUBLISH_defects_II.tsv').open() as f:
        rows = csv.DictReader(f, delimiter='\t')
        dump = next(row['old_text'] for row in rows if row['change_id'] == 'II-C3-IDENTITY-ARRAY-DUPLICATES-01')
printed = {}
for name, body in re.findall(r'\\displaystyle\s+([^=]+)=\\begin\{pmatrix\}(.*?)\\end\{pmatrix\}', dump, re.S):
    rows = [[s.Integer(x.strip()) for x in row.split('&')] for row in body.split('\\\\') if row.strip()]
    printed[name.strip()] = s.Matrix(rows)

pairs = list(itertools.combinations(range(4), 2))

def wedge(x, y):
    return s.Matrix([x[i] * y[j] - x[j] * y[i] for i, j in pairs])

def exterior(matrix):
    return s.Matrix.hstack(*(wedge(matrix[:, i], matrix[:, j]) for i, j in pairs))

S = [s.Matrix([[0,0,1,0],[0,0,0,1],[1,0,0,0],[0,1,0,0]]),
     s.Matrix([[0,-1,0,0],[1,0,0,0],[0,-1,1,0],[1,0,0,1]]),
     s.Matrix([[1,0,0,0],[0,1,0,0],[0,-1,1,0],[1,0,0,1]])]
expected = {}
R1, R2 = [], []
for i, matrix in enumerate(S, 1):
    assert matrix.det() == 1
    inv = matrix.inv()
    assert inv * matrix == s.eye(4)
    expected[f'S_{i}'] = matrix
    R1.append(inv[1:, :])
    R2.append(exterior(inv)[1:, :])
    expected[f'R_{{1,{i}}}'] = R1[-1]
    expected[f'R_{{2,{i}}}'] = R2[-1]

expected['\\partial_1'] = s.zeros(1, 4)
expected['\\partial_2'] = s.zeros(4, 7)
expected['\\partial_2'][0, 6] = 1
expected['\\partial_3'] = s.zeros(7, 6)
expected['\\partial_3'][0, 4] = 1
expected['\\partial_4'] = s.zeros(6, 2)
for i in [1, 2, 3]:
    assert expected[f'\\partial_{i}'] * expected[f'\\partial_{i+1}'] == s.zeros(expected[f'\\partial_{i}'].rows, expected[f'\\partial_{i+1}'].cols)

F0 = s.Matrix([[1,1,1],[-1,0,0],[0,-1,0],[0,0,-1]])
F1 = s.zeros(15, 15)
F2 = s.zeros(29, 30)
g = [s.eye(4)[:, 0], s.zeros(4, 1), s.zeros(4, 1)]
v = [s.Matrix([1,0]), s.Matrix([0,1]), s.Matrix([-1,-1])]
for i in range(3):
    F1[:4, 5*i:5*i+4] = s.eye(4)
    F1[:4, 5*i+4] = g[i]
    F1[4:6, 5*i+4] = v[i]
    F1[6+3*i:9+3*i, 5*i:5*i+4] = -R1[i]
    F2[:6, 10*i:10*i+6] = s.eye(6)
    for j in range(4):
        F2[:6, 10*i+6+j] = wedge(s.eye(4)[:, j], g[i])
        for k in range(2):
            F2[6+4*k+j, 10*i+6+j] = v[i][k]
    F2[14+5*i:19+5*i, 10*i:10*i+6] = -R2[i]

expected.update({'F_0': F0, 'F_1': F1, 'F_2': F2})
RH1 = s.Matrix.hstack(s.eye(4)[:, 0], *(x[:, 0] for x in S))
RH2 = s.Matrix.hstack(*(wedge(s.eye(4)[:, 0], s.eye(4)[:, j]) for j in [1,2,3]), *(wedge(x[:, 0], x[:, 1]) for x in S))
expected['R_{H_1}'] = RH1
expected['R_{H_2}'] = RH2
assert set(expected) == set(printed)
for name, matrix in expected.items():
    assert matrix == printed[name], name
    print(f'{name}: all {matrix.rows * matrix.cols} entries agree with the defining maps')
assert (RH1.det(), RH2.det(), F1.det(), F0.rank()) == (-1, 1, -1, 3)
for name, matrix in [('F_1', F1), ('F_2', F2)]:
    diag = smith_normal_form(matrix, domain=s.ZZ)
    factors = [abs(diag[i,i]) for i in range(min(diag.shape))]
    assert all(x == 1 for x in factors)
    print(f'{name}: {len(factors)} unit Smith factors')
print('All 18 matrices, quotient bases, differential composites and determinant assertions agree. No geometric proof is inferred from this comparison.')
