"""Exact minimal-model terms for the unresolved ruled foliation calculation.

This records algebraic identities only. It does not claim that the remaining
vertical determinant and foliation-zero divisors have been bounded.
"""
from pathlib import Path
import json
import sympy as sp

r,z,h,a,rf,zf=sp.symbols('r z h a rf zf')
# Coordinates on the span of H,F: H^2=-h-a, H.F=1, F^2=0.
Q=sp.Matrix([[-h-a,1],[1,0]])
H=sp.Matrix([1,0]); F=sp.Matrix([0,1])
K=-2*H-a*F; W=h*F; R=r*H+rf*F; Z=z*H+zf*F
def pair(x,y):return sp.expand((x.T*Q*y)[0])
B=sp.expand(pair(R,R)-pair(K,R)-pair(W,R)-pair(Z,R)
            -pair(K,Z)+2*pair(W,Z)+pair(Z,Z))
immersive=sp.expand(B.subs({r:0,z:0}))
cuspidal=sp.expand(B.subs({r:1,z:1}))
assert immersive==2*rf+2*zf
assert cuspidal==-3*a-4*h+3*rf+3*zf
assert pair(K,K)-pair(K,W)+pair(W,W)==-2*h
result={'purpose':'Working identities for ruled resolution sector',
        'basis':['H','F'],'intersection_matrix':[[str(v) for v in Q.row(i)] for i in range(2)],
        'B':str(B),'immersive_horizontal':str(immersive),
        'cuspidal_horizontal':str(cuspidal),
        'chern_constant_before_blowups':'-2*h',
        'remaining_obligation':'Bound actual vertical R0 and Z0; no bound is asserted here.',
        'all_checks_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print('Ruled minimal-model Chern bookkeeping: PASS')
print('Immersive horizontal term:',immersive)
print('Cuspidal horizontal term:',cuspidal)
print('Chern constant:',pair(K,K)-pair(K,W)+pair(W,W))
print('The remaining vertical-divisor bound is not established by this calculation.')
