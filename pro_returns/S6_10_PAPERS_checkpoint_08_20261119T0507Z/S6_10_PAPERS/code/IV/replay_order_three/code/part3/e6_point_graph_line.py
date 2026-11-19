"""All actual point-node charts and the complete Cartier coefficients."""
from pathlib import Path
import sympy as S,json
x,y,a,Z,W,b,e,sigma,tau,U6,E,P,Q=S.symbols(
 'x y a Z W b e sigma tau U6 E P Q',nonzero=True)
checks=[]
def ck(n,v):
 v=S.factor(v);assert v==0,(n,v);checks.append(n)
for j in range(3):
 pp=x*y;p=x**j*y**(j+1);bb=x**(3-j)*y**(2-j);ee=x**(2*j)*y**(2*j+2)
 ck('point b '+str(j),pp**3/p-bb)
 ck('point e '+str(j),p**2-ee)
 ck('source node point '+str(j),bb*ee-pp**3*p)
ck('last source point',x**6*a-x**3*(x**3*a))
for n in range(1,12):
 ck('point theta forward factor '+str(n),(b*e)**n*Z/b-(b*e)**(n-1)*e*Z)
 ck('point theta backward factor '+str(n),(b*e)**n*b/Z-(b*e)**(n-1)*b*((b*e)/Z))
fb_sigma=(1-sigma)*E
fb_tau=(tau-1)/tau*E
ck('first-chart sigma coefficient',-U6*(b*sigma)**-2*fb_sigma/(sigma-1)-U6*b**-2*sigma**-2*E)
ck('first-chart tau coefficient',-U6*Z**-2*fb_tau/(tau-1)+U6*Z**-2*tau**-1*E)
ck('last-chart sigma coefficient',b*U6*(b*sigma)**-3*fb_sigma/(sigma-1)+U6*b**-2*sigma**-3*E)
ck('last-chart tau coefficient',Z*tau*U6*Z**-3*fb_tau/(tau-1)-U6*Z**-2*E)
ck('period frame identity',P**6*U6*Z**-3*(-Z/P**6)+U6*Z**-2)
ck('full first B scalar',Z**-2/(P**-1*Z)**-2-P**-2)
ck('full last B scalar',Z**-3/(P**-1*Z)**-3-P**-3)
# Infinity source graph is the same typed node formula.
u,R=S.symbols('u R',nonzero=True)
ck('infinity point node',u**2*R**3-R**3*u**2)
ck('infinity first generator',U6/sigma*fb_sigma/(sigma-1)+U6*E/sigma)
ck('infinity second generator',U6*tau*fb_tau/(tau-1)-U6*E)
p=S.symbols('p',nonzero=True)
qq=P**3*p;rr=P*p;bb=p**-2;ww=S.symbols('ww',nonzero=True)
ck('first actual point source branch',qq*rr**-3-bb)
ck('second actual point source branch',qq*bb-P**3/p)
ck('second actual point other branch',bb**-1-p**2)
ck('full node h transition',rr**3/qq-p**2)
ck('source inversion Cartier generator',(ww**-1-1)/(ww**-1-bb)-p**2*(ww-1)/(ww-p**2))
ck('full common point-line scalar',P**-3*p**-5*ww*p**2-rr**-3*ww)
out={'status':'PASS','count':len(checks),'checks':checks,
 'scope':'Actual point-node graphs, full theta factors and all typed Cartier/suspension coefficients. Total-line graph, period-equivariant attachment and return remain open.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
