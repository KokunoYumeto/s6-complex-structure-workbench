"""Full cube and exceptional period maps, with all powers retained."""
from pathlib import Path
import sympy as S,json
P,R,Q,Z,x,w,t,eta,c,p,N,d,xi=S.symbols('P R Q Z x w t eta c p N d xi',nonzero=True)
checks=[]
def ck(n,e):
 assert S.factor(e)==0,(n,S.factor(e));checks.append(n)
ck('actual coefficient cube root period',P**2/(P*P*R)-R**(-1))
ck('actual coefficient cube root suspension',P*(eta*w/x)**2*x/(2*t*w/x)-P*eta**2*w/(2*t))
u=P*eta**2/(2*t);K=(P/t)**3*eta**6
ck('actual full scalar cube',K-8*u**3)
ck('period generator determinant',S.Matrix([[0,1],[-1,3]]).det()-1)
# Verify for arbitrary symbolic units and every admitted even N in a finite range.
for n in range(4,42,2):
 D=P**n*(p-1)**n*c
 b=(p-1)**(-n)/c
 a=p**(n-3)*(p-1)**(3*n)*c**3
 ck('H1 actual line '+str(n),P**n/D-b)
 ck('H2 actual line '+str(n),p**n*(p*P)**(-3)*D**3-P**(3*(n-1))*a)
 ck('retained unit norm '+str(n),a*b**3-p**(n-3))
 ck('exceptional determinant '+str(n),S.Matrix([[3,-1],[-3,n]]).det()-3*(n-1))
ck('P-face primitive source kernel',(S.Matrix([[2,-1]])*S.Matrix([1,2]))[0])
out={'status':'PASS','count':len(checks),'checks':checks,'scope':'actual open exceptional atlas, full cube and period maps; its three ends and full compact strip are unfilled.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
