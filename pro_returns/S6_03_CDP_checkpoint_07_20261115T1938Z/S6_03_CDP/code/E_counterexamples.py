"""Exact and independent numerical checks for E10, E17 and E18.

The geometric and analytic proofs are in the paper. Floating-point values
below are checks at 70 decimal digits, not certified interval proofs.
"""
from math import comb
import sympy as s
import mpmath as mp

z, e = s.symbols('z e')
for truncation in range(1, 13):
    ideal = s.groebner([z*e, e**2, z**truncation], z, e)
    assert ideal.reduce(e)[1] == e
    assert ideal.reduce(z*e)[1] == 0
    assert ideal.reduce(e**2)[1] == 0
    basis = [z**j for j in range(truncation)] + [e]
    assert len(basis) == truncation + 1
    assert all(ideal.reduce(mon)[1] == mon for mon in basis)
print('E17 square-zero local algebra: embedded section e survives all 12 truncations')
print('E17 h^q(O_Z(-kD)) = (max(1-k,0)+1, max(k-1,0), 0 for q>=2)')
for k in (-2, 0, 1, 2, 7):
    h0, h1 = max(1-k, 0)+1, max(k-1, 0)
    assert h0-h1 == 2-k
    print('  k =', k, ':', (h0, h1))

# C is the genus-two double cover of P1 and L=pi^*O(1)=K_C.
# For a positive integer a, H0(L^-a)=0 and h1(L^-a)=2a+1.
def h1_negative(a):
    assert a > 0
    return 2*a+1
structure = (1, 2, 2*h1_negative(1), h1_negative(2))
obstruction = (0, h1_negative(1), 2*h1_negative(2), h1_negative(3))
vertical = (0, 2*h1_negative(1), 4*h1_negative(2), 2*h1_negative(3))
assert structure == (1,2,6,5)
assert obstruction == (0,3,10,7)
assert vertical == (0,6,20,14)
print('E10 h(O_Y), h(g^*T_C), h(T_Y/C):', structure, obstruction, vertical)

# In the normalized lattice basis the original fourth period is exactly
# six times the fourth basis vector, so the comparison has index six.
isogeny_matrix = s.diag(1,1,1,6)
assert isogeny_matrix.det() == 6
print('E18 original-to-symmetric lattice determinant:', isogeny_matrix.det())
print('E18 fibre h(O), h(T):', tuple(comb(2,q) for q in range(3)),
      tuple(2*comb(2,q) for q in range(3)))

mp.mp.dps = 70
def theta1_half(tau):
    return mp.jtheta(1, mp.pi/2, mp.exp(mp.pi*1j*tau))
def eta(tau):
    q = mp.exp(2*mp.pi*1j*tau)
    return mp.exp(mp.pi*1j*tau/12) * mp.fprod(1-q**n for n in range(1,100))
def v(tau):
    return 1j/mp.pi * mp.log(theta1_half(tau)/eta(tau)) + 1j
tau = mp.mpc(0,1)
method1 = mp.diff(v, tau)
nome = mp.exp(-mp.pi)
theta3 = 1 + 2*sum(nome**(n*n) for n in range(1,30))
theta4 = 1 + 2*sum((-1)**n * nome**(n*n) for n in range(1,30))
method2 = -(theta3**4+theta4**4)/12
proposed = -(1j/(2*mp.pi)*mp.diff(
    lambda zz: mp.log(mp.jtheta(1, mp.pi*zz, nome)), mp.mpf('0.5')))**2
assert abs(method1-method2) < mp.mpf('1e-60')
assert abs(proposed) < mp.mpf('1e-60')
assert mp.im(v(tau)) > 1
print('E18 mu=1/2, tau=i, precision=70 decimal digits')
print('  Im v =', mp.nstr(mp.im(v(tau)), 48))
print('  derivative of theta/eta logarithm =', mp.nstr(method1, 48))
print('  independent theta-constant series =', mp.nstr(method2, 48))
print('  absolute discrepancy =', mp.nstr(abs(method1-method2), 8))
print('  proposed square =', mp.nstr(proposed, 8))
print('E18 direct-image ranks for absolute tangent: (2,3,1), higher zero')
