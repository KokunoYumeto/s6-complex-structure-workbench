from pathlib import Path
import json,hashlib,datetime,csv
p=Path('/workspace/scratch/6c4e6df38b6d/S6_SERIES_GRIND_work');d=p/'audit_corrections';s=(p/'parts/V.body.linked.tex').read_text();pre='code/current_audits/audit_corrections/code/reconstruct_V_cusp_06';patch=[]
def add(old,new):
 assert s.count(old)==1,(s.count(old),old[:80]);patch.append({'label':'night:P1.11','old_text':old,'new_text':new,'reason':'Fresh complete reconstruction of the displayed finite cusp incidence/Smith/collapse scope; no replay of absent historical programs or global P1.19 certificate inferred.'})
add(r'''The program
\texttt{cusp\_complex.py} enumerates the $26$ simplex classes, all
$74$ codimension-one incidences, and exports every matrix, basis, and
Smith certificate to \texttt{cusp\_complex.json}.''',r'''The exact reconstruction in
\path{'''+pre+r'''.py} enumerates all $26$ simplex classes and
$74$ codimension-one incidences. Its JSON output supplies every integral
quotient and right inverse, each differential, cycle basis, incoming
matrix, homology projection and marked collapse matrix. All Smith
identities and unimodular basis changes are checked by exact multiplication.''')
add(r'''The newly authored program
\path{P1_11_collapse_fresh.py} in \path{code/continuation_V/}
computes the induced maps on integral cycle and quotient bases.''',r'''The program \path{'''+pre+r'''.py} constructs the induced maps
on integral cycle and quotient bases from the face projections and the
Poincar\'e-dual Alexander--Whitney formula in step 9. Its complete
integral output is \path{'''+pre+r'''.json}.''')
add(r'''Tensoring with an angular exterior vector and applying (1.11.1)
gives the matrices exported by \texttt{cusp\_marked\_collapse.py}.''',r'''Tensoring with an angular exterior vector and applying (1.11.1)
gives the marked matrices exported in
\path{'''+pre+r'''.json}. Their source basis is the ordered exterior
basis $(a_1,a_2,a_3,b_1,b_2,b_3)$; the output gives the integral
target homology projections and all Smith basis maps.''')
# A fourth guard states what the fresh exact finite arithmetic establishes.
add(r'''and every group is free.  Support leaves only the possible higher
differential $d_2:E^2_{3,0}\to E^2_{1,1}$.''',r'''and every group is free. The reconstructed incoming Smith matrices
have only unit nonzero factors and reproduce every entry of this table.
Support leaves only the possible higher differential
$d_2:E^2_{3,0}\to E^2_{1,1}$.''')
(d/'V_P111_guarded_patches_06.json').write_text(json.dumps(patch,indent=2))
result=json.loads((d/'code/reconstruct_V_cusp_06.json').read_text());now=datetime.datetime.now(datetime.timezone.utc).isoformat()
receipt={'utc':now,'program':'audit_corrections/code/reconstruct_V_cusp_06.py','program_sha256':hashlib.sha256((d/'code/reconstruct_V_cusp_06.py').read_bytes()).hexdigest(),'output_sha256':hashlib.sha256((d/'code/reconstruct_V_cusp_06.json').read_bytes()).hexdigest(),'assertions':result['assertions'],'status':result['status'],'full_receiving_proof_read':True,'exposure':'All nine printed proof steps read before this fresh computation. No new whole before-proof derivation is claimed.','mathematical_scope':'26simplex classes,74incidences, primitive integer quotient/right-inverse maps, allE1differentials, freeE2groups, PD/AW actual marked collapse, monodromy annihilation, exact ranks/primitive image. Geometry is the explicit stratified moment/deck/log-collapse proof; higher differential is killed by the actual angular identity section.','remaining':'Four body guards await root integration; current changed-page image gate remains root-owned. Full global P1.19 complex is being reconstructed separately.','historical_scope':'No absent producer imported; no old JSON treated as present.','patch_count':len(patch),'source_sha256':hashlib.sha256(s.encode()).hexdigest()}
(d/'V_P111_receiving_receipt_06.json').write_text(json.dumps(receipt,indent=2))
ass=json.loads((d/'row_assessments.json').read_text());ass['night:P1.11']={'confidence_state':'high; full receiving geometry and fresh finite cusp calculation agree','confidence_line':'All nine current proof steps were checked. A new complete186-assertion exact reconstruction supplies every finite incidence/Smith/PD-collapse calculation, with homology(1,3,9,9,10,3,1) and primitive collapse image ranks(1,3,9,9,9,3,1).','independent_routes':'Explicit moment/face/deck homeomorphism and logarithmic actual-collapse comparison in the full receiving proof; fresh reconstructed26simplex/74incidence angular complex with unit Smith maps; actual marked PD/Alexander–Whitney collapse and exterior monodromy kernel comparison. This new code is post-receiving and does not claim a new blind geometric proof.','remaining_risk':receipt['remaining']+' Retained exact Cox12.2.5p571 and Achinger–Ogus4.1.1pp480–482 source readings are used at their stated hypotheses; fresh source reopening not awarded here.','format_check':None,'layout_check':None,'completion_state':None};(d/'row_assessments.json').write_text(json.dumps(ass,indent=2))
f=d/'CHECK_EVENTS.tsv';ev=list(csv.DictReader(f.open(),delimiter='\t'));actor='GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited from root (not separately exposed), S6_SERIES_GRIND/corrections_audit';new=[]
for typ,scope in [('targeted proof check','Read all9current P1.11 proof steps: exact marked stratified unit-removal, actual moment and face/deck maps and inverse, logarithmic angular collapse, filtration/section argument, and primitive-image inference. No new whole before-proof derivation claimed.'),('computation or formal certificate','PASS186fresh assertions in reconstruct_V_cusp_06.py: full26simplex/74incidence integral angular quotient complex, allE2Smith groups, actual PD/AW marked collapse matrices, monodromy annihilation, primitive images and every asserted rank. All basis maps and matrices preserved. This does not establish P1.19globalchain.')]:
 out=scope+' Evidence: audit_corrections/V_P111_receiving_receipt_06.json and code/reconstruct_V_cusp_06.json.';eid='s6sg:'+hashlib.sha256((typ+out).encode()).hexdigest()[:20];new.append({'statement_id':'night:P1.11','date':now,'who':actor,'type':typ,'outcome':out,'event_id':eid,'phase':'S6_SERIES_GRIND'})
seen={e['event_id'] for e in ev};new=[e for e in new if e['event_id'] not in seen]
with f.open('w',newline='') as h:w=csv.DictWriter(h,fieldnames=ev[0].keys(),delimiter='\t');w.writeheader();w.writerows(ev+new)
print(json.dumps({'patches':4,'events_total':len(ev)+len(new),'own_rows':len(ass),'receipt':str(d/'V_P111_receiving_receipt_06.json')}))
