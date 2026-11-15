"""Independent numerical checks of A.4.8, not a substitute for its proof."""
import mpmath as mp

mp.mp.dps = 80
a = mp.mpf(17)
B = 12 * mp.sqrt(2)

def K(s, kap):
    return 2**(s-1)*mp.gamma((s+1j*kap)/2)*mp.gamma((s-1j*kap)/2)/mp.gamma(s)

def fs(s, r):
    return 2**(-s)*mp.cosh(r)**(-s)*mp.hyp2f1(s/2,s/2,s+mp.mpf('.5'),mp.sech(r)**2)

def kernel(s, u):
    x = B*mp.cosh(u)
    return (mp.gamma(s)/(mp.sqrt(mp.pi)*mp.gamma(s+mp.mpf('.5')))
            *s*2**(-s)*a*x**(-s-1)
            *mp.hyp2f1((s+1)/2,(s+2)/2,s+mp.mpf('.5'),-x**-2))

def m_hyper(s, kap):
    p, q = (s+1+1j*kap)/2, (s+1-1j*kap)/2
    return (a*B**(-s-1)*mp.gamma(p)*mp.gamma(q)
            /(mp.sqrt(mp.pi)*mp.gamma(s+mp.mpf('.5')))
            *mp.hyp2f1(p,q,s+mp.mpf('.5'),-B**-2))

def fmt(z):
    return mp.nstr(z,70)

print('mpmath decimal precision:',mp.mp.dps)
print('B^2=',fmt(B**2))
for s, kap in [(mp.mpf(1),mp.mpf(0)),
               (mp.mpf('.5')+1j,mp.mpf('.7')),
               (mp.mpf('1.3')+2j,mp.mpf('2.5'))]:
    h=2*mp.quad(lambda u:(a+B*mp.cosh(u))**(-s)*mp.cos(kap*u),[0,1,3,6,12,mp.inf])
    khat=2*mp.quad(lambda u:kernel(s,u)*mp.cos(kap*u),[0,1,3,6,12,mp.inf])
    m=m_hyper(s,kap)
    print('\ns=',fmt(s),'kappa=',fmt(kap))
    print('m=',fmt(m))
    print('|direct H/K - m|=',fmt(abs(h/K(s,kap)-m)))
    print('|direct Fourier(k) - m|=',fmt(abs(khat-m)))
    r=mp.mpf(4)
    ode=mp.diff(lambda z:fs(s,z),r,2)+mp.tanh(r)*mp.diff(lambda z:fs(s,z),r)+s*(1-s)*fs(s,r)
    print('|outgoing ODE residual|=',fmt(abs(ode)))
    assert abs(h/K(s,kap)-m)<mp.mpf('1e-60')
    assert abs(khat-m)<mp.mpf('1e-60')
    assert abs(ode)<mp.mpf('1e-60')
for u in [mp.mpf(0),mp.mpf('.5'),mp.mpf(3)]:
    err=abs(mp.pi*kernel(1,u)-a/(1+B**2*mp.cosh(u)**2))
    print('s=1 scalar check u=',fmt(u),'residual=',fmt(err))
    assert err<mp.mpf('1e-70')
print('\nAll independent numerical checks passed.')
