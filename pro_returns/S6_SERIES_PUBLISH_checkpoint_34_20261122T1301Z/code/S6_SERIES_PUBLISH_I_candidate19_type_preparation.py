#!/usr/bin/env python3
"""Bind25 candidate19 source dispositions to actual application/build; no status writes."""
from pathlib import Path
import collections
import copy
import csv
import datetime
import hashlib
import io
import json
import re
import fitz
from S6_SERIES_PUBLISH_I_candidate18_type_preparation import core_hash, types_of, bibliography
from S6_SERIES_PUBLISH_I_candidate17_combined import math, displays, refs

R=Path(__file__).resolve().parents[1]
O=R/'agents/i_cont_edits'
sha=lambda b:hashlib.sha256(b).hexdigest()
PRIOR='agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate18_type_closure_preparation.json'
PRIOR_SHA='527c26a57e40204709ad4880756a688ef900de84b9dfa12cb2f91276832078b2'
APPLY='agents/continuation_infra/S6_SERIES_PUBLISH_I_candidate18_combined_apply_receipt.json'
APPLY_SHA='6f4f76cb0a75bc2eaa6603bcf0ed6c1bb31100e947c5452301e7d3b076edce1b'
AG='records/S6_SERIES_PUBLISH_I_candidate19_source_AG_binding.json'
AG_SHA='16ec6e52fc3f1be46b740933962e3c49443239fbbd4016450a6eed5e74ae9b1d'
MATRIX='agents/continuation_infra/S6_SERIES_PUBLISH_I_candidate17_bibliography_audit_matrix_final_v3.json'
MATRIX_SHA='6c38d39d983e7080cdb6ecee1bac5a9a49284fdad4b36274c8ec4ab0481a66c0'
SOURCE='f9e40fb592eb7f5c6d48070ba207e93d5b48ca71432176202041b88dd01278f7'
PDF='e7a48c79d7bc5588f272b7d138f82fef8bbc504e86626f06a01c0bd86de32f7f'
CORE=['change_id','type','statement_id','old_text','new_text','reason']


def read(p):return json.loads((R/p).read_text())


def ev(p,scope,expected=None):
 h=sha((R/p).read_bytes())
 if expected:assert h==expected,(p,h,expected)
 return {'path':p,'sha256':h,'scope':scope}


