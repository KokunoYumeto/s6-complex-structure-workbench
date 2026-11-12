"""Two independent special-value computations and an explicitly non-rigorous grid.
Method I: mpmath Jacobi theta (its own theta-series) and eta product.
Method II: Jacobi triple product with 120 terms, evaluated at 90 digits.
No grid output is a certificate for a global maximum.
"""
import mpmath as mp
import cmath,math,json
mp.mp.dps=90
A=5+2*mp.sqrt(6); r=mp.exp(mp.pi*1j/3)
mu0a=mp.mpf('.5')-1j*mp.log(A)/(2*mp.pi)
mu0b=mp.findroot(lambda z:mp.pi**2/mp.sin(mp.pi*z)**2-mp.pi**2/3,(.5-.3j,.5-.4j))
print('mpmath decimal precision:',mp.mp.dps)
print('mu0 log root:',mp.nstr(mu0a,75))
print('mu0 trigonometric root:',mp.nstr(mu0b,75))
print('mu0 discrepancy:',mp.nstr(abs(mu0a-mu0b),5))

def beta_methods(t,z):
 q=mp.exp(2j*mp.pi*t)
 ep=mp.exp(mp.pi*1j*t/12)
 for n in range(1,121):ep*=1-q**n
 theta=mp.jtheta(1,mp.pi*z,mp.exp(mp.pi*1j*t))
 b1=6j/mp.pi*mp.log(theta/(2*mp.sqrt(3)*ep))
 ratio=2*mp.exp(mp.pi*1j*t/6)*mp.sin(mp.pi*z)
 for n in range(1,121):ratio*=1-2*q**n*mp.cos(2*mp.pi*z)+q**(2*n)
 b2=6j/mp.pi*mp.log(ratio/(2*mp.sqrt(3)))
 return b1,b2
for name,t,z in [('z1',r,(2-r)/3),('z2',1j,(1-1j)/2)]:
 b1,b2=beta_methods(t,z)
 print(name,'tau',mp.nstr(t,75),'mu',mp.nstr(z,75))
 print('beta method1',mp.nstr(b1,75))
 print('beta method2',mp.nstr(b2,75))
 print('beta discrepancy',mp.nstr(abs(b1-b2),5))
 print('D',mp.nstr(mp.im(b1)-6*mp.im(z)**2/mp.im(t),75))
print('Exact D(z2)=-(3/pi)log6:',mp.nstr(-3/mp.pi*mp.log(6),75))
print('Corresponding candidate radius exactly216; its square exactly46656.')
# Coarse analytic upper bounds: all ingredients are monotone bounds described in paper.
T0=mp.sqrt(3)/2;r0=mp.exp(-2*mp.pi*T0)
series_bound=1+mp.exp(-mp.pi*T0)/(1-mp.exp(-3*mp.pi*T0))
bound_small=2*mp.exp(mp.pi/6)*series_bound*mp.exp(r0/(1-r0)**2)
r2=mp.exp(-4*mp.pi)
wp_error=1/mp.sinh(mp.pi)**2+8*(r2/(1-r2)**3+mp.mpf('.5')*(mp.exp(-2*mp.pi)/(1-mp.exp(-2*mp.pi))**2+mp.exp(-6*mp.pi)/(1-mp.exp(-6*mp.pi))**2)/(1-r2))
bound_large=2*mp.cosh(mp.pi)*mp.exp(-mp.pi/3)*mp.exp(2*mp.cosh(2*mp.pi)*r2/(1-r2)+r2**2/(1-r2**2))
print('Theta-norm upper bound for sqrt3/2<=T<=2:',mp.nstr(bound_small,40))
print('wp/pi² error for T>=2,1<=|Im mu|<=T/2 (must <1/3):',mp.nstr(wp_error,40))
print('Theta-norm upper bound for T>=2:',mp.nstr(bound_large,40))
print('D upperbound large:',mp.nstr(6/mp.pi*mp.log(bound_large/(2*mp.sqrt(3))),40))
# exact-t4 numerical periods for the explicit counterexample.
def jfun(t):
 q=mp.exp(2j*mp.pi*t)
 E4=1+240*sum(n**3*q**n/(1-q**n) for n in range(1,81))
 E6=1-504*sum(n**5*q**n/(1-q**n) for n in range(1,81))
 return 1728*E4**3/(E4**3-E6**2)
T4=mp.findroot(lambda T:mp.re(jfun(1j*T))-1728*mp.mpf(32)/5,(1.4,1.6))
t4=1j*T4;z4=(2-t4)/4;b4,_=beta_methods(t4,z4)
N=101;target=(mp.mpf(9)/8-mp.mpf(N)/4)*t4-mp.mpf(9)/4;c4=target-b4
print('t=32/5 tau:',mp.nstr(t4,60),'mu:',mp.nstr(z4,60))
print('Counterexample c with N=101:',mp.nstr(c4,60))
print('Counterexample Im c < -2:',mp.im(c4)<-2)
# Complex double Newton and product, independent of mpmath grid evaluation.
pi=math.pi
zstart=complex(mu0a)
def wpfast(z,t):
 q=cmath.exp(2j*pi*t)
 total=pi*pi/cmath.sin(pi*z)**2-pi*pi/3
 deriv=-2*pi**3*cmath.cos(pi*z)/cmath.sin(pi*z)**3
 for n in range(1,31):
  c=q**n/(1-q**n)
  total+=8*pi*pi*n*c*(1-cmath.cos(2*pi*n*z))
  deriv+=16*pi**3*n*n*c*cmath.sin(2*pi*n*z)
 return total,deriv
def Dfast(t):
 if abs(t-1j)<1e-13:z=.5-.5j
 else:
  z=zstart
  for k in range(100):
   v,d=wpfast(z,t);step=v/d
   if abs(step)>0.15:step*=.15/abs(step)
   z-=step
   if abs(step)<2e-14:break
  if abs(wpfast(z,t)[0])>1e-8:raise RuntimeError((t,z))
 q=cmath.exp(2j*pi*t)
 lr=math.log(abs(2*cmath.sin(pi*z)))-pi*t.imag/6
 for n in range(1,31):lr+=math.log(abs(1-2*q**n*cmath.cos(2*pi*z)+q**(2*n)))
 return 6/pi*(lr-math.log(2*math.sqrt(3)))-6*z.imag*z.imag/t.imag
samples=[]
for ix in range(51):
 x=ix/100;y0=math.sqrt(1-x*x)
 for iy in range(101):
  y=y0+(3-y0)*iy/100;t=complex(x,y)
  samples.append((Dfast(t),x,y))
print('Non-certified grid points:',len(samples),'sample maximum:',max(samples))
# Cross-check grid method at selected points with independent mpmath nonlinear root + theta.
for t in [0.1+1j,0.25+1j,0.5+1j,2j,0.5+2j]:
 def wpmp(z):
  q=mp.exp(2j*mp.pi*t)
  return mp.pi**2/mp.sin(mp.pi*z)**2-mp.pi**2/3+8*mp.pi**2*sum(n*q**n/(1-q**n)*(1-mp.cos(2*mp.pi*n*z)) for n in range(1,81))
 z=mp.findroot(wpmp,(mu0a,mu0a+.01));b,_=beta_methods(t,z)
 dm=mp.im(b)-6*mp.im(z)**2/mp.im(t)
 print('grid cross-check',t,'double',Dfast(t),'mpmath',mp.nstr(dm,35),'absolute discrepancy',mp.nstr(abs(dm-Dfast(t)),5))
