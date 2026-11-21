#!/usr/bin/env python3
"""Apply only root's exact approved 78-row append and D15 numeric substitution.

The two operations have separate receipts.  The original ledger/log bytes and
body-only before-source are archived before mutation.  This script never builds.
"""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,importlib.util,io,json,os,re
from S6_SERIES_PUBLISH_I_cont_recount import recount,KINDS

R=Path(__file__).resolve().parents[2];O=Path(__file__).resolve().parent
A=O/'continuation_reread_append'
sha=lambda b:hashlib.sha256(b).hexdigest()
fs=lambda p:sha(p.read_bytes())
bind=lambda p:{'path':str(p.relative_to(R)),'sha256':fs(p)}
NOW=lambda:datetime.now(timezone.utc).isoformat()
csv.field_size_limit(100_000_000)
BASE='e45bf7b52aff58c0d9fb4a474cd97e9dd7615c761c4a1a79983e268bd27fe714'
AFTER_LEDGER='0f95daacb5cc1ddbd927d380e982b61bc28fad77edbbfbff4c8823eab22dfd78'
BODY='d3922ad95bbc654a42424abfc27f9e05d18e3a0850b20a31d02bea19ac449f4a'
LOG='7fb7f215a3c7554a1fcf459237a77be4dcfe1fa7949a5efd52ddf34c4d2bed10'
def load(p):return json.loads(p.read_text())
def table(raw):
    rd=csv.DictReader(io.StringIO(raw.decode(),newline=''),delimiter='\t')
    return rd.fieldnames,list(rd)
def save_json(p,x):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def save_copy(p,raw):
    if p.exists():assert p.read_bytes()==raw
    else:p.write_bytes(raw)
def atomic(p,raw):
    tmp=p.with_name(p.name+'.I_reread_approved_tmp')
    assert not tmp.exists();tmp.write_bytes(raw);os.replace(tmp,p)

approvalp=R/'records/S6_SERIES_PUBLISH_I_reread_append_root_approval.json'
assert fs(approvalp)=='76e8473b7ecf61802036d75a262e85115f3d9f0c4dc0a0ce45a0d06b366800a1'
approval=load(approvalp)
manifestp=A/'S6_SERIES_PUBLISH_I_continuation_reread_manifest.json'
assert fs(manifestp)==approval['manifest_sha256']=='55272839a98d16e54e57280775f07caa2bdbd78609647186fe8cf39c94fff408'
manifest=load(manifestp)
guardp=A/'S6_SERIES_PUBLISH_I_methodology_count_guard.json'
assert fs(guardp)==approval['methodology_count_edit']['guard']['sha256']=='25aef473e8d88ffe1d6527bb1a98be73ce0c2ad101412bce7b01d5b6c64574df'
guard=load(guardp)
assert approval['approved'] and approval['approved_event_count']==78
assert approval['methodology_count_edit']['approved']
assert manifest['candidate19_application_gate_discharged']
assert manifest['candidate_event_count']==len(manifest['events'])==78
source=R/'S6_SERIES_PUBLISH_I.tex';ledger=R/'CHECK_EVENTS.tsv';log=R/'S6_SERIES_PUBLISH_defects_I.tsv'
source_before=source.read_bytes();ledger_before=ledger.read_bytes();log_before=log.read_bytes()
assert sha(source_before)==BODY==guard['immediate_before_source']['sha256']
assert sha(ledger_before)==BASE and sha(log_before)==LOG
fields,oldrows=table(ledger_before);log_fields,oldlog=table(log_before)
assert len(oldrows)==7866 and len(oldlog)==2224
assert max(int(x['change_id'].split('-')[-1]) for x in oldlog)==2224

proposal=A/'I_continuation_reread_event_bundle.tsv';bundle_raw=proposal.read_bytes()
assert sha(bundle_raw)==approval['event_bundle_sha256']=='d7f88c6f3dffb97f008c312145a3136d8b6f323df5335d0362840d8d35b65c28'
bundle_fields,additions=table(bundle_raw);assert fields==bundle_fields and len(additions)==78
assert all(x['type']=='used and rechecked in this run' for x in additions)
assert len({x['statement_id'] for x in additions})==78
bundle_target=R/manifest['final_event_bundle_path'];assert not bundle_target.exists()
for n,x in enumerate(additions,2):
    assert x['publish_input_file']==bundle_target.name and x['publish_input_row']==str(n)
ledger_after=ledger_before+bundle_raw.split(b'\r\n',1)[1]
assert sha(ledger_after)==AFTER_LEDGER==approval['approved_after_ledger_sha256']
assert ledger_after==(A/'I_continuation_after_ledger_preview.tsv').read_bytes()
assert len(table(ledger_after)[1])==7944

