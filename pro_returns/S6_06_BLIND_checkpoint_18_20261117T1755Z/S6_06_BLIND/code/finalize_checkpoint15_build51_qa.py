"""Finalize the recorded direct visual review of the corrected complete master."""
from datetime import datetime,timezone
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
records=root/'records'
qa=json.loads((records/'typesetting_checkpoint15.json').read_text())
assert qa['master_build']==51
names=['root','checks','blind','fourfold']
reviews=[json.loads((records/f'checkpoint15_visual_{name}.json').read_text()) for name in names]
assert all(r['status']=='PASS' and r['master_build']==51 for r in reviews)
pages=[p for r in reviews for group in r['contact_sheets'].values() for p in group]
assert sorted(pages)==qa['rendered_pages'],(len(pages),len(qa['rendered_pages']))
assert len(set(pages))==len(qa['rendered_pages'])
bounds=json.loads((records/'page_boundaries_checkpoint15.json').read_text())
assert bounds['checked_pages']==qa['pages'] and not bounds['out_of_page_words']
assert not bounds['undefined_reference_warnings'] and not bounds['missing_character_warnings']
qa.update({
 'visual_inspection':'PASS: every rendered page was directly reviewed, including all pages of K57--63, all fourteen scalar-correction statement openings and their neighbouring pages, and a sample across the complete paper.',
 'visual_review_records':[f'records/checkpoint15_visual_{name}.json' for name in names],
 'visual_reviewed_page_count':len(pages),'contact_sheets_reviewed':len(qa['contact_sheets']),
 'full_size_pages_reviewed':sorted({p for r in reviews for p in r['full_size_pages']}),
 'page_boundary_audit':'records/page_boundaries_checkpoint15.json',
 'before_over_2pt':0,'after_overfull_over_2pt':qa['overfull_over_2pt'],
 'prior_master_preserved':'records/checkpoint15_prior_master49/',
 'pre_correction_master_preserved':'records/attempts/scalar_fan_premise_correction/',
 'scalar_scope_correction':'records/scalar_fan_correction_scope.json',
 'review_finalized_utc':datetime.now(timezone.utc).isoformat()
})
(records/'typesetting_checkpoint15.json').write_text(json.dumps(qa,indent=2)+'\n')
print(json.dumps({'status':'PASS','master_pages':qa['pages'],
 'rendered_and_reviewed':len(pages),'contact_sheets':len(qa['contact_sheets']),
 'max_overfull_pt':qa['max_overfull_pt'],'overfull_over_2pt':qa['overfull_over_2pt']},indent=2))
