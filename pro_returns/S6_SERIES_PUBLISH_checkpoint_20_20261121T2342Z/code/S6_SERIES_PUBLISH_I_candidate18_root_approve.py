#!/usr/bin/env python3
"""Bind the root's actual complete-proof readings and21 literal repair decisions."""
from pathlib import Path
import datetime, hashlib, json
from S6_SERIES_PUBLISH_I_candidate17_combined import archive, write_stable
R=Path(__file__).resolve().parents[1];sha=lambda b:hashlib.sha256(b).hexdigest()
source='3542f2632cad8f1eb78f0f30f8a64ca91998f3bd1d97010ca76d89297c4bffe7'
assert sha((R/'S6_SERIES_PUBLISH_I.tex').read_bytes())==source
inputs=[
 ('agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate18_root_guards_v2.json','40fd9dba1ac88a6115b555346159449d385ecf6f7b31b7f9318966451575934b',6),
 ('agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate18_edits_guards_v3.json','c0139cf29b3848f7ff6d885d57bef51e6ce67c72b94b2b22c8bf409c98b63563',7),
 ('agents/i_cont_provenance/S6_SERIES_PUBLISH_I_candidate18_provenance_guards.json','93ac33f0121360fd086b7f5ed4cda04be6688215d1198db7402998fcbaab10f3',7),
 ('agents/continuation_infra/S6_SERIES_PUBLISH_I_candidate18_infra_layout_guard_final.json','9c1ef9c9521663c8ccb4b75d555be5a2d2e69a88a1e302e76c591c188cc2df69',1)]
rows=[];proofs={};contexts={}
for p,h,n in inputs:
 raw=(R/p).read_bytes();assert sha(raw)==h;x=json.loads(raw);gs=x if isinstance(x,list) else x['guards'];assert len(gs)==n
 for g in gs:
  assert g['source_sha256']==source
  pa,ha,pb,hb=archive(g)
  assert sha((R/pa).read_bytes())==ha and sha((R/pb).read_bytes())==hb
  old=(R/pa).read_text();new=(R/pb).read_text()
  ctx=contexts.setdefault((pa,pb),{'statement_id':g['statement_id'],'original':pa,'original_sha256':ha,'proposed':pb,'proposed_sha256':hb,'guard_ids':[],'root_actually_read_complete_original_context':True,'root_actually_compared_exact_proposed_changes':True})
  ctx['guard_ids'].append(g['id'])
  if r'\begin{proof}' in old:proofs[(pa,pb)]=ctx
  rows.append({'guard_id':g['id'],'type':g['type'],'statement_id':g['statement_id'],'old':g['before'],'new':g['after'],'reason':g['reason'],'root_approved':True})
assert len(rows)==21 and len(proofs)==15 and len(contexts)==16
review={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'paper':'I','candidate':18,'source_sha256':source,
 'root_reader':'GPT-6 Astra (OpenAI), ChatGPT Pro mode; root, continuation of21 November2026',
 'actual_reading_scope':'Root read the complete section heading and all15 complete owning statements with their entire attached proofs directly from the source or exact full-block archives. Root then read every literal before/after pair and its positive retained witnesses, including all five merged editor diffs and all seven provenance changes. The complete receiving Definition2.1 was also read. This comparison is after exposure to the printed arguments and claims no independent derivation.',
 'full_proof_comparisons':list(proofs.values()),'all_context_comparisons':list(contexts.values()),'literal_decisions':rows,
 'explicit_exceptions':[{'guard_id':'I18-edits-01','removed_repeated_inline':'$E$','preservation':'The statement defines E and steps1–3 retain finite S, nonempty S intersect E, exact equivariance and the torsion equation.'},{'guard_id':'I18-edits-03','removed_repeated_inline':'$Y$','preservation':'The period lattice definition, multiplicative character pairing, quotient sequence, exponentiation and u/gamma valuation maps remain.'},{'guard_id':'I18-prov-03','added_reference':r'\ref{def:common-conventions}','preservation':'The old first-page locator is replaced by the actual Definition2.1 fixing the clockwise root deck convention and positive-loop endpoint identification.'},{'guard_id':'I18-root-05','removed_duplicate_reference':r'\eqref{pub:I:eq:D-2}','preservation':'The exact displayed E/G equation and full bundle/cocycle/splitting proof remain.'}],
 'source_changed':False,'events_added_by_this_record':0,'event_accounting_note':'The prompt§4.3 requirement for actual edited-proof rereadings is under a separate append-only review. The zero here records this operation, not a decision to omit qualifying rereadings from the final ledger.'}
rp=R/'records/S6_SERIES_PUBLISH_I_candidate18_root_complete_proof_comparison.json';write_stable(rp,json.dumps(review,ensure_ascii=False,indent=2)+'\n')
doc={'paper':'I','candidate':18,'source_sha256':source,'pdf_sha256':'702aaa0abd1a4d8376e213ecaf03a0296592e22063f26db324d805502987e66e','root_approved':True,'guard_files':[{'path':p,'sha256':h,'count':n} for p,h,n in inputs],
 'complete_coverage':{'path':'records/S6_SERIES_PUBLISH_I_candidate18_complete_coverage_snapshot.json','sha256':'9bd9fbdf59befb531f07319624e74f66f0693f65d246a57909d12f42cd2171be'},
 'root_review':{'path':str(rp.relative_to(R)),'sha256':sha(rp.read_bytes())},'approved_guard_count':21,'source_changed':False,'events_added_by_this_record':0}
mp=R/'records/S6_SERIES_PUBLISH_I_candidate18_root_approved_inputs.json';write_stable(mp,json.dumps(doc,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'manifest':str(mp.relative_to(R)),'sha256':sha(mp.read_bytes()),'root_complete_proof_comparison':str(rp.relative_to(R)),'comparison_sha256':sha(rp.read_bytes()),'guards':21,'actual_complete_proofs':15,'canonical_source_changed':False}))
