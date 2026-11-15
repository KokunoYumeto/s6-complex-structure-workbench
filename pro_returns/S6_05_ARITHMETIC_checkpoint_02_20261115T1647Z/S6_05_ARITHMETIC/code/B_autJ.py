"""Exact full automorphism group of J via its intrinsic A2^12 roots.

Nauty only computes automorphisms of an explicitly encoded finite code.
Completeness follows from the written reduction to the code; all returned
24 by24 lattice matrices are independently checked over Z.
"""
import json,sys,time
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from collections import Counter
from flint import fmpz_mat,fmpq_mat
import pynauty
from sympy.combinatorics import Permutation,PermutationGroup
ROOT=Path(__file__).resolve().parents[1];REC=ROOT/'records';sys.path.insert(0,str(ROOT/'code'))
from B_exact_lattices import basis,gram,dot,det,J,qmat,over,e,lift

def rref(a,p=3):
 a=[[int(x)%p for x in row] for row in a];nr=len(a);nc=len(a[0]) if a else 0;r=0;piv=[]
 for j in range(nc):
  k=next((k for k in range(r,nr) if a[k][j]),None)
  if k is None:continue
  a[r],a[k]=a[k],a[r];v=pow(a[r][j],-1,p);a[r]=[x*v%p for x in a[r]]
  for k in range(nr):
   if k!=r and a[k][j]:
    v=a[k][j];a[k]=[(x-v*y)%p for x,y in zip(a[k],a[r])]
  piv.append(j);r+=1
  if r==nr:break
 return a[:r],piv
def nullspace(a,n):
 rr,piv=rref(a);out=[]
 for j in range(n):
  if j in piv:continue
  v=[0]*n;v[j]=1
  for row,k in zip(rr,piv):v[k]=-row[j]%3
  out.append(v)
 return out
def get_roots(name):
 b=json.loads((REC/f'B_{name}.basis.json').read_text());rr=[]
 for line in (REC/f'B_{name}.out').read_text().splitlines():
  if line.startswith('vector 2 '):
   a=list(map(int,line.split()[2:]));rr.append(tuple(sum(a[i]*b[i][j] for i in range(24)) for j in range(28)))
 return rr
roots=get_roots('over_2');assert set(roots)==set(get_roots('over_6')) and len(roots)==72
root0=roots[0]
def inJ(x):return basis(J+[x])==J
pos=[x for x in roots if inJ(tuple(a-b for a,b in zip(x,root0)))];assert len(pos)==36
components=[];seen=set()
for a in roots:
 if a in seen:continue
 cc={b for b in roots if dot(a,b)!=0};assert len(cc)==6;components.append(cc);seen|=cc
A=[]
for cc in components:
 a=next(a for a in pos if a in cc);b=next(b for b in pos if b in cc and dot(a,b)==-1);A += [a,b]
assert len(A)==24 and det(A)==3**12
Amat=fmpq_mat([list(a) for a in A]);Jmat=fmpq_mat([list(a) for a in J]);Ad=qmat(gram(A)).inv()*Amat
C=Jmat*Ad.transpose()/144
rows=[]
for i in range(24):
 vals=[F(str(C[i,j])) for j in range(24)]
 c=[int(3*vals[2*k+1])%3 for k in range(12)]
 assert all((vals[2*k]+vals[2*k+1]).denominator==1 for k in range(12))
 h=int(sum(vals))-sum(c);rows.append(c+[h%3])
graph,piv=rref(rows);assert len(graph)==5 and 12 not in piv
D=[r[:12] for r in graph];f=[r[12] for r in graph]
assert all(sum(x*y for x,y in zip(a,b))%3==0 for a in D for b in D)
z0=[0]*12
for k,pi in enumerate(piv):z0[pi]=f[k]
assert all(sum(x*y for x,y in zip(z0,c))%3==h for c,h in zip(D,f))
code=[]
for coeff in product(range(3),repeat=5):code.append(tuple(sum(coeff[k]*D[k][j] for k in range(5))%3 for j in range(12)))
print('A2 components',len(components),'D dimension',len(D),'weight enumerator',dict(sorted(Counter(sum(x!=0 for x in c) for c in code).items())),flush=True)
print('D generator matrix',D,'f',f,'normalizing rotations',z0,flush=True)
adj={i:[i^1] for i in range(24)}
for c in code:
 if not any(c):continue
 k=len(adj);adj[k]=[2*i+int(x==2) for i,x in enumerate(c) if x]
 for j in adj[k]:adj[j].append(k)
