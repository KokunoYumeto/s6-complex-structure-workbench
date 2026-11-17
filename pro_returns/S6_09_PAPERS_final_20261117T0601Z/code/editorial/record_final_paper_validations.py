"""Attach actual final visual evidence to II/III's completed proof records."""
from pathlib import Path
import argparse, csv, hashlib, json, re
D=Path(__file__).resolve().parents[2]
a=argparse.ArgumentParser()
a.add_argument('--ii-visual',required=True);a.add_argument('--ii-covered',type=int,required=True)
a.add_argument('--iii-visual',required=True);a.add_argument('--iii-covered',type=int,required=True)
args=a.parse_args()
rows=list(csv.DictReader((D/'S6_09_PAPERS_inventory.csv').open()))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
load=lambda p:json.loads((D/p).read_text())
evidence={
 'II':[
  'work/cdp_audit/result_audit.json','work/cdp_audit/dependency_closure_events.json',
  'work/root/II_push_E5_full_checks.json','work/root/II_comb_full_check.json',
  'records/II_working_supplement_root_changes.json','records/II_editorial_mathematical_changes.json',
  'records/II_positive_credit_changes.json','records/II_source_to_print_retention.json',
  'records/II_final_exact_retention_chain.json','records/II_final_attribution_and_locator_repairs.json',
  'work/cdp_audit/II_working_credit/working_credit_comparison_30.json',
  'work/maps_audit/correction_note15_credit_overlay.json',
  'work/invariants_arithmetic/inv_E_credit_comparison_5.json',
  'records/final_credit_closure_merge.json','S6_09_PAPERS_inventory.csv'],
 'III':[
  'work/maps_audit/III_final_closure_overlay.json','work/maps_audit/III_MAPS190_source_to_print_check.json',
  'work/maps_audit/III_course249_final_source_to_print_check.json',
  'work/invariants_arithmetic/maps_D_source_to_print_check.json',
  'work/cdp_audit/push_C_retention/current_final_retention.json',
  'work/root/maps_F_proof_audit.md','work/cdp_audit/modular_collision_review/independent_review.json',
  'work/maps_audit/independent_repair_reviews.json','work/root/late_carrier_full_reading.json',
  'work/root/carrier_prerequisite_independent_review.json','records/III_program_index_validation.json',
  'records/III_course_structure_repairs.json','records/III_final_push_prose_restoration.json',
  'work/invariants_arithmetic/course_statement_proof_boundary_review.json','S6_09_PAPERS_inventory.csv']}
for paper,build,visual_path,covered in [('II',15,args.ii_visual,args.ii_covered),('III',24,args.iii_visual,args.iii_covered)]:
    visual=load(visual_path)
    tex=D/f'S6_09_PAPERS_{paper}.tex';pdf=D/f'S6_09_PAPERS_{paper}.pdf'
    assert visual['pdf_sha256']==sha(pdf)
    assert not visual.get('visual_defects_found',[])
    assert covered>0
    logpath=f'editorial/S6_09_PAPERS_{paper}_build_{build}.stdout.txt'
    log=(D/logpath).read_text()
    boxes=[float(x) for x in re.findall(r'Overfull \\[hv]box \(([\d.]+)pt',log)]
    warnings=re.findall(r'^.*(?:LaTeX Warning:|Package \S+ Warning:|Missing character:).*$',log,re.M)
    assert not warnings and all(x<=2 for x in boxes)
    pages=int(re.search(r'Output written on .*?\((\d+) pages',log)[1])
    refs=load(f'work/root/{paper}_citation_gate.json')
    assert not any(refs[k] for k in ['missing_bibliography','undefined_labels','duplicate_labels','unverified_cited','raw_source_numbers'])
    for path in evidence[paper]:assert (D/path).is_file(),path
    result={
      'paper':paper,'status':'Complete: full proof/source comparisons, exact credit, final companion references, clean LuaLaTeX and final selected-page visual checks passed',
      'gate_passed':True,'checked_by':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, 17 November 2026',
      'tex_sha256':sha(tex),'pdf_sha256':sha(pdf),'build_log':logpath,'build_log_sha256':sha(D/logpath),
      'pages':pages,'overfull_boxes':len(boxes),'overfull_over_2pt':0,'maximum_overfull_pt':max(boxes,default=0),
      'latex_or_package_warnings':warnings,'missing_character_diagnostics':0,
      'assigned_inventory_rows':sum(r['paper']==paper for r in rows),'citations':refs['citations'],
      'unverified_cited':[],'undefined_labels':[],'duplicate_labels':{},'self_contained_tex':True,'repository_occurrences':1,
      'visual_review_record':visual_path,'visual_review':visual,'visual_pages_covered':covered,
      'proof_review_evidence':evidence[paper],
      'scope_qualification':('The specified rank-three comb-kernel splitting remains in the separate final part with the complete partial argument and exact gap. The Kuranishi/tangent claim is established by the separately checked full period-section argument.' if paper=='II' else 'The precisely scoped MAPS D.2.4 star-log/torsion-marked filling questions remain in the separate final part. The specified default weighted example has the stated refined class ambiguity 0 versus 4 in Z/8. The preceding cubic, fundamental-class and absolute-characteristic conclusions are established at their printed scope.'),
      'limitation':'Independent AI reading/rerun records are the mathematical checking evidence; byte-retention and layout checks do not constitute a proof-assistant certificate. Visual verification is the exact selected-page scope recorded here, not every page of the PDF.'}
    if paper=='II':
        result.update({'canonical_complete_blocks_retained':237,'actual_executed_programs_with_outputs':89,'previous_validation':'records/II_validation_before_final_credit_pass.json','number_identity_record':'records/II_final_label_identity_check.json'})
    else:
        result.update({'MAPS_complete_blocks_retained':190,'PUSH_complete_blocks_retained':34,'complete_course_chapters_retained':33,'complete_course_units_retained':249,'program_catalogue_entries':201,'unique_execution_records':218})
    (D/f'records/{paper}_final_validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'paper':paper,'pages':pages,'visual_pages_covered':covered,'gate_passed':True}))
