"""Bind and admit reviewed II checks; preserve every pre-existing event byte.

This script writes an approved event bundle and completion rows. The separate
record refresh merges that bundle, then --verify checks the exact old prefix.
"""
from pathlib import Path
import csv,datetime,hashlib,io,json,sys
R=Path(__file__).resolve().parents[1]
csv.field_size_limit(100_000_000)
sha=lambda b:hashlib.sha256(b.encode() if isinstance(b,str) else b).hexdigest()
out=R/'records/S6_SERIES_PUBLISH_II_checks_01'
bundle=R/'records/S6_SERIES_PUBLISH_zzz_continuation_001_CHECK_EVENTS.tsv'
def bound(p):
 p=Path(p);p=p if p.is_absolute() else R/p
 return dict(path=str(p.relative_to(R)),sha256=sha(p.read_bytes()))
if '--verify' in sys.argv:
 m=json.loads((out/'manifest.json').read_text());old=(out/'before_ledger.tsv').read_bytes();new=(R/'CHECK_EVENTS.tsv').read_bytes()
 assert sha(old)==m['before_ledger_sha256'] and new.startswith(old)
 oldrows=list(csv.DictReader(io.StringIO(old.decode(),newline=''),delimiter='\t'))
 newrows=list(csv.DictReader(io.StringIO(new.decode(),newline=''),delimiter='\t'))
 additions=list(csv.DictReader(bundle.open(),delimiter='\t'))
 assert newrows[:len(oldrows)]==oldrows and newrows[len(oldrows):]==additions
 assert len({x['event_id'] for x in newrows})==len(newrows)
 receipt=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),manifest=bound(out/'manifest.json'),event_bundle=bound(bundle),before_rows=len(oldrows),after_rows=len(newrows),added_rows=len(additions),before_ledger_sha256=sha(old),after_ledger_sha256=sha(new),old_ledger_bytes_and_rows_preserved=True,required_checks_completed=len(m['completed_owners']))
 (out/'append_verification.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2));sys.exit(0)
assert not out.exists() and not bundle.exists();out.mkdir()
old=(R/'CHECK_EVENTS.tsv').read_bytes();assert sha(old)=='0f95daacb5cc1ddbd927d380e982b61bc28fad77edbbfbff4c8823eab22dfd78'
(out/'before_ledger.tsv').write_bytes(old)
reader=csv.DictReader(io.StringIO(old.decode(),newline=''),delimiter='\t');oldrows=list(reader);fields=reader.fieldnames
assert len(oldrows)==7944
source=(R/'S6_SERIES_PUBLISH_II.tex').read_text();now=datetime.datetime.now(datetime.timezone.utc).isoformat()
who=lambda actor:'GPT-6 Astra (OpenAI), ChatGPT Pro mode; reasoning effort inherited, no separate numerical setting exposed; S6_SERIES_PUBLISH '+actor
events=[];completed={};evidence=[]
def add(owner,typ,outcome,eid,actor,path,group):
 e={k:'' for k in fields};e.update(statement_id=owner,date='2026-11-21',who=who(actor),type=typ,outcome=outcome,event_id=eid,phase='S6_SERIES_PUBLISH_II',source_file=path,source_row=str(len(events)+2),source_event_type=typ,evidence_group=group,date_utc=now,where=path,publish_input_file=bundle.name,publish_input_row=str(len(events)+2))
 events.append(e)
ap='agents/ii_checks_A/S6_SERIES_PUBLISH_II_A_group01_event_proposals.json';a=json.loads((R/ap).read_text())
ag=json.loads((R/'records/S6_SERIES_PUBLISH_II_A_group01_editorial_guard.json').read_text())
for b in ag['bindings']:
 for side in ['before','after']:
  assert sha((R/b[side]['path']).read_bytes())==b[side]['sha256']
 assert source.count((R/b['after']['path']).read_text())==1
for e in a['events']:
 for p,h in e.get('artifact_hashes',{}).items():assert sha((R/p).read_bytes())==h,(p,h)
 outcome=e['outcome']
 if e['statement_id']=='cdp:st:D.1.15':
  outcome+=' The postrelease Gaussian-integer interpolation and fraction-free Bareiss supplement supplies the different computational method; it adds no prereading claim.'
 if e['statement_id']=='cdp:st:D.1.12':
  outcome+=' The exact method map from the independently multiplied Bernoulli factors is c1=sum(x_i), c2=sum(i<j,x_i*x_j); the older routine took the Todd coefficient as input.'
 add(e['statement_id'],e['type'],outcome,e['event_id'],'checker ii_check_a',ap,e['evidence_group'])
 if e['type']=='targeted proof check':completed[e['statement_id']]='Complete prereading derivation and whole printed-proof comparison; exact current full block and applied edits bound. Computational supplements have explicit postrelease timing.'
bp='agents/ii_checks_provenance/group01/S6_SERIES_PUBLISH_II_B_group01_event_proposals.json';b=json.loads((R/bp).read_text())
assert sha((R/bp).read_bytes())=='cc747902cb2c1e10df83b19734aac346874202a7c23434675f61455486800d37'
summaries={
 '01BN':'Derived the exponential-sequence Picard-component isomorphism and smooth threefold HRR index before proof release; sparse graded Fraction convolution rechecks the index by a different method. Explicit smooth scope and all coded receiving uses are bound.',
 '01BP':'Derived componentwise generic endpoint vanishing, Serre-dual inversion, the Euler lower bound and proper semicontinuity before proof release. Current proof expands the same scope and supplies the exact CDP98 Corollary1.3 transport and exponential family.',
 '01GG':'Derived verticality of every effective divisor by positive fibre intersection and the meromorphic-field pullback by clearing base poles; every printed step compared.',
 '01AG':'Derived Jacobian containment in the conductor by Weierstrass trace duality, the inverse-Jacobian kernel, and the conductor square through the stated exact analytic-ring maps; complete printed proof compared.',
 '01AJ':'Derived the normalization, parity description of the inverse Jacobian and vertical residue before proof release. Universal parity inequalities and degree-bounded integer interpolation check all computational identities by methods distinct from the prior finite exponent scan and symbolic differentiation.',
 '01AK':'Derived the cusp example before proof release and compared the complete printed proof. Postrelease different-method supplements check the faithful finite-free algebra, conductor lattice, truncated jets, interpolated gradients, conormal exterior products and direct ideal-square reduction; all values agree. Their postrelease timing is explicit.'}
for e in b['events']:
 for v in e.values():
  if isinstance(v,dict) and set(['path','sha256'])<=set(v):assert sha((R/v['path']).read_bytes())==v['sha256'],v['path']
 block=(R/e['reviewed_final_full_block']['path']).read_text();assert source.count(block)==1
 owner=e['statement_id'];group='II-B-group01-'+e['tag']
 add(owner,'targeted proof check',summaries[e['tag']]+' Related Paper I inputs were previously read; no additional blind derivation of those inputs is claimed.',e['proposed_event_id'],'checker i_provenance',bp,group)
 add(owner,'used and rechecked in this run','The checker actually read the complete original and revised statement/proof pair; exact literal edits, source/proof hashes, scope repairs and primary-source transports are recorded. This event records the separate editorial rereading and adds no independent derivation credit.',e['proposed_event_id']+'_editorial_reread','checker i_provenance',bp,group)
 completed[owner]=summaries[e['tag']]+' Complete original/revised proof reading and final applied block are bound.'
rp='records/S6_SERIES_PUBLISH_II_root_proof_edits_01/actual_reread.json';rr=json.loads((R/rp).read_text())
for e in rr['rows']:
 assert e['complete_original_and_proposed_blocks_read']
 scope=e['scope']
 if e['owner'].endswith('UN.2'):scope+=' The subsequently located historical program is now verified at the pinned commit and appears in the single end table.'
 add(e['owner'],e['type'],scope,'S6_SERIES_PUBLISH_II_root_'+e['owner'].split(':')[-1]+'_reread_20261121','root',rp,'II-root-UN-editorial')
assert len(events)==35 and len(completed)==15
assert len({x['event_id'] for x in events})==len(events)
assert not {x['event_id'] for x in events}&{x['event_id'] for x in oldrows}
with bundle.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(events)
evidence_paths=[ap,bp,rp,'records/S6_SERIES_PUBLISH_II_A_group01_editorial_guard.json','records/S6_SERIES_PUBLISH_II_A_group01_editorial_apply.json','records/S6_SERIES_PUBLISH_II_B_group01_editorial_apply.json','records/S6_SERIES_PUBLISH_II_Bv2_C1_editorial_apply.json','records/S6_SERIES_PUBLISH_II_reference_transports_01/apply.json','agents/ii_checks_A/S6_SERIES_PUBLISH_II_A_group01_E4_actual_rereads.json','agents/ii_checks_A/S6_SERIES_PUBLISH_II_A_group01_actual_rereading_records.json','agents/ii_checks_A/S6_SERIES_PUBLISH_II_A_group01_computation_method_addendum.md','code/S6_SERIES_PUBLISH_II_A_01FZ_integer_certificate.py','code/S6_SERIES_PUBLISH_II_A_01FZ_integer_certificate.out','agents/ii_checks_provenance/group01/v2_addendum/S6_SERIES_PUBLISH_II_B_group01_scope_methods_addendum.json']
m=dict(schema=1,created_utc=now,approved=True,paper='II',source_sha256=sha(source),before_ledger_sha256=sha(old),before_ledger_path=str((out/'before_ledger.tsv').relative_to(R)),event_bundle=bound(bundle),events=len(events),completed_owners=completed,evidence=[bound(p) for p in evidence_paths],review_scope='Root reviewed all comparison narratives, literal edits, method supplements and current exact block bindings. Complete paired proof readings are the named checker records. No visual-reading credit is assigned.')
(out/'manifest.json').write_text(json.dumps(m,indent=2)+'\n')
mp=R/'records/S6_SERIES_PUBLISH_required_check_completion_manifest.json';mold=mp.read_bytes();d=json.loads(mold);(out/'before_completion_manifest.json').write_bytes(mold)
for owner,scope in completed.items():
 assert owner not in d['rows'],owner
 d['rows'][owner]=dict(paper='II',status='done',recorded_utc=now,evidence_path=str((out/'manifest.json').relative_to(R)),evidence_sha256=sha((out/'manifest.json').read_bytes()),scope=scope)
d['updated_utc']=now;mp.write_text(json.dumps(d,indent=2)+'\n')
print(json.dumps(dict(manifest=bound(out/'manifest.json'),bundle=bound(bundle),events=len(events),required_checks_completed=len(completed),completion_manifest_sha256=sha(mp.read_bytes())),indent=2))
