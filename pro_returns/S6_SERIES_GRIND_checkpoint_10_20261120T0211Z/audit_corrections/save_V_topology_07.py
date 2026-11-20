from pathlib import Path
from datetime import datetime, timezone
import json,csv,hashlib

d=Path(__file__).parent;root=d.parent
actor='GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited from root (not separately exposed), S6_SERIES_GRIND/corrections_audit'
now=datetime.now(timezone.utc).isoformat()
report=d/'V_topology_receiving_07.md'
programs={}
for name in ['reconstruct_V_cusp_06','independent_V_topology_inputs_07','reconstruct_V_global_06','verify_V_global_saved_07']:
    p=d/'code'/f'{name}.py';o=p.with_suffix('.json');data=json.loads(o.read_text())
    assert data['status']=='PASS'
    programs[name]={'source':str(p.relative_to(root)),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
                    'output':str(o.relative_to(root)),'output_sha256':hashlib.sha256(o.read_bytes()).hexdigest(),
                    'assertions':data['assertions'],'seconds':data.get('seconds',data.get('elapsed_seconds'))}
ass={
'night:P1.10':{
 'confidence_state':'high; full receiving proof and actual construction maps checked',
 'confidence_line':'All three construction, properness, logarithmic finite-attachment, cusp van Kampen and Euler proof steps pass at the stated P1.9/P1.11 inputs. The exact group relation determinant is -1.',
 'independent_routes':'Retained whole before-proof derivation ce:64a9c12e7765a81aca60 and separate determinant execution ce:c95d917129d51f23482c; current complete receiving read; fresh topology-input program PASS33 verifies actual affine/coinvariant/cusp-marking/presentation data.',
 'remaining_risk':'No mathematical gap found at the stated family scope. The current merged proof and its changed dependency pages still need the root format/layout gate. Historical ce:a984ed66ddfa587d244b describes characteristic/diffeomorphism work and is not counted as a current P1.10 proof.'},
'night:P1.11':{
 'confidence_state':'high; complete marked cusp proof and fresh full finite certificate checked',
 'confidence_line':'All nine current steps pass, with actual moment/face/deck maps and inverse, logarithmic collapse, spectral-sequence section argument, exact marked PD/AW matrices, primitive images and saturated monodromy kernel.',
 'independent_routes':'Retained separately frozen step derivations are explicitly aggregated in ce:3377110f4531f3afafaf, ce:34eae7ae19c5e740f1b0, ce:5ce089f9d77d06f64538; separate retained finite programs have their exact scopes. Current full receiving review and new186-assertion complete quotient/collapse reconstruction. No new whole before-proof claim.',
 'remaining_risk':'Four guarded available-code/basis replacements await root integration and current rendered QA. Known Cox12.2.5p571 and Achinger–Ogus4.1.1/4.1.2–3pp480–482 credit remains at its precise retained opening/morphism scope. Historical ce:7f02243183c0758fc56b describes characteristic/diffeomorphism work and is not used for this gate.'},
'night:P1.12':{
 'confidence_state':'high; full marked gluing proof and actual low-degree basis maps checked',
 'confidence_line':'All ten receiving steps pass, including exact evaluation/collar maps, finite signed-permutation cellular models and norm maps, the complete complement cone, actual vertical kernel cycles and unit collapse matrices, Mayer–Vietoris, Hurewicz and integral duality.',
 'independent_routes':'Retained whole complement/Mayer–Vietoris prederivation ce:ef69db3392bc6a6db8f0 with444 exact prereading checks ce:394a72ff6f057a0d8aa3; separately frozen marked-collar, based mapping-space and Ext routes. Current complete receiving comparison; fresh989-check global reconstruction and914-check saved verifier explicitly reconstruct the actual complement/boundary bases, vertical kernels, H1 map, torsion cycle and all entries of new1.12.7–9.',
 'remaining_risk':'Six guarded computational/basis replacements await root integration and current rendered QA; no mathematical gap found. The new literal degree2/3 matrices replace unsupported historical basis assertions. Exact Achinger–Ogus source comparison is retained as ce:10c3b530fb82b98d68e5. Historical ce:3ce1d2827a4a5ebd6840 describes characteristic/diffeomorphism work and is not used for this gate.'},
'night:P1.19':{
 'confidence_state':'high; actual global cellular proof and reproducible certificate complete',
 'confidence_line':'All thirteen receiving steps pass. A fresh complete global integral complex, actual marked cusp transport, local odd Ext class, primitive j4, and full W/X/T/r/e chain equivalence give the asserted torsion-free homology without global duality. The saved-matrix verifier independently validates its integer certificates and exact basis adapters.',
 'independent_routes':'Retained full receiving review ce:f05095a9c475d7f4cf47 and historical complete executions ce:f3cddd879c44451e78ac retain their actual scope. Current complete proof review, fresh989-assertion full reconstruction, separate914-assertion saved-certificate/basis/relative/even verification, and fresh original Hatcher3.43p254 exact local cap-product application.',
 'remaining_risk':'Mathematical and missing-implementation gates are closed. Ten guarded exact basis/certificate/source replacements and current rendered QA await root integration. A documented complete independent derivation before receiving P1.19 is not supplied by this branch or the retained P1.19 events examined; do not promote after-reading reconstruction or an Euler check into that methodological gate.'}}
for a in ass.values():
    a.update({'format_check':None,'layout_check':None,'completion_state':None})
