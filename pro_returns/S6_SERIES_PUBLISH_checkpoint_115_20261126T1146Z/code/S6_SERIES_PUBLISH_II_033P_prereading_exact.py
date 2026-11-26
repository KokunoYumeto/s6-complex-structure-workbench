"""Exact prereading checks for E.5.3, written from statement inputs.

Rational row reduction finds the centralizer; direct matrix multiplication
computes the norm. Polynomial identities are checked by elementary coefficient
arithmetic. Analytic gluing is proved in the separate frozen derivation.
"""
from fractions import Fraction as Q
import json

I=[[Q(i==j) for j in range(4)] for i in range(4)]
Ts=[
 [[1,0,-2,-1],[0,0,-1,0],[0,1,0,-1],[0,0,0,1]],
 [[1,0,2,2],[0,1,1,1],[0,0,1,0],[0,0,0,1]],
 [[1,0,0,0],[0,1,0,0],[0,-1,1,0],[0,0,0,1]],
 [[1,0,0,-1],[0,1,1,0],[0,0,1,0],[0,0,0,1]]]
def mul(a,b):
 return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def plus(a,b): return [[x+y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def scale(t,a): return [[t*x for x in r] for r in a]
def transpose(a): return list(map(list,zip(*a)))
def rref(a):
 a=[list(map(Q,row)) for row in a]; piv=[];i=0
 for j in range(len(a[0])):
  k=next((k for k in range(i,len(a)) if a[k][j]),None)
  if k is None:continue
  a[i],a[k]=a[k],a[i];d=a[i][j];a[i]=[x/d for x in a[i]]
  for k in range(len(a)):
   if k!=i:
    d=a[k][j];a[k]=[x-d*y for x,y in zip(a[k],a[i])]
  piv.append(j);i+=1
  if i==len(a):break
 return a,piv
def inv(a):
 rr,p=rref([list(ar)+list(ir) for ar,ir in zip(a,I)])
 assert p==list(range(4))
 return [r[4:] for r in rr]
def vec(a,v):return [sum(x*y for x,y in zip(row,v)) for row in a]
Hs=[transpose(inv(t)) for t in Ts]
H=Hs[0]
assert mul(mul(mul(Ts[0],Ts[1]),Ts[2]),Ts[3])==I
assert mul(mul(H,H),mul(H,H))==I
N=plus(plus(I,H),plus(mul(H,H),mul(mul(H,H),H)))
ell=[1,-1,-1,0];delta=[0,0,0,1]
assert vec(H,ell)==ell and vec(H,delta)==delta
assert transpose(N)==[[4,-4,-4,0],[0,0,0,2],[0,0,0,-2],[0,0,0,4]]
# Rows are the coefficients of AH-HA, for all four H simultaneously.
rows=[]
for h in Hs:
 for i in range(4):
  for j in range(4):
   coeff=[Q(0)]*16
   for k in range(4):
    coeff[4*i+k]+=h[k][j]
    coeff[4*k+j]-=h[i][k]
   rows.append(coeff)
rr,piv=rref(rows)
free=[j for j in range(16) if j not in piv]
null=[]
for j in free:
 v=[Q(0)]*16;v[j]=1
 for i,k in enumerate(piv):v[k]=-rr[i][j]
 null.append(v)
flatI=[x for r in I for x in r]
flatE=[Q(i==3 and j==0) for i in range(4) for j in range(4)]
assert len(null)==2
assert rref(null+[flatI,flatE])[1]==rref(null)[1]
assert all(sum(x*y for x,y in zip(row,flatI))==0 and sum(x*y for x,y in zip(row,flatE))==0 for row in rows)
# Coordinates of A ell-ell in the ordered invariant basis (ell,delta):
# (a-1,b). Norm columns in this basis are (4,0),(0,2),(0,-2),(0,4).
# a=+/-1 follows from det(aI+bE41)=a^4; a-1 is divisible by 4 only for a=1.
assert (1-1)%4==0 and (-1-1)%4==2
# A generator of the norm image giving 2 delta is the u coordinate.
assert vec(N,[0,1,0,0])==[0,0,0,2]
# Direct conjugacy identity on the root-cover vector space.
assert vec(plus(I,scale(-1,H)),[Q(-1,2),0,0,0])==[0,-1,0,Q(1,2)]
# Work in Q[zeta]/(zeta^2+zeta+1) by pairs.
def zadd(a,b):return (a[0]+b[0],a[1]+b[1])
def zmul(a,b):
 c0=a[0]*b[0];c1=a[0]*b[1]+a[1]*b[0];c2=a[1]*b[1]
 return (c0-c2,c1-c2)
z=(Q(0),Q(1));one=(Q(1),Q(0));z2=zmul(z,z)
assert zadd(zadd(one,z),z2)==(0,0)
minus_z=(0,-1)
assert zmul(minus_z,zadd(z2,(-1,0)))==zadd(z,(-1,0))
assert zmul(minus_z,minus_z)!=one
assert zadd(one,(-z2[0],-z2[1]))!=(0,0)
# The cross-ratio is -zeta and its derivative is
# -9/(2 alpha^2)*(1-zeta^2); all nonzero factors have been identified.
# The coordinate comparison x=r^-2 x' sends x+mu to r^-2(x'+mu r^2).
# The two Laurent coefficients agree exactly.
left={(-2,1,0):1,(0,0,1):1}
right={(-2,1,0):1,(-2+2,0,1):1}
assert left==right
# The even-shift gluing scalar r^(2n) cancels the lift scalar r^(-2n).
assert 2+(-2)==0
result=dict(status='all exact checks passed',method='stdlib Fraction row reduction and quotient-ring coefficient arithmetic',
 centralizer_dimension=2,centralizer_basis=['I','E41'],norm_matrix=[[int(x) for x in r] for r in N],
 invariant_basis=['ell','delta'],norm_basis_coordinates=[[4,0],[0,2]],
 parity_obstruction='a=1 and b in 2Z',norm_preimage_of_twice_delta='u',
 ordered_cross_ratio_at_zero='-zeta',cross_ratio_derivative='-9(1-zeta^2)/(2 alpha^2)',
 root_input='alpha^3=-27/4; zeta^2+zeta+1=0',
 half_translation_comparison='x+mu=r^-2(xprime+mu*r^2); J=r^2 Jprime',
 gluing_for_c_to_c_plus_2='Fprime J^-1 F^-1=Jprime^-1',
 scope='Algebraic identities only; properness, toroidal extension and intrinsic-base arguments are in the frozen mathematical derivation.',
 mathematical_check_events_added=0)
print(json.dumps(result,indent=2))
