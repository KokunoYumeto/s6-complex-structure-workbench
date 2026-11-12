"""Exact algebra checks for the retained quartic Fourier comparison.

Run with Python and SymPy. No numerical spectral grids, file writes, network,
TeX, Lean, or approximation to the quartic ground state are performed.
The analytic domain, positivity, smoothness, min-max and Duhamel arguments
are proved in moving_fourier_comparison.tex, not by this symbolic checker.
One named exact identity counts as one check.
"""

import sympy as S

checks = 0


def exact(name, expression):
    global checks
    entries = list(expression) if isinstance(expression, S.MatrixBase) else [expression]
    assert all(S.simplify(S.expand(v)) == 0 for v in entries), name
    checks += 1


hbar, V, Gamma, k, w, w0, E, T, rho = S.symbols(
    "hbar V Gamma k omega omega_star E T rho", positive=True
)
m2 = S.symbols("m_squared", nonnegative=True)
q, y, theta, qdot, ydot, pq, py = S.symbols(
    "q y theta qdot ydot p_q p_y", real=True
)
Smat = S.diag(1, -1, 0) / S.sqrt(2)
exact("Hermitian slice trace", S.trace(Smat))
exact("Hermitian slice metric", S.trace(Smat * Smat) - 1)
exact("Retained determinant vanishes on the slice", Smat.det())


def average(expr):
    return S.integrate(S.expand_trig(S.expand(expr)), (theta, 0, 2 * S.pi)) / (2 * S.pi)


for power, value in [(1, 0), (2, S.Rational(1, 2)), (3, 0), (4, S.Rational(3, 8))]:
    exact(f"Fourier cosine average power {power}", average(S.cos(theta) ** power) - value)

field = q + y * S.cos(theta)
kinetic = V * average((qdot + ydot * S.cos(theta)) ** 2) / 2
mass = V * m2 * average(field ** 2) / 2
gradient = V * average((-k * y * S.sin(theta)) ** 2) / 2
quartic = V * Gamma * average(field ** 4) / 4
exact("Unequal Fourier kinetic masses", kinetic - V * qdot ** 2 / 2 - V * ydot ** 2 / 4)
exact("Retained mass terms", mass - V * m2 * q ** 2 / 2 - V * m2 * y ** 2 / 4)
exact("Retained gradient term", gradient - V * k ** 2 * y ** 2 / 4)
exact("Retained quartic coefficients", quartic - V * Gamma * (q ** 4 + 3 * q ** 2 * y ** 2 + S.Rational(3, 8) * y ** 4) / 4)
exact("q momentum", S.diff(kinetic, qdot) - V * qdot)
exact("y momentum", S.diff(kinetic, ydot) - V * ydot / 2)
legendre = (pq * qdot + py * ydot - kinetic).subs({qdot: pq / V, ydot: 2 * py / V})
exact("Legendre coefficients", legendre - pq ** 2 / (2 * V) - py ** 2 / V)
exact("Two-coordinate mass measure", S.det(S.diag(V, V / 2)) - (V / S.sqrt(2)) ** 2)

a = hbar ** 2 / (2 * V)
ay = hbar ** 2 / V
b = V * w ** 2 / 4
c = 3 * Gamma * V / 32
d = 3 * Gamma * V / 2
Vq = V * (m2 * q ** 2 / 2 + Gamma * q ** 4 / 4)
full_potential = mass + gradient + quartic
exact("Full retained Hamiltonian potential", full_potential - Vq - V * (m2 + k ** 2 + 3 * Gamma * q ** 2) * y ** 2 / 4 - c * y ** 4)
exact("Fibre first derivative coefficient", S.diff(V * (m2 + k ** 2 + 3 * Gamma * q ** 2) / 4, q) - d * q)
exact("Fibre second derivative coefficient", S.diff(V * (m2 + k ** 2 + 3 * Gamma * q ** 2) / 4, q, 2) - d)
exact("Kinetic coefficients retain mass ratio", ay - 2 * a)

