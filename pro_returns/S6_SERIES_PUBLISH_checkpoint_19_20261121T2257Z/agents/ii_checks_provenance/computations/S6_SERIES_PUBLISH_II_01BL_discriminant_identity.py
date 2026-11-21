"""Fresh exact coefficient/Bézout checks for the Weierstrass example."""
from fractions import Fraction as Q
import json
def add(a,b):
 out=dict(a)
 for k,v in b.items():out[k]=out.get(k,Q(0))+v
 return {k:v for k,v in out.items() if v}
def mul(a,b):
 out={}
 for i,c in a.items():
  for j,d in b.items():out[i+j]=out.get(i+j,Q(0))+c*d
 return {k:v for k,v in out.items() if v}
def sc(a,n):return {k:n*v for k,v in a.items() if n*v}
def ev(a,x):return sum(v*x**k for k,v in a.items())
A={4:Q(1),0:Q(1)};B={6:Q(1)}
D=add(sc(mul(mul(A,A),A),4),sc(mul(B,B),27))
assert D=={12:Q(31),8:Q(12),4:Q(12),0:Q(4)}
P={3:Q(31),2:Q(12),1:Q(12),0:Q(4)}
dP={k-1:k*v for k,v in P.items() if k}
identity=add(sc(P,3),sc(mul({1:Q(1)},dP),-1))
assert identity=={2:Q(12),1:Q(24),0:Q(12)}
assert ev(dP,-1)==81 and ev(P,0)==4 and ev(P,-1)==-27
# Eliminate q using q=(1+lambda)/(1-lambda) and q^2=2/3.
plus={0:Q(1),1:Q(1)};minus={0:Q(1),1:Q(-1)}
lam=add(sc(mul(plus,plus),3),sc(mul(minus,minus),-2))
assert lam=={2:Q(1),1:Q(10),0:Q(1)}
assert ev(lam,1)==12 and ev(lam,-1)==-8
print(json.dumps({'method':'exact sparse rational coefficient convolution and a direct common-root identity; no numerical roots or gcd routine',
 'discriminant_coefficients':{str(k):str(v) for k,v in sorted(D.items())},
 'squarefreeness_certificate':'3P(u)-uPprime(u)=12(u+1)^2; Pprime(-1)=81; P(0)=4',
 'no_cusp_certificate':'P(-1)=-27, so A=t^4+1 does not vanish at a discriminant root',
 'infinity_discriminant':31,'singular_fibre_count':12,
 'nodal_gluing_polynomial':'lambda^2+10lambda+1',
 'non_torsion_reason':'Its two roots are negative real numbers different from -1 and 1; neither is a root of unity.',
 'all_assertions_passed':True},indent=2))
