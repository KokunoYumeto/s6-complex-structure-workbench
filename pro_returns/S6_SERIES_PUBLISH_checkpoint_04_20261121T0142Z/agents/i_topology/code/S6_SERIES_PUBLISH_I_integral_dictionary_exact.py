#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import permutations
from math import gcd
from pathlib import Path
import json
Pth=Path(__file__).resolve().parents[1]
def mm(A,B):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]
def add(A,B):return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]
def neg(A):return [[-x for x in row] for row in A]
def mv(A,v):return [sum(x*y for x,y in zip(row,v)) for row in A]
def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def det(A):return sum((-1)**sum(s[i]>s[j] for i in range(len(s)) for j in range(i+1,len(s)))*__import__('functools').reduce(lambda a,i:a*A[i][s[i]],range(len(s)),1) for s in permutations(range(len(A))))
def rref(A):
 A=[list(map(F,row)) for row in A];i=0;piv=[]
 for j in range(len(A[0])):
  k=next((k for k in range(i,len(A)) if A[k][j]),None)
  if k is None:continue
  A[i],A[k]=A[k],A[i];d=A[i][j];A[i]=[v/d for v in A[i]]
  for k in range(len(A)):
   if k!=i:
    d=A[k][j];A[k]=[x-d*y for x,y in zip(A[k],A[i])]
  piv.append(j);i+=1
  if i==len(A):break
 return A,piv
def inv(A):return [r[len(A):] for r in rref([list(a)+e for a,e in zip(A,eye(len(A)))])[0]]
def norm(A,n):
 B=eye(4);out=[[0]*4 for _ in range(4)]
 for _ in range(n):out=add(out,B);B=mm(B,A)
 return out
A1=[[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]]
A2=[[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]]
PV=[[-2,1,0,1],[-6,0,-1,0],[0,-1,0,0],[-1,0,0,0]]
QE=[[-2,1,0,-2],[-1,0,0,0],[3,-1,1,0],[0,0,0,1]]
PE=[[0,-2,-1,-2],[2,-1,0,-1],[0,2,1,3],[-1,0,0,0]]
V0=[[1,-1,0,2],[0,-1,-1,6],[0,1,0,0],[0,0,0,1]]
V1=[[1,0,1,-3],[0,0,1,0],[0,-1,0,6],[0,0,0,1]]
assert det(PV)==-1 and det(QE)==1 and mm(QE,PV)==PE
assert mm(V0,PV)==mm(PV,A1) and mm(V1,PV)==mm(PV,A2)
delta=[0,0,0,1];eps=[1,2,-4,0];epsp=[1,3,-3,0]
images=[mv(PV,v) for v in [delta,eps,epsp]]
assert images==[[1,0,0,0],[0,-2,-2,-1],[1,-3,-3,-1]]
N3,N4=norm(A1,3),norm(A2,4)
assert N3==[[3,0,0,0],[6,0,0,0],[-12,0,0,0],[0,2,1,3]]
assert N4==[[4,0,0,0],[12,0,0,0],[-12,0,0,0],[0,2,2,4]]
Y1=[[0,0],[1,0],[0,1],[F(-2,3),F(-1,3)]];B1=[[0,0],[F(2,3),F(1,3)],[F(-1,3),F(1,3)],[0,0]]
Y2=[[0,0],[1,0],[0,1],[F(-1,2),F(-1,2)]];B2=[[0,0],[F(1,2),F(-1,2)],[F(1,2),F(1,2)],[0,0]]
assert mm(add(eye(4),neg(A1)),B1)==Y1 and mm(add(eye(4),neg(A2)),B2)==Y2
assert mm(N3,Y1)==[[0,0]]*4 and mm(N4,Y2)==[[0,0]]*4
A0=inv(mm(A1,A2));adj=mv(neg(A0),[0,1,-2,0]);assert adj==[0,-1,1,0]
# Solve all entrywise commutator equations for the rational centralizer.
eq=[]
for A in [A1,A2]:
 for i in range(4):
  for j in range(4):
   row=[F(0)]*16
   for h in range(4):row[i*4+h]+=A[h][j];row[h*4+j]-=A[i][h]
   eq.append(row)
_,piv=rref(eq);assert len(piv)==14
E=[[0]*4 for _ in range(4)];E[3][0]=1
assert mm(E,A1)==mm(A1,E) and mm(E,A2)==mm(A2,E)
# Repeated norms, explicit ell-solutions, and CRT cycles on all coprime pairs <=20.
pairs=[];total_residues=0
for k in range(1,21):
 for l in range(1,21):
  m,n=3*k,4*l
  if gcd(m,n)!=1:continue
  assert norm(A1,m)==[[k*v for v in row] for row in N3]
  assert norm(A2,n)==[[l*v for v in row] for row in N4]
  N0=pow(n,-1,m);N1=(1-n*N0)//m
  assert n*N0+m*N1==1 and gcd(N0,m)==gcd(N1,n)==1
  residues={(h*N0%k,h*N1%(2*l)) for h in range(2*k*l)}
  assert len(residues)==2*k*l and gcd(k,2*l)==1
  # Generic divisibility data dr1=m*a, dr2=n*b, ds1=k*c, ds2=2l*d.
  for a,b,c,d in [(2,-3,5,-7),(-1,4,-6,8),(0,0,0,0)]:
   d1=[m*a,m*a*2,m*a*(-4),k*c];d2=[n*b,n*b*3,n*b*(-3),2*l*d]
   ell1=[-a,0,-c,0];ell2=[-b,-d,0,0]
   assert mv(norm(A1,m),ell1)==[-v for v in d1]
   assert mv(norm(A2,n),ell2)==[-v for v in d2]
  total_residues+=2*k*l;pairs.append([k,l,2*k*l])
summary={'all_assertions_passed':True,'det_PV':det(PV),'det_QE':det(QE),'PV_inverse':[[str(x) for x in row] for row in inv(PV)],'QE_times_PV':PE,'two_intertwinings':True,'marked_vector_images':images,'N3':N3,'N4':N4,'centralizer_equation_rank':len(piv),'centralizer_dimension':2,'centralizer_basis':'I, E=deltahat tensor gamma','rational_norm_kernel_solutions_verified':True,'cusp_adjustment':list(map(str,adj)),'CRT_pairs_le20':len(pairs),'total_residue_states':total_residues,'all_CRT_orbit_lengths_correct':True,'scope':'Exact integer/Fraction matrix operations and direct finite group orbits, no retained program used. Global holomorphic gluing is checked separately in the comparison note.'}
(Pth/'output/S6_SERIES_PUBLISH_I_integral_dictionary_exact.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