def review(typ,old,new):
 ids=', '.join(c['guard_id'] for c in new)
 if typ=='D02':
  return ('Four applied guards resolve the candidate18 defensive-tail findings. The marked-period proof retains its finite exceptional set, dense-core equivariance, finite orbit and torsion witness; the branch-resolution proof retains the alternating summand and positive orientation-local-system formulation; the log-torus proof retains its defined period lattice, exponentiation fact, valuation map and connecting-class obstruction. The leading-factor proof now states the existing exactly-once summation scope positively as a partition of the remaining indices into segments with the same257 boundaries, retaining the first10280 terms and all bounds. Only the repeated E/Y mentions explicitly named in the receipt are removed. Complete original/reworded proof readings and the exact current block matches support this disposition. Guards: '+ids+'.')
 if typ=='D06':
  return ('I18-prov-03 resolves the explicitly reopened stale locator in inv:B3.1. The source now names Definition2.1 through the existing def:common-conventions label; the complete receiving definition fixes the clockwise root generators, counterclockwise base meridians and endpoint identification. Its full definition text is unchanged and the actual candidate19 auxiliary file resolves the label to2.1,p18. The reader and root inspected the owning proof and target. The one added reference is declared, and all affine generator powers and group relations are retained. The earlier D06 closure and its reopening remain preserved as history.')
 if typ=='D08':
  return ('Nine applied guards resolve every recorded candidate18 pure method/closing recap in the bound review scopes: the vertical-bundle calculation, quadric–parabolic smoothing, Hopf anticanonical and coherent-direct-image argument, partial cusp filling, monomial degeneration, endpoint-period trace, and two Poincare-height passages. The earlier context-disposition audits and all346 actual candidate18 page readings remain bound. Each deletion has a complete source comparison and positive retained witnesses. The sole removed duplicate equation reference belongs to I18-root-05; its labelled equation and operative splitting proof remain. The p224 conventional closing sentence was expressly reconsidered under prompt section3.2 and removed by the final v3 guard; the operative p237 cited admissibility application remains. No conclusion is drawn from keyword absence alone. Guards: '+ids+'.')
 if typ=='D11':
  return ('I18-edits-06 resolves the reopened repeated finite-support scope comparison in push:src:B.4.13. The exact deletion is one final sentence of proofstep4, beginning The original finite-support argument. The preceding parabolic-axis consequence remains, together with the full first assertion, finite-image/equivariance/orbit proof, separate nonzero-normal-degree hypothesis and derivative/Abel–Jacobi calculation. The reopening record informally says final two sentences; its quoted before-text, approved guard and actual applied map all identify this one sentence. The current source matches the merged complete proof exactly. Prior scope-consolidation exceptions remain recorded in the immutable older dossiers.')
 if typ=='D23':
  return ('Six applied typography guards resolve the four Neron–Severi accent instances and the two visibly stretched paragraphs discovered in candidate18. The accents are restored in the section heading and complete D.1.4/D.1.7 contexts. The real-period inputs in ari:C.6.R2 are separated into paragraphs, retaining every row, T value, sign and bound; the monomial/acyclicity paragraph in push:src:E.2.1 gains one blank line. Actual private paragraph previews and complete source comparisons are bound in the approved input records. The candidate19 build reports no overfull boxes, unresolved references/citations, missing glyphs/fonts, repeated labels or duplicate destinations; this does not substitute for the separately pending whole-image reading. Guards: '+ids+'.')
 if typ=='D18':
  return ('The final root-reviewed bibliography matrixv3 still binds all117 complete current entries, with45 reviewed corrections and72 retained entries. The candidate18→19 batch changes no bibliography entry, citation key, publication field, DOI, version pin or cited-edition note. Exact current complete-entry hashes equal the matrix proposed-entry hashes, and the source-specific primary-record limitations remain preserved. The existing root review of all117 entries and final candidate18 bibliography-page coverage supply the contextual evidence; no new publication/DOI-absence assertion is made.')
 if typ=='D15':
  return (old+' The candidate18→19 changes leave the front matter and methodology text byte-identical; the current source scope is transported through the exact21-change map. The requested section4.3 rereading-event manifest, its deduplicated count update and the consequent section1.5/source-report/deposit rebinding remain explicit pending work. This row does not certify those future counts or their future source.')
 return (old+' This individually reviewed scope is carried to candidate19 by the actual21-change forward/inverse source map and the complete candidate18 reading record. No additional confirmed instance of this type appears among the current contextual findings. New candidate19 changed-page reading and final count/provenance binding remain separate; no keyword-absence or new independent proof credit is inferred.')


