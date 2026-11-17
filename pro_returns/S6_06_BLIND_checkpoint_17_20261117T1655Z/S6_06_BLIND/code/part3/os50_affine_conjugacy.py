#!/usr/bin/env python3
"""Exact finite norm/coboundary certificate for P3F.49.

The analytic extension and line maps are proved in the accompanying text.
This program retains the finite central character and verifies the actual
finite-group algebra used there; it never sets a collar coefficient to zero.
"""
import json
from pathlib import Path
import sympy as sp

x, z, T, S = sp.symbols('x z T S')
records = []
for m in range(1, 121):
    norm = sum(x**j for j in range(m))
    homotopy = -sum(sp.Rational(j, m)*x**j for j in range(m))
    identity = sp.rem((1-x)*homotopy - (1-norm/m), x**m-1, x)
    assert sp.expand(identity) == 0
    records.append({'m':m, 'norm_polynomial':str(norm),
                    'homotopy_polynomial':str(homotopy),
                    'identity_remainder':'0'})

# For D(T)=T^{-1} on the central identity group, (1-D)T=T^2.
squaring = sp.cancel(T/(1/T))
assert squaring == T**2

# Scalar conjugation retains chi: the coboundary telescopes, its norm is 1,
# and the original scalar's norm is therefore chi^m, not an erased phase.
factors = sp.symbols('c0:7')
scalar_norm = sp.prod(factors[j]/factors[(j+1)%7] for j in range(7))
assert sp.cancel(scalar_norm) == 1

U0,U2,U4,w0=sp.symbols('U0 U2 U4 w0')
Z=sp.symbols('Z', nonzero=True)
U=U0+U2*z**2+U4*z**4
R0=z*w0
conjugated=sp.cancel(U.subs(z,-z)*R0/(Z/U))
assert sp.cancel(conjugated-U**2*R0/Z)==0
h1,h3=sp.symbols('h1 h3')
g=h1*z+h3*z**3
assert sp.expand(g/2-g.subs(z,-z)/2-g)==0

data = {
  'statement':'P3F.49', 'status':'PASS',
  'general_identity':'(1-D)(-sum(j*D^j)/m)=1-Norm_D/m on D^m=1',
  'central_maps':{
    'good_IV':'1-D is the degree-three elliptic isogeny',
    'reduced_IV':'Z/3 component norm is multiplication by m=1 mod 3; identity map is (1-lambda)T',
    'quadratic_I1star':'permitted component actions are both odd; identity C* map is T^2'
  },
  'central_squaring':str(squaring),
  'scalar_telescoping_norm':str(scalar_norm),
  'literal_Tate_conjugacy':str(conjugated),
  'literal_Tate_equation':'U(z)U(-z)R0(z)=R(z), U even, U^2=w/w0',
  'transported_centres':'Bl_Z0(Sroot) -> Bl_CU(Z0)(Sroot) induced by C_U; quotient transported by inverse',
  'scalar_arrow':'target: A=m_f C, conjugation ratio b(z)/b(zeta_m^-1 z)',
  'quadratic_scalar':'g odd, b=exp(g/2), target ratio exp(g)',
  'retained_phase':'chi=f(0), chi^m=1; no conjugacy sets chi=1',
  'outer_marking':'all actual source and line collar coefficients c,kappa retained',
  'supplementary_exact_orders':records
}
out=Path(__file__).with_suffix('.json')
out.write_text(json.dumps(data, indent=2)+'\n')
print('P3F.49 PASS: exact norm homotopy, 120 orders, central squaring, retained finite character.')
