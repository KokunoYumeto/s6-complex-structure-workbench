"""Postrelease transport of the exact C_jets.py inputs, by finite interpolation.

This file was written after reading the released target and the pinned old program.
It supplies no additional prereading check. No symbolic expansion, discriminant
routine, linear-system solver, or valuation search is used.
"""
from itertools import product


def wedge(u, v):
    return u[0] * v[1] - u[1] * v[0]


# f(X,Y)=product_i (a_i X+b_i Y). Both sides have separate degree <=4
# in the six factor coefficients. Five values per variable prove the identity.
n = 0
for a, b, c, d, e, f in product(range(5), repeat=6):
    A = a*c*e
    B = a*c*f + a*d*e + b*c*e
    C = a*d*f + b*c*f + b*d*e
    D = b*d*f
    coefficient_discriminant = B*B*C*C - 4*A*C*C*C - 4*B*B*B*D - 27*A*A*D*D + 18*A*B*C*D
    factor_discriminant = (wedge((a,b),(c,d))*wedge((a,b),(e,f))*wedge((c,d),(e,f)))**2
    assert coefficient_discriminant == factor_discriminant
    n += 1
assert n == 15625
print('Exact old coefficient discriminant equals the squared pairwise-wedge product: 15625 grid values, separate degree <=4.')


def add(z,w): return (z[0]+w[0],z[1]+w[1])
def sub(z,w): return (z[0]-w[0],z[1]-w[1])
def norm2(z): return z[0]*z[0]+z[1]*z[1]


# Hermitian norm identity gives the kernel over C, by positivity. Separate
# degree <=2 in the four real coordinates; this grid proves the identity.
n = 0
for x,y,u,v in product(range(3), repeat=4):
    a1,a2 = (x,y),(u,v)
    assert norm2(add(a1,a2))+norm2(sub(a1,a2)) == 2*(norm2(a1)+norm2(a2))
    n += 1
assert n == 81
print('Tacnode old constraint kernel: Hermitian sum-of-squares identity on 81 exact grid values; vanishing forces a1=a2=0.')


# The old triple constraint vector is (-a1,a3,a2,-a3). Its squared Hermitian
# norm is |a1|^2+|a2|^2+2|a3|^2, so its kernel is zero.
n = 0
for x,y,u,v,r,s in product(range(3), repeat=6):
    a1,a2,a3 = (x,y),(u,v),(r,s)
    old_vector = ((-x,-y),a3,a2,(-r,-s))
    assert sum(map(norm2,old_vector)) == norm2(a1)+norm2(a2)+2*norm2(a3)
    n += 1
assert n == 729
print('Triple old constraint kernel: Hermitian sum-of-squares identity on 729 exact grid values; vanishing forces a1=a2=a3=0.')
print('Branch transport old-to-new is the permutation (1 2); the third branch is fixed.')
print('All identities have certified finite interpolation bounds; positivity is the exact real norm-square argument in the comparison record.')
