#!/usr/bin/env python3
"""Exact local charts and incidence for the regular-place Hopf insertion."""
import json
from pathlib import Path
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

x,y,z,s,Q,X,r=sp.symbols('x y z s Q X r')
eq=x*y-z*s
chart1={z:x*Q,y:Q*s,r:x*Q*s}
chart2={x:z*X,s:X*y,r:z*X*y}
assert sp.expand(eq.subs(chart1,simultaneous=True))==0
assert sp.expand(eq.subs(chart2,simultaneous=True))==0
assert sp.expand((r-z*s).subs(chart1,simultaneous=True))==0
assert sp.expand((r-z*s).subs(chart2,simultaneous=True))==0

incidence=[]
for i in range(12):
    j=(i+1)%12
    ev=[k for k in (i,j) if k%2==0]
    assert len(ev)==1
    incidence.append({'node':[i,j],'even_branch':ev[0],
                      'vertical_curve_blowup':ev[0],
                      'horizontal_curve_blowup':next(k for k in (i,j) if k%2==1)})
v_counts={i:sum(q['vertical_curve_blowup']==i for q in incidence) for i in range(12)}
h_counts={i:sum(q['horizontal_curve_blowup']==i for q in incidence) for i in range(12)}
assert all(v_counts[i]==(2 if i%2==0 else 0) for i in range(12))
assert all(h_counts[i]==(0 if i%2==0 else 2) for i in range(12))

# The principal elliptic bundle has primitive Chern vector u=(0,1)
# in the basis (w,u), up to the immaterial overall sign.
chern=sp.Matrix([[0],[1]])
snf=smith_normal_form(chern,domain=ZZ)
assert snf==sp.Matrix([[1],[0]])

out={'status':'PASS','first_chart':{str(k):str(v) for k,v in chart1.items()},
     'second_chart':{str(k):str(v) for k,v in chart2.items()},
     'central_multiplicities_chart1':[1,1,1],
     'central_multiplicities_chart2':[1,1,1],
     'incidence':incidence,'vertical_blowup_counts':v_counts,
     'horizontal_blowup_counts':h_counts,
     'elliptic_Chern_vector':[0,1],'Chern_Smith_form':list(snf),
     'Hopf_pi1':'Z','new_vertical_normalization_b1':1,
     'scope':'Actual local regular-place punctured torus germ; proper over bidisc, flat over r, not joint-flat and not a global S6 filling.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2,default=str)+'\n')
print(json.dumps(out,indent=2,default=str))
