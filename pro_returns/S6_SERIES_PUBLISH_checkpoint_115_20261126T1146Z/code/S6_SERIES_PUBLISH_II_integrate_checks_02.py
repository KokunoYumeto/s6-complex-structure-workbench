"""Admit the four reviewed C checks and their separate editorial rereadings."""
from pathlib import Path
import csv,datetime,hashlib,io,json,sys
R=Path(__file__).resolve().parents[1];csv.field_size_limit(100_000_000)
sha=lambda b:hashlib.sha256(b).hexdigest()
out=R/'records/S6_SERIES_PUBLISH_II_checks_02';bundle=R/'records/S6_SERIES_PUBLISH_zzz_continuation_002_CHECK_EVENTS.tsv'
def bound(p):
 p=R/p if isinstance(p,str) else p
 return dict(path=str(p.relative_to(R)),sha256=sha(p.read_bytes()))
if '--verify' in sys.argv:
 m=json.loads((out/'manifest.json').read_text());old=(out/'before_ledger.tsv').read_bytes();new=(R/'CHECK_EVENTS.tsv').read_bytes()
 assert sha(old)==m['before_ledger_sha256'] and new.startswith(old)
 oldrows=list(csv.DictReader(io.StringIO(old.decode(),newline=''),delimiter='\t'));newrows=list(csv.DictReader(io.StringIO(new.decode(),newline=''),delimiter='\t'));additions=list(csv.DictReader(bundle.open(),delimiter='\t'))
 assert newrows[:len(oldrows)]==oldrows and newrows[len(oldrows):]==additions
 assert len({x['event_id'] for x in newrows})==len(newrows)
 d=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),manifest=bound(out/'manifest.json'),event_bundle=bound(bundle),before_rows=len(oldrows),after_rows=len(newrows),added_rows=len(additions),before_ledger_sha256=sha(old),after_ledger_sha256=sha(new),old_ledger_bytes_and_rows_preserved=True,required_checks_completed=4)
 (out/'append_verification.json').write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(d,indent=2));sys.exit(0)
assert not out.exists() and not bundle.exists();out.mkdir();now=datetime.datetime.now(datetime.timezone.utc).isoformat()
old=(R/'CHECK_EVENTS.tsv').read_bytes();assert sha(old)=='3590e48ec3e5ea66be61d455e99b0d7bb2c8bbd6040b062837290ab69fe67f32';(out/'before_ledger.tsv').write_bytes(old)
reader=csv.DictReader(io.StringIO(old.decode(),newline=''),delimiter='\t');oldrows=list(reader);fields=reader.fieldnames
proposal='agents/ii_infra/S6_SERIES_PUBLISH_II_first_four_event_proposals.json';p=json.loads((R/proposal).read_text())
source=(R/'S6_SERIES_PUBLISH_II.tex').read_text();events=[];owners=[]
def validate(obj):
 if isinstance(obj,dict):
  if 'path' in obj and 'sha256' in obj:assert sha((R/obj['path']).read_bytes())==obj['sha256'],obj['path']
  for v in obj.values():validate(v)
 elif isinstance(obj,list):
  for v in obj:validate(v)
validate(p)
method={
 '01F8':'The prereading affine homogeneous-matrix computation and integer Smith relations provide a different method from the old sixfold symbolic sigma substitution and determinant. The explicit real diffeomorphism Phi, its two-sided inverse and five equivariances transport the lattice and deck calculation exactly. Complex-analytic and canonical-character assertions were verified separately in each construction; no unproved holomorphic identification is used.',
 '01F9':'The prereading A5 perfectness and central commutator method is transported to the printed120-element set by the explicit injective quaternion-to-SU2 homomorphism, adjoint kernel plus/minus1, and60-element rotation/permutation graph. The coordinate swap of the icosahedron is explicit. This central-extension route supplies the different method beyond the overlapping full multiplication-table check.',
 '01FA':'The smooth ambient scope required for Cartier pullback is explicit. Root verified all coded receiving uses and the complete INT2 receiving proof; every mathematical step agrees at this scope.',
 '01G8':'The proof uses the exact rational-cohomology pullback from the connected-fibre base to deduce genus zero, then the general component formula. Smoothness is explicit for the component-resolution obstruction, and all coded receiving uses are checked.'}
for e in p['events']:
 b=e['applied_owning_block'];assert source.count((R/b['path']).read_text())==1
 owner=e['statement_id'];owners.append(owner)
 for typ,kind,outcome in [(e['type'],'check',e['outcome']+' '+method[e['tag']]+' Original target proofs were withheld until the frozen derivation; previously read II outlines are inputs without fresh independence credit. The transport supplement was written after release.'),('used and rechecked in this run','editorial_reread','The checker actually read both complete original and proposed statement/proof blocks. The exact title, scope and prose changes are recorded in the applied14-guard batch. This is the separate editorial rereading, with no additional independent derivation claim.')]:
  row={k:'' for k in fields};row.update(statement_id=owner,date='2026-11-21',who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; reasoning effort inherited, no separate numerical setting exposed; S6_SERIES_PUBLISH checker restore_build',type=typ,outcome=outcome,event_id=f'S6_SERIES_PUBLISH_II_C_{e["tag"]}_{kind}_20261121',phase='S6_SERIES_PUBLISH_II',source_file=proposal,source_row=str(len(events)+2),source_event_type=typ,evidence_group=e['evidence_group'],publish_input_file=bundle.name,publish_input_row=str(len(events)+2),date_utc=now,where=proposal);events.append(row)
assert len(owners)==len(set(owners))==4 and len(events)==8
with bundle.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(events)
evidence=[proposal,'agents/ii_infra/S6_SERIES_PUBLISH_II_first_four_comparison.json','records/S6_SERIES_PUBLISH_II_Bv2_C1_editorial_apply.json','records/S6_SERIES_PUBLISH_II_01FA_01G8_root_receiver_audit.json','code/S6_SERIES_PUBLISH_II_first_four_transport_compare.py','agents/ii_infra/checks/S6_SERIES_PUBLISH_II_first_four_transport_output.json']
m=dict(schema=1,created_utc=now,approved=True,paper='II',source_sha256=sha(source.encode()),before_ledger_sha256=sha(old),event_bundle=bound(bundle),events=len(events),completed_owners=owners,method_comparisons=method,evidence=[bound(x) for x in evidence],reading_scope='Root read complete method supplement and all literal guards/comparisons; actual whole original/revised block reading is the checker record.',visual_reading_credit=0)
(out/'manifest.json').write_text(json.dumps(m,indent=2)+'\n')
mp=R/'records/S6_SERIES_PUBLISH_required_check_completion_manifest.json';mold=mp.read_bytes();(out/'before_completion_manifest.json').write_bytes(mold);d=json.loads(mold)
for e in p['events']:
 owner=e['statement_id'];assert owner not in d['rows']
 d['rows'][owner]=dict(paper='II',status='done',recorded_utc=now,evidence_path=str((out/'manifest.json').relative_to(R)),evidence_sha256=sha((out/'manifest.json').read_bytes()),scope=method[e['tag']]+' Complete prereading derivation, original proof comparison and applied revised-block reading bound.')
d['updated_utc']=now;mp.write_text(json.dumps(d,indent=2)+'\n')
print(json.dumps(dict(manifest=bound(out/'manifest.json'),events=len(events),required_checks_completed=4)))
