"""Admit the two genuine manual-block checks and their actual paired rereadings."""
from pathlib import Path
import csv,datetime,hashlib,io,json,sys
R=Path(__file__).resolve().parents[1];csv.field_size_limit(100_000_000)
O=R/'records/S6_SERIES_PUBLISH_II_G3_G4_checks_01';B=R/'records/S6_SERIES_PUBLISH_zzz_continuation_008_manual_CHECK_EVENTS.tsv'
sha=lambda b:hashlib.sha256(b).hexdigest()
def read(p):return json.loads((R/p).read_text())
def bound(p):
 p=R/p if isinstance(p,str) else p
 return dict(path=str(p.relative_to(R)),sha256=sha(p.read_bytes()))
if '--verify' in sys.argv:
 m=read(str((O/'manifest.json').relative_to(R)));old=(O/'before_ledger.tsv').read_bytes();new=(R/'CHECK_EVENTS.tsv').read_bytes();assert sha(old)==m['before_ledger_sha256'] and new.startswith(old)
 a=list(csv.DictReader(io.StringIO(old.decode(),newline=''),delimiter='\t'));b=list(csv.DictReader(io.StringIO(new.decode(),newline=''),delimiter='\t'));c=list(csv.DictReader(B.open(newline=''),delimiter='\t'))
 assert b[:len(a)]==a and b[len(a):]==c and len({x['event_id'] for x in b})==len(b)
 result=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),before_rows=len(a),after_rows=len(b),added_rows=len(c),before_ledger_sha256=sha(old),after_ledger_sha256=sha(new),whole_old_ledger_byte_prefix_preserved=True,old_rows_unchanged=True,new_tail_exactly_bundle=True,all_event_ids_unique=True,independent_required_checks_completed=2,manifest=bound(O/'manifest.json'),bundle=bound(B))
 p=O/'append_verification.json';assert not p.exists();p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));sys.exit(0)
assert not O.exists() and not B.exists();old=(R/'CHECK_EVENTS.tsv').read_bytes()
assert sha(old)=='1ab487f36ca58d09761fe9d7ad22d60fdcf7cad7cee0cd423f50c1faeb28d66a'
reader=csv.DictReader(io.StringIO(old.decode(),newline=''),delimiter='\t');oldrows=list(reader);fields=reader.fieldnames
source=(R/'S6_SERIES_PUBLISH_II.tex').read_text();assert sha(source.encode())=='459c8c7c3dff70ff2621e567383ac56eaf92fd271b02f83775d2cb994f332d6e'
prior=read('records/S6_SERIES_PUBLISH_II_clean_checks_03/manifest.json')
paths=[x['path'] for x in prior['source_application_chain']]+['records/S6_SERIES_PUBLISH_II_G3_G4_editorial_apply_01.json'];chain=[read(p) for p in paths]
for a,b in zip(chain,chain[1:]):assert a['source_after_sha256']==b['source_before_sha256']
assert chain[-1]['source_after_sha256']==sha(source.encode());history={x[k] for x in chain for k in ['source_before_sha256','source_after_sha256']};historical=[]
def validate(x):
 if isinstance(x,dict):
  if 'path' in x and 'sha256' in x:
   p=R/x['path']
   if sha(p.read_bytes())!=x['sha256']:
    assert p==R/'S6_SERIES_PUBLISH_II.tex' and x['sha256'] in history,x;historical.append(x)
  for v in x.values():validate(v)
 elif isinstance(x,list):
  for v in x:validate(v)
