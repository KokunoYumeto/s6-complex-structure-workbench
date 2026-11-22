"""Admit a separate frozen dependency check, preserving the 197-row index and completion map."""
from pathlib import Path
import csv,datetime,hashlib,io,json,sys
R=Path(__file__).resolve().parents[1]
csv.field_size_limit(100_000_000)
def sha(x):return hashlib.sha256(x).hexdigest()
def read(p):return json.loads((R/p).read_text())
def bound(p):return dict(path=str(p),sha256=sha((R/p).read_bytes()))
def rows(data):return list(csv.DictReader(io.StringIO(data.decode(),newline=''),delimiter='\t'))
cfg=sys.argv[1];c=read(cfg);O=R/c['record_directory'];B=R/c['event_bundle']
mp=R/'records/S6_SERIES_PUBLISH_required_check_completion_manifest.json'
assert c['independent_checks']==0 and c['additional_independent_checks']==1
index=c['immutable_required_index'];assert bound(index['path'])==index
ix=read(index['path']);assert len(ix['candidates'])==197
required={x['statement_owner'] for x in ix['candidates']}
if '--verify' in sys.argv:
    m=read(str((O/'manifest.json').relative_to(R)))
    old=(O/'before_ledger.tsv').read_bytes();new=(R/'CHECK_EVENTS.tsv').read_bytes()
    a,z,q=rows(old),rows(new),rows(B.read_bytes())
    assert new.startswith(old) and z[:len(a)]==a and z[len(a):]==q
    assert len({x['event_id'] for x in z})==len(z)
    assert mp.read_bytes()==(O/'before_completion_manifest.json').read_bytes()
    assert bound(index['path'])==index
    v=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        before_rows=len(a),after_rows=len(z),added_rows=len(q),before_ledger_sha256=sha(old),after_ledger_sha256=sha(new),
        whole_old_ledger_byte_prefix_preserved=True,old_rows_unchanged=True,new_tail_exactly_bundle=True,
        all_event_ids_unique=True,independent_required_checks_completed=0,additional_independent_checks_completed=1,
        required_completion_manifest_byte_identical=True,immutable_197_index_unchanged=True,
        manifest=bound(str((O/'manifest.json').relative_to(R))),bundle=bound(c['event_bundle']))
    p=O/'append_verification.json';assert not p.exists();p.write_text(json.dumps(v,indent=2)+'\n')
    print(json.dumps(v,indent=2));sys.exit(0)
assert not O.exists() and not B.exists()
old=(R/'CHECK_EVENTS.tsv').read_bytes();assert sha(old)==c['before_ledger_sha256']
source=(R/'S6_SERIES_PUBLISH_II.tex').read_text();assert sha(source.encode())==c['source_sha256']
for x in [c[k] for k in ['prior_admission','proposal','event_proposal','root_review']]+c['source_applications']:
    assert bound(x['path'])==x
prior=read(c['prior_admission']['path'])
chainbindings=prior['source_application_chain']+c['source_applications']
chain=[read(x['path']) for x in chainbindings]
for a,z in zip(chain,chain[1:]):assert a['source_after_sha256']==z['source_before_sha256']
assert chain[-1]['source_after_sha256']==c['source_sha256']
source_history={x[k] for x in chain for k in ['source_before_sha256','source_after_sha256']}
ledger_history={sha(old)}
for p in (R/'records').glob('S6_SERIES_PUBLISH_II_*/before_ledger.tsv'):
    raw=p.read_bytes();assert old.startswith(raw);ledger_history.add(sha(raw))
historical=[]
def validate(x):
    if isinstance(x,dict):
        if 'path' in x and 'sha256' in x:
            actual=bound(x['path'])['sha256']
            if actual!=x['sha256']:
                assert ((x['path']=='S6_SERIES_PUBLISH_II.tex' and x['sha256'] in source_history)
                     or (x['path']=='CHECK_EVENTS.tsv' and x['sha256'] in ledger_history)),x
                historical.append(x)
        for v in x.values():validate(v)
    elif isinstance(x,list):
        for v in x:validate(v)
