import mpmath as mp
import json
mp.mp.dps=50
A=5+2*mp.sqrt(6)
mu0=mp.mpf('.5')-1j*mp.log(A)/(2*mp.pi)
rho=mp.e**(mp.pi*1j/3)

def eta(tau):
    q=mp.e**(2j*mp.pi*tau)
    return mp.e**(mp.pi*1j*tau/12)*mp.nprod(lambda k:1-q**k,[1,mp.inf])
def wp(z,tau):
    q=mp.e**(2j*mp.pi*tau)
    return mp.pi**2/mp.sin(mp.pi*z)**2-mp.pi**2/3+8*mp.pi**2*mp.nsum(lambda n:n*q**n/(1-q**n)*(1-mp.cos(2*mp.pi*n*z)),[1,mp.inf])
def mu(tau):
    if abs(tau-1j)<mp.mpf('1e-35'): return (1-1j)/2
    if abs(tau-rho)<mp.mpf('1e-35'):return (2-rho)/3
    # Two roots coincide modulo periods at tau=i. The theta norm is branch-independent.
    return mp.findroot(lambda z:wp(z,tau),(mu0,mu0+mp.mpf('.01')),solver='secant',maxsteps=100)
def beta(tau,z=None):
    if z is None:z=mu(tau)
    return 6j/mp.pi*mp.log(mp.jtheta(1,mp.pi*z,mp.e**(mp.pi*1j*tau))/(2*mp.sqrt(3)*eta(tau)))
def D(tau):
    z=mu(tau)
    return mp.im(beta(tau,z))-6*mp.im(z)**2/mp.im(tau)
if __name__=='__main__':
    out={}
    for name,t,z in [('cusp',None,mu0),('z1',rho,(2-rho)/3),('z2',1j,(1-1j)/2)]:
        out[name]={'tau':str(t),'mu':str(z)}
        if t is not None:
            b=beta(t,z)
            out[name].update(beta=str(b),D=str(mp.im(b)-6*mp.im(z)**2/mp.im(t)))
    print(json.dumps(out,indent=2))
    for t in [rho,.5+1j,1j,1.01j,1.1j,1.5j,2j,3j,.25+1j,.1+1j,.5+2j]:
        print('sample',str(t),'mu',mp.nstr(mu(t),25),'D',mp.nstr(D(t),25))
