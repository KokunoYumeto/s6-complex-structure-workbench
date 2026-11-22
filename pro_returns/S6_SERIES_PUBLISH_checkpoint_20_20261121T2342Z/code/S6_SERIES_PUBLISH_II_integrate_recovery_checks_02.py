"""Admit A02/A03/B03 using durable freezes and new complete comparisons."""
from pathlib import Path
import csv, datetime, hashlib, io, json, sys

R = Path(__file__).resolve().parents[1]
csv.field_size_limit(100_000_000)
O = R / 'records/S6_SERIES_PUBLISH_II_recovery_checks_02'
BUNDLE = R / 'records/S6_SERIES_PUBLISH_zzz_continuation_004_recovery_CHECK_EVENTS.tsv'
sha = lambda b: hashlib.sha256(b).hexdigest()
def bound(p):
    p = R / p if isinstance(p, str) else p
    return dict(path=str(p.relative_to(R)), sha256=sha(p.read_bytes()))
def read(p):
    return json.loads((R / p).read_text())

if '--verify' in sys.argv:
    m = json.loads((O / 'manifest.json').read_text())
    old, new = (O / 'before_ledger.tsv').read_bytes(), (R / 'CHECK_EVENTS.tsv').read_bytes()
    assert sha(old) == m['before_ledger_sha256'] and new.startswith(old)
    before = list(csv.DictReader(io.StringIO(old.decode(), newline=''), delimiter='\t'))
    after = list(csv.DictReader(io.StringIO(new.decode(), newline=''), delimiter='\t'))
    extra = list(csv.DictReader(BUNDLE.open(newline=''), delimiter='\t'))
    assert after[:len(before)] == before and after[len(before):] == extra
    assert len({x['event_id'] for x in after}) == len(after)
    d = dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
             before_rows=len(before), after_rows=len(after), added_rows=len(extra),
             before_ledger_sha256=sha(old), after_ledger_sha256=sha(new),
             whole_old_ledger_byte_prefix_preserved=True, old_rows_unchanged=True,
             new_tail_exactly_bundle=True, all_event_ids_unique=True,
             required_checks_completed=19, manifest=bound(O / 'manifest.json'), bundle=bound(BUNDLE))
    p = O / 'append_verification.json'; assert not p.exists()
    p.write_text(json.dumps(d, indent=2)+'\n'); print(json.dumps(d, indent=2)); sys.exit(0)

assert not O.exists() and not BUNDLE.exists()
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
old = (R / 'CHECK_EVENTS.tsv').read_bytes()
assert sha(old) == '3caee00f4eeabd8940f89d47c981437ea8a16dd6fb9583e4199afa19b0a84013'
reader = csv.DictReader(io.StringIO(old.decode(), newline=''), delimiter='\t')
oldrows, fields = list(reader), reader.fieldnames
source = (R / 'S6_SERIES_PUBLISH_II.tex').read_text()
chain_paths = [
    'records/S6_SERIES_PUBLISH_II_root_recovery_edits_01/apply_receipt.json',
    'records/S6_SERIES_PUBLISH_II_B_recovery_group02_editorial_apply.json',
    'records/S6_SERIES_PUBLISH_II_C_recovery_group02_editorial_apply.json',
    'records/S6_SERIES_PUBLISH_II_A_recovery_groups02_03_apply.json',
    'records/S6_SERIES_PUBLISH_II_B_recovery_group03_editorial_apply.json']
chain = [read(p) for p in chain_paths]
assert chain[0]['source_before_sha256'] == '33e5e01d81b96aed7be0d5af71fc4425537f534af855b5f50d7b3a4b0835c573'
for a, b in zip(chain, chain[1:]):
    assert a['source_after_sha256'] == b['source_before_sha256']
assert chain[-1]['source_after_sha256'] == sha(source.encode())
history = {x[k] for x in chain for k in ['source_before_sha256', 'source_after_sha256']}
historical_bindings = []
def validate(obj):
    if isinstance(obj, dict):
        if 'path' in obj and 'sha256' in obj:
            p = R / obj['path']
            if sha(p.read_bytes()) != obj['sha256']:
                assert p == R / 'S6_SERIES_PUBLISH_II.tex' and obj['sha256'] in history, obj
                historical_bindings.append(obj)
        for v in obj.values(): validate(v)
    elif isinstance(obj, list):
        for v in obj: validate(v)
