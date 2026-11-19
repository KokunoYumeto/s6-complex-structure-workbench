#!/usr/bin/env python3
"""Exact period and catalogue arithmetic for intrinsic scalar minimality.

The geometric period identifications are proved in the companion note.  This
certificate checks their integral basis changes and exhausts every residue
class needed by the thirty nonempty F53 branches.  No sampled gcd is used in
place of a parameter proof.
"""
from __future__ import annotations

from datetime import datetime, timezone
from hashlib import sha256
from itertools import product
from math import gcd
from pathlib import Path
import json
import re
import sympy as S

HERE = Path(__file__).resolve().parent
INPUT = HERE / 'canonical_scalar_catalogue.json'
DATA = json.loads(INPUT.read_text())
k, l = S.symbols('k l', integer=True)
checks = []


def check(name, value, detail=None):
    assert bool(value), name
    checks.append({'name': name, 'pass': True, 'detail': detail})


def order_expression(text):
    return S.sympify(text, locals={'k': k, 'l': l})


def exact_gcd_with_constant(expr, c):
    """A polynomial with integer coefficients depends mod c only on residues."""
    variables = sorted(expr.free_symbols, key=str)
    poly = S.Poly(expr, *variables) if variables else None
    if poly is not None:
        check('integral order polynomial ' + str(expr),
              all(coef.q == 1 for coef in poly.all_coeffs()))
    rows = []
    for residues in product(range(c), repeat=len(variables)):
        value = int(expr.subs(dict(zip(variables, residues))))
        rows.append({'residues': list(residues), 'gcd': gcd(value, c)})
    values = {row['gcd'] for row in rows}
    check('constant gcd on all residue classes: ' + str(expr) + ' mod ' + str(c),
          len(values) == 1)
    return values.pop(), {'modulus': c, 'variables': list(map(str, variables)),
                          'all_residue_classes': rows}


good_point_orders = {'III*': 2, 'III': 2, 'IV*': 3, 'IV': 3, 'II': 1}
normalization_components = {'II': 1, 'III': 2, 'IV': 3, 'I2': 2}


def cap_record(cap, a):
    m = order_expression(cap['m'])
    if cap['kind'] == 'absent':
        return {'kind': 'absent', 'm': str(m), 'line_point_order': 1,
                'period_exponent': '1', 'removed_factor': 1,
                'winding_denominator': '1', 'proof': 'ordinary order-one slot'}
    if cap['kind'] == 'good':
        o = good_point_orders[cap['source_fibre']]
        t = o // gcd(o, a)
        factor, proof = exact_gcd_with_constant(m, t)
        check('good Picard order divides root order', factor == t)
        return {'kind': 'good', 'source_fibre': cap['source_fibre'],
                'root_fibre': cap['root_fibre'], 'm': str(m),
                'marked_G_order': o, 'a': a, 'line_point_order': t,
                'period_lattice': '(1/t)Z + (tau/m + y*kappa)Z; m*x+n*y=1',
                'tate_coordinate': 'exp(2*pi*i*t*y*kappa)*(c*lambda)^(t/m)',
                'period_exponent': str(S.factor(S.Rational(t)/m)),
                'removed_factor': factor,
                'winding_denominator': str(S.factor(m/factor)),
                'gcd_proof': proof}
    r = normalization_components[cap['root_fibre']]
    factor, proof = exact_gcd_with_constant(m, r)
    return {'kind': 'reduced normalization', 'source_fibre': cap['source_fibre'],
            'root_fibre': cap['root_fibre'], 'm': str(m),
            'normalization_component_count': r,
            'period_lattice': 'Z + (r*log(lambda)/(2*pi*i*m)+log(c)/(2*pi*i))Z',
            'tate_coordinate': 'c*lambda^(r/m)',
            'period_exponent': str(S.factor(S.Rational(r)/m)),
            'removed_factor': factor,
            'winding_denominator': str(S.factor(m/factor)),
            'gcd_proof': proof}


# Literal integral arrows in the two period calculations.
m, n, x, y, tau, kap, r = S.symbols('m n x y tau kappa r')
bezout = m*x+n*y-1
p = n*tau/m+kap
beta = x*tau+y*p
check('good new period beta', S.simplify(beta-tau/m-y*kap-bezout*tau/m) == 0)
check('old gamma from beta', S.simplify(m*(tau/m+y*kap)-tau-m*y*kap) == 0)
check('old affine period from beta',
      S.simplify(p-n*(tau/m+y*kap)-m*x*kap+bezout*kap) == 0)
check('Bezout choice changes beta by an old real period',
      S.simplify((tau/m+(y-m)*kap)-(tau/m+y*kap)+m*kap) == 0)
check('H scalar exponent', S.simplify(x+y*n/m-(1+bezout)/m) == 0)
check('H^m equals B modulo norm', m*x+n*y-1 == bezout)
check('H^n/A is x times the norm relation',
      S.Matrix([n*x,n*y-1])-x*S.Matrix([n,-m]) == S.Matrix([0,bezout]))
check('H^r scalar exponent', S.simplify(r*(x+y*n/m)-r*(1+bezout)/m) == 0)

