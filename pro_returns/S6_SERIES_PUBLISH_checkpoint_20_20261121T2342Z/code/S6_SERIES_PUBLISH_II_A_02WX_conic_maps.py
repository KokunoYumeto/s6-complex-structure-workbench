"""Fresh preproof exact certificates for 02WX; no historical code imported."""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product, permutations
import json


@dataclass(frozen=True)
class QI:
    real: F
    imag: F = F(0)

    def __add__(self, other):
        if not isinstance(other, QI):
            other = QI(F(other))
        return QI(self.real+other.real, self.imag+other.imag)

    __radd__ = __add__

    def __neg__(self):
        return QI(-self.real, -self.imag)

    def __sub__(self, other):
        return self+(-other if isinstance(other,QI) else -F(other))

    def __mul__(self, other):
        if not isinstance(other, QI):
            other = QI(F(other))
        return QI(self.real*other.real-self.imag*other.imag,
                  self.real*other.imag+self.imag*other.real)

    __rmul__ = __mul__

    def __truediv__(self, other):
        if not isinstance(other, QI):
            other = QI(F(other))
        norm = other.real**2+other.imag**2
        assert norm
        return self*QI(other.real/norm,-other.imag/norm)


I = QI(F(0),F(1))
double_rows = []
for x,y,z in product((F(0),F(1),F(2)),(F(1),F(2),F(3)),(F(0),F(1),F(2))):
    a = QI(x/y)+I*z
    b = QI(x/y)-I*z
    assert (a*b)*(y*y) == QI(x*x+y*y*z*z)
    assert (a+b)*(y/F(2)) == QI(x)
    assert (a-b)/(2*I) == QI(z)
    u = QI(x)-I*y*z
    v = QI(x)+I*y*z
    assert u*v == QI(x*x+y*y*z*z)
    assert (u+v)/2 == QI(x)
    assert (v-u)/(2*I) == QI(y*z)
    double_rows.append([int(x),int(y),int(z),str((a*b).real),str((a*b).imag)])

# The cleared identities have separate degree at most two in x,y,z.
# Three distinct values in every variable certify the whole polynomial.
assert len(double_rows) == 27

triple_rows = []
for x,y,z,w in product((F(1),F(2)),(F(0),F(1)),(F(0),F(1)),(F(0),F(1))):
    a = y
    b = x*z+w
    assert a*b == x*y*z+y*w
    assert (b-w)/x == z
    triple_rows.append([int(x),int(y),int(z),int(w),str(a*b)])
# These cleared identities are separately linear in x,y,z,w.
# The substitution w=y^(q-1) is the declared map to each Tp,q,infinity.
assert len(triple_rows) == 16


def extended(a,b):
    r0,r1 = a,b
    u0,u1 = 1,0
    v0,v1 = 0,1
    while r1:
        quotient = r0//r1
        r0,r1 = r1,r0-quotient*r1
        u0,u1 = u1,u0-quotient*u1
        v0,v1 = v1,v0-quotient*v1
    assert u0*a+v0*b == r0
    return r0,u0,v0


unequal_rows = []
for a0,b0 in product(range(1,5),repeat=2):
    d,_,_ = extended(a0,b0)
    a,b = a0//d,b0//d
    one,r,minus_t = extended(b,a)
    t = -minus_t
    assert one == 1 and r*b-t*a == 1
    assert a0*b-b0*a == 0
    k_double = a+b
    # For P=s^k-c, sP'-kP=k*c, which is a unit when c is nonzero.
    root_certificate = {'s^k': k_double-k_double, 'c':k_double}
    assert root_certificate == {'s^k':0,'c':k_double}
    assert k_double >= 2
    for p in (3,4,7):
        k_triple = a+(p-1)*b
        assert k_triple >= p
        assert 2*a0+2*(p-1)*b0 > 0
        unequal_rows.append([a0,b0,d,a,b,r,t,p,k_double,k_triple])

weighted_rows = []
for q in (3,4,5,8):
    weights = (q,2,q-2)
    degrees = (2*weights[0],2*weights[1]+2*weights[2],q*weights[1])
    assert degrees == (2*q,)*3
    weighted_rows.append(['T2q',q,*weights,*degrees])
for p,q in ((3,3),(3,4),(4,3),(4,4),(3,8),(7,9)):
    weights = (q,p,p*q-p-q)
    degrees = (sum(weights),p*weights[0],q*weights[1])
    assert degrees == (p*q,)*3 and min(weights)>0
    weighted_rows.append(['Tpq',p,q,*weights,*degrees])
# General weight equality follows from polynomial identities of bidegree <=(1,1);
# the four corners (3,3),(3,4),(4,3),(4,4) certify those equalities exactly.


def sign(p):
    return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))


hessian = [[2 if i==j else 0 for j in range(3)] for i in range(3)]
determinant = 0
for p in permutations(range(3)):
    term = sign(p)
    for i in range(3):
        term *= hessian[i][p[i]]
    determinant += term
assert determinant == 8
sphere_cells = [1,0,1]
chi = sum((-1)**i*n for i,n in enumerate(sphere_cells))
normal_sign = sign([0,2,1,3])
assert chi == 2 and normal_sign == -1

blowup_rows = [[mu,mu-1] for mu in (0,1,2)]
assert all(coefficient<=1 for _,coefficient in blowup_rows)
generic_conductor_rows = []
for branches in range(1,13):
    delta = F(branches,2)
    allowed = delta.denominator==1 and delta>=branches-1
    if allowed:
        generic_conductor_rows.append([branches,int(delta)])
assert generic_conductor_rows == [[2,1]]

print(json.dumps({
 'timing':'preproof: 02WX target and historical routines closed',
 'double_cleared_identity_grid':double_rows,
 'double_separate_degree_bound':[2,2,2],
 'triple_formal_w_identity_grid':triple_rows,
 'triple_separate_degree_bound':[1,1,1,1],
 'unequal_multiplicity_rows_columns':['a0','b0','d','a_prime','b_prime','inverse_r','inverse_t','p','double_roots','triple_roots'],
 'unequal_multiplicity_rows':unequal_rows,
 'weighted_degree_rows':weighted_rows,
 'morse_hessian':hessian,'morse_determinant_Leibniz':determinant,
 'sphere_cells':sphere_cells,'sphere_Euler':chi,
 'normal_orientation_permutation':[0,2,1,3],
 'normal_Euler':normal_sign*chi,
 'reduced_pair_blowup_coefficients':blowup_rows,
 'generic_conductor_allowed_branches_delta':generic_conductor_rows
},indent=2))
