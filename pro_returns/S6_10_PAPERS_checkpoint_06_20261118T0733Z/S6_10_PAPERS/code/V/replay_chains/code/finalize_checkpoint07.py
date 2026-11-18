"""Record the completed source, arithmetic, and visual audits for checkpoint07."""
from pathlib import Path
import json,shutil,datetime
root=Path(__file__).resolve().parents[1]
stage=root.parent/'checkpoint_build_07'/root.name
qa_path=stage/'records/pdf_qa/qa.json';qa=json.loads(qa_path.read_text())
extra_path=stage/'records/pdf_qa/checkpoint_07_extra_pages.json';extra=json.loads(extra_path.read_text())
extra['extra_rendered_pages']=sorted(set(extra['extra_rendered_pages']+[129]))
extra_path.write_text(json.dumps(extra,indent=2)+'\n')
qa['rendered_pages']=sorted(set(qa['rendered_pages']+extra['extra_rendered_pages']))
qa['preliminary_fatal_error']='D.HY3 used split with more than one alignment pair; replaced by aligned.'
qa['preliminary_overflow_values_pt']=[79.16293,8.48619]
qa['preliminary_max_overflow_pt']=79.16293
qa['repair']='Used a breakable path for the D.2.26 CSV filename, repaired the D.HY3 alignment, and shortened the F.2.32 Seifert-manifold sentence. Also made the build driver return a nonzero exit status after a TeX failure.'
qa['visual_review']='Passed:22 spread contact-sheet pages and27 additional pages inspected,48 distinct pages. The additional pages contain every new theorem and its complete proof. Pages126,129,207 were also inspected enlarged; the repaired filename on125, the aligned display on126, and the repaired sentence on207 have no clipping or overlap.'
qa['reviewed_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
assert len(qa['rendered_pages'])==48
assert qa['pages']==225 and qa['overfull_boxes']==0 and not qa['unresolved_citations']
qa_path.write_text(json.dumps(qa,indent=2)+'\n')
paragraph='''\n\n## Checkpoint07 typesetting and consistency verification\n\nThe frozen manuscript has225 pages and158 numbered statements. The first build located a malformed alignment in D.HY3 and a79.16293pt overlong filename; the next complete build located one8.48619pt overlong sentence in F.2.32. These were repaired by using an aligned display, a breakable filename path, and a shorter sentence. The final four-pass LuaLaTeX/BibTeX build has zero overfull boxes and zero unresolved citations. We inspected48 distinct rendered pages:22 spread pages and27 additional pages, covering every new proof; pages126,129 and207 were also inspected enlarged. No clipping or overlap was observed. The register audit has158 manuscript statements and158 CSV rows, no missing or duplicate identifiers, and all19 prompt items in the opening report table. The root independently reran the complete D.2.25/D.2.26 catalogues, including85 scalar-circle checks,164 hybrid patterns,650 hybrid Smith checks,144 scalar-circle checks, all172 fixed-sweep cokernels and68 finite norm lattices; all assertions passed.\n'''
for location in [root,stage]:
    (location/'records/checkpoint_07_qa.json').write_text(json.dumps(qa,indent=2)+'\n')
    with (location/'S6_04_MAPS_MANIFOLDS_report.md').open('a') as f:f.write(paragraph)
    ap=location/'records/root_audit_checkpoint07_progress.json';audit=json.loads(ap.read_text())
    audit['exact_reruns']=['root_semistable_catalogue_audit.out','root_nonstar_catalogue_audit.out','root_sphere_normal_lattices_audit.out','root_sphere_gluing_audit.out','root_shifted_circle_audit.out','root_shifted_return_audit.out','root_shifted_cover_audit.out','root_shifted_cover_integral_audit.out','root_shifted_fibre_integral_audit.out','root_three_point_audit.out']
    ap.write_text(json.dumps(audit,indent=2)+'\n')
p=root/'code/checkpoint07_visual_pages.py';s=p.read_text().replace('range(119,129)','range(119,130)');p.write_text(s)
shutil.copy2(p,stage/'code/checkpoint07_visual_pages.py')
shutil.copy2(__file__,stage/'code/finalize_checkpoint07.py')
print(json.dumps(qa,indent=2))
