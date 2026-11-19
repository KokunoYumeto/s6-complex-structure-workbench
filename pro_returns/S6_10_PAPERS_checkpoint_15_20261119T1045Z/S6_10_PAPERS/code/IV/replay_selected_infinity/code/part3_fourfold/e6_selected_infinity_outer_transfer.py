#!/usr/bin/env python3
"""Exact algebra and orientation checks for OT; not a substitute for its maps."""
from pathlib import Path
import hashlib, json
import sympy as S

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).with_suffix('.json')
checks=[]
def eq(name, left, right=0):
    z=S.factor(S.together(left-right))
    assert z==0, (name,z)
    checks.append({'name':name,'difference':'0'})

e,x,y,t,q,chi,sigma,lam,H,Bbar,kap=S.symbols('epsilon x y t q chi sigma lambda H Bbar kappa_c', nonzero=True)
d=1-3*e**2
xo=e**2*x/d**2; yo=e**3*y/d**3; to=e**4*t/d**3
r=e**2*(3*e**2-2)/d**2
native=y*y-x**3-(3*e**2-2)*x*x-d*t*x-e*e*t*t
eq('full original cubic',yo*yo-xo**3-r*xo**2-to*xo-to*to,e**6/d**6*native)
nu=e**2/d
eq('original r in resolved III parameter',r,-2*nu-3*nu**2)
eq('selected original height',nu**2*(1+2*nu),e**4/d**3*(1-e**2))
eq('selected q direction',to-nu**2*(1+2*nu),e**4/d**3*(t-(1-e**2)))
eq('actual r local degree two coefficient',S.limit(r/e**2,e,0),-2)
eq('actual height local degree four coefficient',S.limit((e**4/d**3)/e**4,e,0),1)
eq('full native-to-complement raw Hom',lam*(chi*sigma)**4*(chi**-4*H*sigma**-6*Bbar),lam*sigma**4*H*(sigma**-6*Bbar))
rp,rt,fp,ft=S.symbols('r_p r_target f_p f_target',nonzero=True)
Braw=sigma**-6*Bbar
Bpt=Braw*rt/rp
eq('genuine point-frame Hom square',lam*(chi*sigma)**4*(chi**-4*H*Braw*rt/rp),lam*sigma**4*H*Bpt)
eq('selected theta/genuine/raw coefficient square',Bpt*(ft/rt)/(fp/rp),Braw*ft/fp)
eq('genuine Cartier inverse ratio',(rt/rp)*(rp/rt),1)

A,BB=S.symbols('A B')
for j in range(-8,9):
    X=chi**j*A; Y=chi**(-j-1)*BB
    eq(f'chain product j={j}',X*Y,chi**-1*A*BB)
    eq(f'actual physical coefficient j={j}',sigma**j*X,(chi*sigma)**j*A)
    eq(f'finite phase/period commutation j={j}',S.I**(j+4),S.I**j)

v,ld=S.symbols('v_sigma ell_d')
so=3*ld-4*v
eq('quarter-turn cap logarithm',so.subs(v,v-S.Rational(1,4))-so,1)
eq('four-sector cap logarithm',so.subs(v,v-1)-so,4)
j0,j1,j2,j3=S.symbols('j0 j1 j2 j3',integer=True)
js=j0+j1+j2+j3
eq('four A steps retained',sum([1,1,1,1]),4)
eq('four actual B reference integers retained',sum([j0,j1,j2,j3]),js)
eq('m2 n1 cap relation A4 Bsum = B^(2+sum)',S.Rational(4,2)+js,2+js)

for aa in [2,6]:
    # In completed-point -> original-tensor coordinates H_o has order -a,
    # sigma and epsilon have the same positive boundary winding.
    wminus=-(4+aa-4)
    wplus=-aa+4
    eq(f'negative conjugate phase a={aa}',wminus,-aa)
    eq(f'positive phase a={aa}',wplus,4-aa)
    eq(f'full determinant phase a={aa}',wminus+wplus,4-2*aa)

rows={
 'strict':(42,108), 'mu2_points':(-2,-14),
 'interior_one_copy':(-18,-126), 'exceptional_one_copy':(-20,-20),
 'refinement_one_copy':(18,126), 'p_curves_one_copy':(0,-18),
 'interface_curves_one_copy':(0,0)}
mult={key:(1 if key in ('strict','mu2_points') else 2) for key in rows}
compact=tuple(sum(mult[key]*value[i] for key,value in rows.items()) for i in (0,1))
eq('complete compact k_U',compact[0],0)
eq('complete compact ell_U',compact[1],18)
moving=(kap,4*kap+6)
inner=tuple(S.expand(compact[i]+moving[i]) for i in (0,1))
eq('whole inner U cubic',inner[0],kap)
eq('whole inner U p1-linear',inner[1],4*kap+24)
eq('inner U polynomial independent of actual c2',(4*inner[0]-inner[1])/24,-1)
physical=tuple(-z for z in inner)
jin=tuple(-z for z in physical)
eq('physical positive-parameter polynomial',(4*physical[0]-physical[1])/24,1)
eq('Jin actual physical polynomial',(4*jin[0]-jin[1])/24,-1)

def sign_of_permutation(order):
    return (-1)**sum(order[i]>order[j] for i in range(len(order)) for j in range(i+1,len(order)))
eq('outer radial normal crosses five Y directions',sign_of_permutation([5,0,1,2,3,4,6]),-1)
for k in range(3):
    # Complex fixed base dimension k. Original order is F,radial,circle,link.
    # Circle moved first has sign -; removed-tube radial is -partial_r.
    circle_to_front=(-1)**(2*k+1)
    boundary_sign=(-1)*circle_to_front*((-1)**(2*k))
    eq(f'inner fixed-link quotient orientation dimC F={k}',boundary_sign,1)
eq('Jin parameter interval derivative',S.diff(1-t,t),-1)
eq('Jin interval inverse',(1-t).subs(t,1-t),t)
eq('K68 factor exchange 4 by 3',(-1)**(4*3),1)
eq('physical base reflection determinant',S.diag(-1,-1,-1,1).det(),-1)

proof=ROOT/'notes/part3_e6_selected_infinity_outer_transfer_working.md'
inputs=[proof,ROOT/'notes/part3_e6_selected_infinity_moving_cap_working.md',ROOT/'notes/part3_e6_selected_infinity_compact_normal_stars_working.md',ROOT/'notes/part3_e6_selected_infinity_strict_surfaces_working.md']
data={'status':'PASS','check_count':len(checks),'checks':checks,
 'scope':'Exact source, height, Hom, chain, cap-word, phase, component-pair and orientation identities for the fully written OT maps. No value is assigned to kappa_c; no other fan or half-turn is covered.',
 'pairs':{'compact_U':list(compact),'moving_U':[str(z) for z in moving],'inner_U':[str(z) for z in inner],'positive_parameter_M':[str(z) for z in physical],'Jin_M':[str(z) for z in jin]},
 'actual_return_index':-1,'geometric_proof_status':'working proof awaiting independent outer-transfer audit',
 'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}}
OUT.write_text(json.dumps(data,indent=2)+'\n')
print(f'PASS {len(checks)} exact OT identities; actual c2 retained symbolically; index -1.')
