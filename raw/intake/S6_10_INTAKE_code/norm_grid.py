# Intake check (Claude Opus 5.5 at effort max), 18 Nov 2026: numerical spot check of the
# maximum claim behind S6_10 Paper I fam:src:C.2.3 (exact domain 0<|w|<216).
# F(tau) = N(v0,tau) = |g_a(tau)| (Siegel function, Paper I line 2095ff) at a zero v0 of wp_tau;
# t = j(tau)/1728 = kleinj(tau).  Claim: max F = sqrt(2), attained only at t=1 (tau=i).
import mpmath as mp
mp.mp.dps = 25
def wp(z, tau):
    q = mp.exp(1j*mp.pi*tau)
    t2 = mp.jtheta(2, 0, q); t3 = mp.jtheta(3, 0, q)
    return (mp.pi*t2*t3*mp.jtheta(4, mp.pi*z, q)/mp.jtheta(1, mp.pi*z, q))**2 - mp.pi**2/3*(t2**4+t3**4)
def wp_zero(tau, guesses):
    for g in guesses:
        try:
            z = mp.findroot(lambda z: wp(z, tau), g, tol=1e-30, maxsteps=60)
        except Exception:
            continue
        a1 = mp.im(z)/mp.im(tau); a2 = mp.re(z - a1*tau)
        if abs(wp(z, tau)) < 1e-15 and min(abs(a1-mp.nint(a1)), 1) + min(abs(a2-mp.nint(a2)),1) > 1e-6:
            return z
    return None
def N(v, tau):
    a1 = mp.im(v)/mp.im(tau); a1 = a1 - mp.floor(a1); v = v - (mp.im(v)/mp.im(tau) - a1)*tau
    q = mp.exp(2j*mp.pi*tau); u = mp.exp(2j*mp.pi*v)
    B2 = a1**2 - a1 + mp.mpf(1)/6
    val = abs(q)**(B2/2)*abs(1-u)
    r = 1
    while True:
        f = abs(1-q**r*u)*abs(1-q**r/u); val *= f
        if abs(q)**r < mp.mpf(10)**-22: break
        r += 1
    return val
# sanity: Laurent check of wp
tau0 = mp.mpc(0.1, 1.3); z = mp.mpf('1e-4')
print("wp(z)-1/z^2 at small z:", mp.nstr(wp(z, tau0) - 1/z**2, 5))
# value at tau=i
v = wp_zero(1j, [(1+1j)/2, mp.mpc(0.45,0.5)])
print("tau=i: zero", mp.nstr(v,8), " N =", mp.nstr(N(v,1j),20), " sqrt2 =", mp.nstr(mp.sqrt(2),20))
# torsion table spot values: solve kleinj(tau)=t on the imaginary axis for real t>1
for tv, claim in [(mp.mpf(32)/5, 10), (64*(47-27*mp.sqrt(3))/11, 17+10*mp.sqrt(3)), (64*(47+27*mp.sqrt(3))/11, 10*mp.sqrt(3)-17)]:
    y = mp.findroot(lambda y: mp.re(mp.kleinj(1j*y)) - tv, max(1.05, mp.log(1728*tv)/(2*mp.pi)))
    tau = 1j*y
    v = wp_zero(tau, [mp.mpc(0.5,0.3655), (1+tau)/2, mp.mpc(0.5, 0.45*y), mp.mpc(0.5, 0.55*y), tau/2, mp.mpf(0.5)])
    print(f"t={mp.nstr(tv,10)}: tau={mp.nstr(tau,10)} N^12={mp.nstr(N(v,tau)**12,15)} claim {mp.nstr(claim,15)}")
# grid over the fundamental domain
best = (0, None); count = 0; viol = []
prev = None
for i in range(0, 21):
    x = -0.5 + 0.05*i
    y = mp.sqrt(1 - x**2) + 1e-9
    while y < 3.0:
        tau = mp.mpc(x, y)
        gs = ([prev] if prev is not None else []) + [mp.mpc(0.5,0.3655), (1+tau)/2, mp.mpc(0.5, 0.5*y), tau/2, mp.mpf(0.5), (1+tau)/3, mp.mpc(0.3,0.4*y), mp.mpc(0.7,0.6*y)]
        v = wp_zero(tau, gs)
        if v is None:
            viol.append(('nozero', mp.nstr(tau,6))); y += 0.05; continue
        prev = v
        n = N(v, tau); count += 1
        if n > best[0]: best = (n, tau)
        if n > mp.sqrt(2) + mp.mpf(10)**-12: viol.append((mp.nstr(tau,6), mp.nstr(n,12)))
        y += 0.05
print("grid points:", count, " max N =", mp.nstr(best[0], 15), "at tau =", mp.nstr(best[1], 8), " t=kleinj =", mp.nstr(mp.kleinj(best[1]), 8))
print("points with N > sqrt2 or failures:", viol[:10], len(viol))
for yy in [1.0, 1.5, 2.0, 3.0, 5.0]:
    tau = 1j*yy; v = wp_zero(tau, [mp.mpc(0.5,0.3655), (1+tau)/2, mp.mpc(0.5,0.5*yy), mp.mpc(0.5, 0.4*yy)])
    print(f"  tau={yy}i  t={mp.nstr(mp.re(mp.kleinj(tau)),8)}  N={mp.nstr(N(v,tau),12)}")
