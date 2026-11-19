# Intake of S6_06_BLIND cp36, gap 4 (Claude Opus 5.5 at effort max, agent a6d42bf6fe2b0d8a8, 19 Nov 2026).
# Checks the orientation identities of P3K.68, PL.1 and PL.2a, by explicit quaternion and complex arithmetic:
#  (a) q_H = c0 + j*conj(c1) is orientation preserving from C^2 (complex orientation) to H = (1, i, j, k);
#  (b) the physical circle q -> q e^{-i theta} has tangent -i at 1 and weights (-1, +1) on (c0, c1);
#  (c) the Hopf map z = q i q^-1 sends the horizontal j, k to -2k, +2j, so [S^3] = -[S^1_delta][S^2_z]
#      (circle first, outward orientations);
#  (d) the right-complex chart d/c0 (d = conj c1) has Hopf derivative (d_x, d_y) -> (-2k, -2j): [P^1_right] = -[S^2_z];
#  (e) the spinor (conj c0, c1) carries the physical circle as a common positive scalar, and its projectivization with
#      the complex orientation is +[S^2_z]; so the physical line (the tautological line of that spinor) has Chern
#      number -1 on S^2_z, and its dual U has +1;
#  (f) the effect of the choice on classes: x -> -x negates k = int x^3 and l = int p1 x, hence A = (4k-l)/24, and
#      leaves every multiplicative rule unchanged.
# Usage: python -I -B physical_line_orientation.py
import numpy as np

def qmul(a, b):
    a0, a1, a2, a3 = a; b0, b1, b2, b3 = b
    return np.array([a0*b0 - a1*b1 - a2*b2 - a3*b3, a0*b1 + a1*b0 + a2*b3 - a3*b2,
                     a0*b2 - a1*b3 + a2*b0 + a3*b1, a0*b3 + a1*b2 - a2*b1 + a3*b0])
def qinv(a): return np.array([a[0], -a[1], -a[2], -a[3]]) / np.dot(a, a)
one, I, J, K = np.eye(4)
def qH(c0, c1):     # c0 + j * conj(c1)
    return np.array([c0.real, c0.imag, 0, 0]) + qmul(J, np.array([c1.real, -c1.imag, 0, 0]))
# (a) Jacobian of (x0, y0, x1, y1) -> q_H
Jac = np.array([qH(1, 0), qH(1j, 0), qH(0, 1), qH(0, 1j)]).T
print('(a) det of C^2 -> H:', round(np.linalg.det(Jac), 6))
# (b) the physical circle on (c0, c1): q e^{-i t} = qH(e^{-it} c0, e^{+it} c1)?
t, c0, c1 = 0.37, 0.8 + 0.1j, -0.3 + 0.5j
lhs = qmul(qH(c0, c1), np.array([np.cos(t), -np.sin(t), 0, 0]))
print('(b) q e^{-it} = qH(e^{-it} c0, e^{it} c1):', np.allclose(lhs, qH(np.exp(-1j*t)*c0, np.exp(1j*t)*c1)))
# (c) Hopf derivatives at q = 1 and the orientation of (circle tangent, horizontal lift) against (i, j, k)
def hopf(q): return qmul(qmul(q, I), qinv(q))
e = 1e-6
dj = (hopf(one + e*J) - hopf(one - e*J)) / (2*e); dk = (hopf(one + e*K) - hopf(one - e*K)) / (2*e)
print('(c) Hopf derivative j ->', np.round(dj, 4), ' k ->', np.round(dk, 4))
base = np.linalg.det(np.array([[dj[2], dk[2]], [dj[3], dk[3]]]))     # in the (j, k) frame of T_i S^2
circle_first = np.linalg.det(np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]]))  # (-i, j, k) against (i, j, k)
print('    horizontal (j,k) -> T S^2_z orientation sign', np.sign(base), '; [S^3] = sign', circle_first * np.sign(base), 'x [S^1][S^2_z]')
# (d) right-complex chart: q = 1 + j * eps (x + i y)
dx = (hopf(one + e*qmul(J, np.array([1, 0, 0, 0]))) - hopf(one)) / e
dy = (hopf(one + e*qmul(J, np.array([0, 1, 0, 0]))) - hopf(one)) / e
sd = np.sign(np.linalg.det(np.array([[dx[2], dy[2]], [dx[3], dy[3]]])))
print('(d) right chart derivatives', np.round(dx, 3), np.round(dy, 3), ' [P^1_right] =', sd, 'x [S^2_z]')
# (e) the spinor s = (conj c0, c1): its projective chart coordinate w = c1 / conj c0 = conj of the right chart d/c0
#     composed with conjugation, so its complex orientation is opposite to P^1_right
print('(e) [P(spinor)] =', -sd, 'x [S^2_z]; tautological line has degree -1 on P(spinor), so the physical line M has',
      int(-1 * (-sd)), 'on S^2_z and U = M^-1 has', int(-sd), '...' if False else '')
print('    physical circle on the spinor: (conj c0, c1) -> (e^{it} conj c0, e^{it} c1): common positive scalar',
      np.allclose(np.array([np.conj(np.exp(-1j*t)*c0), np.exp(1j*t)*c1]), np.exp(1j*t)*np.array([np.conj(c0), c1])))
# (f) examples under both lines: classes c (M) and -c (U); a consistent flop rule A' = 7A in both
for name, cM in (('primitive K22, d=8', 3), ('d=14', 6), ('d=20', 9), ('d=30', 14), ('OS45', 3), ('OS47', 4), ('E7 loop', -1)):
    cU = -cM
    print('(f) %-20s M: class %2d, flop %2d | U: class %2d, flop %2d | old printed U-flop (x -5): %2d'
          % (name, cM % 28, (7 * cM) % 28, cU % 28, (7 * cU) % 28, (-5 * cU) % 28))
