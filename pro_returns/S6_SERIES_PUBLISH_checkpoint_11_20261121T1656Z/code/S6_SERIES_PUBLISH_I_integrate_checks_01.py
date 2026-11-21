from pathlib import Path
import csv, datetime, hashlib, json, sys
from S6_SERIES_PUBLISH_editing import Editor
root=Path(__file__).resolve().parents[1]
ed=Editor('I')
guard=json.loads((root/'agents/i_provenance/S6_SERIES_PUBLISH_I_C12_guards.json').read_text())
for k,g in enumerate(guard['changes']):
    ed.replace(g['old'],g['new'],'D25' if k==0 else ('D23' if k==1 else 'D05'),g['reason'],'ari:C.1.2')
ed.save()

p=root/'agents/provenance/code/S6_SERIES_PUBLISH_recompute_records.py'
guard=json.loads((root/'agents/i_provenance/S6_SERIES_PUBLISH_I_shared_parser_interlude_guards.json').read_text())
before=p.read_text(); text=before
for g in guard['changes']:
    assert text.count(g['old'])==1,g['id']
    text=text.replace(g['old'],g['new'])
p.write_text(text)
(root/'records/S6_SERIES_PUBLISH_I_parser_interlude_applied.json').write_text(json.dumps({
 'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'before_sha256':hashlib.sha256(before.encode()).hexdigest(),
 'after_sha256':hashlib.sha256(text.encode()).hexdigest(),
 'changes':[g['id'] for g in guard['changes']],
 'scope':'Metadata parsing only; no new mathematical check event.'},indent=2)+'\n')

p=root/'S6_DEFECT_REGISTER.csv'
with p.open() as f: reader=csv.DictReader(f); cols=reader.fieldnames; rows=list(reader)
assert not any(r['type_id']=='D25' for r in rows)
rows.append(dict(zip(cols,[
 'D25','proof','An incorrect intermediate assertion in a proof',
 'A proof gives a false reason for an exclusion or identifies a special point incorrectly, even where the theorem remains true.',
 'Paper I, ari:C.1.2, rhombic boundary in the proof',
 'At tau=1/2+iT the point mu=1/2-iT=1-tau was described as another half-period zero; it is a lattice point at which wp has a pole.',
 '(read every inference and its coordinate map in context)',
 'Replace the false intermediate assertion by a complete justified step; compare the replacement with the theorem and all uses, record the exact error and scope, and recheck its conclusion.',
 'blocks publication'])))
with p.open('w') as f: w=csv.DictWriter(f,fieldnames=cols);w.writeheader();w.writerows(rows)

out={
 'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'label':'inv:A2.3',
 'outcome':'The target conclusion agrees with the preread argument using established fam:src:B.1.1 and fam:src:B.1.3 as inputs. Those two input proofs duplicate printed steps 1–5; this event does not claim a new blind derivation of them.',
 'comparison':[
 'The affine map mu=1-z0 and its local positive imaginary derivative agree exactly with printed step 6 and the primary Theorem 1.',
 'The new root-atlas chord-and-tangent program gives x(2P)=9r^2/8, y(2P)=sqrt(2)(32-5r^3)/32 and x(3P)=16(r^3-1)(5r^3-32)/(81r^4). Multiplication by r^4 and r^6 recovers all three original cubic formulas in step 7.',
 'The new formal parameter -X(3P)/Y(3P) has exact order two and leading coefficient 9sqrt(2)/32. The Abel-coordinate map transports that order to mu-(2-tau)/3; it agrees with the printed wp principal-part argument.',
 'Printed steps 1–5 reproduce the section-generation and height calculation already fully present in fam:src:B.1.1 and fam:src:B.1.3. They will be consolidated with exact references and unchanged conclusions.',
 'The arithmetic and geometric Weierstrass equations are connected by the exact pointed map already recorded in I:weierstrass-comparison; no identification by j alone is used.'
 ],
 'prior_exposure':'Three citation/one-minus lines were exposed by rg after the same affine map had already been derived. The target’s other proof steps were opened only after the frozen record.',
 'mathematical_disagreement':None}
(root/'records/S6_SERIES_PUBLISH_I_A23_comparison.json').write_text(json.dumps(out,indent=2)+'\n')

columns=['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group']
rows=[]
events=[('targeted proof check',
 'PASS: derived the complete target from the already read section-generation and visible-section results fam:src:B.1.1 and B.1.3, with a fresh primary-source affine branch map mu=1-z0 and exact root-atlas order-two calculation before opening the target proof. Compared every printed step; the duplicated input proofs are reread inputs, not newly blind-derived claims. Three formula-attribution lines were incidentally exposed after the affine map had been derived; this exposure is disclosed.',
 'records/S6_SERIES_PUBLISH_I_A23_comparison.json'),
 ('computation or formal certificate',
 'PASS: a new exact chord-and-tangent calculation on the smooth r^3=t Weierstrass model verifies 2P and 3P on the cubic and computes -X(3P)/Y(3P)=(9sqrt(2)/32)r^2+O(r^5). This uses the formal parameter directly, compared with the printed wp principal-part method; no floating-point inference.',
 'records/S6_SERIES_PUBLISH_I_A23_preread_computation.json')]
for k,(typ,outcome,evidence) in enumerate(events,1):
 h=hashlib.sha256((typ+evidence).encode()).hexdigest()[:16]
 rows.append(dict(zip(columns,['inv:A2.3','2026-11-21','GPT-6 Astra (OpenAI), ChatGPT Pro mode; reasoning effort inherited, no separate numerical setting exposed; S6_SERIES_PUBLISH root',typ,outcome,'ce:publish-I-A23-'+h,'S6_SERIES_PUBLISH_I','work/'+evidence,str(k),typ,'eg:publish-I-A23-'+h])))
p=root/'records/S6_SERIES_PUBLISH_I_root_A23_CHECK_EVENTS.tsv'
with p.open('w') as f: w=csv.DictWriter(f,fieldnames=columns,delimiter='\t');w.writeheader();w.writerows(rows)
print(json.dumps({'new_register_type':'D25','A23_events':len(rows),'parser_repair_applied':True}))
