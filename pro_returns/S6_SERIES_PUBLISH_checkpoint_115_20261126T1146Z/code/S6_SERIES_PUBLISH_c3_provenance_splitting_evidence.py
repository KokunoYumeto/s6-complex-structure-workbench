#!/usr/bin/env python3
"""Record the exposed full splitting-unit comparison; no shared writes."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation3_provenance/splitting'
now = datetime.now(timezone.utc).isoformat()


def read(name):
    with (OUT/name).open(newline='') as f:
        return list(csv.DictReader(f,delimiter='\t'))


def write(name, rows):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,list(rows[0]),delimiter='\t',lineterminator='\n')
        w.writeheader();w.writerows(rows)


rows=read('S6_SERIES_PUBLISH_splitting_defects.tsv')
for row in rows:
    row['review_status']='Complete original174-line final unit and complete receiving P320/P321/final problem read. Complete E15/P278/E2.2/E2.4/E2.5 input owners read. Exact maps and final bounded wording reread. Used and rechecked; no independent, program-execution or final-page credit.'
write('S6_SERIES_PUBLISH_splitting_defects.tsv',rows)

outcomes=[
('inv:E2.3','final-problem',
 'Read the entire original174-line final section and entire receiving final problem. Preserve general tooth counts, special members outside the exact nonempty open12-tooth family, the rank3 bundle and its section question. Preserve (-8,-9,-9), zero sections, Hodge49/48, and the complete established tangent/Kuranishi scope. All proved blocks move earlier; tag000B, tag01SW and labelapp:II:programs remain. Equationtag01TW moves unchanged with its single owner. No open question is reclassified as proved.'),
('prop:II:comb-kernel-bounds;invII:eq:E.7','degree-bounds',
 'Read every original degree/bounds/pencil paragraph and complete receiving P320. Exact identity on the positive-comb data. Read E15 characters and nonnegative splittings: (r,k)=(3,2),(4,1). Verify the equivariant-to-coarse matrix and its inverse, the two length1 quotients, determinant/coarse degree minus2, weighted y target frame and generic-rank kernel degree. Preserve all four Hom contributions and both arithmetic cases. Hodge bounds use the identical E2.2 K_m. D_0 is the old D by identity on each summand; preserve both pencil maps and give both global kernel injections and chartwise inverse divisions. All m12 numerical outputs remain; no comb realization of the abstract pencil maps is asserted.'),
('prop:II:comb-cup-duality','cup-duality',
 'Read the complete old and receiving cup-duality arguments. Keep the same F,G,D,L,N and Cech convention. J has matrix[[0,1],[-1,0]] and inverse minusJ; the root cup row is(b,-a,d,-c). Dualizing gives N*=ker(delta0*), and I_F tensorJ with its explicit inverse gives the root kernel identification. Finite averaging descends both inverse maps. Torsion of N is annihilated by Hom(-,O), so the original unsaturated cokernel scope is preserved. R1 tangent and Q_m are the exact E4a objects, with their original period-map support data.'),
('cdp:st:E15;def:II:comb-cup-kernel;inv:E2.2;inv:E2.4;inv:E2.5','receiving-inputs',
 'Read all five complete input owners/proofs. E15 supplies the same root bundles, characters, coarse degrees/nonnegative splittings, tangent tuple and full period-family Kuranishi argument. P278 supplies generic rank of the identical kappa1. E2.2 supplies E4a/E5 under the same bundle maps. E2.5 was read through all seven steps: seed pairing, family lift/free node kernel, sufficient mixed jet, conic-frame identity, dominant two-jet map, balanced modifications and collapse/semicontinuity. With T=[[a,c],[b,d]], its trace(T eta J) is precisely P321 row(b,-a,d,-c); its unchanged m12 source/target degrees specialize P320. E2.4 remains untouched. This is exposed receiving-input use, not a second independent proof or a new full-unit closure of those earlier owners.'),
]
events=[]
for ids,key,outcome in outcomes:
    events.append(dict(statement_id=ids,date=now[:10],
        who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; continuation3 provenance',
        type='used and rechecked in this run',outcome=outcome,
        event_id='publish:c3:splitting:'+key,phase='publication full owner transfer',
        source_file='agents/continuation3_provenance/splitting/S6_SERIES_PUBLISH_splitting_CHECK_EVENTS.tsv',
        source_row='',source_event_type='used and rechecked in this run',
        evidence_group='publish:c3:splitting:'+key,publish_input_file='',publish_input_row='',
        date_utc=now,where='Original final splitting unit and complete named receiving/input owners'))
write('S6_SERIES_PUBLISH_splitting_CHECK_EVENTS.tsv',events)

classes={
'D01':'Remove now/already/evaluated narration; all mathematics is stated directly.',
'D02':'Replace the unspecified-member and no-saturation disclaimers by their exact positive domains and maps.',
'D03':'No internal-proposal refutation is introduced. The two pencil morphisms are stated and proved on their explicit bundle domain.',
'D04':'Every reference is a resolving label; the old equation tag is preserved under the section counter.',
'D05':'No prompt item occurs.',
'D06':'No compendium reference occurs.',
'D07':'No agent/run language occurs in the mathematics.',
'D08':'Each actual/fully/available/complete-derivation occurrence removed or replaced by a precise mathematical object.',
'D09':'Both body filenames move to plain-path appendix159; full pinned sources read, not executed.',
'D10':'Inherited done; StatementRecord renderer and permanent-tag renderer untouched.',
'D11':'Keep the original open domain once in the final problem; full positive scopes of the two proved inputs are explicit.',
'D12':'The degree/bounds/examples and cup duality have one owner each. E15 owns tangent/Kuranishi and E2.5 owns the attained12-tooth splitting.',
'D13':'Both orphan proved paragraphs and the unnumbered cup identity become numbered propositions with full proofs; an open problem has no proof environment.',
'D14':'Proved inputs follow E15/P278/E2.2 in the comb section and precede the12-tooth block; only the exact remaining question stays in the final part.',
'D15':'No front-matter/methodology block in these local units; global first-part update remains root-owned.',
'D16':'Inherited titles retained; both genuinely new numbered owners have short mathematical titles.',
'D17':'Use the complete earlier E15/P278/E2.2/E2.5 owners. New short calculations prove the exact character and pencil maps used here; no known general theorem is re-proved.',
'D18':'No new external citation in these two extracted results. Existing exact primary-source applications stay at their unchanged earlier owners; final bibliography remains a separate pass.',
'D19':'E.7 becomes section-numbered, with its exact formula/label/permanent target preserved.',
'D20':'Same E_m,G_m,rho,kappa,K_m,e_m throughout. Old abstract D is D_0 by identity on each summand. Duality uses the same Cech convention and explicit inverse wedge map.',
'D21':'The universal formulas are proved algebraically; finite program ranges are described only in the appendix and source records.',
'D22':'Supply local equivariant/coarse inverse matrices, target invariant generator, both pencil kernel inverses, and exact receiving hypotheses.',
'D23':'No manual display tag, blank paragraph in an equation, body filename or duplicated clearpage remains in the receiving units. Integrated typesetting remains root-owned.',
'D24':'No paper-structure description is asserted locally; global first-part concordance remains root-owned.',
'D25':'No original theorem is refuted or narrowed. Full original and receiving statements/proofs were compared; the original open splitting question remains open at precisely its stated domain.'}
unitrows=[]
for unit,ids in [('subsec:II:comb-kernel-bounds-duality','prop:II:comb-kernel-bounds;prop:II:comb-cup-duality'),('app:II:programs','inv:E2.3')]:
    for kind,outcome in classes.items():
        status=('inherited done' if kind in ['D10','D16'] else
                'not applicable locally; global pending' if kind in ['D15','D24'] else
                'source ready; integrated build/page reading pending' if kind=='D23' else
                'locally ready for source admission')
        unitrows.append(dict(unit=unit,statement_id=ids,defect_type=kind,status=status,
            outcome=outcome,credit='Exposed complete original/receiving proof comparison; no independent or final-page credit.',date_utc=now))
write('S6_SERIES_PUBLISH_splitting_unit_status.tsv',unitrows)

main=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
for guard in read('S6_SERIES_PUBLISH_splitting_guards.tsv'):
    assert main.count(guard['old_text'])==1
    main=main.replace(guard['old_text'],guard['new_text'],1)
proved=(OUT/'S6_SERIES_PUBLISH_splitting_proved.tex').read_text()
problem=(OUT/'S6_SERIES_PUBLISH_splitting_problem.tex').read_text()
for keys in re.findall(r'\\(?:cref|ref|eqref|SeriesRef)\{([^}]+)\}',proved+problem):
    for key in keys.split(','):
        assert r'\label{'+key+'}' in main,key
status=json.loads((OUT/'S6_SERIES_PUBLISH_splitting_status.json').read_text())
status.update(complete_receiving_read='complete; final bounded wording reread',
    exposed_check_events=len(events),unit_class_rows=len(unitrows),
    local_reference_checks='all receiving labels resolve in guarded insertion',ready=True)
(OUT/'S6_SERIES_PUBLISH_splitting_status.json').write_text(json.dumps(status,indent=2)+'\n',newline='\n')
print(json.dumps(status,indent=2))
