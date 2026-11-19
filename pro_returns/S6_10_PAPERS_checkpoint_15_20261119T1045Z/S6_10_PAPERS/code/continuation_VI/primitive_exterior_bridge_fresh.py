#!/usr/bin/env python3
"""Fresh exact exterior-square bridge; no target or old producer imports."""
from fractions import Fraction as F
from itertools import combinations, permutations
from pathlib import Path
from hashlib import sha256
import json
checks=[]
def ck(n,c):
 if not c:raise AssertionError(n)
 checks.append(n)
def zero(n,m):return [[F(0) for _ in range(m)] for _ in range(n)]
def eye(n):return [[F(int(i==j)) for j in range(n)] for i in range(n)]
def tr(a):return list(map(list,zip(*a)))
def mm(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(a,c):return [[c*x for x in r] for r in a]
def sub(a,b):return add(a,scale(b,-1))
def rank(a):
 a=[list(map(F,r)) for r in a];i=0
 if not a:return 0
 for j in range(len(a[0])):
  k=next((k for k in range(i,len(a)) if a[k][j]),None)
  if k is None:continue
  a[i],a[k]=a[k],a[i];d=a[i][j];a[i]=[x/d for x in a[i]]
  for k in range(len(a)):
   if k!=i and a[k][j]:
    d=a[k][j];a[k]=[x-d*y for x,y in zip(a[k],a[i])]
  i+=1
  if i==len(a):break
 return i
def det(a):
 a=[list(map(F,r)) for r in a];ans=F(1)
 for j in range(len(a)):
  k=next((k for k in range(j,len(a)) if a[k][j]),None)
  if k is None:return F(0)
  if k!=j:a[j],a[k]=a[k],a[j];ans=-ans
  d=a[j][j];ans*=d
  for k in range(j+1,len(a)):
   c=a[k][j]/d
   for l in range(j,len(a)):a[k][l]-=c*a[j][l]
 return ans
pairs=list(combinations(range(4),2))
def wedge2(a):return [[a[i][k]*a[j][l]-a[i][l]*a[j][k] for k,l in pairs] for i,j in pairs]
def sign(p):return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
W=zero(6,6)
for i,p in enumerate(pairs):
 for j,q in enumerate(pairs):
  if len(set(p+q))==4:W[i][j]=sign(p+q)
B=zero(6,5)
for i,j,c in [(1,0,1),(2,1,1),(4,2,-1),(3,3,1),(0,4,1),(5,4,-1)]:B[i][j]=F(c)
L=zero(5,6)
for i,j,c in [(0,1,1),(1,2,1),(2,4,-1),(3,3,1),(4,0,1)]:L[i][j]=F(c)
omega=[[F(int(i in (0,5)))] for i in range(6)]
Q=mm(mm(tr(B),W),B)
Qexpected=zero(5,5)
for i,j in [(0,2),(2,0),(1,3),(3,1)]:Qexpected[i][j]=1
Qexpected[4][4]=-2
ck('exact primitive Gram matrix',Q==Qexpected)
ck('omega has normtwo',mm(mm(tr(omega),W),omega)==[[F(2)]])
ck('primitive basis is orthogonal toomega',mm(mm(tr(omega),W),B)==zero(1,5))
ck('primitive extraction is actual leftinverse',mm(L,B)==eye(5))
J=zero(4,4)
for i,j in [(0,1),(2,3)]:J[i][j]=1;J[j][i]=-1

def derivative(x):
 D=zero(6,6)
 for col,(i,j) in enumerate(pairs):
  for k in range(4):
   for a,b,c in [(k,j,x[k][i]),(i,k,x[k][j])]:
    if a==b:continue
    s=1 if a<b else -1;ab=tuple(sorted((a,b)));D[pairs.index(ab)][col]+=s*c
 return D
# Blocks in e1,e2,f1,f2 order, then permute to interleaved order.
sp=[];perm=[0,2,1,3]
for typ in ['A','B','C']:
 indices=list((i,j) for i in range(2) for j in range(2)) if typ=='A' else list(combinations(range(2),2))+[(0,0),(1,1)]
 for i,j in indices:
  x=zero(4,4)
  if typ=='A':x[i][j]=1;x[j+2][i+2]=-1
  elif typ=='B':x[i][j+2]=1;x[j][i+2]=1
  else:x[i+2][j]=1;x[j+2][i]=1
  y=zero(4,4)
  for k in range(4):
   for l in range(4):y[perm[k]][perm[l]]=x[k][l]
  ck('symplectic Lie basis satisfies infinitesimalform',add(mm(tr(y),J),mm(J,y))==zero(4,4));sp.append(y)
Ds=[]
for x in sp:
 D=derivative(x);d=mm(mm(L,D),B)
 ck('differential killsomega',mm(D,omega)==zero(6,1))
 ck('differential retainsprimitive subspace',mm(D,B)==mm(B,d))
 ck('differential isQskew',add(mm(tr(d),Q),mm(Q,d))==zero(5,5));Ds.append([e for row in d for e in row])
ck('ten-dimensional differential isinjective',len(sp)==10 and rank(Ds)==10)
T=eye(4);T[0][1]=1
ck('transvection preserves symplecticform',mm(mm(tr(T),J),T)==J)
rhoT=mm(mm(L,wedge2(T)),B);N=sub(rhoT,eye(5));expected=zero(5,5);expected[1][2]=-1;expected[0][3]=1
ck('exacttransvection twoarrow matrix',N==expected)
ck('orthogonalJordan221 ranktwo squareszero',rank(N)==2 and mm(N,N)==zero(5,5))
ck('both central signs have identicalexterior image',wedge2(scale(T,-1))==wedge2(T))
ck('positive lift hasrankone nilpotentpart',rank(sub(T,eye(4)))==1)
ck('negative lift hasrankone shiftedpart',rank(add(scale(T,-1),eye(4)))==1)
ck('full exterior representationpreserves form',mm(mm(tr(wedge2(T)),W),wedge2(T))==W)
# Exact diagonal weights in the two independent exponent variables x,y.
weights=[(1,0),(-1,0),(0,1),(0,-1)]
wedgeweights=[tuple(weights[i][k]+weights[j][k] for k in range(2)) for i,j in pairs]
primitiveweights=[]
for col in range(5):
 w={wedgeweights[i] for i in range(6) if B[i][col]};ck('each primitivebasisvector isaneigenvector',len(w)==1);primitiveweights.append(next(iter(w)))
ck('diagonaleigenvalue map',primitiveweights==[(1,1),(1,-1),(-1,-1),(-1,1),(0,0)])
# Universal skew coefficient change is a two-by-two Laurent identity; verify
# exact coefficient algebra for independently chosen nonzero rational c.
J2=[[F(0),F(1)],[F(-1),F(0)]]
for c in [F(n,d) for n in range(-7,8) if n for d in range(1,5)]:
 S=[[c,F(0)],[F(0),F(1)]];Sinv=[[1/c,F(0)],[F(0),F(1)]]
 ck('actualWitt coefficient change cJtoJ',mm(mm(Sinv,scale(J2,c)),tr(Sinv))==J2)
# Reflections are explicit actual orthogonal maps; compose pairs for SO.
Qinv=zero(5,5)
for i,j in [(0,2),(2,0),(1,3),(3,1)]:Qinv[i][j]=1
Qinv[4][4]=F(-1,2)
def reflect(v):
 v=[[F(x)] for x in v];norm=mm(mm(tr(v),Q),v)[0][0]
 if not norm:return None
 return sub(eye(5),scale(mm(v,mm(tr(v),Q)),F(2)/norm))
vs=[[a,b,c,d,e] for a,b,c,d,e in [(1,0,1,0,0),(0,1,0,1,0),(1,1,1,0,1),(2,1,1,1,1),(1,2,3,1,0),(2,0,0,1,1)]]
Rs=[reflect(v) for v in vs];Rs=[r for r in Rs if r]
for r in Rs:ck('reflection isQorthogonal determinantminusone',mm(mm(tr(r),Q),r)==Q and det(r)==-1)
for r,s in [(r,s) for r in Rs for s in Rs]:
 Fm=mm(r,s);Finv=mm(mm(Qinv,tr(Fm)),Q);Nm=mm(mm(Fm,N),Finv)
 ck('explicitconjugating map liesinSO',det(Fm)==1 and mm(mm(tr(Fm),Q),Fm)==Q)
 ck('orthogonalconjugated nilpotent hascorrecttype',rank(Nm)==2 and mm(Nm,Nm)==zero(5,5))
 ck('actualintertwining equality',mm(Nm,Fm)==mm(Fm,N))
 ck('ranktwoimage isotropic and skew',mm(mm(tr(Nm),Q),Nm)==zero(5,5) and add(mm(tr(Nm),Q),mm(Q,Nm))==zero(5,5))
# Encode rational matrices without lossy conversion.
def enc(a):return [[str(x) for x in row] for row in a]
out={'status':'PASS','checks':len(checks),'method':'new pure-stdlib Fraction matrix/exterior algebra; no target/producer imports','primitive_basis_gram':enc(Q),'transvection_image_minus_identity':enc(N),'Lie_differential_rank':rank(Ds),'diagonal_exponent_weights':primitiveweights,'check_names':checks,'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Universal image/kernel/conjugacy proved in frozen written note; exact finite matrix checks validate its computational steps.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='check_names'},indent=2))
