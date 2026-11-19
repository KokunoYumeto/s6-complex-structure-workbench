"""Ten exact graph charts and both full periods at p=1."""
from pathlib import Path
import sympy as S,json
x,y,a,b,v,p,c,P=S.symbols('x y a b v p c P',nonzero=True)
checks=[]
def ck(n,e):
    e=S.factor(e);assert e==0,(n,e);checks.append(n)
ck('full H2 source',(P**3*p)*P**-3-p)
ck('full H2 line',p**-2*(P**3*v**4*c)**3-P**9*p**-2*v**12*c**3)
ck('period index',S.Matrix([[3,-1],[0,1]]).det()-3)
for k in range(3):
    xx=a*b;U=xx**k*a;V=xx**(2-k)*y**3*v**4*b
    ck('x chart product '+str(k),U*V-xx**3*y**3*v**4)
    ck('x chart volume '+str(k),S.Matrix([xx,y,v,U]).jacobian([a,b,y,v]).det()/U+1)
    aa=p**(-k-2)*a;bb=p**(k+3)*b;yy=p**-1*y
    ck('h x source '+str(k),aa*bb-p*xx)
    ck('h x U '+str(k),(aa*bb)**k*aa-p**-2*U)
    ck('h x V '+str(k),(aa*bb)**(2-k)*yy**3*v**4*bb-p**2*V)
    ck('B x U '+str(k),(c*a*c**-1*b)**k*(c*a)-c*U)
    ck('B x V '+str(k),(c*a*c**-1*b)**(2-k)*y**3*v**4*c**-1*b-c**-1*V)
    xp=y**-1;yp=xx*y**2;ap=y**(3-2*k)*a;bp=y**(2*k-1)*b
    ck('source overlap node '+str(k),ap*bp-yp)
    ck('source overlap U '+str(k),xp**3*yp**k*ap-U)
    ck('source overlap V '+str(k),yp**(2-k)*v**4*bp-V)
for k in range(3):
    yy=a*b;U=x**3*yy**k*a;V=yy**(2-k)*v**4*b
    ck('y chart product '+str(k),U*V-x**3*yy**3*v**4)
    ck('y chart volume '+str(k),S.Matrix([x,yy,v,U]).jacobian([x,a,b,v]).det()/U-1)
    xx=p*x;aa=p**(k-5)*a;bb=p**(4-k)*b
    ck('h y source '+str(k),aa*bb-p**-1*yy)
    ck('h y U '+str(k),xx**3*(aa*bb)**k*aa-p**-2*U)
    ck('h y V '+str(k),(aa*bb)**(2-k)*v**4*bb-p**2*V)
    ck('B y U '+str(k),x**3*(c*a*c**-1*b)**k*c*a-c*U)
    ck('B y V '+str(k),(c*a*c**-1*b)**(2-k)*v**4*c**-1*b-c**-1*V)
for k in range(4):
    vv=a*b;U=x**3*y**3*vv**k*a;V=vv**(3-k)*b
    ck('v chart product '+str(k),U*V-x**3*y**3*vv**4)
    ck('v chart volume '+str(k),S.Matrix([x,y,vv,U]).jacobian([x,y,a,b]).det()/U+1)
    xx=p*x;yy=p**-1*y;aa=p**-2*a;bb=p**2*b
    ck('h v base '+str(k),aa*bb-vv)
    ck('h v U '+str(k),xx**3*yy**3*(aa*bb)**k*aa-p**-2*U)
    ck('h v V '+str(k),(aa*bb)**(3-k)*bb-p**2*V)
    ck('B v U '+str(k),x**3*y**3*(c*a*c**-1*b)**k*c*a-c*U)
    ck('B v V '+str(k),(c*a*c**-1*b)**(3-k)*c**-1*b-c**-1*V)
for i in range(3):
    ck('actual source node '+str(i),P**i*x*P**(2-i)*p*y-P**2*p*x*y)
out={'status':'PASS','count':len(checks),'checks':checks,
     'scope':'Ten smooth local graph charts, actual h/B index and unit maps, source overlaps and canonical factors. No global component count or return.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
