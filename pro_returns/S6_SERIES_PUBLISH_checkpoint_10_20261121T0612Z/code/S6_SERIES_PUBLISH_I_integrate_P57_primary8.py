from pathlib import Path
import json,hashlib,datetime
from S6_SERIES_PUBLISH_editing import Editor

r=Path(__file__).resolve().parents[1];ed=Editor('I')
rp=r/'agents/i_marking/S6_SERIES_PUBLISH_I_nightP57_check_receipt.json';receipt=json.loads(rp.read_text())
assert receipt['outcome'].startswith('PASS') and receipt['evidence_groups_added']==1
for field,key in [('comparison','comparison_sha256'),('events','events_sha256'),('guard','history_guard_sha256'),('frozen_derivation','frozen_derivation_sha256')]:
    assert hashlib.sha256((r/receipt['paths'][field]).read_bytes()).hexdigest()==receipt[key]
for x in json.loads((r/receipt['paths']['guard']).read_text())['guards']:
    ed.replace(x['old'],x['new'],'D15',x['reason'],'night:P5.7',x['count'])
p=r/'agents/i_provenance/S6_SERIES_PUBLISH_I_primary_citation_guards_08.json'
for x in json.loads(p.read_text())['changes']:
    ed.replace(x['old'],x['new'],'D18',x['reason'],x['id'])
bp=r/'S6_SERIES_PUBLISH_references.bib';before=bp.read_text();s=before
gp=r/'agents/i_provenance/S6_SERIES_PUBLISH_I_shared_bib_guards_08.json'
for x in json.loads(gp.read_text())['changes']:
    assert s.count(x['old'])==1,x.get('id');s=s.replace(x['old'],x['new'])
ed.save();bp.write_text(s)
mp=r/'records/S6_SERIES_PUBLISH_required_check_completion_manifest.json';m=json.loads(mp.read_text())
assert 'night:P5.7' not in m['rows']
m['rows']['night:P5.7']={
 'paper':'I','status':'done','recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'evidence_path':receipt['paths']['comparison'],'evidence_sha256':receipt['comparison_sha256'],
 'scope':'Statement/primary-directed derivation frozen before complete target-proof exposure; exact coefficient reconstruction and full parameter/chart/half-plane comparison, with v1 primary pages and v2 statement inventory read. Expected-map hint and shared inputs disclosed. Two events form one evidence group. The September8 public-history claim is attributed to authorial chronology; no independent earlier-deposit authentication or alias transfer is claimed.'
}
mp.write_text(json.dumps(m,indent=2)+'\n')
(r/'records/S6_SERIES_PUBLISH_I_P57_primary8_integration.json').write_text(json.dumps({
 'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'source_sha256':hashlib.sha256(ed.text.encode()).hexdigest(),
 'P57_receipt_sha256':hashlib.sha256(rp.read_bytes()).hexdigest(),
 'P57_history_guard_applied':True,
 'primary8_guards_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
 'shared_bib_before_sha256':hashlib.sha256(before.encode()).hexdigest(),
 'shared_bib_after_sha256':hashlib.sha256(s.encode()).hexdigest(),
 'scope':'Root read the complete P5.7 comparison and accounting limits, the history guard, all5CDL/Xiao citation guards and full primary scope receipt. Integration changes no mathematical claim or formula and adds no root check event.'
},indent=2)+'\n')