def freeze_release(fb, rb):
    validate(fb); validate(rb)
    f, r = read(fb['path']), read(rb['path'])
    validate(f); validate(r)
    assert r['freeze_receipt_sha256'] == fb['sha256']
    assert datetime.datetime.fromisoformat(f['created_utc']) < datetime.datetime.fromisoformat(r['created_utc'])
    assert r['statement_owner'] == f['statement_owner']
    assert r['derivation_sha256'] == f['derivation_sha256']
    for key, hkey in [('frozen_derivation_path','derivation_sha256'), ('target_proof_path','target_proof_sha256'), ('packet_path','packet_sha256')]:
        assert sha((R / f[key]).read_bytes()) == f[hkey]
    for key, hkey in [('released_proof_path','released_proof_sha256'), ('full_owning_block_path','full_owning_block_sha256')]:
        assert sha((R / r[key]).read_bytes()) == r[hkey]
    assert r['released_proof_sha256'] == f['target_proof_sha256']
    return f['statement_owner']

events, completed, evidence = [], {}, []
def add(owner, tag, typ, scope, checker, evidence_path, after, completion=False):
    assert typ in ['targeted proof check', 'used and rechecked in this run', 'computation or formal certificate']
    validate(after)
    assert source.count((R / after['path']).read_text()) == 1, owner
    n = len(events)+1
    row = {k: '' for k in fields}
    row.update(statement_id=owner, date='2026-11-21',
               who=f'GPT-6 Astra (OpenAI), ChatGPT Pro mode; reasoning effort inherited, no separate numerical setting exposed; {checker}',
               type=typ, outcome=scope, event_id=f'S6_SERIES_PUBLISH_II_RECOVERY02_{tag}_{n:02d}_20261121',
               phase='S6_SERIES_PUBLISH_II', source_file=evidence_path, source_row=str(n+1),
               source_event_type=typ, evidence_group=f'S6_SERIES_PUBLISH_II_RECOVERY02_{tag}',
               publish_input_file=BUNDLE.name, publish_input_row=str(n+1), date_utc=now, where=evidence_path)
    events.append(row)
    if completion:
        assert owner not in completed
        completed[owner] = scope

ap = 'agents/ii_checks_A/recovery_20261121T195642Z/'
index_path = ap+'S6_SERIES_PUBLISH_II_A_recovery_group02_03_final_index.json'
assert bound(index_path)['sha256'] == 'efff143b63ebd8f3626faef0c678afcd92919a86ecd7cc2d10f8fc45dc68b89e'
evidence.append(index_path)
for group in read(index_path)['groups']:
    for key, hkey in [('manifest','manifest_sha256'), ('reread_record','reread_sha256'), ('event_proposals','events_sha256')]:
        assert bound(group[key])['sha256'] == group[hkey]
        evidence.append(group[key])
    proposals = {x['statement_owner']: x for x in read(group['manifest'])['proposals']}
    for rr in read(group['reread_record'])['records']:
        owner = freeze_release(dict(path=rr['freeze_receipt_path'],sha256=rr['freeze_receipt_sha256']),
                               dict(path=rr['release_receipt_path'],sha256=rr['release_receipt_sha256']))
        assert owner == rr['statement_owner']
        assert rr['full_original_owning_block_read'] and rr['full_proposed_owning_block_read']
        assert sha((R / rr['original_full_block_path']).read_bytes()) == rr['original_full_block_sha256']
        assert sha((R / rr['proposed_full_block_path']).read_bytes()) == rr['proposed_full_block_sha256']
    for e in read(group['event_proposals'])['events']:
        t = proposals[e['statement_id']]
        after = dict(path=t['proposed_block_path'], sha256=t['proposed_block_sha256'])
        add(e['statement_id'], t['tag'], e['type'], e['outcome']+
            ' Exact durable prerelease receipts and freshly dated complete recovery comparisons are bound. Source guards are applied. Recovery adds no invented historical record or extra prereading event.',
            'ii_check_a', group['event_proposals'], after, e['type']=='targeted proof check')
