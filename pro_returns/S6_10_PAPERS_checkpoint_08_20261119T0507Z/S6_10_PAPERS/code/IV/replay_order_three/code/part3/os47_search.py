"""Exact bounded search for the primitive normal-function lift on I7+III+2I1.

The elliptic tuple is an explicit positive factorization; the normal
function is reconstructed from local component 2 mod7, finite order4,
one rank-two scalar zero, and the sphere relation.
"""
from pathlib import Path
import sympy as s
import json

def tr(v):
    p,q=v
    return s.Matrix([[1-p*q,p*p],[-q*q,1+p*q]])

E7=tr((1,0))**7
E1=tr((0,1))
E2=tr((3,1))
EA=(E7*E1*E2).inv()
assert EA.trace()==0 and EA**2==-s.eye(2)

def lift(E,k,a=7,b=2,c=0):
    p,q,r,t=list(E)
    j,h=list(k)
    return s.Matrix([[1,b*(r*j-p*h),b*(t*j-q*h),c],
                     [0,p,q,a*j],[0,r,t,a*h],[0,0,0,1]])

def finite_lift(E,k,a=7,b=2):
    zero=lift(E,k,a,b,0)
    c=-s.Rational((zero**4)[0,3],4)
    out=lift(E,k,a,b,c)
    assert out**4==s.eye(4)
    return out,c

answers=[]
for r in range(-5,6):
    for t in range(-5,6):
        k7=s.Matrix([2,0])
        k1=r*s.Matrix([0,1])
        k2=t*s.Matrix([3,1])
        kA=-EA*(k7+E7*k1+E7*E1*k2)
        TA,cA=finite_lift(EA,kA)
        T7=lift(E7,k7,c=8)
        T1=lift(E1,k1,c=14*r*r)
        T2=lift(E2,k2,c=14*t*t-1)
        # The rank-one central coefficient is computed invariantly below,
        # because the displayed r,t are coefficients of different vanishing
        # vectors, and their source matrix need not be the upper shear.
        def rankone(E,k):
            c=s.Symbol('c')
            N=lift(E,k,c=c)-s.eye(4)
            pol=[N.extract(i,j).det() for i in [(0,1),(0,2),(1,2)]
                 for j in [(1,2),(1,3),(2,3)]]
            sol=s.solve(pol,c)
            val=sol[c] if isinstance(sol,dict) else 0
            L=lift(E,k,c=val)
            assert (L-s.eye(4)).rank()==1
            return L,val
        T1,c1=rankone(E1,k1)
        T2,c2=rankone(E2,k2)
        T2[0,3]-=1
        product=TA*T7*T1*T2
        if product==s.eye(4) and all(v.q==1 for T in [TA,T7,T1,T2] for v in T):
            answers.append({'r':r,'t':t,'kA':list(map(int,kA)),
                            'cA':int(cA),'c1':int(c1),'c2_without_zero':int(c2),
                            'matrices':[[list(map(int,T.row(i))) for i in range(4)]
                                        for T in [TA,T7,T1,T2]]})

out={'bounds':[-5,5], 'elliptic_tuple':[list(map(list,[E.row(i) for i in range(2)]))
               for E in [EA,E7,E1,E2]],'answers':answers}
# Convert the few SymPy elliptic entries before serializing.
out['elliptic_tuple']=[[[int(x) for x in row] for row in E] for E in out['elliptic_tuple']]
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('elliptic tuple',out['elliptic_tuple'])
print('number of exact lifts',len(answers))
for a in answers: print(a)
