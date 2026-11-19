"""Exact N=4 period multiplication at the p=infinity exceptional end."""
from pathlib import Path
import json
import sympy as s
R,u,f=s.symbols('R u f',nonzero=True)
h=(u**2*R**3,R**-3);B=(u**-1*R**-1,R**4*f)
def multiply(a,b):return tuple(s.factor(x*y) for x,y in zip(a,b))
def power(a,n):return tuple(s.factor(x**n) for x in a)
def characters(a):return a[0],s.factor(a[0]**5/a[1])
K=multiply(h,power(B,2));L=multiply(power(h,-1),power(B,-3))
checks=[]
for name,actual,wanted in [('K ordinary',K,(R,R**5*f**2)),('L ordinary',L,(u,R**-9*f**-3)),('K characters',characters(K),(R,f**-2)),('L characters',characters(L),(u,R**9*u**5*f**3))]:
 for i,(a,b) in enumerate(zip(actual,wanted)):
  assert s.factor(a-b)==0;checks.append({'name':name,'coordinate':i,'actual':str(a),'expected':str(b),'pass':True})
C=s.Matrix([[1,0],[5,-1]]);J=s.Matrix([[1,-1],[2,-3]])
assert C.det()==-1 and J.det()==-1 and J.inv()==s.Matrix([[3,-1],[2,-1]])
assert C*C==s.eye(2)
for name,value in [('character_det',C.det()),('period_det',J.det()),('product_orientation',C.det()*J.det())]:checks.append({'name':name,'value':int(value),'pass':True})
out={'status':'PASS','exact_checks':len(checks),'scope':'N=4 actual h,B periods; p=infinity chart P=uR; full unit f=(1-u)^4 c retained. No compact corner or return assigned.','characters':[[int(x) for x in C.row(i)] for i in range(2)],'period_basis':[[int(x) for x in J.row(i)] for i in range(2)],'checks':checks}
p=Path(__file__).with_suffix('.json');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
