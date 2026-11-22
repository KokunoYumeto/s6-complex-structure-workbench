"""Exact prereading calculations for the LR cusp; no target proof is read.

Methods: truncated Gaussian-rational algebras, graph cochains, and an explicit
interpolation inverse. The geometric identifications are proved in the
separate derivation; this program checks the stated finite calculations.
"""
from fractions import Fraction as F
import json


def add(a, b):
    return (a[0]+b[0], a[1]+b[1])


def neg(a):
    return (-a[0], -a[1])


def mul(a, b):
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def div(a, b):
    n = b[0]*b[0]+b[1]*b[1]
    assert n
    return mul(a, (b[0]/n, -b[1]/n))


ZERO = (F(0), F(0))
ONE = (F(1), F(0))
TWO_I = (F(0), F(2))


def poly_mul(a, b, order):
    out = [ZERO for _ in range(order)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j < order:
                out[i+j] = add(out[i+j], mul(x,y))
    return out


def rank(matrix):
    a = [[F(x) for x in row] for row in matrix]
    r = 0
    for c in range(len(a[0]) if a else 0):
        pivot = next((i for i in range(r,len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r],a[pivot] = a[pivot],a[r]
        pivot_value = a[r][c]
        a[r] = [x/pivot_value for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                factor = a[i][c]
                a[i] = [x-factor*y for x,y in zip(a[i],a[r])]
        r += 1
    return r


def mm(a,b):
    return [[sum(F(a[i][k])*F(b[k][j]) for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def strq(x):
    if isinstance(x,F):
        return str(x)
    if isinstance(x,tuple):
        return [str(x[0]),str(x[1])]
    if isinstance(x,list):
        return [strq(y) for y in x]
    if isinstance(x,dict):
        return {k:strq(v) for k,v in x.items()}
    return x


# LR old Weierstrass coefficients after x=t^2 X,y=t^3 Y.
k = F(27,4)
old_a = {3:k,4:-k}
old_b = {5:k,6:-k}
a_new = {n-4:v for n,v in old_a.items()}
b_new = {n-6:v for n,v in old_b.items()}
assert a_new == b_new == {-1:k,0:-k}
# The a*x and b terms cancel at x=-t^2.
assert {n+2:-v for n,v in old_a.items()} == {n:-v for n,v in old_b.items()}

# Cubic discriminant, as a polynomial in epsilon, evaluated by its five terms.
# a=4,b=27,c=54e,d=27e^2.
disc = {}
for power, coefficient in [
    (2,27**2*54**2), (3,-4*4*54**3), (2,-4*27**3*27),
    (4,-27*4**2*27**2), (3,18*4*27*54*27),
]:
    disc[power] = disc.get(power,0)+coefficient
disc = {n:c for n,c in disc.items() if c}
assert disc == {3:314928,4:-314928}

# Translation by -2P on the normalization: zeta -> zeta-2i,
# w=1/zeta -> w/(1-2iw), in Q(i)[w]/(w^3).
inverse = [ONE,TWO_I,mul(TWO_I,TWO_I)]
denominator = [ONE,neg(TWO_I),ZERO]
assert poly_mul(inverse,denominator,3) == [ONE,ZERO,ZERO]
w_new = poly_mul([ZERO,ONE,ZERO],inverse,3)
assert w_new == [ZERO,ONE,TWO_I]
cusp_difference = [add(x,neg(y)) for x,y in zip(w_new,[ZERO,ONE,ZERO])]
assert cusp_difference == [ZERO,ZERO,TWO_I]

# -1/(1+x) in Q[x]/(x^2) is -1+x.
epsilon_class = [F(-1),F(1)]
epsilon_denominator = [F(1),F(1)]
assert [sum(epsilon_class[j]*epsilon_denominator[n-j] for j in range(n+1))
        for n in range(2)] == [F(-1),F(0)]

# Normalization hexagon -> critical theta graph.
theta_d0 = [[-1,1] for _ in range(3)]
hex_d0 = [[int(j==(i+1)%6)-int(j==i) for j in range(6)] for i in range(6)]
vertex_pullback = [[int(j==i%2) for j in range(2)] for i in range(6)]
edge_pullback = [[((-1)**i if j==i%3 else 0) for j in range(3)] for i in range(6)]
assert mm(hex_d0,vertex_pullback) == mm(edge_pullback,theta_d0)
assert [sum(edge_pullback[i][j] for i in range(6)) for j in range(3)] == [0,0,0]
assert rank(theta_d0) == 1 and rank(hex_d0) == 5
theta_h1 = 3-rank(theta_d0)
hex_h1 = 6-rank(hex_d0)
assert (theta_h1,hex_h1) == (2,1)

# Structure-sheaf normalization complex of the toric fibre:
# one rational component, three rational double curves, two triple points.
d1 = [[1,1,-1],[-1,-1,1]]
assert rank(d1) == 1
toric_h = [1,3-rank(d1),2-rank(d1)]
assert toric_h == [1,2,1]
# Two cochains with c=a+b represent a basis; AW cup on the oriented square.
u = [1,0,1]
v = [0,1,1]
assert mm(d1,[[u[j],v[j]] for j in range(3)]) == [[0,0],[0,0]]
cup = lambda a,b:a[0]*b[1]-a[1]*b[0]
assert [[cup(a,b) for b in [u,v]] for a in [u,v]] == [[0,1],[-1,0]]

# Root-curve line-bundle cohomology, D=(1/4) infinity, L=O(-D).
def line_h(n):
    degree = n//4
    return (max(degree+1,0), max(-degree-1,0))


def total_h(exponents_by_direct_image):
    result = [0,0,0,0]
    for q, exponents in enumerate(exponents_by_direct_image):
        for exponent in exponents:
            h0,h1 = line_h(exponent)
            result[q] += h0
            result[q+1] += h1
    return result


vertical_h = total_h([[0,-1],[0,-1,-1,-2],[-1,-2]])
base_tangent_h = total_h([[5],[5,4],[4]])
assert vertical_h == [1,1,0,0]
assert base_tangent_h == [2,4,2,0]

c0 = F(-27,4)
h0_restriction = [[1,0],[0,0],[1,c0]]
assert rank(h0_restriction) == 2
# Appending the nilpotent cusp-jet column completes the target.
assert rank([row+[int(i==1)] for i,row in enumerate(h0_restriction)]) == 3

# H^1 restriction: a(T),b(T) linear; target bases are proved geometrically.
# The map is (a(0),2i*b(0),a(c0),b(c0)).
def restriction(coefficients):
    a0,a1,b0,b1 = coefficients
    return [a0,mul(TWO_I,b0),add(a0,mul((c0,F(0)),a1)),add(b0,mul((c0,F(0)),b1))]


def interpolation(target):
    x,y,z,w = target
    a0 = x
    b0 = div(y,TWO_I)
    return [a0,div(add(z,neg(a0)),(c0,F(0))),b0,div(add(w,neg(b0)),(c0,F(0)))]


for i in range(4):
    basis = [ONE if i==j else ZERO for j in range(4)]
    assert restriction(interpolation(basis)) == basis
    assert interpolation(restriction(basis)) == basis

critical_h = [3,4,0,0]
image_h = [0, critical_h[0]-2+base_tangent_h[1]-4,
           critical_h[1]-4+base_tangent_h[2],0]
assert image_h == [0,1,2,0]
tangent_h = [vertical_h[0],vertical_h[1]+image_h[1],image_h[2],0]
assert tangent_h == [1,2,2,0]

output = {
    'method':'Exact quotient algebras, graph cochains and explicit interpolation inverse; no sampling and no symbolic determinant command.',
    'LR_coordinate_coefficients':strq({'a_new':{str(n):v for n,v in a_new.items()},'b_new':{str(n):v for n,v in b_new.items()}}),
    'discriminant_epsilon_polynomial':disc,
    'cusp_translation_difference_mod_w3':strq(cusp_difference),
    'epsilon_local_Jacobi_class_mod_x2':strq(epsilon_class),
    'theta_and_hexagon_h1':[theta_h1,hex_h1],
    'hexagon_pullback_on_h1':'zero, by exact edge-cochain cancellation',
    'toric_fibre_coherent_dimensions':toric_h,
    'toric_cup_pairing':[[0,1],[-1,0]],
    'root_line_cohomology':{str(n):line_h(n) for n in [-2,-1,0,1,4,5]},
    'vertical_tangent_dimensions':vertical_h,
    'pulled_back_root_base_tangent_dimensions':base_tangent_h,
    'critical_quotient_dimensions':critical_h,
    'h0_restriction_rank':2,
    'h1_restriction_inverse_checked_on_full_basis':True,
    'image_sheaf_dimensions':image_h,
    'tangent_dimensions':tangent_h,
    'scope':'Only the finite calculations of the independently written geometric derivation. This output does not itself prove the sheaf or geometric identifications.',
    'target_proof_read':False,
    'events_added':0,
}
print(json.dumps(output,indent=2))
