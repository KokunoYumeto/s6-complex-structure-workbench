import sympy as s
T=s.symbols('t');a=-s.Rational(3,4)*T**3*(T-1);b=s.Rational(1,4)*T**4*(T-1)**2;y=T**2*(T-1)/2
ps={1:s.Integer(1),2:2*y,3:-a*a,4:4*y*(-8*b*b-a**3)}
ps[5]=s.factor(ps[4]*ps[2]**3-ps[3]**3)
ps[6]=s.factor(ps[3]*(ps[5]*ps[2]**2-ps[4]**2)/(2*y))
for k in range(2,7):print('psi_%d(P) ='%k,s.factor(ps[k]))
print('gcd non-singular factors psi4 psi6:',s.gcd(5*T-32,11*T*T-6016*T+8192))
print('psi6 factor discriminant:',s.discriminant(11*T*T-6016*T+8192,T))
C=s.Matrix([[2,-1,0,0,0,0],[-1,2,-1,0,0,0],[0,-1,2,-1,-1,0],[0,0,-1,2,0,0],[0,0,-1,0,2,-1],[0,0,0,0,-1,2]])
print('E6 Cartan determinant:',C.det(),'inverse diagonal:',list(C.inv().diagonal()))
print('height P =',2-s.Rational(4,3)-s.Rational(1,2))
print('n=6k intersections:',[(k,3*k*k-1) for k in range(1,6)])
# At t4, mu=(2-tau)/4; map L=3*zeta1+4*zeta2.
tau,N=s.symbols('tau N');mu=(2-tau)/4;beta=(s.Rational(9,8)-N/4)*tau-s.Rational(9,4)
cols=[(6*mu,beta),(tau,mu),(1,0),(0,1)]
print('Counterexample images of four periods:',[s.expand(3*x+4*y) for x,y in cols])
# Integral NS test at fixed tau,mu: beta=-3n²tau+12nmu.
n=s.symbols('n',integer=True)
E=s.zeros(4);E[0,2]=-3*n*n;E[0,3]=6*n;E[1,2]=-n;E[1,3]=1
E=E-E.T
print('Projective sequence c1 matrix:',E)
print('Pfaffian:',s.factor(E[0,1]*E[2,3]-E[0,2]*E[1,3]+E[0,3]*E[1,2]))
# Actual algebraic-dimension-one period locus beta=-6tau-12mu.
a0,b0=s.symbols('a0 b0',integer=True)
eta=s.zeros(4);eta[0,3]=6;eta[1,2]=1;eta=eta-eta.T
iso=s.zeros(4);iso[0,2]=-6;iso[0,3]=-6;iso[1,2]=1;iso[1,3]=1;iso=iso-iso.T
F=a0*eta+b0*iso
print('a=1 locus Pfaffian:',s.expand(F[0,1]*F[2,3]-F[0,2]*F[1,3]+F[0,3]*F[1,2]))
mu=s.symbols('mu');beta=-6*tau-12*mu
print('a=1 locus period equation:',s.expand(iso[0,1]-iso[0,2]*tau+(6*iso[1,2]-iso[0,3])*mu+iso[1,3]*beta+iso[2,3]*(6*mu**2-tau*beta)))
