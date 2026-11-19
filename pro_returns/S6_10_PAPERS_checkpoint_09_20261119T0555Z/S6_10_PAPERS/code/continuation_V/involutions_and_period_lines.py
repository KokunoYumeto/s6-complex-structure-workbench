#!/usr/bin/env python3
"""Independent exhaustive F2 similarity, involution representatives, period lines.
No earlier verification program or representative table is read.
"""
from itertools import product
from pathlib import Path
import json
import sympy as S

def decode(a,n):
 return [[(a>>(i*n+j))&1 for j in range(n)] for i in range(n)]
def encode(a):
 n=len(a);return sum((a[i][j]&1)<<(i*n+j) for i in range(n) for j in range(n))
def mul(a,b):
 n=len(a);return [[sum(a[i][k]*b[k][j] for k in range(n))%2 for j in range(n)] for i in range(n)]
def inv(a):
 n=len(a);a=[r+[int(i==j) for j in range(n)] for i,r in enumerate(a)]
 for j in range(n):
  k=next((k for k in range(j,n) if a[k][j]),None)
  if k is None:return None
  a[j],a[k]=a[k],a[j]
  for i in range(n):
   if i!=j and a[i][j]:a[i]=[x^y for x,y in zip(a[i],a[j])]
 return [r[n:] for r in a]
counts=[];reps={};orbit_sizes={};binary_unit_dets={}
for n in range(4):
 mats={k:decode(k,n) for k in range(2**(n*n))}
 group=[(m,im) for m in mats.values() if (im:=inv(m)) is not None]
 remain=set(mats);rr=[];sizes=[]
 while remain:
  k=min(remain);orb={encode(mul(mul(g,mats[k]),ig)) for g,ig in group}
  assert orb<=remain
  remain-=orb;rr.append(k);sizes.append(len(orb))
 counts.append(len(rr));reps[n]=rr;orbit_sizes[n]=sizes
 binary_unit_dets[n]=sorted({int(S.Matrix(g).det()) if n else 1 for g,ig in group})
 assert binary_unit_dets[n] in ([1],[-1,1])
assert counts==[1,2,6,14]
N=S.zeros(6);N[:3,3:]=S.eye(3);allreps=[]
for c in [0,1]:
 for a in range(4-2*c):
  b=3-a-2*c
  p=S.diag(*([S.Integer(1)]*a+[-S.Integer(1)]*b+([S.Matrix([[0,1],[1,0]])] if c else [])))
  for ka,kb in product(reps[a],reps[b]):
   q=S.zeros(3)
   if a:q[:a,:a]=S.Matrix(decode(ka,a))
   if b:q[a:a+b,a:a+b]=S.Matrix(decode(kb,b))
   m1=p.row_join(q).col_join(S.zeros(3).row_join(-p))
   m2=m1*(S.eye(6)-N);m0=S.eye(6)+N
   assert m1*m1==m2*m2==S.eye(6)
   assert m0*m1*m2==S.eye(6)
   assert (m1-S.eye(6)).rank()==(m2-S.eye(6)).rank()==3
   allreps.append({'type':[a,b,c],'binary_similarity':[ka,kb],'M1':[list(map(int,m1.row(i))) for i in range(6)],'M2':[list(map(int,m2.row(i))) for i in range(6)]})
assert len(allreps)==56
Q=[]
for i in range(3):
 for j in range(3):
  if i!=j:
   m=S.zeros(3);m[i,j]=1;Q.append(m)
for i,j in [(0,1),(1,2)]:
 u=S.zeros(3,1);v=S.zeros(3,1);u[i]=u[j]=1;v[i]=1;v[j]=-1;Q.append(u*v.T)
Q.append(S.Matrix([[1,-1,0],[1,1,0],[0,0,0]]))
y=S.symbols('y',real=True)
line_dets=[S.factor((S.eye(3)+y*q).det()) for q in Q]
assert line_dets[:8]==[1]*8 and S.expand(line_dets[8]-(1+y)**2-y**2)==0
spanning=S.Matrix.hstack(*(S.Matrix(9,1,list(q)) for q in Q))
assert spanning.det()!=0
out={'F2_similarity_counts':counts,'F2_representatives':reps,'orbit_sizes':orbit_sizes,'binary_GL_lift_determinants':binary_unit_dets,'involution_count':len(allreps),'involution_representatives':allreps,'period_line_determinants':list(map(str,line_dets)),'period_line_spanning_determinant':str(spanning.det()),'status':'PASS'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='involution_representatives'},indent=2))
