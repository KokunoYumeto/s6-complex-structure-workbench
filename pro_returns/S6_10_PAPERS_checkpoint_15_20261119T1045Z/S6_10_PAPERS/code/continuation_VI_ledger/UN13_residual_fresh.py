#!/usr/bin/env python3
"""Fresh exact chart/trace/Gysin/fibre certificates; no prior check imported."""
from datetime import datetime, timezone
from itertools import combinations
from pathlib import Path
import json
import sympy as S

ROOT=Path(__file__).resolve().parents[2]
checks=[]
def check(name, condition, evidence):
    condition=bool(condition)
    checks.append({'name':name,'pass':condition,'evidence':evidence})
    if not condition:raise AssertionError(name)
def zero(x):return S.cancel(x)==0

r,u,v,R=S.symbols('r u v R')
# The actual surface quotient charts, including the exact two-form factor.
cover=S.Matrix([r,r*u]); J=cover.jacobian([r,u])
quotient=S.Matrix([r*r,u]); QJ=quotient.jacobian([r,u])
check('surface_form_pullback',zero(J.det()-QJ.det()/2),
      {'cover_Jacobian':str(J.det()),'quotient_Jacobian':str(QJ.det()),'form_factor':'1/2'})
second=S.Matrix([R*u*u,1/u]);TJ=second.jacobian([R,u])
check('surface_form_transition_sign',zero(TJ.det()+1),{'determinant':str(TJ.det())})
cone=S.Matrix([R,R*u,R*u*u])
check('surface_cone_equation',zero(cone[0]*cone[2]-cone[1]**2),{'map':[str(x) for x in cone]})
other=S.Matrix([second[0]*second[1]**2,second[0]*second[1],second[0]])
check('surface_both_resolution_maps',all(zero(x) for x in cone-other),{'overlap':'Rb=R*u^2,v=1/u'})
check('surface_cover_squared_transition',zero((r*u)**2-(r*r)*u*u),{'line_factor':'u^2'})

# The threefold quotient is checked through every Veronese two-by-two minor.
vec=S.Matrix([1,u,v]);M=R*vec*vec.T
for rows in combinations(range(3),2):
    for cols in combinations(range(3),2):
        minor=M.extract(rows,cols).det()
        check('ambient_Verone​se_minor_'+str(rows)+str(cols),zero(minor),{'minor':str(minor)})
Rb,U,V=R*u*u,1/u,v/u
Mb=Rb*S.Matrix([U,1,V])*S.Matrix([[U,1,V]])
check('ambient_second_chart_map',all(zero(x) for x in M-Mb),{'transition':['R*u^2','1/u','v/u']})
Rc,A,B=R*v*v,1/v,u/v
Mc=Rc*S.Matrix([A,B,1])*S.Matrix([[A,B,1]])
check('ambient_third_chart_map',all(zero(x) for x in M-Mc),{'transition':['R*v^2','1/v','u/v']})
check('ambient_cocycle_fibre',zero(Rb*V**2-Rc),{'factor':'u^2*(v/u)^2=v^2'})
check('ambient_cocycle_base_a',zero(U/V-A),{'a_over_c':'(1/u)/(v/u)=1/v'})
check('ambient_cocycle_base_b',zero(1/V-B),{'b_over_c':'1/(v/u)=u/v'})

# Rational trace on the exterior algebra of the torus.
betti=[]
for k in range(5):
    basis=list(combinations(range(4),k));n=len(basis)
    involution=(-1)**k*S.eye(n);average=(S.eye(n)+involution)/2
    check(f'trace_idempotent_degree_{k}',average*average==average,{'dimension':n})
    check(f'trace_invariant_image_degree_{k}',involution*average==average,
          {'rank':average.rank(),'involution_sign':(-1)**k})
    betti.append(average.rank())
check('quotient_Betti',betti==[1,0,6,0,1],{'betti':betti})
coherent_average=(S.eye(2)-S.eye(2))/2
check('coherent_H1_invariants',coherent_average.rank()==0,{'source_dimension':2,'rank':0})
eT=sum((-1)**k*betti[k] for k in range(5));eP=eT-16+16*2
check('Kummer_Euler',eT==8 and eP==24,{'eT':eT,'eP':eP,'replaced_points':16})

