"""Finalize direct visual review of the 498-page checkpoint13 master."""
from datetime import datetime, timezone
from pathlib import Path
import json

root = Path(__file__).resolve().parents[1]
records = root / 'records'
qa = json.loads((records / 'typesetting_checkpoint13.json').read_text())
assert qa['master_build'] == 47 and qa['pages'] == 498
root_review = {
    'utc': datetime.now(timezone.utc).isoformat(), 'reviewer': 'root',
    'status': 'PASS', 'master_build': 47,
    'contact_sheets': {k: qa['contact_sheets'][k] for k in ['1', '2', '6']},
    'page_count_reviewed': 19, 'full_size_pages': [18, 85, 154, 240],
    'method': 'Direct image review of three build47 contact sheets and four full-size pages.',
    'findings': {
        'clipping': 'None observed, including the existing 1.61101pt overflow on page18.',
        'collisions': 'None observed.', 'missing_symbols': 'None observed.',
        'tables_and_matrices': 'Dense page85 table and page154 matrices are legible and aligned.',
        'scope_correction': 'The clarified K29 statement on page240 fits cleanly.',
        'ending': 'The final bibliography page498 is complete and legible.'
    },
    'scope': 'Visual layout only.'
}
(records / 'checkpoint13_visual_root.json').write_text(json.dumps(root_review, indent=2) + '\n')
names = ['root', 'checks', 'blind', 'fourfold']
reviews = [json.loads((records / f'checkpoint13_visual_{name}.json').read_text()) for name in names]
assert all(r['status'] == 'PASS' and r['master_build'] == 47 for r in reviews)
pages = [p for r in reviews for group in r['contact_sheets'].values() for p in group]
assert sorted(pages) == qa['rendered_pages'] and len(set(pages)) == 43
assert sum(r['page_count_reviewed'] for r in reviews) == 43
bounds = json.loads((records / 'page_boundaries_checkpoint13.json').read_text())
assert bounds['checked_pages'] == 498
assert not bounds['out_of_page_words']
assert not bounds['undefined_reference_warnings'] and not bounds['missing_character_warnings']
qa.update({
    'visual_inspection': 'PASS: all six contact sheets and all43 rendered pages directly inspected, including every page of K46-49, the clarified K29 statement and a full-document sample. Eleven dense or modified pages were additionally inspected full-size.',
    'visual_review_records': [f'records/checkpoint13_visual_{name}.json' for name in names],
    'visual_reviewed_page_count': 43, 'contact_sheets_reviewed': 6,
    'full_size_pages_reviewed': sorted({p for r in reviews for p in r['full_size_pages']}),
    'page_boundary_audit': 'records/page_boundaries_checkpoint13.json',
    'before_over_2pt': 0, 'before_overfull_over_2pt': 0, 'after_overfull_over_2pt': 0,
    'prior_master_preserved': 'records/checkpoint13_prior_master46/'
})
(records / 'typesetting_checkpoint13.json').write_text(json.dumps(qa, indent=2) + '\n')
print(json.dumps({'status': 'PASS', 'master_pages': 498, 'rendered_and_reviewed': 43,
                  'contact_sheets': 6, 'max_overfull_pt': qa['max_overfull_pt'],
                  'overfull_over_2pt': 0}, indent=2))
