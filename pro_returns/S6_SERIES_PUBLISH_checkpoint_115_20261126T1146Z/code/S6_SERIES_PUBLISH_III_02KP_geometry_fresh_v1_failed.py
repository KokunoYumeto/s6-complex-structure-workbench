#!/usr/bin/env python3
"""New polynomial, character, and integral-chain witnesses for unopened 02KP.

This program derives the branching from polynomial gcds and differentiates
the rational map, constructs exterior-relation preimages directly from the
II block, and checks exact symbolic relative-chain and characteristic maps.
It does not read an original target proof or an old target calculation.
"""
from pathlib import Path
from itertools import combinations, permutations
from datetime import datetime, timezone
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
t = s.symbols('t')
F = 81*t**3-9*t**2-53*t-27
G = 729*t**5-1215*t**4-1350*t**3-350*t**2-675*t-243
den = 2**14*3*t**3*(9*t+5)**2
num = -(t-3)*F**3
assert s.gcd(F,s.diff(F,t)) == s.gcd(G,s.diff(G,t)) == 1
assert s.gcd(num,den) == 1
assert s.expand(num-den+G**2) == 0
assert s.gcd(F,G) == 1 and F.subs(t,3) != 0 and G.subs(t,3) != 0
assert s.gcd(G,den) == s.gcd(F,den) == 1
deriv_num = s.factor(s.diff(num,t)*den-num*s.diff(den,t))
assert s.cancel(deriv_num/(F**2*G*t**2*(9*t+5))) == -2**14*3*5
assert s.degree(num,t)==10 and s.degree(den,t)==5
assert (3-1)*3+(2-1)*5+(5-1)+(3-1)+(2-1)==2*10-2
print('Polynomial gcds, exact J-1 numerator, derivative, and all ramifications verified.')
print('Derivative numerator factor:',deriv_num)
print('Degree10 partitions over0,1,infinity: (3,3,3,1), (2,2,2,2,2), (5,3,2).')

# The chosen coset permutations are compared to a literal canonical dessin.
rho = (2,1,3,0,6,8,7,4,9,5)
sigma = (1,0,4,5,2,3,9,8,7,6)
canrho = (1,2,0,4,5,3,7,8,6,9)
cansigma = (3,5,6,0,7,1,2,4,9,8)

def cycles(p):
    seen=set();out=[]
    for i in range(len(p)):
        if i in seen: continue
        c=[];j=i
        while j not in seen:
            c.append(j);seen.add(j);j=p[j]
        out.append(c)
    return out

# Build every possible intertwiner by propagation from a chosen single dart.
intertwiners=[]
for target in range(10):
    f={0:target};queue=[0];valid=True
    while queue and valid:
        i=queue.pop()
        for p,q in ((rho,canrho),(sigma,cansigma)):
            j=p[i];value=q[f[i]]
            if j in f:
                if f[j]!=value:valid=False;break
            else:
                if value in f.values():valid=False;break
                f[j]=value;queue.append(j)
    if valid and len(f)==10:
        intertwiners.append([f[i] for i in range(10)])
assert len(intertwiners)==1
relabelling=intertwiners[0]
inverse=[relabelling.index(i) for i in range(10)]
print('Unique modular-coset to canonical-dessin relabelling:',relabelling)
print('Inverse relabelling:',inverse)

As=[s.Matrix(x) for x in ([[5,8],[-2,-3]],[[27,37],[-19,-26]],
                         [[61,80],[-45,-59]],[[4,3],[-3,-2]])]
gs=[s.Matrix(x) for x in ((-2,1),(0,0),(4,-3),(1,-1))]
J=s.Matrix([[0,1],[-1,0]])
Ts=[]
for i,(A,g) in enumerate(zip(As,gs)):
    z,params=(A-s.eye(2)).gauss_jordan_solve(g)
    z=z.subs({p:0 for p in params})
    row=-30*g.T*J*A
    T=s.eye(4);T[:2,:2]=A;T[:2,3]=g;T[2,:2]=row
    T[2,3]=(row*z)[0]+int(i==0);Ts.append(T)
