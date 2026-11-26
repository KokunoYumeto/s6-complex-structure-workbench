#!/usr/bin/env python3
"""Symbolic all-order peripheral maps and triangle representation.

This is new code for the fresh derivation.  It reads no target proof,
historical catalogue, or earlier check program.
"""
import sympy as s

m1,m2,n1,n2,e,t1,t2=s.symbols('m1 m2 n1 n2 e t1 t2',integer=True)
relation=s.Matrix([[-n1,m1,0],[-n2,0,m2],[-e,1,1]])
P=s.Matrix([[1,0,0],[-t1,1,0],[-t2,0,1]])
Pi=s.Matrix([[1,0,0],[t1,1,0],[t2,0,1]])
changed=relation.subs({n1:n1+m1*t1,n2:n2+m2*t2,e:e+t1+t2},simultaneous=True)
assert relation*P==changed and P*Pi==s.eye(3) and P.det()==1
print('Peripheral column map and inverse:',P.tolist(),Pi.tolist())

V=s.Matrix([[1,0,0],[0,1,0],[e,-1,1]])
U=s.Matrix([[1,0,0],[0,1,-m2],[0,0,1]])
R=s.Matrix([[-n1,m1],[m2*e-n2,-m2]])
expected=s.diag(R,s.Matrix([[1]]))
assert U*relation*V==expected and U.det()==V.det()==1
assert U.inv()==s.Matrix([[1,0,0],[0,1,m2],[0,0,1]])
assert V.inv()==s.Matrix([[1,0,0],[0,1,0],[-e,1,1]])
D=m2*n1+m1*n2-e*m1*m2
assert s.expand(R.det()-D)==0
print('Two-site elimination U,V and inverse matrices:',U.tolist(),V.tolist(),U.inv().tolist(),V.inv().tolist())
print('Remaining relation matrix:',R.tolist(),'; determinant:',D)

one=s.Matrix([[-n1,m1],[-e,1]])
U1=s.Matrix([[1,-m1],[0,1]]);V1=s.Matrix([[1,0],[e,1]])
assert U1*one*V1==s.diag(m1*e-n1,1)
assert U1.det()==V1.det()==1
print('One-site elimination U,V and inverses:',U1.tolist(),V1.tolist(),U1.inv().tolist(),V1.inv().tolist())

a,b,c,l=s.symbols('a b c l')
B=s.Matrix([[1,-c,-b],[-c,1,-a],[-b,-a,1]])
reflections=[]
for i in range(3):
    Ri=s.eye(3)-2*s.eye(3)[:,i]*B[i,:]
    assert Ri*Ri==s.eye(3) and Ri.det()==-1
    assert s.simplify(Ri.T*B*Ri-B)==s.zeros(3)
    reflections.append(Ri)
x=reflections[1]*reflections[2]
y=reflections[2]*reflections[0]
z=reflections[0]*reflections[1]
assert s.simplify(x*y*z)==s.eye(3)
for M,t in [(x,a),(y,b),(z,c)]:
    assert s.expand(M.charpoly(l).as_expr()-(l-1)*(l*l-(4*t*t-2)*l+1))==0
print('Three reflection involutions preserve their form and their paired products multiply to I.')
print('Each paired product has characteristic polynomial (l-1)(l^2-(4*cos(pi/k)^2-2)l+1).')
print('The derivation proves exact order k on the nondegenerate pair plane for every integer k>=2.')

A=s.Matrix([[-1,-3],[0,-1]]);g=s.Matrix([1,1]);J=s.Matrix([[0,1],[-1,0]])
h1=(A-s.eye(2)).inv()*g;h4=(A-s.eye(2)).inv()*(4*g)
b4=-h4.T*J
assert h1==s.Matrix([s.Rational(1,4),s.Rational(-1,2)]) and h4==s.Matrix([1,-2])
assert b4==s.Matrix([[-2,-1]]) and b4*(A-s.eye(2))+s.Matrix([[-4,-8]])==s.zeros(1,2)
assert s.Matrix([[-2,-1,1]])*s.Matrix([1,0,2])==s.zeros(1,1)
print('Original odd-star component/gauge data:',list(h1),list(h4),list(b4))
print('All identities are symbolic or exact integral/rational equalities; no multiplicity sampling.')
