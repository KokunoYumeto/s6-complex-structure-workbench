#!/usr/bin/env python3
"""Record the root model's reviewed exact event append and count-only source edit."""
from pathlib import Path
import datetime,hashlib,json
R=Path(__file__).resolve().parents[1];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
mp=R/'agents/i_cont_provenance/continuation_reread_append/S6_SERIES_PUBLISH_I_continuation_reread_manifest.json'
assert sha(mp)=='55272839a98d16e54e57280775f07caa2bdbd78609647186fe8cf39c94fff408';m=json.loads(mp.read_text())
vp=R/'records/S6_SERIES_PUBLISH_I_reread_manifest_final_validation.json';v=json.loads(vp.read_text());assert v['manifest']['sha256']==sha(mp) and v['unique_printed_owners']==78 and v['actual_comparison_instances']==124 and v['exact_old_ledger_prefix_and_tail']
gp=R/m['methodology_count_guard']['path'];assert sha(gp)=='25aef473e8d88ffe1d6527bb1a98be73ce0c2ad101412bce7b01d5b6c64574df';g=json.loads(gp.read_text())
x=(R/g['original_full_block']['path']).read_text();y=(R/g['proposed_full_block']['path']).read_text()
assert hashlib.sha256(x.encode()).hexdigest()=='631ac5d190095f6d944d37719020c053c4f8bd49f560f03b9ca16dd6634b0ad5'
assert x.count(g['old'])==1 and x.replace(g['old'],g['new'],1)==y
assert g['old']=='It also records 731 readings of the proofs and applications,'
assert g['new']=='It also records 809 readings of the proofs and applications,'
source=R/'S6_SERIES_PUBLISH_I.tex';ledger=R/'CHECK_EVENTS.tsv'
assert sha(source)=='d3922ad95bbc654a42424abfc27f9e05d18e3a0850b20a31d02bea19ac449f4a'
assert sha(ledger)=='e45bf7b52aff58c0d9fb4a474cd97e9dd7615c761c4a1a79983e268bd27fe714'
assert source.read_text().count(x)==1
record={'approved':True,'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'approver':'GPT-6 Astra (OpenAI), ChatGPT Pro mode; root model in the continuation','manifest_path':str(mp.relative_to(R)),'manifest_sha256':sha(mp),'event_type':'used and rechecked in this run','approved_event_count':78,'new_independent_targeted_computation_credit':0,'new_background_or_refutation_credit':0,'before_ledger_sha256':sha(ledger),'approved_after_ledger_sha256':m['prospective_after_ledger_sha256'],'approved_after_rows':7944,'event_bundle_sha256':m['proposal_event_bundle']['sha256'],'root_review':'Root read every one of the78 current owning-statement associations, all19 distinct actual comparison-scope descriptions, their124-instance mapping, all excluded scopes and both exact label/header/aux alias maps. Root reviewed the complete v2-to-final difference record and verified all event, comparison, exclusion, alias and count fields remained identical. The final validation verifies342 bound files, exact owning source environments, individual manual attestations, complete proof archive boundaries and hashes, and the exact preserved7866-row prefix plus78-row tail. This approval assigns the recorded exposed-proof comparison scope only; no human review or independent mathematical derivation is claimed.','validation':{'path':str(vp.relative_to(R)),'sha256':sha(vp)},'methodology_count_edit':{'approved':True,'guard':{'path':str(gp.relative_to(R)),'sha256':sha(gp)},'before_source_sha256':sha(source),'root_review':'Root read the complete current methodology block and compared the single731-to809 substitution; its full proposed block equals exactly that substitution. Apply after the approved event append and a fresh canonical recount. The printed before-source/PDF remain the separately identified candidate19 scope.','new_check_credit':0},'canonical_source_mutated_by_approval':False,'canonical_ledger_mutated_by_approval':False}
p=R/'records/S6_SERIES_PUBLISH_I_reread_append_root_approval.json';assert not p.exists();p.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'approval':str(p.relative_to(R)),'sha256':sha(p),'events':78,'ledger_rows_after':7944,'count_edit':g['new']},indent=2))
