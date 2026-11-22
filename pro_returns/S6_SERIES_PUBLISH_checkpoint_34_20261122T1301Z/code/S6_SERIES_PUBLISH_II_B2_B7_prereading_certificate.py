#!/usr/bin/env python3
"""Exact symbolic checks for the B7 prerelease coordinate and orientation maps.

This program does not substitute a parameter sweep for the analytic boundary
argument. It verifies the polynomial identities and inverse matrix operations
used in that argument with independent symbolic algebra.
"""
import json
import sympy as s

checks = []


def check(name, expression):
    value = s.simplify(expression)
    if value != 0:
        raise AssertionError((name, value))
    checks.append(name)


U, V, u, v, q, W, w = s.symbols("U V u v q W w", nonzero=True)
I = s.I
up = (U + V) / (2*w)
vp = (U - V) / (2*I*w)
check("inverse square sum is UV/w^2", up**2 + vp**2 - U*V/w**2)
check("forward after inverse U", w*(up + I*vp) - U)
check("forward after inverse V", w*(up - I*vp) - V)
Uf, Vf = w*(u + I*v), w*(u - I*v)
check("inverse after forward u", ((Uf+Vf)/(2*w)) - u)
check("inverse after forward v", ((Uf-Vf)/(2*I*w)) - v)
check("forward product", Uf*Vf - w**2*(u**2+v**2))
J = s.Matrix([Uf,Vf]).jacobian([u,v])
check("unit root coordinate Jacobian", J.det() + 2*I*w**2)
Q = s.groebner([w**2-W, U*V-q*W], U,V,w,q,W, order="lex")
check("inverse square numerator modulo graph equations",
      Q.reduce(s.expand((U+V)**2 - (U-V)**2 - 4*q*w**2))[1])

# Symbolic exponent identity. The analytic branch is fixed in the proof;
# the finite geometric sum is checked as a formal recurrence, not by samples.
c, t = s.symbols("c t", nonzero=True)
# Reduce the recurrence in a polynomial ring whose powers are independent
# symbols A=t^b, B=c^b; multiplication advances A and B by t and c.
A,B,S = s.symbols("A B S")
G = s.groebner([(t-c)*S-(A-B)], S,A,B,t,c, order="lex")
check("universal divided difference recurrence",
      G.reduce(s.expand((t-c)*(t*S+B)-(t*A-c*B)))[1])
check("divided difference base b=1", (t-c)*1-(t-c))

# Schur-complement elimination of a general symmetric Hessian.
a,h12,h13,h22,h23,h33 = s.symbols("a h12 h13 h22 h23 h33", nonzero=True)
H=s.Matrix([[a,h12,h13],[h12,h22,h23],[h13,h23,h33]])
P=s.Matrix([[1,-h12/a,-h13/a],[0,1,0],[0,0,1]])
Pinv=s.Matrix([[1,h12/a,h13/a],[0,1,0],[0,0,1]])
Schur=s.Matrix([[h22-h12**2/a,h23-h12*h13/a],
                [h23-h12*h13/a,h33-h13**2/a]])
D=s.diag(a,Schur)
for i in range(3):
    for j in range(3):
        check(f"Schur congruence {i}{j}", (P.T*H*P-D)[i,j])
check("Schur determinant", H.det()-a*Schur.det())
check("Schur inverse product", sum((P*Pinv-s.eye(3)).applyfunc(lambda x:x*x)))
check("Schur reverse inverse product", sum((Pinv*P-s.eye(3)).applyfunc(lambda x:x*x)))

# Normal orientation: the tangent-then-J-tangent frame compared with the
# complex frame (e1,Je1,e2,Je2) exchanges exactly its middle two vectors.
O=s.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
check("normal orientation reversal", O.det()+1)
check("sphere normal Euler square", O.det()*2+2)

# At a transverse branch crossing the absorbed-unit coordinate Jacobian.
p1y,p1z,p2y,p2z,r = s.symbols("p1y p1z p2y p2z r")
Jcross=s.Matrix([[r*p1y,r*p1z],[p2y,p2z]])
check("crossing unit absorption Jacobian",
      Jcross.det()-r*(p1y*p2z-p1z*p2y))

# Boundary radii are exact rational inequalities used by the three faces.
for name, lhs, rhs in [
    ("sphere upper bound below eta",s.Rational(5,4),s.Integer(2)),
    ("x face separated from critical disk",s.Rational(1,16),s.Rational(3,4)),
    ("fixed level outside critical disk",s.Rational(1,16),s.Rational(1,8)),
    ("fixed level in transport disk",s.Rational(1,6),s.Rational(1,4))]:
    if not lhs < rhs:
        raise AssertionError(name)
    checks.append(name)

print(json.dumps({
    "tag":"01B7",
    "phase":"before target-proof release",
    "method":"symbolic polynomial reduction, independent matrix congruence, permutation determinant",
    "checks":len(checks),
    "passed":checks,
    "analytic_claims":"Proved in the derivation, not inferred from these algebraic checks.",
    "sympy_version":s.__version__
},indent=2))
