#!/usr/bin/env python3
"""Bind both source steps and the approved event append; hold final PDF claims."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,importlib.util,json,re
from S6_SERIES_PUBLISH_I_cont_recount import recount,KINDS
R=Path(__file__).resolve().parents[2];O=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
bind=lambda p:{'path':str(p.relative_to(R)),'sha256':sha(p)}
def load(p):return json.loads(p.read_text())
src=R/'S6_SERIES_PUBLISH_I.tex';ledger=R/'CHECK_EVENTS.tsv'
assert sha(src)=='179fcc4e85fb7902aaf978bcd809cf9928ebc0a46cda5628d5096e6fa0011d74'
assert sha(ledger)=='0f95daacb5cc1ddbd927d380e982b61bc28fad77edbbfbff4c8823eab22dfd78'
old=O/'candidate19_review_blocks/S6_SERIES_PUBLISH_I_candidate19_source_snapshot.tex'
rp1=R/'agents/continuation_infra/S6_SERIES_PUBLISH_I_candidate19_combined_apply_receipt.json'
rp2=R/'records/S6_SERIES_PUBLISH_I_methodology_count_apply_receipt.json'
assert sha(rp1)=='0c6abd7046757d887f8e4092478d7a5047f95de17072b4724c6d37fffdeb0b18'
assert sha(rp2)=='cb7c0bfe0f30f50c56f3b630b78a9e14c03909be50df1d9a64f928a3b0143ca4'
receipts=[load(rp1),load(rp2)]
text=old.read_text();steps=[]
for receipt in receipts:
    assert hashlib.sha256(text.encode()).hexdigest()==receipt['before_source_sha256']
    initial=text;offsets=[]
    for change in receipt['changes']:
        assert text.count(change['old'])==1
        at=text.index(change['old']);offsets.append((change,at))
        text=text.replace(change['old'],change['new'],1)
    assert hashlib.sha256(text.encode()).hexdigest()==receipt['after_source_sha256']
    inverse=text
    for change,at in reversed(offsets):
        assert inverse[at:at+len(change['new'])]==change['new']
        inverse=inverse[:at]+change['old']+inverse[at+len(change['new']):]
    assert inverse==initial
    steps.append({'before_source_sha256':receipt['before_source_sha256'],'after_source_sha256':receipt['after_source_sha256'],
        'change_ids':[x['change_id'] for x in receipt['changes']],'guard_ids':[x['guard_id'] for x in receipt['changes']],
        'exact_forward_and_inverse_reconstruction':True})
assert text==src.read_text() and len(steps[0]['change_ids'])==7 and len(steps[1]['change_ids'])==1

vp=R/'code/S6_SERIES_PUBLISH_I_verify_reread_append.py'
sp=importlib.util.spec_from_file_location('append_verifier',vp);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
appendp=R/'records/S6_SERIES_PUBLISH_I_continuation_reread_append_receipt.json'
append=m.verify_append(appendp)
priorp=O/'S6_SERIES_PUBLISH_I_candidate19_recount.json';prior=load(priorp)
currentp=O/'S6_SERIES_PUBLISH_I_candidate20_recount.json';current=load(currentp)
assert current['source_sha256']==sha(src) and current['ledger_sha256']==sha(ledger)
fresh=recount(R,R.parent/'S6_SERIES_PUBLISH_work')
for key in ['counts','statements','selected_ledger_rows','selected_event_ids','declared_evidence_groups']:
    assert fresh[key]==current[key]
cols=['id','kind','identities']
assert [[s[k] for k in cols] for s in prior['statements']]==[[s[k] for k in cols] for s in current['statements']]
assert current['selected_ledger_rows']==prior['selected_ledger_rows']+list(range(7868,7946))
assert current['selected_event_ids']==prior['selected_event_ids']+append['appended_event_ids']
groups=set(current['declared_evidence_groups'])-set(prior['declared_evidence_groups'])
assert groups=={'publish-I-continuation-20261121-exposed-proof-reread'}
assert [current['counts'][k] for k in KINDS]==[767,10,143,809,194,1]
assert [current['counts'][k]-prior['counts'][k] for k in KINDS]==[0,0,0,78,0,0]
assert current['counts']['event_associations']==1924 and current['counts']['statements']==333
assert current['counts']['subject_identifiers']==353 and current['counts']['declared_evidence_groups']==1615
method=re.search(r'\\subsection\{Methodology\}.*?(?=\\subsection\{How the paper is organized\})',text,re.S)[0]
assert method.count('It also records 809 readings of the proofs and applications,')==1
claims=load(O/'candidate18_source/S6_SERIES_PUBLISH_I_cont_three_way_claims.json')
status=[]
for section,rows in claims['exact_main_status_binding'].items():
    for role,row in rows.items():
        assert text.count(row['text'])==1
        status.append({'section':section,'role':role,'text':row['text'],'occurrences':1})
assert len(status)==21
result={'created_utc':datetime.now(timezone.utc).isoformat(),'paper':'I','candidate':20,
    'source':bind(src),'ledger':bind(ledger),'candidate19_source':bind(old),
    'source_edit_receipts':[bind(rp1),bind(rp2)],'source_steps':steps,
    'exact_whole_source_forward_and_inverse_reconstruction':True,
    'reread_append_receipt':bind(appendp),'reread_append_verification':append,
    'candidate19_recount':bind(priorp),'candidate20_recount':bind(currentp),
    'counts':current['counts'],'printed_statement_identity_sequence_unchanged':True,
    'old_selected_ledger_row_and_event_sequence_preserved':True,
    'all78_appended_rows_selected_once_for_current_printed_owners':True,
    'sole_category_delta':{'used and rechecked in this run':78},
    'new_declared_evidence_groups':sorted(groups),'main_status_string_bindings':status,
    'source_status_strings_verified':21,'methodology_counts_equal_fresh_ledger_recount':True,
    'printed_before_D15_scope':{'source':receipts[1]['printed_before_source'],'pdf':receipts[1]['printed_before_pdf'],
        'pages':[16,17],'count_literal_page':16,'body_only_intermediate_source':receipts[1]['before_source_sha256'],
        'intermediate_source_has_no_pdf':True,'complete_methodology_block_equal':True,
        'complete_methodology_block_sha256':receipts[1]['equal_methodology_before_block_sha256']},
    'all_42_claims_finalized':False,'final_42_claim_guard_generated':False,
    'remaining_gate':'Candidate20 clean PDF, current D08/D09 occurrence correspondence, and certified complete image coverage.',
    'mathematical_events_added_by_this_binding':0,'previously_approved_reread_events_appended':78,
    'new_independent_targeted_computation_credit':0,'page_reading_credit_added':0,'shared_files_modified':False}
p=O/'S6_SERIES_PUBLISH_I_candidate20_source_count_rebinding.json';assert not p.exists()
p.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'receipt':bind(p),'counts':result['counts'],'exact_source_steps':2,'source_status_strings_verified':21},indent=2))
