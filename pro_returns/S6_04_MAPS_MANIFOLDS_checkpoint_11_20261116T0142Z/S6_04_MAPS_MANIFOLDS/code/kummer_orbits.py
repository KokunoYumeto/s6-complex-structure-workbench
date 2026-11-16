"""Exact monodromy orbits of the local Kummer sublattice.

The lattice is <gamma,u,Nw,Ndelta>.  Column Hermite normal form is
a canonical integral representative; no floating point arithmetic.
Bounds below are exploratory, not an exhaustive classification theorem.
"""
from pathlib import Path
from collections import deque
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form

T1=s.Matrix([[1,0,-6,2],[0,-1,1,1],[0,-1,0,1],[0,0,0,1]])
T2=s.Matrix([[1,6,0,-3],[0,0,-1,1],[0,1,0,0],[0,0,0,1]])
A1=T1.inv().T
A2=T2.inv().T
M0=(A1*A2).inv()
lines=[f'A1={A1.tolist()}',f'A2={A2.tolist()}',f'M0={M0.tolist()}']
assert A1**3==s.eye(4) and A2**4==s.eye(4)
assert (M0-s.eye(4))**2==s.zeros(4)
for n in [2,3,4,5,6,7,8]:
    L=s.diag(1,1,n,n)
    assert L.inv()*M0**n*L==M0
    initial=tuple(L)
    seen={initial}
    queue=deque([L])
    while queue:
        X=queue.popleft()
        for A in [A1,A2]:
            Y=hermite_normal_form(A*X)
            key=tuple(Y)
            if key not in seen:
                seen.add(key)
                queue.append(Y)
    lines.append(f'N={n}: orbit_size={len(seen)}, ratio={s.Rational(len(seen),n)}')
out='\n'.join(lines)+'\n'
print(out,end='')
Path(__file__).with_suffix('.out').write_text(out)
