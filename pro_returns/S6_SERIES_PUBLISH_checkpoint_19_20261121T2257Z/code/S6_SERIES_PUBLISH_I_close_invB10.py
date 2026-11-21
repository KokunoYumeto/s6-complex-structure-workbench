from pathlib import Path
import json, hashlib, datetime

r=Path(__file__).resolve().parents[1]
receipt=json.loads((r/'agents/i_marking/S6_SERIES_PUBLISH_I_invB10_check_receipt.json').read_text())
assert receipt['outcome']=='PASS' and receipt['evidence_groups_added']==1
for field,key in [('comparison','comparison_sha256'),('events','events_sha256'),('frozen_derivation','frozen_derivation_sha256')]:
    assert hashlib.sha256((r/receipt['paths'][field]).read_bytes()).hexdigest()==receipt[key]
p=r/'records/S6_SERIES_PUBLISH_required_check_completion_manifest.json'
j=json.loads(p.read_text())
assert 'inv:B1.0' not in j['rows']
j['rows']['inv:B1.0']={
    'paper':'I','status':'done','recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'evidence_path':receipt['paths']['comparison'],'evidence_sha256':receipt['comparison_sha256'],
    'scope':'Fresh statement-directed derivation frozen before complete target-proof exposure; newly written exact full-kernel reconstruction, coordinate solves and fraction-free determinant calculation. Primary transcriptions are shared inputs; two event rows constitute one evidence group, with no alias transfer.'
}
p.write_text(json.dumps(j,indent=2)+'\n')
print('Completed inv:B1.0 with one scoped fresh evidence group.')
