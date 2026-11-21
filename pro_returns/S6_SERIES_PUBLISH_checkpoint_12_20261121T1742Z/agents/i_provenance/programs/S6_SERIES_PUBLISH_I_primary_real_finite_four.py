"""Exact central real loci at the multiplicity-four filling.

All equations are integer congruences. Grid denominator 24 suffices:
translation denominators divide 12 and nonzero Smith factors of I-R
are 1,2. Connected components are classified in im(I-R)_R/(I-R)Z^4.
"""
from pathlib import Path
from itertools import combinations
import numpy as np
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form,smith_normal_form
A=s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
H=s.Matrix([[1,0,0,0],[0,1,0,0],[-6,0,-1,0],[0,-1,0,-1]])
E=s.zeros(4);E[3,0]=1
v=s.Matrix([-1,-3,3,0]);d=s.Matrix([0,0,0,1])
den=24
grid=np.indices((den,)*4,dtype=np.int64).reshape(4,-1).T
lines=[]
for name,a,b in [('negative',s.Rational(1,2),s.Matrix([s.Rational(1,3),0,0,-s.Rational(1,6)])),
                 ('positive',-s.Rational(1,2),s.Matrix([s.Rational(1,2),0,0,s.Rational(1,4)]))]:
 R0=-H+2*a*E
 for half in [0,1]:
  for k in [0,1]:
   R=A**k*R0;beta=A**k*(b+half*d/2)+s.Rational(k,4)*v
   C=s.eye(4)-R;hnf=hermite_normal_form(C)
   factors=smith_normal_form(C,domain=s.ZZ).diagonal()
   assert sorted(abs(int(z)) for z in factors if z)!=[ ]
   assert all(abs(int(z)) in [0,1,2] for z in factors)
   target=beta*den
   assert all(z.q==1 for z in target)
   nums=grid@np.array(C.tolist(),dtype=np.int64).T-np.array(target,dtype=np.int64).reshape(1,4)
   inds=np.flatnonzero(np.all(nums%den==0,axis=1))
   reps={}
   if len(inds):
    rows=next(rows for rows in combinations(range(4),2) if hnf[list(rows),:].det()!=0)
    inv=hnf[list(rows),:].inv()
    origin=s.Matrix((nums[inds[0]]//den).tolist())
    def key(x):
     n=C*x-beta-origin
     z=inv*n[list(rows),:]
     return tuple(t-s.floor(t) for t in z)
    for index in inds:
     x=s.Matrix(grid[index].tolist())/den
     reps.setdefault(key(x),x)
     if len(reps)==2:break
    perm={str(kk):str(key(A**2*x+v/2)) for kk,x in reps.items()}
   else:perm={}
   lines.append(f'{name} half_delta={half} lift_parity={k}: components={len(reps)}, deck_square_permutation={perm}')
out='\n'.join(lines)+'\n';print(out,end='');Path(__file__).with_suffix('.out').write_text(out)
