"""Exact stratification of isotropic flags with an A2^12 neighbour.

The output consists of affine actions on F3^16.  The full group is
C2 x (3^6 : Aut_mon(G12)); no sampling is used in the stratum search.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from collections import Counter
import json, numpy as np,pynauty
from flint import fmpq_mat,fmpz_mat
from sympy.combinatorics import Permutation,PermutationGroup
from B_exact_lattices import N,J,neighbour,gram,qmat,basis,dot
ROOT=Path(__file__).resolve().parents[1];REC=ROOT/'records'
def rr(a,p=3):
 a=np.array(a,dtype=np.int64)%p;r=0;piv=[]
 for j in range(a.shape[1]):
  z=next((z for z in range(r,len(a)) if a[z,j]),None)
  if z is None:continue
  a[[r,z]]=a[[z,r]];a[r]=a[r]*pow(int(a[r,j]),-1,p)%p
  for z in range(len(a)):
   if z!=r:a[z]=(a[z]-a[z,j]*a[r])%p
  piv.append(j);r+=1
  if r==len(a):break
 return a[:r],piv

def null(a,n):
 r,piv=rr(np.array(a).reshape((-1,n)));out=[]
 for j in range(n):
  if j in piv:continue
  v=np.zeros(n,dtype=np.int64);v[j]=1
  for row,k in zip(r,piv):v[k]=-row[j]%3
  out.append(v)
 return np.array(out,dtype=np.int64)
def inv(a):
 n=len(a);r,p=rr(np.concatenate([a,np.eye(n,dtype=np.int64)],axis=1));assert p==list(range(n));return r[:,n:]
def fentries(a):return [[F(str(a[i,j])) for j in range(a.ncols())] for i in range(a.nrows())]
def intarray(a):
 v=fentries(a);assert all(x.denominator==1 for r in v for x in r);return np.array([[int(x) for x in r] for r in v],dtype=np.int64)
A=json.loads((REC/'B_autJ_data.json').read_text())['root_basis'];Nm=neighbour(2)
Am=fmpq_mat(A);Nmq=fmpq_mat(Nm);AG=qmat(gram(A));NG=qmat(gram(Nm));Nd=NG.inv()*Nmq
Crat=Nmq*(AG.inv()*Am).transpose()/144
craw=[]
for row in fentries(Crat):craw.append([int(3*row[2*i+1])%3 for i in range(12)])
C,piv=rr(craw);assert C.shape==(6,12);Cmap=np.array(craw,dtype=np.int64)[:,piv]
code=[tuple((np.array(a)@C%3).tolist()) for a in product(range(3),repeat=6)];print('Golay',dict(Counter(sum(x!=0 for x in c) for c in code)),flush=True)
adj={i:[i^1] for i in range(24)}
for c in code:
 if not any(c):continue
 k=len(adj);adj[k]=[2*i+int(x==2) for i,x in enumerate(c) if x]
 for j in adj[k]:adj[j].append(k)
graph=pynauty.Graph(len(adj),adjacency_dict=adj,vertex_coloring=[set(range(24)),set(range(24,len(adj)))])
gg,ma,ex,_,_=pynauty.autgrp(graph);perms=[Permutation(g[:24]) for g in gg];PG=PermutationGroup(perms);assert int(PG.order())==190080
mono=[([g(2*i)//2 for i in range(12)],[1 if g(2*i)%2==0 else -1 for i in range(12)]) for g in perms]
I=fmpq_mat([[int(i==j) for j in range(24)] for i in range(24)]);r=fmpq_mat([[0,1],[-1,-1]]);sw=fmpq_mat([[0,1],[1,0]])
def rot(z):
 T=fmpq_mat(I)
 for i,k in enumerate(z):
  a=r**int(k)
  for j in range(2):
   for l in range(2):T[2*i+j,2*i+l]=a[j,l]
 return T

def monoT(p):
 T=fmpq_mat(24,24)
 for i in range(12):
  j=p(2*i)//2;a=sw if p(2*i)%2 else fmpq_mat([[1,0],[0,1]])
  for z in range(2):
   for w in range(2):T[2*i+z,2*j+w]=a[z,w]
 return T

def toNfull(T):
 a=Crat*T*Crat.inv();z=intarray(a);assert a*NG*a.transpose()==NG;return z
def toN(T):return toNfull(T)%3
Nrots=[toN(rot(z)) for z in C];Nmonos=[toN(monoT(p)) for p in perms]
rho=np.sum(np.array(A,dtype=np.int64),axis=0);rhoN=intarray(fmpq_mat([rho.tolist()])*Nd.transpose()/144)[0]%3
GN=intarray(NG)%3;ell=GN@rhoN%3;j=next(j for j,x in enumerate(rhoN) if x);unit=np.zeros(24,dtype=np.int64);unit[j]=1
W,wpiv=rr(null([ell,unit],24));assert W.shape==(22,24)
CP=W@Cmap%3;ker=null(CP.T,22);assert ker.shape==(16,22)
# Add sections of the six code-coordinate standard basis.
aug,pivs=rr(CP.T);assert len(pivs)==6
sec=np.zeros((6,22),dtype=np.int64);sec[:,pivs]=inv(CP[pivs,:])
assert np.array_equal(sec@CP%3,np.eye(6,dtype=np.int64))
B=np.concatenate([ker,sec]);Bi=inv(B);Y=B@W%3
assert np.array_equal(Y[:16]@Cmap%3,np.zeros((16,6),dtype=np.int64))
assert np.array_equal(Y[16:]@Cmap%3,np.eye(6,dtype=np.int64))
Q=Y@GN@Y.T%3
# Transform any N-isometry preserving rho line to Y quotient coordinates.
def toY(T):
 Z=Y@T%3;Z=(Z-Z[:,j,None]*pow(int(rhoN[j]),-1,3)*rhoN[None,:])%3
 out=Z[:,wpiv]@Bi%3;assert np.array_equal(out@Y%3,Z);return out
YR=[toY(T) for T in Nrots];YM=[toY(T) for T in Nmonos]
assert all(np.array_equal(T[:16,16:],np.zeros((16,6),dtype=np.int64)) for T in YR+YM)

def actc(c,p):
 out=[0]*12
 for i,x in enumerate(c):out[p(2*i)//2]=x*(1 if p(2*i)%2==0 else -1)%3
 return tuple(out)
seen=set();strata=[]
for c in code:
 if c in seen:continue
 orb=[c];oid={c:0};rp=[Permutation(list(range(24)))];edges=[]
 for v in orb:
  si=oid[v];ee=[]
  for p in perms:
   w=actc(v,p)
   if w not in oid:oid[w]=len(orb);orb.append(w);rp.append(rp[si]*p)
   ee.append(oid[w])
  edges.append(ee)
 seen.update(orb)
 sg=[];sub=PermutationGroup([Permutation(list(range(24)))])
 for si,ee in enumerate(edges):
  for gi,di in enumerate(ee):
   p=rp[si]*perms[gi]*rp[di]**-1
   if sub.contains(p):continue
   sg.append(p);sub=PermutationGroup(sg)
 assert int(sub.order())*len(orb)==190080
 fullmats=[toNfull(rot(z)) for z in C]+[toNfull(monoT(p)) for p in sg]
 mats=YR+[toY(toN(monoT(p))) for p in sg]
 if any(c):
  negc=Permutation([i^1 for i in range(24)]);assert PG.contains(negc)
  mats.append(toY((-toN(monoT(negc)))%3));fullmats.append(-toNfull(monoT(negc)))
 else:
  mats.append(-np.eye(22,dtype=np.int64)%3);fullmats.append(-np.eye(24,dtype=np.int64))
 cv=np.array(c,dtype=np.int64)[piv];assert np.array_equal(cv@C%3,c)
 aff=[]
 for T in mats:
  assert np.array_equal(cv@T[16:,16:]%3,cv)
  aff.append(np.concatenate([T[:16,:16],(cv@T[16:,:16]%3)[None,:]],axis=0).tolist())
 n=len(strata);inp=REC/f'B_A2_stratum_{n}.in'
 # Polynomial x Q x/2 with full coordinates [x16,cv6].
 q=Q[:16,:16]*2%3;lin=cv@(Q[16:,:16]+Q[:16,16:].T)*2%3;con=int(cv@Q[16:,16:]@cv*2%3)
 with inp.open('w') as f:
  f.write(f'16 {len(aff)}\n')
  for T in aff:
   for row in T:f.write(' '.join(map(str,row))+'\n')
  for row in q:f.write(' '.join(map(str,row))+'\n')
  f.write(' '.join(map(str,lin))+'\n'+str(con)+'\n')
 print('stratum',n,'weight',sum(x!=0 for x in c),'code_orbit',len(orb),'code_stabilizer',sub.order(),'affine_generators',len(aff),flush=True)
 assert len(fullmats)==len(aff)
 strata.append({'c':c,'c_coeff':cv.tolist(),'code_orbit':len(orb),'code_stabilizer':int(sub.order()),'affine_generators':aff,'generators_in_N_basis':[T.tolist() for T in fullmats],'group_order':2*729*int(sub.order())})
assert len(strata)==4
out={'A':A,'N_basis':Nm,'N_Gram':intarray(NG).tolist(),'C':C.tolist(),'C_pivots':piv,'N_code_map':Cmap.tolist(),'rho_N_mod3':rhoN.tolist(),'Y_basis':Y.tolist(),'Y_Gram_mod3':Q.tolist(),'monomial_generators':[p.array_form for p in perms],'strata':strata}
(REC/'B_A2_strata_setup.json').write_text(json.dumps(out))
