"""Admit recovered B02/C02 checks and actual post-reset editorial rereadings."""
from pathlib import Path
import csv,datetime,hashlib,io,json,sys
R=Path(__file__).resolve().parents[1];csv.field_size_limit(100_000_000)
O=R/'records/S6_SERIES_PUBLISH_II_recovery_checks_01'
BUNDLE=R/'records/S6_SERIES_PUBLISH_zzz_continuation_003_recovery_CHECK_EVENTS.tsv'
sha=lambda b:hashlib.sha256(b).hexdigest()
def bound(p):
 p=R/p if isinstance(p,str) else p
 return {'path':str(p.relative_to(R)),'sha256':sha(p.read_bytes())}
def read(p):return json.loads((R/p).read_text())
if '--verify' in sys.argv:
 m=json.loads((O/'manifest.json').read_text());old=(O/'before_ledger.tsv').read_bytes();new=(R/'CHECK_EVENTS.tsv').read_bytes()
 assert sha(old)==m['before_ledger_sha256'] and new.startswith(old)
 before=list(csv.DictReader(io.StringIO(old.decode(),newline=''),delimiter='\t'));after=list(csv.DictReader(io.StringIO(new.decode(),newline=''),delimiter='\t'));extra=list(csv.DictReader(BUNDLE.open(newline=''),delimiter='\t'))
 assert after[:len(before)]==before and after[len(before):]==extra
 assert len({r['event_id'] for r in after})==len(after)
 d={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'before_rows':len(before),'after_rows':len(after),'added_rows':len(extra),'before_ledger_sha256':sha(old),'after_ledger_sha256':sha(new),'whole_old_ledger_byte_prefix_preserved':True,'old_rows_unchanged':True,'new_tail_exactly_bundle':True,'all_event_ids_unique':True,'required_checks_completed':7,'manifest':bound(O/'manifest.json'),'bundle':bound(BUNDLE)}
 (O/'append_verification.json').write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(d,indent=2));sys.exit(0)
assert not O.exists() and not BUNDLE.exists()
now=datetime.datetime.now(datetime.timezone.utc).isoformat();old=(R/'CHECK_EVENTS.tsv').read_bytes()
assert sha(old)=='ab3847841c727fbd82721649174a05b48d2d7548d8c963d43b499f4b6a23a7ba'
reader=csv.DictReader(io.StringIO(old.decode(),newline=''),delimiter='\t');oldrows=list(reader);fields=reader.fieldnames
source=(R/'S6_SERIES_PUBLISH_II.tex').read_text()
chain_paths=['records/S6_SERIES_PUBLISH_II_root_recovery_edits_01/apply_receipt.json','records/S6_SERIES_PUBLISH_II_B_recovery_group02_editorial_apply.json','records/S6_SERIES_PUBLISH_II_C_recovery_group02_editorial_apply.json']
chain=[read(p) for p in chain_paths]
assert chain[0]['source_before_sha256']=='33e5e01d81b96aed7be0d5af71fc4425537f534af855b5f50d7b3a4b0835c573'
for a,b in zip(chain,chain[1:]):assert a['source_after_sha256']==b['source_before_sha256']
assert chain[-1]['source_after_sha256']==sha(source.encode())
history={x[k] for x in chain for k in ['source_before_sha256','source_after_sha256']}
historical_bindings=[]
def validate(obj):
 if isinstance(obj,dict):
  if 'path' in obj and 'sha256' in obj:
   p=R/obj['path'];actual=sha(p.read_bytes())
   if actual!=obj['sha256']:
    assert p==R/'S6_SERIES_PUBLISH_II.tex' and obj['sha256'] in history,obj
    historical_bindings.append(obj)
  for v in obj.values():validate(v)
 elif isinstance(obj,list):
  for v in obj:validate(v)
def freeze_release(fb,rb):
 validate(fb);validate(rb);f=read(fb['path']);r=read(rb['path'])
 assert r['freeze_receipt_sha256']==fb['sha256']
 assert datetime.datetime.fromisoformat(f['created_utc'])<datetime.datetime.fromisoformat(r['created_utc'])
 for key,hkey in [('frozen_derivation_path','derivation_sha256'),('target_proof_path','target_proof_sha256'),('packet_path','packet_sha256')]:assert sha((R/f[key]).read_bytes())==f[hkey]
 assert r['derivation_sha256']==f['derivation_sha256']
 return f['statement_owner']
events=[];completed={};evidence=[]
def add(owner,tag,typ,scope,checker,evidence_path,after,completion=False):
 validate(after);assert source.count((R/after['path']).read_text())==1,(owner,after)
 row={k:'' for k in fields};n=len(events)+1
 row.update(statement_id=owner,date='2026-11-21',who=f'GPT-6 Astra (OpenAI), ChatGPT Pro mode; reasoning effort inherited, no separate numerical setting exposed; {checker}',type=typ,outcome=scope,event_id=f'S6_SERIES_PUBLISH_II_RECOVERY01_{tag}_{n:02d}_20261121',phase='S6_SERIES_PUBLISH_II',source_file=evidence_path,source_row=str(n+1),source_event_type=typ,evidence_group=f'S6_SERIES_PUBLISH_II_RECOVERY01_{tag}',publish_input_file=BUNDLE.name,publish_input_row=str(n+1),date_utc=now,where=evidence_path)
 events.append(row)
 if completion:
  assert owner not in completed
  completed[owner]=scope