beta = V * w / (2 * hbar)
Cy = S.sqrt(V / 2)
chi = (V / 2) ** (-S.Rational(1, 4)) * (beta / S.pi) ** S.Rational(1, 4) * S.exp(-beta * y ** 2 / 2)
norm = S.integrate(Cy * chi ** 2, (y, -S.oo, S.oo))
moment2 = S.integrate(Cy * y ** 2 * chi ** 2, (y, -S.oo, S.oo))
moment4 = S.integrate(Cy * y ** 4 * chi ** 2, (y, -S.oo, S.oo))
exact("Gaussian normalization in retained mass measure", norm - 1)
exact("Gaussian second moment", moment2 - hbar / (V * w))
exact("Gaussian fourth moment", moment4 - 3 * hbar ** 2 / (V ** 2 * w ** 2))
exact("Harmonic Gaussian eigenvalue", (-ay * S.diff(chi, y, 2) + b * y ** 2 * chi) / chi - hbar * w / 2)
exact("Harmonic first excitation", (-ay * S.diff(y * chi, y, 2) + b * y ** 2 * y * chi) / chi - 3 * hbar * w * y / 2)
exact("True quartic action is not constant on Gaussian", (-ay * S.diff(chi, y, 2) + b * y ** 2 * chi + c * y ** 4 * chi) / chi - hbar * w / 2 - c * y ** 4)
delta = 9 * Gamma * hbar ** 2 / (32 * V * w ** 2)
exact("Variational quartic correction", c * moment4 - delta)
exact("Relative variational correction", delta / (hbar * w) - 9 * Gamma * hbar / (32 * V * w ** 3))
exact("Explicit gap-regime threshold", (9 * Gamma * hbar / (32 * V * w0 ** 3)).subs(V, 9 * Gamma * hbar / (16 * w0 ** 3)) - S.Rational(1, 2))
exact("Gap lower bound from min-max", 3 * hbar * w / 2 - (hbar * w / 2 + hbar * w / 2) - hbar * w / 2)

lam = hbar * w / 2
eupper = hbar * w
mu2upper = 4 * hbar / (V * w)
Mmoment = 2 * S.sqrt(5) * hbar / (V * w)
exact("True-state second moment bound coefficient", eupper / b - mu2upper)
exact("True-state fourth moment bound coefficient", eupper ** 2 / b ** 2 + ay / b - Mmoment ** 2)
exact("Weighted reduced-resolvent factor", (eupper + lam) / c - 16 * hbar * w / (Gamma * V))

# Use q>=0 for algebraic absolute-value derivative bounds; evenness restores q<0.
x = S.symbols("x", nonnegative=True)
L = 6 * S.sqrt(5) * Gamma * x / w ** 2
ep = 6 * Gamma * hbar * x / w
weighted = 4 * L * S.sqrt(hbar * w / (Gamma * V))
exact("First derivative coefficient", d * x * Mmoment / lam - L)
exact("Hellmann-Feynman derivative coefficient", d * x * mu2upper - ep)
second_raw = (d * Mmoment + 2 * d * x * weighted + 2 * ep * L) / lam
second_stated = (
    6 * S.sqrt(5) * Gamma / w ** 2
    + 144 * S.sqrt(5) * Gamma ** S.Rational(3, 2) * S.sqrt(V / hbar) * x ** 2 / w ** S.Rational(5, 2)
    + 144 * S.sqrt(5) * Gamma ** 2 * x ** 2 / w ** 4
)
exact("All pointwise second derivative constants", second_raw - second_stated)

