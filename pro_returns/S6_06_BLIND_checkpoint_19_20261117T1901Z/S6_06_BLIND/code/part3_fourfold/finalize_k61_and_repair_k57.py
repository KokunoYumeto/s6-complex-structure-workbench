#!/usr/bin/env python3
"""Record K61 visual QA and retain K57's narrow audited C2 scalar comparison."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil

ROOT=Path(__file__).resolve().parents[2]
now=datetime.now(timezone.utc).isoformat()
with (ROOT/'records/literature_fourfold.md').open('a') as f:
    f.write('\n- '+now+' — Opened K61 final page images 1–3, qa_k61.json, and the K57 infinity excision source. Reason: direct final layout verification and audited K62 dependency repair. Material: all three K61 pages, their actual outer determinant obstruction, and IE.6 initial/reflected fan scope.\n')
p=ROOT/'records/qa_k61.json';r=json.loads(p.read_text())
assert r['compile']=='PASS' and r['pages']==3 and not r['overflows_pt']
assert not r['boundary_issues'] and not r['missing_character'] and not r['undefined_reference']
r.update(visual_review='PASS',visual_review_utc=now,reviewer='fourfold',
 page_count_reviewed=3,full_size_pages=[1,2,3],
 findings=['All three final pages directly reviewed at full size.',
 'No clipping, equation collision, malformed matrix, missing symbol, orphan heading, or bad page boundary found.',
 'The actual degree-M closed atlas, full outer determinant map, and arbitrary-equivariant-normal-derivative obstruction are retained.',
 'No corrected global residue or all-fan invariant is assigned.'],
 pdf_sha256=hashlib.sha256((ROOT/'code/part3_fourfold/k61_standalone.pdf').read_bytes()).hexdigest(),
 source_sha256=hashlib.sha256((ROOT/'notes/part3_scalar_outer_clutch_audit.md').read_bytes()).hexdigest(),
 exact_certificate='code/part3_fourfold/scalar_outer_clutch_certificate.json')
p.write_text(json.dumps(r,indent=2)+'\n')
(ROOT/'records/k61_standalone_visual_qa.json').write_text(json.dumps(r,indent=2)+'\n')

archive=ROOT/'records/k57_pre_k62_dependency';archive.mkdir(exist_ok=True)
for name in ['notes/part3_source_infinity_excision_working.md',
             'notes/part3_source_infinity_return.tex',
             'notes/part3_source_infinity_return.md',
             'code/part3_fourfold/k57_standalone.pdf',
             'records/qa_k57.json','records/k57_standalone_visual_qa.json']:
    src=ROOT/name;dest=archive/src.name
    if not dest.exists(): shutil.copy2(src,dest)
p=ROOT/'notes/part3_source_infinity_excision_working.md'
s=p.read_text()
needle='with a further flopped fan is used here.\n'
addition=r'''
The fixed-source scalar integers in these two particular markings
are equal by the actual C2 comparison of P3K.62. Its first outer
branch map is the identity; its second has base multiplier
\(\kappa^{-1}\) and normal matrix
\(\operatorname{diag}(\alpha^{-1},\kappa\alpha)\), both independent
of the scalar parameter. These are exactly the outer maps used
on the selected collar here. Together with the equal inner
charged-cap gauges, they give the line-preserving integer
comparison in P3K.62. This invocation retains the two outer
maps and uses no assertion of equality for a further fan.
'''
assert needle in s and 'The fixed-source scalar integers in these two particular markings' not in s
s=s.replace(needle,needle+addition,1)
p.write_text(s)
record=dict(utc=now,statement='P3K.57',previous_versions=str(archive.relative_to(ROOT)),
 correction='Replace the implicit initial/reflected scalar-equality dependency by the proved narrow P3K.62 C2 outer/inner cochain comparison.',
 explicit_k25_citation_before=False,scope_unchanged=True,
 maps=['first outer branch identity','second base kappa^-1; normal diag(alpha^-1,kappa alpha)','equal inner charged-cap gauges'],
 peer_audit='fourfold independently passed SCN.8–9; root passed complete SCN.1–9')
(ROOT/'records/k57_k62_dependency_repair.json').write_text(json.dumps(record,indent=2)+'\n')
print('K61 visual QA PASS; K57 source repaired with preserved previous versions.')
