"""Exact nineteen-chart graph maps for UV=x^9 y^9 p."""
from pathlib import Path
import sympy as S,json
a,b,x,y,p,beta,d=S.symbols('a b x y p beta d',nonzero=True)
checks=[]
def ck(n,e):
    e=S.factor(e)
    assert e==0,(n,e)
    checks.append(n)
for k in range(9):
    xx=a*b;U=xx**k*a;V=xx**(8-k)*y**9*p*b
    ck('x product '+str(k),U*V-xx**9*y**9*p)
    F=S.Matrix([xx,y,p,U]);vars=S.Matrix([a,b,y,p])
    ck('x canonical volume '+str(k),F.jacobian(vars).det()/U+1)
    w=[k+1,-k-2,1,0]
    ck('x weight sum '+str(k),sum(w))
    for label,g in [('H1',beta),('K',d**-1)]:
        aa=g**w[0]*a;bb=g**w[1]*b;yy=g*y
        ck(label+' x source '+str(k),aa*bb-g**-1*xx)
        ck(label+' x U '+str(k),(aa*bb)**k*aa-g*U)
        ck(label+' x V '+str(k),(aa*bb)**(8-k)*yy**9*p*bb-g**-1*V)
    xp=1/y;yp=xx*y**2
    ap=y**(9-2*k)*a;bp=y**(2*k-7)*b
    ck('source overlap y prime '+str(k),ap*bp-yp)
    ck('source overlap U '+str(k),xp**9*yp**k*ap-U)
    ck('source overlap V '+str(k),yp**(8-k)*p*bp-V)
for k in range(9):
    yy=a*b;U=x**9*yy**k*a;V=yy**(8-k)*p*b
    ck('y product '+str(k),U*V-x**9*yy**9*p)
    F=S.Matrix([x,yy,p,U]);vars=S.Matrix([x,a,b,p])
    ck('y canonical volume '+str(k),F.jacobian(vars).det()/U-1)
    w=[-1,10-k,k-9,0]
    ck('y weight sum '+str(k),sum(w))
    for label,g in [('H1',beta),('K',d**-1)]:
        xx=g**-1*x;aa=g**w[1]*a;bb=g**w[2]*b
        ck(label+' y source '+str(k),aa*bb-g*yy)
        ck(label+' y U '+str(k),xx**9*(aa*bb)**k*aa-g*U)
        ck(label+' y V '+str(k),(aa*bb)**(8-k)*p*bb-g**-1*V)
pp=a*b;U=x**9*y**9*a;V=b
ck('last product',U*V-x**9*y**9*pp)
F=S.Matrix([x,y,pp,U]);vars=S.Matrix([x,y,a,b])
ck('last canonical volume',F.jacobian(vars).det()/U+1)
ck('last weight sum',-1+1+1-1)
for label,g in [('H1',beta),('K',d**-1)]:
    xx=g**-1*x;yy=g*y;aa=g*a;bb=g**-1*b
    ck(label+' last base',aa*bb-pp)
    ck(label+' last U',xx**9*yy**9*aa-g*U)
    ck(label+' last V',bb-g**-1*V)
out={'status':'PASS','count':len(checks),'checks':checks,
 'scope':'Proper local nineteen-chart resolution, canonical form, actual full-unit period lifts and source-chain overlaps. No global corner gluing, face count, characteristic pair or return.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
