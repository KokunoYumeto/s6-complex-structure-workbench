#!/usr/bin/env python3
"""Record full-size direct visual review of the five K59 proof pages."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'records/qa_k59.json';r=json.loads(p.read_text())
assert r['compile']=='PASS' and r['pages']==5 and not r['overflows_pt']
assert not r['boundary_issues'] and not r['missing_character'] and not r['undefined_reference']
r.update(visual_review='PASS',visual_review_utc=datetime.now(timezone.utc).isoformat(),reviewer='fourfold',
 page_count_reviewed=5,full_size_pages=[1,2,3,4,5],
 findings=['All five final pages directly reviewed at full size.',
 'The initially overlong CF.13 display was split into three aligned rows; the final build has zero overfull boxes.',
 'No clipping, equation collision, malformed matrix, missing symbol, orphan heading, or bad page boundary found.',
 'The complete all-j statement, explicit CF.6a unitary path and proved-P0-only diagnostic scope are present.'],
 pdf_sha256=hashlib.sha256((ROOT/'code/part3_fourfold/k59_standalone.pdf').read_bytes()).hexdigest(),
 source_sha256=hashlib.sha256((ROOT/'notes/part3_source_cusp_mutation_staircase_working.md').read_bytes()).hexdigest(),
 peer_certificate='code/part3_fourfold/source_cusp_mutation_peer_certificate.json')
p.write_text(json.dumps(r,indent=2)+'\n')
(ROOT/'records/k59_standalone_visual_qa.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({k:r[k] for k in ['visual_review','pages','overflows_pt','pdf_sha256','source_sha256']},indent=2))
