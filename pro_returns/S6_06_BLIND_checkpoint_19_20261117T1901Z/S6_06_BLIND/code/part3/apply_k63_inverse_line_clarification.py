#!/usr/bin/env python3
"""Preserve and clarify K63's real-connection versus complex-line sign."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil
R=Path(__file__).resolve().parents[2]
archive=R/'code/part3/attempts/k63_inverse_line_convention'
archive.mkdir(parents=True,exist_ok=False)
paths=[
 'notes/part3_source_cusp_shear_pontryagin_working.md',
 'notes/part3_source_cusp_shear_pontryagin.tex',
 'code/part3/source_cusp_shear_pontryagin.py',
 'code/part3/source_cusp_shear_pontryagin.json',
 'code/part3/source_cusp_shear_pontryagin.out',
 'code/part3/source_cusp_shear_pontryagin.err',
 'code/part3/k63_standalone.pdf',
 'records/k63_standalone_visual_qa.json',
]
before={}
for name in paths:
 p=R/name
 shutil.copy2(p,archive/p.name)
 before[name]=hashlib.sha256(p.read_bytes()).hexdigest()
p=R/paths[0]
src=p.read_text()
old=r'''For a rho turn d_n changes to d_n-6nv, and for a q turn it changes'''
new=r'''Here \(A_n(\partial_d)=1\) is a real principal-circle
connection. The physical complex line \(\mathcal L_\delta\) has
unitary connection \(2\pi iA_n\), so
\(c_1(\mathcal L_\delta)=-dA_n\). Thus the positive real-curvature
class used below is that of its inverse
\(\mathcal U_n=\mathcal L_\delta^{-1}\). P3K.66, EC.1--2,
records the local Hopf and associated-line arrow explicitly.
The vanishing pairing proved here is unchanged by this sign.

For a rho turn d_n changes to d_n-6nv, and for a q turn it changes'''
assert src.count(old)==1
src=src.replace(old,new)
replacements={
'''parameter-dependent Chern class differs from the old one by''':
'''inverse-line Chern class differs from the old inverse-line class by''',
'''One can realize this class directly by cutting in theta: its circle
coordinate is glued by d to d-6n b at the two ends.''':
'''One can realize this inverse-line class directly by cutting in theta:
the physical circle coordinate is glued by d to d-6n b at the two ends,
and the dual coefficient has the opposite gluing.''',
'''Thus this supplies an actual
representative of (SQ.15) on C_0, including the cap identification.''':
'''Its dual therefore supplies an actual
representative of (SQ.15) on C_0, including the cap identification.''',
'''These maps identify the circle-line difference with
(SQ.15), up to the exact curvature terms already retained in (SQ.14)''':
'''These maps identify the inverse-circle-line difference with
(SQ.15), equivalently the physical Euler-line difference with its
negative, up to the exact curvature terms already retained in (SQ.14)''',
'''has only the interior term (SQ.15) and
the exact curvature terms in (SQ.13)--(SQ.14).''':
'''has only the physical Euler interior term, the negative of (SQ.15),
and the exact curvature terms in (SQ.13)--(SQ.14).''',
}
for old,new in replacements.items():
 assert src.count(old)==1,(old,src.count(old))
 src=src.replace(old,new)
p.write_text(src)
p=R/'code/part3/source_cusp_shear_pontryagin.py'
src=p.read_text()
src=src.replace("'exact boundary Euler primitive'","'exact real principal-connection primitive'")
old="'retained_Euler_difference':'6*n*[dtheta] cup b, with outer primitive -n*(du+alpha_Q*dv) plus the full periodic-unit one-form',"
new="""'retained_Euler_difference':'-6*n*[dtheta] cup b for the physical complex line L_delta',
        'inverse_line_Chern_difference':'6*n*[dtheta] cup b for U=L_delta^(-1)',
        'connection_convention':'A(partial_delta)=1, c1(L_delta)=-dA, c1(U)=dA',
        'retained_real_connection_primitive':'-n*(du+alpha_Q*dv) plus the full periodic-unit one-form',"""
assert src.count(old)==1
p.write_text(src.replace(old,new))
record={
 'utc':datetime.now(timezone.utc).isoformat(),
 'status':'Clarification of real-connection and associated-line signs',
 'before_sha256':before,
 'reason':'K66 makes explicit that a positive real principal connection has c1(L_delta)=-dA. The positive SQ15 class is c1 of the inverse line. K63 ell=0, all stated numerical and relative conclusions, and its 29 algebraic identities are unchanged.',
 'audit':'Root and blind_control full EC1--5 audits pass; exact local Hopf/page line arrow retained.',
 'scope':'Only K63 proof notation and certificate metadata are clarified; no new fan value is assigned here.'
}
(archive/'clarification.json').write_text(json.dumps(record,indent=2)+'\n')
(archive/'README.md').write_text(
 '# Preserved K63 connection convention\n\n'
 'These are the exact preclarification artifacts. The displayed positive '
 'real-curvature class in SQ.15 is the Chern class of the inverse physical '
 'line. The physical Euler class has the opposite sign. This has no effect '
 'on the zero Pontryagin pairing or any statement of P3K.63. '
 'The full typed sign and orientation comparison is EC.1--2 of P3K.66.\n')
print('Preserved old K63 artifacts and clarified inverse-line convention.')