old_source_copy=A/'I_source_body_before_count.tex';save_copy(old_source_copy,source_before)
old_log_copy=A/'I_before_D15_defect_log.tsv';save_copy(old_log_copy,log_before)
old_ledger_copy=A/'I_continuation_before_ledger.tsv';save_copy(old_ledger_copy,ledger_before)
text=source_before.decode();old,new=guard['old'],guard['new']
assert old=='It also records 731 readings of the proofs and applications,'
assert new=='It also records 809 readings of the proofs and applications,'
assert text.count(old)==1 and text.count(new)==0
original_method=(R/guard['original_full_block']['path']).read_bytes()
proposed_method=(R/guard['proposed_full_block']['path']).read_bytes()
assert sha(original_method)==guard['original_full_block']['sha256']==guard['methodology_block_sha256_in_both_before_sources']
assert sha(proposed_method)==guard['proposed_full_block']['sha256']
assert original_method.decode().replace(old,new,1)==proposed_method.decode()
assert text.count(original_method.decode())==1
printed_before=R/guard['printed_before_source']['path']
assert fs(printed_before)==guard['printed_before_source']['sha256']
assert printed_before.read_text().count(original_method.decode())==1
assert fs(R/guard['printed_before_pdf']['path'])==guard['printed_before_pdf']['sha256']

# First operation: approved event bundle and exact canonical append.
assert ledger.read_bytes()==ledger_before and source.read_bytes()==source_before and log.read_bytes()==log_before
bundle_target.write_bytes(bundle_raw)
atomic(ledger,ledger_after)
appendp=R/'records/S6_SERIES_PUBLISH_I_continuation_reread_append_receipt.json'
append_receipt={'schema_version':1,'paper':'I','applied':True,'created_utc':NOW(),
    'before_ledger':bind(old_ledger_copy),'before_rows':7866,
    'after_ledger_sha256':fs(ledger),'after_rows':7944,'event_bundle':bind(bundle_target),
    'manifest':bind(manifestp),'appended_event_ids':[x['event_id'] for x in additions],
    'old_ledger_prefix_preserved':True,'approved_manifest_sha256':fs(manifestp),
    'approval':bind(approvalp),'appended_event_count':78,
    'appended_event_type':'used and rechecked in this run',
    'new_independent_targeted_computation_credit':0,'new_background_or_refutation_credit':0,
    'canonical_source_changed_by_append':False,'defect_log_changed_by_append':False,
    'after_tail_exactly_equals_approved_bundle_rows':True,
    'scope':'Append the root-approved record of actual exposed-proof comparative readings, once per current owning printed statement. No new derivation is performed by this operation.'}
save_json(appendp,append_receipt)
vp=R/'code/S6_SERIES_PUBLISH_I_verify_reread_append.py'
spec=importlib.util.spec_from_file_location('append_verifier',vp);v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
verified=v.verify_append(appendp)
verificationp=R/'records/S6_SERIES_PUBLISH_I_continuation_reread_append_verification.json'
save_json(verificationp,{'recorded_utc':NOW(),'verifier':bind(vp),'result':verified,'mathematical_events_added_by_verification':0})

fresh=recount(R,R.parent/'S6_SERIES_PUBLISH_work')
assert fresh['ledger_sha256']==AFTER_LEDGER and fresh['source_sha256']==BODY
assert fresh['counts']==manifest['counts_after']
assert [fresh['counts'][k] for k in KINDS]==[767,10,143,809,194,1]
assert {x['event_id'] for x in additions}<=set(fresh['selected_event_ids'])
recount_beforep=A/'S6_SERIES_PUBLISH_I_after_append_before_count_recount.json';save_json(recount_beforep,fresh)

# Second operation: the approved numeric metadata change and one appended log row.
changed=text.replace(old,new,1)
assert changed.replace(new,old,1)==text
source_after=changed.encode();at=text.index(old)
for pat in [r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}',r'\\(?:[A-Za-z@]+|.)']:
    assert re.findall(pat,text,re.S)==re.findall(pat,changed,re.S)
