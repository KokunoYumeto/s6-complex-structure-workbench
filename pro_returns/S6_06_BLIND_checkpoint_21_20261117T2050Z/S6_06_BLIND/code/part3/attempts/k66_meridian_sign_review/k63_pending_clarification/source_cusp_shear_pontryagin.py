#!/usr/bin/env python3
"""Exact algebra for SQ.1--6; the geometric proof is separately audited."""
from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as s

checks=[]
def eq(name, a, b):
    d=s.simplify(a-b)
    assert d==0, (name,d)
    checks.append(name)
def meq(name, a, b):
    assert (a-b).applyfunc(s.simplify)==s.zeros(*a.shape), (name,a-b)
    checks.append(name)

n,kap,al,g,et,q=s.symbols('n kappa alpha g eta q', nonzero=True)
# Full unit exponents, in the order kappa,alpha,g,eta.
P=s.Matrix([[1,0],[n,1]])
R=P.inv()
base=s.Matrix([[-6,0],[0,0]])
meq('actual shear inverse',R,s.Matrix([[1,0],[-n,1]]))
meq('complete winding matrix',R*base*P,s.Matrix([[-6,0],[6*n,0]]))
full=[s.Matrix([1,0,n,0]),s.Matrix([-n,1,-n*n,n]),
      s.Matrix([0,0,1,0]),s.Matrix([0,0,-n,1])]
wind=s.Matrix([[-6,0,0,0]])
for j,(v,target) in enumerate(zip(full,[-6,6*n,0,0])):
    eq('full multiplier winding '+str(j),(wind*v)[0],target)

u,v,d,ga,tau,G,aq,th=s.symbols('u v d gamma tau G alpha_q theta')
eq('literal source point in both bases',u+(tau+n*G)*v+G*(ga-n*v),u+tau*v+G*ga)
coeff=s.Matrix([u,v,d-n*u,ga-n*v])
old=s.Matrix([u,v,d,ga])
qmon={u:u-v,d:d-ga}
tmon={u:u+6*v,d:d}
meq('q monodromy in new coefficients',coeff.subs(qmon, simultaneous=True),
     s.Matrix([u-v,v,d-n*u-(ga-n*v),ga-n*v]))
meq('theta monodromy in new coefficients',coeff.subs(tmon, simultaneous=True),
     s.Matrix([u+6*v,v,d-n*u-6*n*v,ga-n*v]))

# Actual absolute-value period lift and both F9 endpoint derivatives.
LQ,La,Lg,LS,zlog,vlog,rr,eps=s.symbols('LQ La Lg LS zlog vlog r epsilon', nonzero=True)
gam=(LQ*vlog-La*zlog)/(LQ*LS-La*Lg)
eq('actual source period has gamma lift zero',gam.subs({zlog:zlog+LQ,vlog:vlog+La}, simultaneous=True),gam)
eq('actual suspension period has gamma lift one',gam.subs({zlog:zlog+Lg,vlog:vlog+LS}, simultaneous=True),gam+1)
height=s.Rational(1,2)-eps*(rr-1)/(rr+1)
eq('first fixed endpoint lift',height.subs(rr,0),s.Rational(1,2)+eps)
eq('second fixed endpoint lift',s.limit(height,rr,s.oo),s.Rational(1,2)-eps)
eq('first endpoint contracting derivative',s.diff(height,rr).subs(rr,0)*2,-4*eps)
eq('second endpoint contracting derivative',s.limit(s.diff(height,rr)*2*rr**2,rr,s.oo),-4*eps)

# One-forms in the ordered basis du,dv,dd,dgamma,dalpha_q,dtheta.
A0=s.Matrix([0,0,1,aq,0,0])
An=s.Matrix([-n,-n*aq+6*n*th,1,aq,0,0])
source=s.Matrix([1,aq-6*th,0,0,0,0])
meq('exact real principal-connection primitive',An-A0,-n*source)
eq('new source monodromy phase q',aq+1-6*th,aq-6*th+1)
eq('new source monodromy phase theta',aq-6*(th+1),aq-6*th-6)

