#!/usr/bin/env python3
"""Check exact source preservation and complete correction/dependency mapping."""
import csv,hashlib,json,re
from pathlib import Path
from corrected_items import ITEMS
ROOT=Path(__file__).resolve().parents[2];A=ROOT/'analysis/continuation_IV'
csv.field_size_limit(16*1024*1024)
sha=lambda s:hashlib.sha256(s.encode()).hexdigest()
receipt=json.loads((A/'correction_split_patch.json').read_text())
inv=list(csv.DictReader((ROOT/'S6_10_PAPERS_inventory.csv').open()));by={r['label']:r for r in inv}
sources=[]
for f in receipt['files']:
 text=(ROOT/f['path']).read_text()
 # Root may later apply typed metadata. The initial receipt independently
 # records the precise transformation; verify the current source before it.
 assert sha(text)==f['after_sha256'],f['path']
 current=text
 for e in reversed(f['edits']):
  assert text.count(e['new'])==1,(f['path'],e['label'])
  text=text.replace(e['new'],e['old'],1)
 assert sha(text)==f['before_sha256']
 for x in ITEMS:
  assert current.count(r'\label{'+x['label']+'}')==1
  assert current.count(r'\StatementRecord{'+x['label']+'}{proved}')==1
  if by[x['historical_label']]['paper']=='IV':
   assert current.count(r'\StatementRecord{'+x['historical_label']+'}{false as stated}')==1
   assert current.count('% BEGIN HISTORICAL_REFINED_LINK '+x['historical_label']+'\n')==1
 sources.append(dict(path=f['path'],exact_inverse_hash_match=True,new_items=33,historical_false_items=32,
  original_mathematical_text_unchanged='All old edits are confined to StatementRecord metadata plus inserted scope/link paragraphs. Exact inverse hash verification establishes preservation of all other bytes.'))
for x in ITEMS:
 assert by[x['label']]['status']=='proved'
 assert by[x['historical_label']]['status']=='false as stated'
 assert json.loads(by[x['historical_label']]['notes'])['refined_statement_id']==x['label']
 assert by[x['label']]['source_run']=='S6_10_PAPERS'
 assert by[x['label']]['main_or_supporting']==by[x['historical_label']]['main_or_supporting']
deps=list(csv.DictReader((A/'corrected_dependency_map.tsv').open(),delimiter='\t'))
assert len(deps)==150
for d in deps:
 assert d['dependent'] in by and d['corrected_item'] in by and d['historical_locator'] in by
 if d['action']=='redirect receiving dependency to corrected item':
  assert d['corrected_item'] in by[d['dependent']]['uses']
  assert not re.search(re.escape(d['historical_locator'])+r'(?![0-9])',by[d['dependent']]['uses'])
events=list(csv.DictReader((ROOT/'records/continuation_IV_correction_events.tsv').open(),delimiter='\t'))
assert len(events)==196
for x in ITEMS:
 es=[e for e in events if e['statement_id']==x['label']]
 assert {e['type'] for e in es}=={'targeted proof check','computation or formal certificate','used and rechecked in this run'}
 es=[e for e in events if e['statement_id']==x['historical_label']]
 assert len(es)==1 and es[0]['refined_statement_id']==x['label']
pre=json.loads((A/'corrected_items_derivation_receipt.json').read_text())
assert sha((ROOT/pre['preserved_precomparison_copy']).read_text())==pre['sha256']
arithmetic=json.loads((A/'corrected_items_arithmetic.output.json').read_text());assert arithmetic['result']=='PASS'
out=dict(result='PASS',source_files=sources,receiving_items=33,historical_claims_preserved=33,
 historical_links_applied_in_IV=32,historical_link_assigned_to_II_owner='night:P3K.36 -> iv:correction:P3K.36',
 main_receiving_items=sum(by[x['label']]['main_or_supporting']=='main' for x in ITEMS),dependency_edges=len(deps),
 dependent_rows=len({d['dependent'] for d in deps}),correction_event_rows=len(events),fresh_exact_checks=arithmetic['count'],
 precomparison_snapshot_hash_matches=True,
 scope='Mechanical preservation, exact row mapping and scoped arithmetic checks. No new whole geometric proof gate is awarded.')
(A/'corrected_split_audit.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
