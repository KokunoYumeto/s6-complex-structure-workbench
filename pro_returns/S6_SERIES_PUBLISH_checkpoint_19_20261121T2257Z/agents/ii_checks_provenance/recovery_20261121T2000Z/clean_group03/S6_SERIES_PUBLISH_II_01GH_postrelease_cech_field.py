"""E10: a second method after proof release and reading the two prior slices.

Q(omega) field norms replace polynomial gcds.  Laurent Cech boundary
matrices on P1, followed by the actual double-cover algebra O + O(-3),
replace insertion of the Riemann--Roch formula.  No independent event is
claimed for this postrelease supplement.
"""
from fractions import Fraction as Q
from itertools import product
import json


def qadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def qmul(a, b):
    # omega^2 = -1-omega
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]-a[1]*b[1])


def qsub(a, b):
    return (a[0]-b[0], a[1]-b[1])


def qnorm(a):
    return a[0]**2-a[0]*a[1]+a[1]**2


one, omega, omega2 = (1, 0), (0, 1), (-1, -1)
assert qmul(omega, omega) == omega2
assert qmul(omega, omega2) == one
critical1 = [one, omega, omega2]  # infinity is the fourth critical value
critical2 = [(4, 0)] + [qadd((4, 0), qmul(v, v)) for v in critical1]
assert set(critical2) == {(4, 0), (5, 0), (4, 1), (3, -1)}
cross_norms = [[qnorm(qsub(a, b)) for b in critical2] for a in critical1]
assert all(n > 0 for row in cross_norms for n in row)
# The second list has no infinity, by the exact inverse Mobius map 4+1/u.
branch_norms = {str(t): [qnorm(qsub((t, 0), a))
                       for a in critical1 + critical2] for t in range(10, 16)}
assert all(n > 0 for row in branch_norms.values() for n in row)


def rank(matrix):
    if not matrix:
        return 0
    a = [[Q(x) for x in row] for row in matrix]
    i = 0
    for j in range(len(a[0])):
        p = next((p for p in range(i, len(a)) if a[p][j]), None)
        if p is None:
            continue
        a[i], a[p] = a[p], a[i]
        q = a[i][j]
        a[i] = [x/q for x in a[i]]
        for k in range(len(a)):
            if k != i and a[k][j]:
                q = a[k][j]
                a[k] = [x-q*y for x, y in zip(a[k], a[i])]
        i += 1
        if i == len(a):
            break
    return i


def p1_cech(d):
    """O(d), e_infinity=t^d e_zero. Cech sends (f,g) to f-t^d g.

    The chart monomial exponents are n>=0 and n<=d.  Outside the
    finite interval below, each monomial has exactly one chart preimage,
    giving an explicit contracting pair.  Hence the finite matrix has
    the same kernel and cokernel as the full Laurent Cech complex.
    """
    lo, hi = min(d, 0)-2, max(d, 0)+2
    rows = list(range(lo, hi+1))
    columns = [('zero', n) for n in rows if n >= 0]
    columns += [('infinity', n) for n in rows if n <= d]
    a = [[(1 if chart == 'zero' else -1) if n == r else 0
          for chart, n in columns] for r in rows]
    r = rank(a)
    h0, h1 = len(columns)-r, len(rows)-r
    kernel_exponents = list(range(0, d+1)) if d >= 0 else []
    cokernel_exponents = list(range(d+1, 0)) if d < -1 else []
    assert (h0, h1) == (len(kernel_exponents), len(cokernel_exponents))
    return {'degree': d, 'rows': rows, 'columns': columns,
            'matrix': a, 'rank': r, 'h': [h0, h1],
            'kernel_exponents': kernel_exponents,
            'cokernel_exponents': cokernel_exponents}


cech = {d: p1_cech(d) for d in range(-7, 3)}


def curve_line(a):
    # pi_* L^{-a}=O(-a)+O(-a-3), by the two basis elements 1 and y.
    return [cech[-a]['h'][i] + cech[-a-3]['h'][i] for i in range(2)]


curve_values = {a: curve_line(a) for a in range(4)}
assert curve_values == {0: [1, 2], 1: [0, 3], 2: [0, 5], 3: [0, 7]}


def leray(a, copies=1):
    # R^q g_* O = L^{-q} with multiplicities 1,2,1; base dimension 1
    # makes all higher Leray differentials zero.
    h = [0]*4
    pieces = []
    for q, multiplicity in enumerate((1, 2, 1)):
        for p, dimension in enumerate(curve_line(a+q)):
            h[p+q] += copies*multiplicity*dimension
            pieces.append({'p': p, 'q': q, 'multiplicity': copies*multiplicity,
                           'curve_line_exponent': -(a+q), 'dimension': dimension})
    return {'h': h, 'pieces': pieces}


tables = {'O_Y': leray(0), 'g_star_T_C': leray(1), 'T_Y_over_C': leray(1, 2)}
assert tables['O_Y']['h'] == [1, 2, 6, 5]
assert tables['g_star_T_C']['h'] == [0, 3, 10, 7]
assert tables['T_Y_over_C']['h'] == [0, 6, 20, 14]

print(json.dumps({
    'timing': 'postrelease; after both E10 prior target-only slices were read',
    'new_independent_events': 0,
    'hesse': {'field': 'Q[omega]/(omega^2+omega+1)',
              'first_finite_critical_values': critical1,
              'first_infinite_critical_value': True,
              'second_critical_values': critical2,
              'second_infinite_critical_value': False,
              'cross_difference_norms': cross_norms,
              'branch_difference_norms': branch_norms},
    'cech_matrices': list(cech.values()),
    'double_cover_pushforward': 'O plus O(-3), basis (1,y), y_infinity=t^-3 y',
    'curve_cohomology': curve_values,
    'threefold_tables': tables,
    'scope': 'Exact geometric identifications and the all-exponent tail contraction are proved in the accompanying comparison, not inferred from a finite sample.'
}, indent=2))
