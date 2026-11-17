from pathlib import Path
import json,hashlib,csv
D=Path(__file__).resolve().parents[2];ROOT=D.parent;W=D/'work/maps_audit'
META={'reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date':'2026-11-17'}
def rd(n):return json.loads((W/n).read_text())
def save(n,x):(W/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
credit_fields=['found_in_AC26','found_in_E26','found_in_DGKX_v1','found_in_DGKX_v2','found_elsewhere','credited_to']
working=rd('working_results_inventory.json');events={r['event_id']:r for r in rd('check_events.json')};events.update({r['event_id']:r for r in rd('working_carrier_full_checks.json')})
peer={r['source_id']:r for r in json.loads((D/'work/cdp_audit/carrier_credit/working_credit_inventory_overlay_39.json').read_text())}
selected=[r for r in working if r['source_id'] in peer]
assert len(selected)==30
kummer=rd('kummer_full_checks.json');carrier=rd('carrier_nullhomotopy_source_chain.json');reviews=rd('independent_repair_reviews.json');pt=rd('pt_relative_bordism_repair_record.json')
closures=[]
for r in selected:
    sid=r['source_id'];es=[events[e] for e in r.get('check_event_ids',[]) if e in events and e.startswith('new-')]
    assert es,sid
    deps=[];repairs=[];outcome=r['check_outcome'];scope='The exact statement and its full supplied proof, with the retained qualifications; no smooth complex S12/S24 construction or retained-angle nullhomotopy is inferred.'
    if sid.startswith('cusp-cover-'):
        deps=[{'record':'deliverables/work/maps_audit/paperI_construction_full_checks.json','scope':'All original marked toric-cusp, period and quotient-geometry prerequisites fully read; exact foundation primary checks retained.'},{'record':'deliverables/work/maps_audit/kummer_full_checks.json','scope':'All five MAPS C.1.1–C.1.5 proofs read: periodic-fan smoothness, smooth-source global obstruction, all-N orbit bound, and connected normal-singular-source global finite-flat extension.'}]
        repairs=['deliverables/work/maps_audit/kummer_compact_chart_repair.tex']
        outcome='Full local proof and final-run global comparison closed. C.1.3 excludes the indicated smooth-source global extension; C.1.5 constructs a different connected normal, generally singular, finite-flat source. The original local-only scope remark is retained as the earlier source state and is followed by these precise later conclusions.'
        scope='The direct local map has degree N^3; its base-changed factor degree N^2 is quasi-etale and nonflat on the identified strata. The later singular global construction does not turn that factor into a smooth-source cover.'
    if sid=='cusp-spec-globalization-obstruction':
        repairs=['deliverables/work/maps_audit/globalization_deck_group_correction.tex','deliverables/work/maps_audit/paperI_circle_quotient.tex']
        deps.append({'record':'deliverables/work/maps_audit/paperI_circle_quotient_manifest.json','scope':'Actual triangle deck group versus universal cover and literal invariant circle quotient are fully proved in Paper I; no duplicate full proof is required in III.'})
    if sid in ['cusp-cone-target-homotopy-types','cusp-cone-explicit-carriers']:
        repairs.append('deliverables/work/maps_audit/carrier_three_complex_wedge.tex')
        deps.append({'record':'deliverables/work/maps_audit/references_verified.json#Hatcher2002','scope':'Absolute and relative Hurewicz Theorem4.32 pp366–367 and homological Whitehead Corollary4.33 pp367–368 opened with full proofs. The supplementary wedge proof constructs a:S2→C and a relative-Hurewicz lift b:S3→C; their wedge is a simply connected integral homology equivalence. It is a classical rederivation, not a new source theorem or a new inventory row.'})
    if 'new-working-angle-forgotten-one-copy-null-20261117' in r.get('check_event_ids',[]):
        repairs.append('deliverables/work/maps_audit/carrier_nullhomotopy_by_extension.tex')
        deps.append({'record':'deliverables/work/maps_audit/carrier_nullhomotopy_source_chain.json','scope':carrier['scope'],'independent_check':carrier['parent_independent_check']})
    if Path(r['source_file']).name in ['cusp_s12_carrier_homotopy.tex','cusp_sphere_route_strengthening.tex']:
        deps.append({'record':'deliverables/work/maps_audit/carrier_source_checks.json','scope':'Original Hatcher Cor4.24 exact stable inequalities; author Chapter5 Th5.41 and suspension diagram; published Isaksen–Wang–Xu Table1; Milnor§7 ThB/Lemma4 exact framed-relative scope. These close the recorded Freudenthal/stem/nullbordism prerequisites; group-order and framed-torus proofs remain distinct.'})
    if sid=='G2-8':
        deps.append({'record':'deliverables/work/maps_audit/working_carrier_full_checks.json#new-working-G2-homotopy-full-20261117','scope':'Full fixed-orientation J-homotopy proof: SO6/U3=CP3, pi6(CP3)=0, relative section obstruction and smooth approximation. The correct octonionic orientation is the negative of the course-labelled field. AC26 exact positive prior credit is in the peer G2 comparison.'})
    credit={k:peer[sid][k] for k in credit_fields if k in peer[sid]}
    if 'found_in_DGKX_v2' not in credit:
        try:credit['found_in_DGKX_v2']=json.dumps(json.loads(credit['found_elsewhere'])['DGKX_v2'],ensure_ascii=False)
        except (KeyError,TypeError,json.JSONDecodeError):pass
    cr={**META,'source_run':r['source_run'],'source_id':sid,'paper':'III','printed_label':peer[sid].get('printed_label',r.get('printed_label')),'source_file':r['source_file'],'source_sha256':r['source_sha256'],'full_receiving_proof_read':True,'source_statement_range':[r['start_line'],r['end_line']],'source_full_proof_range':[r.get('proof_start_line'),r.get('proof_end_line')],'receiving_read_records':es,'current_check_event_ids':[e['event_id'] for e in es],'source_dependency_status':'Closed in the precise recorded scopes; historical earlier reservations retained below.','exact_dependency_closure':deps,'repair_files':repairs,'check_outcome':outcome,'your_check':' | '.join(e['event_id']+': '+e['scope'] for e in es),'limitation':scope,'credit_record':'deliverables/work/cdp_audit/carrier_credit/working_credit_inventory_overlay_39.json#'+sid,'historical_audit_state':{k:r.get(k) for k in ['your_check','check_outcome','recorded_checks','check_event_ids']},**credit}
    closures.append(cr)
    r.setdefault('historical_closure_states',[])
    if not any(t.get('event')=='final-carrier-closure-20261117' for t in r['historical_closure_states']):r['historical_closure_states'].append({'event':'final-carrier-closure-20261117','previous_check_outcome':r['check_outcome']})
    r['check_outcome']=outcome;r['current_final_closure']='deliverables/work/maps_audit/III_working30_final_closure.json#'+sid
save('III_working30_final_closure.json',closures);save('working_results_inventory.json',working)
# The six actual inventory repair units retain their identities. The wedge
# supplement is accounted for under cusp-cone-target-homotopy-types above.
recommend=rd('reviewed_repair_label_recommendations.json')['rows']
nullcredit=next(r for r in rd('maps60_credit_comparison.json') if r['source_id']=='B.3.2')
ptcredit=next(r for r in rd('course249_credit_comparison.json') if r.get('group')=='pt')
repaircredits=[];repairclosure=[]
for r in recommend:
    sid=r['source_id'];ispt=sid.startswith('MAPS-AUDIT-PT-');base=ptcredit if ispt else nullcredit
    text=(W/r['proof_file']).read_text();sha=hashlib.sha256(text.encode()).hexdigest()
    credit={k:base[k] for k in credit_fields if k in base}
    if ispt:
        credit['found_elsewhere']='Classical relative embedding and tangent/normal framing comparison, written here with full Gram-matrix, collar and block-order formulas. Milnor1965 Differential Topology from the Differentiable Viewpoint §7, TheoremB and Lemma4, pp42–50 gives the opened embedded framed-bordism/collapse correspondence; it is not asserted to print these specific RB.1–RB.6 formulas. Full coordinate derivations and the independent root review are printed and preserved.'
        credit['credited_to']='Pontryagin and Thom for the classical correspondence; Milnor for the opened explicit framed-bordism formulation; the writing-stage bridge supplies the receiving relative-embedding and stable-framing coordinate proof.'
    else:
        credit['found_in_AC26']='AC26 original Corollary4.8 p30 supplies the null base meridian and toric cusp inclusion used by the application. The generic suspension-extension lemma and these specified angle-forgotten one-copy maps are not stated in that opened scope. Full-file nullhomotopy/cofiber/wedge searches and their inspected contexts are retained.'
        credit['found_elsewhere']='Classical lifting and homotopy-extension reasoning is rederived in full: a torus-valued map with the same pi1 homomorphism as an extending map has a real-valued difference lift; first interpolate at fixed radial height, then move height to the collapsed endpoint. The actual no-drift disc and quotient inclusion are checked against the complete original cusp construction. The separate original framed-torus proof remains retained; no worldwide absence or priority claim is made.'
        credit['credited_to']='AC26 for the underlying complex construction and actual toric disc; classical covering-space and homotopy-extension principles for the method; this writing-stage coordinate homotopy closes the specified former one-copy circle question. It does not apply to retained-angle maps.'
    rc={**META,'source_run':'WRITING_REPAIR','source_id':sid,'printed_label':r['printed_label'],'proof_file':'deliverables/work/maps_audit/'+r['proof_file'],'proof_sha256':sha,'scope':r['relationship'],**credit,'bounded_comparison_scope':base.get('bounded_comparison_scope','Four version-distinct attached baseline files plus 43 other unique attached source files were searched by the recorded thematic terms; selected relevant mathematical hits and separately scoped primary sources were read. No exhaustive worldwide absence claim.'),'reused_actual_search_evidence':{'record':'deliverables/work/maps_audit/course249_credit_comparison.json#'+ptcredit['source_id'] if ispt else 'deliverables/work/maps_audit/maps60_credit_comparison.json#B.3.2','search_log':'deliverables/work/maps_audit/course249_credit_search_log.json' if ispt else 'deliverables/work/maps_audit/maps60_credit_search_log.json','search_group':'pt' if ispt else 'null_and_cone','scope':'These actual completed searches concern precisely the same classical PT method or specified carrier maps; they are reused, not claimed newly executed for each writing-stage lemma.'},'historical_credit_status':'Scoped comparison/full literature comparison pending in the earlier writing-stage row; now replaced by this bounded, explicit comparison without deleting that earlier state.'}
    repaircredits.append(rc)
    independent=pt['independent_check'] if ispt else carrier['parent_independent_check']
    repairclosure.append({**META,'source_run':'WRITING_REPAIR','source_id':sid,'paper':'III','printed_label':r['printed_label'],'full_receiving_proof_read':True,'source_blocks':[{'file':rc['proof_file'],'source_sha256':sha,'scope':'Complete proof of the labelled unit, with the retained surrounding definitions and coordinate formulas.'}],'current_check_event_ids':[pt['event_id'] if ispt else 'new-working-angle-forgotten-one-copy-null-20261117',independent['event_id']],'receiving_read_records':['deliverables/work/maps_audit/pt_relative_bordism_repair_record.json' if ispt else 'deliverables/work/maps_audit/carrier_nullhomotopy_source_chain.json'],'independent_review':independent,'source_dependency_status':'Closed at the exact scope of this coordinate bridge; no stable-group computation is inferred from the bridge.' if ispt else 'Closed for the angle-forgotten carrier, including the actual no-drift disc and the corrected closed codimension-zero neighbourhood hypothesis.','check_outcome':independent['outcome'],'credit_record':'deliverables/work/maps_audit/III_repair6_credit_comparison.json#'+sid,**credit,'historical_audit_state':rc['historical_credit_status'],'limitation':independent.get('excluded_scope',independent.get('precise_scope'))})
assert len(repaircredits)==6
save('III_repair6_credit_comparison.json',repaircredits);save('III_repair6_final_closure.json',repairclosure)
# Final combined overlay is rebuilt from the stable component files and new
# explicitly scoped components; no peer records or top-level inventory edited.
combined=rd('III_maps60_final_closure.json')+rd('III_course249_final_closure.json')+rd('III_pushC35_final_closure.json')+closures+repairclosure
assert len(combined)==len({(r['source_run'],r['source_id']) for r in combined})==380
save('III_final_closure_overlay.json',combined)
summary=rd('III_final_closure_summary.json');summary.update({'total_rows':380,'original_working_carrier_rows':30,'writing_repair_rows':6,'common_reference_repairs':'deliverables/work/maps_audit/III_course_common_reference_repairs.json','new_closure_components':['III_working30_final_closure.json','III_repair6_final_closure.json'],'wedge_inventory_placement':'Supplementary classical proof retained under existing cusp-cone-target-homotopy-types; no new inventory identity.'});save('III_final_closure_summary.json',summary)
# Mirror the existing CSV schema without dropping the original historical fields.
for name in ['working_results_inventory','results_audit']:
    jp=W/(name+'.json');cp=W/(name+'.csv')
    if not cp.exists():continue
    with cp.open(newline='') as f:cols=next(csv.reader(f))
    vals=json.loads(jp.read_text())
    with cp.open('w',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=cols,extrasaction='ignore');wr.writeheader()
        for r in vals:wr.writerow({k:(json.dumps(r[k],ensure_ascii=False) if isinstance(r.get(k),(dict,list)) else r.get(k,'')) for k in cols})
print('Combined closure:380 rows =60 MAPS+249 course/provider+35 PUSH C+30 original working+6 writing repairs.')
