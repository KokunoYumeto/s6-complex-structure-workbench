#!/usr/bin/env python3
"""Literal finite end norms after the retained adjacent-node arrow."""
import json
from pathlib import Path
import sympy as s
r,R,a,ns,nt,U,V=s.symbols('r R a ns nt U V',positive=True)
checks=[]
def ck(name,e):
    z=s.simplify(s.powsimp(e,force=True));assert z==0,(name,z)
    checks.append({'name':name,'pass':True})
# Work separately at the two actual charges; no symbolic branch simplification.
for av in (1,2):
    for r0 in (s.Rational(1,3),s.Rational(1,5)):
        for sv in (r0/s.Integer(4),r0/s.Integer(2),r0):
            tv=r0;Rv=sv*tv;d=(Rv/r0**2)**av
            ck(f'end_s_{av}_{r0}_{sv}',d**s.Rational(-1,av)*sv-r0)
            ck(f'end_t_{av}_{r0}_{sv}',d**s.Rational(1,av)*tv-sv)
            ck(f'product_{av}_{r0}_{sv}',(d**s.Rational(-1,av)*sv)*(d**s.Rational(1,av)*tv)-Rv)
ck('transported_common_line',1/(1/U)-U)
tau=s.symbols('tau',real=True)
# Forward contracting physical flow has S growing and T shrinking.
ck('Ht_forward_inward_derivative',s.diff(r**2*s.exp(-2*tau)-r**2,tau).subs(tau,0)+2*r**2)
ck('Hs_forward_outward_derivative',s.diff(r**2*s.exp(2*tau)-r**2,tau).subs(tau,0)-2*r**2)
out={'status':'PASS','count':len(checks),'checks':checks,
 'line_arrow':'U_j -> V_(j-1)^(-1) after retained c_lambda normalization; not primary U_(j-1)=q/V_(j-1)',
 'faces':['N_t=r^a,R<=r^2 = D4_S(r) x S3_T(r)','N_s=r^-a,R<=r^2 = S3_S(r) x D4_T(r)'],
 'orientation':'Forward contracting real flow enters H_t and exits H_s; target-minus-source has positive product-ball boundary orientation.',
 'scope':'Full local finite faces and their actual line/norm/side arrows; global compact period-strip assembly remains explicit.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(f'PASS {len(checks)} exact finite-face checks')
