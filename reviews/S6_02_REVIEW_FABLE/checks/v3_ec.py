# Reviewer's independent check of D.1.1-D.1.3 and of the constants in C.2.2.
import sympy as s
t = s.symbols("t")
A = -3 * t**3 * (t - 1)
B = 2 * t**4 * (t - 1)**2
print("disc factor:", s.factor(4 * A**3 + 27 * B**2), "  j/1728 =", s.cancel(4 * A**3 / (4 * A**3 + 27 * B**2)))
y0 = s.sqrt(2) * t**2 * (t - 1)
P = (s.Integer(0), y0)


def add(P1, P2):
    if P1 is None:
        return P2
    if P2 is None:
        return P1
    x1, y1 = P1
    x2, y2 = P2
    if s.simplify(x1 - x2) == 0:
        if s.simplify(y1 + y2) == 0:
            return None
        lam = (3 * x1**2 + A) / (2 * y1)
    else:
        lam = (y2 - y1) / (x2 - x1)
    lam = s.cancel(lam)
    x3 = s.cancel(lam**2 - x1 - x2)
    y3 = s.cancel(lam * (x1 - x3) - y1)
    return (x3, y3)


P2 = add(P, P)
P3 = add(P2, P)
P4 = add(P2, P2)
P6 = add(P3, P3)
print("x(2P) =", s.factor(P2[0]))
print("x(4P) =", s.factor(P4[0]))
print("denominator of x(6P):", s.factor(s.denom(s.together(P6[0]))))
r = s.solve(11 * t**2 - 6016 * t + 8192, t)
print("roots of 11t^2-6016t+8192:", r, [s.N(v, 12) for v in r], " claimed 64(47 +- 27 sqrt3)/11:", [s.N(64 * (47 + sg * 27 * s.sqrt(3)) / 11, 12) for sg in (-1, 1)])
# order of P at t = 32/5
sub = {t: s.Rational(32, 5)}
print("at t=32/5: y(2P) =", s.simplify(P2[1].subs(sub)), " (0 means 2P is 2-torsion, so 4P=O);  x(2P) =", s.simplify(P2[0].subs(sub)), " y(P) =", s.simplify(y0.subs(sub)))
# lattice images of L = 3 zeta1 + 4 zeta2 at mu=(2-tau)/4, beta = (9/8-101/4) tau - 9/4
tau = s.symbols("tau")
mu = (2 - tau) / 4
beta = (s.Rational(9, 8) - s.Rational(101, 4)) * tau - s.Rational(9, 4)
print("L-images of periods:", [s.expand(3 * a + 4 * b) for a, b in ((6 * mu, beta), (tau, mu), (1, 0), (0, 1))])
# admissibility of that c: Im c = (9/8-101/4) T - Im beta_part
import mpmath as mp
mp.mp.dps = 30
T = mp.findroot(lambda T: mp.kleinj(1j * T) - mp.mpf(32) / 5, 1.5)  # mpmath kleinj = j/1728
q = mp.exp(-mp.pi * T)
tauv = 1j * T
muv = (2 - tauv) / 4
th1 = mp.jtheta(1, mp.pi * muv, q)
et = mp.exp(1j * mp.pi * tauv / 12) * mp.qp(mp.exp(2j * mp.pi * tauv))
bpart = (6j / mp.pi) * mp.log(th1 / et / (2 * mp.sqrt(3)))
cval = (mp.mpf(9) / 8 - mp.mpf(101) / 4) * tauv - mp.mpf(9) / 4 - bpart
print("T =", T, " Im beta_part =", mp.im(bpart), " c =", cval, " (return: -2.25-34.02109724218209472308 i; Re defined mod branch)")
# constants of C.2.2
g2 = 60 * mp.nsum(lambda m, n: 0 if (m == 0 and n == 0) else 1 / (m + 1j * n)**4, [-mp.inf, mp.inf], [-mp.inf, mp.inf]) if False else None
# g2(i) = Gamma(1/4)^8/(16 pi^2)  (lattice Z+iZ)
g2i = mp.gamma(mp.mpf(1) / 4)**8 / (16 * mp.pi**2)
print("g2(i)/4 =", g2i / 4, " (return: 47.26 < . < 47.30)")
e2 = lambda tt: (mp.pi**2 / 3) * (mp.jtheta(2, 0, mp.exp(1j * mp.pi * tt))**4 - mp.jtheta(4, 0, mp.exp(1j * mp.pi * tt))**4)
dd = mp.diff(e2, 1j)
print("e2'(i) =", dd, " => d =", dd / 1j, " (return: 10.03 < d < 10.04);  3 d/(g2(i)/4) =", 3 * (dd / 1j) / (g2i / 4), "  2/pi =", 2 / mp.pi)
# sup of |G| and |H| on the distinguished boundary of the polydisc |h|<=1/5, |x|<=1/10 (sampled)
def G(h, x):
    tt = 1j + x
    qq = mp.exp(1j * mp.pi * tt)
    z = mp.pi * ((1 - tt) / 2 + h)
    t1 = mp.jtheta(1, z, qq)
    t1d = mp.jtheta(1, z, qq, 1)
    t1dd = mp.jtheta(1, z, qq, 2)
    c = mp.jtheta(1, 0, qq, 3) / mp.jtheta(1, 0, qq, 1) / 3
    return mp.pi**2 * (-(t1dd * t1 - t1d**2) / t1**2 + c)


def Hf(h, x):
    tt = 1j + x
    qq = mp.exp(1j * mp.pi * tt)
    return mp.log(mp.jtheta(3, mp.pi * h, qq) / (mp.exp(1j * mp.pi * tt / 12) * mp.qp(qq**2)))


mp.mp.dps = 15
mG = 0
mH = 0
n1 = 48
for a in range(n1):
    for b in range(n1):
        h = mp.mpf(1) / 5 * mp.exp(2j * mp.pi * a / n1)
        x = mp.mpf(1) / 10 * mp.exp(2j * mp.pi * b / n1)
        mG = max(mG, abs(G(h, x)))
        mH = max(mH, abs(Hf(h, x)))
print("sampled sup|G| on the torus |h|=1/5,|x|=1/10:", mG, " (return bound 18.373 < 20);  sampled sup|H|:", mH, " (return bound 0.547 < 0.6)")
print("G(0,0) =", mp.chop(G(0, 0)), " H(0,0) - log sqrt2 =", mp.chop(Hf(0, 0) - mp.log(mp.sqrt(2))))
