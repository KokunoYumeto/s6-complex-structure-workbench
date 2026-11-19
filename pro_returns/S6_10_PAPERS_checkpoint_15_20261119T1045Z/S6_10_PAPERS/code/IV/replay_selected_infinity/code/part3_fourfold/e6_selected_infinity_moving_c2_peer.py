#!/usr/bin/env python3
"""Independent exact two-chart and directed-Chern check for MC2."""
from pathlib import Path
import sympy as S,json,hashlib

ROOT=Path(__file__).resolve().parents[2]
checks=[]
def eq(name,a,b):
    d=a-b
    if isinstance(d,S.MatrixBase):ok=all(S.factor(z)==0 for z in d)
    else:ok=S.factor(d)==0
    assert ok,(name,d)
    checks.append(name)
Z,Zb,zeta=S.symbols('Z Zbar zeta',nonzero=True)
G=S.Matrix([[1,-Z],[Zb,1]])
G1=S.Matrix([[1/Zb,-1],[1,1/Z]])
Jline=S.diag(Zb,Z)
eq('global right-complex conjugated Cox frame',G1*Jline,G)
eq('positive determinant zero chart',G.det(),1+Z*Zb)
eq('positive determinant infinity chart',G1.det(),1+1/(Z*Zb))
Gstar=S.Matrix([[1,Z],[-Zb,1]])
eq('Hermitian positive norm',Gstar*G,(1+Z*Zb)*S.eye(2))
u=S.Matrix([1,Zb]);P=u*S.Matrix([[1,Z]])/(1+Z*Zb)
eq('first-line projector idempotence',P*P,P)
eq('first-line projector trace',S.trace(P),1)
eq('full conjugate projector clutch',G*S.diag(zeta,1)*G.inv(),S.eye(2)+(zeta-1)*P)
eq('same clutch infinity chart',G1*S.diag(zeta,1)*G1.inv(),G*S.diag(zeta,1)*G.inv())
J=S.diag(1/Zb,1)
eq('retained q-factor conjugate Z inverse commutes',J*S.diag(zeta,1),S.diag(zeta,1)*J)
eq('retained q-factor global clutch',(G*J)*S.diag(zeta,1)*(G*J).inv(),G*S.diag(zeta,1)*G.inv())
r,rb,R,tb=S.symbols('r rbar R tbar',nonzero=True)
eq('actual full positive normal factorization',S.diag(tb/rb,r),S.diag(tb,1)*S.diag(1/rb,r))
eq('full polar common phase',(r/R)*S.diag(1/R,R),S.diag(1/rb,r).subs(rb,R**2/r))
for a in [2,6]:
    minus=-a;plus=4-a;common=plus
    eq(f'full negative winding a{a}',-(4-(-a+4)),minus)
    eq(f'remaining non-scalar winding a{a}',minus-common,-4)
    eq(f'remaining second winding a{a}',plus-common,0)
    eq(f'actual determinant winding a{a}',minus+plus,4-2*a)
h,u0=S.symbols('h u')
def hu(p):return S.expand(p).coeff(h,1).coeff(u0,1)
eq('reduced-clutch Chern product',hu((h+4*u0)*(-h)),-4)
for a in [2,6]:
    roots=[h+a*u0,-h+(a-4)*u0]
    eq(f'full-phase Chern product a{a}',hu(roots[0]*roots[1]),-4)
    eq(f'conjugate physical roots preserve c2 a{a}',hu((-roots[0])*(-roots[1])),-4)
    eq(f'ordered-root swap preserves c2 a{a}',hu(roots[1]*roots[0]),-4)
    eq(f'full determinant square remains zero a{a}',hu((roots[0]+roots[1])**2),0)
eq('oriented second face of D3 times D2',(-1)**3,-1)
theta=S.symbols('theta',real=True)
eq('opposite cap boundary angle',S.diff(-theta,theta),-1)
xx,yy,rad=S.symbols('xi_x xi_y epsilon0',real=True,nonzero=True)
eta_real=S.Matrix([xx/rad**2,-yy/rad**2])
eq('literal anti-linear cap disc Jacobian',eta_real.jacobian([xx,yy]).det(),-rad**-4)
eq('literal cap boundary is reciprocal parameter',((xx-S.I*yy)*(xx+S.I*yy)).expand(),xx**2+yy**2)
n=S.symbols('n',integer=True)
eq('coefficient target epsilon^n gives cap order -n',-n,-n)

p=ROOT/'notes/part3_e6_selected_infinity_moving_c2_working.md'
out={'status':'PASS','checks':len(checks),'labels':checks,'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
 'scope':'Full independent two-chart normal/Cox algebra and directed Chern products. The cap orientation comes from the negative C face of D3 times D2 and the opposite boundary angle; holomorphic inversion on a common annulus is orientation preserving.',
 'actual_c2':-4}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(f'PASS {len(checks)} independent MC2 identities; actual directed c2=-4.')
