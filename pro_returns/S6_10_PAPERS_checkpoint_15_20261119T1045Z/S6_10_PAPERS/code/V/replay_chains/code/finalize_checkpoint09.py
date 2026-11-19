"""Record completed mathematical, register, and visual audits for checkpoint09."""
from pathlib import Path
import json, shutil, datetime

root = Path(__file__).resolve().parents[1]
stage = root.parent / 'checkpoint_build_09' / root.name
qa_path = stage / 'records/pdf_qa/qa.json'
qa = json.loads(qa_path.read_text())
extra = json.loads((stage / 'records/pdf_qa/checkpoint_09_extra_pages.json').read_text())
qa['rendered_pages'] = sorted(set(qa['rendered_pages'] + extra['extra_rendered_pages']))
qa['preliminary_overflow_values_pt'] = [1.89905, 9.77196]
qa['preliminary_max_overflow_pt'] = 9.77196
qa['repair'] = 'Made four long F.2.35 program filenames breakable paths. The visual-page helper was also corrected to recognize the resolved F.2.4 Conclusion heading; its first failed lookup is retained.'
qa['visual_review'] = ('Passed:22 spread pages and49 additional pages were inspected,69 distinct pages after two overlaps. '
                       'They cover all nine newly registered statements and their complete proofs, the three changed scope conclusions, '
                       'and F.2.37. Pages158,259,266 were additionally inspected enlarged. No clipping, overlap, or displaced labels was observed.')
qa['enlarged_pages'] = [158, 259, 266]
qa['reviewed_utc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
assert len(qa['rendered_pages']) == 69
assert qa['pages'] == 283 and qa['overfull_boxes'] == 0 and not qa['unresolved_citations']
qa_path.write_text(json.dumps(qa, indent=2) + '\n')
paragraph = '''

## Checkpoint09 typesetting and consistency verification

The frozen manuscript has 283 pages and 178 numbered statements. The initial preflight found two overfull lines of 1.89905pt and 9.77196pt. Four long program filenames in F.2.35 were made breakable. The final four-pass LuaLaTeX/BibTeX build has zero overfull boxes and zero unresolved citations. We inspected 69 distinct rendered pages: 22 spread pages and 49 additional pages, with two overlapping pages. These cover all nine newly registered statements and their complete proofs, the updated D.2.4, E.2.4, and F.2.4 conclusions, and F.2.37; pages 158, 259, and 266 were also inspected enlarged. No clipping, overlap, or displaced labels was observed. The visual-page extraction helper initially missed the resolved Conclusion heading of F.2.4; its heading expression was corrected and the failed output is preserved. This was a page-selection error, not a LaTeX build error. The register audit found 178 manuscript statements and 178 CSV rows, with no missing or duplicate identifiers and all 19 prompt items in the opening report table.

The source freeze was 23:38:17 UTC on 15 November 2026. D.2.37 and E.2.19 were still source-only drafts at that instant, and the mixed 10/14-torsion work was a local certificate, not a registered smooth classification theorem. None is included in the frozen count. Later results belong to the working manuscript and the next scheduled checkpoint. F.2 is complete; D.2 and E.2 remain open. The nine-hour progress decision is CONTINUE for the main-item advances recorded above.
'''
for location in [root, stage]:
    (location / 'records/checkpoint_09_qa.json').write_text(json.dumps(qa, indent=2) + '\n')
    with (location / 'S6_04_MAPS_MANIFOLDS_report.md').open('a') as f:
        f.write(paragraph)
shutil.copy2(root / 'code/checkpoint09_visual_pages.py', stage / 'code/checkpoint09_visual_pages.py')
shutil.copy2(__file__, stage / 'code/finalize_checkpoint09.py')
print(json.dumps(qa, indent=2))
