#!/usr/bin/env python3
"""Fresh exact checks of the regular-chart attempt, not a global atlas.

GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort; same-family.
No historical executable is imported. SymPy exact algebra only.
"""
from pathlib import Path
import datetime
import hashlib
import json
import platform
import time

import sympy as s

START=time.monotonic()
checks=[]

def scalar_zero(x):
    return s.cancel(s.expand(x)) == 0

def check(name, expression):
    if isinstance(expression, s.MatrixBase):
        ok=all(scalar_zero(x) for x in expression)
    else:
        ok=scalar_zero(expression)
    checks.append({'name':name,'passed':bool(ok)})
    if not ok:
        raise AssertionError((name,expression))

I=s.I
yr,mr,br,y,m,r=s.symbols('tau_R mu_R beta_R y m r',real=True)
TR=s.Matrix([[yr,6*mr],[mr,br]])
Y=s.Matrix([[y,6*m],[m,r]])
T=TR+I*Y
Tb=TR-I*Y
D=s.diag(1,6)
S=D*Y.inv()
check('weighted holomorphic period symmetry',D*T-T.T*D)
check('weighted imaginary period symmetry',D*Y-Y.T*D)
check('S symmetry',S-S.T)
check('S explicit entries',S-s.Matrix([[r,-6*m],[-6*m,6*y]])/(y*r-6*m*m))

q1,q2,p1,p2=s.symbols('q1 q2 p1 p2',real=True)
q=s.Matrix([q1,q2]);p=s.Matrix([p1,p2])
z=p+T*q;zb=p+Tb*q
check('exact Betti inverse q',Y.inv()*(z-zb)/(2*I)-q)
check('exact Betti inverse p',(z+zb)/2-TR*Y.inv()*(z-zb)/(2*I)-p)

# Independent full alternating-matrix pullback, ordered (p1,p2,q1,q2).
J=s.eye(2).row_join(T).col_join(s.eye(2).row_join(Tb))
Fz=s.zeros(4)
Fz[:2,2:]=-I*S/2
Fz[2:,:2]=I*S/2
Fpq=s.zeros(4);Fpq[:2,2:]=-D;Fpq[2:,:2]=D
check('full complex-coordinate form equals flat Betti eta',J.T*Fz*J-Fpq)

# Original coordinate order r_gamma,r_u,r_w,r_delta.
E=s.Matrix([[0,0,0,6],[0,0,1,0],[0,-1,0,0],[-6,0,0,0]])
P=s.Matrix([[0,0,1,0],[0,0,0,1],[0,1,0,0],[1,0,0,0]])
check('exact original marking pullback',P.T*Fpq*P-E)
A1=s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
for name,A,order,v in [('finite_three',A1,3,s.Matrix([1,2,-4,0])),
                        ('finite_four',A2,4,s.Matrix([-1,-3,3,0]))]:
    check(name+' preserves eta',A.T*E*A-E)
    check(name+' finite order',A**order-s.eye(4))
    check(name+' fixes actual affine vector',A*v-v)
A0=(A1*A2).inv();N=A0-s.eye(4)
check('cusp nilpotent square',N*N)
check('cusp preserves eta',A0.T*E*A0-E)

# Exact theta invariance retains differential of the moving periods.
ta,mu,be=s.symbols('tau_prime mu_prime beta_prime')
K=s.Matrix([[ta,6*mu],[mu,be]])
n1,n2,a1,a2,np1,np2,ap1,ap2=s.symbols('n1 n2 a1 a2 np1 np2 ap1 ap2',integer=True)
n=s.Matrix([n1,n2]);a=s.Matrix([a1,a2])
np=s.Matrix([np1,np2]);ap=s.Matrix([ap1,ap2])
theta=s.Matrix(s.symbols('theta1 theta2'))
check('full lattice theta invariance',theta+K*n-K*(q+n)+K*q-theta)

# A direct polynomial check of both automorphy and metric logarithms.
zz=s.Matrix(s.symbols('zeta1 zeta2'))
def logarithm(bb,ww):
    return (bb.T*D*ww)[0]+(bb.T*D*T*bb)[0]/2
