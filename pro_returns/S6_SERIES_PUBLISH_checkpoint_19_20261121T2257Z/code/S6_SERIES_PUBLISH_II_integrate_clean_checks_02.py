"""Admit four fresh proof checks and resolve one retired production-only remark."""
from pathlib import Path
import csv,datetime,hashlib,io,json,re,sys
R=Path(__file__).resolve().parents[1]
csv.field_size_limit(100_000_000)
O=R/'records/S6_SERIES_PUBLISH_II_clean_checks_02'
BUNDLE=R/'records/S6_SERIES_PUBLISH_zzz_continuation_006_clean_CHECK_EVENTS.tsv'
sha=lambda b:hashlib.sha256(b).hexdigest()
def read(p):return json.loads((R/p).read_text())
def bound(p):
 p=R/p if isinstance(p,str) else p
 return dict(path=str(p.relative_to(R)),sha256=sha(p.read_bytes()))
def check(item):
 assert sha((R/item['path']).read_bytes())==item['sha256'],item

if '--verify' in sys.argv:
 m=read(str((O/'manifest.json').relative_to(R)))
 old=(O/'before_ledger.tsv').read_bytes();new=(R/'CHECK_EVENTS.tsv').read_bytes()
 assert sha(old)==m['before_ledger_sha256'] and new.startswith(old)
 a=list(csv.DictReader(io.StringIO(old.decode(),newline=''),delimiter='\t'))
 b=list(csv.DictReader(io.StringIO(new.decode(),newline=''),delimiter='\t'))
 c=list(csv.DictReader(BUNDLE.open(newline=''),delimiter='\t'))
 assert b[:len(a)]==a and b[len(a):]==c and len({x['event_id'] for x in b})==len(b)
 result=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),before_rows=len(a),after_rows=len(b),added_rows=len(c),
   before_ledger_sha256=sha(old),after_ledger_sha256=sha(new),whole_old_ledger_byte_prefix_preserved=True,
   old_rows_unchanged=True,new_tail_exactly_bundle=True,all_event_ids_unique=True,
   independent_required_checks_completed=4,production_only_required_rows_retired=1,manifest=bound(O/'manifest.json'),bundle=bound(BUNDLE))
 p=O/'append_verification.json';assert not p.exists();p.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2));sys.exit(0)

assert not O.exists() and not BUNDLE.exists()
old=(R/'CHECK_EVENTS.tsv').read_bytes()
assert sha(old)=='8dd4d8a3323558c6500ea3346726685969433b57543b7b218d322b0952da0e1a'
reader=csv.DictReader(io.StringIO(old.decode(),newline=''),delimiter='\t');oldrows=list(reader);fields=reader.fieldnames
source=(R/'S6_SERIES_PUBLISH_II.tex').read_text()
assert sha(source.encode())=='39f88bb8e8588fd496dedc2e99536ac0b062713d3de627c785485628d440cf80'
prior=read('records/S6_SERIES_PUBLISH_II_clean_checks_01/manifest.json')
chain_paths=[x['path'] for x in prior['source_application_chain']]+[
 'records/S6_SERIES_PUBLISH_II_TQ_alias_01/apply_receipt.json',
 'records/S6_SERIES_PUBLISH_II_A_clean_01_editorial_apply.json']
chain=[read(p) for p in chain_paths]
for a,b in zip(chain,chain[1:]):assert a['source_after_sha256']==b['source_before_sha256']
assert chain[-1]['source_after_sha256']==sha(source.encode())
for item in prior['source_application_chain']:check(item)

