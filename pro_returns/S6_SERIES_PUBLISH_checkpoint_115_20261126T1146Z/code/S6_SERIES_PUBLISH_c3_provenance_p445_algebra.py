#!/usr/bin/env python3
"""Exact polynomial checks for the exposed P280/P4.45 derivation.

This is an editorial algebra check. It does not prove analytic normality,
factor lifting, boundary admissibility or the topological transport.
"""
import json
import sympy as s

a,b,c,d,h,w,t=s.symbols('a b c d h w t')
f=a*h**3+b*h**2*w+c*h*w**2+d*w**3
M=s.Matrix([[-a*h,-b*h,c*h+d*w],[w,-h,0],[0,w,h]])
assert s.expand(M.det()-f)==0

omega=a*t
nu=a*t**2+b*t
q=a*t**3+b*t**2+c*t+d
products=[omega**2+b*omega-a*nu,
          omega*nu+a*d+c*omega,
          nu**2+b*d+d*omega+c*nu]
for p in products:
    assert s.rem(p,q,t)==0
relations=(s.Matrix([[1,omega,nu]])*M).subs(h,w*t)
for p in relations:
    assert s.rem(s.expand(p),q,t)==0

v,A,B,C,mu1,mu2,mu3=s.symbols('v A B C mu1 mu2 mu3')
critical=(mu1*(v-B)*(v-C)+mu2*(v-A)*(v-C)
          +mu3*(v-A)*(v-B))
for root,weight,other in [(A,mu1,(B,C)),(B,mu2,(A,C)),(C,mu3,(A,B))]:
    assert s.expand(critical.subs(v,root)-weight*(root-other[0])*(root-other[1]))==0
disc=s.factor(s.discriminant(critical.subs({A:-1,B:0,C:1}),v))
assert s.expand(disc-((mu1-mu3)**2+4*mu2*(mu1+mu2+mu3)))==0

N,q0,L,q11,q12,q22,z1,z2=s.symbols('N q0 L q11 q12 q22 z1 z2', nonzero=True)
Q=s.Matrix([[q11,q12],[q12,q22]])
z=s.Matrix([z1,z2])
schur=N*q0**(N-1)*Q
full=s.Matrix.vstack(s.Matrix([[L,z1,z2]]),s.Matrix.hstack(z,schur+z*z.T/L))
assert s.simplify(full.det()-L*N**2*q0**(2*N-2)*Q.det())==0

print(json.dumps({
    'status':'passed',
    'checks':['determinant presentation', 'three cubic-algebra products',
              'three generator relations', 'weighted critical numerator at each root',
              'positive real-root discriminant formula', 'Schur complement determinant'],
    'discriminant_at_minus_one_zero_one':s.sstr(disc),
    'scope':'exact polynomial identities only; exposed analytic proof separately read'
},indent=2))
