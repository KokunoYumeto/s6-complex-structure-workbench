"""Record the direct master-PDF image reviews for checkpoint12."""
from datetime import datetime, timezone
from pathlib import Path
import json

root=Path(__file__).resolve().parents[1]
records=root/'records'
qa=json.loads((records/'typesetting_checkpoint12.json').read_text())
root_review={
    'utc':datetime.now(timezone.utc).isoformat(),
    'reviewer':'root','status':'PASS','master_build':45,
    'contact_sheets':{k:qa['contact_sheets'][k] for k in ['1','2','7']},
    'page_count_reviewed':19,'full_size_pages':[18,85,154],
    'method':'Direct image-tool inspection of all three contact sheets and the three full-size pages.',
    'findings':{
        'clipping':'None observed. The existing 1.61101pt overflow on page18 remains inside the page and legible.',
        'collisions':'None observed.',
        'missing_symbols':'None observed.',
        'dense_displays':'The return table on page85 and integral matrices on page154 remain clearly rendered.',
        'ending':'The final bibliography page is clean, with normal spacing and no truncation.'
    },
    'scope':'Visual layout review only.'
}
(records/'checkpoint12_visual_root.json').write_text(json.dumps(root_review,indent=2)+'\n')
names=['root','checks','blind']
reviews=[json.loads((records/f'checkpoint12_visual_{name}.json').read_text()) for name in names]
assert all(r['status']=='PASS' for r in reviews)
reviewed=[p for r in reviews for group in r['contact_sheets'].values() for p in group]
assert sorted(reviewed)==qa['rendered_pages']
assert len(reviewed)==len(set(reviewed))==sum(r['page_count_reviewed'] for r in reviews)==51
assert sum(len(r['contact_sheets']) for r in reviews)==7
bounds=json.loads((records/'page_boundaries_checkpoint12.json').read_text())
assert bounds['checked_pages']==qa['pages']==479
assert not bounds['out_of_page_words']
assert not bounds['undefined_reference_warnings']
assert not bounds['missing_character_warnings']
qa.update({
    'visual_inspection':'PASS: all seven contact sheets, covering all51 rendered pages, directly reviewed. The overflow page and eight selected dense/new pages were also reviewed full-size.',
    'visual_review_records':[f'records/checkpoint12_visual_{name}.json' for name in names],
    'visual_reviewed_page_count':len(reviewed),
    'contact_sheets_reviewed':7,
    'page_boundary_audit':'records/page_boundaries_checkpoint12.json',
    'before_over_2pt':0,
    'after_overfull_over_2pt':0
})
(records/'typesetting_checkpoint12.json').write_text(json.dumps(qa,indent=2)+'\n')
print(json.dumps({'status':'PASS','master_pages':479,'rendered_and_reviewed':51,'contact_sheets':7,'overfull_over_2pt':0,'max_overfull_pt':qa['max_overfull_pt']},indent=2))
