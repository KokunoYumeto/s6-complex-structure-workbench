"""Record the completed mathematical, register, and visual audits for checkpoint08."""
from pathlib import Path
import json,shutil,datetime
root=Path(__file__).resolve().parents[1]
stage=root.parent/'checkpoint_build_08'/root.name
qa_path=stage/'records/pdf_qa/qa.json';qa=json.loads(qa_path.read_text())
extra_path=stage/'records/pdf_qa/checkpoint_08_extra_pages.json'
extra=json.loads(extra_path.read_text())
extra['repaired_line_pages']=[179,181,230,232]
extra_path.write_text(json.dumps(extra,indent=2)+'\n')
qa['rendered_pages']=sorted(set(qa['rendered_pages']+extra['extra_rendered_pages']))
qa['preliminary_fatal_error']='Two display-math closing delimiters were missing in F.2.36; both were restored before the frozen build.'
qa['preliminary_overflow_values_pt']=[12.01521,6.52959,72.9253]
qa['preliminary_max_overflow_pt']=72.9253
qa['repair']='Split the E.2.17 initial definition into two gathered rows, used breakable paths for the E.2.17 and F.2.33 program filenames, and restored the two F.2.36 display delimiters. Also gave F.2.37 unique equation tags.'
qa['visual_review']='Passed:22 spread contact-sheet pages and30 additional pages were inspected,51 distinct pages. The additional pages cover all11 new numbered statements and their complete proofs. Pages179,230,232 were also inspected enlarged. All repaired regions fit; no clipping, overlap, or displaced equation labels were observed.'
qa['reviewed_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
assert len(qa['rendered_pages'])==51
assert qa['pages']==253 and qa['overfull_boxes']==0 and not qa['unresolved_citations']
qa_path.write_text(json.dumps(qa,indent=2)+'\n')
paragraph='''\n\n## Checkpoint08 typesetting and consistency verification\n\nThe frozen manuscript has 253 pages and 169 numbered statements. The initial preflight found two missing display delimiters in F.2.36 and three overfull lines of 12.01521pt, 6.52959pt, and 72.9253pt. The delimiters were restored; the E.2.17 definition was split into two rows and the long program filenames were made breakable. The final four-pass LuaLaTeX/BibTeX build has zero overfull boxes and zero unresolved citations. We inspected 51 distinct rendered pages: 22 spread pages and 30 additional pages, covering all 11 new statements and their complete proofs, with one overlapping page. Pages 179, 230, and 232 were also inspected enlarged. No clipping or overlap was observed. The register audit found 169 manuscript statements and 169 CSV rows, with no missing or duplicate identifiers and all 19 prompt items in the opening report table.\n\nThe source freeze was 22:39:48 UTC on 15 November 2026. The global F.2.35 integration and D.2.31 smooth extension were still under final review at that instant; their source drafts are retained, but neither is included in the frozen theorem register or counted among its 169 statements. Later results belong to the working manuscript and the next scheduled checkpoint. The eight-hour progress decision is CONTINUE for the main-item advances recorded above.\n'''
for location in [root,stage]:
    (location/'records/checkpoint_08_qa.json').write_text(json.dumps(qa,indent=2)+'\n')
    with (location/'S6_04_MAPS_MANIFOLDS_report.md').open('a') as f:f.write(paragraph)
shutil.copy2(root/'code/checkpoint08_visual_pages.py',stage/'code/checkpoint08_visual_pages.py')
shutil.copy2(__file__,stage/'code/finalize_checkpoint08.py')
print(json.dumps(qa,indent=2))
