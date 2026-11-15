"""Full cubic stabilizer in Wilson's coordinate-block stabilizer.
Rational triality lifts, a lattice orbit, then a finite binary-code orbit.
Every matrix and cubic identity is checked exactly.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations,product
from math import gcd,lcm
from collections import deque
import json,time
from flint import fmpz_mat,fmpq_mat
from sympy.combinatorics import Permutation,PermutationGroup
from B_triality import TAB,mul,E,R,L,CONJ,entries
ROOT=Path(__file__).resolve().parents[1];REC=ROOT/'records'
eye=lambda n:fmpq_mat([[int(i==j) for j in range(n)] for i in range(n)])
Eb=fmpq_mat(8,8)
for i in range(8):Eb[i,0]='-1/2' if i==0 else '1/2'
for j in range(1,7):Eb[j,j]=1;Eb[j+1,j]=-1
Eb[6,7]=1;Eb[7,7]=1
Ei=Eb.inv()
roots=[]
for i,j in combinations(range(8),2):
 for a,b in product([-1,1],repeat=2):
  v=[0]*8;v[i]=2*a;v[j]=2*b;roots.append(tuple(v))
for v in product([-1,1],repeat=8):
 if sum(x<0 for x in v)%2:roots.append(v)
assert len(roots)==240;rid={r:i for i,r in enumerate(roots)}
data=json.loads((REC/'B_triality_lifts.json').read_text())
gens=[tuple(fmpq_mat(d[k]) for k in ['A','B','C']) for d in data]
gens.append((eye(8),-eye(8),-eye(8)))
def perm_block(M):
 mm=entries(M);out=[]
 for v in roots:
  w=tuple(sum(mm[i][j]*v[j] for j in range(8)) for i in range(8));assert all(x.denominator==1 for x in w);out.append(rid[tuple(map(int,w))])
 return out
perms=[]
for A,B,C in gens:
 p=perm_block(A)+[240+x for x in perm_block(B)];perms.append(Permutation(p))
PG=PermutationGroup(perms);order=int(PG.order());print('triality lift group order',order,flush=True)
assert order==5160960
def can(B):
 vv=entries(B);den=lcm(*(x.denominator for row in vv for x in row));H=fmpz_mat([[int(x*den) for x in row] for row in vv]).hnf()
 nums=[int(H[i,j]) for i in range(8) for j in range(8)];g=gcd(den,*nums);den//=g;nums=[x//g for x in nums]
 return (den,tuple(nums))
def uncan(key):
 den,v=key;return fmpq_mat([v[8*i:8*(i+1)] for i in range(8)])/den
idkey=can(Eb.transpose());keys=[idkey];index={idkey:0};reps=[(eye(8),eye(8),eye(8))];rperms=[Permutation(list(range(480)))];edges=[]
for si,key in enumerate(keys):
 basis=uncan(key);edge=[]
 for gi,gen in enumerate(gens):
  nxt=can(basis*gen[2].transpose())
  if nxt not in index:
   index[nxt]=len(keys);keys.append(nxt);reps.append(tuple(gen[k]*reps[si][k] for k in range(3)));rperms.append(rperms[si]*perms[gi])
  edge.append(index[nxt])
 edges.append(edge)
 if si%100==0:print('C lattice orbit',si,'discovered',len(keys),flush=True)
 assert len(keys)<100000
print('C lattice orbit size',len(keys),'stabilizer order',order//len(keys),flush=True)
stgens=[];stperms=[];sub=PermutationGroup([Permutation(list(range(480)))])
for si,edge in enumerate(edges):
 for gi,di in enumerate(edge):
  p=rperms[si]*perms[gi]*(rperms[di]**-1)
  if sub.contains(p):continue
  T=tuple(reps[di][k].inv()*gens[gi][k]*reps[si][k] for k in range(3))
  assert perm_block(T[0])+[240+x for x in perm_block(T[1])]==list(p.array_form)
  assert can(Eb.transpose()*T[2].transpose())==idkey
  stgens.append(T);stperms.append(p);sub=PermutationGroup(stperms)
assert int(sub.order())*len(keys)==order
print('C lattice stabilizer independent generators',len(stgens),flush=True)

# Binary Wilson glue C: pair sums in M=L*bar(s), total in N=L*s.
sv=[F(-1,2)]+[F(1,2)]*7;sbar=[sv[0]]+[-x for x in sv[1:]]
S=Ei*R(sv)*Eb;T=Ei*R(sbar)*Eb
def bitcols(a):
 return [sum((int(a[i,j])%2)<<i for i in range(8)) for j in range(8)]
def echelon(vv):
 bs={}
 for v in vv:
  while v:
   p=v.bit_length()-1
   if p in bs:v^=bs[p]
   else:
    bs[p]=v;break
 for p in sorted(bs):
  for q in sorted(bs):
   if q>p and (bs[q]>>p)&1:bs[q]^=bs[p]
 return tuple(bs[p] for p in sorted(bs))
mb=echelon(bitcols(T));nb=echelon(bitcols(S));assert len(mb)==len(nb)==4
code=echelon([m|(m<<16) for m in mb]+[(m<<8)|(m<<16) for m in mb]+[n|(n<<8)|(n<<16) for n in nb]);assert len(code)==12
acts=[]
for triple in stgens:
 out=[]
 for k,a in enumerate(triple):
  z=Ei*a*Eb;assert all(z[i,j].denom()==1 for i in range(8) for j in range(8));out += [v<<(8*k) for v in bitcols(z)]
 acts.append(out)
def act(v,a):
 w=0
 while v:
  bit=v&-v;i=bit.bit_length()-1;w^=a[i];v^=bit
 return w
codes=[code];idx={code:0};words=[()];cedges=[]
for si,c in enumerate(codes):
 edge=[]
 for gi,a in enumerate(acts):
  nc=echelon([act(v,a) for v in c])
  if nc not in idx:idx[nc]=len(codes);codes.append(nc);words.append(words[si]+(gi,))
  edge.append(idx[nc])
 cedges.append(edge)
 if si%1000==0:print('Wilson code orbit',si,'discovered',len(codes),flush=True)
 assert len(codes)<1000000
print('Wilson code orbit size',len(codes),'block cubic stabilizer order',order//len(keys)//len(codes),flush=True)

# Schreier generators, keeping only independent permutations.
wp=[Permutation(list(range(480))) for _ in words]
for i,w in enumerate(words):
 if w:wp[i]=wp[idx[echelon([act(v,acts[w[-1]]) for v in codes[i]])]] if False else Permutation(list(range(480)))
 for gi in w:wp[i]=wp[i]*stperms[gi]
outgen=[];outperm=[];sg=PermutationGroup([Permutation(list(range(480)))])
for si,edge in enumerate(cedges):
 for gi,di in enumerate(edge):
  p=wp[si]*stperms[gi]*(wp[di]**-1)
  if sg.contains(p):continue
  def wordmat(w):
   z=(eye(8),eye(8),eye(8))
   for g in w:z=tuple(stgens[g][k]*z[k] for k in range(3))
   return z
  a=wordmat(words[si]);b=wordmat(words[di]);z=tuple(b[k].inv()*stgens[gi][k]*a[k] for k in range(3))
  assert perm_block(z[0])+[240+x for x in perm_block(z[1])]==list(p.array_form)
  outgen.append(z);outperm.append(p);sg=PermutationGroup(outperm)
  print('block cubic stabilizer generated',sg.order(),'generators',len(outgen),flush=True)
  if int(sg.order())==order//len(keys)//len(codes):break
 if int(sg.order())==order//len(keys)//len(codes):break
assert int(sg.order())*len(codes)*len(keys)==order
out={'triality_group_order':order,'C_lattice_orbit':len(keys),'Wilson_glue_orbit':len(codes),'block_stabilizer_order':int(sg.order()),'full_stabilizer_order':3*int(sg.order()),'block_generators':[[[[str(x) for x in row] for row in entries(M)] for M in triple] for triple in outgen]}
(REC/'B_wilson_stabilizer.json').write_text(json.dumps(out))
print('full cubic stabilizer order',out['full_stabilizer_order'],flush=True)
