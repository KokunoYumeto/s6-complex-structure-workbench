"""Admit five fresh post-reset derivations with exact original/proposed comparisons."""
from pathlib import Path
import csv, datetime, hashlib, io, json, sys

R = Path(__file__).resolve().parents[1]
csv.field_size_limit(100_000_000)
O = R / 'records/S6_SERIES_PUBLISH_II_clean_checks_01'
BUNDLE = R / 'records/S6_SERIES_PUBLISH_zzz_continuation_005_clean_CHECK_EVENTS.tsv'
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
             required_checks_completed=5, manifest=bound(O / 'manifest.json'), bundle=bound(BUNDLE))
    p = O / 'append_verification.json'; assert not p.exists()
    p.write_text(json.dumps(d, indent=2)+'\n'); print(json.dumps(d, indent=2)); sys.exit(0)

assert not O.exists() and not BUNDLE.exists()
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
old = (R / 'CHECK_EVENTS.tsv').read_bytes()
assert sha(old) == 'c6c3bbd3355b890af7058537c353c97d7d3438f7bc0db096f686b0b120b0e777'
reader = csv.DictReader(io.StringIO(old.decode(), newline=''), delimiter='\t')
oldrows, fields = list(reader), reader.fieldnames
source = (R / 'S6_SERIES_PUBLISH_II.tex').read_text()
chain_paths = [
    'records/S6_SERIES_PUBLISH_II_root_recovery_edits_01/apply_receipt.json',
    'records/S6_SERIES_PUBLISH_II_B_recovery_group02_editorial_apply.json',
    'records/S6_SERIES_PUBLISH_II_C_recovery_group02_editorial_apply.json',
    'records/S6_SERIES_PUBLISH_II_A_recovery_groups02_03_apply.json',
    'records/S6_SERIES_PUBLISH_II_B_recovery_group03_editorial_apply.json',
    'records/S6_SERIES_PUBLISH_II_natbib_fix_01_apply.json',
    'records/S6_SERIES_PUBLISH_II_clean_checks_01_editorial_apply.json']
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
               type=typ, outcome=scope, event_id=f'S6_SERIES_PUBLISH_II_CLEAN01_{tag}_{n:02d}_20261121',
               phase='S6_SERIES_PUBLISH_II', source_file=evidence_path, source_row=str(n+1),
               source_event_type=typ, evidence_group=f'S6_SERIES_PUBLISH_II_CLEAN01_{tag}',
               publish_input_file=BUNDLE.name, publish_input_row=str(n+1), date_utc=now, where=evidence_path)
    events.append(row)
    if completion:
        assert owner not in completed
        completed[owner] = scope

bp = 'agents/ii_checks_provenance/recovery_20261121T2000Z/clean_group01/S6_SERIES_PUBLISH_II_clean_group01_final_proposals.json'
be = 'agents/ii_checks_provenance/recovery_20261121T2000Z/clean_group01/S6_SERIES_PUBLISH_II_clean_group01_event_proposals.json'
assert bound(bp)['sha256'] == '9acaef2ff18edeecaa4bceb7e98b5362e7e055682110f397839f966d4e176672'
assert bound(be)['sha256'] == 'f071a83d0730ccca8f97b5412ac588c347d0db5985554126fc88435573fb769b'
b, ev = read(bp), read(be); validate(b); validate(ev); evidence.extend([bp, be])
for t in b['targets']:
    assert freeze_release(t['freeze_receipt'],t['release_receipt']) == t['statement_owner']
    assert t['actual_complete_original_proof_read'] and t['actual_complete_proposed_proof_read']
for e in ev['events']:
    typ = {'used and rechecked':'used and rechecked in this run'}.get(e['event_type'],e['event_type'])
    add(e['statement_owner'],e['tag'],typ,e['scope']+
        ' This is a new preproof derivation by a checker unexposed to the target, followed by a complete printed-proof comparison and complete original/proposed rereading. Source guards are applied. The FC all-m lens-space computation is explicitly postrelease and receives no extra independent event.',
        'i_provenance_recovery',be,e['proposed_full_block'],typ=='targeted proof check')
cp = 'agents/ii_infra/recovery_20261121/S6_SERIES_PUBLISH_II_WJ_WL_comparison.json'
ce = 'agents/ii_infra/recovery_20261121/S6_SERIES_PUBLISH_II_WJ_WL_event_proposals.json'
assert bound(cp)['sha256'] == 'b97905d45a7e4047dd577ba70c26e344ffbc4ddb734f404a819d7a2041001e5e'
assert bound(ce)['sha256'] == 'f313286fa50f188173f0334549dfd40f891ae7b828c12c06adc4b567266263e1'
c, cev = read(cp), read(ce); validate(c); validate(cev); evidence.extend([cp,ce])
checks = {x['statement_id']:x for x in c['checks']}
for e in cev['events']:
    owner=freeze_release(e['freeze_receipt'],e['release_receipt']);assert owner==e['statement_id']
    t=checks[owner];assert t['actual_full_original_and_v2_proposed_reading'] and t['actual_every_printed_step_comparison']
    assert not t['unresolved_mathematical_issue']
    scope=e['outcome'].replace('Root review/application and final block binding pending.','Root review and exact source application are complete; final full-block bytes are bound.')
    scope+=' The WJ coherent formal-functions step includes all infinitesimal fibres without a flatness premise. WL includes exact compact cyclic quotients, an explicit inverse on the normalized quotient, and conductor algebras stated only analytically locally. The prerelease and postrelease computations have separate timestamps and method comparisons.'
    add(owner,e['tag'],'targeted proof check',scope,'restore_build_recovery',ce,e['proposed_full_block'],True)
    add(owner,e['tag'],'used and rechecked in this run','Actually read both complete original and final v2 statement/proof blocks and the complete program-table pair. The exact hypothesis and citation changes, coherent infinitesimal-fibre argument, and explicit compact conductor constructions were compared with their source claims. No extra independent derivation is assigned for this editorial reading.','restore_build_recovery',cp,e['proposed_full_block'])
assert len(completed)==5 and len(events)==10
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
         recovery_scope='Five fresh prereading derivations by newly assigned unexposed checkers are admitted, with five actual complete editorial rereadings. Old lost freezes are not reconstructed; computational supplements retain their actual pre- or postrelease timing.',
         visual_reading_credit=0)
(O / 'manifest.json').write_text(json.dumps(m, indent=2)+'\n')
for owner, scope in completed.items():
    completion['rows'][owner] = dict(paper='II', status='done', recorded_utc=now,
                                   evidence_path=str((O / 'manifest.json').relative_to(R)),
                                   evidence_sha256=sha((O / 'manifest.json').read_bytes()), scope=scope)
completion['updated_utc'] = now; mp.write_text(json.dumps(completion, indent=2)+'\n')
print(json.dumps(dict(manifest=bound(O / 'manifest.json'), events=len(events), required_checks_completed=len(completed)), indent=2))
