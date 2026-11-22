#!/usr/bin/env python3
"""Post-reading algebra and character checks for editorial batch 03.

This checks finite algebra and the exact printed character formula. The analytic
module proofs and descent maps are read separately, not certified by this code.
"""
from pathlib import Path
import hashlib
import json
import sympy as s

x,y,z,t,u,v,lam,a,b=s.symbols('x y z t u v lambda a b')
Fc=x*x-y**3
dc=s.Matrix([2*x,-3*y*y,0]);tc=s.Matrix([2*y,-3*x,0])
assert x*tc-y*dc == s.Matrix([0,-3*Fc,0])
assert y*y*tc-x*dc == s.Matrix([-2*Fc,0,0])
Fp=x*x-y*y*z
dp=s.Matrix([2*x,-2*y*z,-y*y]);tp=s.Matrix([2*y*z,-2*x*z,-x*y])
assert y*tp-x*dp == s.Matrix([-2*Fp,0,0])
assert (x*tp-y*z*dp-s.Matrix([0,-2*z*Fp,-y*Fp])).applyfunc(s.expand)==s.zeros(3,1)
param=s.Matrix([u*v,u,v*v])
assert s.simplify(param.jacobian([u,v]).T*tp.subs({x:u*v,y:u,z:v*v}))==s.zeros(2,1)
assert s.expand((tc[0]*3*t*t+tc[1]*2*t).subs({x:t**3,y:t*t}))==0
# The adjacent AJ proposition is not a computation in A_local_algebra.py.
# Check its printed pullback separately, with the actual parametrization.
param_AJ=s.Matrix([u*u*v**3,u,v*v])
vertical=s.Matrix([2*y*y*z,-4*x*y*z,-3*x*y*y])
assert s.simplify(param_AJ.jacobian([u,v]).T*vertical.subs({x:u*u*v**3,y:u,z:v*v}))==s.zeros(2,1)

F=y*y-x*x*(x+1)-t
assert s.expand(F.subs({x:u*u-1,y:u*(u*u-1),t:0}))==0
assert s.diff(F,t)==-1
assert s.solve([F,s.diff(F,x),s.diff(F,y)],(x,y,t))==[(-s.Rational(2,3),0,-s.Rational(4,27)),(0,0,0)]
scalar=(1-a)*(1+b)/((1-b)*(1+a))
assert s.factor(scalar.subs({a:(1-lam)/(1+lam),b:0})-lam)==0
assert s.limit(scalar.subs(b,0),a,s.oo)==-1
# The cohomology polynomials follow from the exact two-term descent complex
# and the displayed direct sums, whose maps are checked in the proof reading.
d,q=s.symbols('d q')
cohomology={'conormal':d*(1+q),'kernel':s.Integer(1),'torsion':s.Integer(1),
            'torsion_free':q+d*q*(1+q),'cotangent':1+q+d*q*(1+q),
            'ambient':1+q+d*q*(1+q)}
table={key:[str(s.expand(poly).coeff(q,k)) for k in range(3)] for key,poly in cohomology.items()}
assert table['torsion_free']==['0','d + 1','d']
assert table['ambient']==['1','d + 1','d']

ROOT=Path(__file__).resolve().parents[1]
old=ROOT/'agents/ii_checks_provenance/group02/A_multiple_fibres.old_output.txt'
assert hashlib.sha256(old.read_bytes()).hexdigest()=='27baf8ddb9ca1452402249268964f965deca7d6dce1f824d3880441375f977cb'
def floor_count(m,k,b):
    return 2*((b+k-1)//m-(b-1)//m)+((b+k)//m-b//m)
rows=[]
for line in old.read_text().splitlines():
    parts=line.split()
    if len(parts)==6 and all(p.isdigit() for p in parts):
        m,k,b,h0,h1,h2=map(int,parts);dim=floor_count(m,k,b)
        assert (dim,2*dim,dim)==(h0,h1,h2)
        rows.append((m,k,b,h0,h1,h2))
assert len(rows)==sum(m*m for m in range(3,13))==645
assert all(floor_count(m,k,1)==(0 if k<=m-2 else 1 if k==m-1 else 3)
           for m in range(3,13) for k in range(1,m+1))

out={'scope':'Post-reading preservation computation, with no independent whole-proof or extra computation-event claim.',
     'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'local_module_identities':{'cusp':['x*tau-y*dF=(0,-3F,0)','y^2*tau-x*dF=(-2F,0,0)'],
       'pinch':['y*tau-x*dF=(-2F,0,0)','x*tau-yz*dF=(0,-2zF,-yF)'],
       'normalization_pullbacks':'zero under the printed explicit Jacobian matrices',
       'AJ_vertical_pole_pullback':'zero; this is not attributed to the historical A_local_algebra source'},
     'nodal_family':{'critical_values':['0','-4/27'],'normalization_residual':0,
       'gluing_scalar':str(scalar),'chosen_a':'(1-lambda)/(1+lambda)','a_infinity_scalar':-1,
       'cohomology_table':table},
     'multiple_fibre':{'method':'Count integral multiples in [b,b+k-1] by floor differences, then apply the two tangent and one normal weights.',
       'formula':'2*(floor((b+k-1)/m)-floor((b-1)/m))+floor((b+k)/m)-floor(b/m)',
       'historical_output_sha256':hashlib.sha256(old.read_bytes()).hexdigest(),
       'historical_rows_compared':len(rows),'m_range':[3,12],
       'b1_h0_steps':['0 for k<=m-2','1 for k=m-1','3 for k=m'],
       'global_Cech_weights':[0,1]},'all_assertions_passed':True}
print(json.dumps(out,indent=2))
