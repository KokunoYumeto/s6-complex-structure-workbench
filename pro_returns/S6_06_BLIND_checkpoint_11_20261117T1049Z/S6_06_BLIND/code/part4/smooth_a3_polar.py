"""Exact polar identities and six-point test for P4R.14.

All calculations use rational arithmetic. The local-degree and boundary
transport proofs are in notes/part4_smooth_a3_working.md.
"""
from pathlib import Path
import json
import sympy as sp

x, y, z, eta, epsilon = sp.symbols('x y z eta epsilon')
H = sp.Function('H')(x, z)
hx = sp.diff(H, x)
hz = sp.diff(H, z)
G = 2*H + x*hx
f = x*(y*y+x*(H-eta*z-epsilon))
h0,hx0,hz0,hxx0,hxz0,hzz0 = sp.symbols('H H_x H_z H_xx H_xz H_zz')
jets = {H:h0,hx:hx0,hz:hz0,sp.diff(H,x,2):hxx0,
        sp.diff(H,x,z):hxz0,sp.diff(H,z,2):hzz0}
def critical_jet(expr):
    return expr.xreplace(jets).subs({y:0,h0:eta*z+epsilon-x*hx0/2,hz0:eta})
fcritical = sp.simplify(critical_jet(f))
assert sp.simplify(fcritical+x**3*hx0/2) == 0

hessian = sp.hessian(f, (x, y, z))
plane = hessian.extract([0, 2], [0, 2])
planecritical = plane.applyfunc(critical_jet)
expected_plane = sp.Matrix([
    [x*(3*hx0+x*hxx0), x*x*hxz0],
    [x*x*hxz0, x*x*hzz0]
])
assert all(sp.simplify(v) == 0 for v in planecritical-expected_plane)
ordered = sp.Matrix([G-2*eta*z-2*epsilon, hz-eta])
J = sp.simplify(critical_jet(ordered.jacobian([x,z]).det()))
assert sp.simplify(planecritical.det()-x**3*J) == 0
assert hessian[1,1] == 2*x
universal = sp.Matrix([hz-eta,G-2*eta*z-2*epsilon]).jacobian([eta,epsilon])
assert universal.det() == 2

h,a,b = sp.symbols('h a b')
Delta = 4*h*b-a*a
assert sp.diff(Delta,b) == 4*h

# A smooth A3 critical axis whose residual normal branch is simple elliptic.
H0 = z*(x-z)*(x-2*z)
f0 = x*(y*y+x*H0)
Hz0 = sp.diff(H0,z)
G0 = 2*H0+x*sp.diff(H0,x)
f0_derivatives = [sp.diff(f0,v) for v in (x,y,z)]
# For x != 0, the undeformed critical equations force y=0, Hz0=G0=0.
# Their common plane zero is isolated; homogeneneity then gives the origin.
axis_resultant = sp.factor(sp.resultant(Hz0,G0,x))
assert axis_resultant == -50*z**6

eq = [Hz0,G0-2]
gb = sp.groebner(eq,x,z,order='lex')
polys = [sp.expand(p.as_expr()) for p in gb.polys]
univariate = [p for p in polys if not p.has(x)]
assert len(univariate) == 1
pz = univariate[0]
assert sp.degree(pz,z) == 6
assert sp.gcd(pz,sp.diff(pz,z)) == 1
assert sp.rem(pz,z,z) != 0
linear_x = [p for p in polys if sp.degree(p,x) == 1]
assert len(linear_x) == 1
assert not sp.diff(linear_x[0],x).has(z)

J0 = sp.Matrix([G0-2,Hz0]).jacobian([x,z]).det()
unit_tests = {}
for label, bad in [('x',x),('H_x',sp.diff(H0,x)),('Jacobian',J0)]:
    test = sp.groebner(eq+[bad],x,z,order='lex')
    passed = len(test.polys) == 1 and test.polys[0].as_expr() == 1
    assert passed
    unit_tests[label] = passed
deformed = f0-x*x
full_hessian_det = sp.hessian(deformed,(x,y,z)).det().subs(y,0)
remainder = gb.reduce(sp.expand(full_hessian_det-2*x**4*J0))[1]
assert remainder == 0
fcrit_remainder = gb.reduce(sp.expand(2*deformed.subs(y,0)+x**3*sp.diff(H0,x)))[1]
assert fcrit_remainder == 0

# In H0-epsilon the six plane solutions scale by epsilon^(1/3).
s = sp.symbols('s')
assert sp.expand(Hz0.subs({x:s*x,z:s*z},simultaneous=True)-s*s*Hz0) == 0
assert sp.expand(G0.subs({x:s*x,z:s*z},simultaneous=True)-s**3*G0) == 0

result = {
  'statement':'P4R.14',
  'critical_value':str(fcritical),
  'plane_hessian':[[str(v) for v in row] for row in planecritical.tolist()],
  'jacobian_order':['G-2*eta*z-2*epsilon','H_z-eta'],
  'plane_hessian_determinant':'x^3 * J',
  'full_hessian_determinant':'2*x^4 * J',
  'parameter_jacobian_order':['H_z-eta','G-2*eta*z-2*epsilon'],
  'parameter_jacobian_determinant':2,
  'example':str(sp.expand(f0)),
  'undeformed_polar_resultant':str(axis_resultant),
  'epsilon_one_groebner_basis':[str(p) for p in polys],
  'epsilon_one_solution_count':6,
  'forbidden_loci_unit_ideals':unit_tests,
  'scaling':'(x,z) -> epsilon^(1/3)*(x,z)',
  'all_checks_passed':True
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print('Smooth A3 polar identities: PASS')
print('Jacobian order: (G-2*eta*z-2*epsilon, H_z-eta).')
print('Critical value = -x^3 H_x/2; full Hessian determinant = 2 x^4 J.')
print('Explicit simple elliptic residual example:',sp.expand(f0))
print('Undeformed polar resultant:',axis_resultant)
print('Exact Groebner basis at epsilon=1:',polys)
print('Six simple plane solutions, all x*H_x*J nonzero; every critical value nonzero.')
print('All six converge to the origin under the exact epsilon^(1/3) scaling.')
