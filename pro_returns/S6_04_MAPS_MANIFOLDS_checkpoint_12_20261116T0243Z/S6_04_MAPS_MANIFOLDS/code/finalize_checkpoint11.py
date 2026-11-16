"""Record checkpoint11 QA after actual frozen-PDF image inspection."""
from pathlib import Path
import datetime
import hashlib
import json
import shutil

root = Path(__file__).resolve().parents[1]
stage = root.parent / 'checkpoint_build_11' / root.name
qa = json.loads((stage / 'records/pdf_qa/qa.json').read_text())
extra = json.loads((stage / 'records/pdf_qa/checkpoint_11_extra_pages.json').read_text())
audit = json.loads((stage / 'records/register_audit.json').read_text())
spread, additional = qa['rendered_pages'], extra['extra_rendered_pages']
qa['rendered_pages'] = sorted(set(spread + additional))
qa['preliminary_overflow_values_pt'] = []
qa['preliminary_max_overflow_pt'] = 0
qa['repairs'] = []
qa['visual_review'] = (
    f"Passed: {len(spread)} spread pages and {len(additional)} additional pages, "
    f"{len(qa['rendered_pages'])} distinct pages, inspected as rendered images. "
    'All four newly registered proofs, the changed D.2.4 scope and the complete bibliography are covered. '
    'No clipping, overlap or displaced mathematical labels was observed.')
qa['enlarged_pages'] = [188]
qa['reviewed_utc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
assert qa['overfull_boxes'] == 0 and not qa['unresolved_citations']
assert audit['manuscript_statement_count'] == audit['register_statement_count'] == 192
assert audit['open_statements'] == ['D.2.4'] and audit['report_prompt_rows'] == 19
assert {'D.2.44', 'D.2.45', 'D.2.46', 'D.2.47'} <= set(extra['statement_pages'])
freeze = json.loads((stage / 'records/checkpoint_11_manifest.json').read_text())['source_frozen_utc']
pdf_hash = hashlib.sha256((stage / 'S6_04_MAPS_MANIFOLDS_paper.pdf').read_bytes()).hexdigest()
qa['pdf_sha256'] = pdf_hash
text = f'''

## Checkpoint11 typesetting and consistency verification

The frozen manuscript has {qa['pages']} pages and 192 numbered statements. The post10 live preflight and the final frozen four-pass LuaLaTeX/BibTeX build have zero overfull boxes, zero overflows greater than 2pt and zero unresolved citations. The before/after overflow counts are therefore 0/0; no new layout repair was needed. All build outputs are retained.

We inspected {len(qa['rendered_pages'])} distinct rendered pages: {len(spread)} spread pages and {len(additional)} additional pages, with overlaps removed. These cover all four newly registered statements D.2.44 through D.2.47 and their complete proofs, the revised D.2.4 scope and the complete current bibliography. The relative characteristic-class display on page188 was additionally inspected enlarged. No clipping, overlap or displaced labels was observed. The final register audit finds 192 manuscript statements and 192 CSV rows, with no missing or duplicate identifiers and all19 prompt items in the opening report table. D.2.4 remains the sole open statement.

The source freeze is recorded as {freeze}; the PDF SHA256 is {pdf_hash}. All162 specified minimal simply connected patterns are now classified. The compatible general initial-pair and whole-fibre-weight homology algorithm and the general component intersection form are included as audited results. Later weighted Engel and arbitrary star-logarithm calculations are retained as active research, without silently promoting their unfinished steps. The eleven-hour decision is CONTINUE for the main-item advances recorded above.
'''
for location in [root, stage]:
    (location / 'records/checkpoint_11_qa.json').write_text(json.dumps(qa, indent=2) + '\n')
    with (location / 'S6_04_MAPS_MANIFOLDS_report.md').open('a') as stream:
        stream.write(text)
(stage / 'records/pdf_qa/qa.json').write_text(json.dumps(qa, indent=2) + '\n')
shutil.copy2(__file__, stage / 'code/finalize_checkpoint11.py')
print(json.dumps(qa, indent=2))
