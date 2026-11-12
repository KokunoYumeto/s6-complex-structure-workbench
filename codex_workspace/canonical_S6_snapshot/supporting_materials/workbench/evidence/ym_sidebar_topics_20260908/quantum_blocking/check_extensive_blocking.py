"""Exact finite diagnostics for the accompanying all-box analytic proofs.

No vacuum approximation, Monte Carlo sample or Lean invocation is used.
Only files in this script's directory are written.
"""
from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parent
assertions = 0


def check(condition, label):
    global assertions
    if not condition:
        raise AssertionError(label)
    assertions += 1


def mat_equal(a, b, label):
    for x in a - b:
        check(s.simplify(x) == 0, label)


def step(v, i, amount=1):
    w = list(v)
    w[i] += amount
    return tuple(w)


def graph(L):
    vertices = list(itertools.product(range(-L, L + 1), repeat=3))
    edges = {(v, i) for v in vertices for i in range(3) if v[i] < L}
    faces = {}
    for v in vertices:
        for i, j in itertools.combinations(range(3), 2):
            if v[i] < L and v[j] < L:
                faces[v, i, j] = [((v, i), 1), ((step(v, i), j), 1),
                                   ((step(v, j), i), -1), ((v, j), -1)]
    return edges, faces


def chains(L, m):
    grid = range(-L, L + 1, m)
    return {(v, i): [(step(v, i, k), i) for k in range(m)]
            for v in itertools.product(grid, repeat=3)
            for i in range(3) if v[i] < L}


