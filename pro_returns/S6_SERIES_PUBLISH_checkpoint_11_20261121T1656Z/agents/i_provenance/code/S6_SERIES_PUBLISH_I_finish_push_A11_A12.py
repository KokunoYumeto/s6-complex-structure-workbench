from pathlib import Path
import json,hashlib,datetime,csv
B=Path('/workspace/scratch/653608133b22');A=B/'work/agents/i_provenance';p=B/'work/S6_SERIES_PUBLISH_I.tex';s=p.read_text();now=datetime.datetime.now(datetime.timezone.utc).isoformat();h='cab50d1206590b4b';group='eg:publish-iprovenance-pushA11A12-preread-'+h
old=r'''Its exceptional
curve has the two affine charts of the total space of
$\mathcal O_{\mathbb P^1}(-1)\oplus
\mathcal O_{\mathbb P^1}(-1)$, as follows by setting $x=za$ on
one chart and $z=xb$ on the other. The two normal coordinates
transform by the reciprocal affine coordinate.'''
new=r'''For $u\ne0$, put $Y=y/u$, so the equation is $xY=zv$.
The resolution associated with the diagonal $[e_1,e_2]$ has charts
\[
 (v,Y,a)\longmapsto(av,uY,aY,v),\qquad
 (x,z,b)\longmapsto(x,ubz,z,bx)
\]
in the coordinates $(x,y,z,v)$. On their overlap,
$b=a^{-1}$ and $(x,z)=a(v,Y)$. The character $a=x/v$ has
valuation $y_1+y_2-h_q$, so these are exactly the two triangles
separated by $[e_1,e_2]$. The exceptional curve is the zero
section in the two normal coordinates. Their transition is
multiplication by $a$, giving
$\mathcal O_{\mathbb P^1}(-1)\oplus\mathcal O_{\mathbb P^1}(-1)$.'''
assert s.count(old)==1,s.count(old)
guard={'source':str(p),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'created_utc':now,'changes':[{'id':'I-push-A12-selected-diagonal-charts','old':old,'new':new,'expected_count':1,'reason':'Frozen independent derivation and fresh exact unimodular cone-ray/incidence computation identify the selected [e1,e2] diagonal. Old x=za charts belong to the other diagonal; the theorem statement is unchanged.'}],'coordination':'Topology batch3 combines this proof; apply this correction there instead of separately if the old paragraph is subsumed.'}
(A/'S6_SERIES_PUBLISH_I_push_A12_selected_diagonal_guard.json').write_text(json.dumps(guard,indent=2,ensure_ascii=False)+'\n')
error={'error_event_id':'ce:publish-iprovenance-pushA12-selected-diagonal-error-'+h,'statement_id':'push:src:A.1.2','scope':'Proof Step7 selected-diagonal chart identification only','old_false_intermediate_claim':'The x=za/z=xb charts are the selected [e1,e2] diagonal resolution.','computed_old_edge':[[0,0,1],[1,1,1]],'computed_selected_edge':[[0,1,1],[1,0,1]],'correction':'Use Y=y/u; (v,Y,a)↦(av,uY,aY,v), (x,z,b)↦(x,ubz,z,bx), with b=1/a and (x,z)=a(v,Y).','actual_morphism_between_resolutions':'Both contract to xY=zv. The common O(-1,-1) over the Segre P1×P1 records both rank-one matrix factors; its two projections contract opposite rulings.','theorem_statement_unchanged':True,'refined_statement_id':None,'mathematical_check_credit':'Included in the targeted A1.2 check and its fresh computation; this error record is not an extra independent mathematical check.','evidence_group':group,'record':str(A/'S6_SERIES_PUBLISH_I_push_A11_A12_check.md')}
(A/'S6_SERIES_PUBLISH_I_push_A12_selected_diagonal_ERROR_EVENT.json').write_text(json.dumps(error,indent=2,ensure_ascii=False)+'\n')
fields=['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group'];who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited (no separate numeric setting exposed), S6_SERIES_PUBLISH/provenance_inventory';rows=[]
def row(id,typ,outcome,event,source_type):
 rows.append(dict(zip(fields,[id,'2026-11-21',who,typ,outcome,event,'S6_SERIES_PUBLISH_I_targeted_preread',str(A/'S6_SERIES_PUBLISH_I_push_A11_A12_check.md'),str(len(rows)+1),source_type,group])))
row('push:src:A.1.1','targeted proof check','PASS full scope: fan intersections including collapsed faces, saturated integral semigroup, exact chart and q=zv independently derived and frozen before target proof; normality method differs from printed monoid subtraction.','ce:publish-iprovenance-pushA11-preread-'+h,'targeted proof check')
row('push:src:A.1.2','targeted proof check','PASS WITH PROOF CORRECTION: complete exact plumbing, Hausdorff/proper compact core, joint flatness, Q conductor, punctured quotient, selected contraction and O(-1)^2 derived before printed proof. Old Step7 charts select opposite diagonal; corrected explicit incidence maps preserve the theorem statement.','ce:publish-iprovenance-pushA12-preread-'+h,'targeted proof check')
row('push:src:A.1.1','computation or formal certificate','PASS fresh exact generator-lattice minors and primitive relation, base Groebner normal form and fixed-u Hessian. One newly written execution shared with A1.2; no attached program rerun.','ce:publish-iprovenance-pushA11-exact-'+h,'new computation')
row('push:src:A.1.2','computation or formal certificate','PASS selected-diagonal correction by fresh unimodular inverse cone-ray extraction, exact polynomial incidence substitutions and O(-1)^2 transition. Old common edge[(0,0,1),(1,1,1)] versus selected[(0,1,1),(1,0,1)]. Shared execution with A1.1.','ce:publish-iprovenance-pushA12-exact-'+h,'new computation')
with (A/'S6_SERIES_PUBLISH_I_push_A11_A12_CHECK_EVENTS.tsv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
receipt={'created_utc':now,'source':str(p),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'preread':json.loads((A/'S6_SERIES_PUBLISH_I_push_A11_A12_preread_receipt.json').read_text()),'read_complete_printed_proofs':True,'read_complete_proposed_correction':True,'outcomes':{'push:src:A.1.1':'PASS full statement','push:src:A.1.2':'PASS unchanged statement, Step7 selected-diagonal proof correction'},'event_rows':4,'independent_executions':1,'evidence_group':group,'error_record':str(A/'S6_SERIES_PUBLISH_I_push_A12_selected_diagonal_ERROR_EVENT.json')}
(A/'S6_SERIES_PUBLISH_I_push_A11_A12_check_receipt.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n')
print('4 check associations,1 evidence group; separate scoped error record;1 guarded correction')
