#!/usr/bin/env python3
"""Refresh outcome/QA records immediately before hourly checkpoint06."""
from pathlib import Path
import datetime,json,re,sys
import fitz

root=Path(__file__).resolve().parents[1]
tag=sys.argv[1] if len(sys.argv)>1 else 'draft23'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
audit=json.loads((root/'code'/f'deliverable_audit_{tag}.json').read_text())
assert audit['passed'],audit
build=json.loads((root/'build_logs'/f'{tag}_summary.json').read_text())
assert len(build)==4 and all(x['returncode']==0 and not x['overfull_pt'] for x in build)
qa=json.loads((root/'qa'/tag/'visual_inspection.json').read_text())
assert not qa['observed_issues'] and qa['visually_inspected_pages']
pages=len(fitz.open(root/'S6_02_PUSH_paper.pdf'))
assembly=json.loads((root/'code'/'assembly_summary.json').read_text())
assessment={
 'assessment_utc':now,'hour':6,'decision':'CONTINUE',
 'main_progress':[
  'B4.10 is an explicit proper parabolic Kato family with the marked normal correction proved.',
  'B4.11 and B4.12 globalize the specific elliptic-cone smoothing into a proper SNC surface family.',
  'B4.13 excludes the actual marked infinite-order period on finite modifications and nonzero-degree elliptic axes.',
  'B4.14 calculates exact tangent weights and reduces a compact-bundle obstruction without claiming the missing globalization.',
  'E2.9 removes the negative-slope horizontal fixed divisor; E2.10 proves smooth-limit pencil persistence and distinct-pair common-limit separation for both signs.',
  'An insertion directly on the prescribed rank-one torus germ at a regular base point is being checked in a separate working note.'
 ],
 'unresolved':[
  'The actual global S6 filling, the component-cover/cusp compatibility and the least semistable exponent.',
  'Topology and component-derived Chern numbers of the unconstructed analytic filling.',
  'Uniqueness of interior smooth completions and arbitrary deformation chains through unknown branches.'
 ],
 'reason':'The last hour closed a genuine open smooth-limit case and constructed new analytic pieces for Part B; current work is directly testing the prescribed torus germ, not only adding peripheral detail.'}
(root/'code'/'progress_assessment_06.json').write_text(json.dumps(assessment,indent=2)+'\n')
p=root/'code'/'refresh_report.py';s=p.read_text()
s=s.replace('| B.3 | B.3.1–B.3.8; B.4.1–B.4.6 |','| B.3 | B.3.1–B.3.8; B.4.1–B.4.14 |')
s=s.replace('| B.4 | B.4.1–B.4.9 |','| B.4 | B.4.1–B.4.14 |')
s=s.replace('A parabolic Kato alternative is under review.',
 'A proper parabolic Kato family and a proper quadric–parabolic SNC surface smoothing are constructed. The second marked period cannot act on a preserved elliptic axis of nonzero normal degree; compact global assembly and prescribed-family comparison remain open.')
s=s.replace('| E.2 | E.2.1–E.2.6 | Partial | Local deformation theory and irreducible-family separation are proved. Every smooth fixed-pair specialization has a holomorphic central pencil; positive canonical slope preserves the relative torus fibration and separates common smooth junctions. Arbitrary chains remain open. |',
 '| E.2 | E.2.1–E.2.10 | Partial, with one-sided smooth limits controlled for both signs | Local deformation theory and irreducible-family separation are proved. Every smooth fixed-pair specialization preserves its relative torus fibration and has an interior period limit; distinct ordered pairs cannot have a common smooth limit. The negative-slope horizontal fixed part is excluded by duality, generic twisting and Riemann–Roch. Interior completion uniqueness and arbitrary chains through new branches remain open. |')
s=s.replace('Draft19 is the current clean140-page paper','Draft19, included in checkpoint05, is a clean140-page paper')
needle='External copyrighted PDFs and private OCR extracts are not republished.'
paragraph=(f'{tag.capitalize()} is the current clean{pages}-page paper with{assembly["statements"]} registered statements and{assembly["bibliography_entries"]} bibliography entries. All four build stages succeeded with zero overfull boxes; the full integration audit passes without unresolved references, citations or rerun warnings. The rendered sample and its inspected pages are recorded in qa/{tag}/visual_inspection.json. Draft20 failed on a literal underscore in a bibliography URL; the corrected URL and successful intermediate draft21/22 logs are retained. The sixth-hour progress assessment is CONTINUE because the negative-slope smooth-limit obstruction was resolved and the main analytic-filling construction is still advancing. Checkpoint06 is scheduled for18:38:56 UTC.\n\n')
assert paragraph not in s
s=s.replace(needle,paragraph+needle)
s=s.replace('"root_E25_E26_referee.md","retention_record.md"',
 '"root_E25_E26_referee.md","root_sixth_hour_audit.md","D_sixth_hour_report.md","B_elliptic_contraction_sources.md","B_equivariant_compactification_attempt.md","D_E229_E2210_referee.md","retention_record.md"')
p.write_text(s)
print(json.dumps({'build':tag,'pages':pages,'statements':assembly['statements'],
 'references':assembly['bibliography_entries'],'assessment':assessment},indent=2))
