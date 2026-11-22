#!/usr/bin/env python3
"""Reconstruct candidate17 from exactly the 48 applied edits and recount; no final guard."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
from S6_SERIES_PUBLISH_I_cont_recount import recount, KINDS
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
OLD_SHA='61ffa2e316814c140fc69723e080b4414ea4016ba27e0ac84bd2d9347fbc93fc'
NEW_SHA='5b74359a048b1eab3e478a65eab35f35b45474c4c65aadaedd639315c19a9379'
LEDGER_SHA='e45bf7b52aff58c0d9fb4a474cd97e9dd7615c761c4a1a79983e268bd27fe714'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
bind=lambda p:{'path':str(p.relative_to(ROOT)),'sha256':sha(p),'bytes':p.stat().st_size}
put=lambda p,v:p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
source=ROOT/'S6_SERIES_PUBLISH_I.tex';ledger=ROOT/'CHECK_EVENTS.tsv'
old_source=OUT/'candidate16_review_blocks/S6_SERIES_PUBLISH_I_candidate16_source_snapshot.tex'
receipt_path=ROOT/'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate16_combined_apply_receipt.json'
assert sha(receipt_path)=='8947b7e89114276fd82e808c1cd5e329dd0000af5ac827f82e8b6f0bb65b9a9d'
receipt=json.loads(receipt_path.read_text())
assert sha(old_source)==OLD_SHA==receipt['before_source_sha256']
assert sha(source)==NEW_SHA==receipt['after_source_sha256']
assert sha(ledger)==LEDGER_SHA
before=old_source.read_text();after=source.read_text();mapped=before
for c in receipt['changes']:
    assert mapped.count(c['old'])==1,c['guard_id']
    mapped=mapped.replace(c['old'],c['new'],1)
assert len(receipt['changes'])==48 and mapped==after
prior_path=OUT/'S6_SERIES_PUBLISH_I_candidate16_recount.json'
prior=json.loads(prior_path.read_text())
fresh=recount(ROOT,ROOT.parent/'S6_SERIES_PUBLISH_work')
assert fresh['source_sha256']==NEW_SHA and fresh['ledger_sha256']==LEDGER_SHA
assert fresh['counts']==prior['counts']
for k in ['selected_ledger_rows','selected_event_ids','declared_evidence_groups']:
    assert fresh[k]==prior[k],k
keys=['id','kind','identities']
assert [{k:s[k] for k in keys} for s in fresh['statements']]==[{k:s[k] for k in keys} for s in prior['statements']]
assert fresh['counts']['statements']==333
assert [fresh['counts'][k] for k in KINDS]==[767,10,143,731,194,1]
fresh_path=OUT/'S6_SERIES_PUBLISH_I_candidate17_recount.json'
put(fresh_path,fresh)
pat=r'\\subsection\{Methodology\}\s*(.*?)\s*\\subsection\{How the paper is organized\}'
assert re.search(pat,before,re.S)[1]==re.search(pat,after,re.S)[1]
prior_claims_path=OUT/'candidate14/S6_SERIES_PUBLISH_I_cont_three_way_claims.json'
claims=json.loads(prior_claims_path.read_text());status=[]
for section,entries in claims['exact_main_status_binding'].items():
    for kind,row in entries.items():
        assert after.count(row['text'])==1
        status.append({'section':section,'kind':kind,'text':row['text'],'occurrences':1})
assert len(status)==21
result={
 'created_utc':datetime.now(timezone.utc).isoformat(),'paper':'I','candidate':17,
 'source':bind(source),'ledger':bind(ledger),'candidate16_source_snapshot':bind(old_source),
 'candidate17_source_snapshot':bind(OUT/'candidate17_review_blocks/S6_SERIES_PUBLISH_I_candidate17_source_snapshot.tex'),
 'source_edit_receipt':bind(receipt_path),'exact_whole_source_reconstruction_from_48_edits':True,
 'applied_guard_ids':[c['guard_id'] for c in receipt['changes']],
 'candidate16_recount':bind(prior_path),'candidate17_recount':bind(fresh_path),
 'counts':fresh['counts'],'printed_statement_identity_sequence_unchanged':True,
 'selected_ledger_row_sequence_unchanged':True,'selected_event_id_sequence_unchanged':True,
 'declared_evidence_group_sequence_unchanged':True,'methodology_bytes_unchanged':True,
 'main_status_string_bindings':status,'source_status_strings_verified':21,
 'source_difference_review':'Read the full 48-change applied receipt; independently reconstructed all current source bytes from the frozen candidate16 source using exactly the recorded replacements. Recomputed printed statements, identifiers, associations and declared groups against the unchanged CHECK_EVENTS ledger.',
 'all_42_claims_finalized':False,'final_42_claim_guard_generated':False,
 'remaining_gate':'Candidate17 source is settled. Final claim closure requires its PDF occurrence correspondence and certified complete page coverage.',
 'mathematical_events_added':0,'page_reading_credit_added':0,'shared_files_modified':False}
dest=OUT/'S6_SERIES_PUBLISH_I_candidate17_source_count_rebinding.json';put(dest,result)
assert sha(source)==NEW_SHA and sha(ledger)==LEDGER_SHA
print(json.dumps({'receipt':str(dest.relative_to(ROOT)),'sha256':sha(dest),'counts':fresh['counts'],
                  'source_status_strings_verified':21,'final_42_claim_guard_generated':False},indent=2))
