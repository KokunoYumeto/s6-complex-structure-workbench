"""Independent numerical checks of the exact regular-crossing coefficient.
The proof is analytic in D.4.5; these are not interval certificates.
"""
import mpmath as m
m.mp.dps=90
pi=m.pi
rho=m.exp(pi*1j/3)
mu0=(2-rho)/3
D0=-3*m.log(48)/(2*pi)
expected=7/(64*pi)
def ep(t):
    q=m.exp(2j*pi*t)
    E4=1+240*sum(n**3*q**n/(1-q**n) for n in range(1,110))
    E6=1-504*sum(n**5*q**n/(1-q**n) for n in range(1,110))
    E2=1-24*sum(n*q**n/(1-q**n) for n in range(1,110))
    tt=E4**3/(E4**3-E6**2)
    td=-2*pi*1j*tt*E6/E4
    return q,E4,E6,tt,td
def wp(z,t):
    q=m.exp(2j*pi*t)
    v=pi*pi/m.sin(pi*z)**2-pi*pi/3
    p=-2*pi**3*m.cos(pi*z)/m.sin(pi*z)**3
    for n in range(1,110):
        a=q**n/(1-q**n)
        v+=8*pi*pi*n*a*(1-m.cos(2*pi*n*z))
        p+=16*pi**3*n*n*a*m.sin(2*pi*n*z)
    return v,p
def mu(t):
    return m.findroot(lambda z:wp(z,t)[0],(mu0,mu0+m.mpf('.001')),tol=m.mpf('1e-80'))
def D(t):
    z=mu(t);q=m.exp(2j*pi*t);X=m.exp(2j*pi*z)
    a=2*m.sin(pi*z)*m.exp(pi*1j*t/6)
    for n in range(1,120):a*=(1-q**n*X)*(1-q**n/X)
    return 6/pi*(m.log(abs(a))-m.log(2*m.sqrt(3)))-6*m.im(z)**2/m.im(t)
def Dt(t):
    z=mu(t);q,E4,E6,tt,td=ep(t)
    L=pi*m.jtheta(1,pi*z,m.exp(pi*1j*t),1)/m.jtheta(1,pi*z,m.exp(pi*1j*t))
    Z=L+2*pi*1j*m.im(z)/m.im(t)
    P=wp(z,t)[1];g2=4*pi**4*E4/3
    return (1j*Z*(3*Z*P-2*g2)/(4*pi*pi*P))/td
print('Precision: 90 decimal digits; analytic proof is independent of this check.')
print('Expected Wirtinger derivative D_t =',m.nstr(expected,40))
for delta in [m.mpf('1e-3'),m.mpf('1e-4'),m.mpf('1e-4')*(1+1j)]:
    tau=rho+delta
    value=Dt(tau)
    eps=m.mpf('1e-20')
    finite=((D(tau+eps)-D(tau-eps))/(2*eps)-1j*(D(tau+1j*eps)-D(tau-1j*eps))/(2*eps))/2
    finite/=ep(tau)[4]
    tt=ep(tau)[3]
    remainder=D(tau)-D0-2*expected*m.re(tt)
    print('delta_tau =',m.nstr(delta,12))
    print('formula D_t =',m.nstr(value,40))
    print('product finite-difference D_t =',m.nstr(finite,40))
    print('two-method discrepancy =',m.nstr(abs(value-finite),10))
    print('distance from limit =',m.nstr(abs(value-expected),10))
    print('Taylor remainder / |t|^(4/3) =',m.nstr(remainder/abs(tt)**(m.mpf(4)/3),20))
