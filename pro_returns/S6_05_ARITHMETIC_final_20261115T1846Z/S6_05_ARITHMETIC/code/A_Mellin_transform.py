"""Numerical diagnostics for exact identities proved in A.4.4.

These diagnostics are not a numerical proof.  All identities are derived by
beta integration and the hypergeometric differential equation in the paper.
The initial exponent/cancellation checks are retained for reproducibility.
"""
import mpmath as mp

mp.mp.dps = 50

def khat(s, k):
    return 2**(s-1)*mp.gamma((s+1j*k)/2)*mp.gamma((s-1j*k)/2)/mp.gamma(s)

def correction(s, k, A):
    return mp.hyp2f1((s+1j*k)/2,(s-1j*k)/2,(s+1)/2,-1/A**2)

def spherical_integral(s,k,A):
    delta = mp.asinh(1/A)
    c = mp.gamma((s+1)/2)/(mp.sqrt(mp.pi)*mp.gamma(s/2))
    # x=cos(theta) avoids endpoint cancellation in 1-x^2.
    return c*mp.quad(lambda th:
        (mp.cosh(2*delta)+mp.cos(th)*mp.sinh(2*delta))**(-(s+1j*k)/2)
        *mp.sin(th)**(s-1),[0,mp.pi/2,mp.pi])

def regularized_spherical_integral(s,k,A):
    delta=mp.asinh(1/A)
    c=mp.gamma((s+3)/2)/(mp.sqrt(mp.pi)*mp.gamma((s+2)/2))
    p=(s+1j*k)/2
    def fun(th):
        x=mp.cos(th)
        base=mp.cosh(2*delta)+x*mp.sinh(2*delta)
        f=base**(-p)
        fx=-p*mp.sinh(2*delta)*base**(-p-1)
        return (f+x*fx/(s+1))*mp.sin(th)**(s+1)
    return c*mp.quad(fun,[0,mp.pi/2,mp.pi])

def G(s,t,k):
    sj=mp.mpf('.5')+1j*t
    return (mp.gamma((s+1)/2)*mp.gamma((s+sj-1)/2)
            *mp.gamma((s-sj)/2)/(mp.gamma(s/2)
            *mp.gamma((s+1j*k)/2)*mp.gamma((s-1j*k)/2)))

def D(s,k):
    return mp.gamma((s+1j*k)/2)*mp.gamma((s-1j*k)/2)/mp.gamma(s)

print('mpmath precision',mp.mp.dps)
for s,k,A in [(mp.mpc('2.4','.7'),2,mp.mpf(3)),
              (mp.mpc('1.3','1.2'),7,mp.mpf(10)),
              (mp.mpc('.8','.3'),20,mp.mpf(30))]:
    f=correction(s,k,A)
    sph=spherical_integral(s,k,A)
    rel=abs(sph-f)/max(1,abs(f))
    print('spherical identity',s,k,A,'absolute/relative diagnostic',mp.nstr(rel,8))
    assert rel<mp.mpf('1e-30')
for s,k,A in [(mp.mpc('-.4','.7'),2,mp.mpf(3)),
              (mp.mpc('-.4','8.2'),70,mp.mpf(10)),
              (mp.mpc('-.7','.3'),20,mp.mpf(30))]:
    f=correction(s,k,A)
    sph=regularized_spherical_integral(s,k,A)
    rel=abs(sph-f)/max(1,abs(f))
    print('regularized spherical identity',s,k,A,'absolute/relative diagnostic',mp.nstr(rel,8))
    assert rel<mp.mpf('1e-30')
for k,A in [(2,mp.mpf(3)),(70,mp.mpf(10)),(20,mp.mpf(30))]:
    rel=abs(correction(mp.mpf(0),k,A)-mp.cos(k*mp.asinh(1/A)))
    print('s=0 correction identity',k,A,mp.nstr(rel,8))
    assert rel<mp.mpf('1e-40')
for s,k,A in [(mp.mpc('2.4','.7'),2,mp.mpf(3)),
              (mp.mpc('1.3','1.2'),7,mp.mpf(10))]:
    direct=2*mp.quad(lambda u:(1+A*A*mp.cosh(u)**2)**(-s/2)*mp.cos(k*u),
                     [0,1,3,8,20,mp.inf])
    predicted=A**(-s)*khat(s,k)*correction(s,k,A)
    rel=abs(direct-predicted)/abs(predicted)
    print('geometric Fourier identity',s,k,A,'relative diagnostic',mp.nstr(rel,8))
    assert rel<mp.mpf('1e-25')
for s,t in [(mp.mpc('2.4','.7'),mp.mpf('1.2')),
            (mp.mpc('1.3','.4'),mp.mpf('2.1'))]:
    sj=mp.mpf('.5')+1j*t
    direct=2*mp.quad(lambda u: mp.cosh(u)**(1-s)
            *mp.hyp2f1(sj/2,(1-sj)/2,mp.mpf('.5'),-mp.sinh(u)**2),
            [0,1,3,8,20,mp.inf])
    predicted=(mp.sqrt(mp.pi)*mp.gamma((s+sj-1)/2)*mp.gamma((s-sj)/2)
               /mp.gamma(s/2)**2)
    rel=abs(direct-predicted)/abs(predicted)
    print('radial beta transform',s,t,'relative diagnostic',mp.nstr(rel,8))
    assert rel<mp.mpf('1e-20')
for t,k in [(1.2,0),(1.2,5),(8,3),(8,20)]:
    t=mp.mpf(t);sj=mp.mpf('.5')+1j*t;k=mp.mpf(k)
    direct=(2*mp.gamma((sj+1)/2)*mp.gamma(sj-mp.mpf('.5'))
            /(mp.gamma(sj/2)*mp.gamma((sj+1j*k)/2)*mp.gamma((sj-1j*k)/2)))
    r=2*mp.gamma((sj+1)/2)*mp.gamma(sj-mp.mpf('.5'))/mp.gamma(sj/2)**3
    rel=abs(direct-r*D(sj,0)/D(sj,k))/max(1,abs(direct))
    print('residue normalization',t,k,mp.nstr(rel,8))
    assert rel<mp.mpf('1e-40')
for tau in [0,1,4,10]:
    for t in [0.7,2,6,15]:
        for k in [0,3,8,20]:
            exponent=t-max(t,k)-max(t,tau)+max(tau,k)
            distance=max(min(tau,k)-t,0,t-max(tau,k))
            assert abs(exponent+distance)<1e-12
print('Stirling exponential factor = exp(-pi/2 * distance to [min(tau,k),max(tau,k)]): PASS')
print('ALL DIAGNOSTICS PASS; analytic proof, not these numerics, establishes the identities.')
