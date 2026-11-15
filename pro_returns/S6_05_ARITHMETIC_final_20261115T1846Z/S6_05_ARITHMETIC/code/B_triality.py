"""Rational triality lifts for the octonion convention of Wilson."""
from fractions import Fraction as F
from math import gcd,isqrt,lcm
from pathlib import Path
import json
from flint import fmpz_mat,fmpq_mat
ROOT=Path(__file__).resolve().parents[1];REC=ROOT/'records'
TAB={}
for i in range(8):TAB[0,i]=(1,i);TAB[i,0]=(1,i)
for i in range(1,8):TAB[i,i]=(-1,0)
for t in range(7):
 a,b,c=t+1,(t+1)%7+1,(t+3)%7+1
 for x,y,z in [(a,b,c),(b,c,a),(c,a,b)]:TAB[x,y]=(1,z);TAB[y,x]=(-1,z)
assert len(TAB)==64
def mul(a,b):
 out=[F(0)]*8
 for i,x in enumerate(a):
  for j,y in enumerate(b):
   s,k=TAB[i,j];out[k]+=s*x*y
 return out
E=[[F(int(i==j)) for j in range(8)] for i in range(8)]
def matrix_cols(cols):return fmpq_mat([[str(cols[j][i]) for j in range(8)] for i in range(8)])
def R(a):return matrix_cols([mul(e,a) for e in E])
def L(a):return matrix_cols([mul(a,e) for e in E])
CONJ=fmpq_mat([[int(i==j)*(1 if i==0 else -1) for j in range(8)] for i in range(8)])
def entries(A):return [[F(str(A[i,j])) for j in range(A.ncols())] for i in range(A.nrows())]
def lift(A):
 aa=entries(A);a=[aa[i][0] for i in range(8)];la=entries(L(a));eq=[]
 for i in range(8):
  ai=[aa[k][i] for k in range(8)];left=entries(L(ai))
  for j in range(8):
   sign,k=TAB[i,j]
   for z in range(8):
    row=[F(0)]*64
    for t in range(8):row[t*8+j]+=left[z][t];row[t*8+k]-=sign*la[z][t]
    d=lcm(*(x.denominator for x in row));eq.append([int(x*d) for x in row])
 H,dim=fmpz_mat(eq).nullspace();assert dim==1
 v=[int(H[i,0]) for i in range(64)];gg=gcd(*v);v=[x//gg for x in v]
 B=fmpq_mat([v[i*8:(i+1)*8] for i in range(8)]);norm=B.transpose()*B
 k=F(str(norm[0,0]));assert norm==fmpq_mat([[str(k*int(i==j)) for j in range(8)] for i in range(8)])
 sn=isqrt(k.numerator);sd=isqrt(k.denominator)
 if sn*sn!=k.numerator or sd*sd!=k.denominator:return None,k
 B=B*sd/sn;D=L(a)*B;C=CONJ*D*CONJ
 assert B.transpose()*B==fmpq_mat([[int(i==j) for j in range(8)] for i in range(8)])
 return (B,C),k
if __name__=='__main__':
 gs=[]
 for i in range(1,8):gs.append((f'R{i}',R(E[i])))
 p=E[0].copy();p[1]=-1
 for i in range(2,8):
  q=E[0].copy();q[i]=1;gs.append((f'Q{i}',R(q)*R(p)/2))
 out=[]
 for name,A in gs:
  bc,k=lift(A);print(name,'rational',bc is not None,'unscaled_norm',k,flush=True)
  if bc is not None:
   B,C=bc;out.append({'name':name,'A':[[str(x) for x in row] for row in entries(A)],'B':[[str(x) for x in row] for row in entries(B)],'C':[[str(x) for x in row] for row in entries(C)]})
 (REC/'B_triality_lifts.json').write_text(json.dumps(out))