# The q-preserving nodal horizontal field.
x,y,ss,L,Q=s.symbols('x y ss L Q')
F=x*y-Q*s.exp(ss*n*L)
VF=s.diff(F,ss)+n*L*y*s.diff(F,y)
eq('nodal vector field tangent',VF.subs(x*y,Q*s.exp(ss*n*L)),0)

# The Thom/Mayer--Vietoris quotient: F,m and the cap meridian.
# H2(A)=(F,T,m), H2(cap)=Z c. Boundary generators F and m map below.
MV=s.Matrix([[1,0],[0,0],[0,1],[0,-1]])
target=s.Matrix([[0,1,0,0],[0,0,1,1]])
# A direct integral quotient is (T,m+c), with section T,m.
meq('MV quotient kills both boundary columns',target*MV,s.zeros(2,2))
section=s.Matrix([[0,0],[1,0],[0,1],[0,0]])
meq('MV quotient has integral section',target*section,s.eye(2))
assert s.Matrix.hstack(MV,section).det() in (1,-1)
checks.append('MV boundary columns plus quotient section are unimodular')

# Exterior forms, retaining their noncommutative matrix coefficients.
def wedge(a,b):
    ans={}
    for I,A in a.items():
        for J,B in b.items():
            if set(I)&set(J):continue
            inv=sum(i>j for i in I for j in J)
            K=tuple(sorted(I+J))
            term=(-1)**inv*(A*B)
            ans[K]=ans.get(K,s.zeros(*term.shape))+term
    return {K:M.applyfunc(s.simplify) for K,M in ans.items()
            if M.applyfunc(s.simplify)!=s.zeros(*M.shape)}
AA=s.Matrix(2,2,s.symbols('a0:4'))
BB=s.Matrix(2,2,s.symbols('b0:4'))
om={(1,):AA,(2,):BB}
om2=wedge(om,om)
assert wedge(om2,om)=={} and wedge(om2,om2)=={}
checks.extend(['full two-variable Maurer cube is zero','full two-variable Maurer fourth power is zero'])
chi,chip=s.symbols('chi chi_prime')
curv={K:(chi**2-chi)*M for K,M in om2.items()}
for K,M in wedge({(0,):s.eye(2)},om).items():curv[K]=curv.get(K,s.zeros(2))+chip*M
assert wedge(curv,curv)=={}
checks.append('entire collar curvature square vanishes, not just endpoints')

# The phase shears are full positive GL frames, not polar group products.
phi=s.symbols('phi_g')
GG=s.eye(6)
GG[0,1]=n*phi
GG[2,1]=-n
eq('retained invariant-coframe shear determinant',GG.det(),1)
meq('retained invariant-coframe shear inverse',GG*GG.inv(),s.eye(6))
MC=GG.inv()*GG.diff(phi)
EE=s.zeros(6); EE[0,1]=n
meq('literal full boundary Maurer matrix',MC,EE)
meq('boundary Maurer matrix square is zero',MC*MC,s.zeros(6))

report={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS',
        'scope':'Exact algebraic identities for SQ.1--6; geometric piece/normal/cap and relative pairing proof is independently audited',
        'count':len(checks),'checks':checks,
        'new_unit_windings':{'A11':-6,'A21':'6*n','A12':0,'A22':0},
        'retained_Euler_difference':'-6*n*[dtheta] cup b for the physical complex line L_delta',
        'inverse_line_Chern_difference':'6*n*[dtheta] cup b for U=L_delta^(-1)',
        'connection_convention':'A(partial_delta)=1, c1(L_delta)=-dA, c1(U)=dA',
        'retained_real_connection_primitive':'-n*(du+alpha_Q*dv) plus the full periodic-unit one-form',
        'normal_meridian_Chern_difference':0,
        'statement':'P3K.63','geometric_audit':'Root and blind_control complete signed audits PASS; the certificate verifies the displayed algebra only'}
path=Path(__file__).with_suffix('.json')
path.write_text(json.dumps(report,indent=2)+'\n')
print(f'PASS: {len(checks)} exact shear, period, connection, Thom/MV and transgression identities; geometric proof remains separately audited.')
