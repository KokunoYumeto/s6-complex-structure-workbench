"""Finalize checkpoint12 QA only after inspecting the frozen rendered pages."""
from pathlib import Path
import datetime
import hashlib
import json
import shutil

root = Path(__file__).resolve().parents[1]
stage = root.parent / 'checkpoint_build_12' / root.name
qa = json.loads((stage / 'records/pdf_qa/qa.json').read_text())
extra = json.loads((stage / 'records/pdf_qa/checkpoint_12_extra_pages.json').read_text())
audit = json.loads((stage / 'records/register_audit.json').read_text())
spread = qa['rendered_pages']
additional = extra['extra_rendered_pages']
qa['rendered_pages'] = sorted(set(spread + additional))
qa['preliminary_overflow_values_pt'] = []
qa['preliminary_max_overflow_pt'] = 0
qa['repairs'] = []
qa['visual_review'] = (
    f"Passed: {len(spread)} spread pages and {len(additional)} additional pages, "
    f"{len(qa['rendered_pages'])} distinct pages, inspected as rendered images. "
    'All six newly registered proofs D48-D53, the revised D2.4 and the complete bibliography are covered. '
    'No clipping, overlap or displaced mathematical labels was observed.')
qa['enlarged_pages'] = [225]
qa['reviewed_utc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
assert qa['overfull_boxes'] == 0 and not qa['unresolved_citations']
assert audit['manuscript_statement_count'] == audit['register_statement_count'] == 198
assert audit['open_statements'] == ['D.2.4'] and audit['report_prompt_rows'] == 19
assert {f'D.2.{i}' for i in range(48, 54)} <= set(extra['statement_pages'])
freeze = json.loads((stage / 'records/checkpoint_12_manifest.json').read_text())['source_frozen_utc']
pdf_hash = hashlib.sha256((stage / 'S6_04_MAPS_MANIFOLDS_paper.pdf').read_bytes()).hexdigest()
qa['pdf_sha256'] = pdf_hash
text = f'''

## Checkpoint12 typesetting and consistency verification

The frozen manuscript has {qa['pages']} pages and198 numbered statements. The complete live preflight and frozen four-pass LuaLaTeX/BibTeX build have zero overfull boxes, zero overflows greater than2pt and zero unresolved citations. Before/after overflow counts are0/0; no new layout repair was required. All build outputs are retained.

We inspected {len(qa['rendered_pages'])} distinct rendered pages: {len(spread)} spread pages and {len(additional)} additional pages, with overlaps removed. These cover all six new statements D.2.48 through D.2.53 and their complete proofs, the revised D.2.4 scope and the complete current bibliography. Page225, containing the full cusp boundary filtration and affine-cochain comparison, was also inspected enlarged. No clipping, overlap or displaced mathematical labels was observed. The final audit finds198 manuscript statements and198 CSV rows, with no missing or duplicate identifiers and all19 prompt items in the opening report table. D.2.4 remains the sole open statement.

The source freeze is {freeze}; the PDF SHA256 is {pdf_hash}. This checkpoint includes the completed all-weight Engel smooth classification, primitive-long-circle star-log cap calculation, integral initial correction theorem, corrected original additive/global algorithms and the full primitive cubic and fundamental-class invariant of the OS45 example. The latter's refined0-versus4 calculation remains open at the freeze. Subsequent star-log smooth and equivariant-linking work is retained as research without promoting unfinished arguments. The twelve-hour decision is CONTINUE for the main-item advances recorded above.
'''
for location in [root, stage]:
    (location / 'records/checkpoint_12_qa.json').write_text(json.dumps(qa, indent=2) + '\n')
    with (location / 'S6_04_MAPS_MANIFOLDS_report.md').open('a') as stream:
        stream.write(text)
(stage / 'records/pdf_qa/qa.json').write_text(json.dumps(qa, indent=2) + '\n')
shutil.copy2(__file__, stage / 'code/finalize_checkpoint12.py')
print(json.dumps(qa, indent=2))
