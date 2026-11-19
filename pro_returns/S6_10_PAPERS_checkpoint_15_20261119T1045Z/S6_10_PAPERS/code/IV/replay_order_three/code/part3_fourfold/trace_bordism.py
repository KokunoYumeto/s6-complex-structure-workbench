#!/usr/bin/env python3
"""Exact characteristic algebra and marked cap maps of the real trace."""
from pathlib import Path
import json
import sympy as sp
out=Path(__file__).resolve().parent
n,b2,p=sp.symbols('p1_normal b_squared p1_base')
k=(n+3*b2)/4
ell=p+n
A=sp.cancel((4*k-ell)/24)
assert A==(3*b2-p)/24
Ha=sp.Matrix([[0,1,0],[0,0,1]])
Hg=sp.Matrix([[1,0,0],[0,1,0]])
assert Ha.rank()==Hg.rank()==2
assert Ha*sp.Matrix([1,0,0])==sp.zeros(2,1)
assert Hg*sp.Matrix([0,0,1])==sp.zeros(2,1)
cases={}
for name,s,sigma in [('primitive_main',-2,-8),('weighted_OS47_page',-14,-24)]:
    val=sp.Rational(3*4*s-3*sigma,24)
    cases[name]={'page_relative_M_square':s,'page_signature':sigma,
        'b_square':4*s,'p1_base':3*sigma,'one_gamma_turn_index':int(val)}
assert cases['primitive_main']['one_gamma_turn_index']==0
assert cases['weighted_OS47_page']['one_gamma_turn_index']==-4
data={
    'status':'exact identities; geometric comparison in notes/part3_fourfold.md P3K.6--7',
    'sphere_bundle_relation':'(2*x-pi*b)^2=pi*p1_normal',
    'push_x':1,'push_x_squared':'b',
    'push_x_cubed':str(k),'p1x':str(ell),'index':str(A),
    'normal_class_cancelled':True,
    'marked_boundary_basis':['a_source_vanishing','b_source_dual','gamma'],
    'H1_map_compression_cap':[[int(v) for v in row] for row in Ha.tolist()],
    'H1_map_regular_cap':[[int(v) for v in row] for row in Hg.tolist()],
    'cap_difference':'S1_b times S3, by the meridian-longitude Heegaard gluing',
    'cases':cases,
    'primitive_cover_degree':6,
    'primitive_original_index':0,
    'OS47_cover_normalization':'The one-gamma-turn value is recorded only; parent tracks the lambda=r^4 parameter cover and final orientation.'
}
(out/'trace_bordism.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