box_receipts = []
for L in (2, 3, 4, 5, 6):
    edges, faces = graph(L)
    check(len(edges) == 3 * (2 * L) * (2 * L + 1) ** 2, 'full edge count')
    check(len(faces) == 3 * (2 * L) ** 2 * (2 * L + 1), 'full face count')
    stars = {e: 0 for e in edges}
    for word in faces.values():
        for e, _ in word:
            stars[e] += 1
    check(max(stars.values()) == 4, 'all incident face bound is attained')
    check(min(stars.values()) >= 2, 'boundary links retain incident faces')
    divisors = [m for m in range(1, 2 * L + 1) if (2 * L) % m == 0]
    levels = {}
    for m in divisors:
        q = (2 * L) // m
        paths = chains(L, m)
        flattened = [e for path in paths.values() for e in path]
        retained = set(flattened)
        check(len(flattened) == len(retained), 'coarse paths edge-disjoint')
        check(retained <= edges, 'every retained edge in original box')
        check(len(paths) == 3 * q * (q + 1) ** 2, 'coarse-edge count')
        check(len(retained) == 3 * (2 * L) * (q + 1) ** 2, 'skeleton count')
        check(len(edges - retained) == 3 * (2 * L) *
              ((2 * L + 1) ** 2 - (q + 1) ** 2), 'eliminated count')
        for e in edges:
            transverse_test = all((e[0][j] + L) % m == 0
                                  for j in range(3) if j != e[1])
            check((e in retained) == transverse_test, 'literal skeleton rule')
        coarse_face_count = 0
        for v in itertools.product(range(-L, L + 1, m), repeat=3):
            for i, j in itertools.combinations(range(3), 2):
                if v[i] == L or v[j] == L:
                    continue
                coarse_face_count += 1
                # Keep all four orientations and the order of inverse paths.
                cw = [((v, i), 1), ((step(v, i, m), j), 1),
                      ((step(v, j, m), i), -1), ((v, j), -1)]
                fine_word = []
                for ce, sign in cw:
                    fine_word.extend((e, sign) for e in
                                     (paths[ce] if sign == 1 else paths[ce][::-1]))
                check(len(fine_word) == 4 * m, 'actual fine perimeter')
                check(len({e for e, _ in fine_word}) == 4 * m, 'simple fine loop')
                current = v
                for (n, axis), sign in fine_word:
                    initial = n if sign == 1 else step(n, axis)
                    terminal = step(n, axis) if sign == 1 else n
                    check(current == initial, 'oriented path continuity')
                    current = terminal
                check(current == v, 'oriented coarse loop closes')
        check(coarse_face_count == 3 * q ** 2 * (q + 1), 'coarse face count')
        levels[m] = (paths, retained)
        box_receipts.append({'L': L, 'm': m, 'fine_edges': len(edges),
                             'retained_fine_edges': len(retained),
                             'eliminated_fine_edges': len(edges-retained),
                             'coarse_edges': len(paths),
                             'coarse_faces': coarse_face_count})
    for m in divisors:
        for n in divisors:
            if n % m:
                continue
            check(levels[n][1] <= levels[m][1], 'nested skeleton')
            for (v, i), path in levels[n][0].items():
                composed = [e for k in range(n // m)
                            for e in levels[m][0][step(v, i, k * m), i]]
                check(composed == path, 'ordered product tower')

# Exact Pauli and noncommuting path-product differential tensor.
I2 = s.eye(2)
pauli = [s.Matrix([[0, 1], [1, 0]]),
         s.Matrix([[0, -s.I], [s.I, 0]]),
         s.Matrix([[1, 0], [0, -1]])]
T = [-s.I * p / 2 for p in pauli]
mat_equal(-sum((t*t for t in T), s.zeros(2)), 3*I2/4, 'fundamental Casimir')
for a in range(3):
    for b in range(3):
        check(-2*s.trace(T[a]*T[b]) == (1 if a == b else 0), 'original metric')

sample = [s.Rational(3, 5)*I2+s.I*s.Rational(4, 5)*pauli[0],
          s.Rational(5, 13)*I2+s.I*s.Rational(12, 13)*pauli[1],
          s.Rational(7, 25)*I2+s.I*s.Rational(24, 25)*pauli[2]]
for u in sample:
    mat_equal(u*u.conjugate().T, I2, 'SU2 exact sample')
    check(s.det(u) == 1, 'sample determinant')
check(sample[0]*sample[1] != sample[1]*sample[0], 'noncommuting sample')
z = sample[0]*sample[1]*sample[2]
prefix = I2
rotations = []
for k, u in enumerate(sample):
    O = s.Matrix(3, 3, lambda b, a: -2*s.trace(T[b]*prefix*T[a]*prefix.inv()))
    rotations.append(O)
    mat_equal(O*O.T, s.eye(3), 'adjoint color rotation')
    check(s.det(O) == 1, 'proper color rotation')
    suffix = I2
    for after in sample[k+1:]:
        suffix = suffix*after
    for a in range(3):
        tangent = prefix*T[a]*u*suffix
        predicted = sum((O[b, a]*T[b]*z for b in range(3)), s.zeros(2))
        mat_equal(tangent, predicted, 'fine-to-coarse tangent')
    prefix = prefix*u
M = s.zeros(9)
M[:3, :3] = s.eye(3)
M[3:6, 3:6] = s.eye(3)
for k, O in enumerate(rotations):
    M[6:9, 3*k:3*k+3] = O
tensor = M*M.T
expected = s.diag(s.eye(3), s.eye(3), 3*s.eye(3))
expected[:3, 6:9] = rotations[0].T
expected[6:9, :3] = rotations[0]
expected[3:6, 6:9] = rotations[1].T
expected[6:9, 3:6] = rotations[1]
mat_equal(tensor, expected, 'complete mixed kinetic tensor')
check(s.det(tensor) == 1, 'kinetic coordinate map nondegenerate')
Y = s.zeros(3, 9)
for k, O in enumerate(rotations):
    Y[:, 3*k:3*k+3] = O/3
mat_equal(Y*Y.T, s.eye(3)/3, 'horizontal derivative coefficient 1/m')

# Exact rational Schur recursion with a nonzero intermediate memory block.
zeta = s.symbols('zeta', positive=True)
base = s.Matrix([[5, 1, 2, 0], [1, 6, 1, 1],
                 [2, 1, 7, 2], [0, 1, 2, 8]])
for k in range(1, 5):
    check(base[:k, :k].det() > 0, 'positive exact block matrix')
full = base+zeta*s.eye(4)
stage1 = full[:2, :2]-full[:2, 2:]*full[2:, 2:].inv()*full[2:, :2]
stage2 = stage1[0, 0]-stage1[0, 1]*stage1[1, 0]/stage1[1, 1]
direct = full[0, 0]-(full[:1, 1:]*full[1:, 1:].inv()*full[1:, :1])[0]
check(s.factor(stage2-direct) == 0, 'Schur associativity as rational function')
check(s.factor(full.inv()[0, 0]-1/direct) == 0, 'compressed inverse')
B = base[1:, :1]
C = base[1:, 1:]
w = (C+zeta*s.eye(3)).inv()*B
norm = 1+(w.T*w)[0]
check(s.factor(s.diff(direct, zeta)-norm) == 0, 'Schur derivative is dressed norm')
v = s.Matrix([1, -w[0], -w[1], -w[2]])
energy = (v.T*base*v)[0]
check(s.factor(energy-(direct-zeta*s.diff(direct, zeta))) == 0,
      'energy includes all eliminated terms')

alpha, Cstar, kappa, ell, G = s.symbols('alpha Cstar kappa ell G', positive=True)
A = 3*alpha/16
cH = 9*alpha**3/(1024*Cstar**2)
check(s.factor(A**2*alpha/(4*Cstar**2)-cH) == 0,
      'exact unnormalized retained high-energy weight constant')
dC = s.symbols('dC', positive=True)
raw_second_upper = Cstar**2*kappa**2*ell**2
raw_tail_bound = (A*kappa*ell*dC/2)**2/raw_second_upper
check(s.factor(raw_tail_bound-A**2*dC**2/(4*Cstar**2)) == 0,
      'unnormalized spectral tail bound retains state mass squared')
check(s.factor(raw_tail_bound-cH*dC
               -9*alpha**2*dC*(dC-alpha)/(1024*Cstar**2)) == 0,
      'raw tail dominates cH times original mass when dC>=alpha')
tau = 8*G/s.sqrt(alpha*cH)
check(s.simplify(4*G/tau-s.sqrt(alpha*cH)/2) == 0, 'dressing norm constant')
check(s.simplify((cH/4)/(1+cH/4)-cH/(4+cH)) == 0, 'dressed weight fraction')
g, spacing, m = s.symbols('g spacing m', positive=True)
check(s.simplify((3*alpha/32)*(2*g**2/spacing)*(4*m)
                 -3*alpha*g**2*m/(4*spacing)) == 0, 'physical threshold')
check(s.simplify((3*alpha/16)*(2*g**2/spacing)*(4*m)
                 -3*alpha*g**2*m/(2*spacing)) == 0, 'physical quotient lower bound')

sources = {}
for name in ['extensive_quantum_blocking.tex', 'check_extensive_blocking.py']:
    sources[name] = hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
receipt = {'status': 'passed', 'exact_assertions': assertions,
           'boxes_and_blocks': box_receipts, 'source_sha256': sources,
           'scope': 'Exact finite incidence, noncommuting SU2 tangent/tensor, '
                    'rational Schur recursion and spectral coefficient diagnostics; '
                    'the analytic all-volume proofs are in the manuscript. '
                    'No interacting vacuum is numerically replaced.'}
(ROOT/'EXACT_CHECKS.json').write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'status': 'passed', 'exact_assertions': assertions,
                  'box_block_cases': len(box_receipts)}, indent=2))
