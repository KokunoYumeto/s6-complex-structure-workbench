# Reviewer's independent numerical checks for C.1, C.2 (uses mpmath's own jtheta / lattice sums,
# not the return's series), plus D.1 elliptic-curve checks.
import mpmath as mp
mp.mp.dps = 40
pi = mp.pi


def eta(tau):
    q = mp.exp(2j * pi * tau)
    return mp.exp(1j * pi * tau / 12) * mp.qp(q)


def theta1(v, tau):
    return mp.jtheta(1, pi * v, mp.exp(1j * pi * tau))


def wp(v, tau):
    # Weierstrass p for the lattice Z + tau Z via theta functions: p(v) = e1 + (pi th2(0) th3(0) th4(v)... )
    # use the formula p(v) = (pi^2/3)(th2^4 + ... ) is easy to get wrong; use the lattice-independent identity
    # p(v) = -d^2/dv^2 log theta1(v) + c,  c = (1/3) theta1'''(0)/theta1'(0)
    q = mp.exp(1j * pi * tau)
    z = pi * v
    t1 = mp.jtheta(1, z, q)
    t1d = mp.jtheta(1, z, q, 1)
    t1dd = mp.jtheta(1, z, q, 2)
    c = mp.jtheta(1, 0, q, 3) / mp.jtheta(1, 0, q, 1) / 3
    return pi**2 * (-(t1dd * t1 - t1d**2) / t1**2 + c)


def wp_direct(v, tau, N=60):
    # brute lattice sum (slow convergence, only a sanity check of wp)
    sres = 1 / v**2
    for m in range(-N, N + 1):
        for n in range(-N, N + 1):
            if m == 0 and n == 0:
                continue
            w = m + n * tau
            sres += 1 / (v - w)**2 - 1 / w**2
    return sres


def mu_of(tau, guess=None):
    if guess is None:
        guess = mp.mpf(1) / 2 - 1j * mp.log(5 + 2 * mp.sqrt(6)) / (2 * pi)
    return mp.findroot(lambda v: wp(v, tau), guess)


def Dpart(tau, guess=None):
    m = mu_of(tau, guess)
    R = theta1(m, tau) / eta(tau)
    T = mp.im(tau)
    val = (6 / pi) * mp.log(abs(R) * mp.exp(-pi * mp.im(m)**2 / T) / (2 * mp.sqrt(3)))
    return val, m


mp.mp.dps = 15
print("sanity: wp via theta vs lattice sum at v=0.3+0.2i, tau=0.1+1.1i:", wp(mp.mpc(0.3, 0.2), mp.mpc(0.1, 1.1)), wp_direct(mp.mpc(0.3, 0.2), mp.mpc(0.1, 1.1)))
mp.mp.dps = 40
# special values
a = 5 + 2 * mp.sqrt(6)
mu0 = mp.mpf(1) / 2 - 1j * mp.log(a) / (2 * pi)
print("mu0 =", mu0, " sin^2(pi mu0) =", mp.sin(pi * mu0)**2)
rho = mp.exp(1j * pi / 3)
# z2: tau=i, mu=(1-i)/2
print("wp((1-i)/2, i) =", mp.chop(wp((1 - 1j) / 2, 1j)), "  wp((2-rho)/3, rho) =", mp.chop(wp((2 - rho) / 3, rho)))
R2 = theta1((1 - 1j) / 2, 1j) / eta(1j)
print("R(z2) =", R2, "  e^{pi/4} sqrt2 =", mp.exp(pi / 4) * mp.sqrt(2))
b2 = (6j / pi) * mp.log(R2 / (2 * mp.sqrt(3)))
print("beta_part(z2) =", b2, "  claimed i(3/2-(3/pi)log6) =", 1j * (mp.mpf(3) / 2 - 3 / pi * mp.log(6)))
R1 = theta1((2 - rho) / 3, rho) / eta(rho)
b1 = (6j / pi) * mp.log(R1 / (2 * mp.sqrt(3)))
print("R(z1) =", R1, " beta_part(z1) (principal log; real part defined mod 12) =", b1)
D1 = mp.im(b1) - 6 * mp.im((2 - rho) / 3)**2 / mp.im(rho)
D2 = mp.im(b2) - 6 * mp.mpf(1) / 4
print("D_part(z1) =", D1, "  D_part(z2) =", D2, "  -(3/pi)log 6 =", -3 / pi * mp.log(6))
print("Im(kappa1_part - kappa2_part) =", D1 - D2)
# transformation-law check of beta_part formula at a generic point, following the branch of mu by continuity is not needed:
# the laws are identities for R(v,tau); check them numerically
v = mp.mpc("0.37", "-0.21")
t = mp.mpc("0.23", "1.31")
Rf = lambda v, t: theta1(v, t) / eta(t)
print("R(v,t+1)/R - e^{i pi/6}:", mp.chop(Rf(v, t + 1) / Rf(v, t) - mp.exp(1j * pi / 6)))
print("R(v/t,-1/t)/R - (-i e^{i pi v^2/t}):", mp.chop(Rf(v / t, -1 / t) / Rf(v, t) + 1j * mp.exp(1j * pi * v**2 / t), tol=mp.mpf(10)**(-30)))
# cusp normalisation: beta_part + tau -> 0 along tau = iT
for T in (3, 5, 8):
    tau = mp.mpc(0, T)
    m = mu_of(tau)
    bp = (6j / pi) * (mp.log(theta1(m, tau) / mp.exp(1j * pi * tau / 12) / mp.qp(mp.exp(2j * pi * tau)) / (2 * mp.sqrt(3))) + 1j * pi * tau / 12)
    print("T=", T, " mu=", mp.nstr(m, 15), " beta_part+tau =", mp.nstr(mp.chop(bp + tau), 8))
# grid scan of D_part over the half fundamental domain 0<=x<=1/2, |tau|>=1, y<=2.2, continuation of the root from the previous point
mp.mp.dps = 20
best = (-mp.inf, None)
vals = 0
import itertools
nx, ny = 50, 140
for ix in range(nx + 1):
    x = mp.mpf(ix) / (2 * nx)
    guess = None
    ys = [mp.mpf("2.2") - (mp.mpf("2.2") - mp.mpf("0.86")) * k / ny for k in range(ny + 1)]
    for y in ys:
        tau = mp.mpc(x, y)
        if abs(tau) < 1:
            continue
        try:
            val, m = Dpart(tau, guess)
        except Exception as ex:
            print("root failure at", tau, ex)
            continue
        guess = m
        vals += 1
        if val > best[0]:
            best = (val, tau)
print("grid points evaluated:", vals, " max D_part on grid:", best[0], " at tau =", best[1], "  M claimed:", -3 / pi * mp.log(6))
# fine scan near i and along the arc |tau|=1 and the line x=1/2
mx = -mp.inf
arg = None
for k in range(0, 301):
    th = pi / 2 - (pi / 2 - pi / 3) * k / 300
    tau = mp.mpc(mp.cos(th), mp.sin(th))
    val, m = Dpart(tau)
    if val > mx:
        mx, arg = val, tau
print("max on the arc |tau|=1:", mx, "at", arg)
for eps in ("1e-2", "1e-3", "1e-4", "1e-5"):
    e = mp.mpf(eps)
    vs = [Dpart(1j + e * mp.exp(2j * pi * k / 8))[0] for k in range(8)]
    print("D_part(i + %s e^{2 pi i k/8}) - M:" % eps, [mp.nstr(v + 3 / pi * mp.log(6), 5) for v in vs])
