"""Record the complete C.1 proof audit and actual exact reruns."""
from pathlib import Path
import csv,hashlib,json
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'deliverables/work/maps_audit'
CODE=ROOT/'deliverables/code/maps_audit'
ACTOR=dict(reader='GPT-6 Astra (OpenAI, ChatGPT Pro mode)',effort='Pro',date='2026-11-17')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
source=ROOT/'sources/returns/S6_04_MAPS_MANIFOLDS/sections/kummer.tex'
event=dict(event_id='new-maps-kummer-all-full-20261117',results=[f'MAPS:C.1.{i}' for i in range(1,6)],
           scope='Read all 329 source lines and rederived all five full proofs: '
           'the exact corrected local power map, invariant analytic rings and '
           'nonflat strata; smoothness across adjacent triangles of the entire '
           'periodic fan; ramification and Stein-factor reduction to the '
           'non-scalar lattice obstruction; arbitrary-N orbit lower bound; '
           'and the connected normal finite flat global extension from its '
           'explicit subgroup and local fractional-monomial bases.',
           outcome='All five internal proofs checked. Smooth-source global '
           'nonexistence and normal-singular-source existence are distinct '
           'conclusions. The C.1.1 transfer of proper discontinuity through the '
           'equivariant finite power map also gives a second proof avoiding '
           'the older working chart-boundedness error. Exact orbit and finite '
           'group examples were independently rerun; the all-N statements '
           'are proved without extrapolating from those finite runs.',
           locator=str(source.relative_to(ROOT))+':1–329; kummer_full_checks.json',
           remaining_dependencies=[],**ACTOR)
events=json.loads((OUT/'check_events.json').read_text())
if not any(e['event_id']==event['event_id'] for e in events):events.append(event)
(OUT/'check_events.json').write_text(json.dumps(events,ensure_ascii=False,indent=2)+'\n')

proof_ranges={1:(8,114),2:(116,158),3:(160,212),4:(214,242),5:(244,329)}
results=json.loads((OUT/'results_audit.json').read_text())
rows=[]
for row in results:
    if row['id'] in [f'C.1.{i}' for i in range(1,6)]:
        row.setdefault('check_event_ids',[])
        if event['event_id'] not in row['check_event_ids']:row['check_event_ids'].append(event['event_id'])
        row['your_check']=event['event_id']+': '+event['scope']
        row['audit_state']='full proof read and independently rederived; exact finite examples rerun'
        row['audit_notes']=event['outcome']
        row['full_proof_read']=True;row['current_reader']=ACTOR
        row['current_unresolved_proof_gaps']=[]
        rows.append(dict(source_id=row['id'],source_file=str(source.relative_to(ROOT)),
                         source_sha256=sha(source),full_read_lines=proof_ranges[int(row['id'].split('.')[-1])],
                         check_event=event['event_id'],operative_sources='Local invariant-ring/normal-extension/smoothness arguments are printed in full; toric chart foundations are checked in Paper I.',**ACTOR))
(OUT/'results_audit.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
keys=list(dict.fromkeys(k for row in results for k in row))
with (OUT/'results_audit.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=keys);w.writeheader()
    for row in results:w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in row.items()})

programs=[]
for name,output in [('kummer_orbits.py','kummer_orbits.out'),('kummer_normal_cover.py','kummer_normal_cover.json')]:
    program=CODE/'MAPS/code'/name
    original=ROOT/'sources/returns/S6_04_MAPS_MANIFOLDS/code'/name
    programs.append(dict(program='MAPS/code/'+name,program_sha256=sha(program),
                         original_sha256=sha(original),mathematical_program_unchanged=sha(program)==sha(original),
                         output='MAPS/code/'+output,output_sha256=sha(CODE/'MAPS/code'/output),
                         exit_code=0,execution_scope='All cases hard-coded in the original program; actual independent rerun completed.',**ACTOR))
reruns=json.loads((CODE/'selected_reruns.json').read_text())
for row in programs:
    if not any(x.get('program')==row['program'] and x.get('date')==row['date'] for x in reruns):reruns.append(row)
(CODE/'selected_reruns.json').write_text(json.dumps(reruns,ensure_ascii=False,indent=2)+'\n')
(OUT/'kummer_full_checks.json').write_text(json.dumps(dict(event=event,per_result=rows,reruns=programs),ensure_ascii=False,indent=2)+'\n')

# The inventory extractor originally skipped paragraphs headed Conclusion.
# Locate them without inferring that their downstream proofs have been read.
blocks_path=OUT/'source_blocks.json'
blocks=json.loads(blocks_path.read_text())
p=ROOT/'sources/returns/S6_04_MAPS_MANIFOLDS/sections/fourfolds.tex'
lines=p.read_text().splitlines()
for key,start,end in [('E.2.4',625,647),('F.2.4',1213,1236),('F.3.3',1238,len(lines))]:
    block=dict(id=key,file=str(p.relative_to(ROOT)),start_line=start,end_line=end,text='\n'.join(lines[start-1:end]))
    if not blocks.get(key):blocks[key]=[block]
blocks_path.write_text(json.dumps(blocks,ensure_ascii=False,indent=2)+'\n')

working=json.loads((OUT/'working_results_inventory.json').read_text())
for row in working:
    if row['source_id']=='cusp-cover-global-scope':
        row['taken_over_by']='MAPS:C.1.3; MAPS:C.1.4; MAPS:C.1.5'
        row['overlap_status']='Earlier limitation superseded by checked full smooth-source obstruction and normal-singular-source globalization; preserve the earlier statement with its source date.'
        row['current_unresolved_proof_gaps']=[]
    if row['source_id']=='cusp-cover-extension-theorem':
        row['taken_over_by']='MAPS:C.1.1'
        row['overlap_status']='Same local result; preserve corrected working proof and distinct final proof transferring freeness/properness through the power map.'
(OUT/'working_results_inventory.json').write_text(json.dumps(working,ensure_ascii=False,indent=2)+'\n')
keys=list(dict.fromkeys(k for row in working for k in row))
with (OUT/'working_results_inventory.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=keys);w.writeheader()
    for row in working:w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in row.items()})
print(json.dumps({'C_full_proofs':len(rows),'exact_reruns':len(programs),'missing_conclusion_locators_filled':3},indent=2))
