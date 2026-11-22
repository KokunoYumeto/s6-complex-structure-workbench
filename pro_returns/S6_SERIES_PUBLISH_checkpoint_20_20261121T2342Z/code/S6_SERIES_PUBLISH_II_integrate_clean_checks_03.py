"""Admit six newly frozen and fully compared Paper II checks."""
from pathlib import Path
import csv,datetime,hashlib,io,json,sys
R=Path(__file__).resolve().parents[1];csv.field_size_limit(100_000_000)
O=R/'records/S6_SERIES_PUBLISH_II_clean_checks_03'
B=R/'records/S6_SERIES_PUBLISH_zzz_continuation_007_clean_CHECK_EVENTS.tsv'
sha=lambda b:hashlib.sha256(b).hexdigest()
def read(p):return json.loads((R/p).read_text())
def bound(p):
 p=R/p if isinstance(p,str) else p
 return dict(path=str(p.relative_to(R)),sha256=sha(p.read_bytes()))
if '--verify' in sys.argv:
 m=read(str((O/'manifest.json').relative_to(R)));a=(O/'before_ledger.tsv').read_bytes();b=(R/'CHECK_EVENTS.tsv').read_bytes()
 assert sha(a)==m['before_ledger_sha256'] and b.startswith(a)
 aa=list(csv.DictReader(io.StringIO(a.decode(),newline=''),delimiter='\t'));bb=list(csv.DictReader(io.StringIO(b.decode(),newline=''),delimiter='\t'));cc=list(csv.DictReader(B.open(newline=''),delimiter='\t'))
 assert bb[:len(aa)]==aa and bb[len(aa):]==cc and len({x['event_id'] for x in bb})==len(bb)
 result=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),before_rows=len(aa),after_rows=len(bb),added_rows=len(cc),before_ledger_sha256=sha(a),after_ledger_sha256=sha(b),whole_old_ledger_byte_prefix_preserved=True,old_rows_unchanged=True,new_tail_exactly_bundle=True,all_event_ids_unique=True,independent_required_checks_completed=6,manifest=bound(O/'manifest.json'),bundle=bound(B))
 p=O/'append_verification.json';assert not p.exists();p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));sys.exit(0)
assert not O.exists() and not B.exists()
old=(R/'CHECK_EVENTS.tsv').read_bytes();assert sha(old)=='fc2a3fc6882eeab6907fdd60b2eede4ddde4d46056c8872e8e3759b748b1806e'
reader=csv.DictReader(io.StringIO(old.decode(),newline=''),delimiter='\t');oldrows=list(reader);fields=reader.fieldnames
source=(R/'S6_SERIES_PUBLISH_II.tex').read_text();assert sha(source.encode())=='12e73204ef053b62a7e47599edb4d22d90641683bbac49105f07a37c2e5f20c5'
prior=read('records/S6_SERIES_PUBLISH_II_clean_checks_02/manifest.json')
paths=[x['path'] for x in prior['source_application_chain']]+['records/S6_SERIES_PUBLISH_II_B_clean_02_editorial_apply.json']
chain=[read(p) for p in paths]
for a,b in zip(chain,chain[1:]):assert a['source_after_sha256']==b['source_before_sha256']
assert chain[-1]['source_after_sha256']==sha(source.encode())
history={x[k] for x in chain for k in ['source_before_sha256','source_after_sha256']}
ledger_history={sha(old),sha((R/'records/S6_SERIES_PUBLISH_II_clean_checks_02/before_ledger.tsv').read_bytes())}
historical=[]
def validate(x):
 if isinstance(x,dict):
  if 'path' in x and 'sha256' in x:
   p=R/x['path'];actual=sha(p.read_bytes())
   if actual!=x['sha256']:
    assert (p==R/'S6_SERIES_PUBLISH_II.tex' and x['sha256'] in history) or (p==R/'CHECK_EVENTS.tsv' and x['sha256'] in ledger_history),x
    historical.append(x)
  for v in x.values():validate(v)
 elif isinstance(x,list):
  for v in x:validate(v)