base='agents/ii_checks_A/recovery_20261121T195642Z/'
ip=base+'S6_SERIES_PUBLISH_II_A_recovery_clean_group01_final_index.json'
assert bound(ip)['sha256']=='6b05cf460cac28cc6429003a649159244e09bf12baed6534112eb460da46a5da'
idx=read(ip)
for f in idx['files']:check(f)
freezes=read(base+'S6_SERIES_PUBLISH_II_A_recovery_clean_group01_freezes.json')
releases=read(base+'S6_SERIES_PUBLISH_II_A_recovery_clean_group01_releases.json')
proofs={};frozen_program_bindings=[]
for fb,rb in zip(freezes,releases):
 assert bound(fb['receipt'])['sha256']==fb['sha256'] and bound(rb['receipt'])['sha256']==rb['sha256']
 f=read(fb['receipt']);r=read(rb['receipt'])
 assert r['freeze_receipt_sha256']==fb['sha256'] and r['derivation_sha256']==f['derivation_sha256']
 assert datetime.datetime.fromisoformat(f['created_utc'])<datetime.datetime.fromisoformat(r['created_utc'])
 assert f['statement_owner']==r['statement_owner']==fb['owner']
 for path,hashkey in [('frozen_derivation_path','derivation_sha256'),('packet_path','packet_sha256'),('target_proof_path','target_proof_sha256')]:
  assert sha((R/f[path]).read_bytes())==f[hashkey]
 for path,hashkey in [('released_proof_path','released_proof_sha256'),('full_owning_block_path','full_owning_block_sha256')]:
  assert sha((R/r[path]).read_bytes())==r[hashkey]
 assert r['released_proof_sha256']==f['target_proof_sha256']
 if f.get('cited_input_supplement'):check(f['cited_input_supplement'])
 for path,h in re.findall(r'^- ([^\n]+?) — SHA256 ([0-9a-f]{64})\.',(R/f['frozen_derivation_path']).read_text(),re.M):
  item=dict(path=path,sha256=h);check(item);frozen_program_bindings.append(item)
 proofs[f['tag']]=dict(owner=f['statement_owner'],freeze=bound(fb['receipt']),release=bound(rb['receipt']))

p=read(idx['files'][0]['path']);blocks={}
rr=read(base+'clean_group01/S6_SERIES_PUBLISH_II_A_recovery_clean_group01_rereads.json')
rrs={x['tag']:x for x in rr['records']}
for b in p['blocks']:
 assert rrs[b['tag']]['complete_original_and_proposed_read']
 for pathkey,hashkey in [('original_path','original_sha256'),('proposed_path','proposed_sha256')]:assert sha((R/b[pathkey]).read_bytes())==b[hashkey]
 assert source.count((R/b['proposed_path']).read_text())==1
 assert rrs[b['tag']]['original_sha256']==b['original_sha256'] and rrs[b['tag']]['proposed_sha256']==b['proposed_sha256']
 blocks[proofs[b['tag']]['owner']]=b
for run in read(base+'S6_SERIES_PUBLISH_II_A_recovery_clean_group01_program_runs.json'):
 assert run['exit_code']==0
 for a,b in [('source_path','source_sha256'),('output_path','output_sha256')]:assert sha((R/run[a]).read_bytes())==run[b]

ep=base+'clean_group01/S6_SERIES_PUBLISH_II_A_recovery_clean_group01_event_proposals.json'
events=[];completed={};now=datetime.datetime.now(datetime.timezone.utc).isoformat()
for e in read(ep)['events']:
 assert e['type'] in ['targeted proof check','used and rechecked in this run','computation or formal certificate']
 assert e['statement_id'] in blocks
 row={k:'' for k in fields};row.update({k:v for k,v in e.items() if k in fields})
 row.update(publish_input_file=BUNDLE.name,publish_input_row=str(len(events)+2),source_event_type=e['type'])
 events.append(row)
 if e['type']=='targeted proof check':
  assert e['statement_id'] not in completed;completed[e['statement_id']]=dict(kind='independent proof check',scope=e['outcome'])
assert len(completed)==4 and len(events)==10

