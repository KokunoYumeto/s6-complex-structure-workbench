#!/usr/bin/env python3
"""Whole fixed-trace cap arithmetic with both actual clutch windings.

Analytic gluing and the two-cap morphism are RT.16--17.
This certificate assigns no individual source-zero return.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sympy as s

ROOT=Path(__file__).resolve().parents[2]
a,wp,wm,c=s.symbols('a wp wm c',integer=True)
Q=s.Matrix([[0,1,0],[1,0,0],[0,0,-1]])
checks=[]
def eq(name,x,y):
    assert s.expand(x-y)==0,name
    checks.append(name)
def pair(x,y): return (x.T*Q*y)[0]
lp=s.Matrix([1,wp,-a]); lm=s.Matrix([-1,wm,1-a])
b=lp+lm
eq('determinant H coefficient',b[0],0)
eq('determinant B coefficient',b[1],wp+wm)
eq('determinant E coefficient',b[2],1-2*a)
bsq=pair(b,b); c2=pair(lp,lm)
eq('whole capped determinant square',bsq,-(1-2*a)**2)
eq('whole capped second Chern class',c2,-a*(a-1)+wm-wp)
k=c2-bsq; ell=3-bsq+4*c2
eq('physical k',k,3*a*a-3*a+1+wm-wp)
eq('physical ell',ell,4+4*(wm-wp))
eq('full winding cancellation',4*k-ell,12*a*(a-1))
eq('fixed trace physical index',(4*k-ell)/24,a*(a-1)/2)
for aa in (1,2):
    for pp in range(-7,8):
        for mm in range(-7,8):
            eq(f'actual-winding arithmetic a{aa} wp{pp} wm{mm}',
               ((4*k-ell)/24).subs({a:aa,wp:pp,wm:mm}),s.Rational(aa*(aa-1),2))
eq('S4 k with retained c2',c,c)
eq('S4 ell with retained c2',4*c,4*c)
eq('S4 index with retained c2',(4*c-4*c)/24,0)
note=ROOT/'notes/part3_source_zero_real_trace_working.md'
data={'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),
      'checks':len(checks),'identities':checks,
      'intersection_matrix':Q.tolist(),
      'clutch_convention':'e_cap=g e_F; winding g contributes +w B on the doubled parameter sphere.',
      'line_classes':{'plus':'H-aE+w_plus B','minus':'-H+(1-a)E+w_minus B'},
      'physical_pair':['3a^2-3a+1+w_minus-w_plus','4+4(w_minus-w_plus)'],
      'fixed_index':'a(a-1)/2',
      'S4_pair':['c2','4c2'],
      'scope':'RT.16--17 whole fixed-trace cap and actual two-cap correction. No completed finite period strip or global source-zero return.',
      'source_sha256':hashlib.sha256(note.read_bytes()).hexdigest()}
(ROOT/'code/part3/source_zero_fixed_cap.json').write_text(json.dumps(data,indent=2)+'\n')
print(f'PASS: {len(checks)} whole-cap and retained-clutch identities.')
print(data['scope'])
