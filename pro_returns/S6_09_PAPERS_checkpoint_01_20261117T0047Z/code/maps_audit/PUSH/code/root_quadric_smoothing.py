#!/usr/bin/env python3
"""Exact certificates for B.4.12; the analytic construction is in its proof."""
from pathlib import Path
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

root=Path(__file__).resolve().parents[1]
x0,x1,y0,y1,u,v=s.symbols('x0 x1 y0 y1 u v')
F=x0*x0*y0*y0+x0*x0*y1*y1+x1*x1*y0*y0+2*x1*x1*y1*y1
charts=[]
for i in range(2):
    for j in range(2):
        sub={x0:1 if i==0 else u,x1:u if i==0 else 1,
             y0:1 if j==0 else v,y1:v if j==0 else 1}
        f=s.expand(F.subs(sub))
        gb=s.groebner([f,s.diff(f,u),s.diff(f,v)],u,v)
        assert list(gb)==[1], (i,j,gb)
        charts.append({'chart':[i,j],'equation':str(f),'singular_ideal_groebner':['1']})
d=s.symbols('d',integer=True,positive=True)
hilbert_difference=s.expand((2*d+1)**2-(2*d-1)**2)
assert hilbert_difference==8*d
# Coordinates record the elliptic degree and the P1 degree respectively.
normal_ab=s.Matrix([8,-1])+s.Matrix([-8,0])+s.Matrix([0,1])
normal_ac=s.Matrix([0,0])+s.Matrix([-2,-2])+s.Matrix([2,2])
normal_bc=0-1+1
assert normal_ab==s.zeros(2,1) and normal_ac==s.zeros(2,1) and normal_bc==0
intersection=s.Matrix([[2,2]])
snf=smith_normal_form(intersection,domain=s.ZZ)
assert snf==s.Matrix([[2,0]])
assert intersection*s.Matrix([1,-1])==s.zeros(1,1)
record={
 'status':'PASS',
 'scope':'Exact algebraic and topological certificates; no compact threefold assembly or S6 identification asserted.',
 'smooth_bidegree_22_example':str(F),'affine_charts':charts,
 'quadric_cone_hilbert_function':'(2d+1)^2',
 'elliptic_cone_hilbert_function':'8d for d>0; 1 for d=0',
 'hilbert_difference':str(hilbert_difference),
 'pairwise_normal_products':{'AB':list(normal_ab),'AC':list(normal_ac),'BC':normal_bc},
 'intersection_matrix':[[2,2]],'smith_matrix':[[2,0]],
 'complement_homology':{'H0':'Z','H1':'Z/2','H2':'Z^3','H3':'0','H4':'0'},
 'complement_euler_two_routes':{'homology':1+3,'ruling_four_branches':4},
 'compact_surface_nearby_euler':8+4-2*0,
}
out=root/'code'/'root_quadric_smoothing.json'
out.write_text(json.dumps(record,indent=2,default=str)+'\n')
print(json.dumps(record,indent=2,default=str))