for name in ['S6_SERIES_PUBLISH_II_A_recovery_group02_03_method_runs.json', 'S6_SERIES_PUBLISH_II_A_recovery_01FY_method_runs.json']:
    p = ap+name; d = read(p); evidence.append(p)
    for run in d['runs']:
        assert run['exit_code'] == 0
        assert sha((R / run['program_path']).read_bytes()) == run['program_sha256']
        assert sha((R / run['output_path']).read_bytes()) == run['output_sha256']
for p in ['agents/ii_checks_A/comparisons/S6_SERIES_PUBLISH_II_A_group02_comparisons.md',
          ap+'S6_SERIES_PUBLISH_II_A_recovery_group03_comparisons.md',
          ap+'S6_SERIES_PUBLISH_II_A_recovery_group02_03_method_addendum.md',
          ap+'S6_SERIES_PUBLISH_II_A_recovery_primary_and_exposure_record.md']:
    evidence.append(p)

bp = 'agents/ii_checks_provenance/recovery_20261121T2000Z/group03/S6_SERIES_PUBLISH_II_B_group03_recovery_proposals.json'
be = 'agents/ii_checks_provenance/recovery_20261121T2000Z/group03/S6_SERIES_PUBLISH_II_B_group03_recovery_event_proposals.json'
assert bound(bp)['sha256'] == '2801a84e116c4a91e4679c183e9dd2191a6fe3b7e74d66ed10fd06ea83170f6b'
assert bound(be)['sha256'] == '87d971795c76d56e4cfe7849a95e70752503bf6f071f14d4b16c5472dc856d5d'
b, ev = read(bp), read(be); validate(b); validate(ev)
evidence.extend([bp, be, b['recovery_transports']['path'], b['primary_retrieval']['path']])
validate(read(b['primary_retrieval']['path']))
for t in b['targets']:
    assert freeze_release(t['freeze_receipt'], t['new_release_receipt']) == t['statement_owner']
    assert t['actual_complete_original_proof_read_in_recovery'] and t['actual_complete_final_proposed_proof_read_in_recovery']
for e in ev['events']:
    typ = {'used and rechecked': 'used and rechecked in this run'}.get(e['event_type'],e['event_type'])
    add(e['statement_owner'], e['tag'], typ, e['scope']+
        ' The original prerelease derivation and freeze survive CP14; this fresh recovery comparison follows historical proof exposure. The recorded AP local-domain and AX fixed-tube draft issues were settled during comparison, with no change to the printed theorem. The exact literal source guards are applied.',
        'i_provenance', be, e['proposed_full_block'], typ=='targeted proof check')
assert len(completed) == 19 and len(events) == 40
mp = R / 'records/S6_SERIES_PUBLISH_required_check_completion_manifest.json'
mold = mp.read_bytes(); completion = json.loads(mold)
assert not set(completed) & set(completion['rows'])
assert not {e['event_id'] for e in events} & {e['event_id'] for e in oldrows}
O.mkdir(); (O / 'before_ledger.tsv').write_bytes(old); (O / 'before_completion_manifest.json').write_bytes(mold)
with BUNDLE.open('w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fields, delimiter='\t'); w.writeheader(); w.writerows(events)
m = dict(schema=1, created_utc=now, approved=True, paper='II', before_ledger_sha256=sha(old),
         event_bundle=bound(BUNDLE), events=len(events), completed_owners=list(completed),
         source_sha256=sha(source.encode()), source_application_chain=[bound(p) for p in chain_paths],
         evidence=[bound(p) for p in evidence], historical_source_bindings_validated_via_exact_apply_chain=historical_bindings,
         event_type_spelling_map={'used and rechecked':'used and rechecked in this run'},
         recovery_scope='Nineteen original frozen checks admitted with fresh complete comparison evidence. Three actual exact-computation events and eighteen complete editorial rereadings are separately classified. No lost post-checkpoint freeze is reconstructed.',
         visual_reading_credit=0)
(O / 'manifest.json').write_text(json.dumps(m, indent=2)+'\n')
for owner, scope in completed.items():
    completion['rows'][owner] = dict(paper='II', status='done', recorded_utc=now,
                                   evidence_path=str((O / 'manifest.json').relative_to(R)),
                                   evidence_sha256=sha((O / 'manifest.json').read_bytes()), scope=scope)
completion['updated_utc'] = now; mp.write_text(json.dumps(completion, indent=2)+'\n')
print(json.dumps(dict(manifest=bound(O / 'manifest.json'), events=len(events), required_checks_completed=len(completed)), indent=2))
