#!/usr/bin/env python3
"""Bind this reader's actual complete proof comparisons without editing events."""
from pathlib import Path
import collections
import datetime
import hashlib
import json
import re

R=Path(__file__).resolve().parents[1]
O=R/'agents/i_cont_edits'
sha=lambda b:hashlib.sha256(b).hexdigest()
# These are explicitly selected manual-review scopes. Environment inspection
# below verifies that a selected rewrite touches its attached proof; it does
# not create a reading claim from the presence of an archive or a page image.
SCOPES=[
 ('S6_SERIES_PUBLISH_I_continuation_edits_receipt.json',13,14,'affected_archives',
  ['push:src:D.1.2','ari:C.6.3','ari:C.7.12','ari:C.7.6','push:src:E.2.1','push:src:B.4.10','fam:src:B.2.1','inv:A2.2'],
  'The complete original candidate13 owning statements/proofs were read and each exact archived replacement was compared; the contemporaneous proof_scope and per-change reasons explicitly attest that comparison.'),
 ('S6_SERIES_PUBLISH_I_continuation_residue_receipt.json',13,14,'archives',
  ['ari:C.6.R2','push:src:D.4.3'],
  'Complete current source statements/proofs read; exact proposed replacement differences read and compared against those complete blocks. The two manual-review flags in this receipt are explicit.'),
 ('S6_SERIES_PUBLISH_I_candidate14_residue_receipt.json',14,15,'archives',
  ['push:src:B.4.22','push:src:B.4.23','fam:src:A.5.2'],
  'Complete current source statements/proofs read, and replacement differences read and compared. The receipt explicitly records both actions.'),
 ('S6_SERIES_PUBLISH_I_candidate15_edits_guards.json',15,16,'full_blocks',
  ['ari:C.6.R5','ari:C.8.10','ari:C.8.14','ari:C.7.1','ari:C.7.2','ari:C.7.3','ari:C.7.9','ari:C.7.10'],
  'Complete printed statements and proofs were actually read across the assigned rendered pages, then the exact source clauses and proposed differences were manually compared against those complete proofs. The unchanged remainder is bound by full-block pairs; this does not assert an independent derivation or a fresh whole proposed-source reading at that earlier stage.'),
 ('S6_SERIES_PUBLISH_I_candidate16_edits_guards.json',16,17,'full_blocks',
  ['ari:C.8.14','ari:C.7.3','ari:C.7.9','ari:C.7.10'],
  'The complete owning source statements/proofs were read and exact replacements compared; the scope and per-block complete_owning_source_block_read flags explicitly record this.'),
 ('S6_SERIES_PUBLISH_I_candidate17_edits_guards.json',17,18,'full_blocks',
  ['ari:C.6.T2','fam:src:F.2.2','fam:src:F.3.1','push:src:E.3.1','inv:A1.2','inv:D4.4','fam:src:B.4.2','push:src:D.4.3','fam:src:E.1.4','ari:C.8.14'],
  'Complete owning source statements/proofs were read against candidate17, and exact proposed replacements manually compared. The scope and per-block manual-reading flags are explicit; context-search membership alone is not the evidence.'),
 ('S6_SERIES_PUBLISH_I_candidate18_edits_guards_v3.json',18,19,'full_blocks',
  ['push:src:B.4.13','push:src:B.4.16','push:src:B.4.24','push:src:B.4.25','push:src:B.4.18'],
  'Every complete original and proposed source statement/proof was actually read. The final v3 full-pair review binds the first four pairs by exact identity to their already completed v2 reread and directly attests the new fifth pair.')
]


def normalized_archive(a):
 if 'current_path' in a:return a['current_path'],a['current_sha256'],a['replacement_path'],a['replacement_sha256']
 if 'before' in a:return a['before'],a['before_sha256'],a['after'],a['after_sha256']
 return a['original'],a['original_sha256'],a['proposed'],a['proposed_sha256']


