"""Typed forward/inverse parameter squares and full selected Cox maps."""
from pathlib import Path
import json
import sympy as S

z,c,P,lam,beta,r,A,B,x0,x1,x2,y0,y1,y2,a,b=S.symbols(
    'z c P lam beta r A B x0 x1 x2 y0 y1 y2 a b',nonzero=True)
h=1-c*z
q=h/z
checks=[]
def ck(name,expr):
    val=S.factor(expr)
    assert val==0,(name,val)
    checks.append(name)

ev=S.Matrix([[1,0,0,-2,0]])
va,vb,vd=S.symbols('va vb vd')
ck('full norm meridian evaluation',(ev*S.Matrix([2,va,vb,1,vd]))[0])
ck('contracting B evaluation',-ev[3]-2)
for j in range(-6,7):
    ck('forward square '+str(j),z**j*q**j-h**j)
    ck('inverse closing '+str(j),q**(-j)-h**(-j)*z**j)
    ck('selected source reindex '+str(j),P**(-j)*P**j-1)
    ck('selected line reindex '+str(j),(lam*q*beta)**j*lam**(-j)*beta**(-j)-q**j)
for J0 in range(-3,4):
    for J1 in range(-3,4):
        for k in (-1,1):
            ck('restored sector '+str((J0,J1,k)),
               r**k*(r**2*B)**J1*A**k
               -(r*A)**k*(r**2*B)**(J1-J0)*(r**2*B)**J0)
plus=[x0/(a*b),a*x1,b*x2]
minus=[a*b*y0,y1/b,y2/a]
ck('plus q',S.prod(plus)-x0*x1*x2)
ck('plus Z',plus[1]-a*x1)
ck('plus V',plus[2]-b*x2)
ck('minus q',S.prod(minus)-y0*y1*y2)
ck('minus Z',minus[0]*minus[1]-a*y0*y1)
ck('minus V',minus[0]*minus[2]-b*y0*y2)

out={'status':'PASS','count':len(checks),'checks':checks,
     'scope':'E87 full marked parameter-square identities; no central coupled filling or return value.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