for p in root.glob('audit_*/row_assessments.json'):
    if p.parent==d:continue
    other=json.loads(p.read_text());overlap=set(ass)&set(other)
    assert not overlap,(str(p),sorted(overlap))
current=json.loads((d/'row_assessments.json').read_text());current.update(ass)
(d/'row_assessments.json').write_text(json.dumps(current,indent=2))
(d/'V_topology_assessments_07.json').write_text(json.dumps(ass,indent=2))

new=[]
def event(label,typ,outcome):
    text=outcome+' Exact comparison: audit_corrections/V_topology_receiving_07.md; actual program/output hashes: V_topology_receiving_receipt_07.json.'
    ident=('s6sg:b4f8e76675c00e5a638a' if 'PASS989 in newly authored reconstruct_V_global_06.py' in outcome else 's6sg:'+hashlib.sha256((label+'|'+typ+'|'+text).encode()).hexdigest()[:20])
    new.append({'statement_id':label,'date':now,'who':actor,'type':typ,'outcome':text,'event_id':ident,'phase':'S6_SERIES_GRIND'})
event('night:P1.10','targeted proof check','Read and compared all3current proof steps: actual evaluation lattice, holomorphic negative-logarithm finite attachment and signs, proper local gluing, cusp fundamental group, exact van Kampen and Euler6. No new whole before-proof derivation claimed; retained ce:64a9c12e7765a81aca60 has that separate scope.')
event('night:P1.12','targeted proof check','Read and compared all10current proof steps and their actual source/lattice/finite collar maps. Fresh displayed1.12.7–9 bases are reconstructed, with literal H1 agreement and new actual degree2/3 kernel matrices. Retained full prereading route ce:ef69db3392bc6a6db8f0 remains separate; no fresh blindness claim.')
event('night:P1.19','targeted proof check','Read and compared all13current proof steps: actual toric boundary retraction, integral filtered suspension support, single boundary Ext class, exact local cap duality, primitive functional and full square-zero boundary chain automorphism/complement homotopies. Current geometric and finite-matrix proof gates close at stated inputs; complete before-receiving methodological gate is not asserted.')
event('night:P1.10','computation or formal certificate','PASS33 in newly authored independent_V_topology_inputs_07.py: actual finite affine powers, primitive lattice splits, both printed signed-permutation conjugators/cycles, coinvariant ell, S cusp transport and van Kampen determinant-1. Post-receiving targeted computation; does not alone prove analytic construction or global homology.')
event('night:P1.19','computation or formal certificate','PASS989 in newly authored reconstruct_V_global_06.py,278.796489seconds (final saved execution; earlier observed duplicate completion271.229945seconds is retained in V_global_execution_recovery_07.json): all complete complement/finite-cap/boundary/global matrices, actual marked kappa transport, j4 integral liftsW/X/T, Ext r/t/e, every global cycle/incoming Smith check and full integral homology. Local cap odd parity is explicitly supplied by the receiving geometric proof. Original historical programs were absent and were not replayed.')
event('night:P1.19','computation or formal certificate','PASS914 in verify_V_global_saved_07.py,91.259443seconds: exact saved integer inverse/kernel/incoming products, outgoing rank witnesses mod1009, full actual low-degree vertical kernel and torsion cycle maps, j4 cokernel row adapter, nine-dimensional K adapter and actual W/X/T, both relative H4 groups and unused even global diagnostic. The first BlockMatrix construction error and successful750/756 versions are retained. Same model family, post-receiving, no blind/cross-model assertion.')
event('night:P1.19','targeted proof check','Fresh primary opening: original author Hatcher Algebraic Topology PDF, Theorem3.43 printedp254 (zero-based physical page262), full theorem/textual proof. Exact application is pullback by actual cusp-cap retraction followed by cap product with its relative fundamental class, n8,k4,R=Z,Aempty,Bboundary. This is known-source application credit, not an independent proof of the source theorem.')
ledger=d/'CHECK_EVENTS.tsv';rows=list(csv.DictReader(ledger.open(),delimiter='\t'));seen={x['event_id'] for x in rows};fresh=[x for x in new if x['event_id'] not in seen]
with ledger.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome','event_id','phase'],delimiter='\t');w.writeheader();w.writerows(rows+fresh)
receipt={'utc':now,'report':str(report.relative_to(root)),'report_sha256':hashlib.sha256(report.read_bytes()).hexdigest(),
         'programs':programs,'source_body_sha256':hashlib.sha256((root/'parts/V.body.linked.tex').read_bytes()).hexdigest(),
         'patches':'audit_corrections/V_P112_P119_guarded_patches_07.json','patch_sha256':hashlib.sha256((d/'V_P112_P119_guarded_patches_07.json').read_bytes()).hexdigest(),
         'retained_event_receipts':['audit_corrections/V_topology_retained_events_07.json','audit_corrections/V_retained_events_06.json'],
         'Hatcher_source_receipt':'audit_corrections/primary_sources/Hatcher2002_author_07.metadata.json',
         'new_events':len(fresh),'event_total':len(rows)+len(fresh),'event_ids':[x['event_id'] for x in fresh],
         'assessment_total':len(current),'new_or_updated_assessments':list(ass),'completion':'unset: exact integration/current layout and P1.19 before-proof methodological gate preserved'}
(d/'V_topology_receiving_receipt_07.json').write_text(json.dumps(receipt,indent=2))
print(json.dumps(receipt,indent=2))
