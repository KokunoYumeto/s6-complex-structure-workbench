# Reviewer's check of closed forms not stated in the return:
#   D_part(z1) = -(3/(2 pi)) log 48,   beta_part(z1) = -1/2 + i(1/sqrt3 - (3/(2 pi)) log 48),
#   nome of Alb(S1) = -w^2/48^3,  nome of Alb(S2) = i w/6^3,   chi(T_X)=1 bookkeeping.
import mpmath as mp
mp.mp.dps = 60
pi = mp.pi
rho = mp.exp(1j * pi / 3)


def R(v, tau):
    # theta1/eta with explicit q^{1/4}=exp(i pi tau/4) branch
    s = mp.mpc(0)
    for n in range(0, 40):
        s += (-1)**n * mp.exp(1j * pi * tau * (n + mp.mpf(1) / 2)**2) * mp.sin((2 * n + 1) * pi * v)
    th = 2 * s
    q = mp.exp(2j * pi * tau)
    et = mp.exp(1j * pi * tau / 12)
    for n in range(1, 200):
        et *= (1 - q**n)
    return th / et


mu1 = (2 - rho) / 3
R1 = R(mu1, rho)
N1 = abs(R1) * mp.exp(-pi * mp.im(mu1)**2 / mp.im(rho))
print("N(z1) =", N1, "  3^(1/4) =", mp.mpf(3)**(mp.mpf(1) / 4), "  diff =", mp.nstr(N1 - mp.mpf(3)**0.25, 5))
b1 = (6j / pi) * mp.log(R1 / (2 * mp.sqrt(3)))
print("beta_part(z1) =", b1)
print("claimed      =", -mp.mpf(1) / 2 + 1j * (1 / mp.sqrt(3) - 3 / (2 * pi) * mp.log(48)))
D1 = mp.im(b1) - 6 * mp.im(mu1)**2 / mp.im(rho)
print("D_part(z1) =", D1, "  -(3/(2pi)) log 48 =", -3 / (2 * pi) * mp.log(48), " diff", mp.nstr(D1 + 3 / (2 * pi) * mp.log(48), 5))
mu2 = (1 - 1j) / 2
R2 = R(mu2, 1j)
b2 = (6j / pi) * mp.log(R2 / (2 * mp.sqrt(3)))
k1 = b1 + 2 * mu1
k2 = b2 + 3 * mu2
print("kappa1_part =", mp.chop(k1), "  kappa2_part =", mp.chop(k2))
print("exp(-2 pi i kappa1_part) =", mp.chop(mp.exp(-2j * pi * k1)), "  -1/48^3 =", -mp.mpf(1) / 48**3)
print("exp(-pi i kappa2_part)   =", mp.chop(mp.exp(-1j * pi * k2)), "  i/216 =", 1j / mp.mpf(216))
# transformation laws with the explicit branch (identities for R)
v = mp.mpc("0.37", "-0.21")
t = mp.mpc("0.23", "1.31")
print("R(v,t+1)/R(v,t) - e^{i pi/6} =", mp.chop(R(v, t + 1) / R(v, t) - mp.exp(1j * pi / 6)))
print("R(v/t,-1/t)/R(v,t) + i e^{i pi v^2/t} =", mp.chop(R(v / t, -1 / t) / R(v, t) + 1j * mp.exp(1j * pi * v**2 / t)))
# g1,g2 laws for beta_part = (6i/pi) log(R/(2 sqrt3)) as identities in (mu,tau) modulo 12Z
for name, mm, tt, shift in (("g1", (1 - v) / t, (t - 1) / t, 2 - 6 * (1 - v)**2 / t), ("g2", 1 + v / t, -1 / t, -3 - 6 * v**2 / t)):
    lhs = (6j / pi) * mp.log(R(mm, tt) / R(v, t))
    print(name, ": (beta o g - beta) - law =", mp.chop(lhs - shift), " (an element of 12Z is allowed)")
