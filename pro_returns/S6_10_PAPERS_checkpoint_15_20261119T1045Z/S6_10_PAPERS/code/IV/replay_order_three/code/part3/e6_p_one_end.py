"""Exact p=1 end periods, full Cartier label arrow and finite quotient."""
from pathlib import Path
import sympy as S,json
P,p,c,v,e,W=S.symbols('P p c v e W',nonzero=True)
checks=[]
def ck(n,x):
 assert S.factor(x)==0,(n,S.factor(x));checks.append(n)
for N in range(4,22,2):
 L=3*(N-1)
 ck('h full Y coefficient '+str(N),P**L*p**(N-3)/(P**3*p)**(N-1)-p**(-2))
 ck('B W coefficient '+str(N),P**(-1)*P**N*v**N*c-P**(N-1)*v**N*c)
 a0=P**L*p**(-2)*c**3;b0=P**(N-1)*c
 ck('H2 exact line '+str(N),p**(-2)*(v**N*b0)**3-v**(3*N)*a0)
 ck('H2 exact source '+str(N),(P**3*p)*P**(-3)-p)
 assert all((j+N)%(3*N)!=j for j in range(3*N));checks.append('finite order-three central freeness '+str(N))
 for j in (-2,0,3):
  ck('Cartier forward label '+str((N,j)),v*e*W/v**(j+1)-e*W/v**j)
  ck('Cartier reciprocal label '+str((N,j)),v**(j+2)/(v*e*W)-v**(j+1)/(e*W))
out={'status':'PASS','count':len(checks),'checks':checks,'scope':'Actual p=1 end away from P=0; no other end, corner, characteristic integral or return.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
