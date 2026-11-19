"""Record the completed visual and register audits of checkpoint 05."""
from pathlib import Path
import json, shutil, datetime

root = Path(__file__).resolve().parents[1]
stage = root.parent/'checkpoint_build_05'/root.name
qa_path = stage/'records/pdf_qa/qa.json'
qa = json.loads(qa_path.read_text())
extra = [46,50,51,54,106,128,151,155,157,158]
qa['rendered_pages'] = sorted(set(qa['rendered_pages']+extra))
qa['preliminary_overfull_boxes'] = 1
qa['preliminary_overflows_over_2pt'] = 1
qa['preliminary_max_overflow_pt'] = 10.4135
qa['repair'] = 'Split the characteristic-polynomial and nilpotent-operator displays in the opening of F.2.20. The repaired statement is on page 151 of the frozen manuscript.'
qa['visual_review'] = 'Passed: all 21 contact-sheet pages inspected, with enlarged pages 46,50,51,54,106,128,151,155,157,158 also inspected; 31 distinct pages in total. No clipping or overlap. The repaired F.2.20 opening display fits within the text block.'
qa['reviewed_utc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
qa_path.write_text(json.dumps(qa, indent=2)+'\n')
paragraph = '''\n\n## Checkpoint 05 typesetting and consistency verification

The frozen manuscript has 173 pages and 133 numbered statements. The preliminary build had one overfull display at 10.4135pt. Splitting the characteristic-polynomial and nilpotent-operator displays in F.2.20 repaired it; the final four-pass LuaLaTeX/BibTeX build has zero overfull boxes and zero unresolved citations. We inspected 31 distinct rendered pages spread across the manuscript, including enlarged pages 46, 50, 51, 54, 106, 128, 151, 155, 157 and 158. The repaired opening display is on page 151. No clipping or overlap was observed. The register audit finds 133 manuscript statements, 133 CSV rows, no missing or duplicate IDs, and all 19 prompt items in the opening report table.
'''
for location in [root,stage]:
    (location/'records/checkpoint_05_qa.json').write_text(json.dumps(qa, indent=2)+'\n')
    report = location/'S6_04_MAPS_MANIFOLDS_report.md'
    with report.open('a') as f:
        f.write(paragraph)
shutil.copy2(__file__,stage/'code/finalize_checkpoint05.py')
print(json.dumps(qa, indent=2))