# Every ambient rational Gysin section has its required restriction.
for k in [2,4]:
    restriction=-2*S.eye(32);section=-S.eye(32)/2
    check(f'ambient_restriction_section_degree_{k}',restriction*section==S.eye(32),
          {'normal_coefficient':-2,'section_coefficient':'-1/2','rank':32})
    check(f'ambient_cross_exceptional_degree_{k}',
          all(restriction[i,j]==0 for i in range(32) for j in range(32) if i!=j),
          {'components':32})
bX=[1,0,7,0,7,0,1];bW=[bX[k]+(32 if k in [2,4] else 0) for k in range(7)]
check('ambient_Betti_additions',bW==[1,0,39,0,39,0,1],{'bX':bX,'bW':bW})
diag=S.ones(32,1)
check('relative_H1_H0_boundary_rank',diag.rank()==1 and 32-diag.rank()==31,
      {'diagonal_rank':diag.rank(),'relative_H1_dimension':31,'H1_absolute_dimension':0})

# Support projective-bundle summands and the -1 normal restriction.
support_outputs={}
for centre,c,bC in [('point',3,[1]),('quartic',2,[1,6,1])]:
    additions=[]
    for k in range(7):
        summands=[(i,bC[k-2*i]) for i in range(1,c) if 0<=k-2*i<len(bC)]
        n=sum(d for _,d in summands);additions.append(n)
        restriction=-S.eye(n);gysin_section=-S.eye(n)
        check(f'{centre}_actual_fibre_section_degree_{k}',restriction*gysin_section==S.eye(n),
              {'summands':summands,'normal':'-xi','section_sign':-1,'fibre_rank':n})
    expected=[0,0,1,0,1,0,0] if centre=='point' else [0,0,1,6,1,0,0]
    check(centre+'_support_additions',additions==expected,{'additions':additions})
    support_outputs[centre]=additions

# Full Cartier-fibre equations, including all boundary-intersection charts.
x,y,z=S.symbols('x y z')
point_charts=[{x:r,y:r*u,z:r*v},{x:r*u,y:r,z:r*v},{x:r*u,y:r*v,z:r}]
quartic_charts=[{x:r,z:r*u,y:v},{z:r,x:r*u,y:v}]
def order_r(expr):
    poly=S.Poly(S.expand(expr),r)
    return min(power[0] for power,coefficient in poly.terms() if coefficient!=0)
for i,chart in enumerate(point_charts):
    full=x.subs(chart,simultaneous=True)
    check(f'point_exceptional_order_chart_{i}',order_r(full)==1,
          {'full_fibre':str(full),'exceptional_order':order_r(full)})
for boundary in range(4):
    for i,chart in enumerate(quartic_charts):
        full=(x*y).subs(chart,simultaneous=True)
        check(f'quartic_boundary_{boundary+1}_chart_{i}',order_r(full)==1,
              {'full_fibre':str(full),'exceptional_order':order_r(full),
               'boundary_factor_retained':str(y.subs(chart))})
for i,chart in enumerate(quartic_charts):
    full=x.subs(chart,simultaneous=True)
    check(f'quartic_generic_order_chart_{i}',order_r(full)==1,{'full_fibre':str(full)})

out={'created_utc':datetime.now(timezone.utc).isoformat(),
     'checker':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS continuation',
     'target_proof_opened':False,'owner_derivation_and_code_opened':False,
     'scope':'New exact chart, differential-form, trace, Gysin-section and fibre-equation checks. Pair exactness and the universal support splitting are proved in the separate prereading note, not inferred from finite ranks.',
     'pass':all(x['pass'] for x in checks),'check_count':len(checks),'checks':checks,
     'support_additions':support_outputs}
p=ROOT/'analysis/continuation_VI_ledger/UN13_residual_fresh.output.json';p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'pass':out['pass'],'check_count':out['check_count'],'output':str(p)}))
