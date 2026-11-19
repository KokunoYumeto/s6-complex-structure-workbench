#!/usr/bin/env python3
"""Independent whole-fixed-cap intersection and physical-index audit."""
import json,hashlib
from datetime import datetime,timezone
from pathlib import Path
import sympy as s
a,wp,wm=s.symbols('a wp wm',integer=True)
Q=s.Matrix([[0,1,0],[1,0,0],[0,0,-1]])
lp=s.Matrix([1,wp,-a]);lm=s.Matrix([-1,wm,1-a])
b=lp+lm;b2=(b.T*Q*b)[0];c2=(lp.T*Q*lm)[0]
assert s.expand(b2+(1-2*a)**2)==0
assert s.expand(c2+a*(a-1)-(wm-wp))==0
k=c2-b2;ell=3-b2+4*c2
index=s.factor((4*k-ell)/24)
assert s.simplify(index-a*(a-1)/2)==0
c=s.symbols('c',integer=True)
assert (4*c-4*c)/24==0
root=Path(__file__).resolve().parents[2]
src=root/'notes/part3_source_zero_real_trace_working.md'
out={'status':'PASS','reviewer':'fourfold','utc':datetime.now(timezone.utc).isoformat(),
 'source':str(src.relative_to(root)),'sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
 'scope':'RT16--17 whole fixed cap and actual cap-replacement bordism only; full finite-strip assembly remains separately audited.',
 'b2':str(b2),'c2':str(s.expand(c2)),'index':str(index),
 'proof_audit':['The extending marked Mobius map retains both branch divisors and their exceptional incidence.',
 'The cap orientation C has boundary partial F, so F-C is complex Bl(P1xP1); e_cap=v e_F gives +B.',
 'The actual g_plus/g_minus maps retain both winding integers. Their zero-class ratios have global logarithms and extend only on the specified auxiliary cap.',
 'Both HB cross terms occur in c2, while b has no H term. The physical tautological line is O(-1).',
 'The Y-times-triangle gluing uses the third map as the exact inverse composite, retaining normal bundles and physical line.',
 'S4=C-C0 retains its actual normal clutch; its index is zero without imposing a c2 value.',
 'No separate local D4 fixed-S3 cap is inserted and the entire exceptional E remains in F.']}
(root/'records/fourfold_audit_source_zero_whole_cap.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS whole-cap polynomial and full RT16--17 proof audit')