change_id='I-02225'
logrow={k:'' for k in log_fields}
logrow.update(change_id=change_id,type='D15',statement_id='section 1.5',
    old_location=f'body-only source line {text.count(chr(10),0,at)+1}; section 1.5; exact printed candidate19 counterpart',
    old_page='16',new_location='section 1.5',new_page='pending candidate20 build',
    old_text=old,new_text=new,
    reason='The approved78-row used-and-rechecked append records actual complete exposed-proof comparisons, deduplicated by current owning statement. A fresh canonical recount changes the readings total731 to809; every other methodology word and number is unchanged. This count-source update itself adds no check-event credit.',
    review_status='applied; root-approved full Methodology block comparison and fresh canonical recount verified; candidate20 changed-page reading pending',
    mapped_old_location='candidate19 section 1.5 count literal on page16; complete unchanged Methodology block spans pages16–17',
    mapped_new_location='pending candidate20 build and changed-page reading',
    page_mapping_method='Immediate before-source '+BODY+' is the body-only state with no PDF. Its exact complete Methodology block equals candidate19 source '+guard['printed_before_source']['sha256']+' and is printed in PDF '+guard['printed_before_pdf']['sha256']+' on pages16–17; the edited literal is on page16. Full-block equality witness: '+guard['methodology_block_sha256_in_both_before_sources']+'.')
stream=io.StringIO(newline='');writer=csv.DictWriter(stream,fieldnames=log_fields,delimiter='\t');writer.writerow(logrow)
log_after=log_before+stream.getvalue().encode()
assert log_after.startswith(log_before)
newlog=table(log_after)[1];assert newlog[:-1]==oldlog and newlog[-1]==logrow and len(newlog)==2225
assert source.read_bytes()==source_before and log.read_bytes()==log_before and fs(ledger)==AFTER_LEDGER
atomic(source,source_after);atomic(log,log_after)
new_source_copy=A/'I_source_after_count.tex';save_copy(new_source_copy,source_after)
change={'guard_id':guard['id'],'change_id':change_id,'type':'D15','statement_id':'section 1.5',
    'old':old,'new':new,'original_offset':at,'applied_offset':at,
    'old_source_line':text.count('\n',0,at)+1,'count_before':731,'count_after':809,
    'full_original_methodology':guard['original_full_block'],'full_proposed_methodology':guard['proposed_full_block'],
    'new_proof_check_credit_from_source_edit':0}
countp=R/'records/S6_SERIES_PUBLISH_I_methodology_count_apply_receipt.json'
count_receipt={'paper':'I','created_utc':NOW(),'mode':'applied','applied':True,
    'before_source_sha256':sha(source_before),'after_source_sha256':fs(source),
    'before_source_snapshot':bind(old_source_copy),'after_source_snapshot':bind(new_source_copy),
    'immediate_before_source_has_no_pdf':True,'printed_before_source':guard['printed_before_source'],
    'printed_before_pdf':guard['printed_before_pdf'],'printed_before_pages':[16,17],
    'count_literal_printed_before_page':16,
    'exact_full_methodology_equal_between_immediate_and_printed_before_sources':True,
    'equal_methodology_before_block_sha256':sha(original_method),
    'before_defect_log_sha256':sha(log_before),'after_defect_log_sha256':fs(log),
    'before_defect_log_snapshot':bind(old_log_copy),'existing_defect_rows':2224,'total_defect_rows':2225,
    'existing_log_bytes_preserved':True,'existing_log_rows_preserved':True,
    'changes':[change],'new_defect_rows':[logrow],
    'exact_whole_source_forward_and_inverse_maps_verified':True,
    'all_source_outside_single_count_substitution_byte_identical':True,
    'all_tex_command_label_and_reference_sequences_identical':True,
    'guard':bind(guardp),'approval':bind(approvalp),'reread_append_receipt':bind(appendp),
    'fresh_canonical_recount_before_source_edit':bind(recount_beforep),
    'ledger_sha256':fs(ledger),'counts':fresh['counts'],
    'mathematical_events_added':0,'new_independent_targeted_computation_credit':0,
    'additional_page_reading_credit':0,'build_performed':False,
    'pending':['Candidate20 clean build and changed-page reading','Final source/PDF/ledger metadata and42-claim coverage binding']}
save_json(countp,count_receipt)
after=recount(R,R.parent/'S6_SERIES_PUBLISH_work')
assert after['counts']==fresh['counts'] and after['selected_event_ids']==fresh['selected_event_ids']
afterp=O/'S6_SERIES_PUBLISH_I_candidate20_recount.json';save_json(afterp,after)
v.verify_append(appendp)
assert fs(source)==sha(source_after) and fs(log)==sha(log_after) and fs(ledger)==AFTER_LEDGER
print(json.dumps({'source_sha256':fs(source),'defect_log_sha256':fs(log),'defect_rows':2225,
    'ledger_sha256':fs(ledger),'ledger_rows':7944,'append_receipt':bind(appendp),
    'append_verification':bind(verificationp),'count_edit_receipt':bind(countp),
    'final_recount':bind(afterp),'counts':after['counts'],'build_performed':False},indent=2))
