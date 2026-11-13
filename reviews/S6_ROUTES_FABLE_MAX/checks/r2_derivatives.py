# Finite-difference checks of two derivative formulas in ROUTES.md (not proofs).
#  (a) dL/dtau (Wirtinger) = (1/2) W R + W^2/(8 pi i),  L = log N(v(tau),tau), R = v' - Im v/Im tau, W = th1'/th1(v) + 2 pi i Im v/Im tau
#  (b) d(beta/6)/dtau - (dv/dtau)^2 = -(v' - (i/2pi) Z)^2, beta/6 = (i/pi) log(th1(v)/eta), Z = d/dz log th1 (z-period 1)
from mpmath import mp, mpf, mpc, pi, exp, sin, cos, log, jtheta, findroot, im, re, fabs, diff
mp.dps = 40
def eta(tau):
    q = exp(2j*pi*tau); p = mpf(1)
    for n in range(1, 160): p *= (1 - q**n)
    return exp(1j*pi*tau/12)*p
th1 = lambda z, tau: jtheta(1, pi*z, exp(1j*pi*tau))
def wp(z, tau):
    q = exp(2j*pi*tau); s = 1/sin(pi*z)**2 - mpf(1)/3
    for n in range(1, 100): s += 8*n*q**n/(1-q**n)*(1-cos(2*pi*n*z))
    return pi**2*s
tau0, g = mpc(0.31, 1.07), mpc(0.526, -0.349)
vz = lambda tau: findroot(lambda z: wp(z, tau), g)
h = mpf(10)**(-12)
v0 = vz(tau0)
vp = (vz(tau0+h) - vz(tau0-h))/(2*h)                     # v'(tau), holomorphic derivative
Z = diff(lambda z: log(th1(z, tau0)), v0)
a = im(v0)/im(tau0)
W, R = Z + 2j*pi*a, vp - a
L = lambda tau: log(exp(-pi*im(vz(tau))**2/im(tau))*fabs(th1(vz(tau), tau)/eta(tau)))
Lx = (L(tau0+h) - L(tau0-h))/(2*h); Ly = (L(tau0+1j*h) - L(tau0-1j*h))/(2*h)
print("(a) numeric dL/dtau =", mp.nstr((Lx - 1j*Ly)/2, 12), "  formula =", mp.nstr(W*R/2 + W**2/(8j*pi), 12))
B = lambda tau: (1j/pi)*log(th1(vz(tau), tau)/eta(tau))
Bp = (B(tau0+h) - B(tau0-h))/(2*h)
print("(b) numeric det =", mp.nstr(Bp - vp**2, 12), "  formula =", mp.nstr(-(vp - 1j*Z/(2*pi))**2, 12), "  = (W+2 pi i R)^2/(4 pi^2):", mp.nstr((W+2j*pi*R)**2/(4*pi**2), 12))
