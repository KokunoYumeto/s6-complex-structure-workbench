#!/usr/bin/env python3
"""Post-release check of the complete invariant-lattice equations in the receiver."""
from datetime import datetime,timezone
from itertools import combinations
import sympy as s

pairs=list(combinations(range(4),2))
def wedge(A):
    return s.Matrix([[A[i,k]*A[j,l]-A[i,l]*A[j,k]
        for k,l in pairs] for i,j in pairs])
R=s.symbols('R',integer=True,positive=True)
x,y,z,t,r,h=s.symbols('x y z t r h')
vector=s.Matrix([x,y,z,t,r,h])
for c in (2,3):
    A=s.Matrix([[1,0,0,0],[0,0,1,0],[-c*R,-1,2-c,0],[-R,0,-1,1]])
    equations=(wedge(A.T)-s.eye(6))*vector
    expected=s.Matrix([-R*h-x-y,R*r+2*R*h+c*R*t+x+(1-c)*y-z,
                       -c*R*h,h,-r-h,r+(1-c)*h])
    assert equations==expected
    # The fourth equation forces h=0; the fifth then forces r=0;
    # the first forces y=-x, and the second gives z=c*(x+R*t).
    solved=s.Matrix([x,-x,c*(x+R*t),t,0,0])
    omega1=s.Matrix([-R,R,0,1,0,0]);omega2=s.Matrix([1,-1,c,0,0,0])
    assert solved==t*omega1+(x+R*t)*omega2
    assert (wedge(A.T)-s.eye(6))*solved==s.zeros(6,1)
    print('c=',c,'full equations:',list(equations),'inverse basis coordinates:',(t,x+R*t))
A2=s.Matrix([[1,0,0,0],[0,1,-1,0],[0,1,0,0],[0,0,0,1]])
equations=(wedge(A2.T)-s.eye(6))*vector
assert equations==s.Matrix([y,-x-y,0,0,h,-r-h])
print('Second lattice full equations:',list(equations),'free coordinates:',(t,z))
print('ALL EXACT FIXED-LATTICE EQUATIONS PASS; post-release comparison only.')
print('Completed UTC:',datetime.now(timezone.utc).isoformat())
