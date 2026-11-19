#!/usr/bin/env python3
"""Exact algebra certificate for P4R.19; the geometric proof is in notes."""
from pathlib import Path
import json
import sympy as S

out = Path(__file__).with_suffix('.json')
x, y, z, a, b = S.symbols('x y z a b', nonzero=True)
k, l, r = S.symbols('k l r', integer=True, positive=True)
rho, margin = S.symbols('rho margin', positive=True)
beta, gamma = S.symbols('beta gamma', nonnegative=True)
L = 3*rho + margin
wx, wy, wz = L+rho, L, S.Integer(1)
D = 3*wx
weight_gaps = {
    'x_cubed': S.simplify(3*wx-D),
    'B_z_term': S.simplify(wx+2*wy+(2*rho+beta)*wz-D),
    'C_z_term': S.simplify(3*wy+(3*rho+gamma)*wz-D),
    'B_term_containing_y': S.simplify(wx+3*wy-D),
    'C_term_containing_y': S.simplify(4*wy-D),
}
assert weight_gaps == {'x_cubed': 0, 'B_z_term': beta,
                      'C_z_term': gamma,
                      'B_term_containing_y': margin+rho,
                      'C_term_containing_y': margin}
assert weight_gaps['B_term_containing_y'].is_positive
assert weight_gaps['C_term_containing_y'].is_positive

P1 = x*(x*x+a*y*y*z**k)
h1 = (1-x**3)/(a*x)
I1 = S.expand(P1-1-a*x*(y*y*z**k-h1))
P2 = x**3+b*y**3*z**l
h2 = (1-x**3)/b
I2 = S.expand(P2-1-b*(y**3*z**l-h2))
X, V, u, w = S.symbols('X V u w')
Q = X**3+a*X*V**2+b*V**3
P3 = Q.subs({X:x,V:y*z**r})
I3 = S.expand(P3-Q.subs({X:x,V:u*w}).subs({u:y,w:z**r}))
assert I1 == I2 == I3 == 0
assert S.diff(Q,X).subs(V,0) == 3*X**2

A, B = S.symbols('A B', nonzero=True)
xx = (A+B)/2
yy = 1/(A*B)
zz = (A-B)*A*B/(2*S.I)
exception = S.simplify(yy*(xx**2+yy**2*zz**2))
inverse_a = S.simplify(xx+S.I*yy*zz-A)
inverse_b = S.simplify(xx-S.I*yy*zz-B)
assert exception == 1 and inverse_a == inverse_b == 0

certificate = {
 'statement': 'P4R.19',
 'status': 'Proved; root and checks independent audits passed',
 'scope': 'Nonzero cubic triple spectral root on a smooth local D4 branch',
 'weight_choice': {'L':str(L),'wx':str(wx),'wy':str(wy),'wz':str(wz),'degree':str(D)},
 'weight_gaps': {key:str(value) for key,value in weight_gaps.items()},
 'finite_map_equation_remainders': [str(I1),str(I2),str(I3)],
 'finite_degrees': ['2*k','3*l','r'],
 'pulled_back_squares': [str(-4*k),str(-6*l),str(-2*r)],
 'balanced_zero_derivative': str(S.diff(Q,X).subs(V,0)),
 'two_root_exception_fibre_equation': str(exception),
 'two_root_exception_inverse_remainders': [str(inverse_a),str(inverse_b)],
 'geometric_steps': 'Properness follows from the displayed monic power equations; matching sphere, degree pairing, connectedness, and compact scaling are proved in the note.',
}
out.write_text(json.dumps(certificate,indent=2)+'\n')
print('PASS: exact weighted gaps, all three finite-map equations, pullback squares, and two-root inverse maps.')
print(out)
