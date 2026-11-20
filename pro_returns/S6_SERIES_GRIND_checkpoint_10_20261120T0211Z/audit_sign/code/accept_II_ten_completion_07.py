"""Record the parent's acceptance; transport only actually viewed sample pages."""
import datetime
import hashlib
import json
from pathlib import Path

import fitz

HERE = Path(__file__).resolve().parents[1]
WORK = HERE.parent
def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

proposal = json.loads((HERE / 'II_10_completion_proposals_07.json').read_text())
old_pdf = HERE / 'II_95_QA_06/S6_SERIES_GRIND_II_build23.pdf'
new_pdf = WORK / 'S6_SERIES_GRIND_II.pdf'
old, new = fitz.open(old_pdf), fitz.open(new_pdf)
expected_current = 'efd984040d1f0c71c1e11ac34b1046acf8ae22c2e5c61926fc33d006ccd6aeba'
assert sha(new_pdf) == expected_current, 'Current PDF changed: inspect transport scope again.'
page_records = []
for n in sorted({n for r in proposal['records'] for n in r['actual_layout_pages']}):
    a = old[n-1].get_pixmap(matrix=fitz.Matrix(1.5, 1.5), alpha=False)
    b = new[n-1].get_pixmap(matrix=fitz.Matrix(1.5, 1.5), alpha=False)
    ah, bh = hashlib.sha256(a.samples).hexdigest(), hashlib.sha256(b.samples).hexdigest()
    assert (a.width,a.height,ah) == (b.width,b.height,bh), f'Changed sample page {n}'
    page_records.append({'page':n,'width':a.width,'height':a.height,'build23_pixel_sha256':ah,
                         'build27_pixel_sha256':bh,'equal':True})

receipt = {
    'date_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'scope':'Exact 108-dpi pixel equality transports the actual build23 visual sample receipt to build27. This is not a new human image viewing or a claim that every intervening proof page was viewed.',
    'prior_visual_receipt':'II_95_visual_QA_06.json',
    'prior_visual_receipt_sha256':sha(HERE/'II_95_visual_QA_06.json'),
    'build23_pdf_sha256':sha(old_pdf),'build27_pdf_sha256':sha(new_pdf),
    'pages':page_records,
}
transport = HERE/'II_ten_build23_to27_layout_transport_07.json'
transport.write_text(json.dumps(receipt,indent=2)+'\n')

canonical = HERE/'row_assessments.json'
rows = json.loads(canonical.read_text())
before = {r['label']:rows[r['label']] for r in proposal['records']}
(HERE/'II_ten_canonical_before_acceptance_07.json').write_text(json.dumps(before,indent=2)+'\n')
for r in proposal['records']:
    label = r['label']
    prior = rows[label]
    full_routes = '; '.join(f"{v['event_id']}: {v['outcome']}" for v in r['exact_retained_outcomes'])
    computation = r['computation_applicability']
    if r.get('current_computation_event_id'):
        computation += ' Current exact certificate: '+r['current_computation_event_id']+'. This program was written after printed-proof comparison; no before-reading credit is inferred.'
    prior.update({
        'confidence_state':'complete at the exact retained whole-step route and recorded receiving scopes',
        'confidence_line':r['full_target_scope']+' Current complete comparison receipt(s): '+', '.join(r['current_comparison_ids'])+'. '+computation,
        'independent_routes':full_routes+' Retained computation scope: '+r['retained_computation_scope']+' Current reviewers use the same GPT-6 Astra model family; no additional model independence is claimed.',
        'remaining_risk':'No row-specific unresolved gate remains in the accepted joined review. Imported dependencies retain their separately recorded proof, reading-order and literature scopes. This row closure does not close any other row or a main theorem. '+r['source_credit']['relation'],
        'format_check':'Passed at full current statement/proof comparison scope; exact targets and source locators in II_candidate_computation_source_applicability_07.json and II_10_completion_proposals_07.json. No changed source-format guard applies to this row.',
        'layout_check':'Actually viewed build23 sample pages '+', '.join(map(str,r['actual_layout_pages']))+' in II_95_visual_QA_06.json; exact pixel equality to build27 established by II_ten_build23_to27_layout_transport_07.json. Intervening unviewed pages are not claimed as visually inspected.',
        'completion_state':'done',
    })
canonical.write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n')
summary = {'date_utc':receipt['date_utc'],'parent_acceptance':'Root message accepting precisely UN5,9,14,20,23,26,28,32,47,74; UN1 remains pending.',
           'labels':[r['label'] for r in proposal['records']],
           'canonical_sha256':sha(canonical),'proposal_sha256':sha(HERE/'II_10_completion_proposals_07.json'),
           'layout_transport_sha256':sha(transport),'sample_pages':len(page_records)}
(HERE/'II_ten_canonical_acceptance_07.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
