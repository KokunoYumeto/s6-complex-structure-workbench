"""Exact independent geometric-coordinate and marking checks."""
import sympy as s
A1=s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
T0=s.Matrix([[0,-1,-1,0],[1,-1,0,0],[0,0,1,0],[0,0,0,1]])
T1=s.Matrix([[-1,1,-1,2],[-1,0,-1,1],[1,1,2,-1],[0,0,0,1]])
P=s.Matrix([[0,-2,-1,-2],[2,-1,0,-1],[0,2,1,3],[-1,0,0,0]])
assert T0*P==P*A1 and T1*P==P*A2 and P.det()==-1
print('Engel common-basis P=',P.tolist(),'; det=',P.det())
print('T0 P=P A1 and T1 P=P A2: exact')
eps=s.Matrix([1,2,-4,0]);epsp=s.Matrix([1,3,-3,0]);d=s.Matrix([0,0,0,1])
print('P eps=',list(P*eps),'P epsprime=',list(P*epsp),'P delta=',list(P*d))
assert P*eps==s.Matrix([0,0,0,-1])
assert P*epsp==s.Matrix([-3,-1,3,-1])
assert P*d==s.Matrix([-2,-1,3,0])
assert s.Matrix([[0,0,0,1]])*P==s.Matrix([[-1,0,0,0]])
# Alternative independent check via Viaclovsky's published intermediate basis.
U=s.Matrix([[-2,1,0,-2],[-1,0,0,0],[3,-1,1,0],[0,0,0,1]])
V0=s.Matrix([[1,-1,0,2],[0,-1,-1,6],[0,1,0,0],[0,0,0,1]])
V1=s.Matrix([[1,0,1,-3],[0,0,1,0],[0,-1,0,6],[0,0,0,1]])
assert U*V0==T0*U and U*V1==T1*U
print('independent Viaclovsky intermediate-basis check: passed')
C=s.Matrix([[2,-1,0,0,0,0],[-1,2,-1,0,-1,0],[0,-1,2,-1,0,0],[0,0,-1,2,0,0],[0,-1,0,0,2,-1],[0,0,0,0,-1,2]])
Ci=s.Matrix([[6,9,6,3,6,3],[9,18,12,6,12,6],[6,12,10,5,8,4],[3,6,5,4,4,2],[6,12,8,4,10,5],[3,6,4,2,5,4]])/3
assert C*Ci==s.eye(6)
print('E6 determinant=',C.det(),'; diagonal endpoint inverse entries=',Ci[3,3],Ci[5,5])
print('minimal nonzero section height=',2-Ci[3,3]-s.Rational(1,2))
X,T=s.symbols('X T')
H=X**2*T+(2+3*X)*T**2-(4*X+3*X**2)*T**3+2*X**2*T**4
cs=s.symbols('c2:7');T0series=sum(cs[i-2]*X**i for i in range(2,7))
eq=s.Poly(s.series(s.diff(H,T).subs(T,T0series),X,0,7).removeO(),X)
sol=s.solve(eq.all_coeffs(),cs,dict=True)[0]
t0=T0series.subs(sol)
ht=s.series(H.subs(T,t0),X,0,7)
assert s.expand(ht.removeO()).coeff(X,4)==-s.Rational(1,8)
print('critical T0 series=',t0)
print('H(X,T0)=',ht)
A=5+2*s.sqrt(6);uu=-A
XX=s.simplify(1+12*uu/(uu-1)**2)
YY=s.simplify(12*s.sqrt(3)*uu*(uu+1)/(uu-1)**3)
assert XX==0 and s.simplify(YY+s.sqrt(2))==0
print('cusp P coordinates for U=-(5+2sqrt6):',XX,YY)
print('ALL EXACT GEOMETRIC CHECKS PASSED')
# Reflection identities used by the antiholomorphic classification.
H=s.Matrix([[1,0,0,0],[0,1,0,0],[-6,0,-1,0],[0,-1,0,-1]])
assert H**2==s.eye(4)
assert H*A2*H==A2.inv()
assert H*A1*H==A2.inv()*A1.inv()*A2
assert -A2*H*eps==-eps+d
assert -H*(-epsp)==epsp-3*d
print('reflection H=',H.tolist())
print('reflection twisted targets:',list(-A2*H*eps),list(H*epsp))
t,m,b=s.symbols('tau mu beta');v=(t,m,b)
def G1(v):
 t,m,b=v;return ((t-1)/t,(1-m)/t,b+2-6*(1-m)**2/t)
def G2(v):
 t,m,b=v;return(-1/t,1+m/t,b-3-6*m*m/t)
def G1i(v):
 t,m,b=v;return(1/(1-t),1-m/(1-t),b-2+6*m*m/(1-t))
def G2i(v):
 t,m,b=v;return(-1/t,(1-m)/t,b+3-6*(1-m)**2/t)
def K(v):
 t,m,b=v;return(-t,1-m,-b)
for left,right in [(K(G1(K(v))),G2i(G1i(G2(v)))),(K(G2(K(v))),G2i(v))]:
 assert all(s.cancel(x-y)==0 for x,y in zip(left,right))
print('reflected full affine period laws: exact rational identities')
# The sign-label correction to course Section10.2.
Tvar=s.symbols('t')
print('course visible P_*: (y/t^2)|_(t=0)=',s.sqrt(2)*(Tvar-1).subs(Tvar,0))
print('ALL REFLECTION CHECKS PASSED')
