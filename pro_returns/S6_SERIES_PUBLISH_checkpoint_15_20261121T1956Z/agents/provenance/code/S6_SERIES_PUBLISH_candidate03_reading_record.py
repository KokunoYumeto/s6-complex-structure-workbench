"""Record the seven page images actually read by provenance_inventory.

The prose below is a manual reading record. Hash checks bind that reading to
the supplied candidate; this script does not perform or claim page reading.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

BASE = Path('/workspace/scratch/653608133b22')
OUT = BASE / 'work/agents/provenance'
RENDER = BASE / 'work/render/V_candidate_03'
SOURCE = BASE / 'work/S6_SERIES_PUBLISH_V.tex'
SOURCE_SHA = 'f89b9eceecd318960aab0df4b292335bf69b5b30635c399efb37f1de1f2d63b7'
PDF_SHA = 'ac8468a9641f9747dbddd74a5e8dfd9c725872a754ec57cc1e8859da43172b73'
ASSIGNED = [135, 136, 137, 138, 139, 145, 164]

NOTES = {
    135: 'Read the complete Proposition 18.6 on the natural stable framing and its bounding spin structure, including proof Steps 1–4. Hirsch is now cited at Chapter 3, §2, Theorem 2.1, p. 74; Theorem 2.5, p. 78; and cutoff globalization, pp. 75–76. These locators agree with the directly viewed corrected fifth printing of the 1976 book recorded in the primary locator receipt. The fixed-collar cutoff argument, surjective differential, stable tangent formula and induced boundary framing are visible and legible. No remaining concrete defect observed.',
    136: 'Read Theorem 18.7 and proof Steps 1–4: the weighted Hopf construction, the four-cone orbifold, the principal torus chart, the contractible universal cover and the fundamental-group/Smith calculation. The Scott citation now prints Theorems 2.3–2.4, p. 425, and the Euler-characteristic comparison, pp. 427–428, matching the previously viewed published article. The maps, formulas and local references are legible. No remaining concrete defect observed.',
    137: 'Read Theorem 18.7 proof Steps 5–7 through its conclusion, then section 19, Definition 19.1 and the beginning of Proposition 19.2. Davis–Kirk is cited at Definition 8.16, p. 209, and Theorem 8.17 and proof, pp. 209–210, matching the directly viewed electronic text and its separately recorded edition evidence. The maps-to-a-space form of Pontryagin–Thom and the extension over the bordism are explicit. The stable splittings, framed inverse image and boundary framing are legible. The section heading is accompanied by the definition and proposition rather than standing alone. No remaining concrete defect observed.',
    138: 'Read the rest of Proposition 19.2 and proof Steps 1–4: the marked peripheral structure, the zero-linking framing, the restriction radical and the ordinary closed spinning construction. The Winter citation explicitly identifies arXiv v3, §3, the paragraph before Theorem 3.4, p. 4; the 2009 year refers to the published bibliography entry and the version-specific page is retained. This agrees with the primary v3 page already viewed. Formula numbering, displayed relations and the page-break continuation are legible. No remaining concrete defect observed.',
    139: 'Read Proposition 19.2 proof Steps 5–6 and its conclusion, followed by Theorem 19.3 and its proof opening. Winter is cited explicitly as arXiv v3, Theorem 4.5 and following discussion, pp. 9–10, agreeing with the viewed statement, proof and longitude qualification. The first-spin source scope is explicit, and the iterated-spin complement decomposition and stronger arbitrary-spin obstruction remain displayed in the paper. No remaining concrete citation, wording or layout defect observed.',
    145: 'Read the continuation of Theorem 20.1 proof, Steps 4–8, including the Euler vector, circle-kernel bundle, faithful central action and exact order of the outer action; then the beginning of Theorem 20.2 with its marked torus twist. Scott Theorem 3.6 now has the verified printed page 436. The integral basis, determinant, Euler-vector sign, character values and displayed boundary marking remain legible. No remaining concrete defect observed.',
    164: 'Read the end of Proposition 22.1, including the explicit translation matrix, endpoint monodromy and full outer-marking comparison, then the opening of Proposition 22.2. Its matrices and fixed vectors now cite local Definition 17.1 and explicitly identify the ordered bases (g,u,w,d)=(gamma-hat,u-hat,w-hat,delta-hat). The current source of Definition 17.1 was also compared for this reference: it displays the two A_j matrices, the v_j vectors and the dual covector gamma in that basis. The B_j matrices on ker(gamma), the quotient convention and the cap boundary map are legible. No remaining concrete defect observed.'
}

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

manifest_path = RENDER / 'manifest.json'
manifest = json.loads(manifest_path.read_text())
pdf = Path(manifest['pdf'])
assert digest(SOURCE) == SOURCE_SHA
assert digest(pdf) == PDF_SHA == manifest['pdf_sha256']
assert manifest['pages'] == 177
images = {row['page']: row for row in manifest['rendered_pages']}
pages = []
for page in ASSIGNED:
    row = images[page]
    image = Path(row['image'])
    actual = digest(image)
    assert actual == row['image_sha256']
    pages.append({
        'page': page,
        'image': str(image),
        'image_sha256': actual,
        'pdf_sha256': PDF_SHA,
        'read_date_utc': '2026-11-21',
        'reading': 'actual rendered image viewed and read',
        'content_and_findings': NOTES[page],
        'remaining_findings': []
    })

record = {
    'candidate': 'V_candidate_03',
    'source': str(SOURCE),
    'source_sha256': SOURCE_SHA,
    'pdf': str(pdf),
    'pdf_sha256': PDF_SHA,
    'pdf_pages': 177,
    'render_manifest': str(manifest_path),
    'render_manifest_sha256': digest(manifest_path),
    'assigned_pages': ASSIGNED,
    'reader': 'GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited (no separate numeric setting exposed), S6_SERIES_PUBLISH/provenance_inventory',
    'recorded_at_utc': datetime.now(timezone.utc).isoformat(),
    'method': 'Direct visual reading of each of the seven actual rendered page images. Extracted text and automated checks were not substituted for reading. Source and manifest hashing bind the record to the candidate; they do not establish mathematical correctness.',
    'defect_scope': 'All 24 prompt defect classes were considered where applicable to these seven body pages, with particular attention to exact cited editions/page locators, the local datum and explicit ordered-basis identification, numbering, cross-references, mathematical wording and layout. Other candidate pages are assigned to the parent and other agents.',
    'primary_locator_receipt': str(OUT / 'literature/S6_SERIES_PUBLISH_V_remaining_locator_receipt.json'),
    'source_comparison_scope': 'The printed local Definition 17.1 reference and ordered-basis identification on p. 164 were compared with the current source of def:V:resolved-product-data. This is integration/reference QA, with no new proof-check credit.',
    'mathematical_events_added': 0,
    'completed': True,
    'pages_read': len(pages),
    'remaining_findings': [],
    'new_guarded_edits': [],
    'scope_limit': 'This record concerns the seven assigned candidate03 pages and the exact immutable images listed below. It does not by itself certify all 177 pages or any subsequent candidate.',
    'pages': pages
}
stem = OUT / 'S6_SERIES_PUBLISH_V_final_candidate03_reading_provenance'
stem.with_suffix('.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')

lines = [
    '# V candidate03: final changed-page reading',
    '',
    '**All seven assigned pages were actually viewed and read. No remaining concrete defect was observed, and no further source guard is proposed.**',
    '',
    f'- Candidate: `V_candidate_03`, 177 pages.',
    f'- Source SHA256: `{SOURCE_SHA}`.',
    f'- PDF SHA256: `{PDF_SHA}`.',
    '- Assigned and read pages: 135–139, 145, 164.',
    '- Reading date: 21 November 2026 UTC.',
    '- Mathematical check events added: **0**.',
    '',
    record['method'],
    '',
    record['defect_scope'],
    '',
    'The source locators were checked against the already opened primary editions recorded in `literature/S6_SERIES_PUBLISH_V_remaining_locator_receipt.json`. The record preserves the distinction between Winter’s published 2009 entry and the explicit arXiv v3 pagination, and between the Hirsch 1976 book and the corrected fifth printing actually viewed. Davis–Kirk’s directly viewed electronic pages and separate publisher edition evidence remain described precisely in that receipt.',
    '',
    '## Per-page reading',
    ''
]
for row in pages:
    lines += [f"### Page {row['page']}", '', row['content_and_findings'], '', f"Image SHA256: `{row['image_sha256']}`.", '', f"PDF SHA256: `{PDF_SHA}`.", '']
lines += ['## Scope', '', record['scope_limit'], '', 'The JSON companion contains the exact image paths, hashes, PDF/source hashes and manifest binding. Hashing was performed after the visual reading solely to identify the reviewed artifacts.', '']
stem.with_suffix('.md').write_text('\n'.join(lines))
print(json.dumps({'completed': True, 'pages_read': len(pages), 'remaining_findings': [], 'mathematical_events_added': 0, 'json': str(stem.with_suffix('.json')), 'markdown': str(stem.with_suffix('.md'))}, indent=2))
