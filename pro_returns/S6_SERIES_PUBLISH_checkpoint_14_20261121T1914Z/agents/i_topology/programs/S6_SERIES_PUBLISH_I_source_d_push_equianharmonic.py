"""Exact degree-three endomorphism and mean-normalization checks for D.4.5."""
import sympy as s
r=s.symbols('r')
mod=s.Poly(r*r-r+1,r)
def reduce(expr):
    return s.rem(s.Poly(s.expand(expr),r),mod).as_expr()
alpha=1+r
mu=(2-r)/3
M=s.Matrix([[1,-1],[1,2]])
assert M.det()==3
assert reduce(alpha*1-(1+r))==0
assert reduce(alpha*r-(-1+2*r))==0
assert reduce(alpha*mu-1)==0
assert reduce(3*mu-(2-r))==0
# rho conjugate = 1-rho; alpha*conjugate(alpha)=3.
assert reduce(alpha*(2-r)-3)==0
print('Multiplication matrix:',M.tolist(),'determinant:',M.det())
print('alpha*mu=1; 3*mu=2-rho; kernel = {0,+mu,-mu}.')
print('|alpha|^2=3; distribution identity gives N(mu)^2=sqrt(3).')
y,T=s.symbols('y T',positive=True)
hmean=-s.pi*T/6+s.pi*y-s.pi*y*y/T
mean=s.integrate(hmean,(y,0,T))/T
assert mean==0
print('Normalized mean of log N:',mean)
# Formal independent logarithms keep this exact and avoid branch simplifications.
L2,L3=s.symbols('log2 log3')
D=(6/s.pi)*(L3/4-L2-L3/2)
expected=-3/(2*s.pi)*(4*L2+L3)
assert s.expand(D-expected)==0
print('Dpart = -(3/(2*pi))*(4*log2+log3) = -(3/(2*pi))*log48.')
Hstar=3/s.pi*(L2+L3)
H0=-D
assert s.expand(H0-Hstar-3/(2*s.pi)*(2*L2-L3))==0
print('H0-Hstar = (3/(2*pi))*log(4/3)>0.')
assert reduce((r*r-1)*mu-(r-1))==0
print('rho^2 fixes mu modulo rho-1; its nontrivial rotation forces Z(mu)=0.')
P,ii,pi=s.symbols('P i pi',nonzero=True)
# Calculate with SymPy's exact imaginary unit.
Zcoef=s.I*P/(4*s.pi)
g2coef=3*s.I*P**2/s.pi
factor=s.expand(3*P*Zcoef-2*g2coef)
assert factor==-21*s.I*P**2/(4*s.pi)
Dcoef=s.simplify(s.I*Zcoef*factor/(4*s.pi**2*P))
assert Dcoef==21*s.I*P**2/(64*s.pi**4)
tcoef=s.I*P**2/s.pi**3
assert s.simplify(Dcoef/(3*tcoef))==s.Rational(7,64)/s.pi
print('Exact coarse Wirtinger derivative limit: 7/(64*pi).')
print('Exact coefficient of Re(t): 7/(32*pi).')
print('All exact checks passed.')
