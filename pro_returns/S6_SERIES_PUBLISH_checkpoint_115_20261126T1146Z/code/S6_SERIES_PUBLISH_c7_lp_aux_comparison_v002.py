#!/usr/bin/env python3
"""Post-exposure exact LP identities; retained v001 used structural equality."""
from datetime import datetime, timezone
import sympy as S

print("Post-exposure auxiliary version002 UTC",datetime.now(timezone.utc).isoformat(),flush=True)
print("The successful historical run is preserved and is not repeated.",flush=True)
d,k,ell,n0,n1,P = S.symbols("d k ell n0 n1 P", integer=True)
C0 = S.Matrix([-2*d*n0,-k,0,0])
C1 = S.Matrix([-3*d*n1,2*ell,0,0])
combination = -P*(2*ell*C0+k*C1)
expected = S.Matrix([d*P*(4*ell*n0+3*k*n1),0,0,0])
assert (combination-expected).applyfunc(S.expand) == S.zeros(4,1)
print("Thom combination",combination.T,"= d P^2 s = d s for P=+/-1",flush=True)
print("Critical preimage xi-values: d*1+d*0+(-6*d) =",S.expand(d-6*d),flush=True)
print("Chosen cap1 Thom coefficient = -k*P; C=-5d*s gives link = 5*k*P",flush=True)
A = S.Matrix([[0,1],[-1,0]])
for matrix,U,V in [
    (A,S.Matrix([[-1,0],[1,-1]]),S.Matrix([[1,1],[0,1]])),
    (A.inv(),S.Matrix([[-1,0],[-1,-1]]),S.Matrix([[1,-1],[0,1]])),
]:
    assert U.det() == V.det() == 1
    assert U*(matrix-S.eye(2))*V == S.diag(1,2)
    print("Order4 matrix",matrix.tolist(),"U",U.tolist(),"Uinv",U.inv().tolist(),
          "V",V.tolist(),"Vinv",V.inv().tolist(),"diagonal",S.diag(1,2).tolist(),flush=True)
x,y,j,h = S.symbols("x y j h",integer=True)
phi=-x*(x-1)/S.Integer(2)+3*y*y
psi=-x*(x-1)/S.Integer(2)+3*y*(y-1)
assert S.expand(psi-phi) == -3*y
assert S.expand(phi.subs(y,y+d)-phi) == 6*d*y+3*d*d
assert S.expand(psi.subs(y,y+d)-psi) == 6*d*y+3*d*d-3*d
print("Support difference",S.expand(psi-phi),"; forward monomial z2^-3, inverse z2^3",flush=True)
print("Gamma factor ratio q^(-3d)*unit_gamma^(-3); same actual ratio for every period.",flush=True)
for sign in (-1,1):
    total=S.expand(S.summation((h+sign*6*j)**2,(j,0,d-1)))
    quotient=h*h+sign*6*h*(d-1)+6*(d-1)*(2*d-1)
    assert S.expand(total-d*quotient) == 0
    print("Independent pure-cube identity sign",sign,"sum/d",S.expand(quotient),flush=True)
print("PASS: all focused exact identities; no fresh whole-LP credit.",flush=True)
