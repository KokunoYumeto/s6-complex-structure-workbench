"""Reconstruct the entire OS45 cubic from the sixteen toric surfaces.

The input is the six marked boundary divisors on each dP6, the periodic
vertices, and the actual half-class restriction. No historical program,
tensor or verification output is imported. This does not evaluate the
missing framed odd three-cycle or reconstruct the separate core matrix.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction as F
import hashlib, json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

R = Path(__file__).resolve().parents[1]
checks = 0

def require(test, label):
    global checks
    checks += 1
    assert test, label

def add(a, b): return tuple(x+y for x, y in zip(a, b))
def scale(n, a): return tuple(n*x for x in a)
def intersect(a, b): return a[0]*b[0] - sum(a[i]*b[i] for i in range(1, 4))

zero = (0, 0, 0, 0)
boundary = [(0, 1, 0, 0), (1, -1, -1, 0), (0, 0, 1, 0),
            (1, 0, -1, -1), (0, 0, 0, 1), (1, -1, 0, -1)]
rays = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]
canonical = scale(-1, tuple(sum(v[k] for v in boundary) for k in range(4)))
fibre = (1, -1, 0, 0)
vertices = list(product(range(8), range(2)))
vertex_index = {v: i for i, v in enumerate(vertices)}
restrictions = []
for i, (r, s) in enumerate(vertices):
    row = [zero for _ in vertices]
    row[i] = canonical
    for ray, divisor in zip(rays, boundary):
        target = ((r+ray[0]) % 8, (s+ray[1]) % 2)
        j = vertex_index[target]
        row[j] = add(row[j], divisor)
    require(tuple(sum(v[k] for v in row) for k in range(4)) == zero,
            'full fibre divisor restricts to zero')
    y = scale((-1)**s, fibre)
    require(scale(2, y) == tuple(sum(row[2*t+1][k] for t in range(8)) for k in range(4)),
            'literal integral half-class on each normalization')
    require(intersect(y, y) == 0, 'half-class square on each normalization')
    restrictions.append(row)

def geometric(i, j, k):
    return intersect(restrictions[i][j], restrictions[i][k])

triangles = set()
for r, s in vertices:
    a = vertex_index[r, s]
    b = vertex_index[(r+1) % 8, s]
    c = vertex_index[r, (s+1) % 2]
    d = vertex_index[(r+1) % 8, (s+1) % 2]
    triangles.add(tuple(sorted((a, b, c))))
    triangles.add(tuple(sorted((b, c, d))))

def printed_component(i, j, k):
    if i == j == k:
        return 6
    unique = set((i, j, k))
    if len(unique) == 2:
        repeated = i if i == j or i == k else j
        other = next(x for x in unique if x != repeated)
        r, s = vertices[repeated]; rr, ss = vertices[other]
        return -2 if r == rr else (-1 if (rr-r) % 8 in (1, 7) else 0)
    return int(tuple(sorted((i, j, k))) in triangles)

component = {}
for i, j, k in product(range(16), repeat=3):
    value = geometric(i, j, k)
    require(value == geometric(j, i, k) == geometric(k, i, j), 'all component symmetries')
    require(value == printed_component(i, j, k), 'all4096 component entries')
    if value: component[i, j, k] = value
for j, k in product(range(16), repeat=2):
    require(sum(geometric(i, j, k) for i in range(16)) == 0, 'fibre relation in every cubic slot')

# Columns are component classes in the declared primitive basis.
B = sp.zeros(15, 16)
for i in range(14): B[i, i] = 1
for i in range(14): B[i, 14 + (i % 2)] = -1
B[14, 14] = -2; B[14, 15] = 2
smith = smith_normal_form(B, domain=ZZ)
require([abs(int(smith[i, i])) for i in range(15)] == [1]*14+[2], 'primitive component index2')
require(B*sp.ones(16, 1) == sp.zeros(15, 1), 'literal all-one kernel vector')
require(B.rank() == 15, 'kernel has rank1')
section = sp.zeros(16, 15)
for i in range(14): section[i, i] = 1
for i in range(1, 16, 2): section[i, 14] = sp.Rational(1, 2)
require(B*section == sp.eye(15), 'exact rational section of primitive coordinates')
error = section*B-sp.eye(16)
require(all(error[i, j] == error[0, j] for i in range(16) for j in range(16)),
        'inverse transport modulo literal fibre relation')

vectors = [[(i, F(section[i, a])) for i in range(16) if section[i, a]] for a in range(15)]

def tensor(a, b, c):
    return sum((v*w*z*geometric(i, j, k)
                for i, v in vectors[a] for j, w in vectors[b] for k, z in vectors[c]), F(0))

primitive = {}
for a, b, c in product(range(15), repeat=3):
    value = tensor(a, b, c)
    require(value.denominator == 1, 'all3375 primitive entries integral')
    ys = sum(t == 14 for t in (a, b, c))
    if ys == 0:
        expected = geometric(a, b, c)
    elif ys >= 2:
        expected = 0
    else:
        j, k = [t for t in (a, b, c) if t != 14]
        r, s = vertices[j]; rr, ss = vertices[k]
        expected = (-1)**s * (int(ss == s and (rr-r) % 8 == 1)
                              + int(ss == s and (rr-r) % 8 == 7)
                              - 2*int((r, s) == (rr, ss)))
    require(value == expected, 'all primitive displayed formulas')
    if value: primitive[a, b, c] = int(value)

# Reconstruct all component entries from the primitive tensor and exact B.
columns = [[(a, int(B[a, i])) for a in range(15) if B[a, i]] for i in range(16)]
for i, j, k in product(range(16), repeat=3):
    value = sum(v*w*z*primitive.get((a, b, c), 0)
                for a, v in columns[i] for b, w in columns[j] for c, z in columns[k])
    require(value == geometric(i, j, k), 'all4096 recovered component entries')

L = sp.Matrix([[8, 24], [-6, -16]])
U = sp.Matrix([[1, 3], [-3, -8]])
require(U.det() == 1, 'marked period basis unimodular')
require(L*U.inv() == sp.diag(8, 2), 'literal period-lattice equality')
out = {
    'status': 'PASS', 'assertions': checks,
    'component_entries_compared': 16**3, 'primitive_entries_compared': 15**3,
    'component_entries_recovered': 16**3, 'triangular_cells': len(triangles),
    'component_index': 2, 'component_matrix': [list(map(int, B.row(i))) for i in range(15)],
    'period_unimodular_matrix': U.tolist(),
    'primitive_tensor_nonzero': [{'indices':list(k),'value':v} for k,v in sorted(primitive.items())],
    'component_tensor_nonzero': [{'indices':list(k),'value':v} for k,v in sorted(component.items())],
    'input_scope': 'Six toric boundary classes, actual16 periodic vertices and half-class restriction; no old code or output imported.',
    'uncomputed': 'The separate core/peripheral Smith matrices and framed odd torsion-cycle linking are not evaluated by this program.',
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
target = R/'code/outputs/III_OS45_primitive_cubic_independent.json'
target.write_text(json.dumps(out, indent=2, default=int)+'\n')
print(json.dumps({k:v for k,v in out.items() if not k.endswith('_nonzero') and k not in ['component_matrix','period_unimodular_matrix']}))
