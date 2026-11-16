"""Independent audit of the real cap transport and all four reflection lifts.

The calculation uses exact integer congruences.  The 24-grid meets every
component because all affine denominators divide 12 and the two nonzero
Smith factors of the fixed equations are 1 and 2.  Component counts are
also bounded, independently, by those Smith factors.
"""
from pathlib import Path
from itertools import combinations
import numpy as np
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form

A1=s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
H=s.Matrix([[1,0,0,0],[0,1,0,0],[-6,0,-1,0],[0,-1,0,-1]])
E=s.zeros(4); E[3,0]=1
d=s.Matrix([0,0,0,1]); w=s.Matrix([0,0,1,0]); u=s.Matrix([0,1,0,0])
v=s.Matrix([-1,-3,3,0]); assert A2*v==v
R=-H-E; Rm=A2.inv()*R; Rl=(A1*A2).inv()*R
B=Rl*Rm; C=B**2
assert B==A2.inv()*A1.inv()*A2 and B**3==s.eye(4)
assert Rm*B*Rm==B.inv() and C*Rm*C.inv()==Rl
assert C*(u+w)==-w+d
assert C*A2**2*C.inv()*w==-w and C*A2**2*C.inv()*d==d
lines=['Cap transport: B=R_left R_middle, B^3=1, R_middle B R_middle=B^-1.',
       'Unique root-lift exponent: 2k=1 (mod 3), k=2; C=B^2.',
       'C(u+w)=-w+d; transported order-four exchange sends w to -w and d to d.']

den=24
grid=np.indices((den,)*4,dtype=np.int64).reshape(4,-1).T
for name,a,b in [('negative',s.Rational(1,2),s.Matrix([s.Rational(1,3),0,0,-s.Rational(1,6)])),
                 ('positive',-s.Rational(1,2),s.Matrix([s.Rational(1,2),0,0,s.Rational(1,4)]))]:
    R0=-H+2*a*E
    assert R0*A2*R0==A2.inv()
    for half in [0,1]:
        expected=([True,True,True,True] if name=='negative' and half==0 else
                  [True,False,True,False] if name=='negative' else
                  [False,False,False,False] if half==0 else [False,True,False,True])
        entries=[]
        for k in range(4):
            Rk=A2**k*R0; beta=A2**k*(b+half*d/2)+s.Rational(k,4)*v
            assert Rk**2==s.eye(4)
            Q=s.eye(4)-Rk; L=hermite_normal_form(Q)
            diag=smith_normal_form(Q,domain=s.ZZ).diagonal()
            assert sorted(abs(int(z)) for z in diag if z)==[1,2]
            nums=grid@np.array(Q.tolist(),dtype=np.int64).T-np.array(beta*den,dtype=np.int64).reshape(1,4)
            indices=np.flatnonzero(np.all(nums%den==0,axis=1))
            assert bool(len(indices))==expected[k]
            if not len(indices):
                entries.append(f'k={k}: empty')
                continue
            rows=next(z for z in combinations(range(4),2) if L[list(z),:].det())
            inv=L[list(rows),:].inv()
            origin=s.Matrix((nums[indices[0]]//den).tolist())
            def component(x):
                z=inv*(Q*x-beta-origin)[list(rows),:]
                return tuple(q-s.floor(q) for q in z)
            reps={}
            for index in indices:
                x=s.Matrix(grid[index].tolist())/den
                reps.setdefault(component(x),x)
                if len(reps)==2:
                    break
            assert len(reps)==2
            for key,x in reps.items():
                assert component(A2**2*x+v/2)!=key
            entries.append(f'k={k}: two tori, G^2 exchanges them')
        lines.append(f'{name} half_delta={half}: '+ '; '.join(entries))

result='\n'.join(lines)+'\n'
print(result,end='')
Path(__file__).with_suffix('.out.txt').write_text(result)