for p in prior['source_application_chain']:validate(p)
cp='agents/ii_infra/recovery_20261121/S6_SERIES_PUBLISH_II_G3_G4_comparison.json';ep='agents/ii_infra/recovery_20261121/S6_SERIES_PUBLISH_II_G3_G4_event_proposals.json'
assert bound(cp)['sha256']=='0ea2ac88ddda3844cf5edb28db0eeee099da7a29b2a624499356662a5416c836';assert bound(ep)['sha256']=='e3737117e647b65c651e0fda6431de55322fe3e61065eefa5042a086bdfa200d'
d=read(cp);e=read(ep);validate(d);validate(e);checks={}
for t in d['checks']:
 f=read(t['freeze_receipt']['path']);r=read(t['release_receipt']['path']);validate(f);validate(r)
 assert r['freeze_receipt_sha256']==t['freeze_receipt']['sha256'] and f['statement_owner']==r['statement_owner']==t['statement_id']
 assert datetime.datetime.fromisoformat(f['created_utc'])<datetime.datetime.fromisoformat(r['created_utc'])
 assert r['derivation_sha256']==f['derivation_sha256']
 for k,h in [('frozen_derivation_path','derivation_sha256'),('packet_path','packet_sha256'),('target_proof_path','target_proof_sha256')]:assert sha((R/f[k]).read_bytes())==f[h]
 for k,h in [('released_proof_path','released_proof_sha256'),('full_owning_block_path','full_owning_block_sha256')]:assert sha((R/r[k]).read_bytes())==r[h]
 assert r['released_proof_sha256']==f['target_proof_sha256']
 original=(R/t['original_full_block']['path']).read_text();released=(R/r['full_owning_block_path']).read_text()
 assert released.rstrip('\n')==original
 assert t['complete_original_actually_read'] and t['complete_proposed_actually_read'] and not t['unresolved_mathematical_findings']
 assert source.count((R/t['proposed_full_block']['path']).read_text())==1
 checks[t['statement_id']]=t
events=[];completed={};now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def add(owner,tag,typ,scope):
 n=len(events)+1;row={k:'' for k in fields};row.update(statement_id=owner,date='2026-11-21',who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; reasoning effort inherited, no separate numerical setting exposed; restore_build',type=typ,outcome=scope,event_id=f'S6_SERIES_PUBLISH_II_MANUAL01_{tag}_{n:02d}_20261121',phase='S6_SERIES_PUBLISH_II',source_file=cp,source_row=str(n+1),source_event_type=typ,evidence_group=f'S6_SERIES_PUBLISH_II_MANUAL01_{tag}',publish_input_file=B.name,publish_input_row=str(n+1),date_utc=now,where=cp);events.append(row)
for x in e['events']:
 owner=x['statement_id'];assert owner in checks
 scope=x['outcome'].replace('Root review/application and final block binding pending.','Root review/application and exact final block binding are complete.')
 scope+=' The entire embedded original argument was released and read; an empty attached-proof list was never treated as a proof check. Fresh standard-library polynomial Bezout and integral lattice witnesses were compared with every computational step. Wang v2 source identity, printed statement/page locators and supplementary postrelease matrix cube are recorded.'
 add(owner,x['tag'],'targeted proof check',scope);completed[owner]=scope
 add(owner,x['tag'],'used and rechecked in this run','Actually reread the complete original mixed statement/argument and complete final proposition/proof pair, with every original mathematical expression retained and every new map or witness compared. The checker also read the full program-table/bibliography pairs; root read both full mathematical pairs and all literal guards. This editorial event carries no additional independent derivation credit.')
assert len(events)==4 and len(completed)==2
mp=R/'records/S6_SERIES_PUBLISH_required_check_completion_manifest.json';mold=mp.read_bytes();completion=json.loads(mold);assert not set(completed)&set(completion['rows']);assert not {x['event_id'] for x in events}&{x['event_id'] for x in oldrows}
O.mkdir();(O/'before_ledger.tsv').write_bytes(old);(O/'before_completion_manifest.json').write_bytes(mold)
with B.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(events)
m=dict(schema=1,created_utc=now,approved=True,paper='II',before_ledger_sha256=sha(old),event_bundle=bound(B),events=len(events),independent_required_checks_completed=2,completed_owners=list(completed),source_sha256=sha(source.encode()),source_application_chain=[bound(p) for p in paths],evidence=[bound(cp),bound(ep)],historical_source_bindings_validated_via_exact_apply_chain=historical,scope='Two genuine statement-first derivations before release of complete embedded arguments, two complete printed-argument comparisons, and two actual complete editorial rereadings. No historical lost check is reconstructed.',visual_reading_credit=0)
(O/'manifest.json').write_text(json.dumps(m,indent=2)+'\n')
for owner,scope in completed.items():completion['rows'][owner]=dict(paper='II',status='done',recorded_utc=now,evidence_path=str((O/'manifest.json').relative_to(R)),evidence_sha256=sha((O/'manifest.json').read_bytes()),scope=scope,completion_kind='independent proof check')
completion['updated_utc']=now;mp.write_text(json.dumps(completion,indent=2)+'\n');print(json.dumps(dict(manifest=bound(O/'manifest.json'),events=4,independent_checks=2),indent=2))
