#!/usr/bin/env python3
"""Record completed K119 audit, exact source patches and scoped row assessment."""
from pathlib import Path
import json, csv, hashlib

root=Path(__file__).resolve().parents[1]
source=Path('/workspace/scratch/6c4e6df38b6d/S6_SERIES_GRIND_source/S6_GRIND_1_papers_cp15/S6_10_PAPERS_IV.tex')
body=source.read_text()
patches=[]
def add(suffix,old,new,reason):
    assert body.count(old)==1, (suffix,body.count(old))
    patches.append(dict(id='IV-K119-'+suffix,statement_id='night:P3K.119',
                        operation='replace_exact',old=old,new=new,reason=reason))
add('fixed-family',r'''lattice-basis selected fan, and an original admitted fixed nonzero
scalar \(\lambda\).

On the original ordered selected-source cover''',r'''lattice-basis selected fan, and an original admitted fixed nonzero
scalar \(\lambda\).
The lifted family is the fixed-$C_*$ continuation of
\cref{night:P3K.116}:
\[
 B_\lambda(p,v_M)=
 \bigl(p-G,\lambda C_*(t-t_c)B_{8,1}(p)v_M\bigr),
 \qquad B_{8,1}=f_2^8\frac{f_8\circ t_{-G}}{f_8}.
\]
The chronological tangent quotients and the single nonzero $C_*$
are fixed by the prescribed initial source and Cartier frames.

On the original ordered selected-source cover''',
'Make the actual fixed Hom normalization and its exact family map explicit, as used by ORC.12; do not infer extension of an independently varying lift.')
add('proof-roadmap',r'''\emph{Completed proof and retained preparation history.} The original opening and OC45.1-\/-5 retain the local-stage scope; OC45.6-\/-11 supplies the full original-reference comparison and all twenty-four points. The original closing preparation-stage audit notice is reproduced verbatim. The complete OCP, OCGC and ORC supporting proofs follow below. Their completed geometric audits, exact certificates and source locks are recorded in \path{records/k119_export_manifest.json}.''',r'''\emph{Proof roadmap.}
OC45.1-\/-5 constructs the local enlargement for the eighteen
unselected-cap points and its specified extending period.
OC45.6-\/-11 constructs the full original-reference comparison
and treats all twenty-four points. OCP gives the integral
based-cell maps and their contraction, OCGC gives the global
source/line and endpoint comparison, and ORC records the full
source, proper-family and return argument.''',
'Replace preparation-history prose inside the proof by the actual logical scope of its four complete parts; preserve historical records separately.')
add('current-proof-state',r'''All previous local-stage bytes and the PASS64
certificate are preserved under
\path{records/attempts/os45_cap_before_global_reference/}.
The full proof remains a working manuscript until
the independent global source/line/cochain and
endpoint audits are recorded.''',r'''The integral contraction, full Lie-cochain solution,
source/line extension and directed endpoint square above
establish the asserted original-reference return.
The remaining supporting proofs give the complete
based-cell, global-comparison and proper-family calculations.''',
'The current complete audit and fresh exact calculation close the former global-reference gate; historical preparation status remains in the event record.')
(root/'K119_patches.json').write_text(json.dumps(patches,indent=2)+'\n')

