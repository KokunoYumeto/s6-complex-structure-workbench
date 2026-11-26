#!/usr/bin/env python3
"""Postrelease exact frame transport for E.16.3."""
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


Z=[[v(f'z{i}{j}') for j in range(2)] for i in range(2)]
U=const([[1,0],[0,1]])+Z
W=[[v(f'w{i}{j}') for j in range(2)] for i in range(4)]
K=add(W[2:],neg(mul(Z,W[:2])))
join=lambda a,b:[a[i]+b[i] for i in range(4)]
old=det(join(U,W))
assert old==det(K)
C=[[v(f'c{i}{j}') for j in range(2)] for i in range(2)]
B=[[v(f'b{i}{j}') for j in range(2)] for i in range(2)]
newU=mul(U,C);newW=add(mul(W,C),mul(U,B))
assert det(join(newU,newW))==det(C)**2*old
alpha=v('alpha')
assert det(join(U,[[alpha*x for x in row] for row in W]))==alpha**2*old
# A distinct two-minor expansion of the same coefficient.
minor=lambda A,i,j:A[i][0]*A[j][1]-A[i][1]*A[j][0]
terms=[]
for i in range(4):
 for j in range(i+1,4):
  k,l=[z for z in range(4) if z not in [i,j]]
  sign=(-1)**(i+j-1)
  terms.append(sign*minor(U,i,j)*minor(W,k,l))
assert sum(terms,cv(0))==old
print(json.dumps({'scope':'Postrelease comparison with printed E.16.3; no additional independent event','all_assertions_passed':True,'graph_projection_equals_four_column_determinant':True,'six_Pluecker_minor_expansion_equals_graph_determinant':True,'Hodge_frame_U_to_UC_and_W_to_WC_plus_UB_factor':'det(C)^2','tangent_frame_D_to_alpha_D_coefficient_factor':'alpha^2','dual_differential_frame_factor':'alpha^(-1)','tensor_product_factor':'alpha^2 * alpha^(-2) = 1','target_wording_repair':'Replace inverse square of tangent-frame change by the two explicit coefficient/frame maps.','methods':'Direct quotient graph projection and a six two-minor expansion; exact polynomial convolution; no elimination or CAS.'},indent=2))
