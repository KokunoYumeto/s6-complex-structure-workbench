#!/usr/bin/env python3
"""Fresh exact restriction-map checks, written before opening WJ/WL proofs.

No inherited proof-checking program or symbolic algebra package is imported.
The arbitrary convergent-series arguments are in the prereading derivations.
"""
from fractions import Fraction as Q
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json

def rref(matrix, ncols):
    a = [[Q(x) for x in row] for row in matrix]
    pivots = []
    row = 0
    for col in range(ncols):
        chosen = next((i for i in range(row, len(a)) if a[i][col]), None)
        if chosen is None:
            continue
        a[row], a[chosen] = a[chosen], a[row]
        scalar = a[row][col]
        a[row] = [x / scalar for x in a[row]]
        for i in range(len(a)):
            if i != row and a[i][col]:
                scalar = a[i][col]
                a[i] = [x - scalar*y for x, y in zip(a[i], a[row])]
        pivots.append(col)
        row += 1
        if row == len(a):
            break
    return a[:row], pivots

def kernel(matrix, ncols):
    reduced, pivots = rref(matrix, ncols)
    out = []
    for free in set(range(ncols)) - set(pivots):
        v = [Q(0)] * ncols
        v[free] = Q(1)
        for row, pivot in zip(reduced, pivots):
            v[pivot] = -row[free]
        out.append(v)
    return out

def images(kind, n):
    branches = 3 if kind == 'triple' else 2
    out = []
    for a in range(n):
        for b in range(n):
            v = [Q(0)] * (branches*n)
            if kind == 'tangent':
                if b == 0:
                    v[a] = 1
                if a+2*b < n:
                    v[n+a+2*b] = 1
            elif kind == 'triple':
                if a == 0:
                    v[b] = 1
                if b == 0:
                    v[n+a] = 1
                if a+b < n:
                    v[2*n+a+b] = 1
            elif kind == 'node':
                if b == 0:
                    v[a] = 1
                if a == 0:
                    v[n+b] = 1
            else:
                raise ValueError(kind)
            if any(v):
                out.append(v)
    return out, branches

def jet_check(kind, n):
    vectors, branches = images(kind, n)
    size = branches*n
    _, image_pivots = rref(vectors, size)
    annihilators = kernel(vectors, size)
    constraints = []
    for branch in range(branches):
        for power in range(n):
            for h in annihilators:
                row = [Q(0)] * size
                for degree in range(n-power):
                    row[branch*n+degree] = h[branch*n+degree+power]
                constraints.append(row)
    reduced, conductor_pivots = rref(constraints, size)
    order = 1 if kind == 'node' else 2
    required = [branch*n+degree for branch in range(branches) for degree in range(order)]
    assert conductor_pivots == required
    for row, col in zip(reduced, conductor_pivots):
        assert row[col] == 1
        assert sum(bool(x) for x in row) == 1
    delta = size-len(image_pivots)
    assert delta == {'node': 1, 'tangent': 2, 'triple': 3}[kind]
    return {'kind': kind, 'jet_order': n, 'normalization_dimension': size,
            'image_dimension': len(image_pivots), 'delta': delta,
            'conductor_dimension': size-len(conductor_pivots),
            'conductor_branch_orders': [order]*branches,
            'all_coordinate_idempotent_and_monomial_multiplier_conditions_checked': True}

def weighted_matrix_identity(n):
    lhs, rhs = defaultdict(int), defaultdict(int)
    def term(poly, coefficient, symbols):
        poly[tuple(sorted(symbols))] += coefficient
    for i in range(n):
        for j in range(n):
            mij = f'M{min(i,j)}_{max(i,j)}'
            term(lhs, 1, [mij, f'n{i}', f'n{j}', f'x{i}', f'x{j}'])
            term(rhs, 1, [mij, f'n{i}', f'n{j}', f'x{i}', f'x{i}'])
    for i in range(n):
        for j in range(i+1, n):
            base = [f'M{i}_{j}', f'n{i}', f'n{j}']
            term(rhs, -1, base+[f'x{i}', f'x{i}'])
            term(rhs, 2, base+[f'x{i}', f'x{j}'])
            term(rhs, -1, base+[f'x{j}', f'x{j}'])
    lhs = {k:v for k,v in lhs.items() if v}
    rhs = {k:v for k,v in rhs.items() if v}
    assert lhs == rhs
    return {'size': n, 'polynomial_identity_exact': True, 'monomial_count': len(lhs)}

path = Path(__file__).resolve()
out = {
    'created_utc': datetime.now(timezone.utc).isoformat(),
    'code_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
    'fresh_before_target_release': True,
    'old_checking_programs_imported_or_opened': False,
    'arithmetic': 'Python standard-library Fraction and formal monomial dictionaries',
    'jet_checks': [jet_check(kind, n) for kind in ['tangent', 'triple', 'node'] for n in range(2, 9)],
    'plane_cubic_chi': Q((0+1)*(0+2),2)-Q((-3+1)*(-3+2),2),
    'normalization_chi': {'tangent': 2-2, 'triple': 3-3},
    'weighted_intersection_matrix_identity': [weighted_matrix_identity(n) for n in range(1, 7)],
    'discrepancy_cycle_rr_identity': '-(D^2+K.D)/2=0 when K=L-D and L.D=0',
    'scope': 'Finite jet matrices and formal polynomial identities check the explicit formulas. The complete arbitrary-series and surface arguments are separately written in the prereading derivations.',
    'events_added': 0,
}
output = path.with_name('S6_SERIES_PUBLISH_II_WJ_WL_fresh_exact_output.json')
with output.open('x') as stream:
    json.dump(out, stream, indent=2, default=lambda x: str(x))
    stream.write('\n')
print(json.dumps({'output': str(output), 'sha256': hashlib.sha256(output.read_bytes()).hexdigest(),
                  'code_sha256': out['code_sha256'], 'checks': len(out['jet_checks'])}, indent=2))
