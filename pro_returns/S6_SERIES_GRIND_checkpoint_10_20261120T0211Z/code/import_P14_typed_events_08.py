"""Lossless controlled-vocabulary transport of the fresh P1.4 event table."""
from pathlib import Path
import csv,hashlib,json
R=Path(__file__).resolve().parents[1]
source=R/'audit_p14_fresh/events_08.tsv'
dest=R/'audit_root/P14_typed_events_08.tsv'
assert not dest.exists()
types={'fresh_exact_computation':'computation or formal certificate',
       'full_derivation_freeze':'independent re-proof',
       'complete_receiving_proof_review':'targeted proof check',
       'whole_row_proposal':'targeted proof check'}
out=[]
with source.open() as f:
 for n,r in enumerate(csv.DictReader(f,delimiter='\t'),2):
  payload=json.dumps(r,sort_keys=True,ensure_ascii=False)
  out.append({'statement_id':r['target'],'date':r['utc'],'who':r['actor'],
    'type':types[r['event_type']],
    'outcome':r['claim_scope']+' [Exposure: '+r['exposure_stage']+'] [Original event kind: '+r['event_type']+'] [Evidence: audit_p14_fresh/'+r['evidence']+']'+(' This proposal records a publication gate; it adds no independent mathematical check.' if r['event_type']=='whole_row_proposal' else ''),
    'event_id':'ce:grind-p14:'+hashlib.sha256(payload.encode()).hexdigest()[:16]})
with dest.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(out[0]),delimiter='\t');w.writeheader();w.writerows(out)
print(json.dumps({'source':str(source.relative_to(R)),'typed_rows':len(out),'raw_source_sha256':hashlib.sha256(source.read_bytes()).hexdigest()}))
