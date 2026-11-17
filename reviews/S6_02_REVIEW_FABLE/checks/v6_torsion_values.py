# N = exp(-pi (Im v)^2/Im tau) |theta1(v,tau)/eta(tau)| at the torsion points of P with known t:
# t = 32/5 (order 4), t = 64(47 +- 27 sqrt3)/11 (order 6). Numerical; looks for small algebraic relations.
import mpmath as mp
mp.mp.dps = 50
pi = mp.pi


def R(v, tau):
    s = mp.mpc(0)
    for n in range(0, 60):
        s += (-1)**n * mp.exp(1j * pi * tau * (n + mp.mpf(1) / 2)**2) * mp.sin((2 * n + 1) * pi * v)
    q = mp.exp(2j * pi * tau)
    et = mp.exp(1j * pi * tau / 12)
    for n in range(1, 300):
        et *= (1 - q**n)
    return 2 * s / et


def wp(v, tau):
    q = mp.exp(1j * pi * tau)
    z = pi * v
    t1 = mp.jtheta(1, z, q)
    t1d = mp.jtheta(1, z, q, 1)
    t1dd = mp.jtheta(1, z, q, 2)
    c = mp.jtheta(1, 0, q, 3) / mp.jtheta(1, 0, q, 1) / 3
    return pi**2 * (-(t1dd * t1 - t1d**2) / t1**2 + c)


def N(v, tau):
    return abs(R(v, tau)) * mp.exp(-pi * mp.im(v)**2 / mp.im(tau))


def tau_of_t(t):
    return 1j * mp.findroot(lambda T: mp.kleinj(1j * T) - t, 1.2 if t < 50 else 1.9)


for name, t in (("32/5", mp.mpf(32) / 5), ("t_-", 64 * (47 - 27 * mp.sqrt(3)) / 11), ("t_+", 64 * (47 + 27 * mp.sqrt(3)) / 11)):
    tau = tau_of_t(t)
    T = mp.im(tau)
    # the zero of wp on the branch Re v = 1/2, -T/2 < Im v < 0
    v = mp.findroot(lambda vv: wp(vv, tau), mp.mpc(0.5, -0.36))
    a1 = mp.im(v) / T
    a2 = mp.re(v) - a1 * mp.re(tau)
    n = N(v, tau)
    D = (6 / pi) * mp.log(n / (2 * mp.sqrt(3)))
    print(name, " T =", mp.nstr(T, 25), " v =", mp.nstr(v, 20), " (a1,a2) =", mp.nstr(a1, 15), mp.nstr(a2, 15))
    print("   N =", mp.nstr(n, 40), "  D_part =", mp.nstr(D, 30))
    for k in (1, 2, 4, 8, 12, 24, 48):
        p = mp.findpoly(n**k, 6, maxcoeff=20000, tol=mp.mpf(10)**(-35))
        if p:
            print("   N^%d is a root of" % k, p)
            break
