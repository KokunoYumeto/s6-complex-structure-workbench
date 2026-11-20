from pathlib import Path
import csv, json, hashlib
root=Path(__file__).resolve().parents[1]
actor='GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited from root (not separately exposed), S6_SERIES_GRIND/corrections_audit'
rows=json.loads((root/'row_assessments.json').read_text())
scope={
 'night:P3K.115':('ES.1–6 at cp15 IV106457–107160',
   'The complete marked-node domain excluding omega=0,1,±1/2; the stated M6 and M2 infinity-cap progressions; inherited order-one norm-zero finite filling including the original III member; both primitive signs, retained characters, full K96 reference and every prescribed basis fan.'),
 'night:P3K.118':('RJC.1–13 at cp15 IV113479–115152',
   'The fixed original E6/III source with the four printed point-line/root progressions, hn_infinity+mn_zero=epsilon=±1, zero additional ordinary total norm, full characters, references, selected fan and actual contraction domain.')}
for label,(locus,extent) in scope.items():
 rows[label]={
  'confidence_state':'proved at the stated scope',
  'confidence_line':'Mathematical continuation gate closed: the complete '+locus+' proves the printed endpoint classification, primitive characteristic pairs and exact all-fan/all-loop return image.',
  'independent_routes':[
    'Retained producing-run complete independent source/root/fan audits remain credited at their recorded scopes; this run does not claim a new read of every duplicate printed peer proof.',
    'This run read the complete primary '+locus+', including actual Cartier modules, root inverses, finite characters, all annular reference terms, primitive endpoint and family phase, genuine completed covering, page/collar and target-prism maps.',
    'IV_open_prereading.md and IV_K118_additional_prereading.md preserve the actual before-proof derivation boundaries; the latter independently derives the two-cap exponents, four page pairs, divisibility target and phase integrality.',
    'Fresh independent_IV_joint_checks.py passed139,172 exact assertions across365 admissible profiles,5,110 signed endpoint representatives and7,014 rational target-prism steps. It reuses only this audit’s earlier independent Gaussian solver, and imports no supplied historical certificate.'],
  'remaining_risk':'No unresolved mathematical gap identified within this exact scope: '+extent+' The already named K67/K68/K69/K71/K73/K96/F35/F46 maps remain explicit retained inputs. Bounded source-credit and editorial cleanup are separate from mathematical closure; no further ordinary-norm or source-moduli classification is asserted.',
  'format_check':None,'layout_check':None,'completion_state':None}
(root/'row_assessments.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
p=root/'CHECK_EVENTS.tsv'
with p.open(newline='') as f:
 rd=csv.DictReader(f,delimiter='\t'); fields=rd.fieldnames; events=list(rd)
def add(label,kind,outcome):
 event={'statement_id':label,'date':'2026-11-19','who':actor,'type':kind,'outcome':outcome,'phase':'S6_SERIES_GRIND'}
 event['event_id']='s6sg:'+hashlib.sha256((label+'|'+kind+'|'+outcome).encode()).hexdigest()[:20]
 if not any(q['event_id']==event['event_id'] for q in events):events.append(event)
for label,(locus,extent) in scope.items():
 add(label,'targeted proof check','Read complete primary '+locus+'. Checked actual source/point-line/root inverses, finite characters, all annular references, phase-preserving shorter-family isomorphism, primitive endpoint exhaustion, actual degree-b completed-cover characteristic comparison, page/collar maps and full target-prism/unit-witness argument. Scope: '+extent+' No unresolved mathematical step identified. Complete report: IV_K115_K118_completion.md. Retained full peer audits credited without claiming every duplicate proof was freshly read.')
 add(label,'computation or formal certificate','Fresh code/independent_IV_joint_checks.py completed PASS139,172 assertions in3.204 seconds,365 admissible profiles,5,110 signed endpoint representatives and7,014 rational nine-variable prism steps. Full functions precede specialization; exact page pairs, finite phases/characters, unit witnesses and residue-period arguments are checked. The program reuses only this audit’s previously written Gaussian solver by AST extraction, without executing its other code; no supplied historical verifier is imported. Output code/independent_IV_joint_checks.json records every name, selected complete witnesses and both code hashes. Bounded tests support, rather than replace, the read geometric and unbounded arguments.')
add('night:P3K.118','independent re-proof','Scoped before-reading derivation only: IV_K118_additional_prereading.md independently derives the degree-mh page Euler inputs and all four proposed characteristic pairs, integral d0 and J0, chronological phase, full positive divisor necessity and negative-annular obstruction target before reading any RJC proof. It explicitly left the actual page/cover/root/fan morphisms to be checked. Those gates were then resolved by the complete RJC.1–13 reading. This is not a claimed blind reproof of the whole theorem.')
with p.open('w',newline='') as f:
 wr=csv.DictWriter(f,fieldnames=fields,delimiter='\t');wr.writeheader();wr.writerows(events)
patches=[{'label':label,'proposed_status':'proved','mathematical_statement_changes':[],
 'scope_confirmation':extent,'proof_locus_read':locus,
 'editorial_action':'Reconcile continuation-review and pending-audit workflow headings with the completed mathematical proof; preserve exact scope and prior evidence.'} for label,(locus,extent) in scope.items()]
(root/'IV_K115_K118_status_patches.json').write_text(json.dumps(patches,ensure_ascii=False,indent=2)+'\n')
print(len(rows),'row assessments;',len(events),'typed events')
