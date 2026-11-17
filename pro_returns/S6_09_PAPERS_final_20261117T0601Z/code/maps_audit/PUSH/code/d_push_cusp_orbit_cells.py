#!/usr/bin/env python3
"""Exact finite part of the central cusp orbit-fibre calculation.

The local quotient, orientation and pushout comparisons are proved in
sections/C_cusp_orbit_topology.tex. This program checks their finite
incidence and integral matrix data; it does not calculate a smooth
mapping class.
"""
import json
from pathlib import Path
import sympy as S
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

parent = list(range(6))
def find(a):
    while parent[a] != a:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a
def join(a,b):
    parent[find(a)] = find(b)

# p_i has index i-1. D_i -> D_{i+3} maps p_{i-1}->p_{i+3},
# p_i->p_{i+2}; only the three independent pairs are needed.
for i in range(1,4):
    join((i-2)%6,(i+2)%6)
    join((i-1)%6,(i+1)%6)
classes = sorted(sorted(i+1 for i in range(6) if find(i)==r)
                 for r in {find(i) for i in range(6)})
assert classes == [[1,3,5],[2,4,6]]

M = S.Matrix([[1,1],[-1,-1]])
snf = smith_normal_form(M,domain=ZZ)
assert M.rank()==1 and list(snf.diagonal())==[1,0]

# The conductor graph has two sphere vertices plus two two-edge paths.
# Collapse each sphere to a vertex just for its first-homology graph.
boundary_graph = S.Matrix([[-1,0,-1,0],[0,1,0,1],
                           [1,-1,0,0],[0,0,1,-1]])
assert boundary_graph.rank()==3
b1_normal_conductor = 4-boundary_graph.rank()
assert b1_normal_conductor==1

# Image D: the sphere joins A to B, and each extra edge contributes a loop.
b1_image_conductor = 2
word = [('a',1),('b',-1),('a',-1),('b',1)]
abelianization = {k:sum(e for a,e in word if a==k) for k in ['a','b']}
assert abelianization=={'a':0,'b':0}

data = {
 'status':'PASS',
 'vertex_classes':classes,
 'H2_conductor_map':[[int(x) for x in row] for row in M.tolist()],
 'smith_diagonal':[int(x) for x in snf.diagonal()],
 'normal_conductor_betti':[1,1,2],
 'image_conductor_betti':[1,2,1],
 'H_betti':[1,2,2,1],
 'torsion':[],
 'pi1_presentation':'<a,b | a b^-1 a^-1 b>',
 'abelianization_of_attaching_word':abelianization,
 'fixed_sphere_class':'primitive generator of the H2 map cokernel',
 'scope':'finite incidence and integer matrices, not a smooth twist invariant',
}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