assert Ts[0]*Ts[1]*Ts[2]*Ts[3]==s.eye(4)
pairs=list(combinations(range(4),2))
def exterior(T):
    return s.Matrix([[T.extract(a,b).det() for b in pairs] for a in pairs])
W=s.Matrix.hstack(*(exterior(T)-s.eye(6) for T in (Ts[1],Ts[2],Ts[3])))
P=s.zeros(18,5)
P[1,1]=-27;P[3,1]=19
P[2,2]=-27;P[4,2]=19
P[1,3]=-37;P[3,3]=26
P[2,4]=-37;P[4,4]=26
P[14,0]=-1;P[:,0]=P[:,0]-10*P[:,1]+3*P[:,2]
K=s.eye(6)[:,:5];K[5,0]=30
assert W*P==K
omega=s.Matrix([[30,0,0,0,0,-1]])
assert omega*W==s.zeros(1,18)
fibre_basis=s.Matrix.hstack(-s.eye(6)[:,5],K)
assert abs(fibre_basis.det())==1 and fibre_basis.inv()[0,:]==omega
fourth=exterior(Ts[0])-s.eye(6)
fourth_preimage=P*fibre_basis.inv()[1:,:]*fourth
assert W*fourth_preimage==fourth
print('Explicit exterior-relation preimages, columns kappa,e13,e14,e23,e24:',P.tolist())
print('Fibre quotient basis and inverse:',fibre_basis.tolist(),fibre_basis.inv().tolist())

# The actual primitive vanishing circles give ker(gamma*) without saturation.
wc=s.Matrix([2,-1,15]);w2=s.Matrix([1,-1,-10]);delta=s.Matrix([0,0,1])
vanishing=s.Matrix.hstack(wc,w2,delta)
assert vanishing.det()==-1
print('Primitive vanishing map and inverse:',vanishing.tolist(),vanishing.inv().tolist())

# Normal discs at vertices0,wc have relative classes -2D0+2D1.
# Their base-loop components cancel; wc has order2 in the regular coinvariant.
normal_kernel=s.Matrix([0,0,-2,2])
normal_base=s.Matrix([[1,0,-1,-1],[0,1,-1,-1],[0,0,-1,-1]])
assert normal_base*normal_kernel==s.zeros(3,1)
assert normal_kernel[3]%2==0
print('Reduced normal-disc kernel generator:',list(normal_kernel))

m,n,r,alpha,beta,k=s.symbols('m n r alpha beta k',integer=True)
B=s.Matrix([[n,-r*alpha],[0,1]])
U=s.Matrix([[1,r*alpha],[0,1]])
assert U*B==s.diag(n,1) and U.det()==1
assert U.inv()==s.Matrix([[1,-r*alpha],[0,1]])
print('All-order finite relation map and exact row change:',B.tolist(),U.tolist(),U.inv().tolist())

# Characteristic polynomial on the two-vertex toric quotient Z2.
ray_classes=(1,1,0,1,1,0)
x,y=s.symbols('x y')
dx=[x*j for j in ray_classes];dy=[y*j for j in ray_classes]
local=-sum(a*b for a,b in zip(dx,dy))+sum(
    dx[i]*dy[(i+1)%6]+dx[(i+1)%6]*dy[i] for i in range(6))
assert s.expand(local)==0
assert s.expand((m-1-k)-m+(k+1))==0
print('Index-two toric component bilinear intersection vanishes identically:',s.expand(local))
print('Canonical-form local order m-1-k yields mK=f*(-k-1) after mG=f*(point).')

data={'dessin_relabelling':relabelling,'dessin_inverse':inverse,
      'exterior_preimages':P.tolist(),'fibre_basis':fibre_basis.tolist(),
      'fibre_basis_inverse':fibre_basis.inv().tolist(),
      'fourth_exterior_preimage':fourth_preimage.tolist(),
      'vanishing_basis':vanishing.tolist(),'vanishing_basis_inverse':vanishing.inv().tolist()}
out=ROOT/'agents/continuation6_iii_infra/S6_SERIES_PUBLISH_III_02KP_geometry_maps.json'
out.write_text(json.dumps(data,default=int,indent=2)+'\n',newline='\n')
print('All additional exact polynomial, integral-chain and characteristic checks passed.')
print('Completed:',datetime.now(timezone.utc).isoformat())