def main():
 protected={p:p.read_bytes() for p in [R/'S6_SERIES_PUBLISH_I.tex',R/'S6_SERIES_PUBLISH_defects_I.tsv',R/'CHECK_EVENTS.tsv']}
 rows={};evidence_files=[];exclusions=[];instances=0
 for filename,before_candidate,after_candidate,key,selected,method in SCOPES:
  path=O/filename;raw=path.read_bytes();d=json.loads(raw)
  evidence_files.append({'path':str(path.relative_to(R)),'sha256':sha(raw),'created_utc':d.get('created_utc'),'manual_scope':d.get('proof_scope',d.get('scope',method))})
  changes=d.get('guards',d.get('changes',[]))
  bylabel={}
  for a in d[key]:
   labels=a.get('statement_ids',[a.get('statement_id')])
   for label in labels:bylabel[label]=a
  assert set(selected)<=set(bylabel)
  for label,a in bylabel.items():
   if label not in selected:
    exclusions.append({'statement_id':label,'evidence_record':str(path.relative_to(R)),'candidate':before_candidate,'reason':'No selected rewritten attached-proof scope in this record: the change is in a statement, prefatory/closing commentary, or a remark without an attached proof. This omission does not deny a separate supported proof reread elsewhere.'})
    continue
   pa,ha,pb,hb=normalized_archive(a);old=(R/pa).read_text();new=(R/pb).read_text()
   assert sha((R/pa).read_bytes())==ha and sha((R/pb).read_bytes())==hb
   start=old.find(r'\begin{proof}');end=old.find(r'\end{proof}',start)
   assert 0<=start<end and r'\end{proof}' in new
   proof_changes=[];outside=[]
   for g in changes:
    if g.get('statement_id')!=label:continue
    x=g.get('before',g.get('old'));p=old.find(x)
    if start<=p<end:proof_changes.append(g.get('id',g.get('guard_id',g.get('change_id'))))
    else:outside.append(g.get('id',g.get('guard_id',g.get('change_id'))))
   assert proof_changes,(filename,label,'no actual proof wording change')
   instances+=1
   row=rows.setdefault(label,{'statement_id':label,'deduplication_key':'I-continuation-20261121-proof-reread:'+label,'attested_event_type':'used and rechecked in this run','actual_activity':'Complete original/reworded proof comparison during this continuation; no independent re-proof, targeted derivation, computation or formal certificate is claimed.','outcome':'The reworded proof was read against its original, and the preserved statement, operative steps, maps, equations and conclusions were checked within that comparative scope. Exact differences and any removed repeated inline mentions are disclosed in the bound review records.','supporting_manual_review_instances':[]})
   support={'before_candidate':before_candidate,'intended_after_candidate':after_candidate,'evidence_record':str(path.relative_to(R)),'evidence_record_sha256':sha(raw),'review_record_created_utc':d.get('created_utc'),'before_source_sha256':d.get('source_sha256',d.get('before_source_sha256')),'after_source_sha256':d.get('after_source_sha256'),'pdf_sha256':d.get('pdf_sha256',d.get('candidate14_pdf_sha256')),'original_full_block':pa,'original_full_block_sha256':ha,'replacement_full_block':pb,'replacement_full_block_sha256':hb,'complete_original_proof_actually_read':True,'proposed_rewording_actually_compared_against_original_proof':True,'manual_review_method':method,'proof_guard_or_change_ids':proof_changes,'other_guard_ids_in_same_block_no_separate_credit':outside,'application_state':'proposed final v3 batch, pending root combined apply at attestation creation' if before_candidate==18 else 'applied in the subsequent recorded continuation source','proof_environment_present_verified':True,'reading_claim_source':'Explicit self-attestation of this reader, supported by the named contemporaneous manual-review record; not inferred from source scanning or archive existence.'}
   if before_candidate==18:
    review=O/'S6_SERIES_PUBLISH_I_candidate18_edits_full_pair_review_v3.json'
    support['additional_manual_review_record']=str(review.relative_to(R));support['additional_manual_review_record_sha256']=sha(review.read_bytes())
    assert support['additional_manual_review_record_sha256']=='3731ecc66773f8b1726eb74bc2212ec01cbc34aa460285bd7fc05730829fcc1e'
   row['supporting_manual_review_instances'].append(support)
 for p,raw in protected.items():assert p.read_bytes()==raw,p
 ordered=[rows[k] for k in sorted(rows)]
 assert len(ordered)==34 and instances==40,(len(ordered),instances)
 result={'paper':'I','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'date':'2026-11-21','reader':'/root/i_final_edits','who':'GPT-6 Astra, ChatGPT Pro mode; effort not separately exposed','record_kind':'Explicit attestation and proposed ledger input; append-only manifest only','latest_reviewed_source_sha256':'3542f2632cad8f1eb78f0f30f8a64ca91998f3bd1d97010ca76d89297c4bffe7','latest_reviewed_pdf_sha256':'702aaa0abd1a4d8376e213ecaf03a0296592e22063f26db324d805502987e66e','canonical_source_sha256_at_attestation':sha(protected[R/'S6_SERIES_PUBLISH_I.tex']),'check_ledger_sha256_at_attestation':sha(protected[R/'CHECK_EVENTS.tsv']),'attestation':'I attest the listed complete proof rereadings and original/reworded comparisons were actually completed by this continuation reader. The selected historical records explicitly describe those actions. Candidate15 is qualified as complete printed-proof reading plus manual comparison of exact proposed source differences; later source-pair scopes are described separately. No activity is inferred solely from archive equality, a keyword hit, or a page-reading receipt.','unique_owning_statement_count':len(ordered),'complete_manual_comparison_instance_count':instances,'deduplication':'One proposed used-and-rechecked event per owning printed statement across the repeated candidates of this continuation. Repeated supporting comparisons provide evidence within that one scope and receive no additional event. Provenance must also deduplicate overlapping owners with other readers before any canonical append.','event_scope_limit':'Used and rechecked in this run only. Independent-re-proof, targeted-proof-check and computation/formal-certificate credits are zero. Merely viewing a rendered page, typography, metadata, citation edits, statement-only/prelude rewrites and automatic comparisons are excluded.','candidate18_application_gate':'The five candidate18 proposed-proof scopes are actually read, but their final canonical replacement/source binding must await the approved combined application; the proposal hash alone is not an applied-source assertion.','historical_zero_event_fields':'Earlier editorial receipts recorded zero events added because they did not mutate CHECK_EVENTS.tsv. They remain unchanged. This separate attestation identifies the actual rereading activity for the root-requested section4.3 manifest and does not itself append any event.','rows':ordered,'evidence_files':evidence_files,'excluded_scopes':exclusions,'additional_exclusions':['All bibliography and publisher/version metadata work','All accent-only typography and page-spacing changes','All page-image reading without a full rewritten-proof comparison','All combined-apply archive preservation checks without this reader’s separate actual complete proof reading','I16-edits-11r1 convention relocation and its statement-only/prelude scope','Any root or other-agent proof review for which this reader only applied or archived the guard'],'canonical_files_modified':False,'check_events_appended':0,'new_independent_or_targeted_or_computational_events':0,'additional_full_page_credit':0}
 p=O/'S6_SERIES_PUBLISH_I_continuation_proof_reread_attestation_edits.json';assert not p.exists();p.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 md=['# Paper I continuation — proof rereading attestation','',f'Attestation SHA-256: `{sha(p.read_bytes())}`','', 'Thirty-four unique owning statements have forty supported complete original/reworded proof comparisons. The proposed event category is **used and rechecked in this run** only, with one event per statement across repeated candidates. This manifest appends no ledger row.','', 'The five candidate18 scopes have actually been read, and their final canonical replacement/source binding remains gated on the approved combined application. Candidate15 evidence records full printed-proof reading and manual exact replacement comparison; it does not claim a fresh independent derivation or a later source-pair reading.','', '| Owning statement | Supporting comparison candidates | Instances |','|---|---|---:|']
 for row in ordered:md.append(f"| `{row['statement_id']}` | {', '.join(str(x['before_candidate'])+'→'+str(x['intended_after_candidate']) for x in row['supporting_manual_review_instances'])} | {len(row['supporting_manual_review_instances'])} |")
 p.with_suffix('.md').write_text('\n'.join(md)+'\n')
 print(json.dumps({'attestation':str(p.relative_to(R)),'sha256':sha(p.read_bytes()),'unique_statements':len(ordered),'manual_comparison_instances':instances,'canonical_files_modified':False,'check_events_appended':0},indent=2))


if __name__=='__main__':main()
