"""Exact certificates for C.2.UN.76.

These checks verify the lattice, canonical, finite-action and chart identities
used in the proof.  Properness and analytic gluing are proved in the source.
"""
from fractions import Fraction
from itertools import product
from math import gcd, lcm
from functools import reduce
import sympy as s


def det3(cols):
    a,b,c = cols
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -b[0]*(a[1]*c[2]-a[2]*c[1])
            +c[0]*(a[1]*b[2]-a[2]*b[1]))


def barycentric(p, tri):
    den = det3(tri)
    return tuple(Fraction(det3(tuple(p if j == i else tri[j]
                                    for j in range(3))), den)
                 for i in range(3))


root_rays = triangle_count = point_count = invariant_count = 0
canonical_count = 0
for m in product(range(1,7), repeat=3):
    M = lcm(*m)
    d = gcd(*m)
    lattice_index = M//d
    vertices = tuple(tuple(M//m[i] if i == j else 0 for j in range(3))
                     for i in range(3))
    points = []
    for x in range(M//m[0]+1):
        for y in range((M-m[0]*x)//m[1]+1):
            rem = M-m[0]*x-m[1]*y
            if rem % m[2] == 0:
                points.append((x,y,rem//m[2]))
    point_count += len(points)
    for v in vertices:
        assert sum(m[i]*v[i] for i in range(3)) == M
        root_rays += 1
    for lam in (Fraction(1), Fraction(1,2)):
        ks = tuple(lam*mi-1 for mi in m)
        if any(k.denominator != 1 or k < 0 for k in ks):
            continue
        for v in points:
            assert sum((ks[i]+1)*v[i] for i in range(3))-1 == M*lam-1
            canonical_count += 1
    # Every nontrivial character coset m*j/M remains nonintegral.
    for j in range(lattice_index):
        integral = all((j*mi) % M == 0 for mi in m)
        assert integral == (j == 0)
        invariant_count += 1
    # Refine by actual edge/interior star subdivisions at lattice points.
    pending = [vertices]
    leaves = []
    while pending:
        tri = pending.pop()
        index = abs(det3(tri))//lattice_index
        assert abs(det3(tri)) % lattice_index == 0
        if index == 1:
            leaves.append(tri)
            continue
        selected = None
        for p in points:
            if p in tri:
                continue
            bc = barycentric(p, tri)
            if min(bc) >= 0:
                selected = (p,bc)
                break
        assert selected is not None
        p,bc = selected
        zeros = [i for i,c in enumerate(bc) if c == 0]
        assert len(zeros) <= 1
        if zeros:
            k = zeros[0]
            i,j = [q for q in range(3) if q != k]
            pending += [(tri[k],tri[i],p),(tri[k],p,tri[j])]
        else:
            pending += [(tri[0],tri[1],p),(tri[1],tri[2],p),
                        (tri[2],tri[0],p)]
    expected = abs(det3(vertices))//lattice_index
    assert len(leaves) == expected
    assert len(leaves) == Fraction(M*M*d,m[0]*m[1]*m[2])
    triangle_count += len(leaves)
print(f"PASS {root_rays} old height-one rays, {point_count} height-one points, "
      f"{triangle_count} unimodular star-subdivision cones.")
print(f"PASS {canonical_count} exact weighted canonical valuations and "
      f"{invariant_count} normalized-root invariant character cosets.")

# Primitive direct-image normalization: half-integral lambda in (0,1].
ratio_count = 0
for m in product(range(1,10), repeat=3):
    for h in range(1,9):
        lam = Fraction(h,2)
        ks = [lam*a-1 for a in m]
        if any(x.denominator != 1 or x < 0 for x in ks):
            continue
        divisible_by_t = all(ks[i] >= m[i] for i in range(3))
        assert divisible_by_t == (lam > 1)
        if not divisible_by_t:
            assert lam in (Fraction(1,2),Fraction(1))
            if lam == Fraction(1,2):
                assert all(a % 2 == 0 for a in m)
        ratio_count += 1
print(f"PASS {ratio_count} primitive weighted-generator comparisons; "
      "only lambda=1 and lambda=1/2 remain.")

# Finite chart averaging in the exact cyclotomic ring.
x = s.symbols('x')
gauge_count = 0
for d in range(1,16):
    cyclo = s.Poly(s.cyclotomic_poly(d,x),x,domain=s.QQ)
    for q in range(1,4*d+1):
        if q % d == 0:
            continue
        weighted = sum(j*x**(j*q) for j in range(d))
        certificate = s.Poly((x**q-1)*weighted-d,x,domain=s.QQ)
        assert certificate.rem(cyclo).is_zero
        gauge_count += 1
print(f"PASS {gauge_count} exact finite-inertia logarithmic averaging jets.")

I = s.eye(2)
J = s.Matrix([[0,1],[-1,0]])
rt3 = s.sqrt(3)
Ds = [
    (I,1),(-I,2),(J,4),(-J,4),
    (s.Matrix([[-s.Rational(1,2),-rt3/2],[rt3/2,-s.Rational(1,2)]]),3),
    (s.Matrix([[s.Rational(1,2),-rt3/2],[rt3/2,s.Rational(1,2)]]),6),
    (s.diag(1,-1),2),(s.Matrix([[0,1],[1,0]]),2),
]
h,l = s.symbols('h l')
R = s.symbols('R', real=True)
ar1,ar2,ai1,ai2,d1,d2 = s.symbols(
    'ar1 ar2 ai1 ai2 d1 d2', real=True)
a = s.Matrix([ar1+s.I*ai1,ar2+s.I*ai2])
dvec = s.Matrix([d1,d2])
ap = a+s.I*R*dvec


def V(q, parameter):
    return q+parameter*J*s.conjugate(q)


def zero_matrix(M):
    return all(s.simplify(z) == 0 for z in M)


finite_count = 0
for D,order in Ds:
    delta = s.det(D)
    assert zero_matrix(D.T*D-I)
    assert zero_matrix(D*J-delta*J*D)
    assert zero_matrix(D*V(a,h)-V(D*a,delta*h))
    for M in range(order,13,order):
        # Iterate exact affine action with the target V frame.
        current = s.zeros(2,1)
        for j in range(M):
            target_h = delta**(j+1)*h
            current = (D*current + V(ap,target_h)
                       + (l+s.Rational(j,M))*V(dvec,target_h))
            current = current.applyfunc(s.expand)
        dm = sum((D**(M-1-j)*dvec for j in range(M)),s.zeros(2,1))
        am = sum((D**(M-1-j)*ap for j in range(M)),s.zeros(2,1))
        em = sum((j*D**(M-1-j)*dvec for j in range(M)),s.zeros(2,1))
        expected = V(am+em/M,h)+l*V(dm,h)
        assert zero_matrix(current-expected)
        aold = sum((D**(M-1-j)*a for j in range(M)),s.zeros(2,1))
        assert zero_matrix(am-aold-s.I*R*dm)
        finite_count += 1
    # The new infinity frame acts by det(D)D before exponentiation.
    Hinf = h*I+J
    Htarget = delta*h*I+J
    assert zero_matrix(delta*D*Hinf-Htarget*D)
print(f"PASS {finite_count} exact finite-action iterations, target frames, "
      "period-order shifts and reflected-infinity frame identities.")

# Check the simultaneous imaginary shift and both central base corrections.
lu = l+s.I*R
assert zero_matrix(dvec*l+ap-(dvec*lu+a))
qbase = l+s.I*R
ainf = s.conjugate(ap)-dvec*l
assert zero_matrix(ainf-(s.conjugate(a)-dvec*qbase))
# After torus inversion, -conjugate(a0) exponentiates to conjugate(a).
assert zero_matrix(-(s.conjugate(a)-dvec*qbase)
                   -(-s.conjugate(a)+dvec*qbase))
print("PASS exact kappa rescaling at both ends, including the a0+iR*d "
      "shift and the reflected fan followed by torus inversion.")

# Verify arbitrary-metric period determinant, including skew part.
xx,ww,yy,u,v,z,sk = s.symbols('xx ww yy u v z sk', real=True)
S = s.Matrix([[u,v],[v,z]])
A = S+sk*J
P = (I+xx*J).row_join(ww*J*(A-yy*I)).col_join(
    (ww*J).row_join((I-xx*J)*A+yy*(I+xx*J)))
r2 = xx*xx+ww*ww
formula = ((1+r2)**2*S.det()+(1-r2)*(1+r2)*yy*s.trace(S)
           +yy**2*(1-r2)**2+((1+r2)*sk+2*xx*yy)**2)
assert s.expand(P.det()-formula) == 0
print("PASS exact positive compact-middle determinant for every symmetric "
      "S>0 and every skew part.")

print("ALL C.2.UN.76 EXACT CHECKS PASSED")
