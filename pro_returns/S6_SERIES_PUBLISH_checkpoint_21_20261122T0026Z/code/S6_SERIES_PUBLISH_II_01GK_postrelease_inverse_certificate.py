#!/usr/bin/env python3
"""E13 postrelease certificate by explicit inverses and coefficient arithmetic.

No SymPy, elimination, determinant, nullspace, or factorization routine is
used. Laurent polynomials are finite exponent -> integer coefficient maps.
This is postrelease comparison work and adds no independent event.
"""
from pathlib import Path
import hashlib
import json

names=('p1','p2','p3','h1','h2','q1','q2','u','v','mu','e1','e2','b','r','x','y','a1','a2')
n=len(names)
zero=(0,)*n

class P:
    def __init__(self,terms=0):
        if isinstance(terms,int): terms={} if terms==0 else {zero:terms}
        self.t={tuple(k):int(v) for k,v in terms.items() if v}
    def __add__(self,o):
        o=coerce(o); d=dict(self.t)
        for k,v in o.t.items(): d[k]=d.get(k,0)+v
        return P(d)
    __radd__=__add__
    def __neg__(self): return P({k:-v for k,v in self.t.items()})
    def __sub__(self,o): return self+-coerce(o)
    def __rsub__(self,o): return coerce(o)+-self
    def __mul__(self,o):
        o=coerce(o);d={}
        for a,x in self.t.items():
            for b,y in o.t.items():
                k=tuple(i+j for i,j in zip(a,b)); d[k]=d.get(k,0)+x*y
        return P(d)
    __rmul__=__mul__
    def __pow__(self,k):
        if k<0:
            assert len(self.t)==1
            exp,c=next(iter(self.t.items()));assert c==1
            return P({tuple(k*i for i in exp):1})
        out=P(1)
        for _ in range(k):out=out*self
        return out
    def __eq__(self,o):return self.t==coerce(o).t
    def coefficient(self,name):
        j=names.index(name);d={}
        for e,c in self.t.items():
            if e[j]==1:
                z=list(e);z[j]=0;d[tuple(z)]=c
            else:assert e[j]==0
        return P(d)
    def serial(self):
        return [{'coefficient':c,'powers':{names[i]:v for i,v in enumerate(e) if v}}
                for e,c in sorted(self.t.items())]

def coerce(x):return x if isinstance(x,P) else P(x)
def var(name):
    e=[0]*n;e[names.index(name)]=1;return P({tuple(e):1})
def product(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),P(0))
             for j in range(len(B[0]))] for i in range(len(A))]
def diagonal(d,k):return [[d if i==j else P(0) for j in range(k)] for i in range(k)]

vrs={name:var(name) for name in names}
p1,p2,p3,h1,h2,q1,q2,u,v=[vrs[x] for x in names[:9]]
D1=p1-p3;D2=p2-p3;H=h1-h2;D=H*D1*D2
U1=q1-u+h1*v;U2=q2-u+h2*v
Bnum=D1*U2-D2*U1
Anum=h1*D1*U2-h2*D2*U1
coeffs=[u*D-p3*Anum,Anum,v*D-p3*Bnum,Bnum]
Bmat=[[a.coefficient(z) for z in ('q1','q2','u','v')] for a in coeffs]
R=[[P(1),p1,-h1,-h1*p1],[P(1),p2,-h2,-h2*p2],
   [P(1),p3,P(0),P(0)],[P(0),P(0),P(1),p3]]
assert product(R,Bmat)==diagonal(D,4)
assert product(Bmat,R)==diagonal(D,4)

a1,a2=vrs['a1'],vrs['a2']
M=[[P(1),-a1],[P(1),-a2]]
N=[[-a2,a1],[-P(1),P(1)]]
assert product(M,N)==diagonal(a1-a2,2)
assert product(N,M)==diagonal(a1-a2,2)
# In the two named differential conventions a_i=2*h_i.
Mfresh=[[P(1),-h1],[P(1),-h2]]
Mprinted=[[P(1),-2*h1],[P(1),-2*h2]]
assert product(Mfresh,[[P(1),P(0)],[P(0),P(2)]])==Mprinted

mu,e1,e2,b,r,x,y=[vrs[z] for z in ('mu','e1','e2','b','r','x','y')]
assert b*(e2+mu)-b*(e1+mu)==b*(e2-e1)
left=(r**(-3)*y+b)*r*(x+mu*r**2)
right=(y+b*r**3)*(r**(-2)*x+mu)
assert left==right
# Exponents in the relative differential/connection comparison cancel.
assert -3+1-(-2)==0

out={'schema':'S6_SERIES_PUBLISH.postrelease_different_method.v1',
     'target':'01GK/cdp:st:E13','timing':'after independent freeze and target release',
     'method':'Explicit interpolation inverse; coefficient-map multiplication in an integer Laurent polynomial ring.',
     'forbidden_algorithms_used':[],
     'checks':{'R_B_equals_D_identity':True,'B_R_equals_D_identity':True,
               'printed_two_by_two_left_inverse':True,'printed_two_by_two_right_inverse':True,
               'exact_factor_two_basis_transport':True,'residue_difference_cross_product':True,
               'good_reduction_Laurent_cross_product':True},
     'inverse_denominator':'D=(h1-h2)(p1-p3)(p2-p3)',
     'inverse_formula':{'U1':'q1-u+h1*v','U2':'q2-u+h2*v',
       'Bnum':'(p1-p3)U2-(p2-p3)U1',
       'Anum':'h1(p1-p3)U2-h2(p2-p3)U1',
       'coefficient_numerators':['uD-p3*Anum','Anum','vD-p3*Bnum','Bnum']},
     'explicit_inverse_numerator_matrix':[[a.serial() for a in row] for row in Bmat],
     'all_polynomial_comparisons_exact':True,'independent_events_added':0,
     'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
p=Path(__file__).with_name(Path(__file__).stem+'_output.json')
p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
                  'all_assertions_passed':True,'events_added':0}))
