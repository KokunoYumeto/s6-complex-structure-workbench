"""Exact q-series identification through the Sturm bound4 for M12(Gamma0(3))."""
from fractions import Fraction as F
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[1];REC=ROOT/'records'
n=8
def mul(a,b):return [sum(a[i]*b[k-i] for i in range(k+1)) for k in range(n+1)]
def powser(a,k):
 b=[1]+[0]*n
 for _ in range(k):b=mul(b,a)
 return b
def sigma(k,m):return sum(d**k for d in range(1,m+1) if m%d==0)
E4=[1]+[240*sigma(3,j) for j in range(1,n+1)]
A=powser(E4,3);A3=[A[j//3] if j%3==0 else 0 for j in range(n+1)]
delta=[1]+[0]*n
for j in range(1,n+1):
 f=[0]*(n+1)
 for k in range(0,min(24,n//j)+1):f[k*j]=(-1)**k*int(s.binomial(24,k))
 delta=mul(delta,f)
delta=[0]+delta[:-1];delta3=[delta[j//3] if j%3==0 else 0 for j in range(n+1)]
eta=[1]+[0]*n
for d in [1,3]:
 for j in range(1,n//d+1):
  f=[0]*(n+1)
  for k in range(0,min(12,n//(d*j))+1):f[k*d*j]=(-1)**k*int(s.binomial(12,k))
  eta=mul(eta,f)
eta=[0,0]+eta[:-2]
cols=[A,A3,delta,delta3,eta];M=s.Matrix([[c[j] for c in cols] for j in range(5)])
b=s.Matrix([1,0,23058,1849032,44291124]);c=M.inv()*b
print('basis E4(tau)^3,E4(3tau)^3,Delta(tau),Delta(3tau),eta(tau)^12 eta(3tau)^12')
print('q0..q4 determinant',M.det())
print('coefficients',list(c))
print('predicted q0..q8',[sum(c[k]*cols[k][j] for k in range(5)) for j in range(n+1)])