def main():
 prior=read(PRIOR);prior_e=ev(PRIOR,'Immutable candidate18 individually reviewed scopes and disclosed remaining findings.',PRIOR_SHA)
 rec=read(APPLY);rec_e=ev(APPLY,'Actual applied21-guard batch, exact maps and complete block comparisons.',APPLY_SHA)
 assert rec['mode']=='applied' and rec['before_source_sha256']==prior['source_sha256']
 assert rec['candidate18_pdf_sha256']==prior['pdf_sha256'] and rec['after_source_sha256']==SOURCE
 assert rec['mathematical_events_added']==0 and not rec['canonical_status_files_modified']
 sp=R/'S6_SERIES_PUBLISH_I.tex';lp=R/'S6_SERIES_PUBLISH_defects_I.tsv';cp=R/'CHECK_EVENTS.tsv'
 sb,lb,cb=sp.read_bytes(),lp.read_bytes(),cp.read_bytes();source=sb.decode()
 assert sha(sb)==SOURCE
 ledger_sha=sha(cb)
 # A subsequent append is an explicit pending provenance gate. It must never
 # be silently substituted for the ledger to which the actual source AG binds.
 application_ledger_sha=rec['check_ledger_sha256']
 rows_log=list(csv.DictReader(io.StringIO(lb.decode()),delimiter='\t'))
 old_n=rec['existing_defect_rows'];changes=rec['changes'];byid={x['guard_id']:x for x in changes}
 assert old_n==prior['unique_edit_rows']==2196
 assert len(rows_log)==rec['total_defect_rows']==2217 and len(changes)==rec['new_defect_rows']==21
 assert core_hash(rows_log[:old_n])==prior['defect_log_content_sha256']
 for n,c in enumerate(changes,old_n):
  row=rows_log[n];assert c['change_id']==row['change_id']==f'I-{n+1:05d}'
  assert [row[k] for k in CORE[1:]]==[c[k] for k in ['type','statement_id','old','new','reason']]
 inputs=read(rec['input_manifest']);inputs_e=ev(rec['input_manifest'],'Exact root approval of all21 active guards.',rec['input_manifest_sha256'])
 assert inputs['root_approved'] and inputs['approved_guard_count']==len(changes)
 assert rec['approved_inputs_sha256']==inputs_e['sha256'] and inputs['source_sha256']==prior['source_sha256']
 approved={}
 for item in inputs['guard_files']:
  ev(item['path'],'Approved complete guarded source comparison.',item['sha256'])
  d=read(item['path']);gs=d if isinstance(d,list) else d['guards'];assert len(gs)==item['count']
  for g in gs:
   c=byid[g['id']];assert c['old']==g.get('before',g.get('old')) and c['new']==g.get('after',g.get('new'))
   assert types_of(c['type'])==types_of(g['type']);approved[g['id']]=g
 assert set(approved)==set(byid)
 root_e=ev(inputs['root_review']['path'],'Root actually read every complete original owning context and all proposed differences.',inputs['root_review']['sha256'])
 root_review=read(root_e['path']);assert len(root_review['full_proof_comparisons'])==15
 coverage_e=ev(inputs['complete_coverage']['path'],'All346 candidate18 full images have actual-reading coverage.',inputs['complete_coverage']['sha256'])
 coverage=read(coverage_e['path']);assert coverage['all_pages_read'] and coverage['source_sha256']==prior['source_sha256'] and coverage['pdf_sha256']==prior['pdf_sha256']
 assert len(coverage['pages'])==346
 # Exact current source map, including the full prior continuation chain.
 chain=prior['source_transport']['applied_changes']+[{**c,'receipt':APPLY} for c in changes]
 bp=R.parent/'S6_SERIES_PUBLISH_work/S6_SERIES_PUBLISH_checkpoint_10/S6_SERIES_PUBLISH_I.tex'
 baseline=bp.read_text();assert sha(baseline.encode())==prior['source_transport']['baseline_source_sha256']
 t=baseline;before=None
 for i,c in enumerate(chain):
  if i==len(prior['source_transport']['applied_changes']):before=t;assert sha(t.encode())==prior['source_sha256']
  pos=c['applied_offset'];assert t[pos:pos+len(c['old'])]==c['old'];t=t[:pos]+c['new']+t[pos+len(c['old']):]
  row=rows_log[int(c['change_id'].split('-')[1])-1]
  assert [row[k] for k in CORE]==[c[k] for k in ['change_id','type','statement_id','old','new','reason']]
 assert t==source and before is not None and len(chain)==264
 for c in reversed(chain):
  pos=c['applied_offset'];assert t[pos:pos+len(c['new'])]==c['new'];t=t[:pos]+c['old']+t[pos+len(c['new']):]
 assert t==baseline
 inline_ids={'I18-edits-01':['$E$'],'I18-edits-03':['$Y$']}
 assert set(rec['exact_inline_exceptions'])==set(inline_ids)
 permitted_inline=before
 for gid,removed in inline_ids.items():
  c=byid[gid];assert c['removed_repeated_inline_mentions']==removed
  assert collections.Counter(math(c['old']))-collections.Counter(math(c['new']))==collections.Counter(removed)
  assert not(collections.Counter(math(c['new']))-collections.Counter(math(c['old'])))
  permitted_inline=permitted_inline.replace(c['old'],c['new'],1)
 assert math(source)==math(permitted_inline) and displays(source)==displays(before)
 ref_ids={'I18-prov-03','I18-root-05'};assert {x['guard_id'] for x in rec['exact_reference_exceptions']}==ref_ids
 permitted_refs=before
 for gid in ref_ids:
  c=byid[gid];permitted_refs=permitted_refs.replace(c['old'],c['new'],1)
 assert refs(source)==refs(permitted_refs)
 for c in changes:
  assert displays(c['old'])==displays(c['new'])
  if c['guard_id'] not in inline_ids:assert math(c['old'])==math(c['new'])
  if c['guard_id'] not in ref_ids:assert refs(c['old'])==refs(c['new'])
 for pat in [r'\\label\{[^}]+\}',r'\\hypertarget\{[^}]+\}',r'\\(?:begin|end)\{[^}]+\}',r'\\bibitem(?:\[[\s\S]*?\])?\{([^}]+)\}']:
  assert re.findall(pat,before)==re.findall(pat,source)
 for w in rec['retained_witnesses']:
  assert sha(w['exact_text'].encode())==w['sha256'] and source.count(w['exact_text'])==1
 # The reference receiver is an exact source witness and resolves in build19.
 target_e=ev('agents/i_cont_provenance/candidate18_guard_review_blocks/D06_target_witness.json','Complete receiving definition and original resolved reference evidence.','76faaa8cb3f35d923a0679399051de50ed4c250a44442173208e60d5bb81a4d2')
 target=read(target_e['path']);definition=(R/target['target_definition']).read_text()
 assert sha(definition.encode())==target['target_definition_sha256'] and source.count(definition)==1
 auxp=R/'build/I_candidate19/S6_SERIES_PUBLISH_I.aux';aux=auxp.read_text()
 auxline=next(x for x in aux.splitlines() if x.startswith(r'\newlabel{def:common-conventions}'))
 assert '{{2.1}{18}' in auxline
 # Every merged block exactly equals the actually applied complete text.
 blocks=[];block_by_guard={};masked0=before;masked1=source
 for i,a in enumerate(rec['archives']):
  for key in ['original','proposed','diff']:assert sha((R/a[key]).read_bytes())==a[key+'_sha256']
  x=(R/a['original']).read_text();y=(R/a['proposed']).read_text();z=x
  for c in changes:
   if c['guard_id'] in a['guard_ids']:assert z.count(c['old'])==1;z=z.replace(c['old'],c['new'],1)
  assert z==y and source.count(y)==1 and before.count(x)==1
  b={**a,'current_complete_block_exact_match':True,'current_source_start_line':source[:source.index(y)].count('\n')+1};blocks.append(b)
  for gid in a['guard_ids']:assert gid not in block_by_guard;block_by_guard[gid]=b
  marker=f'BOUND_CANDIDATE19_BLOCK_{i}';masked0=masked0.replace(x,marker,1);masked1=masked1.replace(y,marker,1)
 assert masked0==masked1 and set(block_by_guard)==set(byid) and len(blocks)==16
 for a in rec['supplied_complete_block_replacements_verified']:
  x=(R/a['original']).read_text();y=(R/a['proposed']).read_text();assert sha(x.encode())==a['original_sha256'] and sha(y.encode())==a['proposed_sha256']
  for gid in a['guard_ids']:c=byid[gid];assert x.count(c['old'])==1;x=x.replace(c['old'],c['new'],1)
  assert x==y
 matrix=read(MATRIX);matrix_e=ev(MATRIX,'Final117-entry primary bibliography audit, retained unchanged in candidate19.',MATRIX_SHA)
 bib0,bib1=bibliography(before),bibliography(source);assert bib0==bib1 and len(bib1)==matrix['entry_count']==117
 bib_bind=[]
 for r in matrix['rows']:
  entry=bib1[r['key']];assert entry==r['proposed_entry'] and sha(entry.encode())==r['proposed_entry_sha256']
  bib_bind.append({'key':r['key'],'current_complete_entry_sha256':sha(entry.encode()),'current_entry_exact_match':True,'matrix_disposition':r['disposition'],'matrix_guard_id':r['guard_id']})
 build_e=ev('build/I_candidate19/build_summary.json','Actual clean candidate19 build and PDF hashes.')
 build=read(build_e['path']);pdfp=R/'build/I_candidate19/S6_SERIES_PUBLISH_I.pdf'
 assert build['source_sha256']==SOURCE and build['pdf_sha256']==PDF==sha(pdfp.read_bytes())
 for k in ['overfull_total','overfull_above_2pt','undefined_references','undefined_citations','missing_characters','missing_fonts','multiply_defined','duplicate_destinations']:assert build[k]==0
 with fitz.open(pdfp) as doc:pages=len(doc)
 assert pages==346
 ag_e=ev(AG,'Actual candidate19 A–G source transport; final ledger/count binding remains pending.',AG_SHA);ag=read(AG)
 assert ag['source_sha256']==SOURCE and ag['ledger_sha256']==application_ledger_sha
 assert ag['source_exact_forward_and_inverse_maps_verified'] and ag['all_label_and_tag_sequences_preserved']
 assert len(ag['exact_edits'])==len(chain) and len(ag['headlines'])==7 and sum(x['outline_items'] for x in ag['headlines'].values())==40 and len(ag['blocks'])==80
 for x,y in zip(ag['exact_edits'],chain):assert (x['change_id'],x['old'],x['new'])==(y['change_id'],y['old'],y['new'])
 # Preserve immutable records. Mutable canonical status/ledger paths, if any,
 # are captured as current dependencies and never overwritten by this tool.
 protected={PRIOR:PRIOR_SHA,APPLY:APPLY_SHA,AG:AG_SHA,MATRIX:MATRIX_SHA}
 for path,h in rec['immutable_reading_dossier_and_status_records'].items():
  if Path(path).suffix in ['.tsv','.csv'] and ('STATUS' in Path(path).name or 'CHECK_EVENTS' in Path(path).name):continue
  assert sha((R/path).read_bytes())==h,(path,'immutable evidence changed');protected[path]=h
 reopen_e=[ev('records/S6_SERIES_PUBLISH_I_candidate18_D06_reopen.json','Explicit D06 reopening now resolved by I18-prov-03.','93059f42e19b85ff72ab5e834a798dc776085af7e473a966f46cd7900c6e6588'),ev('records/S6_SERIES_PUBLISH_I_candidate18_D11_reopen.json','Explicit D11 reopening; exact quoted one-sentence scope is controlling.','bcd7fa3f99030a3a5add6491f3a9fee2430d89003b9099c85616c93eafde0665')]
 progress_e=ev('records/S6_SERIES_PUBLISH_I_candidate18_type_progress.json','Root individual type review plus new visual findings; later D06/D11 reopenings are separately bound.','c12465f619c3b5132f0b928be939f9c64d164b1e4bd48fe204924c5511c7591d')
 dependencies=['Actually read every changed candidate19 complete image; carry earlier page readings only through complete image hash equality.',
  'Complete and deduplicate the actual used-and-rechecked proof-rereading manifest, append only its authorized events, update section1.5 counts/model provenance and rebuild/rebind the resulting source if it changes.',
  'Bind final source/PDF/check-ledger/report/deposit claims, including the42 provenance claims and the final A–G ledger binding.',
  'Finalize defect-page mapping and the full mapped-log hash while preserving the stable edit-content and type-association hashes.']
 evidence=[prior_e,rec_e,inputs_e,root_e,coverage_e,build_e,ag_e,progress_e]
 type_rows=[];associations=[]
 for old in prior['rows']:
  typ=old['type_id'];r=copy.deepcopy(old);new=[c for c in changes if typ in types_of(c['type'])]
  selected=[x for x in rows_log if typ in types_of(x['type'])];cont=[c for c in chain if typ in types_of(c['type'])]
  resolutions=[]
  for c in new:
   b=block_by_guard[c['guard_id']]
   resolutions.append({'guard_id':c['guard_id'],'change_id':c['change_id'],'type':c['type'],'statement_id':c['statement_id'],'old_text_sha256':sha(c['old'].encode()),'new_text_sha256':sha(c['new'].encode()),'current_complete_block':b['proposed'],'current_complete_block_sha256':b['proposed_sha256'],'current_source_start_line':b['current_source_start_line'],'exact_current_replacement_verified':True,'inline_math_segments_identical':c['inline_math_segments_identical'],'removed_repeated_inline_mentions':c['removed_repeated_inline_mentions'],'all_display_math_identical':True,'reference_sequence_identical':c['reference_sequence_identical'],'added_reference':c['added_reference'],'removed_reference':c['removed_reference'],'positive_retained_witnesses':[w for w in rec['retained_witnesses'] if w['guard_id']==c['guard_id']]})
  r.update({'status':'source_clear_pending_final_render_count_and_provenance_binding','source_clear_in_recorded_review_scope':True,'proposed_disposition':'Every confirmed source instance in the inherited contextual and complete candidate18 reading scopes is exactly resolved in the applied candidate19 source. Root may review this row under rule0.3; final changed-page, count, provenance and map dependencies remain separate.','candidate18_source_review_as_recorded':old['source_review'],'candidate18_pending_issues_as_recorded':old['remaining_content_issues'],'source_review':review(typ,old['source_review'],new),'remaining_content_issues':[],'exact_applied_guard_resolutions':resolutions,'applied_candidate18_guard_resolutions':resolutions,'current_edit_associations':len(selected),'continuation_edit_associations':len(cont),'edit_ids':[x['change_id'] for x in selected],'continuation_edit_ids':[x['change_id'] for x in cont],'edit_content_sha256':core_hash(selected),'remaining_dependencies':dependencies,'new_page_credit':0,'mathematical_events_added':0})
  r['evidence']+=evidence
  if typ=='D06':r['evidence']+=[reopen_e[0],target_e]
  if typ=='D11':r['evidence'].append(reopen_e[1])
  if typ=='D18':r['evidence'].append(matrix_e)
  r['source_absence_evidence']={'method':'Exact current complete-block resolutions of every named confirmed instance, inherited individual contextual dispositions and complete candidate18 actual-page coverage; keyword absence is not a closure premise.','named_current_guards_resolved':[x['guard_id'] for x in resolutions],'inherited_individual_scope':{'path':PRIOR,'sha256':PRIOR_SHA,'type_id':typ},'remaining_confirmed_instances':0,'current_changed_page_reading_still_required':True}
  type_rows.append(r)
  for x in selected:associations.append({'type_id':typ,'change_id':x['change_id'],'statement_id':x['statement_id'],'origin':'inherited candidate13' if int(x['change_id'].split('-')[1])<=prior['inherited_unique_edit_rows'] else 'continuation'})
 assert len(type_rows)==25 and {x['type_id'] for x in type_rows}=={f'D{i:02d}' for i in range(1,26)}
 ab=io.StringIO(newline='');w=csv.DictWriter(ab,fieldnames=['type_id','change_id','statement_id','origin'],delimiter='\t');w.writeheader();w.writerows(associations);abytes=ab.getvalue().encode()
 ap=O/'S6_SERIES_PUBLISH_I_candidate19_type_associations.tsv'
 result={'schema':5,'paper':'I','candidate':'I_candidate19','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':SOURCE,'pdf_sha256':PDF,'page_count':pages,'defect_log_sha256':sha(lb),'defect_log_content_sha256':core_hash(rows_log),'defect_log_content_hash_specification':prior['defect_log_content_hash_specification'],'applied_defect_log_sha256':rec['after_defect_log_sha256'],'full_log_hash_relation':'Current full log equals the apply receipt.' if sha(lb)==rec['after_defect_log_sha256'] else 'Mapping/review fields changed; every stable edit-content field and type association matches the prior log and actual21 changes.','source_path':'S6_SERIES_PUBLISH_I.tex','pdf_path':'build/I_candidate19/S6_SERIES_PUBLISH_I.pdf','defect_log_path':'S6_SERIES_PUBLISH_defects_I.tsv','defect_type_associations':{'path':str(ap.relative_to(R)),'sha256':sha(abytes),'count':len(associations)},'unique_edit_rows':len(rows_log),'inherited_unique_edit_rows':prior['inherited_unique_edit_rows'],'continuation_unique_edit_rows':len(chain),'latest_applied_guards':len(changes),'latest_guard_type_associations':dict(collections.Counter(c['type'] for c in changes)),'inherited_edit_type_associations':prior['inherited_edit_type_associations'],'edit_type_associations':len(associations),'count_semantics':prior['count_semantics'],'all_types_source_clear':True,'source_clear_scope':'All25 rows are clear within their individually read inherited scopes and the complete candidate18 actual reading; all21 newly confirmed instances have exact applied resolutions. Candidate19 changed-image reading and the requested final count/provenance update remain distinct dependencies.','final_certified':False,'canonical_status_modified':False,'mathematical_events_added':0,'new_page_credit':0,'prior_immutable_dossier':prior_e,'applied_batch':rec_e,'root_approved_inputs':inputs_e,'source_transport':{'baseline_source_sha256':prior['source_transport']['baseline_source_sha256'],'previous_source_sha256':prior['source_sha256'],'current_source_sha256':SOURCE,'exact_forward_and_inverse_reconstruction':True,'applied_changes':chain,'latest_complete_blocks_verified':blocks},'supplied_complete_block_comparisons_verified':len(rec['supplied_complete_block_replacements_verified']),'merged_complete_blocks_verified':len(blocks),'immutable_reading_and_dossier_records_verified':protected,'inherited_evidence_files_verified':prior['inherited_evidence_files_verified'],'check_ledger_sha256':ledger_sha,'application_check_ledger_sha256':application_ledger_sha,'ledger_hash_matches_application':ledger_sha==application_ledger_sha,'count_provenance_update_pending':True,'current_build':build_e,'current_AG_binding':ag_e,'contextual_reviews':prior['contextual_reviews'],'root_complete_context_reviews':prior['root_complete_context_reviews']+[root_e],'candidate18_complete_coverage':coverage_e,'candidate18_individual_type_progress':progress_e,'reopening_records':reopen_e,'D06_current_target':{'witness':target_e,'definition_path':target['target_definition'],'definition_sha256':target['target_definition_sha256'],'current_source_exact_match':True,'candidate19_aux_path':str(auxp.relative_to(R)),'candidate19_aux_sha256':sha(auxp.read_bytes()),'exact_aux_line':auxline},'D11_reopening_wording_qualification':'The historical reopening finding says final two sentences, but the quoted old text, approved guard and applied change remove one final sentence only; the preceding parabolic-axis consequence is unchanged.','bibliography_audit':matrix_e,'bibliography_complete_entry_bindings':bib_bind,'bibliography_primary_file_evidence_verified':prior['bibliography_primary_file_evidence_verified'],'bibliography_record_limits':matrix['primary_record_limit'],'declared_scope_exceptions':{'exact_inline_exceptions':rec['exact_inline_exceptions'],'exact_reference_exceptions':rec['exact_reference_exceptions'],'inline_math_difference':rec['inline_math_difference'],'reference_difference':rec['reference_difference'],'retained_witnesses':rec['retained_witnesses'],'all_other_inline_and_reference_sequences_identical':True,'all_display_sequences_identical':True},'rows':type_rows,'remaining_dependencies':dependencies,'limitations':['This dossier adds no page reading or check event.','New actual candidate19 image findings may reopen their affected type.','The count manifest and section1.5 update require a later final source/ledger/PDF binding.','Root alone controls canonical type statuses and final Paper I certification.']}
 md=['# Paper I candidate19 —25 individual source dispositions','',f'Source SHA-256: `{SOURCE}`','',f'PDF SHA-256: `{PDF}` ({pages} pages).','',f'Defect log SHA-256: `{sha(lb)}`',f'Stable edit-content SHA-256: `{core_hash(rows_log)}`','',f'The actual21-guard batch resolves four D02, one D06, nine D08, one D11 and six D23 instances. It is bound to {len(blocks)} complete merged contexts and {len(chain)} exact continuation edits. The log has {len(rows_log):,} rows and {len(associations):,} type associations. All117 bibliography entries still equal the final matrixv3 text.','', 'All25 source rows are clear within the recorded review scopes. No canonical status is changed. Candidate19 changed-page reading, the rereading-event/count manifest, section1.5 update and final provenance/map bindings remain pending.','', 'The declared exceptions remove repeated E/Y mentions, add the exact Definition2.1 locator and remove one repeated equation-reference recap. All displayed mathematics and every other inline/reference sequence are retained.','', '| Type | Log associations | New applied guards | Current source disposition |','|---|---:|---:|---|']
 for r in type_rows:md.append(f"| {r['type_id']} | {r['current_edit_associations']} | {len(r['exact_applied_guard_resolutions'])} | Clear in recorded scope; final dependencies pending |")
 for r in type_rows:md+=['',f"## {r['type_id']} — {r['defect']}",'',r['source_review']]
 md+=['','## Remaining dependencies','',*['- '+x for x in dependencies],'']
 out=O/'S6_SERIES_PUBLISH_I_candidate19_type_closure_preparation.json';files={out:(json.dumps(result,ensure_ascii=False,indent=2)+'\n').encode(),out.with_suffix('.md'):'\n'.join(md).encode(),ap:abytes}
 assert sp.read_bytes()==sb and lp.read_bytes()==lb and cp.read_bytes()==cb
 for path,h in protected.items():assert sha((R/path).read_bytes())==h
 for p in files:assert not p.exists(),('immutable output already exists',str(p))
 for p,b in files.items():p.write_bytes(b)
 print(json.dumps({'dossier':str(out.relative_to(R)),'sha256':sha(files[out]),'source_sha256':SOURCE,'pdf_sha256':PDF,'page_count':pages,'defect_log_sha256':sha(lb),'defect_log_content_sha256':core_hash(rows_log),'type_association_sha256':sha(abytes),'rows':len(rows_log),'associations':len(associations),'types':25,'all_types_source_clear':True,'continuation_edits':len(chain),'latest_guards':len(changes),'complete_merged_blocks':len(blocks),'count_provenance_update_pending':True,'canonical_status_modified':False},indent=2))


if __name__=='__main__':main()
