#!/usr/bin/env python3
"""Read-only source19 reconstruction/recount, with exact recorded exceptions."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re
from S6_SERIES_PUBLISH_I_cont_recount import recount, KINDS

R = Path(__file__).resolve().parents[2]
O = Path(__file__).resolve().parent
OLD = '3542f2632cad8f1eb78f0f30f8a64ca91998f3bd1d97010ca76d89297c4bffe7'
NEW = 'f9e40fb592eb7f5c6d48070ba207e93d5b48ca71432176202041b88dd01278f7'
LEDGER = 'e45bf7b52aff58c0d9fb4a474cd97e9dd7615c761c4a1a79983e268bd27fe714'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
digest = lambda s: hashlib.sha256(s.encode()).hexdigest()
bind = lambda p: {'path': str(p.relative_to(R)), 'sha256': sha(p)}
def put(p, x):
    assert not p.exists(), str(p)
    p.write_text(json.dumps(x, ensure_ascii=False, indent=2)+'\n')

src = R/'S6_SERIES_PUBLISH_I.tex'
old = O/'candidate18_review_blocks/S6_SERIES_PUBLISH_I_candidate18_source_snapshot.tex'
rp = R/'agents/continuation_infra/S6_SERIES_PUBLISH_I_candidate18_combined_apply_receipt.json'
j = json.loads(rp.read_text())
assert sha(src) == NEW == j['after_source_sha256']
assert sha(old) == OLD == j['before_source_sha256']
assert sha(R/'CHECK_EVENTS.tsv') == LEDGER == j['check_ledger_sha256']
before, after = old.read_text(), src.read_text()
cs = sorted(j['changes'], key=lambda c:c['original_offset'])
assert len(cs) == len({c['guard_id'] for c in cs}) == 21
assert all(a['original_offset']+len(a['old']) <= b['original_offset'] for a,b in zip(cs,cs[1:]))
forward = before
for c in reversed(cs):
    n=c['original_offset']; assert before[n:n+len(c['old'])] == c['old']
    assert before.count(c['old']) == 1
    forward=forward[:n]+c['new']+forward[n+len(c['old']):]
assert forward == after
offsets, delta = {}, 0
for c in cs:
    offsets[c['guard_id']] = c['original_offset']+delta
    delta += len(c['new'])-len(c['old'])
inverse=after
for c in reversed(cs):
    n=offsets[c['guard_id']]; assert after[n:n+len(c['new'])] == c['new']
    inverse=inverse[:n]+c['old']+inverse[n+len(c['new']):]
assert inverse == before
for a in j['archives']:
    for k in ['original','proposed','diff']: assert sha(R/a[k]) == a[k+'_sha256']
    assert before.count((R/a['original']).read_text()) == 1
    assert after.count((R/a['proposed']).read_text()) == 1
for w in j['retained_witnesses']:
    assert digest(w['exact_text']) == w['sha256']
    assert before.count(w['exact_text']) == after.count(w['exact_text']) >= 1
assert set(j['exact_inline_exceptions']) == {'I18-edits-01','I18-edits-03'}
assert {x['guard_id'] for x in j['exact_reference_exceptions']} == {'I18-prov-03','I18-root-05'}
for key,pat in {'labels':r'\\label\{([^}]+)\}','targets':r'\\hypertarget\{([^}]+)\}','bibkeys':r'\\bibitem\[[\s\S]*?\]\{([^}]+)\}'}.items():
    assert re.findall(pat,before) == re.findall(pat,after), key
fresh=recount(R,R.parent/'S6_SERIES_PUBLISH_work')
prior=json.loads((O/'S6_SERIES_PUBLISH_I_candidate18_recount.json').read_text())
assert fresh['counts'] == prior['counts']
assert [fresh['counts'][k] for k in KINDS] == [767,10,143,731,194,1]
for k in ['selected_ledger_rows','selected_event_ids','declared_evidence_groups']:
    assert fresh[k] == prior[k]
assert [[x[k] for k in ['id','kind','identities']] for x in fresh['statements']] == [[x[k] for k in ['id','kind','identities']] for x in prior['statements']]
method=r'\\subsection\{Methodology\}.*?(?=\\subsection\{How the paper is organized\})'
assert re.search(method,before,re.S)[0] == re.search(method,after,re.S)[0]
sd=O/'candidate19_review_blocks'; sd.mkdir(exist_ok=True)
snapshot=sd/'S6_SERIES_PUBLISH_I_candidate19_source_snapshot.tex'
if snapshot.exists(): assert sha(snapshot)==NEW
else: snapshot.write_bytes(src.read_bytes())
cp=O/'S6_SERIES_PUBLISH_I_candidate19_recount.json';put(cp,fresh)
result={'recorded_utc':datetime.now(timezone.utc).isoformat(),'paper':'I','candidate':19,
    'source':bind(src),'source19_snapshot':bind(snapshot),'before_source':bind(old),
    'source_edit_receipt':bind(rp),'ledger':bind(R/'CHECK_EVENTS.tsv'),
    'exact_whole_source_forward_and_inverse_reconstruction':True,
    'applied_guard_ids':[x['guard_id'] for x in cs],
    'complete_archive_count':len(j['archives']),
    'all_archive_hashes_and_unique_source_matches_verified':True,
    'retained_witnesses_verified':j['retained_witnesses'],
    'exact_inline_exceptions':j['exact_inline_exceptions'],
    'exact_reference_exceptions':j['exact_reference_exceptions'],
    'preservation_scope':j['inline_math_difference']+' '+j['reference_difference']+' Text accent commands disappear only with the named deleted text; no whole-source command identity is asserted.',
    'recount':bind(cp),'counts':fresh['counts'],'printed_identity_sequence_preserved':True,
    'selected_events_and_declared_evidence_groups_preserved':True,
    'methodology_block_byte_identical':True,
    'all_42_claims_finalized':False,'final_42_claim_guard_generated':False,
    'remaining_gate':'Final source/ledger after the explicitly attested proof-reread append, final PDF, and certified full image coverage.',
    'mathematical_events_added':0,'page_reading_credit_added':0,'shared_files_modified':False}
dest=O/'S6_SERIES_PUBLISH_I_candidate19_source_count_rebinding.json';put(dest,result)
assert sha(src)==NEW and sha(R/'CHECK_EVENTS.tsv')==LEDGER
print(json.dumps({'receipt':str(dest.relative_to(R)),'sha256':sha(dest),'counts':fresh['counts']},indent=2))
