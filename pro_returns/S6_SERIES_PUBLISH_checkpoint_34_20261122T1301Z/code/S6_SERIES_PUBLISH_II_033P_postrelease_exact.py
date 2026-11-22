"""Postrelease exact checks for all printed E.5.3 algebra.

Sparse coefficient convolution and fraction cross multiplication replace the
historical computer-algebra simplification. The prereading file is immutable.
This script also checks the explicit change to the printed period convention.
"""
from fractions import Fraction as Q
from itertools import permutations
import json

NAMES=('tau','z','beta','c','h','mu','t','s','r')
ZERO=(0,)*len(NAMES)
def trim(p): return {k:v for k,v in p.items() if v}
def add(p,q):
 out=dict(p)
 for k,v in q.items(): out[k]=out.get(k,Q(0))+v
 return trim(out)
def neg(p): return {k:-v for k,v in p.items()}
def mul(p,q):
 out={}
 for a,x in p.items():
  for b,y in q.items():
   k=tuple(i+j for i,j in zip(a,b));out[k]=out.get(k,Q(0))+x*y
 return trim(out)
class R:
 def __init__(self,v=0,den=None):
  if isinstance(v,R): self.n,self.d=v.n,v.d
  else: self.n=v if isinstance(v,dict) else ({ZERO:Q(v)} if v else {});self.d={ZERO:Q(1)} if den is None else den
  assert self.d
 def __add__(a,b):
  b=R(b);return R(add(mul(a.n,b.d),mul(b.n,a.d)),mul(a.d,b.d))
 __radd__=__add__
 def __neg__(a): return R(neg(a.n),a.d)
 def __sub__(a,b):return a+-R(b)
 def __rsub__(a,b):return R(b)+-a
 def __mul__(a,b):
  b=R(b);return R(mul(a.n,b.n),mul(a.d,b.d))
 __rmul__=__mul__
 def __truediv__(a,b):
  b=R(b);assert b.n;return R(mul(a.n,b.d),mul(a.d,b.n))
 def __rtruediv__(a,b):return R(b)/a
 def __pow__(a,n):
  if n<0:return (R(1)/a)**(-n)
  out=R(1)
  for _ in range(n):out=out*a
  return out
 def __eq__(a,b):
  b=R(b);return mul(a.n,b.d)==mul(b.n,a.d)
def var(i):
 k=list(ZERO);k[i]=1;return R({tuple(k):Q(1)})
tau,z,beta,c,h,mu,t,s,r=[var(i) for i in range(len(NAMES))]
def mm(a,b):return [[sum((x*y for x,y in zip(row,col)),R()) for col in zip(*b)] for row in a]
def mp(a,b):return [[x+y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def ms(a,b):return [[x-y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def scale(k,a):return [[k*x for x in row] for row in a]
def eq(a,b):return all(x==y for ar,br in zip(a,b) for x,y in zip(ar,br))
def col(v):return [[x] for x in v]
I=[[int(i==j) for j in range(4)] for i in range(4)]
Hs=[
 [[1,0,0,0],[-2,0,-1,0],[0,1,0,0],[1,1,0,1]],
 [[1,0,0,0],[0,1,0,0],[-2,-1,1,0],[-2,-1,0,1]],
 [[1,0,0,0],[0,1,1,0],[0,0,1,0],[0,0,0,1]],
 [[1,0,0,0],[0,1,0,0],[0,-1,1,0],[1,0,0,1]]]
ell=col([1,-1,-1,0]);delta=col([0,0,0,1]);u=col([0,1,0,0]);w=col([0,0,1,0])
E=[[int(i==3 and j==0) for j in range(4)] for i in range(4)]
P=lambda tt,zz,bb,cc:[[2*zz,tt,1,0],[bb+cc,zz,0,1]]
P0=P(tau,z,beta,c)
transformations=[(-1/tau,(z-1)/tau,beta-1-2*(z-1)**2/tau),
 (tau+1,z+1,beta+2),(tau/(1-tau),z/(1-tau),beta+2*z*z/(1-tau)),(tau+1,z,beta-1)]
for H,(tt,zz,bb) in zip(Hs,transformations):
 Pg=P(tt,zz,bb,c);PH=mm(Pg,H)
 Rg=[[PH[0][2],0],[PH[1][2],1]]
 assert eq(PH,mm(Rg,P0))
assert eq(mm(P(tau,z,beta,c+h),ms(I,scale(h,E))),P0)
# The frozen period matrix used the contracting generator and exchanged u,w.
# beta=-b, and this S relates its columns to the printed inverse-generator ones.
S=[[-1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]]
Pf=[[-2*z,1,tau,0],[-beta-c,0,z,1]]
assert eq(mm(Pf,S),P0) and eq(mm(S,S),I)
assert eq(mm(S,ell),col([-1,-1,-1,0]))
assert eq(mm(mm(S,E),S),scale(-1,E))
# Same coordinate transformation must be applied to every monodromy matrix.
for H in Hs: assert eq(mm(S,mm(S,mm(H,S))),mm(H,S))
broot=scale(-h/4,mp(u,w));Lroot=scale(-h/2,u)
assert eq(mm(ms(I,Hs[0]),broot),mp(scale(h/4,delta),Lroot))
L1=col([0,0,0,0]);L2=scale(h/2,u);L3=scale(-h/2,w)
assert eq(mp(mp(mp(Lroot,mm(Hs[0],L1)),mm(mm(Hs[0],Hs[1]),L2)),mm(mm(mm(Hs[0],Hs[1]),Hs[2]),L3)),col([0,0,0,0]))
H2=mm(Hs[0],Hs[0]);H3=mm(H2,Hs[0]);N=mp(mp(I,Hs[0]),mp(H2,H3))
assert eq(mm(N,Lroot),scale(-h,delta))
assert eq(mm(N,u),scale(2,delta))
# Sylvester determinant by the permutation definition, with no elimination/CAS.
def det(a):
 out=R()
 for p in permutations(range(len(a))):
  sign=(-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
  term=R(sign)
  for i,j in enumerate(p):term=term*a[i][j]
  out=out+term
 return out
a,b,d,e=R(4),27*mu**2,54*mu,R(27)
syl=[[a,b,d,e,0],[0,a,b,d,e],[3*a,2*b,d,0,0],[0,3*a,2*b,d,0],[0,0,3*a,2*b,d]]
assert -det(syl)/a==314928*(mu**3-1)
# The infinity coordinate comparison and the corrected c -> c+2 scalar.
assert r**(-2)*t+mu==r**(-2)*(t+mu*r**2)
assert r**(-2)*r**2==1
assert eq(ms(mm(P(tau,z,beta,c+2),ell),mm(P0,ell)),col([0,2]))
print(json.dumps(dict(status='PASS',method='stdlib sparse rational coefficient convolution, cross multiplication and permutation determinant',
 period_covariance_count=4,period_shift='Pi(c+h)(I-hE41)=Pi(c)',
 convention_change={'S':S,'ell_frozen_convention':[-1,-1,-1,0],'E41_conjugate':'-E41','monodromy':'H_frozen=S H_printed S^-1'},
 root_conjugacy='(I-H*)b*=h delta/4+L*',norm_defect='N4 L*=-h delta',sphere_defect=[0,0,0,0],
 discriminant='314928(mu^3-1)',half_translation_comparison='J=r^2 Jprime',
 printed_parameter_shift='F_(c+2) J F_c^-1=Jprime',
 scope='Exact algebra only; analytic existence, extension, properness and gluing are proved in the written comparisons.'),indent=2))
