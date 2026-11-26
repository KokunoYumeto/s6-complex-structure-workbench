from pathlib import Path
from fractions import Fraction
from itertools import combinations
import json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation3_foundations'
source = (ROOT / 'S6_SERIES_PUBLISH_II.tex').read_text()
start = source.index(r'\subsection{The explicit threefold with identity monodromy}')
end = source.index(r'\subsection{The normal-crossings sign theorem}', start)
path = OUT / 'S6_SERIES_PUBLISH_II_construction_P4_input.tex'
if not path.exists():
    path.write_text(source[start:end])
start = source.rfind(r'\begin{proposition}', 0, source.index(r'\label{cdp:st:D.2.7}'))
end = source.index(r'\end{proof}', start) + len(r'\end{proof}')
path = OUT / 'S6_SERIES_PUBLISH_II_construction_D27_input.tex'
if not path.exists():
    path.write_text(source[start:end] + '\n')

def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]

def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]

def inverse(a):
    n = len(a)
    rows = [[Fraction(x) for x in row] + [Fraction(x) for x in unit]
            for row, unit in zip(a, identity(n))]
    for k in range(n):
        pivot = next(i for i in range(k, n) if rows[i][k])
        rows[k], rows[pivot] = rows[pivot], rows[k]
        value = rows[k][k]
        rows[k] = [x / value for x in rows[k]]
        for i in range(n):
            if i != k:
                value = rows[i][k]
                rows[i] = [x - value * y for x, y in zip(rows[i], rows[k])]
    result = [row[n:] for row in rows]
    assert all(x.denominator == 1 for row in result for x in row)
    return [[int(x) for x in row] for row in result]

def det(a):
    n = len(a)
    rows = [[Fraction(x) for x in row] for row in a]
    value = Fraction(1)
    for k in range(n):
        pivot = next((i for i in range(k, n) if rows[i][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            rows[k], rows[pivot] = rows[pivot], rows[k]
            value = -value
        value *= rows[k][k]
        factor = rows[k][k]
        rows[k] = [x / factor for x in rows[k]]
        for i in range(k + 1, n):
            factor = rows[i][k]
            rows[i] = [x - factor * y for x, y in zip(rows[i], rows[k])]
    assert value.denominator == 1
    return int(value)

pairs = list(combinations(range(4), 2))
def wedge(a):
    return [[a[i][k] * a[j][l] - a[i][l] * a[j][k]
             for k, l in pairs] for i, j in pairs]

def quotient(v):
    pivot = next(i for i, x in enumerate(v) if abs(x) == 1)
    indices = [i for i in range(len(v)) if i != pivot]
    matrix = [[int(i == j) - (v[i] // v[pivot]) * int(j == pivot)
               for j in range(len(v))] for i in indices]
    section = [[int(i == j) for j in indices] for i in range(len(v))]
    assert mul(matrix, section) == identity(len(v) - 1)
    return matrix, section

S = [
    [[0,0,1,0],[0,0,0,1],[1,0,0,0],[0,1,0,0]],
    [[0,-1,0,0],[1,0,0,0],[0,-1,1,0],[1,0,0,1]],
    [[1,0,0,0],[0,1,0,0],[0,-1,1,0],[1,0,0,1]],
]
maps = []
for i, matrix in enumerate(S, 1):
    a = [row[0] for row in matrix]
    eta = [row[0] for row in wedge(matrix)]
    R1 = inverse(matrix)[1:]
    R2 = wedge(inverse(matrix))[1:]
    Q1, H1 = quotient(a)
    Q2, H2 = quotient(eta)
    M1, M2 = mul(R1, H1), mul(R2, H2)
    assert mul(M1, Q1) == R1
    assert mul(M2, Q2) == R2
    assert abs(det(M1)) == abs(det(M2)) == 1
    maps.append(dict(i=i, S=matrix, a=a, eta=eta, Q1=Q1, Q2=Q2,
                     R1=R1, R2=R2, M1=M1, M2=M2,
                     detM1=det(M1), detM2=det(M2)))

def blockdiag(blocks):
    rows = sum(len(b) for b in blocks)
    columns = sum(len(b[0]) for b in blocks)
    result = [[0] * columns for _ in range(rows)]
    r = c = 0
    for b in blocks:
        for i, row in enumerate(b):
            for j, value in enumerate(row):
                result[r+i][c+j] = value
        r += len(b)
        c += len(b[0])
    return result

def mv(kind):
    F1 = [[0] * 15 for _ in range(15)]
    F2 = [[0] * 30 for _ in range(29)]
    gs = [[1,0,0,0], [0,0,0,0], [0,0,0,0]]
    vs = [[1,0], [0,1], [-1,-1]]
    for i in range(3):
        r1, r2 = maps[i][kind+'1'], maps[i][kind+'2']
        for j in range(4):
            F1[j][i*5+j] = 1
            F1[j][i*5+4] = gs[i][j]
        for j in range(2):
            F1[4+j][i*5+4] = vs[i][j]
        for j in range(3):
            for k in range(4):
                F1[6+i*3+j][i*5+k] = -r1[j][k]
        for j in range(6):
            F2[j][i*10+j] = 1
        for j in range(4):
            for k, (a,b) in enumerate(pairs):
                F2[k][i*10+6+j] = int(a == j) * gs[i][b] - int(b == j) * gs[i][a]
            for k in range(2):
                F2[6+k*4+j][i*10+6+j] = vs[i][k]
        for j in range(5):
            for k in range(6):
                F2[14+i*5+j][i*10+k] = -r2[j][k]
    return F1, F2

early1, early2 = mv('Q')
late1, late2 = mv('R')
transport1 = blockdiag([identity(6)] + [row['M1'] for row in maps])
transport2 = blockdiag([identity(14)] + [row['M2'] for row in maps])
assert mul(transport1, early1) == late1
assert mul(transport2, early2) == late2
assert det(early1) == 1 and det(late1) == -1 and det(transport1) == -1
result = dict(local_maps=maps, det_F1_Q=det(early1), det_F1_R=det(late1),
              det_transport1=det(transport1), det_transport2=det(transport2),
              relation='F1_R=diag(I6,M1_i)F1_Q; F2_R=diag(I14,M2_i)F2_Q; identical source bases',
              scope='Dependent coordinate derivation from the already exposed proofs; not an independent required check or rerun of either original program.')
(OUT / 'S6_SERIES_PUBLISH_construction_basis_maps.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
