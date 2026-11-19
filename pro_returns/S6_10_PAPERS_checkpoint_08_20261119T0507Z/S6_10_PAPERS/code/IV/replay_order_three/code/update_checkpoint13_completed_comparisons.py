"""Register K48-49 and preserve their precise unresolved continuation steps."""
from datetime import datetime,timezone
from pathlib import Path
import ast
import json

root=Path(__file__).resolve().parents[1]
utc=datetime.now(timezone.utc).isoformat()
path=root/'code/update_report.py'
source=path.read_text().replace('P3K.40–P3K.47','P3K.40–P3K.49')
old=('The separate nonfixed-edge integer and the general source-loop fan '
     'formula remain under proof.')
new=('P3K.48 constructs the actual periodic ordinary smooth product of the '
     'three labelled curve neighbourhoods. Its exact quaternion normal '
     'maps retain the physical-circle axis of degree+3 and the closed '
     'fixed-curve frame degrees(6,0) in complex-curve orientation, '
     'equivalently(-6,0) in the K23 Hopf orientation. All nonlinear units '
     'and vertex collars are carried by explicit maps. The connecting-map '
     'sign, common-exterior variation correction, separate nonfixed-edge '
     'integer and general source-loop fan formula remain under proof.')
assert source.count(old)==2
source=source.replace(old,new)
old=('The old source-coordinate loop also requires its exact finite-cap endpoint comparison: '
     'v=u^3, T=u^4*t and z_old^m=u^4*z_new^m retain a threefold source covering '
     'and a root rotation. The generic suspension scalar cancellation does not replace that character square.')
new=('P3K.49 completes the actual punctured old-u/new-v family comparison, '
     'with v=u^3, T=u^4*t, the root endpoint D^(-4), the reduced doubled '
     'period, and the full annular d-delta clutch retained. It fixes the '
     'previously unselected F0 by continuation of the entire old reference '
     'map, solves the full root-groupoid cochain, and constructs the global '
     'annular isomorphism by an explicit scalar factorization. The oriented '
     'old mapping torus is that of the third new return, with the actual '
     'scalar rescaling retained. This establishes the parameter comparison '
     'without asserting the still-unassembled central attachment or a '
     'numerical source-zero return.')
assert source.count(old)==2
source=source.replace(old,new)
ast.parse(source)
path.write_text(source)

record={
 'utc':utc,'reviewer':'root','statement':'P3K.48','status':'PASS',
 'proof':'notes/part3_source_cusp_ordinary_product_working.md',
 'checks':[
  'The actual second vertex map gives the three specified reciprocal tangent coordinates and ordered normal transition matrices.',
  'All zero-winding units have their based periodic logarithms. The residual loops diag(1,exp(-6i theta)) and diag(exp(-6i theta),1) are filled by the displayed based quaternion maps.',
  'The convention Q=n0+j*conjugate(n1) preserves the complex normal orientation and gives exactly the required two endpoint actions.',
  'The actual-to-reference equality z*D_ref*K=z*D_source fixes the tube-map direction. The three tubes glue to both vertex collars, with normal rescaling and cutoff velocity flows carrying all higher terms.',
  'The fixed and both nonfixed physical-circle conjugations are literal. The full unit maps remain as explicit outer conjugations.',
  'The three preimages of minus i have derivatives 4*vartheta_prime*k and 3*j; (k,j) is positive there, so the collapsed cylinder degree is +3.',
  'For the closed fixed-curve gauge, the exact product formula for -tr((g^-1 dg)^3)/(24*pi^2) gives two boundary traces +6*dpsi*dtheta. Their integral is +6 in complex-z orientation, hence -6 in Hopf-h orientation.',
  'The right gauge factors through the radial/parameter cylinder and has zero third class. Diagonal unit-log contractions preserve both computed degrees.'
 ],
 'peer_audit':'fourfold independently passed OP1-4; root additionally verified OP5 coefficient and orientation',
 'scope_limits':'The ordinary marked product and its explicit circle/frame defect. No connecting homomorphism sign, relative-return correction or general fan class is entered.'
}
(root/'records/root_audit_P3K_48.json').write_text(json.dumps(record,indent=2)+'\n')
record={'utc':utc,'new_statements':['P3K.48','P3K.49'],
        'audits':['records/root_audit_P3K_48.json','records/root_audit_P3K_49.json'],
        'standalone_qa':['records/k48_standalone_visual_qa.json','records/k49_standalone_visual_qa.json'],
        'central_attachment_status':'unproved; exact local-system mismatch retained',
        'source_zero_numeric_return':'uncomputed'}
(root/'records/checkpoint13_completed_comparisons_inclusion.json').write_text(json.dumps(record,indent=2)+'\n')

bib=root/'S6_06_BLIND_references.bib'
entry=(root/'code/part3_fourfold/references_atiyah_bott.bib').read_text()
assert 'AtiyahBott1984' not in bib.read_text()
with bib.open('a') as f:
    f.write('\n'+entry.strip()+'\n')
log=root/'S6_06_BLIND_literature_log.md'
text=log.read_text()
entries=[]
for line in (root/'records/literature_fourfold.md').read_text().splitlines():
    if ('2026-11-17T12:00:18.526081' in line or '2026-11-17T12:02:52.101362' in line) and 'Atiyah' in line:
        stamp=line.split(' — ',1)[0].removeprefix('- ')
        body=line.split(' — ',1)[1].replace('|',' / ')
        entries.append('| '+stamp+' | Atiyah–Bott1984 primary scan | Actual compact fixed-component localization input | '+body+' Original detailed entry: records/literature_fourfold.md. |\n')
assert len(entries)==2
marker='| 2026-11-17T12:08:'
position=text.find(marker)
if position<0:
    position=len(text)
text=text[:position]+'\n'+''.join(entries)+'\n'+text[position:]
log.write_text(text)
print('Registered K48-49, root audit, verified localization reference and chronological primary read entries.')
