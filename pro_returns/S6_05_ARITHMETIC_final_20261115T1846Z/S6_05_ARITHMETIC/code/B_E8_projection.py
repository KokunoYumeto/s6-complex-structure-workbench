"""Completeness bound for block projections in the Wilson cubic problem."""
from fractions import Fraction as F
from itertools import product,combinations
from pathlib import Path
import json
from flint import fmpz_mat,fmpq_mat
from sympy.combinatorics import Permutation,PermutationGroup
from B_triality import TAB,mul,E,R,L,entries
ROOT=Path(__file__).resolve().parents[1];REC=ROOT/'records'
Eb=fmpq_mat(8,8)
for i in range(8):Eb[i,0]='-1/2' if i==0 else '1/2'
for j in range(1,7):Eb[j,j]=1;Eb[j+1,j]=-1
Eb[6,7]=1;Eb[7,7]=1
Ei=Eb.inv();roots=[]
for i,j in combinations(range(8),2):
 for a,b in product([-1,1],repeat=2):
  v=[F(0)]*8;v[i]=a;v[j]=b;roots.append(tuple(v))
for v in product([-1,1],repeat=8):
 if sum(x<0 for x in v)%2:roots.append(tuple(F(x,2) for x in v))
rid={r:i for i,r in enumerate(roots)}
pos=[r for r in roots if next(x for x in r if x)>0]
rho=[sum(r[i] for r in pos)/2 for i in range(8)]
simple=[r for r in roots if sum(x*y for x,y in zip(r,rho))==1];assert len(simple)==8
eye=fmpq_mat([[int(i==j) for j in range(8)] for i in range(8)])
wg=[]
for r in simple:wg.append(eye-fmpq_mat([[str(x*y) for y in r] for x in r]))
def perm(M):
 mm=entries(M)
 return Permutation([rid[tuple(sum(mm[i][j]*r[j] for j in range(8)) for i in range(8))] for r in roots])
W=PermutationGroup([perm(g) for g in wg]);wo=int(W.order());assert wo==696729600
def ech(vv):
 bs={}
 for v in vv:
  while v:
   p=v.bit_length()-1
   if p in bs:v^=bs[p]
   else:bs[p]=v;break
 for p in sorted(bs):
  for q in sorted(bs):
   if q>p and (bs[q]>>p)&1:bs[q]^=bs[p]
 return tuple(bs[p] for p in sorted(bs))
def cols(M):
 assert all(M[i,j].denom()==1 for i in range(8) for j in range(8))
 return [sum((int(M[i,j])%2)<<i for i in range(8)) for j in range(8)]
def act(v,a):return __import__('functools').reduce(int.__xor__,(a[i] for i in range(8) if (v>>i)&1),0)
sbar=[F(-1,2)]*8;M=ech(cols(Ei*R(sbar)*Eb));assert len(M)==4
acts=[cols(Ei*g*Eb) for g in wg];keys=[M];index={M:0}
for c in keys:
 for a in acts:
  cc=ech([act(v,a) for v in c])
  if cc not in index:index[cc]=len(keys);keys.append(cc)
data=json.loads((REC/'B_triality_lifts.json').read_text());gg=[fmpq_mat(d['A']) for d in data]
G=PermutationGroup([perm(g) for g in gg]);go=int(G.order())
assert wo==go*len(keys)
assert all(g.det()==1 and ech([act(v,cols(Ei*g*Eb)) for v in M])==M for g in gg)
print('Aut(E8) order',wo,'orbit of M mod2',len(keys),'full M-stabilizer order',go)
print('all displayed projection generators have determinant+1')
for anti in [False,True]:
 rows=[]
 for i in range(8):
  for j in range(8):
   s,k=TAB[j,i] if anti else TAB[i,j]
   A=L(E[i])*L(E[j])-L(E[k])*s
   rows+= [[int(A[a,b]) for b in range(8)] for a in range(8)]
 _,dim=fmpz_mat(rows).nullspace()
 print('reversed' if anti else 'associative','right-multiplier solution dimension',dim)
 assert dim==(0 if anti else 1)
(REC/'B_E8_projection.json').write_text(json.dumps({'E8_order':wo,'M_orbit':len(keys),'projection_order':go,'simple_roots':[[str(x) for x in r] for r in simple]}))
