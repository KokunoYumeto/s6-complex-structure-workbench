# Numerical sanity checks for identities used in ROUTES.md (Claude Fable 5.2, 13 Nov 2026).
# Unverified hunches are tested here to ~1e-12 (mpmath) or ~1e-3 (grid integral). Not proofs.
from mpmath import mp, mpf, mpc, pi, exp, sin, cos, log, sqrt, jtheta, findroot, qfrom, kleinj, nsum, inf, fabs, im, re, conj
import numpy as np
mp.dps = 30
def eta(tau):
    q = exp(2j*pi*tau)
    p = mpf(1)
    for n in range(1, 200):
        p *= (1 - q**n)
    return exp(1j*pi*tau/12)*p
def th1(z, tau):
    return jtheta(1, pi*z, exp(1j*pi*tau))
def N(z, tau):
    return exp(-pi*im(z)**2/im(tau))*fabs(th1(z, tau)/eta(tau))
def wp(z, tau):
    q = exp(2j*pi*tau)
    s = 1/sin(pi*z)**2 - mpf(1)/3
    for n in range(1, 120):
        s += 8*n*q**n/(1-q**n)*(1-cos(2*pi*n*z))
    return pi**2*s
def zero_of_wp(tau, guess):
    return findroot(lambda z: wp(z, tau), guess)
def t_of(tau):
    return kleinj(tau)   # mpmath kleinj = j/1728
print("== (1) duplication: N(P)^4 = 3^(3/4) N(2P) |t-1|^(-1/4)")
for tau, g in [(mpc(0, 1.3), mpc(0.5, -0.45)), (mpc(0.31, 1.07), mpc(0.4, -0.4)), (mpc(0.5, 1.9), mpc(0.5, -0.36)), (mpc(0.12, 1.02), mpc(0.45,-0.48))]:
    v = zero_of_wp(tau, g)
    t = t_of(tau)
    lhs = N(v, tau)**4
    rhs = mpf(3)**(mpf(3)/4)*N(2*v, tau)/fabs(t-1)**(mpf(1)/4)
    print(" tau=", tau, " v=", mp.nstr(v, 12), " N=", mp.nstr(N(v,tau), 15), " lhs/rhs=", mp.nstr(lhs/rhs, 15))
print("== (1b) equianharmonic and lemniscatic values")
rho = exp(1j*pi/3)
print(" N((2-rho)/3, rho)^4 =", mp.nstr(N((2-rho)/3, rho)**4, 20), "  N((1-i)/2, i)^2 =", mp.nstr(N(mpc(0.5,-0.5), mpc(0,1))**2, 20))
print("== (3) Gaussian-sum formula: N(z)^2 sqrt(2T)|eta|^2 = sum_{mu in Lambda/2} eps(mu) exp(-2 pi |z-mu|^2/T)")
def gauss_sum(z, tau, R=14):
    T = im(tau); s = mpf(0)
    for k in range(-2*R, 2*R+1):
        for l in range(-2*R, 2*R+1):
            mu = (k*tau + l)/2
            eps = -1 if (k % 2 == 0 and l % 2 == 0) else 1
            s += eps*exp(-2*pi*fabs(z-mu)**2/T)
    return s
for tau, z in [(mpc(0.2, 1.1), mpc(0.3, 0.4)), (mpc(0, 1), mpc(0.5, 0.5)), (mpc(-0.4, 0.95), mpc(0.11, -0.27))]:
    T = im(tau)
    lhs = N(z, tau)**2*sqrt(2*T)*fabs(eta(tau))**2
    print(" tau=", tau, " z=", z, " lhs/rhs=", mp.nstr(lhs/gauss_sum(z, tau), 15))
print("== (2) Mahler measure: 2 log N(v) = log(4 pi^2 |eta|^4) - mean_E log|wp|   (grid, double precision)")
def wp_np(z, tau, nmax=60):
    q = np.exp(2j*np.pi*tau)
    s = 1/np.sin(np.pi*z)**2 - 1/3
    for n in range(1, nmax):
        s = s + 8*n*q**n/(1-q**n)*(1-np.cos(2*np.pi*n*z))
    return np.pi**2*s
for tau, g in [(complex(0.31, 1.07), mpc(0.4, -0.4)), (complex(0, 1.3), mpc(0.5, -0.45))]:
    M = 1400
    a = (np.arange(M)+0.5)/M - 0.5
    b = (np.arange(M)+0.5)/M - 0.5
    A, B = np.meshgrid(a, b, indexing="ij")
    Z = A*tau + B
    m = np.mean(np.log(np.abs(wp_np(Z, tau))))
    v = zero_of_wp(mpc(tau), g)
    lhs = 2*log(N(v, mpc(tau)))
    rhs = log(4*pi**2*fabs(eta(mpc(tau)))**4) - m
    print(" tau=", tau, " 2logN(v)=", mp.nstr(lhs, 8), " formula=", mp.nstr(rhs, 8))
print("== (4) torsion value at t=32/5 from duplication twice: N^16 = 40*(5/32)^(1/3) = 10^(4/3)")
print("  ", mp.nstr(40*(mpf(5)/32)**(mpf(1)/3), 20), mp.nstr(mpf(10)**(mpf(4)/3), 20))
