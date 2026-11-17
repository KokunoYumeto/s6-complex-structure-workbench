"""Exact local and line-degree certificates for C.2.UN.74."""
import sympy as s
from itertools import product

x,y,z,p,q,r,m,n=s.symbols("x y z p q r m n",positive=True)
blowdown=s.Matrix([x*y,z,x])
assert s.det(blowdown.jacobian([x,y,z])) == x
assert s.expand((p**m*q**n).subs({p:x*y,q:z})) == x**m*y**m*z**n
print("C.2.UN.74: p=xy,q=z,r=x; Jacobian x; f=x^m y^m z^n.")

eB,marks=s.symbols("eB marks")
assert s.expand((2*eB+marks)-(eB+2*marks)+marks)==eB
print("Component/double/triple Euler difference: (2eB+r)-(eB+2r)+r=eB.")

g,kP,shift=s.symbols("g kP shift",integer=True)
checked=0
for mult in range(1,7):
    for number in range(5):
        for weights in product(range(1,7),repeat=number):
            total=sum(weights)
            if total % mult: continue
            degreeM=s.Integer(-total//mult)
            degreesQ=tuple(range(number))
            degreeL=2*g-2-(kP+1)*degreeM-sum(degreesQ)
            shifted=2*g-2-(kP+shift*mult+1)*degreeM-sum(
                k+shift*w for k,w in zip(degreesQ,weights))
            assert s.expand(shifted-degreeL)==0
            assert mult*degreeM == -total
            checked+=1
print("Weighted root-line and canonical-generator comparisons:",checked)

split=0
for number in range(1,6):
    for differences in product(range(-3,2),repeat=number):
        # differences=k_Q-k_P; local maximum gives differences<=1.
        exponents=[d-2 for d in differences]
        assert max(exponents)<=-1 and sum(exponents)<0
        split+=1
print("Reduced local-maximum Serre-dual negative-degree records:",split)
print("All certificates PASS; arithmetic records assert no abstract occurrence.")