radicand = w0 ** 2 + 3 * Gamma * x ** 2
ratio1 = x / radicand
xstar = w0 / S.sqrt(3 * Gamma)
exact("First derivative maximum stationarity", S.diff(ratio1, x).subs(x, xstar))
max1 = 1 / (2 * S.sqrt(3 * Gamma) * w0)
exact("First derivative exact maximum value", ratio1.subs(x, xstar) - max1)
u = S.symbols("u", nonnegative=True)
ratio2 = u / (w0 ** 2 + 3 * Gamma * u) ** 2
ustar2 = w0 ** 2 / (3 * Gamma)
exact("Quadratic ratio stationarity", S.diff(ratio2, u).subs(u, ustar2))
max2 = 1 / (12 * Gamma * w0 ** 2)
exact("Quadratic ratio maximum value", ratio2.subs(u, ustar2) - max2)
ratio3 = u / (w0 ** 2 + 3 * Gamma * u) ** S.Rational(5, 4)
ustar3 = 4 * w0 ** 2 / (3 * Gamma)
exact("Fractional ratio stationarity", S.diff(ratio3, u).subs(u, ustar3))
max3 = 4 / (3 * Gamma * 5 ** S.Rational(5, 4) * S.sqrt(w0))
exact("Fractional ratio maximum value", ratio3.subs(u, ustar3) - max3)
M1 = S.sqrt(15 * Gamma) / w0
M2 = 18 * S.sqrt(5) * Gamma / w0 ** 2 + 192 / 5 ** S.Rational(3, 4) * S.sqrt(Gamma * V / (hbar * w0))
exact("Global M1", 6 * S.sqrt(5) * Gamma * max1 - M1)
exact("Global M2", 6 * S.sqrt(5) * Gamma / w0 ** 2 + 144 * S.sqrt(5) * Gamma ** S.Rational(3, 2) * S.sqrt(V / hbar) * max3 + 144 * S.sqrt(5) * Gamma ** 2 * max2 - M2)
exact("Born-Huang global upper coefficient", a * M1 ** 2 - 15 * Gamma * hbar ** 2 / (2 * V * w0 ** 2))

# Exact product rule and projection identities, with the normalization scalar
# <Omega,Omega''>=-||Omega'||² entered explicitly as the proved analytic identity.
f = S.Function("f")(q)
O = S.Function("Omega")(q)
fibre_energy = S.Function("e")(q)
Bnorm = S.symbols("Omega_prime_norm_squared", nonnegative=True)
H_on_product = -a * S.diff(f * O, q, 2) + (Vq + fibre_energy) * f * O
effective_times_O = (-a * S.diff(f, q, 2) + (Vq + fibre_energy + a * Bnorm) * f) * O
residual = -a * (2 * S.diff(f, q) * S.diff(O, q) + f * (S.diff(O, q, 2) + Bnorm * O))
exact("Exact effective and off-diagonal product rule", H_on_product - effective_times_O - residual)
exact("Residual ground component vanishes", -a * (2 * S.diff(f, q) * 0 + f * (-Bnorm + Bnorm)))

error = S.sqrt(30 * Gamma * E) / (w0 * S.sqrt(V)) + 9 * S.sqrt(5) * Gamma * hbar / (V * w0 ** 2) + 96 / 5 ** S.Rational(3, 4) * S.sqrt(Gamma * hbar / (V * w0))
exact("Physical-time error constant", (2 * S.sqrt(a) * M1 * S.sqrt(E) + a * M2) / hbar - error)
threshold1 = 270 * Gamma * E * T ** 2 / (rho ** 2 * w0 ** 2)
threshold2 = 27 * S.sqrt(5) * Gamma * hbar * T / (rho * w0 ** 2)
threshold3 = 288 ** 2 * Gamma * hbar * T ** 2 / (5 ** S.Rational(3, 2) * rho ** 2 * w0)
term1 = T * S.sqrt(30 * Gamma * E) / (w0 * S.sqrt(V))
term2 = T * 9 * S.sqrt(5) * Gamma * hbar / (V * w0 ** 2)
term3 = T * 96 / 5 ** S.Rational(3, 4) * S.sqrt(Gamma * hbar / (V * w0))
exact("First target-volume threshold", term1.subs(V, threshold1) - rho / 3)
exact("Second target-volume threshold", term2.subs(V, threshold2) - rho / 3)
exact("Third target-volume threshold", term3.subs(V, threshold3) - rho / 3)

print(f"PASS: {checks} named exact algebraic checks; no spectral numerics or analytic-proof substitution.")
