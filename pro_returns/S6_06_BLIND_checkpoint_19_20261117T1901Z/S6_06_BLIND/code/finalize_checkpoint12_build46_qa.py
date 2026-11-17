"""Finalize direct image review of the 481-page checkpoint12 master."""
from datetime import datetime,timezone
from pathlib import Path
import json

root=Path(__file__).resolve().parents[1]
records=root/'records'
qa=json.loads((records/'typesetting_checkpoint12.json').read_text())
assert qa['master_build']==46 and qa['pages']==481
root_review={
    'utc':datetime.now(timezone.utc).isoformat(),'reviewer':'root',
    'status':'PASS','master_build':46,
    'contact_sheets':{k:qa['contact_sheets'][k] for k in ['1','2','7']},
    'page_count_reviewed':22,'full_size_pages':[18,85,154],
    'method':'Direct review of the freshly rendered build46 contact sheets and three full-size pages.',
    'findings':{'clipping':'None observed, including the existing1.61101pt overflow on page18.',
                'collisions':'None observed.','missing_symbols':'None observed.',
                'tables_and_matrices':'Dense page85 table and page154 matrices remain legible and correctly aligned.',
                'ending':'Final bibliography pages480-481 render cleanly.'},
    'scope':'Visual layout only.'
}
(records/'checkpoint12_visual_root.json').write_text(json.dumps(root_review,indent=2)+'\n')
names=['root','checks','fourfold']
reviews=[json.loads((records/f'checkpoint12_visual_{name}.json').read_text()) for name in names]
assert all(r['status']=='PASS' and r['master_build']==46 for r in reviews)
pages=[p for r in reviews for group in r['contact_sheets'].values() for p in group]
assert sorted(pages)==qa['rendered_pages'] and len(set(pages))==54
assert sum(r['page_count_reviewed'] for r in reviews)==54
bounds=json.loads((records/'page_boundaries_checkpoint12.json').read_text())
assert bounds['checked_pages']==481
assert not bounds['out_of_page_words'] and not bounds['undefined_reference_warnings'] and not bounds['missing_character_warnings']
qa.update({
    'visual_inspection':'PASS: all seven contact sheets and all54 rendered pages directly inspected, including every page of the six new proofs and a full-document sample. The overflow page and eight additional dense/new pages were also inspected full-size.',
    'visual_review_records':[f'records/checkpoint12_visual_{name}.json' for name in names],
    'visual_reviewed_page_count':54,'contact_sheets_reviewed':7,
    'page_boundary_audit':'records/page_boundaries_checkpoint12.json',
    'before_over_2pt':0,'after_overfull_over_2pt':0,
    'superseded_review_evidence':'records/checkpoint12_build45/'
})
(records/'typesetting_checkpoint12.json').write_text(json.dumps(qa,indent=2)+'\n')
print(json.dumps({'status':'PASS','master_pages':481,'rendered_and_reviewed':54,'contact_sheets':7,'max_overfull_pt':qa['max_overfull_pt'],'overfull_over_2pt':0},indent=2))
