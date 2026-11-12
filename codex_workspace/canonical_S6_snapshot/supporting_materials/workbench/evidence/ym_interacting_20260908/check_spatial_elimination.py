"""Exact sign/coefficient checks; the unbounded-domain proofs are in the TeX.

The finite matrices below are an algebra diagnostic, not a numerical model
of the interacting Yang--Mills vacuum or a continuum approximation.
"""
import sympy as s


def zero(value):
    assert s.simplify(value) == 0, value


def matrix_zero(value):
    for entry in value:
        zero(entry)


checks = 0
x, y = s.symbols('x y', real=True)
kappa, z = s.symbols('kappa z', positive=True)
rho = s.Function('rho')(y, x)
marginal = s.Function('rho_R')(x)
f = s.Function('f')(x)
full_lift = -kappa * (s.diff(f, x, 2) + s.diff(rho, x) * s.diff(f, x) / rho)
reduced = -kappa * (s.diff(f, x, 2)
                    + s.diff(marginal, x) * s.diff(f, x) / marginal)
score = s.diff(rho, x) / rho - s.diff(marginal, x) / marginal
zero(full_lift - reduced + kappa * score * s.diff(f, x))
checks += 1

# The first retained basis vector is an exact zero-energy constant.
lmat = s.Matrix([[0, 0, 0], [0, 5, 2], [0, 2, 3]])
jmat = s.Matrix([[1, 0], [0, 1], [0, 0]])
amat = s.diag(0, 5)
bmat = s.Matrix([[0, 2]])
cmat = s.Matrix([[3]])
rmat = (cmat + z * s.eye(1)).inv()
schur = amat + z * s.eye(2) - bmat.T * rmat * bmat
matrix_zero(jmat.T * (lmat + z * s.eye(3)).inv() * jmat - schur.inv())
matrix_zero(jmat.T * lmat * jmat - amat)
matrix_zero(jmat.T * lmat**2 * jmat - amat**2 - bmat.T * bmat)
checks += 3

fvec = s.Matrix([0, 1])
wvec = rmat * bmat * fvec
uvec = jmat * fvec - s.Matrix([0, 0, wvec[0]])
base_energy = (fvec.T * amat * fvec)[0]
correction = (fvec.T * bmat.T * wvec)[0]
wnorm = (wvec.T * wvec)[0]
num = base_energy - correction - z * wnorm
den = (fvec.T * fvec)[0] + wnorm
zero((uvec.T * lmat * uvec)[0] - num)
zero((uvec.T * uvec)[0] - den)
zero((num / den).subs(z, 0) - s.Rational(33, 13))
zero((num / den - 5) - (-4 * (8 + 2 * z) / ((z + 3)**2 + 4)))
checks += 4

f1, f2, h = s.symbols('f1 f2 h', real=True)
fv = s.Matrix([f1, f2])
hv = s.Matrix([h])
v = jmat * fv + s.Matrix([0, 0, h])
square = ((fv.T * schur * fv)[0]
          + ((hv + rmat * bmat * fv).T
             * (cmat + z * s.eye(1)) * (hv + rmat * bmat * fv))[0])
zero((v.T * (lmat + z * s.eye(3)) * v)[0] - square)
checks += 1

# Formal short-time coefficient from the memory equation has the plus sign.
t = s.symbols('t', nonnegative=True)
kseries = s.eye(2) - t * amat + t**2 * (amat**2 + bmat.T * bmat) / 2
matrix_zero(kseries.diff(t).subs(t, 0) + amat)
matrix_zero(kseries.diff(t, 2).subs(t, 0) - amat**2 - bmat.T * bmat)
checks += 2

# Exact metric dictionary in the B term: X_c=2X, sigma_c=2sigma, kappa_c=kappa/4.
sigma, xf = s.symbols('sigma xf', real=True)
zero(-(kappa / 4) * (2 * sigma) * (2 * xf) + kappa * sigma * xf)
checks += 1

print(f'PASS: {checks} exact scalar/block assertions, plus exact matrix entries.')
print('Checked conditional-score cancellation, Schur inverse and reconstruction,')
print('square completion, corrected Rayleigh numerator/denominator, second moment,')
print('memory sign, and original metric factor. No vacuum approximation was used.')
