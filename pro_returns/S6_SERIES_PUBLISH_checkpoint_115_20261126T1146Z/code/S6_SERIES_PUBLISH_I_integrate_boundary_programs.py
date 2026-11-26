from pathlib import Path
import json,hashlib,datetime
from S6_SERIES_PUBLISH_editing import Editor

r=Path(__file__).resolve().parents[1]
p=r/'agents/i_provenance/S6_SERIES_PUBLISH_I_boundary_program_guards.json'
j=json.loads(p.read_text())
assert hashlib.sha256(p.read_bytes()).hexdigest()=='7054cc23f466b288757c047c5d8b11d446cdc5ff6192faad27eceb60794f23c9'
ed=Editor('I')
for x in j['changes']:
    ed.replace(x['old'],x['new'],x['defect'],x['reason'],x['statement_id'])
ed.save()
(r/'records/S6_SERIES_PUBLISH_I_boundary_program_integration.json').write_text(json.dumps({
    'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'guard_path':str(p.relative_to(r)), 'guard_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
    'source_sha256':hashlib.sha256(ed.text.encode()).hexdigest(), 'guards':len(j['changes']),
    'root_review':'Read all guarded diffs, all six program rows and the complete nine-proof comparison. No formulas, labels, permanent tags or local morphisms changed. The complete old/proposed proofs were reread by the provenance agent; nine exposed reread associations retain their single evidence group. Root integration adds no check events.'
},indent=2)+'\n')
