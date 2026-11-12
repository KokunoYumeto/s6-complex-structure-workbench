"""Exact independent checks for the invariant-sector continuation; no numerics."""
from pathlib import Path
import json
import sympy as S

I=S.I
u=S.ones(3,1)
v=S.Matrix([1,-1,0]); w=S.Matrix([1,1,-2])
rows=[]
def check(name,expr):
    items=list(expr) if isinstance(expr,S.MatrixBase) else [expr]
    assert all(S.expand(x)==0 for x in items), name
    rows.append({'check':name,'result':'PASS'})

def herm(prefix):
    x=S.symbols(prefix+'0:8',real=True)
    return S.Matrix([[x[0],x[2]+I*x[3],x[4]+I*x[5]],
        [x[2]-I*x[3],x[1],x[6]+I*x[7]],
        [x[4]-I*x[5],x[6]-I*x[7],-x[0]-x[1]]])
Phi=herm('p'); V=herm('v')
br=S.symbols('b0:6',real=True); cr=S.symbols('c0:6',real=True)
b=S.Matrix([br[2*j]+I*br[2*j+1] for j in range(3)])
bd=S.Matrix([cr[2*j]+I*cr[2*j+1] for j in range(3)])
t=S.trace(Phi**2); n=(b.H*b)[0]; s=t+2*n
adj=Phi.adjugate(); T=adj-b*b.H; T0=T-S.trace(T)*S.eye(3)/3
check('adjugate of full eight-variable Hermitian matrix',adj-Phi**2+t*S.eye(3)/2)
check('exact vector cancellation with original s',T0*b-Phi**2*b+s*b/3)
a,k=S.symbols('a k',real=True)
PhiDD=-a*Phi+k*T0; bDD=-a*b-k*Phi*b
rho=(u.H*b)[0]; c=(u.H*Phi*b)[0]; h=(u.H*V*bd)[0]
cDD=(u.H*(PhiDD*b+2*V*bd+Phi*bDD))[0]
check('full c second derivative identity',cDD+2*a*c+k*s*rho/3-2*h)
E=v*v.H/2; F=w*w.H/6
Phi0=E-F+w*u.H+u*w.H
check('sector projection idempotent',E**2-E)
check('sector Hermitian commutation',Phi0*E-E*Phi0)
check('sector trace',S.trace(Phi0))
check('nonzero Phi b',Phi0*v-v)
check('retained norm t=38',S.trace(Phi0**2)-38)
check('retained scalar s=42',S.trace(Phi0**2)+2*(v.H*v)[0]-42)
P=S.Matrix([[1,-1,0],[0,1,-1]]); R=P.H*(P*P.H).inv()
check('original marked chi',R.H*v-S.Matrix([1,0]))
check('original marked nonzero z',P*Phi0*u/3-S.Matrix([0,3]))
check('original marked lambda',(u.H*Phi0*u)[0]/9)
H=(u*w.H+w*u.H)/3
check('fourth jet: trace',S.trace(H))
check('fourth jet: initial rho',(u.H*v)[0])
check('fourth jet: initial rho prime',(u.H*w)[0])
check('fourth jet: c prime',(u.H*H*v)[0])
check('fourth jet: h=6',(u.H*H*w)[0]-6)
check('fourth jet: derivative=-12k',-2*k*(u.H*H*w)[0]+12*k)
for r,dim in [(1,6),(2,8)]:
    check(f'configuration dimension r={r}',r*r+(3-r)**2-1+2*r-dim)

if __name__=='__main__':
    out=Path(__file__).with_name('invariant_sector_results.json')
    out.write_text(json.dumps({'all_passed':True,'checks':rows},indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'all_passed':True,'checks':len(rows),'output':str(out)}))
