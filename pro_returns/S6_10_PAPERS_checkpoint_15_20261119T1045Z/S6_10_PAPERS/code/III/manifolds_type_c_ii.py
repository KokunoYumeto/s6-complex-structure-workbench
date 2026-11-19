"""D.2.11: explicit OS49 IV*+II+I2 geometry and all-order topology.

The linearization divisor is one I2 component. Q=3P exchanges the
two I2 components; the norm divisor is the full fibre. This is
outside the public engine's local-narrowness input restriction.
All matrices below are explicit and checked directly; the engine
is not called or altered. The full geometric proof is in D.2.11.
"""
from pathlib import Path
from math import gcd
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

ROOT=Path(__file__).resolve().parents[1]
t=s.symbols('t')
f=-3*t**3*(t-1)
g=t**4*(t-1)*(2*t-1)
disc=s.factor(4*f**3+27*g**2)
assert disc==27*t**8*(t-1)**2
assert s.expand(t**4-(t**6+f*t**2+g))==0
j=s.factor(1728*4*f**3/disc)
assert s.expand(j-6912*t*(1-t))==0
print('Weierstrass coefficients:',f,g)
print('Section P=(t^2,t^2); 4f^3+27g^2=',disc,'; j=',j)

# Marked homology matrices, in fibre order II, IV*, I2.
# The first two are the Poincare lifts at locally narrow finite fibres;
# the last is forced by the global product relation. No narrowness at
# I2 is assumed in deriving it.
MII=s.Matrix([[1,1,0,0],[-1,0,0,0],[0,0,1,0],[0,0,0,1]])
MIV=s.Matrix([[0,-1,0,0],[1,-1,0,-3],[0,1,1,1],[0,0,0,1]])
MI2=s.Matrix([[1,2,0,3],[0,1,0,0],[0,-1,1,-1],[0,0,0,1]])
assert MII*MIV*MI2==s.eye(4)
assert MII**6==MIV**3==s.eye(4)
assert (MI2-s.eye(4))**2==s.zeros(4)
T1=s.Matrix([[1,-3,0,1],[0,-1,1,1],[0,-1,0,0],[0,0,0,1]])
T2=s.Matrix([[1,0,0,0],[0,0,-1,0],[0,1,1,0],[0,0,0,1]])
S=s.Matrix([[0,0,-1,0],[0,-1,1,1],[0,0,0,1],[-1,0,3,0]])
assert S.det()==-1
U=MIV;V=U.inv()*MII*U
assert U.inv().T*S==S*T1
assert V.inv().T*S==S*T2
print('Integral conjugacy to Yang Type C after the finite Hurwitz reorder:',S)
print('Conjugacy determinant:',S.det())

k,n=s.symbols('k n',integer=True)
D=s.Matrix([[-1,1,0,1,0,0,0],
            [k,-k,3*k,0,0,0,-n],
            [0,0,0,-1,0,0,0],
            [0,0,1,0,0,0,0]])
C=s.Matrix([[1,0,0],[-k,3*k,-n],[0,1,0]])
assert C.det()==n
print('Full 4x7 Mayer--Vietoris matrix:',D)
print('Unrestricted reduced matrix:',C,'; determinant=',C.det())
checked=0
for kval in range(1,13):
    for nval in range(-15,16):
        if gcd(nval,3*kval)!=1:continue
        DD=D.subs({k:kval,n:nval})
        sn=smith_normal_form(DD,domain=s.ZZ)
        factors=[abs(int(sn[i,i])) for i in range(4)]
        assert factors==[1,1,1,abs(nval)]
        checked+=1
print('Full Smith cases:',checked,'; 1<=k<=12,-15<=n<=15,gcd(n,3k)=1.')
print('For every k>0,n=+/-1,r arbitrary: pi1=0 and integral homology of S6.')
payload=dict(theorem='D.2.11',f=str(f),g=str(g),discriminant=str(disc),j=str(j),
             P=['t^2','t^2'],Q='3P',linearization_divisor='identity component C0 of I2',
             matrices=[x.tolist() for x in (MII,MIV,MI2)],
             conjugacy=S.tolist(),full_matrix=D.tolist(),reduced=C.tolist(),
             checks=checked)
(Path(__file__).resolve().parent/'manifolds_type_c_ii.json').write_text(
    json.dumps(payload,indent=2,default=lambda x:int(x) if isinstance(x,s.Integer) else str(x))+'\n')
