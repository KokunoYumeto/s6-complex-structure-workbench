"""Record the completed source, arithmetic, and visual audits for checkpoint06."""
from pathlib import Path
import json, shutil, datetime

root=Path(__file__).resolve().parents[1]
stage=root.parent/'checkpoint_build_06'/root.name
qa_path=stage/'records/pdf_qa/qa.json'
qa=json.loads(qa_path.read_text())
extra_path=stage/'records/pdf_qa/checkpoint_06_extra_pages.json'
extra=json.loads(extra_path.read_text())
extra['extra_rendered_pages']=sorted(set(extra['extra_rendered_pages']+[119]))
extra_path.write_text(json.dumps(extra,indent=2)+'\n')
qa['rendered_pages']=sorted(set(qa['rendered_pages']+extra['extra_rendered_pages']))
qa['preliminary_overfull_boxes']=2
qa['preliminary_overflows_over_2pt']=2
qa['preliminary_overflow_values_pt']=[70.98384,3.38715]
qa['preliminary_max_overflow_pt']=70.98384
qa['repair']='Separated the long program-reference sentences in B.6.23 and F.2.26. The repaired lines are on pages56 and179 of the frozen manuscript. The final frozen build also assembles the newly added bibliography before its four passes.'
qa['visual_review']='Passed: all22 spread contact-sheet pages and21 extra pages inspected, for41 distinct pages. The extra pages cover every new theorem opening, the full D.2.22 initial-data reduction and table, the F.2.30 synthesis, and both repaired lines. Pages56,119,179 were also inspected enlarged. No clipping, overlapping type, or overflowing displays were observed.'
qa['reviewed_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
assert len(qa['rendered_pages'])==41
assert qa['pages']==202 and qa['overfull_boxes']==0 and not qa['unresolved_citations']
qa_path.write_text(json.dumps(qa,indent=2)+'\n')

paragraph='''\n\n## Checkpoint06 typesetting and consistency verification\n\nThe frozen manuscript has202 pages and149 numbered statements. The preliminary build had two overfull lines, measuring70.98384pt and3.38715pt. Separating the program-reference sentences in B.6.23 and F.2.26 repaired them; the corresponding final pages are56 and179. The final four-pass LuaLaTeX/BibTeX build has zero overfull boxes and zero unresolved citations. We inspected41 distinct rendered pages:22 spread pages and21 additional pages, including the new statements, the complete D.2.22 reduction and table, and the F.2.30 classification. Pages56,119 and179 were also inspected enlarged. No clipping or overlap was observed. The register audit finds149 manuscript statements,149 CSV rows, no missing or duplicate identifiers, and all19 prompt items in the opening report table. The final frozen D.2.22 program was independently rerun, including both exact catalogues and the symbolic invariant-form identity; all assertions passed.\n'''
for location in [root,stage]:
    (location/'records/checkpoint_06_qa.json').write_text(json.dumps(qa,indent=2)+'\n')
    with (location/'S6_04_MAPS_MANIFOLDS_report.md').open('a') as f:f.write(paragraph)
    ap=location/'records/root_audit_checkpoint06_progress.json'
    audit=json.loads(ap.read_text())
    name='root_sphere_initial_final_audit.out'
    if name not in audit['exact_reruns']:audit['exact_reruns'].append(name)
    ap.write_text(json.dumps(audit,indent=2)+'\n')
shutil.copy2(stage/'records/root_sphere_initial_final_audit.out',root/'records/root_sphere_initial_final_audit.out')
shutil.copy2(root/'code/checkpoint06_visual_pages.py',stage/'code/checkpoint06_visual_pages.py')
shutil.copy2(__file__,stage/'code/finalize_checkpoint06.py')
print(json.dumps(qa,indent=2))
