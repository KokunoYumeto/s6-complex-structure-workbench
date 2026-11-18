"""Exact symbolic checks for Part D. No numerical theorem is inferred here."""
import sympy as S
x,y,T,R,a,Bre,Bim,p,q,r,mg=S.symbols('x y T R a Bre Bim p q r mg', real=True)
M=S.Matrix([[1,R,0,6*x],[0,T,0,6*y],[S.Rational(1,2),S.Rational(1,2)+x,1,a+Bre],[0,y,0,Bim]])
D=Bim-6*y*y/T
print('real period determinant:', S.factor(M.det()))
assert S.simplify(M.det()-T*D)==0
num=mg-r*a-6*p*x-6*y*(q-p*R-r*x)/T-r*Bre
t=num/D
cov=S.Matrix([p,(q-p*R-r*x-t*y)/T,r,t])
print('dual covector equation:', [S.simplify(v) for v in (M.T*cov)])
assert S.simplify((M.T*cov)[0]-(p+r/2))==0
assert S.simplify((M.T*cov)[1]-(q+r/2))==0
assert S.simplify((M.T*cov)[2]-r)==0
assert S.simplify((M.T*cov)[3]-mg)==0
print('quadratic normal form numerator:', S.expand(num.subs({mg:r*a,R:0,T:1,Bre:6*x*y})))
assert S.expand(num.subs({mg:r*a,R:0,T:1,Bre:6*x*y}))==-6*p*x-6*q*y
print('quadratic determinant factor:',S.expand(D.subs({Bim:-3*(x*x-y*y),T:1})))
n=S.symbols('n', positive=True,integer=True)
model=M.subs({x:1/n,y:0,T:1,R:0,a:0,Bre:0,Bim:-3/n**2})
coeff=S.Matrix([-6*n,0,3*n,n*n])
print('Lead 9 counterexample lattice vector:', list(model*coeff))
assert model*coeff==S.Matrix([0,0,0,-3])
A=S.symbols('A', positive=True)
g2=4*S.pi**4*A**2
# A=theta_2(i)^4=theta_4(i)^4.
e2prime=2*S.pi**3*S.I*A**2/3
print('e2prime/g2:',S.simplify(e2prime/g2))
assert S.simplify(e2prime/g2)==S.I/(6*S.pi)
print('h^2 coefficient in tau-i:',S.simplify(e2prime/(g2/4)))
print('tau-i coefficient in h^2:',S.simplify((g2/4)/e2prime))
E4=S.symbols('E4', positive=True)
alpha=-3*S.pi*S.I/2
print('t-1 coefficient in h^4:',S.simplify(-S.pi**2*E4*alpha**2))
for den in range(1,13):
    period=S.Rational(S.gcd(den,2),2*den)
    print('a denominator',den,'central circle period',period,'dual generator',S.ilcm(2,den))
print('ALL EXACT CHECKS PASSED')
