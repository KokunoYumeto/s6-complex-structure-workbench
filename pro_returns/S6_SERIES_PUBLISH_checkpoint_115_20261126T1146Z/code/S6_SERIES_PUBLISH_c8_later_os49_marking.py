#!/usr/bin/env python3
"""Candidate marked-lattice bridge; geometric stem transport is a separate proof."""
import sympy as s

TA=s.Matrix([[1,-3,-3,-1],[0,-2,-3,-1],[0,1,1,0],[0,0,0,1]])
TB=s.Matrix([[1,0,0,0],[0,1,1,0],[0,-1,0,0],[0,0,0,1]])
TC=s.Matrix([[1,0,3,1],[0,1,2,1],[0,0,1,0],[0,0,0,1]])
A,B,C=[T.inv().T for T in (TA,TB,TC)]
MII=s.Matrix([[1,1,0,0],[-1,0,0,0],[0,0,1,0],[0,0,0,1]])
MIV=s.Matrix([[0,-1,0,0],[1,-1,0,-3],[0,1,1,1],[0,0,0,1]])
MI2=s.Matrix([[1,2,0,3],[0,1,0,0],[0,-1,1,-1],[0,0,0,1]])
U=MIV
V=U.inv()*MII*U
assert A*B*C==s.eye(4) and MII*MIV*MI2==s.eye(4)
z=s.symbols('z0:9')
F=s.Matrix([[z[0],z[1],z[2],0],[z[3],z[4],z[5],0],
            [z[6],z[7],z[8],1],[1,0,0,0]])
equations=list(U*F-F*A)+list(V*F-F*B)
solution=s.linsolve(equations,z)
print('A=',A.tolist())
print('B=',B.tolist())
print('V=',V.tolist())
print('SOLUTION_WITH_DELTA_AND_SUSPENSION_FIXED=',solution)
for values in solution:
    G=F.subs(dict(zip(z,values)))
    print('F=',G.tolist())
    print('DET=',s.factor(G.det()))
    print('F_INVERSE=',G.inv().tolist())
    print('FINITE_VECTOR_IMAGE=',(G*s.Matrix([1,-1,0,0])).tolist())
    print('CUSP_CONJUGACY=',MI2*G==G*C)
S=s.Matrix([[0,0,-1,0],[0,-1,1,1],[0,0,0,1],[-1,0,3,0]])
for values in solution:
    G=F.subs(dict(zip(z,values)))
    print('P26_TO_YANG=',(S.T*G).tolist())
    print('P26_VECTOR_IN_YANG=',(S.T*G*s.Matrix([1,-1,0,0])).tolist())
print('LATTICE_IDENTITIES_ONLY; GEOMETRIC_STEM_AND_LINE_FRAME_MAPS_NOT_INFERRED')
