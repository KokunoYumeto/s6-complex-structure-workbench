"""Diagnostics for A.4.7; exact identities are proved in the text.

The numerical tests below check constants and branches, not theorem validity.
"""
import mpmath as mp
import sympy as sp

mp.mp.dps=60
a=mp.mpf(17); B=12*mp.sqrt(2); arc=mp.log(3/(2*mp.sqrt(2)))
R=mp.acosh(a)

def K(s,k):
    return 2**(s-1)*mp.gamma((s+1j*k)/2)*mp.gamma((s-1j*k)/2)/mp.gamma(s)
def H_quad(s,k):
    # Evenness reduces the Fourier transform to a cosine transform.
    # Exponential tails after 160 are less than exp(-80) on Re(s)=1/2.
    return 2*mp.quad(lambda u:(a+B*mp.cosh(u))**(-s)*mp.cos(k*u),
                    list(range(0,161,2)))
def H_euler(s,k):
    alpha=mp.e**arc
    return ((2/B)**s*alpha**(-s-1j*k)
        *mp.beta(s+1j*k,s-1j*k)
        *mp.hyp2f1(s,s+1j*k,2*s,1-alpha**(-2)))
def H_legendre(s,k):
    return (mp.sqrt(2*mp.pi/B)
        *mp.gamma(s+1j*k)*mp.gamma(s-1j*k)/mp.gamma(s)
        *mp.legenp(-mp.mpf(".5")+1j*k,mp.mpf(".5")-s,a/B,type=3))
def phase(rho):
    q=mp.sqrt(B*B+rho*rho)
    xi=mp.log((q+a*rho)/(B*mp.sqrt(1-rho*rho)))
    S=mp.log(a+q)-mp.log(1-rho*rho)/2-rho*xi
    amp=(1-rho*rho)**mp.mpf(".25")/mp.sqrt(q)
    return S,amp,xi

x=sp.symbols('x',positive=True)
U=(3*x+2*sp.sqrt(2))/(2*sp.sqrt(2)*x+3)
assert sp.simplify(x*sp.diff(U,x)/U-1/(17+6*sp.sqrt(2)*(x+1/x)))==0
c=sp.symbols('c',real=True)
assert sp.expand((17-12*c)**2+144*(c*c-1)
                 -(288*c*c-408*c+145))==0
assert sp.factor(288*c*c-408*c+145-25*c*c)==(c-1)*(263*c-145)
print("Exact Mobius weight and complex-shift lower-bound polynomial: PASS")
print("R=",mp.nstr(R,30),"arc=",mp.nstr(arc,30))
for t,k in [(0,0),(2,0),(2,1),(2,4),(5,3),(5,8)]:
    s=mp.mpf(".5")+1j*t
    q=H_quad(s,k); e=H_euler(s,k); l=H_legendre(s,k)
    scale=max(mp.mpf(1),abs(q))
    e1=abs(e-q)/scale;e2=abs(l-q)/scale
    print("t,k",t,k,"quad/Euler",mp.nstr(e1,6),"quad/Legendre",mp.nstr(e2,6))
    assert e1<mp.mpf("1e-28") and e2<mp.mpf("1e-28")
assert abs(H_euler(1,0)-2*arc)<mp.mpf("1e-50")
assert abs(H_euler(mp.mpf(".5")+2j,0)
           -2*mp.legenq(-mp.mpf(".5")+2j,0,a,type=3))<mp.mpf("1e-50")
print("Constant mode and standard Legendre Q normalization: PASS")
for rho in [mp.mpf(0),mp.mpf(".2"),mp.mpf(".6"),mp.mpf("-.6")]:
    S,amp,xi=phase(rho)
    derivative=mp.diff(lambda z:phase(z)[0],rho)
    assert abs(derivative+xi)<mp.mpf("1e-50")
    time=S-rho*derivative
    assert abs(time-mp.asinh(B*mp.cosh(xi)))<mp.mpf("1e-50")
    print("rho",rho,"xi",mp.nstr(xi,12),"canonical time",mp.nstr(time,12))
    for t in [40,80,160]:
        k=rho*t
        m=H_euler(mp.mpf(".5")+1j*t,k)/K(mp.mpf(".5")+1j*t,k)
        rel=m/(amp*mp.exp(-1j*t*S))-1
        print("  stationary t",t,"relative error",mp.nstr(abs(rel),7),
              "t*error",mp.nstr(t*abs(rel),7))
print("All exact/special-function checks PASS; stationary errors scale as O(1/t).")