for b in prior['source_application_chain']:validate(b)
base='agents/ii_checks_provenance/recovery_20261121T2000Z/clean_group02/'
pp=base+'S6_SERIES_PUBLISH_II_clean_group02_final_proposals.json';ep=base+'S6_SERIES_PUBLISH_II_clean_group02_event_proposals.json'
assert bound(pp)['sha256']=='016785e949ae4cd67469a3c985591b3d9d28cd9f4fefc682a8fe7c9fbf32eb96'
assert bound(ep)['sha256']=='abb56779615c9733bb7d2e480751cf5423e3ed91d8449f10e0f4480e8242471d'
d=read(pp);ev=read(ep);validate(d);validate(ev);targets={}
for t in d['targets']:
 f=read(t['freeze_receipt']['path']);r=read(t['release_receipt']['path']);validate(f);validate(r)
 assert r['freeze_receipt_sha256']==t['freeze_receipt']['sha256']
 assert datetime.datetime.fromisoformat(f['created_utc'])<datetime.datetime.fromisoformat(r['created_utc'])
 assert r['statement_owner']==f['statement_owner']==t['statement_owner']
 assert r['derivation_sha256']==f['derivation_sha256']
 for k,h in [('frozen_derivation_path','derivation_sha256'),('packet_path','packet_sha256'),('target_proof_path','target_proof_sha256')]:assert sha((R/f[k]).read_bytes())==f[h]
 for k,h in [('released_proof_path','released_proof_sha256'),('full_owning_block_path','full_owning_block_sha256')]:assert sha((R/r[k]).read_bytes())==r[h]
 assert r['released_proof_sha256']==f['target_proof_sha256']
 assert t['actual_complete_original_proof_read'] and t['actual_complete_proposed_proof_read']
 assert source.count((R/t['proposed_full_block']['path']).read_text())==1
 targets[t['statement_owner']]=t
events=[];completed={};now=datetime.datetime.now(datetime.timezone.utc).isoformat()
for e in ev['events']:
 owner=e.get('statement_owner',e.get('statement_id'));typ=e.get('event_type',e.get('type'));typ={'used and rechecked':'used and rechecked in this run'}.get(typ,typ)
 assert owner in targets and typ in ['targeted proof check','used and rechecked in this run']
 scope=e.get('scope',e.get('outcome'))
 row={k:'' for k in fields};n=len(events)+1
 row.update(statement_id=owner,date='2026-11-21',who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; reasoning effort inherited, no separate numerical setting exposed; i_provenance_recovery',type=typ,outcome=scope+' Exact source guards are now applied; complete source pairs, freeze/release chronology, primary receipts and every computation are bound. Ancillary postrelease E12/E17 calculations receive no extra independent-check event.',event_id=f'S6_SERIES_PUBLISH_II_CLEAN03_{targets[owner]["tag"]}_{n:02d}_20261121',phase='S6_SERIES_PUBLISH_II',source_file=ep,source_row=str(n+1),source_event_type=typ,evidence_group=f'S6_SERIES_PUBLISH_II_CLEAN03_{targets[owner]["tag"]}',publish_input_file=B.name,publish_input_row=str(n+1),date_utc=now,where=ep)
 events.append(row)
 if typ=='targeted proof check':assert owner not in completed;completed[owner]=scope
assert len(completed)==6 and len(events)==12
mp=R/'records/S6_SERIES_PUBLISH_required_check_completion_manifest.json';mold=mp.read_bytes();completion=json.loads(mold)
assert not set(completed)&set(completion['rows']);assert not {e['event_id'] for e in events}&{e['event_id'] for e in oldrows}
O.mkdir();(O/'before_ledger.tsv').write_bytes(old);(O/'before_completion_manifest.json').write_bytes(mold)
with B.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(events)
m=dict(schema=1,created_utc=now,approved=True,paper='II',before_ledger_sha256=sha(old),event_bundle=bound(B),events=len(events),independent_required_checks_completed=6,completed_owners=list(completed),source_sha256=sha(source.encode()),source_application_chain=[bound(p) for p in paths],evidence=[bound(pp),bound(ep)],historical_bindings_validated_via_exact_apply_chain_or_ledger_prefix=historical,proof_repairs=['WK specifies the Nth power as the unipotent operator.','WK transports the cohomology action through the evaluation pairing to A^T and uses determinant-transpose equality.'],scope='Six fresh preproof derivations with complete printed-proof comparisons and six actual complete editorial rereadings. Original statements retain their conclusions. All postrelease supplements retain their actual timing.',visual_reading_credit=0)
(O/'manifest.json').write_text(json.dumps(m,indent=2)+'\n')
for owner,scope in completed.items():completion['rows'][owner]=dict(paper='II',status='done',recorded_utc=now,evidence_path=str((O/'manifest.json').relative_to(R)),evidence_sha256=sha((O/'manifest.json').read_bytes()),scope=scope,completion_kind='independent proof check')
completion['updated_utc']=now;mp.write_text(json.dumps(completion,indent=2)+'\n')
print(json.dumps(dict(manifest=bound(O/'manifest.json'),events=len(events),independent_checks=6),indent=2))
