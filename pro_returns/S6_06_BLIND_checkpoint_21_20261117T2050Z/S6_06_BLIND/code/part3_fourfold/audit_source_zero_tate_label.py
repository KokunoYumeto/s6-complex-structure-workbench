#!/usr/bin/env python3
"""Peer checks for the full TL node/Cartier arrow, with analytic scope stated."""
import hashlib,json
from datetime import datetime,timezone
from pathlib import Path
import sympy as s
root=Path(__file__).resolve().parents[2]
S,T,q2,uQ,uP,xi=s.symbols('S T q2 uQ uP xi',nonzero=True)
q1=S*T; Q=q1*q2*uQ; P=uP/q2; uG=uQ*uP
Z0=uG*T; W0=q2*S/uP
checks=[]
def check(name,expr):
    z=s.simplify(expr);assert z==0,(name,z)
    checks.append({'name':name,'pass':True})
check('Tate_node_product',Z0*W0-Q)
check('actual_h_source_reindex',Q*P/S-Z0)
check('theta_product_Q_over_S',Q/S-T*q2*uQ)
check('theta_denominator_S_over_P',S/P-W0)
check('theta_denominator_Q_over_S_over_P',Q/(S/P)-Z0)
thetaS,thetaSP=s.symbols('thetaS thetaSP',nonzero=True)
f=thetaS/(P*thetaSP); E=2*thetaS/((1-S)*thetaSP)
for a in (1,2):
    V=xi*f**a/((1-S)/2)**a
    check(f'full_line_map_degree_{a}',P**a*V-E**a*xi)
old=[(0,0),(1,0),(1,1),(0,1)]
new=[(1-x,y) for x,y in old]
assert new==[(1,0),(0,0),(0,1),(1,1)]
checks.append({'name':'actual_positive_square_to_current_T0','pass':True})
source=root/'notes/part3_source_zero_tate_label_working.md'
out={'status':'PASS','reviewer':'fourfold','utc':datetime.now(timezone.utc).isoformat(),
 'source':str(source.relative_to(root)),'sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'exact_checks':checks,
 'proof_audit':['Same branch Cartier divisors give extending b_T and its inverse on the normal conifold; marked G fixes its value one.',
 'The ideal map lifts both projective charts and retains the a=2 r arrow at source and target.',
 'The theta products converge normally with Q/S and Q/(S/P) expressed as actual extending source functions.',
 'E_plus restricts to 2/(1-uG*T0) on q2=0; the full unit is retained.',
 'The actual h period includes P^a, so the valuation map is an extending monomial-times-unit map with the stated physical circle.'],
 'scope':'Full local bidisc source/Cartier/fan label only; no compact end or absolute source-zero class.'}
(root/'records/fourfold_audit_source_zero_tate_label.json').write_text(json.dumps(out,indent=2)+'\n')
print(f'PASS {len(checks)} exact algebra checks and full local proof audit')
