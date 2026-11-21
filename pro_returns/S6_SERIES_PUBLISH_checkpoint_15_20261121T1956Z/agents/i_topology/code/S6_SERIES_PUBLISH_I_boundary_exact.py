#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
from math import gcd,lcm
import json
P=Path(__file__).resolve().parents[1]
# Sparse polynomials in x,a,b,m,T,r,u,v,p,q; no symbolic library or retained code.
N=10
zero={}
def const(c):return {(0,)*N:F(c)} if c else {}
def var(i):
 e=[0]*N;e[i]=1;return {tuple(e):F(1)}
def add(a,b):
 c=a.copy()
 for e,v in b.items():c[e]=c.get(e,F(0))+v
 return {e:v for e,v in c.items() if v}
def scale(a,c):return {e:v*c for e,v in a.items() if v*c}
def mul(a,b):
 c={}
 for e,v in a.items():
  for f,w in b.items():
   g=tuple(x+y for x,y in zip(e,f));c[g]=c.get(g,F(0))+v*w
 return {e:v for e,v in c.items() if v}
def sq(a):return mul(a,a)
x,a,b,m,T,r,u,v,p,q=map(var,range(N))
mat=[[scale(a,6),x,const(1),zero],[scale(m,6),T,zero,zero],[b,a,zero,const(1)],[r,m,zero,zero]]
det={}
for s in permutations(range(4)):
 sign=(-1)**sum(s[i]>s[j] for i in range(4) for j in range(i+1,4));term=const(sign)
 for i in range(4):term=mul(term,mat[i][s[i]])
 det=add(det,term)
assert det==add(mul(T,r),scale(sq(m),-6))
# Clear denominator 2T^3 in the superharmonic identity for m^2/T.
derivative=add(add(mul(sq(T),add(sq(u),sq(v))),scale(mul(mul(m,T),add(mul(u,p),mul(v,q))),-2)),mul(sq(m),add(sq(p),sq(q))))
norm=add(sq(add(mul(T,u),scale(mul(m,p),-1))),sq(add(mul(T,v),scale(mul(m,q),-1))))
assert derivative==norm
coarse_h4=(-F(1))*((-F(3,2))**2)*(-1) # -pi^2 E4 * (-3 pi i/2)^2
coarse_eps2=coarse_h4*F(1,3)**2
assert coarse_h4==F(9,4) and coarse_eps2==F(1,4)
Hstar=[F(3),F(3)];H0=[F(6),F(3,2)];difference=[j-i for i,j in zip(Hstar,H0)]
assert difference==[F(3),F(-3,2)]
# Rational annihilator bases for exact coefficient representations of k.
def nullspace(M):
 A=[list(map(F,row)) for row in M];nr=len(A);nc=len(A[0]);pivot=[];i=0
 for j in range(nc):
  h=next((h for h in range(i,nr) if A[h][j]),None)
  if h is None:continue
  A[i],A[h]=A[h],A[i];d=A[i][j];A[i]=[x/d for x in A[i]]
  for h in range(nr):
   if h!=i:
    d=A[h][j];A[h]=[x-d*y for x,y in zip(A[h],A[i])]
  pivot.append(j);i+=1
  if i==nr:break
 out=[]
 for j in range(nc):
  if j in pivot:continue
  v=[F(0)]*nc;v[j]=1
  for h,k in enumerate(pivot):v[k]=-A[h][j]
  den=lcm(*(x.denominator for x in v));ints=[int(x*den) for x in v];g=0
  for z in ints:g=gcd(g,abs(z))
  out.append([z//g for z in ints])
 return out
cases={
 'rational':[ [1,F(1,2),F(1,3),F(1,5)] ],
 'one_quadratic':[[1,0,0,0],[0,1,0,0]],
 'two_independent_quadratics':[[1,0,0,0],[0,1,0,0],[0,0,1,0]],
 'full_biquadratic_basis':[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]}
ann={k:nullspace(M) for k,M in cases.items()};assert [len(v) for v in ann.values()]==[3,2,1,0]
for value in [F(7,3),F(-2,5),F(1001,997)]:
 for n in [1,2,7,31,100,997]:
  nearest=(value*n+F(1,2)).numerator//(value*n+F(1,2)).denominator
  assert abs(F(nearest,n)-value)<=F(1,2*n)
summary={'all_assertions_passed':True,'real_period_determinant':'T*r-6*m^2','superharmonic_identity':'2*T^3*ddbar(m^2/T) = (T*u-m*p)^2+(T*v-m*q)^2','coarse_h4_coefficient_after_pi4_E4':str(coarse_h4),'coarse_epsilon2_coefficient_after_pi4_E4':str(coarse_eps2),'pi_Hstar_log2_log3':list(map(str,Hstar)),'pi_H0_log2_log3':list(map(str,H0)),'pi_H0_minus_Hstar_log2_log3':list(map(str,difference)),'annihilator_integer_bases':ann,'Chabauty_example':'diag(1/n,1,1,1) Z4 -> R x Z3; nearest integer estimate <=1/(2n) verified, with general proof in note','not_recomputed':'ari:C.8.15 global critical/radial certificate; analytic value E4(i); these remain stated inputs.'}
(P/'output/S6_SERIES_PUBLISH_I_boundary_exact.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
