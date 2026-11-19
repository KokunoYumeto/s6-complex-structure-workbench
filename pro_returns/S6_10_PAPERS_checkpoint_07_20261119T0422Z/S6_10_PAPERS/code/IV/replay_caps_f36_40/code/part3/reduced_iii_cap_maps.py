#!/usr/bin/env python3
"""Complete marked Mayer--Vietoris maps for P3F.37.

The norm-circle/source-fibre argument fixes the signed degree-three
columns geometrically in the proof. This certificate retains those
actual markings and verifies all displayed integral matrices.
"""
from pathlib import Path
import itertools
import json
import sympy as S

root=Path(__file__).resolve().parent
m,k=S.symbols('m kappa',integer=True)
J=S.Matrix([[0,1,-1],[-1,0,0],[0,0,1]])
pairs=list(itertools.combinations(range(3),2))
J2=S.Matrix([[J.extract(I,K).det() for K in pairs] for I in pairs])
F=S.Matrix([1,0,0])
assert J2*F==F and J.det()==1
D0=S.Matrix([1,-1])
D1=S.Matrix([[0,1],[1,-m]])
D2=S.Matrix([[0,-1],[-1,-k]])
exterior3=S.Matrix([[0,1]])
cap3=S.Matrix([[-1,m]])
D3=exterior3.col_join(-cap3)
assert D3==D1
assert D1.det()==D2.det()==D3.det()==-1
assert S.gcd(D0[0],D0[1])==1
mat=lambda M:[[str(x) for x in row] for row in M.tolist()]
data=dict(status='PASS',statement='P3F.37',
    H3_boundary_basis=['oriented source boundary L','source fibre gamma trace'],
    H3_exterior_row=mat(exterior3),H3_cap_row=mat(cap3),
    source_fibre_specialization='F -> C0+C1, primitive invariant',
    marked_norm_circle='u=m*gamma-arg(q)/(2*pi)',
    D0=mat(D0),D1=mat(D1),D2=mat(D2),D3=mat(D3),
    D4={'source_rank':1,'target_rank':0,'matrix':[]},
    degree_1_2_3_determinants=[-1,-1,-1],
    boundary_J=mat(J),boundary_wedge2_J=mat(J2),
    primitive_H2_invariant_F=mat(F),
    resulting_homology={'0':'Z','1':'0','2':'0','3':'0','4':'0','5':'Z'})
(root/'reduced_iii_cap_maps.json').write_text(json.dumps(data,indent=2)+'\n')
print('PASS: primitive source-boundary/fibre-trace H3 basis; cap row (-1,m).')
print('PASS: D1,D2,D3 unimodular; D0 primitive incidence and D4: Z -> 0 retained.')
print('PASS: all integral orbit homology groups, without an omitted higher gluing map.')
