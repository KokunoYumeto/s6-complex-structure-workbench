# Tests of the hand-derived formulas written into Lead 13 and Lead 16 (c) of S6_05 on 13 Nov 2026 (not proofs).
from mpmath import mp, mpf, mpc, pi, exp, sin, cos, jtheta, findroot, kleinj, im, fabs
mp.dps = 30
def eta(tau):
    q = exp(2j*pi*tau); p = mpf(1)
    for n in range(1, 200): p *= (1 - q**n)
    return exp(1j*pi*tau/12)*p
th1 = lambda z, tau: jtheta(1, pi*z, exp(1j*pi*tau))
N = lambda z, tau: exp(-pi*im(z)**2/im(tau))*fabs(th1(z, tau)/eta(tau))
def wp(z, tau):
    q = exp(2j*pi*tau); s = 1/sin(pi*z)**2 - mpf(1)/3
    for n in range(1, 120): s += 8*n*q**n/(1-q**n)*(1-cos(2*pi*n*z))
    return pi**2*s
print("N(P)^9 = 16 N(3P) |t|^(-2/3):")
for tau, g in [(mpc(0, 1.3), mpc(0.5, -0.45)), (mpc(0.31, 1.07), mpc(0.4, -0.4)), (mpc(0.5, 1.9), mpc(0.5, -0.36))]:
    v = findroot(lambda z: wp(z, tau), g); t = kleinj(tau)
    print("  tau =", tau, " ratio =", mp.nstr(N(v, tau)**9/(16*N(3*v, tau)*fabs(t)**(-mpf(2)/3)), 15))
T = findroot(lambda y: kleinj(mpc(0, y)).real - mpf(32)/5, 1.5); tau = mpc(0, T)
v = findroot(lambda z: wp(z, tau), mpc(0.5, -0.4))
print("t = 32/5: T =", mp.nstr(T, 12), " N^12 =", mp.nstr(N(v, tau)**12, 15), " 64/t =", mp.nstr(mpf(64)*5/32, 15), " 4v mod lattice: v =", mp.nstr(v, 12))
tau = mpc(0, 1.3); v = findroot(lambda z: wp(z, tau), mpc(0.5, -0.45)); t = kleinj(tau).real; Tt = im(tau)
x = 2*fabs(im(v))/Tt
rhs = mpf(3)**(mpf(3)/4)*(t-1)**(-mpf(1)/4)*fabs(th1(x, mpc(0, 1/Tt))/eta(mpc(0, 1/Tt)))
print("real t > 1 (tau = 1.3 i): N(P)^4 / [3^(3/4)(t-1)^(-1/4)|theta1(x,i/T)/eta(i/T)|] =", mp.nstr(N(v, tau)**4/rhs, 15))