defect=logarithm(n,zz+ap+T*np)+logarithm(np,zz)-logarithm(n+np,zz)
check('automorphy logarithm defect is integral n.D.ap',defect-(n.T*D*ap)[0])
phi=(q.T*D*Y*q)[0]
check('metric logarithm variation',((q+n).T*D*Y*(q+n))[0]-phi-
      (2*n.T*D*Y*q+n.T*D*Y*n)[0])

# Mixed Hessian by literal differentiation on independently chosen exact jets.
# Each case is a full six-coordinate rational calculation with the base
# derivative present. The universal identity is also derived in NEW_ROUTE.md.
t,tb,z1,z2,bz1,bz2=s.symbols('t tb z1 z2 bz1 bz2')
coords=[t,z1,z2];bcoords=[tb,bz1,bz2]
jet_cases=[
    ((0,0,0,2,0,-3),(1,2,3),(2,-1,1)),
    ((1,-1,2,3,1,-4),(-2,1,3),(1,2,-2)),
    ((-2,2,1,4,-1,-3),(3,-2,1),(-1,1,2)),
    ((2,1,-3,5,2,-5),(1,1,-2),(3,2,1)),
]
for no,(base,kre,kim) in enumerate(jet_cases,1):
    subs=dict(zip([yr,mr,br,y,m,r],map(s.Integer,base)))
    T0=T.subs(subs);Tb0=Tb.subs(subs)
    Kj=s.Matrix([[kre[0]+I*kim[0],6*(kre[1]+I*kim[1])],
                 [kre[1]+I*kim[1],kre[2]+I*kim[2]]])
    Kbj=s.conjugate(Kj)
    Tj=T0+t*Kj;Tbj=Tb0+tb*Kbj
    Yj=(Tj-Tbj)/(2*I)
    vj=s.Matrix([z1-bz1,z2-bz2])/(2*I)
    phij=(vj.T*D*Yj.inv()*vj)[0] # phi/(2pi)
    at={t:0,tb:0,z1:s.Rational(2,3)+I/5,z2:-s.Rational(1,4)+2*I/7,
        bz1:s.Rational(2,3)-I/5,bz2:-s.Rational(1,4)-2*I/7}
    qj=(Yj.inv()*vj).subs(at)
    Pj=(-Kj*qj).row_join(s.eye(2))
    Pbj=(-Kbj*qj).row_join(s.eye(2))
    expected=Pj.T*(D*Yj.inv()).subs(at)*Pbj/2
    H=s.Matrix(3,3,lambda aa,bb:s.diff(phij,coords[aa],bcoords[bb]).subs(at))
    check(f'literal full mixed Hessian exact jet {no}',H-expected)

# Exact leading rational cusp expression; no discarded period unit is
# assumed zero in the asymptotic proof.
L,c_y,c_r,c_m=s.symbols('L c_y c_r c_m',real=True)
S11=(-L+c_r)/((L+c_y)*(-L+c_r)-6*c_m*c_m)
check('cusp leading coefficient lim L*S11 = 1',s.limit(L*S11,L,s.oo)-1)
z0,z1c,z2c,eps=s.symbols('z0 z1c z2c epsilon',positive=True)
qbase=z0*z1c*z2c
check('exact fixed-q tangent along equal-coordinate cusp path',
      (s.diff(qbase,z1c)-s.diff(qbase,z0)).subs({z0:eps,z1c:eps,z2c:eps}))

output={'checker':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort; same family',
        'phase':'S6_SERIES_GRIND','timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'purpose':'Exact bounded certificate for a new regular coefficient-atlas attempt; inv:C3.8 remains open.',
        'python':platform.python_version(),'sympy':s.__version__,
        'checks':checks,'check_count':len(checks),'result':'PASS',
        'elapsed_seconds':time.monotonic()-START,
        'limitations':['No cusp correction cochain constructed.',
                       'No global Hermitian Green operator evaluated.',
                       'The four full Hessian jet checks supplement, rather than replace, the universal written identity.',
                       'No period-exclusion or global-atlas proof claimed.']}
folder=Path(__file__).resolve().parent
out=folder/'exact_regular_atlas.output.json'
out.write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({'result':output['result'],'check_count':len(checks),
                  'elapsed_seconds':output['elapsed_seconds'],'output':str(out),
                  'sha256':hashlib.sha256(out.read_bytes()).hexdigest()},indent=2))
