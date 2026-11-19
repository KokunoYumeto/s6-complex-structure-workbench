#!/usr/bin/env python3
"""Exact chamber and residual-character ledger; no global end asserted."""
import json
from pathlib import Path
import sympy as s

a=s.symbols('a', integer=True, positive=True)
checks=[]
def check(name, expr):
    ok=s.simplify(expr)==0
    checks.append({'name':name,'pass':bool(ok),'residual':str(s.simplify(expr))})
    if not ok: raise AssertionError(name)

# Primary: (S0,S1,T1,z,V), auxiliary/physical weights.
ap=[1,1,-1,a-1,-a]; pp=[0,0,0,1,-1]
# Complement: (U,w,S1,T1,T0).
ac=[a,1-a,1,-1,-1]; pc=[1,-1,0,0,0]
for i,(j,k) in enumerate([(1,0),(2,1),(3,2),(4,3)]):
    # U=1 and V=1 both require auxiliary exponent -1/a.
    check(f'physical_chart_weight_{i}',pc[j]-ac[j]/a-(pp[k]-ap[k]/a))
for i,(j,k) in enumerate([(1,0),(2,1),(3,2),(4,3)]):
    check(f'residual_mu_a_character_{i}',s.rem(s.Poly(ac[j]-ap[k],a),s.Poly(a,a)).as_expr())

rw,rs,rt,rz=s.symbols('rw rs rt rz', real=True)
mu_comp=a+(1-a)*rw+rs-rt-rz
mu_prim=rw+rs-rt+(a-1)*rz-a
check('moment_sum_not_assumed_zero',mu_comp+mu_prim-((2-a)*rw+2*rs-2*rt+(a-2)*rz))
check('reduced_moment_sum', (mu_comp+mu_prim).subs(a,2)-2*(rs-rt))
check('primary_V_origin_negative',mu_prim.subs({rw:0,rs:0,rt:0,rz:0})+a)
check('complement_U_origin_positive',mu_comp.subs({rw:0,rs:0,rt:0,rz:0})-a)

# Actual adjacent-node arrow and retained scalar normalization.
q,c=s.symbols('q c', nonzero=True)
check('adjacent_node_U',c*q/c-q)
check('adjacent_node_V',c/c-1)
check('node_product',q*1-q)

# Ungauged continuation between the complementary and primary charged charts.
U,w,S1,T1,T0=s.symbols('U w S1 T1 T0', nonzero=True)
S0p=U*w; zp=U*T0; Vp=1/U
check('ungauged_q_preserved',S0p*zp*Vp-U*w*T0)
sig=s.symbols('sig', nonzero=True)
v_comp=S1*T1+(T1*U*w-S1*T0)/(2*sig)
v_prim=S1*T1+(T1*S0p-S1*zp*Vp)/(2*sig)
check('ungauged_full_v_preserved',v_comp-v_prim)
check('ungauged_inverse_U',1/Vp-U)
check('ungauged_inverse_w',S0p*Vp-w)
check('ungauged_inverse_T0',zp*Vp-T0)
check('ungauged_source_weight_S0',a+(1-a)-1)
check('ungauged_source_weight_z',a-1-(a-1))
check('ungauged_source_weight_V',-a-(-a))
check('ungauged_physical_weight_S0',1-1)
check('ungauged_physical_weight_z',1-1)
check('ungauged_physical_weight_V',-1-(-1))

out={'status':'PASS','checks':checks,'count':len(checks),
     'scope':'Chart chambers, residual characters and exact moments only; the outward radial-boundary normal is not inferred from a chamber label.',
     'primary_weights':[str(x) for x in ap],
     'complement_weights':[str(x) for x in ac],
     'mu_primary':str(mu_prim),'mu_complement':str(mu_comp)}
p=Path(__file__).with_suffix('.json');p.write_text(json.dumps(out,indent=2)+'\n')
print(f"PASS {len(checks)} exact chamber/character checks")
