"""Retain the fully read duality/Euler prerequisite, with strictly bounded scope."""
from pathlib import Path
import csv, hashlib, json
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'deliverables/work/maps_audit'
SRC=ROOT/'sources/codex_workspace/courses/CG-S6/sources/manifold-duality-the-diagonal-and-wu-classes.source.txt'
META=dict(reader='GPT-6 Astra (OpenAI, ChatGPT Pro mode)',effort='Pro',date='2026-11-17')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,x):(OUT/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
lines=SRC.read_text().splitlines()
ret=OUT/'checked_course_providers/manifold-duality-through-euler.md'
ret.write_text('\n'.join(lines[:250])+'\n')
event=dict(event_id='new-course-provider-duality-euler-scoped-20261117',source=str(SRC.relative_to(ROOT)),source_sha256=sha(SRC),
 locator='Source lines1–250, complete sections1–4 through Corollary4.2; section5 Wu classes and subsequent exercises are outside this reading',
 raw_producer_header=lines[2],producer='GPT-6.1 Sol (OpenAI)',producer_effort='Ultra',producer_date='October 2026 (no day recorded)',
 full_proof_read_in_scope=True,whole_source_file_read=False,retained_complete_proof=str(ret.relative_to(ROOT)),retained_sha256=sha(ret),
 outcome='All needed singular duality, tubular, compact embedding and signed-diagonal/Euler proofs read and rederived. No analytic Hodge argument or Wu-class proof is certified by this event.',
 independent_derivation=[
 'Recomputed the right-cap boundary identity and compact-support filtered direct limits, all Mayer–Vietoris connecting signs, finite-union and countable-union Poincare-duality proof.',
 'Checked the finite-generation argument using faces of a finite fundamental cycle, perfect field pairing, coefficient-independent Euler characteristic and torsion cancellation in the universal-coefficient formula.',
 'Read the contraction proof of the inverse-function theorem, smooth local flows and chart-patched local addition; checked the proper-exhaustion radius choice giving a globally injective tubular map, including locally closed embeddings.',
 'Checked the finite chart-block embedding and finite cubical neighbourhood retraction, without assuming triangulation of the original manifold.',
 'Recomputed the Thom dual-class evaluation, tangent-first diagonal-normal determinant 2^d, every Koszul sign in the cup-dual basis formula and the Euler pullback/evaluation equal to chi.',
 'Also read the receiving tangent-index chapter lines229–285 and350–448. Its signed-diagonal Euler step agrees with this complete singular proof; the analytic Hodge assertions in the surrounding chapter are not replaced by a claim of having read their distinct providers.'
 ],
 remaining_imported_dependencies=[
 'Singular excision, front/back products, coefficient and Thom prerequisites are the previously retained Paper I chain and complete characteristic-class providers; retain their actual labels.',
 'The compact-set orientation/fundamental-class construction is explicitly invoked in source lines11–16. The receiving tangent-index section4 prints its gluing argument; do not replace this with an unexpanded appeal to Hodge theory.',
 'The precise external Euler/diagonal comparison with Milnor–Stasheff is recorded separately. This event does not claim a full reading of Section11 or of source sections5–6.'
 ], **META)
save('course_duality_euler_full_check.json',event)
history=json.loads((OUT/'check_events.json').read_text())
if not any(e.get('event_id')==event['event_id'] for e in history):history.append(event)
save('check_events.json',history)

spec=[('2.1','Lemma','The compact-support gluing square',54,77),('2.2','Theorem','Poincare duality',78,85),('2.3','Corollary','Finite generation and perfect pairings',86,99),('3.1','Lemma','Local inverse and local flows',104,126),('3.2','Theorem','Tubular neighbourhood',127,146),('3.3','Lemma','Compact Euclidean embedding and finite domination',147,154),('4.1','Theorem','The signed diagonal formula',207,238),('4.2','Corollary','Euler number and Euler characteristic',239,250)]
rows=[]
for num,kind,title,start,end in spec:
 block='\n'.join(lines[start-1:end])+'\n'
 rows.append(dict(source_run='WORKING_EDITION_COURSE_PROVIDER',source_id='CG-S6-DUALITY-'+num,source_number=num,source_file=str(SRC.relative_to(ROOT)),source_sha256=sha(SRC),
  kind=kind,title=title,paper='III',reserved_label='courseIII:duality:'+num,printed_label='',start_line=start,end_line=end,proof_range=[start,end],full_setup_range=[1,start-1],
  statement_as_printed=lines[start-1],complete_source_text=block,complete_source_text_sha256=hashlib.sha256(block.encode()).hexdigest(),retained_complete_proof=str(ret.relative_to(ROOT)),
  producer=event['producer'],producer_effort=event['producer_effort'],producer_date=event['producer_date'],raw_producer_header=lines[2],
  full_proof_read=True,current_check_event=event['event_id'],check_outcome=event['outcome'],
  source_credit='Classical singular duality and Milnor–Stasheff diagonal/Euler formulas; complete receiving exposition by the explicitly recorded GPT-6.1 Sol provider. No novelty claim.',
  duplicate_of_existing_inventory=False,taken_over_by='',
  notes='Keep this exact provider proof once. Several earlier geometric arguments rederive special cases; those are distinct coordinate proofs. Do not import unread Wu-class material.',**META))
save('course_duality_euler_provider_inventory.json',rows)
with (OUT/'course_duality_euler_provider_inventory.csv').open('w',newline='') as f:
 keys=['source_run','source_id','source_file','paper','reserved_label','kind','title','start_line','end_line','full_proof_read','current_check_event','producer','producer_effort','producer_date','raw_producer_header','source_sha256','duplicate_of_existing_inventory','taken_over_by','check_outcome','retained_complete_proof']
 w=csv.DictWriter(f,fieldnames=keys,extrasaction='ignore');w.writeheader();w.writerows(rows)

ms=ROOT/'sources/external/maps_audit/milnor_stasheff1974.pdf'
ref=dict(key='MilnorStasheff1974',keys=['MilnorStasheff1974','mapsMilnorStasheff74'],url='https://www.maths.ed.ac.uk/~v1ranick/papers/milnstas.pdf',source=str(ms.relative_to(ROOT)),sha256=sha(ms),
 status='verified in the specified scope',opened_locators=[
 'Printed pp.119–120, Theorem11.3 and complete dual-class/Euler proof, original PDF physical pages120–121: text opened and read',
 'Printed pp.121–122, Lemma11.5 and complete diagonal-normal-bundle proof, original PDF physical pages122–123: text opened and read',
 'Printed pp.128–130, Theorems11.10–11.11 and Corollary11.12 with their complete proofs, original PDF physical pages129–131: visually opened and read'
 ],verification_scope='Closed smooth oriented manifold and an oriented embedded normal bundle. Exact Thom dual-class restriction gives Euler class; the normal bundle of the diagonal identifies with TM with the displayed orientation; the signed cup-dual-basis diagonal formula gives e(TM)[M]=chi(M). Matched every orientation and finite-dimensional field-cohomology hypothesis of the retained source. No reading of the full book or of the subsequent Wu-class statements is claimed.',**META)
refs=json.loads((OUT/'references_verified.json').read_text())
if not any(x.get('key')==ref['key'] for x in refs):refs.append(ref)
save('references_verified.json',refs)
checks=json.loads((OUT/'course_geometric_source_checks.json').read_text())
if not any(x.get('key')==ref['key'] for x in checks):checks.append(ref)
save('course_geometric_source_checks.json',checks)
save('duality_euler_source_check.json',ref)
(OUT/'duality_euler_checked_references.bib').write_text('''@book{MilnorStasheff1974,
  author = {Milnor, John W. and Stasheff, James D.},
  title = {Characteristic Classes},
  year = {1974},
  series = {Annals of Mathematics Studies},
  number = {76},
  publisher = {Princeton University Press},
  address = {Princeton, NJ},
  url = {https://www.maths.ed.ac.uk/~v1ranick/papers/milnstas.pdf}
}
''')
print(json.dumps(dict(scoped_complete_proofs=len(rows),retained_lines=[1,250],unread_Wu_scope_excluded=True,primary_reference=ref['key'])))
