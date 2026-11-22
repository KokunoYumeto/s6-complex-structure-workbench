"""Exact finite checks for the auxiliary genus-one-torsor plumbing.

The charts and existence are proved in B.3.7.  This auxiliary family
has Euler24 and a multiple cusp; it is not the prescribed S6 family.
"""
from pathlib import Path
from fractions import Fraction
import json
import sympy as s

x=s.symbols('x')
# Holomorphic forms da/b^2, a da/b^2, da/b under sigma=(ia,omega b).
holomorphic_exponents=[(3-8)%12,(6-8)%12,(3-4)%12]
assert holomorphic_exponents==[7,10,11]
h1_exponents=sorted(holomorphic_exponents+[(-v)%12 for v in holomorphic_exponents])
assert h1_exponents==[1,2,5,7,10,11]
p=s.expand(s.cyclotomic_poly(12,x)*s.cyclotomic_poly(6,x))
q=x**5+x**2+x
assert p==x**6-x**5+x**3-x+1
assert p.subs(x,1)==1
assert s.expand(p+(1-x)*q)==1
print('H^(1,0)(C) deck exponents modulo12:',holomorphic_exponents)
print('H^1(C) characteristic polynomial:',p)
print('Integral inverse identity: p(x)+(1-x)*(x^5+x^2+x)=1.')
print('Thus (1-sigma*) is an automorphism of Pic0(C), inverse sigma*^5+sigma*^2+sigma*.')

heightP=2
translation_multiple=6
displacement_degree=heightP*translation_multiple
normal_degree=Fraction(displacement_degree,12)
assert displacement_degree==12 and normal_degree==1
print('M^2=-2; degree of M/(t_6P)^*M:',displacement_degree)
print('Degree of M/A^*M:',normal_degree)

n=12
eV=n
eR=2*eV
eNodal=n
eSmooth=eNodal+n
eNormalized=eR+n*(3-1)
eCentral=eNormalized-eV
eNearby=eCentral-eV
assert (eR,eNodal,eSmooth,eNormalized,eCentral,eNearby)==(24,12,24,48,36,24)
print('Euler route1: nodal=',eNodal,'; twelve small resolutions give=',eSmooth)
print('Euler route2: normalization=',eNormalized,'central=',eCentral,'nearby=',eNearby)
print('Auxiliary base-fibre multiplicities at0,1,infinity:3,4,12.')

# Explicit exponents in the elementary radial-gradient retraction used
# in the independent proof of B.4.2 for complex total dimension4.
gradient_exponents=[Fraction(2*k-1,2*k) for k in range(1,5)]
assert max(gradient_exponents)==Fraction(7,8)
print('Gradient exponents 1-1/(2k), k=1..4:',[str(v) for v in gradient_exponents])
out={'holomorphic_deck_exponents':holomorphic_exponents,
     'H1_deck_exponents':h1_exponents,
     'characteristic_polynomial':str(p),
     'inverse_polynomial':str(q),
     'line_square':-2,'normal_line_degree':str(normal_degree),
     'Euler':{'V':eV,'R':eR,'nodal_general':eNodal,'smooth_general':eSmooth,
              'modified_normalization':eNormalized,'semistable_central':eCentral},
     'base_fibre_multiplicities':[3,4,12],
     'gradient_exponents':[str(v) for v in gradient_exponents],
     'scope':'Constructed auxiliary family only; no S6 filling or characteristic invariant follows.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('ALL AUXILIARY PLUMBING CHECKS PASSED')
