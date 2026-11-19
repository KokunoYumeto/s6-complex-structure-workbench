"""Exact extension of the relative normal-form calculation to two order-six spectra."""
from fourfolds_relative_normalform import *

# The same equations also give the two repeated-negative order-six loci.
a=S.symbols('a')
ba=b.copy();ba[8]=a-1;ba[9]=1-a
YA=S.Matrix(2,5,list((E_inverse*ba).applyfunc(S.factor)))
print('trace-parameter first column=',[S.factor(YA[i,0]) for i in range(2)])
for avalue in (-1,0,1):
    Yv=YA.subs(a,avalue)
    Cv=((I+X*Yv)*A).applyfunc(S.factor)
    assert S.factor(Cv.charpoly(x).as_expr()-(x-1)*(x+1)**2*(x*x-avalue*x+1))==0
    minimal=(x-1)*(x+1)*(x*x-avalue*x+1)
    assert zero((Cv-I)*(Cv+I)*(Cv*Cv-avalue*Cv+I))
    assert S.rem(x**(4 if avalue==0 else 6)-1,minimal,x)==0
    print('trace parameter',avalue,'finite-order and characteristic identities PASS')
    for point in ((3,2,1),(4,1,3)):
        E=D.subs(dict(zip((r,s,t),point)))
        bv=ba.subs(a,avalue)
        print('trace parameter',avalue,'exception point',point,'aug rank',E.row_join(bv).rank())
print('ALL SYMBOLIC CHECKS PASSED')

u=S.symbols('u')
Qminus=r*r-r*s+s*t
assert S.factor(DD.subs({r:u,s:1,t:u-u*u})+(7*u*u-11*u+7)*(u**4-u**3+u*u-u+1))==0
assert S.expand((u*u-u/2)**2+S.Rational(3,4)*(u-S.Rational(2,3))**2+S.Rational(2,3)-(u**4-u**3+u*u-u+1))==0
YE6=S.Matrix([[4*z+S.Rational(26,5),0,-2*z-2,-2*z-S.Rational(1,5),2*z+1],
               [2*z-S.Rational(2,5),0,-z,S.Rational(2,5)-z,z]])
CE6=(I+XE*YE6)*A
assert zero(YE6*XE) and zero(YE6*R*XE-S.eye(2))
assert zero((CE6-I)*(CE6+I)*(CE6*CE6+CE6+I))
print('irreducibility conic and full exceptional order-six line: exact PASS')
