"""Exact algebra and integral group checks for C.2.UN.65.

The source proof supplies the actual adjunction, residue, collar and
realization morphisms.  These computations check their signs, weights,
Euler arithmetic and the integral obstruction used in that proof.
"""
from math import gcd
import sympy as S

r,t=S.symbols('r t', integer=True, nonnegative=True)
chi_components=r-t
canonical_squares=3*t
e_components=12*chi_components-canonical_squares
e_support=S.expand(e_components-2*r+t)
assert e_support==10*r-14*t
assert S.simplify(e_support.subs(r,S.Rational(3,2)*t)-t)==0
print('PASS exact Euler identity: sum chi=r-t, sum K^2=3t, e(S)=10r-14t=t when 2r=3t.')

curve_pairs=[]
for genus in range(41):
    for triples in range(121):
        if 2*genus-2==-triples:
            curve_pairs.append((genus,triples))
assert curve_pairs==[(0,2),(1,0)]
for triples in range(1001):
    if (3*triples)%2==0:
        rational=3*triples//2
        assert triples%2==0
        assert e_support.subs({r:rational,t:triples})==triples
print('PASS double-curve degree possibilities (genus, triple incidences):',curve_pairs)
print('PASS all incidence counts through 1000 triple points have even t and e=t.')

# Actual anticanonical eigenfunctions after a central resonant power.
weight_cases=0
for p in range(1,61):
    for q in range(1,61):
        if gcd(p,q)!=1:
            continue
        monomials={(i,j) for i in range((p+q)//p+1)
                   for j in range((p+q)//q+1) if p*i+q*j==p+q}
        if p==q==1:
            expected={(2,0),(1,1),(0,2)}
        elif q==1:
            expected={(1,1),(0,p+1)}
        elif p==1:
            expected={(1,1),(q+1,0)}
        else:
            expected={(1,1)}
        assert monomials==expected,(p,q,monomials)
        weight_cases+=1
print('PASS all',weight_cases,'coprime resonant anticanonical weight pairs through 60: the exact monomial lists in C.CZ.11.')

z,w,a,b,gamma=S.symbols('z w a b gamma',nonzero=True)
for p in range(2,61):
    transformed=z+(b/a)*w**p
    assert S.expand(w*(a*z+b*w**p)-a*w*transformed)==0
    assert S.expand(transformed.subs({z:gamma**p*z,w:gamma*w}, simultaneous=True)
                    -gamma**p*transformed)==0
print('PASS 59 actual triangular coordinate changes reduce the reduced resonant pair to the two axes and commute with the contraction.')
assert S.Matrix([[0,1],[1,0]]).det()==-1
print('PASS an axis interchange acts by -1 on the logarithmic two-form.')

# The exact integral central extension of a degree-d line complement.
# All triples here are actual integers; the centre (0,0,c) is injective.
d=S.symbols('d',integer=True)
aa,bb,cc,xx,yy,zz,pp,qq,rr=S.symbols('a b c x y z p q r',integer=True)
def mul(v,w,degree):
    return (v[0]+w[0],v[1]+w[1],v[2]+w[2]+degree*v[0]*w[1])
def inv(v,degree):
    return (-v[0],-v[1],-v[2]+degree*v[0]*v[1])
left=mul(mul((aa,bb,cc),(xx,yy,zz),d),(pp,qq,rr),d)
right=mul((aa,bb,cc),mul((xx,yy,zz),(pp,qq,rr),d),d)
assert all(S.expand(x-y)==0 for x,y in zip(left,right))
assert all(S.expand(x)==0 for x in mul((aa,bb,cc),inv((aa,bb,cc),d),d))
group_cases=0
for degree in range(-50,51):
    A=(1,0,0); B=(0,1,0)
    comm=mul(mul(mul(A,B,degree),inv(A,degree),degree),inv(B,degree),degree)
    assert comm==(0,0,degree)
    assert (comm==(0,0,0))==(degree==0)
    for exponent in range(-30,31):
        centre=(0,0,exponent)
        assert mul(A,centre,degree)==mul(centre,A,degree)
        assert mul(B,centre,degree)==mul(centre,B,degree)
        assert (centre==(0,0,0))==(exponent==0)
        group_cases+=1
print('PASS symbolic group associativity/inversion and',group_cases,'integral central-fibre checks: [a,b]=c^d, and abelianness forces d=0.')

# Check the actual extension of the volume form through xy=t.
x,y,zz=S.symbols('x y z',nonzero=True)
coefficient=S.Matrix([[y,x,0],[1/x,0,0],[0,0,1]]).det()
assert coefficient==-1
assert S.Matrix([[0,1,0],[1,0,0],[0,0,1]]).det()==coefficient
print('PASS exact wedge sign: d(xy) wedge dx/x wedge dz = dy wedge dx wedge dz.')
print('PASS all C.2.UN.65 exact arithmetic, eigenfunction, integral-group and local-volume checks.')
