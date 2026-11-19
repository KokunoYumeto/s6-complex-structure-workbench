# Intake of S6_06_BLIND cp36, section 7 (Claude Opus 5.5 at effort max, agent a6d42bf6fe2b0d8a8, 19 Nov 2026).
# An independent computation of the Eells-Kuiper invariant of the Hopf gluing lambda(f) of P3F.22 for an arbitrary
# Torelli element f with Jin's coordinates (k, l), directly (no reduction by a-powers, no use of the homomorphism
# property), and for the generators a = (1, 4) and b = (8, 8).
# The spin-c Eells-Kuiper formula is first rederived from the A-hat and L genera:
#   index = int e^{z/2} Ahat = (p1^2 - 4 sigma)/896 - z^2 p1/192 + z^4/384 in degree 8.
# Coboundary: W = D(L) u (D^4 x D^4) over N_f (the run's construction), with cycles C1 = CP^2 (trivial normal bundle)
# and C2 = generator of H_4(N_f); then C1.C1 = 0, C1.C2 = 1, C2.C2 = int_N x^3 = k; restrictions:
# z^2 -> (1, k), p1 -> (3, l + k), since TW|N = TN + L and p1(TN) = l y, x^2 = k y, <xy, [N]> = 1.
# Usage: python -I -B p3f22_normalization.py
from fractions import Fraction as F
import sympy as sp

# 1. the degree-8 part of e^{z/2} Ahat, with p2 eliminated by the signature (L-genus)
p1, p2, z, s = sp.symbols('p1 p2 z sigma')
Ahat8 = (7 * p1**2 - 4 * p2) / 5760
Ahat4 = -p1 / 24
expz = 1 + z / 2 + z**2 / 8 + z**3 / 48 + z**4 / 384
deg8 = sp.expand(Ahat8 + (z**2 / 8) * Ahat4 + z**4 / 384)
deg8 = sp.simplify(deg8.subs(p2, (45 * s + p1**2) / 7))
target = (p1**2 - 4 * s) / 896 - z**2 * p1 / 192 + z**4 / 384
print('spin-c Eells-Kuiper formula rederived:', sp.simplify(deg8 - target) == 0)

def mu_boundary(k, l):
    Q = sp.Matrix([[0, 1], [1, k]])
    Qi = Q.inv()
    rp = sp.Matrix([3, l + k]); rz = sp.Matrix([1, k])
    p1sq = (rp.T * Qi * rp)[0]; z2p1 = (rz.T * Qi * rp)[0]; z4 = (rz.T * Qi * rz)[0]
    ev = Q.eigenvals(); sig = sum(m * (1 if sp.re(v) > 0 else -1) for v, m in ev.items())
    mu = F(int(sp.numer(p1sq - 4 * sig)), int(sp.denom(p1sq - 4 * sig))) / 896 - F(str(z2p1)) / 192 + F(str(z4)) / 384
    return Q.det(), sig, p1sq, z2p1, z4, mu

print('general k, l: mu(boundary W) =', sp.simplify(((6 * sp.Symbol('l') - 3 * sp.Symbol('k')) / 896
      - (sp.Symbol('l') + sp.Symbol('k')) / 192 + sp.Symbol('k') / 384)), ' (= -(4k - l)/(24*28))')
for name, (k, l) in (('a', (1, 4)), ('b', (8, 8)), ('a^-8 b', (0, -24)), ('b^2', (16, 16))):
    det, sig, p1sq, z2p1, z4, mu = mu_boundary(k, l)
    A = F(4 * k - l, 24)
    print('%-7s (k,l)=(%3d,%3d): det Q=%2d sigma=%d p1^2=%4s z^2p1=%4s z^4=%3s mu(dW)=%s -> mu(lambda) = %s mod 1; A/28 = %s'
          % (name, k, l, det, sig, p1sq, z2p1, z4, mu, (-mu) % 1, (A / 28) % 1))
# 2. the classical normalization: Milnor's sphere S_{2,-1}: Euler number 1, p1 = 6, signature 1
print('Milnor sphere S_{2,-1}: (36 - 4)/896 =', F(36 - 4, 896))
