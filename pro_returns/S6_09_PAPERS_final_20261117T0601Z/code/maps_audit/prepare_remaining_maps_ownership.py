"""Propose disjoint remaining proof reads; never alter any earlier check."""
from pathlib import Path
import collections, csv, json, re
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'deliverables/work/maps_audit'
rows=json.loads((OUT/'results_audit.json').read_text())
blocks=json.loads((OUT/'source_blocks.json').read_text())
events=json.loads((OUT/'check_events.json').read_text())
evmap={e.get('event_id',e.get('id')):e for e in events}
remaining=[];already=[]
for row in rows:
 ident=row['id']; part=ident.split('.')[0]
 if part=='D':continue
 current=row.get('your_check','')
 incomplete=(not current or 'Partial proof readings only' in current)
 target=remaining if incomplete else already
 locs=blocks.get(ident,row.get('source_blocks',[]))
 prior=[evmap.get(e,{'event_id':e,'note':'Inspect the original preserved record'}) for e in row.get('check_event_ids',[])]
 item=dict(id=ident,statement=row['statement'],source_status=row.get('status'),
  reading_scope=('Partial inspection; a complete proof read is still needed' if ident in {'B.5.2','E.1.4','F.2.2'} else 'Complete new proof read still needed') if incomplete else 'Receiving proof already fully read; close only separately stated dependencies, source checks, reruns and credit comparison',
  proposed_owner=('/root/maps_audit' if part in 'ABC' else '/root/cdp_audit' if part=='E' else '/root'),
  ownership_status='Proposal sent to parent; parent determines final assignment',
  sources=[{k:v for k,v in b.items() if k!='text'} for b in locs],
  inputs_to_follow=[m for b in locs for m in re.findall(r'\\input\{([^}]+)\}',b.get('text',''))],
  current_recorded_check=current,prior_checks=prior,
  note='Read every nested proof input and operative prerequisite. A source-block range is a locator, not a certification that all proof text lies inside that range. Keep all previous source/self/reviewer checks.')
 if ident in {'E.2.4','F.2.4','F.3.3'}:
  item['special_source_scope']='This is a final conclusion/synthesis statement. Follow all referenced later complete proofs; do not mistake its short paragraph for an independent full proof.'
 target.append(item)

counts=collections.Counter(x['proposed_owner'] for x in remaining)
manifest=dict(reader='GPT-6 Astra (OpenAI, ChatGPT Pro mode)',effort='Pro',date='2026-11-17',
 complete_receiving_reads_non_D=len(already),remaining_complete_reads_non_D=len(remaining),
 proposed_counts=dict(counts),canonical_source_root='sources/returns/S6_04_MAPS_MANIFOLDS',
 source_blocks='deliverables/work/maps_audit/source_blocks.json',
 full_inventory='deliverables/work/maps_audit/results_audit.json',
 preserved_events='deliverables/work/maps_audit/check_events.json',
 original_programs='sources/returns/S6_04_MAPS_MANIFOLDS/code',
 prior_rerun_outputs='deliverables/code/maps_audit/MAPS/code',
 instruction='D69 belongs to invariants_arithmetic and is excluded. Do not edit the maps audit updater, top inventory or originals. Save new independent audit events in your own work directory for later merging. No PaperIII assembly before parent authorization.',
 remaining=remaining,already_full_read_dependency_only=already)
(OUT/'remaining_maps_ownership_proposal.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
with (OUT/'remaining_maps_ownership_proposal.csv').open('w',newline='') as f:
 keys=['id','proposed_owner','reading_scope','statement','source_locators','note']
 w=csv.DictWriter(f,fieldnames=keys);w.writeheader()
 for x in remaining:
  w.writerow({**{k:x[k] for k in ['id','proposed_owner','reading_scope','statement','note']},'source_locators':'; '.join(f"{b['file']}:{b['start_line']}–{b['end_line']}" for b in x['sources'])})
for who in counts:
 batch=[x for x in remaining if x['proposed_owner']==who]
 name={'/root':'remaining_F_batch.json','/root/cdp_audit':'remaining_E_batch.json','/root/maps_audit':'remaining_B_batch.json'}[who]
 (OUT/name).write_text(json.dumps(batch,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:manifest[k] for k in ['complete_receiving_reads_non_D','remaining_complete_reads_non_D','proposed_counts']}))