bp='agents/ii_checks_provenance/recovery_20261121T2000Z/group02/S6_SERIES_PUBLISH_II_B_group02_recovery_proposals.json'
be='agents/ii_checks_provenance/recovery_20261121T2000Z/group02/S6_SERIES_PUBLISH_II_B_group02_recovery_event_proposals_v2.json'
b=read(bp);ev=read(be);validate(b);validate(ev);evidence.extend([bp,be,b['restored_methods_addendum']['path']])
for t in b['targets']:
 assert freeze_release(t['freeze_receipt'],t['release_receipt'])==t['statement_owner']
 assert t['actual_original_complete_proof_read'] and t['actual_proposed_complete_proof_read']
for e in ev['events']:
 typ=e['event_type'];assert typ in ['targeted proof check','used and rechecked in this run']
 add(e['statement_owner'],e['tag'],typ,e['scope']+' Exact original prerelease records survived CP14. Final literal guards were reapplied after new actual paired reading. Postrelease supplements receive no extra independent event.', 'i_provenance',be,e['proposed_full_block'],typ=='targeted proof check')
cp='agents/ii_infra/recovery_20261121/S6_SERIES_PUBLISH_II_second_group_comparison.json'
ce='agents/ii_infra/recovery_20261121/S6_SERIES_PUBLISH_II_second_group_event_proposals.json'
c=read(cp);cev=read(ce);validate(c);validate(cev);evidence.extend([cp,ce])
for e in cev['events']:
 owner=freeze_release(e['freeze_receipt'],e['release_receipt']);assert owner==e['statement_id']
 scope=e['outcome'].replace('Proposed publication/scope guards await root approval and application.','The reviewed exact guards are now applied.')+' '+e['scope']+' The new computation derives Todd terms from individual Chern-root factors under c1=sum(x_i), c2=sum(x_i*x_j), c3=product(x_i); this explicitly transports the root calculation to the printed Chern classes. Historical final bytes were missing; only durable original freezes and newly dated comparisons support this admission.'
 add(owner,e['tag'],'targeted proof check',scope,'restore_build',ce,e['proposed_full_block'],True)
 add(owner,e['tag'],'used and rechecked in this run','The complete original and reconstructed proposed statement/proof blocks were actually reread after restoration. All formulas and references are preserved under the named exact scope/reference changes; source application is bound separately. No additional independent derivation is claimed.','restore_build',cp,e['proposed_full_block'])
f9=c['editorial_only_additional_owner'];assert f9['complete_original_and_proposed_block_actually_read']
add(f9['statement_id'],f9['tag'],'used and rechecked in this run','A new complete paired rereading covers the current C.3.3 proof and the removal of program narration. The explicit quaternion set, surjective single-commutator claim and exact quotient maps remain. Its required independent check was already admitted and receives no new completion.','restore_build',cp,f9['proposed_full_block'])
rp='records/S6_SERIES_PUBLISH_II_root_recovery_edits_01/actual_reread.json';r=read(rp);validate(r);evidence.append(rp)
for e in r['rows']:
 assert e['actual_original_and_revised_complete_blocks_read']
 add(e['statement_id'],e['tag'],e['type'],e['reading_scope']+' Complete original and revised blocks were actually reread after reset. Literal source inverse maps and program-table relocation are bound. No independent derivation or page-image credit.','root',rp,e['after'])
assert len(completed)==7 and len(events)==17
mp=R/'records/S6_SERIES_PUBLISH_required_check_completion_manifest.json';mold=mp.read_bytes();completion=json.loads(mold)
assert not set(completed)&set(completion['rows'])
O.mkdir();(O/'before_ledger.tsv').write_bytes(old);(O/'before_completion_manifest.json').write_bytes(mold)
with BUNDLE.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(events)
m={'schema':1,'created_utc':now,'approved':True,'paper':'II','before_ledger_sha256':sha(old),'event_bundle':bound(BUNDLE),'events':len(events),'completed_owners':list(completed),'source_sha256':sha(source.encode()),'source_application_chain':[bound(p) for p in chain_paths],'evidence':[bound(p) for p in evidence],'historical_source_bindings_validated_via_exact_apply_chain':historical_bindings,'recovery_scope':'Seven original frozen independent checks are revalidated; no lost post-checkpoint freeze is reconstructed. New paired readings are recorded with their actual category.','visual_reading_credit':0}
(O/'manifest.json').write_text(json.dumps(m,indent=2)+'\n')
for owner,scope in completed.items():completion['rows'][owner]={'paper':'II','status':'done','recorded_utc':now,'evidence_path':str((O/'manifest.json').relative_to(R)),'evidence_sha256':sha((O/'manifest.json').read_bytes()),'scope':scope}
completion['updated_utc']=now;mp.write_text(json.dumps(completion,indent=2)+'\n')
print(json.dumps({'manifest':bound(O/'manifest.json'),'events':len(events),'required_checks_completed':len(completed)},indent=2))
