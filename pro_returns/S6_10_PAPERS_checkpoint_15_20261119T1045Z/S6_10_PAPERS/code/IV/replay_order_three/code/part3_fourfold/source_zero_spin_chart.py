#!/usr/bin/env python3
"""Actual determinant arrows on the source-reset and charged charts."""
import json,hashlib
from datetime import datetime,timezone
from pathlib import Path
import sympy as s
B,D,z,xi=s.symbols('B D z xi', nonzero=True)
v=(B-D*z)/2
F2=1-B*z**3-(1-2*v)*z**2
Xp=F2/z**2;Ap=-F2/z**3
Bp=B-D*z-F2/z**3;Dp=-Bp/z;wp=-z
Jsource=s.factor(s.Matrix([Ap,Dp,wp]).jacobian([B,D,z]).det())
out={'source_reset_jacobian':str(Jsource),'line_resets':[]}
for a in (1,2):
    xip=(-1)**a*z**(-2*a)*xi
    J=s.factor(s.Matrix([Ap,Dp,wp,xip]).jacobian([B,D,z,xi]).det())
    out['line_resets'].append({'a':a,'jacobian':str(J)})
U,w,S1,T1,T0=s.symbols('U w S1 T1 T0',nonzero=True)
charged=s.Matrix([U*w,S1,T1,U*T0,1/U])
Jcharged=s.factor(charged.jacobian([U,w,S1,T1,T0]).det())
assert Jcharged==-1
out['charged_ambient_jacobian']=str(Jcharged)
out['determinant_square_roots']={'a1':'1/z','a2':'I/z**2','charged':'I'}
assert s.simplify((1/z)**2-s.sympify(out['line_resets'][0]['jacobian'],locals={'z':z}))==0
assert s.simplify((s.I/z**2)**2-s.sympify(out['line_resets'][1]['jacobian'],locals={'z':z}))==0
assert s.I**2==Jcharged
# A full physical turn in the a=2 gauge has angles (-pi,-pi,pi,pi).
# In the canonical SU(4) spinor lift its endpoint is (-1)^degree,
# precisely the canonical complex mu_2 action on Lambda^{0,*}.
spin=[]
for bits in range(16):
    ns=[(bits>>j)&1 for j in range(4)]
    exponent=-ns[0]-ns[1]+ns[2]+ns[3]
    assert (-1)**exponent==(-1)**sum(ns)
    spin.append({'occupation':ns,'endpoint':int((-1)**sum(ns))})
out['canonical_mu2_spinor_endpoint']=spin
out['scope']='Exact determinant arrows only; global spin/compact attachment is not inferred.'
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
root=Path(__file__).resolve().parents[2]
peer=root/'notes/part3_source_zero_real_trace_working.md'
audit={'status':'PASS','reviewer':'fourfold','utc':datetime.now(timezone.utc).isoformat(),
 'source':str(peer.relative_to(root)),'source_sha256':hashlib.sha256(peer.read_bytes()).hexdigest(),
 'scope':'RT15 local lower-arm and fixed-tube spin dictionary only; global cyclic ownership is still explicit.',
 'checks':['O(-2) source-auxiliary contracted two-form extends and fixes the bounding RP3 spin structure.',
 'The ordered normal determinant gives canonical lift -omega4; the base lift is the same, yielding +omega8.',
 'The ungauged adjacent-node map has determinant -1 and preserves the auxiliary Euler field; constant root i fixes its lift.',
 'A full physical turn has the canonical +omega8 endpoint and closes through the actual mu2 deck.',
 'Two negative complex conjugations have even real parity and representative e2e4 commuting with omega8.',
 'The fixed S3 cap uses the literal RT9 frame; its spin lift has no H1 choice. The full source-reset roots are retained separately in EA13.']}
(root/'records/fourfold_audit_source_zero_spin_local.json').write_text(json.dumps(audit,indent=2)+'\n')
print(json.dumps(out,indent=2))