tq='records/S6_SERIES_PUBLISH_II_TQ_alias_01/'
g=read(tq+'reviewed_guard.json');check(g['paired_rereading']);review=read(g['paired_rereading']['path'])
assert review['actual_complete_original_and_proposed_read']
assert source.count((R/g['proposed_full_block']['path']).read_text())==1
assert r'\begin{remark}[provenance of the repair]' not in source
for kind in ['labels','targets']:
 ident=chain[-2]['identities'][kind]
 assert not ident['original_sequence_preserved'] and ident['unchanged_relative_order_of_every_other_identity']
 assert ident['complete_occurrence_bijection']==g['identity_permutations'][kind]
row={k:'' for k in fields};row.update(statement_id='wb:thm:uniform-nontorsion-audit',date='2026-11-21',
 who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; reasoning effort inherited, no separate numerical setting exposed; root continuation',
 type='used and rechecked in this run',outcome=review['scope']+' The coordinate isomorphism and inverse, current full-fibre restriction map, and derivative-character normal quotient were read against all seven original proof items. All other identifier order is preserved by the complete occurrence bijection.',
 event_id='S6_SERIES_PUBLISH_II_TQ_OWNER_WORDING_20261121',phase='S6_SERIES_PUBLISH_II',source_file=g['paired_rereading']['path'],
 source_row='1',source_event_type='used and rechecked in this run',evidence_group='S6_SERIES_PUBLISH_II_TQ_OWNER',
 publish_input_file=BUNDLE.name,publish_input_row=str(len(events)+2),date_utc=now,where=g['paired_rereading']['path'])
events.append(row)
completed['inv:wb:uniform-nontorsion-provenance']=dict(kind='retired nonmathematical production remark',scope='Retired the production-history remark after archiving its whole text and mapping its four mathematical references to their exact current owners. Its original label and tag are preserved as aliases of the uniform non-torsion theorem, through a complete occurrence-index bijection. No independent proof check or computation is credited to the retired remark; the owning proof receives one actual paired-rereading event.')
mp=R/'records/S6_SERIES_PUBLISH_required_check_completion_manifest.json';mold=mp.read_bytes();completion=json.loads(mold)
assert not set(completed)&set(completion['rows'])
assert not {e['event_id'] for e in events}&{e['event_id'] for e in oldrows}
O.mkdir();(O/'before_ledger.tsv').write_bytes(old);(O/'before_completion_manifest.json').write_bytes(mold)
with BUNDLE.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(events)
manifest=dict(schema=1,created_utc=now,approved=True,paper='II',before_ledger_sha256=sha(old),event_bundle=bound(BUNDLE),
 events=len(events),independent_required_checks_completed=4,production_only_required_rows_retired=1,completed_owners=list(completed),
 completion_kinds={k:v['kind'] for k,v in completed.items()},source_sha256=sha(source.encode()),
 source_application_chain=[bound(p) for p in chain_paths],evidence_index=bound(ip),freeze_release_bindings=proofs,
 frozen_program_bindings=frozen_program_bindings,production_remark_claim_map=g['claim_owner_map'],
 paired_rereading=bound(tq+'paired_rereading.json'),alias_apply=bound(tq+'apply_receipt.json'),
 scope='Four fresh frozen derivations and full comparisons, four actual editorial rereadings, two computations, and one owning-proof rereading. One nonmathematical required-candidate disposition is resolved by retirement and exact alias/claim maps. These five row resolutions are not described as five independent checks.',visual_reading_credit=0)
(O/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
for owner,c in completed.items():
 completion['rows'][owner]=dict(paper='II',status='done',recorded_utc=now,evidence_path=str((O/'manifest.json').relative_to(R)),evidence_sha256=sha((O/'manifest.json').read_bytes()),scope=c['scope'],completion_kind=c['kind'])
completion['updated_utc']=now;mp.write_text(json.dumps(completion,indent=2)+'\n')
print(json.dumps(dict(manifest=bound(O/'manifest.json'),events=len(events),independent_checks=4,retired_production_rows=1),indent=2))
