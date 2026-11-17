# Data for Part 1 of S6_06_BLIND: the monodromy tuple of the fourfold, as stated by the earlier run (S6_04 F.2.5).
# This file defines data only. It proves nothing; every property claimed for these matrices is to be checked by you.
import sympy as s

# cohomological matrices (the earlier run's convention)
A = s.Matrix([[1, 0, 0, 1, -1, 1],
              [0, 1, -1, -1, 1, 0],
              [0, 1, 0, -1, 0, 0],
              [0, 2, -1, -1, 0, 1],
              [0, 2, 0, -1, 0, 0],
              [0, 1, 1, -1, 0, 0]])
B = s.Matrix([[1, 0, 0, 0, 0, 0],
              [0, 0, -1, 0, 1, 0],
              [0, 0, -1, 0, 0, 1],
              [0, 0, -1, 0, 0, 0],
              [0, 1, -1, 0, 0, 0],
              [0, 0, -1, 1, 0, 0]])

# homology monodromies on H_1(T^6; Z) = Z^6 at the two finite special values, and at the cusp
M1 = A.T            # stated order 5
M2 = B.T            # stated order 4
M0 = (M1 * M2).inv()  # stated unipotent, (M0 - 1)^2 = 0, rank(M0 - 1) = 3

# twist vectors of the two free affine fillings: tau_i(x) = M_i x + v_i / m_i on R^6 / Z^6, m_1 = 5, m_2 = 4
v1 = s.Matrix([1, 3, -2, -1, 2, 0])
v2 = s.Matrix([-1, 0, 0, 0, 0, 0])

# stated invariant covector: ell(x) = x_0
ell = s.Matrix([[1, 0, 0, 0, 0, 0]])

# companion matrices of Phi_5 and of T^4 + 1; the earlier run states that the lower 5 x 5 blocks of A and B are the
# exterior squares of Cf^{-1} and of Cg, conjugated by the matrix Q below (identity with first column all ones)
Cf = s.Matrix([[0, 0, 0, -1], [1, 0, 0, -1], [0, 1, 0, -1], [0, 0, 1, -1]])
Cg = s.Matrix([[0, 0, 0, -1], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]])
Q = s.eye(6)
for i in range(6):
    Q[i, 0] = 1

# the genus-two pencil of the stated period construction: y^2 = x^5 + lam^3 x + lam^4, singular values lam = 0,
# infinity and lam_* = -256/3125
lam_star = s.Rational(-256, 3125)
