"""Record the completed visual and register audits of checkpoint04."""
from pathlib import Path
import json, shutil, datetime
root = Path(__file__).resolve().parents[1]
stage = root.parent/'checkpoint_build_04'/root.name
qa_path = stage/'records/pdf_qa/qa.json'
qa = json.loads(qa_path.read_text())
qa['rendered_pages'] = sorted(set(qa['rendered_pages']+[35,43,88,93,135,136,137]))
qa['preliminary_overfull_boxes'] = 1
qa['preliminary_overflows_over_2pt'] = 1
qa['preliminary_max_overflow_pt'] = 9.46272
qa['repair'] = 'Separated the program-reference paragraph in the B.6.10 proof; the repaired line appears on page35.'
qa['visual_review'] = 'Passed: all22 contact-sheet pages inspected, with seven enlarged pages35,43,88,93,135,136,137 also inspected;28 distinct pages in total. No clipping or overlap. The repaired line on page35 is within the text block.'
qa['reviewed_utc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
qa_path.write_text(json.dumps(qa, indent=2)+'\n')
for location in [root,stage]:
    (location/'records/checkpoint_04_qa.json').write_text(json.dumps(qa, indent=2)+'\n')
    audit = location/'records/root_audit_checkpoint04_progress.json'
    a = json.loads(audit.read_text())
    a['statements']['B.6.15'] = 'Passed: Wang and Gysin sequences, spin mapping-torus structure, twisted Dirac congruence ell=4k mod24, Thom intersection form and all spin-c characteristic coefficients independently derived. Exact program independently rerun. This is conditional and makes no claim about the actual fixed-curve framing, k, ell or surgery correction.'
    audit.write_text(json.dumps(a, indent=2)+'\n')
    report = location/'S6_04_MAPS_MANIFOLDS_report.md'
    with report.open('a') as f:
        f.write('\n\n## Checkpoint04 typesetting and consistency verification\n\nThe frozen manuscript has143 pages and115 numbered statements. The preliminary build had one overfull line at9.46272pt. Separating the B.6.10 program-reference paragraph repaired it; the final four-pass LuaLaTeX/BibTeX build has zero overfull boxes and zero unresolved citations. We inspected28 distinct rendered pages spread across the manuscript, including enlarged pages35,43,88,93,135,136 and137; the repaired line is on page35. No clipping or overlap was observed. The register audit finds115 manuscript statements,115 CSV rows, no missing or duplicate IDs, and all19 prompt items in the opening report table. The audit was corrected to count statement headings rather than cross-references within a scope heading.\n')
shutil.copy2(root/'records/root_free_circle_audit.out',stage/'records/root_free_circle_audit.out')
shutil.copy2(__file__,stage/'code/finalize_checkpoint04.py')
print(json.dumps(qa, indent=2))
