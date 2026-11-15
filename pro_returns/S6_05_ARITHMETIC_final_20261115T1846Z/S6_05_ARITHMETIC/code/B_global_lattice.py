"""Rational lattice and F3 linear algebra for the full plane-orbit search."""
from pathlib import Path
from fractions import Fraction as F
from math import lcm
from itertools import product,combinations
import numpy as np,json
from flint import fmpq_mat,fmpz_mat
from B_gram_utils import qmat,qrows,matrows,hnf,enumerate_gram,root_system
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

def inv(a):
 n=len(a);r,p=rr(np.concatenate([a,np.eye(n,dtype=np.int64)],axis=1));assert p==list(range(n));return r[:,n:]
def ints(a):
 z=qrows(a);assert all(x.denominator==1 for row in z for x in row);return [[int(x) for x in row] for row in z]
def span(rows):
 den=lcm(*(x.denominator for row in rows for x in row));H=hnf([[int(x*den) for x in row] for row in rows]);return fmpq_mat(H)/den

def congruence_kernel(c):
 c=[int(x)%3 for x in c];j=next(j for j,x in enumerate(c) if x);ci=pow(c[j],-1,3);n=len(c);B=[[int(i==k) for k in range(n)] for i in range(n)]
 for i in range(n):
  if i==j:B[i][j]=3
  else:B[i][j]=-c[i]*ci%3
 return fmpq_mat(B)

def intersect(A,B):
 # Standard coordinate pairing suffices for lattice intersection.
 return (span(qrows(A.inv().transpose())+qrows(B.inv().transpose()))).inv().transpose()

def qjson(A):return [[str(x) for x in row] for row in qrows(A)]

class PlaneModel:
 def __init__(self,Ngram,root_basis,rho_factor=F(1),correction=1):
  self.G=qmat(Ngram);self.R=qmat(root_basis);self.N=fmpq_mat([[int(i==j) for j in range(24)] for i in range(24)])
  self.rho=qmat([[F(str(sum(self.R[i,j] for i in range(24))))*rho_factor for j in range(24)]]);self.alpha=qmat([qrows(self.R)[0]])
  assert (self.rho*self.G*self.rho.transpose())[0,0] in [12,24]
  ell=ints(self.N*self.G*self.rho.transpose());self.K=congruence_kernel([x[0] for x in ell]);self.L=span(qrows(self.K)+qrows(self.rho/3-correction*self.alpha));self.Li=self.L.inv();self.v=3*self.alpha
  assert (self.L*self.G*self.L.transpose()).det()==1
 def plane(self,y,prefix):
  y=qmat([y]);V=qmat(qrows(self.v)+qrows(y));P=ints(self.L*self.G*V.transpose());J=self.L
  for k in range(2):
   c=ints(J*self.G*V.transpose());T=congruence_kernel([r[k] for r in c]);J=T*J
  GJ=J*self.G*J.transpose();assert GJ.det()==81
  _,piv=rr(np.array(P).T);assert len(piv)==2
  E=qmat([qrows(self.L)[j] for j in piv]+qrows(V/3));GE=E*self.G*E.transpose()
  elements=list(product(range(3),repeat=4))
  def iso(c):return sum(F(str(GE[i,j]))*c[i]*c[j] for i in range(4) for j in range(4))%2==0
  isot=[c for c in elements if iso(c)];planes=set()
  for a,b in combinations(isot[1:],2):
   s=frozenset(tuple((i*x+j*y)%3 for x,y in zip(a,b)) for i,j in product(range(3),repeat=2))
   if len(s)==9 and all(iso(c) for c in s):planes.add(s)
  assert len(planes)==8
  overs=[]
  for i,s in enumerate(sorted(planes,key=lambda z:sorted(z))):
   nz=sorted(c for c in s if any(c));a=nz[0];b=next(c for c in nz if c!=a and c!=tuple(2*x%3 for x in a))
   B=span(qrows(J)+qrows(fmpq_mat([a,b])*E));g=ints(B*self.G*B.transpose());assert fmpz_mat(g).det()==1
   roots=[x for norm,x in enumerate_gram(g,2,Path(str(prefix)+f'_over_{i}')) if norm==2]
   rs=root_system(g,roots)
   # Index of intersection in L; equality or neighbour are determined exactly.
   K=intersect(self.L,B);index=abs(F(str((K*self.Li).det())))
   overs.append({'basis':qjson(B),'root_system':rs,'roots':roots,'L_intersection_index':int(index)})
  return {'y':qjson(y)[0],'J_basis':qjson(J),'discriminant_basis':qjson(E),'extensions':overs}

def model_A2():
 d=json.loads((REC/'B_A2_strata_setup.json').read_text());A=qmat(d['A']);N=qmat(d['N_basis']);NG=qmat(d['N_Gram']);R=A*(NG.inv()*N).transpose()/144
 return PlaneModel(d['N_Gram'],qrows(R))

def orbit_map(name):
 import gzip,shutil
 cache=ROOT.parent/'B_cache';cache.mkdir(exist_ok=True)
 p=REC/name
 if not p.exists():
  p=cache/name
  if not p.exists():
   with gzip.open(REC/(name+'.gz'),'rb') as a,p.open('wb') as b:shutil.copyfileobj(a,b)
 return np.memmap(p,dtype=np.uint16,mode='r')