assessment_path=root.parent/'row_assessments.json'
rows=json.loads(assessment_path.read_text())
rows['night:P3K.119']={
 'confidence_state':'proved; high confidence at the complete stated fixed-C_* scope',
 'confidence_line':'All twenty-four ordinary-cap meridians and their reciprocals have zero return for the original positive norm-one cap, complete prescribed reference, all prescribed integral basis fans and every original admitted fixed scalar. Complete source/Cartier/integral/Lie/properness/endpoint review and fresh exact reconstruction close the prior original-reference gate.',
 'independent_routes':[
   'Statement-first frozen source algebra: original selected cover, collision factorization and disjointness, exact moving-node and inverse-Tate leading coefficient; no claim that prereading alone proves the global cap comparison.',
   'Complete post-reading geometric audit of OC45.1–11, OCP.1–6, OCGC.1–4 and ORC.1–10, including K78 invariant-stalk calculation and previously audited literal K10/K116/F35 sphere and fan morphisms.',
   'Fresh independent code after proof reading: 175 exact checks, all twenty inverse-transpose matrices for four selected sites, complete 20-by-20 raw/based maps and integral inverses, 20-by-36 cone signs, primitive D/B image matrices and D′L+JB′=I6 contraction, chronological Miller and original-height node identities, full Laurent off-diagonal algebra and noncommutative endpoint order.'
 ],
 'remaining_risk':'No remaining mathematical gate identified at the stated scope. Keeps established reference-sphere/fan dependencies and fixed Hom normalization. Same-family review; no full-priority claim or historical executable replay. Layout and package validation remain with root.',
 'format_check':'Exact statement insertion makes fixed C_* continuation explicit. Proof-roadmap and obsolete preparation-stage status replacements supplied in K119_patches.json. Theorem status can be proved; no layout/completion status asserted.'
}
assessment_path.write_text(json.dumps(rows,indent=2)+'\n')
event_path=root/'events.tsv'
with event_path.open(newline='') as f:
    reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;events=list(reader)
who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort; same model family'
new_events=[
 ('IV-K119-prereading','independent re-proof','Statement-first frozen original source, ordered marked cover, collision factorization/disjointness, moving-node coefficient and original-height inverse-Tate checks. Full global reference comparison was outside prereading scope.'),
 ('IV-K119-complete-proof','targeted proof check','All four complete OC45/OCP/OCGC/ORC arguments read and checked, with actual source and Cartier inverses, invariant period stalks, integral cone signs, full off-diagonal Lie solve, both parameter jumps, physical endpoint conjugacy and proper protected-cap disc. The full stated fixed-C_* original-reference gate is closed.'),
 ('IV-K119-fresh-code','computation or formal certificate','Fresh post-reading 175-check program reconstructs all original source/node/Miller and four selected-site integral comparison matrices. Complete 20-by-20 inverse coordinate maps, 20-by-36 cone, primitive D/B contraction, full Laurent algebra and noncommutative endpoint order PASS; no original unavailable program replay claimed.'),
 ('IV-K119-source-scope','targeted proof check','K10/K116 literal source and reference-sphere maps, F35/O45P.6 fan transport and K78 OCS.1 local invariant-stalk argument read at their used scopes. Preserves primary-source and historical input credit; no broader novelty or priority claim.')]
existing={e['event_id'] for e in events}
for eid,kind,outcome in new_events:
    if eid not in existing:
        events.append(dict(statement_id='night:P3K.119',date='2026-11-19',who=who,type=kind,outcome=outcome,event_id=eid,phase='S6_SERIES_GRIND'))
with event_path.open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t');writer.writeheader();writer.writerows(events)

def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
receipt={
 'status':'PASS','mathematical_conclusion':'proved at complete stated fixed-C_* scope; high confidence',
 'patch_exact_unique_matches':len(patches),
 'check_count':json.loads((root/'output/k119_afterreading_exact.json').read_text())['check_count'],
 'program':'code/k119_afterreading_exact.py','program_sha256':digest(root/'code/k119_afterreading_exact.py'),
 'output':'output/k119_afterreading_exact.json','output_sha256':digest(root/'output/k119_afterreading_exact.json'),
 'review':'K119_REVIEW.md','review_sha256':digest(root/'K119_REVIEW.md'),
 'patches':'K119_patches.json','patches_sha256':digest(root/'K119_patches.json'),
 'attribution':who,
 'proof_reading_scope':'All OC45.1–11, OCP.1–6, OCGC.1–4, ORC.1–10; used K78 OCS.1; K10/K116/F35 antecedents previously checked in this branch.',
 'remaining_gate':'None mathematically at stated scope. Root owns source integration, layout and package validation.'
}
(root/'K119_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
