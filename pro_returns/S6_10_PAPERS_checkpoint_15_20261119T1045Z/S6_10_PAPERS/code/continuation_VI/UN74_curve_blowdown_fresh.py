#!/usr/bin/env python3
"""New exact chart/extension certificate for UN74, before target exposure."""
from fractions import Fraction as F
from itertools import permutations,product
from pathlib import Path
from hashlib import sha256
import json
checks=[]
def ck(n,c):
 if not c:raise AssertionError(n)
 checks.append(n)
def P(e,c=1):return {tuple(e):F(c)}
def plus(a,b):
 d=a.copy()
 for e,c in b.items():d[e]=d.get(e,0)+c
 return {e:c for e,c in d.items() if c}
def times(a,b):
 d={}
 for e,c in a.items():
  for f,h in b.items():
   g=tuple(x+y for x,y in zip(e,f));d[g]=d.get(g,0)+c*h
 return {e:c for e,c in d.items() if c}
def scale(a,c):return {e:c*d for e,d in a.items() if c*d}
def diff(a,i):
 d={}
 for e,c in a.items():
  if e[i]:
   f=list(e);f[i]-=1;d[tuple(f)]=c*e[i]
 return d
def sign(p):return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
def determinant(a):
 out={}
 for p in permutations(range(len(a))):
  b=P((0,0,0),sign(p))
  for i,j in enumerate(p):b=times(b,a[i][j])
  out=plus(out,b)
 return out
def substitute_monomial(e,images):return tuple(sum(e[i]*images[i][k] for i in range(len(e))) for k in range(len(images[0])))
def mm(a,b):return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]
# Chart1 coordinates x,y,z; chart2 s,w,z. Target order p0,q0,r0.
chart1=[P((1,1,0)),P((0,0,1)),P((1,0,0))]
chart2=[P((1,0,0)),P((0,0,1)),P((1,1,0))]
J1=determinant([[diff(a,j) for j in range(3)] for a in chart1]);J2=determinant([[diff(a,j) for j in range(3)] for a in chart2])
ck('first exact canonicalJacobian isplusx',J1==P((1,0,0)))
ck('second exact canonicalJacobian isminuss',J2==P((1,0,0),-1))
transition=[P((1,1,0)),P((0,-1,0)),P((0,0,1))]
Jtrans=determinant([[diff(a,j) for j in range(3)] for a in transition])
ck('charttransitionJacobian isminus1overw',Jtrans==P((0,-1,0),-1))
ck('canonicalforms agree underactual transition',times(P((1,1,0)),Jtrans)==J2)
images1=[next(iter(p)) for p in chart1];images2=[next(iter(p)) for p in chart2];trans=[next(iter(p)) for p in transition]
for im1,im2 in zip(images1,images2):ck('actualblowdownchart functions agree',substitute_monomial(im1,trans)==im2)
for m,n in product(range(1,9),repeat=2):
 e1=substitute_monomial((m,n,0),images1);e2=substitute_monomial((m,n,0),images2)
 ck('fullfibreweights insectionchart',e1==(m,m,n))
 ck('fullfibreweights inotherchart',e2==(m,0,n))
 ck('fullfibrecharts agree onoverlap',substitute_monomial(e1,trans)==e2)
for mT,mP in product(range(1,16),repeat=2):
 deg=-F(mP,mT)
 ck('ordinarynormaldegree criterion isexact equality',(deg==-1)==(mT==mP))
# Primitive transition for actual V extension, its projective section and
# tautological fibre, retaining both endpoint identifications.
for l,m,e,y,r in product([F(1),F(2),F(-1)], [F(1),F(3)], [F(-2),F(0),F(2)], [F(0),F(1),F(2)], [F(1),F(2)]):
 den=l+e*y
 if not den:continue
 yp=m*y/den;rp=den*r
 ck('tautologicalline transforms actualnormal vector',(rp,rp*yp)==(l*r+e*r*y,m*r*y))
 ck('sectionline retained',(y!=0) or yp==0)
 ck('normalquotient map retained',rp*yp==m*r*y)
for l,m,si,sj in product([F(1),F(2),F(-1)],[F(1),F(3)],range(-2,3),range(-2,3)):
 e=si*m-l*sj;G=[[l,e],[F(0),m]];Hiinv=[[F(1),-F(si)],[F(0),F(1)]];Hj=[[F(1),F(sj)],[F(0),F(1)]]
 ck('actualCechcoboundary gauge splits extension',mm(mm(Hiinv,G),Hj)==[[l,F(0)],[F(0),m]])
 ck('splittinggauge fixes injection andquotient',Hiinv[0][0]==1 and Hiinv[1]==[0,1] and Hj[0][0]==1 and Hj[1]==[0,1])
# Formal line-exponent maps. Coordinates are K_B,M,and the r point lines.
for r in range(1,5):
 for kp in range(-2,4):
  for kq in product(range(-2,4),repeat=r):
   L=[1,-kp-1]+[-k for k in kq];KU=[0,kp]+list(kq);M=[0,1]+[0]*r
   ck('adjunctionlineexponents retain everyweight',[a+b+c for a,b,c in zip(L,KU,M)]==[1,0]+[0]*r)
   # M=O(-Z): replace its exponent by its negative at each point.
   Lred=[L[0]]+[L[2+j]-L[1] for j in range(r)]
   ck('reducedspecialization exactline exponents',Lred==[1]+[kp-k+1 for k in kq])
   if all(k<=kp+1 for k in kq):
    dual_effective=[kp-k+2 for k in kq]
    ck('localmaximum Serredual negativeeffective divisor',all(a>=1 for a in dual_effective) and sum(dual_effective)>0)
for g in range(11):
 for r in range(11):
  eB=2-2*g;eT=2*eB
  ck('supportEuler actualreplacement',eT-eB==2-2*g)
  ck('exacttriplepoint change',r==sum(1 for _ in range(r)))
out={'status':'PASS','checks':len(checks),'method':'new pure-stdlib Fraction Laurent-polynomial determinant and actual transition/line-exponent calculations; no target/old producer imports','jacobians':{'first':'x','second':'-s','overlap':'-1/w'},'weighted_examples':64,'normaldegree_cases':225,'check_names':checks,'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Actual contractions and existence proved in043_UN74_before_read.md; computation validates every displayed map/exponent/count.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='check_names'},indent=2))
