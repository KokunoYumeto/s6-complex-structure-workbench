#!/usr/bin/env python3
"""Record the seventh-hour assessment and the inspected build before packaging."""
from pathlib import Path
import csv,datetime,json,re,sys
import fitz

root=Path(__file__).resolve().parents[1]
tag=sys.argv[1]
audit=json.loads((root/'code'/f'deliverable_audit_{tag}.json').read_text())
assert audit['passed']
qa=json.loads((root/'qa'/tag/'visual_inspection.json').read_text())
assert not qa['observed_issues']
pages=len(fitz.open(root/'S6_02_PUSH_paper.pdf'))
rows=list(csv.DictReader((root/'S6_02_PUSH_results.csv').open()))
assert len(rows)==audit['registry_rows']
record={
 'assessment_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'hour':7,'decision':'CONTINUE',
 'main_progress':[
  'B4.15 constructs non-Kahler vertical components directly on the prescribed regular torus germ; B4.16 proves the precise remaining dual-cycle obstruction.',
  'B4.18 constructs the corrected actual cusp family over the bidisc minus its origin, with an explicit affine comparison and the required component rotation.',
  'E2.11--15 prove good-Jacobian purity, absence of extra critical values, persistence of finite root charts, and exclusion of every collision of the labelled critical values.',
  'E2.16--18 prove that the remaining cusp is reduced and irreducible, remains relative normal crossings, and has the prescribed normalized dP6 hexagon.',
  'E2.19 extends the actual marked two-dimensional torus action over the whole cusp bidisc; a full working reconstruction of its analytic toric cover is undergoing independent review.'
 ],
 'unresolved':[
  'Proper analytic completion at the missing origin of the corrected cusp, global S6 filling, descent and least semistable exponent.',
  'Topology and component-derived Chern numbers of that unconstructed analytic filling.',
  'Final analytic cusp-completion identification and the consequence for arbitrary deformation chains; the reconstruction working proof is not yet promoted.'
 ],
 'reason':'The seventh hour resolved several main smooth-limit obstructions and reduced the actual local filling problem to one base point. Work is advancing the requested existence and deformation-class questions.'
}
(root/'code'/'progress_assessment_07.json').write_text(json.dumps(record,indent=2)+'\n')

p=root/'code'/'refresh_report.py'
s=p.read_text()
s=s.replace('B.4.1–B.4.14','B.4.1–B.4.18')
s=s.replace('E.2.1–E.2.10 | Partial, with one-sided smooth limits controlled for both signs | Local deformation theory and irreducible-family separation are proved. Every smooth fixed-pair specialization preserves its relative torus fibration and has an interior period limit; distinct ordered pairs cannot have a common smooth limit. The negative-slope horizontal fixed part is excluded by duality, generic twisting and Riemann–Roch. Interior completion uniqueness and arbitrary chains through new branches remain open.',
'''E.2.1–E.2.19 | Partial, with the actual cusp geometry now controlled | Every smooth fixed-pair specialization preserves its relative torus fibration and interior period. Its three critical values stay distinct; finite multiplicities persist. The cusp is reduced and irreducible, remains relative normal crossings, has normalized toric dP6 with its marked hexagon, and carries the extended marked two-dimensional torus action. Distinct ordered pairs cannot have a common smooth limit. Full analytic cusp identification and arbitrary deformation chains remain open pending the reconstruction proof.''')
s=s.replace('The second marked period cannot act on a preserved elliptic axis of nonzero normal degree; compact global assembly and prescribed-family comparison remain open.',
'''The second marked period cannot act on a preserved elliptic axis of nonzero normal degree. Actual regular-place Hopf insertions exist, with a computed unchanged dual-cycle homotopy. The corrected cusp now exists over the bidisc minus its origin, with the prescribed reduced q-boundary and required r-component rotation. A proper completion at that origin and compact global assembly remain open.''')
s=s.replace('Corrected cusp and global filling still required; auxiliary constructions and obstructions are specified.',
'''The corrected cusp is constructed over the punctured bidisc. Its proper origin completion and global filling remain open; auxiliary constructions and obstructions are specified.''')
s=s.replace('"root_sixth_hour_audit.md",',
'''"root_sixth_hour_audit.md","root_seventh_hour_audit.md","E_E211_referee.md","D_E2211_E2212_referee.md","D_E2213_E2214_referee.md","E_E215_referee.md","D_E2216_referee.md","D_E2217_referee.md","D_corrected_cusp_overlap_referee.md","D_cusp_origin_attempts.md",''')
build=(f'\n\nThe seventh-hour checkpoint build is {tag}: {pages} pages, {len(rows)} statement rows and '
       f'{audit["bibliography_entries"]} bibliography entries. All four compiler stages succeeded with zero overfull boxes; '
       f'the final integration audit passes without unresolved references, citations or rerun warnings. '
       f'{len(qa["visually_inspected_pages"])} distinct pages were rendered and visually inspected, including the seventh-hour proofs. '
       f'The exact record is qa/{tag}/visual_inspection.json. The seventh-hour assessment is CONTINUE. '
       'Checkpoint07 is scheduled for 19:38:56 UTC; it is not created earlier.\n\n')
s=s.replace('External copyrighted PDFs and private OCR extracts are not republished.',build+'External copyrighted PDFs and private OCR extracts are not republished.')
s=s.replace('Draft23 is the current clean159-page paper','Draft23 was the clean159-page paper at checkpoint06')
p.write_text(s)
p=root/'sections'/'root_seventh_hour_audit.md'
s=p.read_text()
s+='\n\n## Completed integrations before checkpoint07\n\n'
s+=('E.2.16 and E.2.17 were fully reviewed by root, classification_e and boundary_d and integrated. '
     'E.2.18 identifies the normalized central pair by three analytic minus-one contractions and the compact-surface classification, '
     'and gives a global relative logarithmic frame by Grauert evaluation. '
     'E.2.19 descends that frame across the conductor, extends it over the full cusp bidisc, '
     'and constructs the marked holomorphic (C*)² action. Root checked its full proof, including the primitive period lattice. '
     'The full E.2.20 reconstruction working proof remains a separately marked candidate; it is not counted as a proved statement.\n\n')
s+=build.strip()+'\n'
p.write_text(s)
print(json.dumps({'build':tag,'pages':pages,'rows':len(rows),'references':audit['bibliography_entries'],
                  'visual_pages':len(qa['visually_inspected_pages']),'assessment':record},indent=2))
