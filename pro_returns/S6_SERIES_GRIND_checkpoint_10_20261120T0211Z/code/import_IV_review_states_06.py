"""Import reviewed source credit and the closed K112 dependency once."""
from pathlib import Path
import csv
import datetime
import hashlib
import json

ROOT=Path(__file__).resolve().parents[1]
credit_path=ROOT/'audit_corrections/IV_whole_row_completion_review_05.json'
review=json.loads(credit_path.read_text())
assert len(review['rows'])==30
inv=ROOT/'S6_SERIES_GRIND_inventory.csv'
with inv.open() as stream:
    rows=list(csv.DictReader(stream));columns=list(rows[0])
changed=[]
for entry in review['rows']:
    assert entry['ready_for_completion_after_parent_global_QA']
    assert not entry.get('remaining_row_text_gates')
    proposal=entry['inventory_credit_proposal']
    targets=[r for r in rows if r['label']==entry['label']]
    assert targets,entry['label']
    for row in targets:
        for k,v in proposal.items():
            if k not in columns:columns.append(k)
            row[k]=v
    changed.append(dict(label=entry['label'],placements=len(targets),fields=proposal))
with inv.open('w',newline='') as stream:
    w=csv.DictWriter(stream,fieldnames=columns);w.writeheader();w.writerows(rows)
assess=ROOT/'audit_root/row_assessments.json'
data=json.loads(assess.read_text())
proposal_path=ROOT/'audit_sign/K112_proposed_assessment.json'
proposal=json.loads(proposal_path.read_text())['night:P3K.112']
assert 'night:P3K.112' in data
proposal['completion_state']='pending current moved-proof layout and final source-credit integration'
data['night:P3K.112']=proposal
alt_path=ROOT/'audit_sign/K111_final_alternate_inventory.json'
alt=json.loads(alt_path.read_text())
data[alt['label']]={k:alt[k] for k in ('confidence_state','confidence_line','remaining_risk')}
data[alt['label']].update(
    format_check='All445 original formula tags retained exactly once across the proved filling and this final alternative; every original relocated passage is byte-preserved. The exact absent arrays and unsupported numerical execution are stated.',
    completion_state='pending current final-part layout and disposition review',
    independent_routes='Exact supplied-file inventory; explicit nonuniqueness witness for the underdetermined old triangulation; guarded relocation with complete original tag/multiplicity comparison. No absent execution is credited as replayed.')
assess.write_text(json.dumps(data,indent=2)+'\n')
receipt=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    imported_source_credit=changed,
    review_sha256=hashlib.sha256(credit_path.read_bytes()).hexdigest(),
    K112_proposal_sha256=hashlib.sha256(proposal_path.read_bytes()).hexdigest(),
    qualification='Only the exact reviewed source-credit fields and K112 mathematical assessment are imported. Current build22 layout and final completion remain explicit gates.')
(ROOT/'analysis/IV_credit_and_K112_import_06.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'source_credit_labels':len(changed),'K112_mathematical_gate':'closed','current_layout':'pending'}))