g=pynauty.Graph(len(adj),adjacency_dict=adj,vertex_coloring=[set(range(24)),set(range(24,len(adj)))])
gg,mant,exp,orbs,norbs=pynauty.autgrp(g)
perms=[p[:24] for p in gg]
PG=PermutationGroup([Permutation(p) for p in perms]);order=int(PG.order())
print('monomial Aut(D) order',order,'nauty',mant,exp,'number generators',len(perms),flush=True)
assert order==int(mant*10**exp)
mono=[]
for p in perms:
 perm=[];sgn=[]
 for i in range(12):
  assert p[2*i]^1==p[2*i+1]
  perm.append(p[2*i]//2);sgn.append(1 if p[2*i]%2==0 else -1)
 assert len(set(perm))==12
 for c in code:
  q=[0]*12
  for i in range(12):q[perm[i]]=sgn[i]*c[i]%3
  assert tuple(q) in code
 mono.append((perm,sgn))

def eye(n):return fmpq_mat([[int(i==j) for j in range(n)] for i in range(n)])
# Row-coordinate matrices: r sends beta->gamma, gamma->-beta-gamma.
r=fmpq_mat([[0,1],[-1,-1]]);ds=fmpq_mat([[0,1],[1,0]]);tt=ds*r
assert tt*tt==eye(2)
def rotations(z):
 out=eye(24)
 for i,v in enumerate(z):
  a=r**int(v%3)
  for j in range(2):
   for k in range(2):out[2*i+j,2*i+k]=a[j,k]
 return out
S=rotations(z0);Si=S.inv();ker=nullspace(D,12);assert len(ker)==7
normalgens=[rotations(z) for z in ker]
for perm,sgn in mono:
 out=fmpq_mat(24,24)
 for i,j in enumerate(perm):
  a=eye(2) if sgn[i]==1 else tt
  for k in range(2):
   for ell in range(2):out[2*i+k,2*j+ell]=a[k,ell]
 normalgens.append(out)
normalgens.append(-eye(24))
origgens=[S*T*Si for T in normalgens]
GJ=qmat(gram(J));Ci=C.inv();integralgens=[];planeacts=[]
for T in origgens:
 Tj=C*T*Ci
 vals=[[F(str(Tj[i,j])) for j in range(24)] for i in range(24)]
 assert all(v.denominator==1 for row in vals for v in row)
 assert Tj*GJ*Tj.transpose()==GJ and Tj.det() in (-1,1)
 integralgens.append([[int(v) for v in row] for row in vals])
 # Permutation of the eight even unimodular extensions, via original bases.
 pp=[]
 for a,b,bb in over:
  bm=fmpq_mat([list(x) for x in bb]);bc=bm*Ad.transpose()/144;im=bc*T*Amat
  vv=[[F(str(im[i,j])) for j in range(28)] for i in range(24)]
  assert all(v.denominator==1 for row in vv for v in row)
  ib=basis([[int(v) for v in row] for row in vv]);pp.append(next(k for k,(_,_,cc) in enumerate(over) if cc==ib))
 planeacts.append(pp)
AP=PermutationGroup([Permutation(p) for p in planeacts]);orb=AP.orbit(5)
grouporder=2*(3**7)*order
print('Aut(J) order',grouporder,'abstract normal form C2 x (3^7 : Aut_mon(D))',flush=True)
print('number checked integral matrix generators',len(integralgens),flush=True)
print('image on eight planes order',AP.order(),'orbits',AP.orbits(),flush=True)
print('stabilizer of L0 in Aut(J)',grouporder//len(orb),'Leech extension orbit',orb,flush=True)
(REC/'B_autJ_data.json').write_text(json.dumps({'root_basis':A,'J_coordinates_in_root_basis':[[str(C[i,j]) for j in range(24)] for i in range(24)],'D':D,'f':f,'normalizing_rotations':z0,'kernel_basis':ker,'monomial_generators':mono,'monomial_order':order,'AutJ_order':grouporder,'AutJ_generators':integralgens,'plane_permutations':planeacts,'plane_image_order':int(AP.order()),'stabilizer_Leech_order':grouporder//len(orb)}))
