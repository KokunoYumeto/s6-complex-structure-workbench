from pathlib import Path
from datetime import datetime, timezone
import csv

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation3_foundations/sec07'
prefix='S6_SERIES_PUBLISH_sec07_local'
path=OUT/(prefix+'_defects.tsv')
with path.open(newline='') as f:
    r=csv.DictReader(f,delimiter='\t');fields=r.fieldnames;rows=list(r)
for row in rows:
    row['review_status']='Complete original and receiving proof comparison read; exact source and prerequisite maps checked; admission and later consumer-unit edits remain separate.'
with path.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
with (ROOT/'agents/continuation3_foundations/S6_SERIES_PUBLISH_foundations_CHECK_EVENTS.tsv').open(newline='') as f:
    event_fields=next(csv.reader(f,delimiter='\t'))
now=datetime.now(timezone.utc).isoformat()
events=[]
for key,owner,outcome in [
 ('numerical','lem:II:torus-tube-numerical','Read all original UN.7, UN.10 and UN.12 statements/proofs and all their receiving statements/proofs after the bounded replacements, plus the complete new P281 proof. Compared canonical evaluation, adjunction, full-fibre Cartier filtration, compact normalization/resolution Riemann–Roch, the oriented radial chain with boundary [F]−m[S], both rational Chern classes and resolution conductor. UNCR.1–2 and UI.2–4 retain their labels and targets at the common owner; normal S is explicitly covered by UN.5 with D=0. During receiving comparison the tube variable U was restored explicitly in the two consumer openings before admission. P233 and P222 complete statements/proofs were read; no ambient compactness or Betti hypothesis was imported.'),
 ('conductor','lem:II:plane-branch-conductor','Read the complete current P4.34 proof and the complete original/receiving RAT.3 and IRR.1 proofs. P4.34 gives c_i=v_i−r_i, while RAT.3 explicitly factors h=u∏f_j. The new P282 proof preserves the exact identity h_y|Ci=u fi,y∏j≠i fj, conductor multiplication into regular differentials, and the finite-duality length identity c_int=2δ. Its c_i=1 consequence supplies IRR.1 exactly; c_i=2 supplies RAT.3 exactly. This removes the sole sec07 C4e forward premise; P263/C4e remain later. The original IRR.1 conclusion permits a disjoint union of image elliptic curves and total degree two over each, consistent with refined P4R.13.'),
 ('purity','cdp:st:C.2.MH.1','Read the entire original and receiving eight-part purity proof. Opened primary arXiv:math/9902134v1 PDF, SHA25670f48cb73d5df029f9d0434618191d21730aa021aa5dc3be0e8a93ecb5286cc9; read printed pp4–9 including Section3 Lemma1, Theorem1 and its complete proof, Corollaries1–3, and Section4 equation(3). Source global ambient is complete algebraic; the receiving proof explicitly transfers only its holomorphic local quotient-residue construction to the same projective compact strata and retains support-cone/Gysin compatibility, finite-cover idempotents, trace injection and common projective hyperresolution. It does not attribute the full analytic theorem to the algebraic source.'),
 ('character','lem:II:torus-tube-character','Read complete original UN.7 and MH.2 statements/proofs, the complete new P289 proof, full receiving MH.2 and UN.7 proofs, and complete P4R.1, P233, P243 and MH.1 prerequisites. The P4R.1 quotient by the regular-fibre image is Z/m, proving injection of rational H1 restriction. P233 gives the same integral tube extension as the global Leray edge isomorphism. Compared prime choice on both S and F, connected cyclic cover, augmentation representation, Koszul contraction, support duality, conductor descent, exceptional-matrix inverse, weight-two kernel/weight-three purity, and every rational/ruled coefficient dimension. The general third-cohomology surjection and fourth-cohomology isomorphism retain their explicit maps before imposing projectivity; the stronger isomorphism and Euler equality are scoped to rational/ruled Z. All MH.8–14 and UI.9–11 identifiers survive through explicit aliases.')
]:
    evidence='publish:c3:foundations:sec07:local:'+key
    event=dict.fromkeys(event_fields,'')
    event.update(statement_id=owner,date=now[:10],who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 foundations',type='used and rechecked in this run',outcome=outcome+' Exact replay found all eleven guards once and preserved every existing label and permanent target with the same multiplicity. No shared main write, independent re-derivation, required-check increment or final PDF reading is claimed.',event_id=evidence,phase='publication text and proof comparison',source_file=str(path.relative_to(ROOT)),source_event_type='used and rechecked in this run',evidence_group=evidence,date_utc=now,where='Local numerical and conductor criteria; complete receiving proof comparison and bounded consumer replacements')
    events.append(event)
with (OUT/(prefix+'_CHECK_EVENTS.tsv')).open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=event_fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(events)
status=[]
for kind in [f'D{i:02}' for i in range(1,26)]+['restructuring']:
    state='done'
    basis='Complete 329-line receiving subsection read against this class; all changed instances are logged. The eleven guards also preserve every old identifier and were read at their full affected consumer proofs. This status covers this subsection only.'
    if kind in ('D10','D16'):
        basis='Existing closure preserved: every statement has a mathematical title, label and permanent tag; dependency records remain hidden.'
    if kind in ('D14','D24','restructuring'):
        state='open'
        basis='The complete subsection is ordered P281, P282, MH.1, P289, MH.2, with all used inputs earlier and one proof per shared calculation. Root admission and final Paper II placement remain; the following contracted-boundary unit is explicitly separated and still open.'
    if kind=='D23':
        basis='Receiving source typography was read. The integrated build and page-reading gates belong to root and are not claimed here.'
    if kind=='D25':
        basis='Every receiving inference was compared with its complete original proof and consumers. No new refuted theorem is reported. Explicit analytic/projective scope, normal/non-normal D, tube variable, cover maps and refined two-image conductor conclusion are retained; later consumer-unit defects remain open.'
    status.append(dict(unit='subsec:II:local-numerical-conductor-inputs',row=kind,status=state,basis=basis,fragment='agents/continuation3_foundations/sec07/S6_SERIES_PUBLISH_II_sec07_local_inputs.tex'))
with (OUT/(prefix+'_unit_progress.tsv')).open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(status[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(status)
print(f'{len(rows)} defect instances, {len(events)} exposed-reading events and {len(status)} bounded subsection-status rows written; P281, P282, P289 used.')