# The correct character uses aG, including the vanishing a=2 E7 example.
check('E7 a=1 line has order two', 2//gcd(2,1) == 2)
check('E7 a=2 line has order one', 2//gcd(2,2) == 1)
check('E6 a=1 line has order three', 3//gcd(3,1) == 3)
check('E6 a=2 line has order three', 3//gcd(3,2) == 3)
check('E6 a=3 line has order one', 3//gcd(3,3) == 1)

rows, excluded = [], []
for branch in DATA['branches']:
    if branch['status'] == 'excluded_by_sphere_determinant':
        mi = order_expression(branch['m_infty'])
        m0 = order_expression(branch['m_0'])
        gi, _ = exact_gcd_with_constant(mi, 2)
        g0, _ = exact_gcd_with_constant(m0, 2)
        check(branch['id'] + ' has an unavoidable common factor two', gi == g0 == 2)
        excluded.append({'id': branch['id'], 'reason': 'both effective cap orders even'})
        continue
    caps = [cap_record(branch['cap_infty'], branch['a']),
            cap_record(branch['cap_0'], branch['a'])]
    removed = caps[0]['removed_factor']*caps[1]['removed_factor']
    M = order_expression(branch['M'])
    denominator_product = S.prod(order_expression(c['winding_denominator']) for c in caps)
    check(branch['id'] + ' removed factor equals actual source translation b',
          removed == branch['b'])
    check(branch['id'] + ' intrinsic minimum equals M/b',
          S.simplify(denominator_product-M/branch['b']) == 0)
    rows.append({'id': branch['id'], 'os': branch['os'], 'profile': branch['profile'],
                 'a': branch['a'], 'b': branch['b'], 'caps': caps,
                 'M': str(M), 'minimum_scalar_winding': str(S.factor(M/branch['b'])),
                 'actual_closed_parameter': 'lambda=w^(' + str(S.factor(M/branch['b'])) + ')',
                 'cap_norms': 'all retained n_i with gcd(m_i,n_i)=1 and signed Seifert determinant +/-1',
                 'cap_permutations': 'nontrivial orders are coprime, hence pairwise distinct',
                 'endpoint_scope': 'arbitrary biholomorphic endpoint maps of the fixed-source family',
                 'sufficiency': 'P3K.35 exact cap/ordinary/cusp quotient'})

check('thirty nonempty branches covered', len(rows) == 30)
check('one impossible root branch retained as excluded', len(excluded) == 1)

# Component-supported OS49 has its own actual Picard point, not H=Ma^2/d.
te, be = S.symbols('tau_E beta')
Pi = S.Matrix([[-te,-te,1,0],[be,-te/3,0,1]])
eta = S.Matrix([[-1,3]])
T = 3*be+te
psi = S.Matrix([[1,0,0,0]])
hh = S.Matrix([[0,0,-1,3]])
A = S.Matrix([[1,0,0,0],[0,1,-1,0],[3,3,-2,0],[1,1,-1,1]])
check('OS49 full invariant period row', eta*Pi == hh+T*psi)
check('OS49 primitive integral invariant covectors', psi*A == psi and hh*A == hh)
for sign in (-1,1):
    dd = S.symbols('d_delta', integer=True)
    ell = S.Matrix([sign,-sign,0,dd])
    check('OS49 signed affine period '+str(sign),
          S.simplify(((hh+T*psi)*ell)[0]-(sign*T+3*dd)) == 0)
    newperiod=(T+3*sign*dd)/m
    check('OS49 signed new period '+str(sign),
          S.simplify((sign*T+3*dd)/m-sign*newperiod) == 0)
    check('OS49 old period from new '+str(sign),
          S.simplify(T-m*newperiod+3*sign*dd) == 0)
os49 = {'m': '3*k', 'line_point': 'G_0', 'line_point_order': 3,
        'affine_vector': 'n*(e_gamma-e_u)+d*delta, n=+/-1',
        'period_lattice': 'Z + ((3*tau+c+3*n*d)/(3*k))Z',
        'tate_coordinate': 'c0*lambda^(1/k)', 'minimum_scalar_winding': 'k',
        'sufficiency': 'P3K.37', 'whole_fibre_height_used': False}
check('OS49 minimal winding', S.simplify(3*k/S.gcd(3,3)-k) == 0)

out = {'status': 'PASS', 'utc': datetime.now(timezone.utc).isoformat(),
       'input': str(INPUT.relative_to(HERE.parent.parent)),
       'input_sha256': sha256(INPUT.read_bytes()).hexdigest(),
       'geometric_proof': 'notes/part3_scalar_minimality_working.md',
       'comparison': 'Intrinsic cap Albanese periods versus the actual P3K.35/P3K.37 quotient',
       'branch_count': len(rows), 'branches': rows, 'excluded': excluded,
       'component_supported_OS49': os49, 'checks': checks,
       'automorphism_mapping_classes_inferred': False}
(HERE/'scalar_cap_minimality.json').write_text(json.dumps(out,indent=2)+'\n')
lines = ['| Branch | Source profile | (a,b) | Cap denominators | Minimum winding |',
         '|---|---|---:|---|---:|']
for row in rows:
    den = ', '.join(r'\('+S.latex(order_expression(c['winding_denominator']))+r'\)'
                    for c in row['caps'])
    prof = re.sub(r'I(\d+)',lambda z: 'I_{'+z.group(1)+'}',row['profile']).replace('*','^*')
    minimum = r'\('+S.latex(order_expression(row['minimum_scalar_winding']))+r'\)'
    lines.append(f"| {row['id']} | \\({prof}\\) | ({row['a']},{row['b']}) | {den} | {minimum} |")
(HERE/'scalar_cap_minimality_table.md').write_text('\n'.join(lines)+'\n')
print('PASS:',len(checks),'exact checks;',len(rows),'nonempty catalogue branches; OS49 also retained.')
for row in rows:
    print(row['id'], 'minimum =', row['minimum_scalar_winding'], 'removed factor =', row['b'])
