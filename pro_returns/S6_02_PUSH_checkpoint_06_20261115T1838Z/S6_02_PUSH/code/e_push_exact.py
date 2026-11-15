"""Exact lattice dictionary and weighted-cohomology checks for Part E.

All arithmetic is integral or rational.  Numerical checks supplement the
symbolic arguments in sections/E_push.tex; they do not replace them.
"""
from math import gcd
from pathlib import Path
import json
import sympy as S

A1=S.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=S.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
V0=S.Matrix([[1,-1,0,2],[0,-1,-1,6],[0,1,0,0],[0,0,0,1]])
V1=S.Matrix([[1,0,1,-3],[0,0,1,0],[0,-1,0,6],[0,0,0,1]])
QE=S.Matrix([[-2,1,0,-2],[-1,0,0,0],[3,-1,1,0],[0,0,0,1]])
PE=S.Matrix([[0,-2,-1,-2],[2,-1,0,-1],[0,2,1,3],[-1,0,0,0]])
PV=QE.inv()*PE
eps=S.Matrix([1,2,-4,0]); eps2=S.Matrix([1,3,-3,0]); d=S.Matrix([0,0,0,1])
u0=S.Matrix([0,2,2,1]);u1=S.Matrix([0,3,3,1]);delta=S.Matrix([1,0,0,0])
print('Viaclovsky column change PV = QE^(-1) PE:')
print(PV)
print('det(PV) =',PV.det())
assert V0*PV==PV*A1 and V1*PV==PV*A2
for name,v in [('delta_hat',d),('epsilon',eps),('epsilon_prime',eps2)]:
    print(name,'maps to',list(PV*v))
assert PV*d==delta
assert PV*eps==-u0
assert PV*eps2==delta-u1
print('Both monodromy intertwining identities and all fixed-vector identities: PASS')

def h0(m,n,d):
    if d<0:return 0
    return sum(1 for a in range(d//m+1) if (d-m*a)%n==0)
def h1(m,n,d):return h0(m,n,-d-m-n)
def h(m,n,d):return (h0(m,n,d),h1(m,n,d))
def add(*vectors):return tuple(sum(x) for x in zip(*vectors))
def cohom_pull(m,n,d,z):
    # R^q f_* O = O; O+O(-z); O(-z), q=0,1,2.
    return (h0(m,n,d),h1(m,n,d)+h0(m,n,d)+h0(m,n,d-z),
            h1(m,n,d)+h1(m,n,d-z)+h0(m,n,d-z),h1(m,n,d-z))

count=0;examples=[];slope_pairs={}
for k in range(1,81):
    for l in range(1,81):
        m,n,z=3*k,4*l,k*l
        if gcd(m,n)!=1:continue
        count+=1
        slope=S.Rational(z-m-n,m*n)
        assert slope not in slope_pairs
        slope_pairs[slope]=(m,n)
        reduced=S.Rational(1,12)-slope
        assert int(S.numer(reduced))==m+n and int(S.denom(reduced))==m*n
        for a in [1,2]:assert h(m,n,-a*z)==(0,0)
        assert h1(m,n,z)==0
        b=m+n-12*z
        assert h(m,n,b)==(0,0)
        e=int(k>1)
        assert h(m,n,b-z)==(0,e)
        vertical=add(cohom_pull(m,n,0,z),cohom_pull(m,n,-z,z))
        horizontal=cohom_pull(m,n,b,z)
        assert vertical==(1,1,0,0)
        assert horizontal==(0,0,e,e)
        assert h0(m,n,z-m-n)==0 and h0(m,n,2*z-m-n)==0
        assert h0(m,n,13*z-2*m-2*n)==e
        if e:
            assert (3*l-2)*m+(k-2)*n==13*z-2*m-2*n
        if (k,l) in [(1,1),(1,2),(3,1),(5,7),(9,11),(79,80)]:
            examples.append({'k':k,'l':l,'m':m,'n':n,'vertical':vertical,
                'horizontal':horizontal,'canonical_weight':z-m-n,
                'residue_monomial_exponents':[3*l-2,k-2] if e else None})
print('All weighted-cohomology identities through k,l <= 80:',count,'coprime pairs: PASS')
print('Signed canonical slope uniquely recovers all',len(slope_pairs),'multiplicity pairs: PASS')
print(json.dumps(examples,indent=2))

E=d*S.Matrix([[1,0,0,0]])
variables=S.symbols('x0:16')
C=S.Matrix(4,4,variables)
equations=list(C*A1-A1*C)+list(C*A2-A2*C)
null=S.linear_eq_to_matrix(equations,variables)[0].nullspace()
assert len(null)==2
print('Rational simultaneous centralizer dimension:',len(null))
for v in null:print(S.Matrix(4,4,v))
for m,A,e0,delta_step in [(3,A1,eps,1),(4,A2,eps2,2)]:
    norm=sum((A**j for j in range(m)),S.zeros(4))
    coords=S.Matrix.hstack(e0,d).inv() if False else None
    print('Base norm N_'+str(m)+':',norm.tolist())
print('Exact arithmetic checks completed.')
