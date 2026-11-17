"""Finalize direct visual review of all46 rendered pages of build49."""
from datetime import datetime, timezone
from pathlib import Path
import json

root=Path(__file__).resolve().parents[1]
records=root/'records'
qa=json.loads((records/'typesetting_checkpoint14.json').read_text())
assert qa['master_build']==49 and qa['pages']==519
root_review={
 'utc':datetime.now(timezone.utc).isoformat(),'reviewer':'root','status':'PASS','master_build':49,
 'contact_sheets':{k:qa['contact_sheets'][k] for k in ['1','2','6']},
 'page_count_reviewed':22,'full_size_pages':[18,85,154,519],
 'method':'Direct image review of three final-master contact sheets and four full-size pages.',
 'findings':{
  'clipping':'None observed, including the existing 1.61101pt overflow on page18.',
  'collisions':'None observed.',
  'missing_symbols':'None observed.',
  'tables_and_matrices':'The dense page85 comparison and page154 integral matrices are legible and aligned.',
  'ending':'The final bibliography page519 is complete and legible.'
 },'scope':'Visual layout only.'
}
(records/'checkpoint14_visual_root.json').write_text(json.dumps(root_review,indent=2)+'\n')
names=['root','checks','blind','fourfold']
reviews=[json.loads((records/f'checkpoint14_visual_{name}.json').read_text()) for name in names]
assert all(r['status']=='PASS' and r['master_build']==49 for r in reviews)
pages=[p for r in reviews for group in r['contact_sheets'].values() for p in group]
assert sorted(pages)==qa['rendered_pages'] and len(set(pages))==46
assert sum(r['page_count_reviewed'] for r in reviews)==46
bounds=json.loads((records/'page_boundaries_checkpoint14.json').read_text())
assert bounds['checked_pages']==519 and not bounds['out_of_page_words']
assert not bounds['undefined_reference_warnings'] and not bounds['missing_character_warnings']
qa.update({
 'visual_inspection':'PASS: all six contact sheets and all46 rendered pages directly inspected, including every page of K50–56 and a sample across the full manuscript. Eleven dense or modified pages were additionally inspected full-size. The K55 inline-math export was repaired and its final standalone also reviewed in full.',
 'visual_review_records':[f'records/checkpoint14_visual_{name}.json' for name in names],
 'visual_reviewed_page_count':46,'contact_sheets_reviewed':6,
 'full_size_pages_reviewed':sorted({p for r in reviews for p in r['full_size_pages']}),
 'page_boundary_audit':'records/page_boundaries_checkpoint14.json',
 'before_over_2pt':0,'after_overfull_over_2pt':0,
 'prior_master_preserved':'records/checkpoint14_prior_master47/',
 'inline_math_attempt_preserved':'records/checkpoint14_inline_math_attempt_build48/',
 'inline_math_review':'records/k55_inline_math_visual_qa.json'
})
(records/'typesetting_checkpoint14.json').write_text(json.dumps(qa,indent=2)+'\n')
print(json.dumps({'status':'PASS','master_pages':519,'rendered_and_reviewed':46,
 'contact_sheets':6,'full_size_reviewed':len(qa['full_size_pages_reviewed']),
 'max_overfull_pt':qa['max_overfull_pt'],'overfull_over_2pt':0},indent=2))
