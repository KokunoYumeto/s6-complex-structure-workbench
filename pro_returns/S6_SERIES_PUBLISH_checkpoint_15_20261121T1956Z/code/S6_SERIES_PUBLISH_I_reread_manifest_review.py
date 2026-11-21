#!/usr/bin/env python3
"""Validate a rereading manifest's bindings and expose every scoped association."""
from pathlib import Path
import argparse,csv,hashlib,io,json
R=Path(__file__).resolve().parents[1];csv.field_size_limit(100_000_000)
sha=lambda b:hashlib.sha256(b).hexdigest()
p=argparse.ArgumentParser();p.add_argument('manifest');p.add_argument('--out',required=True);a=p.parse_args()
mp=R/a.manifest;mr=mp.read_bytes();x=json.loads(mr);checked={}
def check(v):
 if isinstance(v,dict):
  if 'path' in v and 'sha256' in v and isinstance(v['path'],str):
   f=(R/v['path']).resolve();assert f.is_relative_to(R);assert sha(f.read_bytes())==v['sha256'],v['path'];checked[v['path']]=v['sha256']
  for w in v.values():check(w)
 elif isinstance(v,list):
  for w in v:check(w)
check(x)
assert x['event_type']=='used and rechecked in this run'
assert x['new_independent_targeted_computation_credit']==0
es=x['events'];assert len(es)==x['candidate_event_count']==len({v['statement_id'] for v in es})
assert len({(v['owning_printed_statement']['kind'],v['owning_printed_statement']['line']) for v in es})==len(es)
source=(R/x['reference_source19']['path']).read_text();lines=source.splitlines(True)
scopes=[];mapped=[];instance_keys=[]
for e in es:
 assert e['event_count']==1 and e['event_type']==x['event_type']
 owner=e['owning_printed_statement'];assert owner['id']==e['statement_id'] and owner['id'] in owner['identities']
 start=sum(map(len,lines[:owner['line']-1]));prefix='\\begin{'+owner['kind']+'}'
 assert source.startswith(prefix,start),(owner,start)
 stop=source.index('\\end{'+owner['kind']+'}',start)+len('\\end{'+owner['kind']+'}')
 block=source[start:stop];assert ('\\StatementRecord{'+owner['id']+'}') in block
 entries=[]
 for inst in e['manual_review_instances']:
  assert inst['complete_exposed_proof_actually_read'] and inst['exact_proposed_change_manually_compared_in_full_proof_context']
  assert inst['independent_derivation_claimed'] is False
  original=(R/inst['original_full_context']['path']).read_text();proposed=(R/inst['proposed_full_context']['path']).read_text()
  for text in [original,proposed]:assert r'\begin{proof}' in text and r'\end{proof}' in text
  scope=inst['actual_scope']
  if scope not in scopes:scopes.append(scope)
  key=(e['statement_id'],inst['reviewer'],inst['before_candidate'],inst['original_full_context']['sha256'],inst['proposed_full_context']['sha256']);assert key not in instance_keys;instance_keys.append(key)
  entries.append({'reviewer':inst['reviewer'],'candidate':inst['before_candidate'],'guards':inst['guard_ids'],'proof_bytes_changed':inst['proof_bytes_changed'],'scope':scopes.index(scope)+1})
 mapped.append({'statement_id':e['statement_id'],'owner_kind':owner['kind'],'owner_line':owner['line'],'instances':entries,'qualification':e.get('R2_qualification')})
for alias in x['attested_identifier_to_current_owner_map']:
 assert source.count(alias['exact_statement_header'])==1
 assert sha(alias['exact_statement_header'].encode())==alias['statement_header_sha256']
 aux=(R/alias['aux']['path']).read_text();assert alias['attested_identifier_aux'] in aux and alias['owner_aux'] in aux
 head=alias['exact_statement_header'];assert ('\\label{'+alias['attested_identifier']+'}') in head and ('\\label{'+alias['current_printed_owner']+'}') in head
before=(R/x['before_ledger']['path']).read_bytes();after=(R/x['preview_ledger']['path']).read_bytes()
assert after.startswith(before) and sha(after)==x['prospective_after_ledger_sha256']
def rows(raw):return list(csv.DictReader(io.StringIO(raw.decode(),newline=''),delimiter='\t'))
bs=rows(before);as_=rows(after);adds=rows((R/x['proposal_event_bundle']['path']).read_bytes())
assert len(bs)==x['before_rows'] and len(as_)==x['prospective_after_rows'] and as_==bs+adds
assert len(adds)==len(es) and [v['event_id'] for v in adds]==[v['event_id'] for v in es]
assert [v['statement_id'] for v in adds]==[v['statement_id'] for v in es]
assert all(v['type']==x['event_type'] and v['evidence_group']==x['evidence_group'] for v in adds)
record={'manifest':{'path':a.manifest,'sha256':sha(mr)},'binding_files_verified':len(checked),'unique_printed_owners':len(es),'actual_comparison_instances':len(instance_keys),'scope_catalog':{i+1:s for i,s in enumerate(scopes)},'rows':mapped,'before_rows':len(bs),'after_rows':len(as_),'exact_old_ledger_prefix_and_tail':True,'counts_after':x['counts_after'],'root_model_review_approval':False,'automatic_validation_adds_check_events':0}
out=R/a.out;assert not out.exists();out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k not in ['rows','scope_catalog']},indent=2))
print('SCOPES',json.dumps(record['scope_catalog'],indent=2))
for i,row in enumerate(mapped,1):print(json.dumps({'n':i,**row},separators=(',',':')))
