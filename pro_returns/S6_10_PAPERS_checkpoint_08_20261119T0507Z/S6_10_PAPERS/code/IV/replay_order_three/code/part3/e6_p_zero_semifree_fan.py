"""An alternative actual p=0 toric resolution with semifree chart weights."""
from pathlib import Path
from itertools import combinations
import sympy as S,json
checks=[]
def ck(n,x):
 x=S.factor(x);assert x==0,(n,x);checks.append(n)
A=(0,0,0,1);B=(0,-1,0,1)
tri=[]
for k in range(-9,0):
 tri += [((-1,k),(0,k),(-1,k+1)),((0,k),(-1,k+1),(0,k+1))]
cones=[(A,)+tuple((x,y,1,0) for x,y in T) for T in tri]
cones.append((A,B,(-1,-9,1,0),(0,-9,1,0)))
data=[]
nodechars=[S.Matrix([1,0,1,0]),S.Matrix([-1,0,0,0]),
           S.Matrix([0,1,9,1]),S.Matrix([0,-1,0,0])]
for i,cs in enumerate(cones):
 N=S.Matrix.hstack(*map(S.Matrix,cs));det=N.det()
 assert abs(det)==1;checks.append('unimodular '+str(i))
 wt=list(map(int,N.inv()*S.Matrix([-1,1,0,0])))
 ck('physical total weight '+str(i),sum(wt))
 assert sorted(wt)==([-1,0,0,1] if i<18 else [-1,-1,1,1])
 checks.append('semifree local weights '+str(i))
 exps=[]
 for m in nodechars:
  row=list(map(int,(m.T*N)));assert min(row)>=0;exps.append(row)
 checks.append('actual original binomial characters '+str(i))
 data.append({'rays':cs,'det':int(det),'physical_weights':wt,
              'dual_characters':[[int(t) for t in row] for row in N.inv().tolist()],
              'original_node_character_exponents':exps})
def facets(row):
 ans=set()
 for cs in cones:
  for F in combinations(cs,3):
   if all(sum(a*b for a,b in zip(row,v))==0 for v in F):
    if S.Matrix.hstack(*map(S.Matrix,F)).rank()==3:ans.add(tuple(sorted(F)))
 return ans
TH=S.Matrix([[1,0,1,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
TK=S.Matrix([[1,0,0,0],[0,1,9,1],[0,0,1,0],[0,0,0,1]])
for n,target,source,T in [
 ('H1',(1,0,0,0),(1,0,1,0),TH),
 ('K0',(0,1,0,0),(0,1,9,1),TK)]:
 fs={tuple(sorted(tuple(map(int,T*S.Matrix(v))) for v in F)) for F in facets(source)}
 assert fs==facets(target);checks.append('exact periodic face '+n)
P,p,b,X,Y=S.symbols('P p b X Y',nonzero=True)
T=P**9*p;d0=b**-6
xx=P*X;yy=X**-1;UU=T*Y;VV=Y**-1
ck('literal source product',xx*yy-P)
ck('literal line product',UU*VV-P**9*p)
ck('literal original binomial',UU*VV-xx**9*yy**9*p)
ck('full translated X factor',P**-1*b*d0**-1-P**-1*b**7)
ck('full translated Y factor',T**-1*b**-1*d0-T**-1*b**-7)
ck('full source cell translate',P**-1*b**7*T**-1*b**-7-P**-10*p**-1)
ck('full line cell translate',(P**-1*b**7)**-4*(T**-1*b**-7)**-3-P**31*p**3*b**-7)
ck('literal B7 h inverse source',P**-7*(P**3*p)**-1-P**-10*p**-1)
ck('literal B7 h inverse line',(P**4/b)**7*(P*p)**3-P**31*p**3*b**-7)
ck('source coefficient in node frame',X*Y-(yy*VV)**-1)
ck('line coefficient in node frame',X**-4*Y**-3-yy**4*VV**3)
rr,tt=S.symbols('rr tt',nonnegative=True)
ck('finite source-height margin',4*(3*rr+tt)-(10*rr+tt)-(2*rr+3*tt))
Ainf=S.Matrix([[-4,-3],[1,1]])
assert Ainf*S.Matrix([-1,1])==S.Matrix([1,0]);checks.append('actual physical cocharacter map')
assert Ainf*S.Matrix([1,0])==S.Matrix([-4,1]);checks.append('first crossing row vector')
assert Ainf*S.Matrix([0,1])==S.Matrix([-3,1]);checks.append('second crossing row vector')
out={'status':'PASS','count':len(checks),'checks':checks,'upper_triangles':tri,'cones':data,
 'scope':'Alternative nineteen-cone proper local toric resolution with actual original-binomial map and full periods. No identification with other resolutions without their common graph; no global fixed count or return.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
