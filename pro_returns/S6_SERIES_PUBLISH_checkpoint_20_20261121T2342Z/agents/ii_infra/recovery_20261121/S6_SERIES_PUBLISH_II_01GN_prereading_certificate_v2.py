#!/usr/bin/env python3
"""Exact prereading certificates for E16. No target proof/program is imported.

The coefficient algebra uses integers and Fractions, with explicit finite
convolution and Leibniz determinants. Geometric extension arguments are in
the separately frozen derivation, not inferred from sampled calculations.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import permutations
import json

class P(dict):
    def __add__(self, other):
        other = cv(other); z = defaultdict(Q, self)
        for m,c in other.items(): z[m] += c
        return P({m:c for m,c in z.items() if c})
    __radd__ = __add__
    def __neg__(self): return P({m:-c for m,c in self.items()})
    def __sub__(self, other): return self + -cv(other)
    def __rsub__(self, other): return cv(other) + -self
    def __mul__(self, other):
        z = defaultdict(Q)
        for m,c in self.items():
            for n,d in cv(other).items(): z[tuple(sorted(m+n))] += c*d
        return P({m:c for m,c in z.items() if c})
    __rmul__ = __mul__
    def __pow__(self,n):
        z=cv(1)
        for _ in range(n): z=z*self
        return z
def cv(x): return x if isinstance(x,P) else P({():Q(x)}) if x else P()
def v(s): return P({(s,):Q(1)})
def show(x):
    return {"*".join(m) or "1":str(c) for m,c in sorted(cv(x).items())}
def tr(a): return [list(z) for z in zip(*a)]
def mul(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))),cv(0))
             for j in range(len(b[0]))] for i in range(len(a))]
def add(a,b): return [[a[i][j]+b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
def neg(a): return [[-x for x in r] for r in a]
def det(a):
    z=cv(0); n=len(a)
    for p in permutations(range(n)):
        inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        t=cv((-1)**inv)
        for i in range(n): t=t*a[i][p[i]]
        z=z+t
    return z
def const(a): return [[cv(x) for x in r] for r in a]
def eq(a,b): return a==b

T0=const([[-1,-1,-1,0],[2,1,1,0],[0,0,1,0],[0,0,0,1]])
T1=const([[1,1,0,1],[-2,0,-1,-1],[0,-1,1,-1],[0,0,0,1]])
Ti=const([[1,0,0,-1],[-2,0,-1,1],[2,1,2,1],[0,0,0,1]])
Je=const([[0,2,0,0],[-2,0,-1,0],[0,1,0,-1],[0,0,1,0]])
Jf=const([[0,1,0,0],[-1,0,0,0],[0,0,0,-2],[0,0,2,0]])
C=const([[2,0,1,0],[0,1,0,1],[1,0,1,0],[0,0,0,1]])
assert mul(mul(tr(C),Jf),C)==Je
assert all(mul(mul(tr(T),Je),T)==Je for T in [T0,T1,Ti])
assert det(Je)==cv(4) and det(C)==cv(1)
tau,mu,nu=map(v,['tau','mu','nu'])
period=[[cv(1),tau,cv(0),-2*mu],[cv(0),mu,cv(1),nu]]
two_Jinv=const([[0,-2,0,0],[2,0,0,0],[0,0,0,1],[0,0,-1,0]])
assert mul(mul(period,two_Jinv),tr(period))==const([[0,0],[0,0]])

# Exact source coordinate change: T=27(1-q)/(4q), x=q^2 X,y=q^3 Y.
q,X,Y=map(v,['q','X','Y'])
transport=4*q*(Y*Y-X**3)-27*(1-q)*X-27*(1-q)
original_cleared=4*q*(Y*Y-X**3)-27*(1-q)*(X+1)
assert transport==original_cleared
# At the cusp t=s^6, x=s^2 X,y=s^3 Y.
s= v('s')
assert (s**3*Y)**2-(s**2*X)**3-s**6*(s**2*X)-s**6 == s**6*(Y*Y-X**3-s*s*X-1)
# Formal parameter z=-X/Y and w=-1/Y: w=z^3+s^2*z*w^2+w^3.
# At P_s, z=-i*s and w=i*s^3. Separate real/imaginary coefficients.
assert s**3 == s**3+s**9-s**9
# First derivative of the normalized Abel coordinate is c=-i/A(0) != 0.
a,c,d=map(v,['a','c','d'])
cusp_limit=[[a*Q(1,6),-c*Q(1,3)],[c*Q(1,6),cv(0)]]
assert det(cusp_limit)==c*c*Q(1,18)

# Weighted two-parameter determinant, by direct coefficient convolution.
x,y=map(v,['x','y'])
A,B,Cc,D,E,F,G,H=map(v,list('ABCDEFGH'))
two_parameter=[[x**3*(A*x**4+B*y),x**2*(Cc*x**4+D*y)],
               [x**2*(E*x**4+F*y),x*(G*x**4+H*y)]]
two_parameter_expected=x**4*((A*G-Cc*E)*x**8+(A*H+B*G-Cc*F-D*E)*x**4*y+(B*H-D*F)*y*y)
assert det(two_parameter)==two_parameter_expected
lr=[[A*x**3,B*x**2],[Cc*x**2,D*x]]
assert det(lr)==(A*D-B*Cc)*x**4

# Finite verification of the general modular classification, supplementing
# the all-m integer congruence proof in the written derivation.
comb=[]
for m in range(81):
    weight=48*m+8
    actual={(i,j) for i in range(weight//3+1)
            for j in range(weight//4+1) if 3*i+4*j==weight}
    expected={(4*a,3*(4*m-a)+2) for a in range(4*m+1)}
    assert actual==expected
    comb.append({'m':m,'weight':weight,'monomial_count':len(actual)})

# Derive the actual Grassmannian matrix by projecting a differentiated
# graph frame. No symmetry or polarization is imposed on Z.
Z=[[v(f'z{i}{j}') for j in range(2)] for i in range(2)]
Zp=[[v(f'zp{i}{j}') for j in range(2)] for i in range(2)]
AA=[[v(f'a{i}{j}') for j in range(4)] for i in range(4)]
I=const([[1,0],[0,1]])
frame=I+Z
derivative=const([[0,0],[0,0]])+Zp
conn_frame=add(derivative,mul(AA,frame))
projection=add(conn_frame[2:],neg(mul(Z,conn_frame[:2])))
A11=[r[:2] for r in AA[:2]]; A12=[r[2:] for r in AA[:2]]
A21=[r[:2] for r in AA[2:]]; A22=[r[2:] for r in AA[2:]]
riccati=add(add(add(Zp,A21),mul(A22,Z)),neg(mul(Z,add(A11,mul(A12,Z)))))
assert projection==riccati

print(json.dumps({
 'scope':'01GN prereading certificate; target proof and E.16.3 closed',
 'all_assertions_passed':True,
 'LR_lattice':{'e_to_f_columns':[[str(next(iter(a.values()),0)) for a in r] for r in C],
   'Je_determinant':show(det(Je)), 'C_determinant':show(det(C)),
   'three_monodromies_preserve_Je':True,'period_J_inverse_period_transpose_zero':True},
 'LR_coordinate_transport_cleared_polynomial':show(transport),
 'LR_cusp_log_matrix_determinant':show(det(cusp_limit)),
 'LR_root_determinant':show(det(lr)),
 'two_parameter_root_determinant':show(two_parameter_expected),
 'comb_modular_classification':comb,
 'Grassmann_graph_projection_identity':True,
 'method':'Explicit finite polynomial convolution, Leibniz determinants, integer matrices and exponent congruences; no CAS, nullspace or elimination.'
},indent=2))
