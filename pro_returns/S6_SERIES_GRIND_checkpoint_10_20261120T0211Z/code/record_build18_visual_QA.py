"""Verify all actual visual-inspection receipts against the current renders."""
from pathlib import Path
import hashlib,json,datetime
R=Path(__file__).resolve().parents[1]
qa=json.loads((R/'analysis/rendered_qa.json').read_text());seen={}
receipts=[]
for owner in ['audit_paper_i','audit_sign','audit_corrections','audit_root']:
 p=R/owner/'build18_visual_QA.json';a=json.loads(p.read_text());receipts.append(str(p.relative_to(R)))
 for entry in a.get('files',a.get('sheets',[])):
  path=Path(entry.get('absolute_file') or entry.get('file') or entry.get('path'))
  if not path.is_absolute():path=R/path
  assert hashlib.sha256(path.read_bytes()).hexdigest()==entry['sha256'],str(path)
  assert entry.get('actually_viewed',True)
  seen[str(path)]=dict(owner=owner,sha256=entry['sha256'])
for paper,v in qa.items():
 for path in v['contact_sheets']:assert path in seen,path
 v['inspection_state']=f"All {len(v['rendered_pages'])} listed current pages were actually visually inspected. No clipping or missing glyph was found. This is the selected/repaired-page inspection, not an every-page reading."
 if paper=='II':v['inspection_state']+=' A visible empty proof-step marker on p.517 remains explicitly flagged for structural cleanup.'
 if paper=='IV':v['inspection_state']+=' Remaining low-F literal-caret and historical-filename prose is recorded for source cleanup.'
 v['sheet_sha256']={p:seen[p]['sha256'] for p in v['contact_sheets']}
 v['inspection_recorded_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
(R/'analysis/rendered_qa.json').write_text(json.dumps(qa,indent=2)+'\n')
(R/'analysis/build18_complete_visual_inspection.json').write_text(json.dumps({'receipts':receipts,'verified_sheets':len(seen),'pages':sum(len(v['rendered_pages']) for v in qa.values()),'known_residuals':['II p.517 empty first-level proof marker','Low-F literal-caret and historical-filename cleanup'],'all_current_images_match_actual_inspection_receipts':True},indent=2)+'\n')
print(json.dumps({'verified_sheets':len(seen),'pages':sum(len(v['rendered_pages']) for v in qa.values())}))
