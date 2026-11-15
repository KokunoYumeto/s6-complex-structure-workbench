"""Numerical scalar checks of the independently derived line spectral density."""
import mpmath as mp
mp.mp.dps=90

def f(s,r):
    return 2**(-s)*mp.cosh(r)**(-s)*mp.hyp2f1(s/2,s/2,s+mp.mpf('.5'),mp.sech(r)**2)

def fp0(s):
    return -2**(1-s)*mp.sqrt(mp.pi)*mp.gamma(s+mp.mpf('.5'))/mp.gamma(s/2)**2

def f_near(s,r):
    A=mp.sqrt(mp.pi)*mp.gamma(s+mp.mpf('.5'))/mp.gamma((s+1)/2)**2
    B=-2*mp.sqrt(mp.pi)*mp.gamma(s+mp.mpf('.5'))/mp.gamma(s/2)**2
    z=mp.tanh(r)**2
    return 2**(-s)*mp.cosh(r)**(-s)*(A*mp.hyp2f1(s/2,s/2,mp.mpf('.5'),z)
               +B*mp.tanh(r)*mp.hyp2f1((s+1)/2,(s+1)/2,mp.mpf('1.5'),z))

print('Precision:',mp.mp.dps,'decimal digits')
for t in [mp.mpf(1),mp.mpf(10),mp.mpf(100)]:
    s=mp.mpf('.5')-1j*t
    derivative=mp.diff(lambda r:f_near(s,r),mp.mpf(0))
    err0=abs(derivative-fp0(s))
    err1=abs(f(s,mp.mpf('.2'))-f_near(s,mp.mpf('.2')))
    source=(2*t/mp.pi)*mp.im(-f(s,0)/(2*fp0(s)))
    exact=t*mp.sinh(mp.pi*t)*abs(mp.gamma(mp.mpf('.25')+1j*t/2))**4/(4*mp.pi**3)
    print('\nt=',t)
    print('right derivative connection residual=',mp.nstr(err0,60))
    print('connection value residual=',mp.nstr(err1,60))
    print('source-density formula residual=',mp.nstr(abs(source-exact),60))
    print('pi*P_t(0)=',mp.nstr(mp.pi*source,60))
    assert err0<mp.mpf('1e-75')
    assert err1<mp.mpf('1e-75')
    assert abs(source-exact)<mp.mpf('1e-75')
    for r in [mp.mpf(0),mp.mpf(2),mp.mpf(5)]:
        alpha=1j*t*mp.exp(-1j*t*r)*mp.sqrt(mp.cosh(r))*f(s,r)/fp0(s)
        print('r=',r,'alpha=',mp.nstr(alpha,50),'t*|alpha-1|=',mp.nstr(t*abs(alpha-1),30))
        assert abs(alpha-1)<1/t
print('\nAll scalar spectral checks passed.')
