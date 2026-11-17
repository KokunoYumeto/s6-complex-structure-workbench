#!/usr/bin/env python3
"""Record direct review of all pages and the two-page heading correction."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'records/qa_k57.json';r=json.loads(p.read_text())
cmp=json.loads((ROOT/'records/k57_final_layout_compare.json').read_text())
assert r['compile']=='PASS' and not r['overflows_pt'] and not r['boundary_issues']
assert cmp['changed_pages']==[15,16]
r.update(visual_review='PASS',visual_review_utc=datetime.now(timezone.utc).isoformat(),reviewer='fourfold',
 page_count_reviewed=22,reviewed_contact_sheets=list(range(1,7)),
 full_size_pages=[1,8,13,15,16,19,22],
 findings=['All22 pages directly inspected through the six contact sheets. No clipping, equation collision, malformed table, or missing symbol found.',
 'The IE.2 heading initially stood alone at the foot of page15. The exporter now keeps each subsection heading with the next paragraph.',
 'Final raster comparison proves pages1–14 and17–22 unchanged. Both changed pages15–16 were directly reviewed at full size; IE.2 now starts page16 with its paragraph.',
 'Final isolated compile has zero overfull boxes, no undefined references, no missing characters, and no page-boundary violations.'],
 pdf_sha256=hashlib.sha256((ROOT/'code/part3_fourfold/k57_standalone.pdf').read_bytes()).hexdigest(),
 layout_comparison='records/k57_final_layout_compare.json')
p.write_text(json.dumps(r,indent=2)+'\n')
(ROOT/'records/k57_standalone_visual_qa.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({k:r[k] for k in ['visual_review','pages','overflows_pt','full_size_pages','pdf_sha256']},indent=2))
