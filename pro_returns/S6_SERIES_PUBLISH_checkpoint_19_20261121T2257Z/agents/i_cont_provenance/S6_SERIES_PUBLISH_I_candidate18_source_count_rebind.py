#!/usr/bin/env python3
"""Bind candidate18 to the exact 109 applied changes and independently recount.

Writes only agent evidence. Historical candidate17 records remain immutable.
No whole-source reference-order or inline-math identity is asserted: the two
documented relocation/duplicate-scope exceptions are checked explicitly.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
from S6_SERIES_PUBLISH_I_cont_recount import recount, KINDS

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
OLD_SHA = '5b74359a048b1eab3e478a65eab35f35b45474c4c65aadaedd639315c19a9379'
NEW_SHA = '3542f2632cad8f1eb78f0f30f8a64ca91998f3bd1d97010ca76d89297c4bffe7'
LEDGER_SHA = 'e45bf7b52aff58c0d9fb4a474cd97e9dd7615c761c4a1a79983e268bd27fe714'
RECEIPT_SHA = 'dfe3f0e522ce67c75188604ab3ce8dc42f3ec803be3dc8c8eeabba637496c275'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
digest = lambda text: hashlib.sha256(text.encode()).hexdigest()
bind = lambda p: {'path':str(p.relative_to(ROOT)), 'sha256':sha(p), 'bytes':p.stat().st_size}

def put(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

source = ROOT / 'S6_SERIES_PUBLISH_I.tex'
ledger = ROOT / 'CHECK_EVENTS.tsv'
old_source = OUT / 'candidate17_review_blocks/S6_SERIES_PUBLISH_I_candidate17_source_snapshot.tex'
receipt_path = ROOT / 'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate17_combined_apply_receipt.json'
assert sha(receipt_path) == RECEIPT_SHA
receipt = json.loads(receipt_path.read_text())
assert sha(old_source) == OLD_SHA == receipt['before_source_sha256']
assert sha(source) == NEW_SHA == receipt['after_source_sha256']
assert sha(ledger) == LEDGER_SHA == receipt['check_ledger_sha256']
before, after = old_source.read_text(), source.read_text()
changes = receipt['changes']
assert len(changes) == 109 and len({c['guard_id'] for c in changes}) == 109
ordered = sorted(changes, key=lambda c:c['original_offset'])
assert all(a['original_offset'] + len(a['old']) <= b['original_offset'] for a,b in zip(ordered,ordered[1:]))
mapped = before
for c in reversed(ordered):
    start = c['original_offset']
    assert before[start:start+len(c['old'])] == c['old'], c['guard_id']
    assert before.count(c['old']) == 1, c['guard_id']
    mapped = mapped[:start] + c['new'] + mapped[start+len(c['old']):]
assert mapped == after, 'Recorded replacements do not reconstruct every current source byte.'
inverse = after
final_offsets = {}
delta = 0
for c in ordered:
    final_offsets[c['guard_id']] = c['original_offset'] + delta
    delta += len(c['new']) - len(c['old'])
for c in reversed(ordered):
    start = final_offsets[c['guard_id']]
    assert after[start:start+len(c['new'])] == c['new'], c['guard_id']
    inverse = inverse[:start] + c['old'] + inverse[start+len(c['new']):]
assert inverse == before, 'Recorded inverse replacements do not reconstruct candidate17.'

for gf in receipt['guard_files']:
    assert sha(ROOT / gf['path']) == gf['sha256']
assert len(receipt['archives']) == 92
for archive in receipt['archives']:
    for name in ('original','proposed','diff'):
        assert sha(ROOT / archive[name]) == archive[name+'_sha256']
    assert before.count((ROOT / archive['original']).read_text()) == 1, archive['statement_id']
    assert after.count((ROOT / archive['proposed']).read_text()) == 1, archive['statement_id']

exceptions = [c for c in changes if c['declared_reference_order_change'] or c['declared_duplicate_scope_removal']]
assert {c['guard_id'] for c in exceptions} == {'I17-edits-02','I17-infra-D11-01'}
assert [c['guard_id'] for c in changes if not c['inline_math_segments_identical']] == ['I17-infra-D11-01']
assert all(c['display_math_segments_identical'] for c in changes)
assert next(c for c in exceptions if c['guard_id']=='I17-infra-D11-01')['removed_inline_mentions_in_prose'] == [r'$\mathcal V$']
for witness in receipt['retained_duplicate_scope_witnesses']:
    assert digest(witness['exact_text']) == witness['sha256']
    assert before.count(witness['exact_text']) == after.count(witness['exact_text']) == 1

for name, pattern in {
    'labels':r'\\label\{([^}]+)\}',
    'targets':r'\\hypertarget\{([^}]+)\}',
    'bibliography_keys':r'\\bibitem\[[\s\S]*?\]\{([^}]+)\}',
}.items():
    assert re.findall(pattern,before) == re.findall(pattern,after), name

prior_path = OUT / 'S6_SERIES_PUBLISH_I_candidate17_recount.json'
prior = json.loads(prior_path.read_text())
fresh = recount(ROOT, ROOT.parent / 'S6_SERIES_PUBLISH_work')
assert fresh['source_sha256'] == NEW_SHA and fresh['ledger_sha256'] == LEDGER_SHA
assert fresh['counts'] == prior['counts']
for key in ['selected_ledger_rows','selected_event_ids','declared_evidence_groups']:
    assert fresh[key] == prior[key], key
keys = ['id','kind','identities']
assert [{k:s[k] for k in keys} for s in fresh['statements']] == [{k:s[k] for k in keys} for s in prior['statements']]
assert fresh['counts']['statements'] == 333
assert [fresh['counts'][k] for k in KINDS] == [767,10,143,731,194,1]
fresh_path = OUT / 'S6_SERIES_PUBLISH_I_candidate18_recount.json'
put(fresh_path, fresh)
pat = r'\\subsection\{Methodology\}\s*(.*?)\s*\\subsection\{How the paper is organized\}'
assert re.search(pat,before,re.S)[1] == re.search(pat,after,re.S)[1]
prior_claims_path = OUT / 'candidate17_source/S6_SERIES_PUBLISH_I_cont_three_way_claims.json'
claims = json.loads(prior_claims_path.read_text())
status = []
for section, entries in claims['exact_main_status_binding'].items():
    for kind, row in entries.items():
        assert after.count(row['text']) == 1
        status.append({'section':section,'kind':kind,'text':row['text'],'occurrences':1})
assert len(status) == 21

snapshot_dir = OUT / 'candidate18_review_blocks'
snapshot_dir.mkdir(exist_ok=True)
snapshot = snapshot_dir / 'S6_SERIES_PUBLISH_I_candidate18_source_snapshot.tex'
if snapshot.exists():
    assert snapshot.read_bytes() == source.read_bytes()
else:
    snapshot.write_bytes(source.read_bytes())

result = {
    'created_utc':datetime.now(timezone.utc).isoformat(),'paper':'I','candidate':18,
    'source':bind(source),'ledger':bind(ledger),'candidate17_source_snapshot':bind(old_source),
    'candidate18_source_snapshot':bind(snapshot),'source_edit_receipt':bind(receipt_path),
    'exact_whole_source_forward_and_inverse_reconstruction_from_109_edits':True,
    'all_92_before_after_archive_hashes_and_unique_source_matches_verified':True,
    'applied_guard_ids':[c['guard_id'] for c in changes],
    'candidate17_recount':bind(prior_path),'candidate18_recount':bind(fresh_path),
    'counts':fresh['counts'],'printed_statement_identity_sequence_unchanged':True,
    'selected_ledger_row_sequence_unchanged':True,'selected_event_id_sequence_unchanged':True,
    'declared_evidence_group_sequence_unchanged':True,'methodology_bytes_unchanged':True,
    'main_status_string_bindings':status,'source_status_strings_verified':21,
    'exact_scope_and_reference_exceptions':exceptions,
    'duplicate_scope_witnesses_verified_unchanged':receipt['retained_duplicate_scope_witnesses'],
    'preservation_qualification':'All 109 approved literal changes reconstruct the complete source in both directions. One repeated mathcal V mention and one repeated push:src:B.4.12 reference are removed from the Euler remark; the object, normal-line identities, noncompactness conclusion and reasons remain in the two exact Proposition22.29 witnesses. I17-edits-02 moves the same period/height convention and definition reference across the proposition header. No blanket inline-math, whole-statement-byte or reference-order identity is asserted.',
    'record_computation_scope':'Independent exact byte reconstruction and fresh printed-identity/ledger recount. Complete proof-reading evidence belongs to the named prior reviewers; this computation creates no independent mathematical check.',
    'all_42_claims_finalized':False,'final_42_claim_guard_generated':False,
    'remaining_gate':'Candidate18 final PDF occurrence correspondence and certified complete page coverage.',
    'mathematical_events_added':0,'page_reading_credit_added':0,'shared_files_modified':False,
    'protected_candidate17_records_modified':False,
}
dest = OUT / 'S6_SERIES_PUBLISH_I_candidate18_source_count_rebinding.json'
put(dest,result)
assert sha(source) == NEW_SHA and sha(ledger) == LEDGER_SHA
print(json.dumps({'receipt':str(dest.relative_to(ROOT)),'sha256':sha(dest),'counts':fresh['counts'],
                  'exact_forward_and_inverse_maps':True,'exceptions':[c['guard_id'] for c in exceptions],
                  'source_status_strings_verified':21,'final_42_claim_guard_generated':False},indent=2))
