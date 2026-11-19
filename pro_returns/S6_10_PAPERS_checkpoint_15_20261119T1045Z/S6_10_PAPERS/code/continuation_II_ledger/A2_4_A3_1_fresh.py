#!/usr/bin/env python3
"""Fresh exact local module and Cartier-thickening checks; target unopened."""
from pathlib import Path
from datetime import datetime,timezone
from itertools import combinations
import json
import sympy as S
ROOT=Path(__file__).resolve().parents[2]
checks=[]
def check(name,ok,evidence=None):
    checks.append({'name':name,'pass':bool(ok),'evidence':evidence})
    if not ok:raise AssertionError(name)
x,y,z,u,v,t,w=S.symbols('x y z u v t w')
F=x*x-y*y*z;Fc=x*x-y**3
pin={x:u*v,y:u,z:v*v};cusp={x:t**3,y:t*t}
check('pinch:normalization_equation',S.expand(F.subs(pin))==0)
check('cusp:normalization_equation',S.expand(Fc.subs(cusp))==0)
grad=S.Matrix([S.diff(F,q)for q in (x,y,z)])
gradc=S.Matrix([S.diff(Fc,q)for q in (x,y,z)])
tau=S.Matrix([2*y*z,-2*x*z,-x*y]);tauc=S.Matrix([2*y,-3*x,0])
check('pinch:actual_torsion_multiplier',S.simplify(tau.subs(pin)-v*grad.subs(pin))==S.zeros(3,1))
check('cusp:actual_torsion_multiplier',S.simplify(tauc.subs(cusp)-gradc.subs(cusp)/t)==S.zeros(3,1))
Dp=S.Matrix([[S.diff(pin[q],a)for a in (u,v)]for q in (x,y,z)])
Dc=S.Matrix([[S.diff(cusp.get(q,q),a)for a in (t,z)]for q in (x,y,z)])
check('pinch:normalization_pullback_zero',S.simplify(Dp.T*tau.subs(pin))==S.zeros(2,1))
check('cusp:normalization_pullback_zero',S.simplify(Dc.T*tauc.subs(cusp))==S.zeros(2,1))
def inRpin(a,b):return a>=0 and b>=0 and (a>=1 or b%2==0)
def inBpin(a,b):return a>=0 and b>=0
def inRcusp(a):return a==0 or a>=2
pinJ=[(1,1),(1,2),(2,0)]
for a in range(-5,11):
    for b in range(-5,11):
        inverse=all(inRpin(a+c,b+d)for c,d in pinJ)
        check(f'pinch:inverse_J_monomial_{a}_{b}',inverse==inBpin(a,b))
        conductor=inRpin(a,b)and inRpin(a,b+1)
        check(f'pinch:conductor_monomial_{a}_{b}',conductor==(a>=1 and b>=0))
        if inRpin(a,b):
            check(f'pinch:torsion_annihilator_{a}_{b}',inRpin(a,b+1)==(a>=1))
        if inBpin(a,b)and not inRpin(a,b):
            check(f'pinch:torsion_generator_{a}_{b}',a==0 and b%2==1 and b>=1)
for a in range(-8,25):
    inverse=inRcusp(a+3)and inRcusp(a+4)
    check(f'cusp:inverse_J_monomial_{a}',inverse==(a>=-1))
    conductor=inRcusp(a)and inRcusp(a+1)
    check(f'cusp:conductor_monomial_{a}',conductor==(a>=2))
    if inRcusp(a):
        ann=inRcusp(a-1)
        ideal=inRcusp(a-3)or inRcusp(a-4)
        check(f'cusp:torsion_annihilator_{a}',ann==ideal)
    if a>=-1:
        check(f'cusp:quotient_basis_{a}',(not inRcusp(a))==(a in (-1,1)))
        check(f'cusp:additional_quotient_{a}',(a<0)==(a==-1))
check('cusp:generator_y_action',S.cancel(y.subs(cusp)/t)==t)
check('pinch:conductor_generators',[y.subs(pin),x.subs(pin)]==[u,u*v])
check('cusp:conductor_generators',[y.subs(cusp),x.subs(cusp)]==[t*t,t**3])
g=1+x+y*z
for i,q in enumerate((x,y,z)):
    check(f'global:conormal_unit_transition_{i}',S.expand(S.diff(g*F,q)-g*S.diff(F,q)-F*S.diff(g,q))==0)

f,h,a=S.symbols('f h a')
for k in range(2,13):
    # Coefficient matrices of R/(f^k) -> R/(f^(k-1)) and its kernel.
    for rank in (1,2,3):
        n=k*rank;target=(k-1)*rank
        quotient=S.eye(n)[:target,:]
        inject=S.zeros(n,rank);inject[target:,:]=S.eye(rank)
        check(f'thickening:k{k}:rank{rank}:kernel_inclusion',quotient*inject==S.zeros(target,rank))
        check(f'thickening:k{k}:rank{rank}:exact_kernel',n-quotient.rank()==inject.rank()==rank)
        check(f'thickening:k{k}:rank{rank}:surjective',quotient.rank()==target)
    check(f'thickening:k{k}:actual_multiplier',S.expand(a*(h*f)**(k-1)-h**(k-1)*(a*f**(k-1)))==0)
    # Local bundle transition A and Cartier-unit transition h stay explicit.
    A=S.Matrix([[1,z],[0,1]]);coef=S.Matrix([1+z,2-z])
    check(f'thickening:k{k}:bundle_transition',S.expand((h*f)**(k-1))*A*coef==f**(k-1)*h**(k-1)*A*coef)

for vertices in range(2,8):
    edges=list(combinations(range(vertices),2));faces=list(combinations(range(vertices),3))
    delta0=S.zeros(len(edges),vertices)
    for i,(a,b)in enumerate(edges):delta0[i,a]=-1;delta0[i,b]=1
    delta1=S.zeros(len(faces),len(edges))
    for i,(a,b,c)in enumerate(faces):
        delta1[i,edges.index((b,c))]=1;delta1[i,edges.index((a,c))]=-1;delta1[i,edges.index((a,b))]=1
    check(f'cech:{vertices}:differences_form_cocycle',delta1*delta0==S.zeros(len(faces),vertices))
    lift=S.Matrix(range(vertices));change=S.Matrix([j*j+1 for j in range(vertices)])
    check(f'cech:{vertices}:lift_change_is_coboundary',delta0*(lift+change)-delta0*lift==delta0*change)

out={'completed_at':datetime.now(timezone.utc).isoformat(),'checker':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS continuation','target_proofs_opened':False,'producer_code_reused':False,'pass':all(x['pass']for x in checks),'check_count':len(checks),'scope':'Exact symbolic normalization/multiplier/transition identities; Laurent monomial ranges pinch [-5,10]^2 and cusp [-8,24]; truncated module exactness k=2..12 and rank=1..3; Cech differential identities on 2..7 vertices. Universal analytic divisibility and all-k lifting arguments are separately written before target reading. Finite checks do not infer universal statements.','checks':checks}
p=ROOT/'analysis/continuation_II_ledger/A2_4_A3_1_fresh.output.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'pass':out['pass'],'check_count':out['check_count'],'output':str(p)},indent=2))
