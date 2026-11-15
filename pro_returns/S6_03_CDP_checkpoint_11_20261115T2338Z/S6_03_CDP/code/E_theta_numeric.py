"""Independent numerical checks of the proven E8 formula (70 digits).

Method 1 differentiates the implicit theta-zero branch using mpmath.diff.
Method 2 evaluates modular forms by exact-divisor Fourier series and uses
the independently derived algebraic g2,g3 formula. Neither is a proof.
"""
import mpmath as m
m.mp.dps=70
def sigma(n,p): return sum(d**p for d in range(1,n+1) if n%d==0)
def Ek(tau,k):
    q=m.exp(2*m.pi*1j*tau)
    mul={2:-24,4:240,6:-504}[k]
    return 1+mul*sum(sigma(n,k-1)*q**n for n in range(1,90))
def theta(v,tau): return m.jtheta(1,m.pi*v,m.exp(m.pi*1j*tau))
def hp(v,tau): return m.diff(lambda z:m.log(theta(z,tau)),v,2)
def wp(v,tau):return -hp(v,tau)-m.pi**2*Ek(tau,2)/3
def mu(tau):return m.findroot(lambda z:wp(z,tau),(.5-.35j,.5-.4j),tol=m.mpf('1e-65'))
def eta(tau):
    q=m.exp(2*m.pi*1j*tau)
    return m.exp(m.pi*1j*tau/12)*m.fprod(1-q**n for n in range(1,90))
def beta6(tau):return (1j/m.pi)*m.log(theta(mu(tau),tau)/eta(tau))
for tau in (m.mpc('0','1.7'),m.mpc('0.2','2')):
    z=mu(tau)
    mup=m.diff(mu,tau)
    d1=m.diff(beta6,tau)-mup**2
    g2=4*m.pi**4*Ek(tau,4)/3
    g3=8*m.pi**6*Ek(tau,6)/27
    d2=-g2**2/(36*m.pi**2*g3)
    sq=-(mup-1j*m.diff(lambda v:m.log(theta(v,tau)),z)/(2*m.pi))**2
    print('tau =',m.nstr(tau,25))
    print('mu =',m.nstr(z,45))
    print('method1 determinant =',m.nstr(d1,45))
    print('method2 determinant =',m.nstr(d2,45))
    print('absolute discrepancy =',m.nstr(abs(d1-d2),6))
    print('square discrepancy =',m.nstr(abs(d1-sq),6))
    assert abs(d1-d2)<m.mpf('1e-55')
    assert abs(d1-sq)<m.mpf('1e-55')