validate(chainbindings)
d,e=read(c['proposal']['path']),read(c['event_proposal']['path']);validate(d);validate(e)
targets={}
for t in d['targets']:
    assert t['additional_dependency_only'] and not t['required_197_row_completion_proposed']
    owner=t['statement_owner'];assert owner not in required
    f,r=read(t['freeze_receipt']['path']),read(t['release_receipt']['path']);validate(f);validate(r)
    assert f['additional_dependency_only'] and r['additional_dependency_only']
    assert f['statement_owner']==r['statement_owner']==owner
    assert datetime.datetime.fromisoformat(f['created_utc'])<datetime.datetime.fromisoformat(r['created_utc'])
    assert r['freeze_receipt']['sha256']==t['freeze_receipt']['sha256']
    assert r['frozen_derivation']==f['frozen_derivation']
    assert r['released_proof']['sha256']==f['target_proof']['sha256']
    assert r['released_full_block']['sha256']==f['full_owning_block']['sha256']
    assert t['original_full_block']['sha256']==f['full_owning_block']['sha256']
    assert f['required_197_index']['sha256']==index['sha256']
    assert not f['required_197_index_modified'] and not r['required_197_index_modified']
    assert t['actual_complete_original_proof_read'] and t['actual_complete_proposed_proof_read']
    assert source.count((R/t['proposed_full_block']['path']).read_text())==1
    targets[owner]=t
oldrows=rows(old);fields=next(csv.reader(io.StringIO(old.decode(),newline=''),delimiter='\t'))
now=datetime.datetime.now(datetime.timezone.utc).isoformat();events=[];checked=set()
for n,x in enumerate(e['events'],1):
    owner=x.get('statement_owner',x.get('statement_id'));typ=x.get('event_type',x.get('type'))
    assert owner in targets and typ in ['targeted proof check','used and rechecked in this run']
    assert x.get('event_count',1)==1
    if typ=='targeted proof check':assert owner not in checked;checked.add(owner)
    row={k:'' for k in fields};row.update(statement_id=owner,date='2026-11-21',who=c['who'],type=typ,
      outcome=x.get('scope',x.get('outcome'))+' '+c['event_scope_suffix'],
      event_id=f'S6_SERIES_PUBLISH_II_{c["batch_id"]}_{targets[owner]["tag"]}_{n:02d}_20261121',
      phase='S6_SERIES_PUBLISH_II',source_file=c['event_proposal']['path'],source_row=str(n+1),source_event_type=typ,
      evidence_group=f'S6_SERIES_PUBLISH_II_{c["batch_id"]}_{targets[owner]["tag"]}',
      publish_input_file=B.name,publish_input_row=str(n+1),date_utc=now,where=c['event_proposal']['path'])
    events.append(row)
assert len(checked)==c['additional_independent_checks'] and len(events)==c['events']
assert not {x['event_id'] for x in events}&{x['event_id'] for x in oldrows}
assert not any(x['event_id'].startswith('S6_SERIES_PUBLISH_II_') and '_01GA_' in x['event_id'] for x in oldrows)
mold=mp.read_bytes();assert not checked&set(json.loads(mold)['rows'])
O.mkdir();(O/'before_ledger.tsv').write_bytes(old);(O/'before_completion_manifest.json').write_bytes(mold)
with B.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(events)
m=dict(schema=1,created_utc=now,approved=True,paper='II',before_ledger_sha256=sha(old),
 event_bundle=bound(c['event_bundle']),events=len(events),independent_required_checks_completed=0,
 additional_independent_checks_completed=len(checked),completed_owners=[],additional_checked_owners=sorted(checked),
 source_sha256=c['source_sha256'],source_application_chain=chainbindings,
 evidence=[c['proposal'],c['event_proposal'],c['root_review'],bound(cfg)],
 historical_bindings_validated_via_exact_apply_chain_or_ledger_prefix=historical,
 proof_repairs=c.get('proof_repairs',[]),scope=c['scope'],visual_reading_credit=0,
 immutable_required_index=index,required_completion_manifest_sha256=sha(mold),required_completion_manifest_unchanged=True)
(O/'manifest.json').write_text(json.dumps(m,indent=2)+'\n')
assert mp.read_bytes()==mold and bound(index['path'])==index
print(json.dumps(dict(manifest=bound(str((O/'manifest.json').relative_to(R))),events=len(events),
 independent_checks=0,additional_independent_checks=len(checked)),indent=2))
