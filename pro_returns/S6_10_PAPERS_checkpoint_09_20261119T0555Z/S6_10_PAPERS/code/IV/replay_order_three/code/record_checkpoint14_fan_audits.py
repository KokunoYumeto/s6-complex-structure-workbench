"""Record completed root audits of the native first flops and shear fans."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

root=Path(__file__).resolve().parents[1]
items=[
('P3K.54','notes/part3_source_cusp_first_flops_working.md','code/part3/source_cusp_first_flops.json',
 ['The three native charts have literal standard transitions with the actual source-height, units, periods and cap overlap retained.',
  'The unrestricted Cox identity gives the actual positive-family boundary arrow and its oriented exterior extension.',
  'The native triples (0,-6,1),(0,-6,1),(-6,0,1) give central classes23,23,1.',
  'The fixed reflection resets the complex normal convention and verifies the three inverse changes.'],
 'The three first periodic flops only.'),
('P3K.56','notes/part3_source_cusp_vertical_fans_working.md','code/part3/source_cusp_vertical_fans.json',
 ['The sheared torus characters and period generators have the displayed integral inverse and full unit multipliers.',
  'The explicit translated triangle identities cover every unimodular fan containing the physical vertical edge.',
  'The general product and exact graph traces give the two nonfixed diagonal variation and derivative entries without using a transverse fixed-edge value.',
  'The universal native-to-ordinary pure-left correction preserves the right integers6n-6 and-6n.',
  'Both adjacent periodic flips have the actual displayed triangle, character and period maps, with the native Cox comparison applied on each fan.',
  'The two inverse recurrences from the actual central change sum for every signed integer n to1-3n(n-1) modulo28.'],
 'All physical-delta-retaining lattice-basis fans for the specified positive source loop. No full characteristic pair is inferred.')]
for ident,proof,certfile,checks,scope in items:
    cert=json.loads((root/certfile).read_text())
    assert cert['status']=='PASS'
    record={'utc':datetime.now(timezone.utc).isoformat(),'reviewer':'root','status':'PASS',
            'statement':ident,'proof':proof,
            'proof_sha256':hashlib.sha256((root/proof).read_bytes()).hexdigest(),
            'certificate':certfile,'verified_maps':checks,'scope':scope}
    path=root/'records'/('root_audit_'+ident.replace('.','_')+'.json')
    path.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'statement':ident,'status':'PASS','record':str(path.relative_to(root))}))
