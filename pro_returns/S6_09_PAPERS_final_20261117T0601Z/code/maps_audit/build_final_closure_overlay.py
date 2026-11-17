"""Append-only current closure view. Historical receiving events are not rewritten."""
from pathlib import Path
import json,re,hashlib
R=Path(__file__).resolve().parents[3];W=R/'deliverables/work/maps_audit'
meta=dict(reader='GPT-6 Astra (OpenAI, ChatGPT Pro mode)',effort='Pro',date='2026-11-17')
J=lambda p:json.loads((R/p).read_text())
credit=J('deliverables/work/maps_audit/maps60_credit_comparison.json');audit=J('deliverables/work/maps_audit/results_audit.json');byid={r['id']:r for r in audit}
events=J('deliverables/work/maps_audit/check_events.json');byevent={e.get('event_id'):e for e in events}
scoped=[]
for n in ['remaining_primary_source_checks.json','maps_B_and_weight_source_checks.json','fourfold_priority_source_checks.json','attached_maps_source_checks.json','final_citation_source_checks.json']:
 for r in J('deliverables/work/maps_audit/'+n):scoped.append((n,r))
# Explicit additions whose exact scope is narrower than a source's general subject.
extra={
'A.2.2':['Hatcher2002','mapsToda52'], 'B.1.1':['mapsBott59'], 'B.1.2':['mapsBott59','mapsToda52','mapsAPS2'],
'B.2.1':['Hatcher2002'], 'B.3.1':['CuspNullMilnor1965','Pontryagin1950Root','Pontryagin1955Root','Johnson1980Root','DebrayGunningham2018Root','Hatcher2002'],
'B.3.2':['Hatcher2002'], 'B.3.3':['Hatcher2002'], 'B.4.1':['mapsLR','mapsVia2','mapsViaLog','mapsEngel','mapsAPS2','mapsToda52'],
'B.5.1':['mapsAC26','mapsWaldhausen68','mapsHatcher02'], 'B.5.2':['Hatcher2002','mapsAC26','mapsEngel'],
'B.6.1':['EellsKuiper1962'], 'B.6.2':['mapsKrylov03','Olbermann2010D','Smale1961','Cerf1970'],
'B.6.3':['DGKX2026v1'], 'B.6.4':['mapsKrylov03','mapsCrowleyNordstrom19'], 'B.6.5':['EellsKuiper1962'], 'B.6.6':['mapsKrylov03'],
'B.6.7':['DGKX2026v1'], 'B.6.8':['DGKX2026v1'], 'B.6.9':['mapsCrowleyNordstrom21'],
'B.6.10':['mapsShioda90'], 'B.6.11':['mapsEngel'], 'B.6.12':['mapsShioda90','mapsGriffiths68II'],
'B.6.15':['mapsCrowleyNordstrom21'], 'B.6.18':['mapsJin26'], 'B.6.19':['mapsCrowleyNordstrom21'],
'B.6.20':['mapsJin26','mapsCrowleyNordstrom21'], 'B.6.21':['EellsKuiper1962','Cerf1970','Smale1961'],
'B.6.24':['mapsCrowleyNordstrom21','EellsKuiper1962'], 'B.6.25':['EellsKuiper1962'],
'C.1.1':['Fulton1993'], 'C.1.2':['Fulton1993'], 'C.1.3':['Fulton1993'], 'C.1.4':['Fulton1993'], 'C.1.5':['Fulton1993'],
'E.1.3':['ffChen','mapsDeligne1974HodgeIII'], 'E.1.5':['ffChen','mapsDeligne1974HodgeIII'],
'F.1.1':['Yang2026'], 'F.1.2':['ffEsoleKang','ffPetersSterk'], 'F.1.3':['ffMandal'],
'F.2.5':['ffChen','mapsDeligne1974HodgeIII'], 'F.2.6':['ffChen','mapsDeligne1974HodgeIII'],
'F.3.4':['ffDeligne'], 'F.3.8':['ffAlarconForstneric25'], 'F.3.9':['ffAlarconForstneric25','ffForstnericPrezelj02'], 'F.3.10':['ffAlarconForstneric25'], 'F.3.11':['ffAlarconForstneric25'],
'F.4.1':['ffNikulin','ffBHS','ffNagy2026','ffMandal']}
limits={
'A.2.2':'Refutation of uniqueness from exterior agreement, with all twelve local bubbles. The specific canonical repaired map is fixed separately.',
'B.3.1':'Retained-angle collapse only; no replacement by the angle-forgotten nullhomotopy. The distinct 734-line working proof is separately retained and root-read.',
'B.3.2':'The original factorization proof and the additional carrier-extension proof have distinct retained arguments. The latter requires the explicit codimension-zero/frontier hypothesis.',
'B.4.1':'Named-family markings and actual primitive quotient are essential. The LR source H1/H2 target typo is logged; the literal Engel cusp formula was repaired in I.',
'B.5.1':'Underlying smooth normal disc bundle at finite multiple fibres, not a holomorphic trivialization. Actual AC26 original p42 sentence corrected; the separate alpha3 typo was working-edition only.',
'B.6.1':'Conditional arithmetic reduction only; without a computed sixfold class this gives no restriction on the original monodromy.',
'B.6.7':'Exact affine quotient defect refutes scalar-shear isotopy; it does not obstruct arbitrary smooth isotopy.',
'B.6.8':'Order-six ordinary affine obstruction is compatible with the proved zero smooth mapping class.',
'B.6.14':'Only the asserted one-component ruled conductor filling is obstructed; no universal impossibility for all fillings.',
'B.6.16':'Identity on two Leray grades alone does not identify the integral H3 extension or shear; later geometric arguments do.',
'B.6.18':'The intermediate unique class is parametrized by B; this row does not yet numerically evaluate B.',
'B.6.19':'The zero correction here is conditional on k=−1, established in the later actual Euler-cube theorem.',
'B.6.25':'The product filling is constructed after the actual isotopy; it is not an independent proof of zero monodromy.',
'C.1.3':'Smooth whole-cusp connected cover obstruction; compatible with C1.5 normal multi-component globalizations.',
'C.1.4':'Single prescribed cusp component and stated degree only.',
'E.1.3':'Rational local invariant cycles plus the separately proved pure/free cellular calculation give integral saturation; the rational source theorem alone does not.',
'F.2.5':'Rational homology and relative almost-complex structure here; integral torsion/three-connectivity are in F2.6.',
'F.2.6':'The earlier missing torsion transgression is supplied by the complete primitive theta=a+4k calculation, not by rank or Smith output alone.',
'F.3.4':'Algebraic polarized abelian-surface family is essential for the applied global Deligne semisimplicity theorem.',
'F.3.7':'Specific candidate with separately constructed finite good-reduction caps; distinct from the general F3.11 one-cusp theorem.',
'F.3.10':'LSAP bundle fibres, not merely an unproved general Oka-1 fibre condition.',
'F.3.11':'One prescribed bounded maximal-cusp correction with the other punctures retained. Does not assert simultaneous finite good reduction at every puncture.',
'F.4.1':'Full unstable normal invariant and inertia input checked; the smooth classification is not inferred from the intersection lattice alone.'}
program_ledgers=['deliverables/code/maps_audit/selected_reruns.json','deliverables/work/maps_audit/maps_B_remaining_program_manifest.json','deliverables/work/maps_audit/final_small_program_manifest.json','deliverables/work/maps_audit/kummer_full_checks.json','deliverables/code/root_maps_F/final_execution_reconciliation.json','deliverables/work/maps_audit/audit_notes.md','deliverables/work/maps_audit/check_events.json']
program_ledgers=[p for p in program_ledgers if (R/p).exists()]
rows=[]
for c in credit:
 sid=c['source_id'];a=byid[sid];ids=a.get('check_event_ids',[])
 source_links=[]
 for n,s in scoped:
  if 'MAPS:'+sid in s.get('applications',s.get('results',[])):
   source_links.append(dict(ledger='deliverables/work/maps_audit/'+n,key=s.get('key',s.get('citation_key')),opened_locators=s.get('opened_locators',[]),scope=s.get('verification_scope',s.get('scope','')),status=s.get('status','')))
 block=[]
 for b in a.get('source_blocks',[]):
  bb=dict(b);p=R/bb['file'];bb['source_sha256']=hashlib.sha256(p.read_bytes()).hexdigest();block.append(bb)
 named=[]
 for b in block:
  text='\n'.join((R/b['file']).read_text().splitlines()[b['start_line']-1:b['end_line']]);named+=re.findall(r'[A-Za-z][A-Za-z0-9_]*\.(?:py|jl)',text)
 row=dict(source_run='S6_04_MAPS_MANIFOLDS',source_id=sid,paper='III',source_status=a['status'],statement=a['statement'],source_blocks=block,full_receiving_proof_read=True,current_check_event_ids=ids,receiving_read_records=[dict(event_id=e,record='deliverables/work/maps_audit/check_events.json',scope=byevent.get(e,{}).get('scope','')) for e in ids if e.startswith('new-')],source_dependency_status='Closed in the exact operative scopes recorded; provider citation/program reviews remain separately itemized rather than inferred from receiving reads.',exact_source_check_records=source_links,additional_opened_source_keys=extra.get(sid,[]),additional_source_ledgers=['deliverables/work/maps_audit/references_verified.json','deliverables/work/invariants_arithmetic/retained_angle_references_verified.json','deliverables/work/invariants_arithmetic/push_C_references_verified.json','deliverables/work/root/classical_references_verified.json','deliverables/work/cdp_audit/maps_E/references_verified.json'],named_programs=sorted(set(named)),program_check_records=a.get('program_check_records',[]),program_ledgers=program_ledgers,credit_record='deliverables/work/maps_audit/maps60_credit_comparison.json#'+sid,check_outcome='Passed full receiving proof and exact operative-source checks at the stated scope; historical partial checks and repaired gaps are preserved.',limitation=limits.get(sid,'Statement retains its exact hypotheses and conventions; finite program output certifies only the stated finite calculation.'),historical_audit_state=a.get('audit_state'),historical_recorded_checks=a.get('recorded_checks',''),**meta)
 if sid=='F.2.6':row['full_repair']='deliverables/work/maps_audit/fourfold_torsion_transgression.tex'
 if sid=='B.3.2':row['full_repair']='deliverables/work/maps_audit/carrier_nullhomotopy_by_extension.tex'
 if sid=='B.6.11':row['upstream_printed_labels']=['I:push:src:A.4.1','I:push:src:A.4.4']
 rows.append(row)
 a['current_closure']=dict(overlay='deliverables/work/maps_audit/III_maps60_final_closure.json',source_id=sid,full_receiving_proof_read=True,check_outcome=row['check_outcome'],**meta)
(W/'III_maps60_final_closure.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
(W/'results_audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
print('Saved own60 final receiving/source closure rows; historical events retained.')
