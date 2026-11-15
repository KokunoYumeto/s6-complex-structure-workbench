"""Exact checks of the endpoint change of variables and stationary algebra."""
import sympy as s

B,D,v,q=s.symbols('B D v q',positive=True)
C=(q+1/q)/2
S=(q-1/q)/2
a2=B**2+1
N0=B*C-a2*S/D
N1=-v*S/D
N2square=a2*(C-B*S/D)**2
res=s.factor((N0**2-N1**2+1-N2square)*D**2)
num=s.together(res).as_numer_denom()[0]
rem=s.rem(s.Poly(num,D),s.Poly(D**2-(a2-v**2),D)).as_expr()
print('Normal-square identity remainder:',s.simplify(rem))
assert s.simplify(rem)==0
inner=s.simplify(B*N0-a2*(C-B*S/D)+C)
print('Translated-source inner-product identity:',inner)
assert inner==0

ell=s.symbols('ell',real=True)
Dv=s.sqrt(a2-v**2)
F=-B*s.cosh(ell)+Dv*s.sinh(ell)
Fvv=s.diff(F,v,2)
res=s.simplify(Fvv+a2*s.sinh(ell)/Dv**3)
print('F_vv = -a^2 sinh(ell)/D^3 residual:',res)
assert res==0
E=Dv*s.cosh(ell)-B*s.sinh(ell)
print('F_ell = E residual:',s.simplify(s.diff(F,ell)-E))
assert s.simplify(s.diff(F,ell)-E)==0

curv=s.simplify(a2*s.sinh(ell)/(Dv**3*E))
special=s.simplify(curv.subs({B:12*s.sqrt(2),v:0,ell:s.acosh(3)}))
print('Shortest stationary curvature:',special)
assert s.simplify(special-2*s.sqrt(2)/51)==0
print('All exact algebraic checks passed.')
