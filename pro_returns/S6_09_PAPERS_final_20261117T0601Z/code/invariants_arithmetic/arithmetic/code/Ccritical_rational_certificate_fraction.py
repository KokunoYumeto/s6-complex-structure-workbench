"""Exact integer/rational interval audit of the finite scalar coefficients.

Every interval endpoint has denominator 10^100. Each arithmetic operation
rounds outwards using integer division. This checks one finite coefficient
identity, not a cover or enumeration of points of the modular domain.
The analytic remainder bounds are printed in Ccritical_certificate.py.
"""
from fractions import Fraction as FQ # portability: exact rational arithmetic, no mathematical change
from fractions import Fraction
def fmpq(a=0,b=None):
 if b is not None:return FQ(a,b)
 if isinstance(a,str) and "." in a:
  a=Fraction(a);return FQ(a.numerator,a.denominator)
 return FQ(a)
import json
from pathlib import Path
D=10**100
class I:
 def __init__(self,a=0,b=None,raw=False):
  if raw:self.l,self.h=a,b;return
  if isinstance(a,I):self.l,self.h=a.l,a.h;return
  a=fmpq(a);self.l=int(a.numerator)*D//int(a.denominator);self.h=-((-int(a.numerator)*D)//int(a.denominator))
  if b is not None:self.h=I(b).h
 def __add__(a,b):
  b=I(b);return I(a.l+b.l,a.h+b.h,True)
 __radd__=__add__
 def __neg__(a):return I(-a.h,-a.l,True)
 def __sub__(a,b):return a+-I(b)
 def __rsub__(a,b):return I(b)+-a
 def __mul__(a,b):
  b=I(b);ss=[a.l*b.l,a.l*b.h,a.h*b.l,a.h*b.h];return I(min(ss)//D,-((-max(ss))//D),True)
 __rmul__=__mul__
 def __truediv__(a,b):
  b=I(b);assert not b.l<=0<=b.h
  if b.h<0:return -a/-b
  inv=I(D*D//b.h,-((-D*D)//b.l),True);return a*inv
 def __rtruediv__(a,b):return I(b)/a
 def __pow__(a,n):
  if n<0:return 1/(a**-n)
  z=I(1)
  while n:
   if n%2:z=z*a
   a=a*a;n//=2
  return z
 def __abs__(a):
  if a.l>=0:return a
  if a.h<=0:return -a
  return I(0,max(-a.l,a.h),True)
 def __lt__(a,b):return a.h<I(b).l
 def __gt__(a,b):return a.l>I(b).h
 def show(a,nd=30):
  def fmt(n):
   sign='-' if n<0 else '';n=abs(n);s=str(n//D)+'.'+str(n%D).zfill(100)[:nd];return sign+s
  return '['+fmt(a.l)+', '+fmt(a.h)+']'

def atan_inv(n,M=100):
 x=I(fmpq(1,n));s=I(0)
 for j in range(M):s+=(-1)**j*x**(2*j+1)/(2*j+1)
 e=x**(2*M+1)/(2*M+1)
 return I(s.l-e.h,s.h+e.h,True)
def exp_pos(x,M=160):
 term=I(1);s=term
 for j in range(1,M+1):term=term*x/j;s+=term
 e=term*x/(M+1)/(1-x/(M+2));return I(s.l,s.h+e.h,True)
pi=16*atan_inv(5)-4*atan_inv(239)
from math import isqrt
sqi=isqrt(3*D*D);assert sqi*sqi<=3*D*D<(sqi+1)**2
sq=I(sqi,sqi+1,True)
assert fmpq('1.73205080756887729352744634150587236694280525381038')**2<3<fmpq('1.73205080756887729352744634150587236694280525381039')**2
q=1/exp_pos(2*pi)
A=1+240*sum((n**3*q**n/(1-q**n) for n in range(1,50)),I(0));tail=240*(4*q)**50/((1-4*q)*(1-q));A=I(A.l,A.h+tail.h,True)
k=pi*pi*A;r0=2-sq;z0=k*r0*r0;cc=1-1/sq
print('pi',pi.show(70));print('z0',z0.show(60));assert k>14 and k<fmpq(72,5)
assert z0>I('1.0315619043558156493568263343177356527388253980203')
assert z0<I('1.0315619043558156493568263343177356527388253980205')
root=Path(__file__).resolve().parents[1];dat=json.loads((root/'records/Ccritical_certificate.json').read_text())
B=[fmpq(v) for v in dat['B']];J=[fmpq(v) for v in dat['J']];H=[fmpq(v) for v in dat['H']];M=100
# All coefficients in this file are rechecked from exact modular ODE recurrence.
N=2*M+2;zz=fmpq(0);aa=[zz]*(N+1);bb=aa.copy();ccc=aa.copy();bb[0]=fmpq(1)
cv=lambda a,b,n:sum((a[j]*b[n-j] for j in range(n+1)),zz)
for n in range(N):
 aa[n+1]=(bb[n]-cv(aa,aa,n))/(3*(n+1));bb[n+1]=fmpq(4,3)*(ccc[n]-cv(aa,bb,n))/(n+1);ccc[n+1]=2*(cv(bb,bb,n)-cv(aa,ccc,n))/(n+1)
assert B==[bb[2*j] for j in range(M+1)] and J==[ccc[2*j+1]/2 for j in range(M+1)]
def power(a,p):
 v=[fmpq(1)]+[zz]*M
 for n in range(1,M+1):v[n]=sum((((p+1)*j-n)*a[j]*v[n-j] for j in range(1,n+1)),zz)/n
 return v
def mult(a,b):return [cv(a,b,n) for n in range(M+1)]
B3=mult(mult(B,B),B);J2=mult(J,J);DD=mult([B3[n]-(4*J2[n-1] if n else 0) for n in range(M+1)],power(J,fmpq(-3,2)))
assert H==[-DD[n]/(16*n*n-1) for n in range(M+1)]
Q=power(J,fmpq(1,2));S=mult(Q,H);T=mult(Q,[(1+4*n)*H[n] for n in range(M+1)])
C=[I(1)]+[I(0)]*M;AA=[I(T[0])-cc*I(S[0])]+[I(0)]*M
for n in range(1,M+1):C[n]=I(B[n])-C[n-1]/z0;AA[n]=I(T[n])-cc*I(S[n])-AA[n-1]/z0
ic=[I(1)]+[I(0)]*M
for n in range(1,M+1):ic[n]=-sum((C[j]*ic[n-j] for j in range(1,n+1)),I(0))
def imult(a,b):return [sum((a[j]*b[n-j] for j in range(n+1)),I(0)) for n in range(M+1)]
AC=imult(AA,ic);QC=imult([I(v) for v in Q],ic)
R=I(fmpq(3,2));Ro=I(fmpq(12,5));s=R/Ro;K=60
bt=400*s**K/(1-s);jt=3000*s**K/(1-s);ct=400*z0/(Ro-z0)*s**K/(1-s)
bn=sum((abs(I(B[n]))*R**n for n in range(K)),I(0))+bt
jn=sum((abs(I(J[n]))*R**n for n in range(K)),I(0))+jt
cn=sum((abs(C[n])*R**n for n in range(1,K)),I(0))+ct
jl=1-I(J[2])*R*R-I(J[1])**2/(8*I(J[2]))-sum((abs(I(J[n]))*R**n for n in range(3,K)),I(0))-jt
assert bn<fmpq(3276,1000) and jn<fmpq(2411,1000) and cn<fmpq(335,1000) and jl>fmpq(2049,10000)
print('outer finite certificates',*[v.show() for v in [bn,jn,cn,jl]])
s=z0/I(fmpq(7,5));act=10000*s**M/(1-s);qct=3*s**M/(1-s);ht=110*s**M/(1-s);hpt=110/z0*s**M*(M/(1-s)+s/(1-s)**2)
n1=(sum((abs(AC[n])*z0**n for n in range(1,M)),I(0))+act)/z0
n2=(sum((abs(QC[n])*z0**n for n in range(1,M)),I(0))+qct)/z0
n3=(sum((abs(I(H[n]))*z0**n for n in range(1,M)),I(0))+ht)/z0
n4=sum((n*abs(I(H[n]))*z0**(n-1) for n in range(1,M)),I(0))+hpt
for name,v,bd in [('AC',n1,fmpq(635,10000)),('QC',n2,fmpq(1368,10000)),('H',n3,fmpq(1115,10000)),('Hprime',n4,fmpq(1293,10000))]:print(name,v.show(60),'<',bd);assert v<bd
print('ALL INTEGER/RATIONAL INEQUALITIES PASSED')
