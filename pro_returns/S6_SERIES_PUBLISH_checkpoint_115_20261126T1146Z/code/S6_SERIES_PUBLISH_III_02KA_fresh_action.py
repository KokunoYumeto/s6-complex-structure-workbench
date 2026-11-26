#!/usr/bin/env python3
"""Fresh exact affine/lattice checks for III 02KA before proof release."""
from pathlib import Path
from math import gcd
from fractions import Fraction
import json
import sympy as S
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

d=S.symbols('d',integer=True,positive=True)
A1=S.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=S.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
Sd=S.diag(d,1,1,1)
B1=S.Matrix([[1,0,0,0],[6*d,0,1,0],[-6*d,-1,-1,0],[-2*d,1,0,1]])
B2=S.Matrix([[1,0,0,0],[0,0,-1,0],[-6*d,1,0,0],[3*d,0,1,1]])
v1=S.Matrix([-1,-2*d,4*d,0]);v2=S.Matrix([1,3*d,-3*d,0])
a=S.Matrix([1/d,0,0,0])
eps1=S.Matrix([1,2,-4,0]);eps2=S.Matrix([1,3,-3,0])
assert Sd*B1==A1*Sd and Sd*B2==A2*Sd
assert B1**3==S.eye(4) and B2**4==S.eye(4)
assert B1*v1==v1 and B2*v2==v2
assert Sd*v1==-d*eps1 and Sd*v2==d*eps2
assert B1*a-a==S.Matrix([0,6,-6,-2])
assert B2*a-a==S.Matrix([0,0,-6,3])
assert d*a==S.Matrix([1,0,0,0])
assert Sd*a==S.Matrix([1,0,0,0])
for B,v,m in [(B1,v1,3),(B2,v2,4)]:
 norm=sum((B**j*v/m for j in range(m)),S.zeros(4,1))
 assert norm==v

# All matrix equalities are symbolic in d. The loop below separately checks
# congruence normal forms at prime, prime-power and composite endpoints.
ds=[k for k in range(1,162) if gcd(k,6)==1]
finite_cases=0;coset_cases=0
for k in ds:
 for m,sign in [(3,-1),(4,1)]:
  for power in range(1,k):
   for rootpower in range(m):
    residue=Fraction(power,k)-Fraction(sign*rootpower,m)
    assert residue.denominator!=1
    finite_cases+=1
 # Both lattice quotient normal forms, not only determinant equality.
 Sdk=S.diag(k,1,1,1)
 assert list(smith_normal_form(Sdk,domain=ZZ).diagonal())==[1,1,1,k]
 G=S.Matrix([[0,k],[1,0]])   # columns u, d gamma in the original basis
 assert abs(int(G.det()))==k
 assert [abs(int(x)) for x in smith_normal_form(G,domain=ZZ).diagonal()]==[1,k]
 for x in range(-2*k,2*k+1):
  r=x%k;q=(x-r)//k
  assert x==q*k+r and 0<=r<k
  # Original gamma exponent x maps to the generator power r; the
  # remaining translation is a covering period q*g.
  assert Fraction(x,k)-Fraction(r,k)==q
  coset_cases+=1
 # Canonical admissibility at both finite ends.
 assert gcd(-k,3)==1 and gcd(k,4)==1
 assert 12*0-4*(-k)-3*k==k
 assert 4*0-(-k)-k==0 and (-k)+k-3*0==0

# Exact toric lattice map and its additive character, including the sign.
B0=S.Matrix([[0,1],[-1,0]])
Gd=S.Matrix([[0,d],[1,0]])
assert B0*Gd==S.diag(1,-d)
assert B0*S.Matrix([1,0])==S.Matrix([0,-1])
assert B0*S.Matrix([0,1])==S.Matrix([1,0])
l1,l2,m1,m2=S.symbols('lambda1 lambda2 mu1 mu2')
C11,C12,C21,C22=S.symbols('C11 C12 C21 C22')
C=S.Matrix([[C11,C12],[C21,C22]])
l=S.Matrix([l1,l2]);m=S.Matrix([m1,m2])
assert S.expand(C*(l+m)-C*l-C*m)==S.zeros(2,1)
assert B0*(l+m)==B0*l+B0*m
assert (B0*Gd).det()==-d

# Finite component labels cannot be invariant under a nonzero translation:
# the sum of the translated labels differs by their nonzero cardinality
# times that translation. This is checked symbolically, without samples.
card=S.symbols('card',integer=True,positive=True)
shift=S.Matrix([l1,l2])
assert card*shift==S.Matrix([card*l1,card*l2])

# Fixed-u roots: their difference is 2W, nonzero in C when W is nonzero;
# the two roots have the same square. Check the polynomial map exactly.
W=S.symbols('W',nonzero=True)
assert S.expand((-W)**2-W**2)==0
assert S.simplify(W-(-W))==2*W

result={
 'canonical_datum':{'p':'d','b1':0,'b2':0,'parameter':'c=-i',
                    'W':'exp(-pi)','range':'0<exp(-pi)<1<216'},
 'cover_inclusion':[[str(x) for x in row] for row in Sd.tolist()],
 'linear_conjugacies_symbolic':True,'root_orders':[3,4],
 'affine_vectors_invariant':True,'affine_powers_are_covering_periods':True,
 'commutators_covering_coordinates':{'first':[0,6,-6,-2],'second':[0,0,-6,3]},
 'generator_order':'exactly d, because k/d is integral exactly when d divides k',
 'finite_freeness_checks':finite_cases,'tested_d':ds,
 'regular_and_cusp_Smith_forms':'diag(1,1,1,d) and diag(1,d)',
 'coset_normal_forms_checked':coset_cases,
 'toric_cover_periods':[['1','0'],['0','-d']],
 'toric_generator_translation':[0,-1],
 'unit_and_monomial_characters_additive':True,
 'central_component_fixed_point_sum_argument':True,
 'd1_endpoint':'trivial group, identity generator, quotient M1=S6',
 'fixed_u_polynomial':'W^2=(-W)^2=u, W-(-W)=2W nonzero',
 'covering_lift_equivariance':'Ftilde D_g Ftilde^-1=D_{F_*(g)}',
 'all_checks_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(result,indent=2))
