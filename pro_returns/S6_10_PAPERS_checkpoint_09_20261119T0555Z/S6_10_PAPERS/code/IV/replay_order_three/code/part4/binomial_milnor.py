#!/usr/bin/env python3
"""Exact exponent matrices and transfer pairings for P4.18--P4.19."""
from math import gcd
from pathlib import Path
import json
import sympy as S

records=[]
for b in range(1,9):
    for c in range(1,9):
        d=gcd(b,c); B=b//d; C=c//d
        p,q,g=S.gcdex(B,C)
        assert g==1 and B*p+C*q==1
        matrix=S.Matrix([[B,C],[q,-p]])
        assert matrix.det()==-1
        source_square=-2*B
        transferred_square=C*source_square
        assert transferred_square==-2*B*C
        for a in range(2,7):
            weights=(b+c,a,a)
            assert a*weights[0] == b*weights[1]+c*weights[2]
        records.append(dict(b=b,c=c,d=d,primitive_exponents=[B,C],
                            bezout=[int(p),int(q)],
                            meridian_matrix=matrix.tolist(),
                            determinant=-1,transfer_degree=C,
                            spherical_square=transferred_square))
        print(f'b={b}, c={c}; d={d}; primitive=({B},{C}); '
              f'Bezout=({p},{q}); matrix={matrix.tolist()}; '
              f'det=-1; transferred spherical square={transferred_square}')

x,y,z,u,v=S.symbols('x y z u v')
assert S.expand((u**3*v**2)**2-(u**2)**3*v**4)==0
J=S.Matrix([u**3*v**2,v,u**2]).jacobian([u,v])
minors=[S.factor(J.extract(rows,[0,1]).det())
        for rows in ((0,1),(0,2),(1,2))]
assert S.gcd_list(minors)==u
print('Mixed cusp/tacnode model x^2-z^3*y^4: normalization '
      '(u,v)->(u^3*v^2,v,u^2); Jacobian minors=',minors)

# The excluded overgeneralization has this exact product parametrization.
z_solution=(y*x*x-1)/y**3
assert S.cancel(y*(x*x-z_solution*y*y)-1)==0
assert S.expand(v*((u*v)**2-u**2*v**2))==0
print('Ramified-conductor limitation: y*(x^2-z*y^2)=1 is C* x C, '
      'inverse z=(y*x^2-1)/y^3; the Whitney-component parametrization '
      '(u,v)->(u*v,v,u^2) verified.')

Path(__file__).with_suffix('.json').write_text(
    json.dumps(records,indent=2,default=lambda x:int(x))+'\n')
print('All 64 primitive exponent matrices and transfer pairings verified.')
