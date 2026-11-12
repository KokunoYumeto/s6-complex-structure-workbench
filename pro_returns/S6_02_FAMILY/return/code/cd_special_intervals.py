import mpmath as m
v=m.iv;v.dps=60
pi=v.pi
cosh=lambda x:(v.exp(x)+v.exp(-x))/2
sinh=lambda x:(v.exp(x)-v.exp(-x))/2
r=v.exp(-pi*v.sqrt(3));T=v.sqrt(3)/2;U=-v.sqrt(3)/6;ch=cosh(pi/v.sqrt(3))
L=v.ln(2*cosh(pi/(2*v.sqrt(3))))-pi*T/6
N=40
for n in range(1,N+1):L+=v.ln(1+2*(-r)**n*ch+r**(2*n))
# |log(1+x)|<=|x|/(1-|x|); sum of omitted errors.
first=2*ch*r**(N+1)+r**(2*(N+1))
e=(2*ch*r**(N+1)/(1-r)+r**(2*N+2)/(1-r*r))/(1-first)
L+=v.mpf([-e.b,e.b])
beta1=6/pi*(L-v.ln(2*v.sqrt(3)))
beta2=v.mpf(3)/2-3/pi*v.ln(6)
kappa1=beta1+2*U;kappa2=beta2-v.mpf(3)/2
print('beta1 imaginary interval',beta1)
print('beta2 imaginary interval',beta2)
print('kappa1-kappa2 imaginary interval',kappa1-kappa2)
assert (kappa1-kappa2).a>v.mpf('-.2');assert (kappa1-kappa2).b<v.mpf('-.1')
# Strong cusp bound, all tau with T>=2, wp(mu)=0.
r2=v.exp(-4*pi);b=v.mpf('.43')
err=1/sinh(pi*b)**2+8*(r2/(1-r2)**3+v.mpf('.5')*(v.exp(-2*pi)/(1-v.exp(-2*pi))**2+v.exp(-6*pi)/(1-v.exp(-6*pi))**2)/(1-r2))
NB=2*cosh(pi*b)*v.exp(-pi/3-pi*b*b/2)*v.exp(2*cosh(2*pi*b)*r2/(1-r2)+r2*r2/(1-r2*r2))
print('wp zero exclusion error for absImmu>=.43,T>=2',err)
print('Cusp theta norm upper bound T>=2',NB)
assert err.b<v.mpf(1)/3;assert NB.b<v.mpf('1.1')
print('All inequalities certified.')
M=-3/pi*v.ln(6)
print('Certified M',M)
print('Radius from interval exponential',v.exp(-pi*M))
print('Independent exact integer radius',6**3)
print('u radius from interval exponential',v.exp(-2*pi*M))
print('Independent exact integer u radius',6**6)
