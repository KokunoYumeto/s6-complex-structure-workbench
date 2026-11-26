#!/usr/bin/env python3
"""Refresh current Paper II derived records from the append-only ledger.

Other papers' rows are preserved, and their sources are never opened. No full
per-refresh copies or check events are created. The original parsing/counting
functions are imported unchanged, with the authoritative ledger used directly.
"""
from pathlib import Path
import collections,csv,datetime as dt,hashlib,importlib.util,io,json
R=Path(__file__).resolve().parents[1]
BASE=R.parent
csv.field_size_limit(100_000_000)
spec=importlib.util.spec_from_file_location('recompute',R/'agents/provenance/code/S6_SERIES_PUBLISH_recompute_records.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
def sha(b):return hashlib.sha256(b).hexdigest()
def read(p,delim='\t'):
 with p.open(newline='') as f:
  rr=csv.DictReader(f,delimiter=delim);return list(rr),rr.fieldnames
def encoded(rows,fields,delim='\t'):
 o=io.StringIO(newline='');w=csv.DictWriter(o,fieldnames=fields,delimiter=delim);w.writeheader();w.writerows(rows);return o.getvalue().encode()
def main():
 now=dt.datetime.now(dt.timezone.utc).isoformat()
 ledger=(R/'CHECK_EVENTS.tsv').read_bytes();events,fields=read(R/'CHECK_EVENTS.tsv')
 baseline=(BASE/'S6_SERIES_PUBLISH_checkpoint_21/CHECK_EVENTS.tsv').read_bytes()
 assert ledger.startswith(baseline)
 assert len({e['event_id'] for e in events})==len(events)
 bundles=sorted((R/'records').glob('S6_SERIES_PUBLISH_continuation2_*_CHECK_EVENTS.tsv'))
 prefix_count=len(read(BASE/'S6_SERIES_PUBLISH_checkpoint_21/CHECK_EVENTS.tsv')[0])
 tail=[]
 for p in bundles:tail.extend(read(p)[0])
 assert events[prefix_count:]==tail
 tags,_=read(BASE/'S6_SERIES_GRIND_tags.tsv')
 inv,_=read(BASE/'S6_SERIES_GRIND_inventory.csv',',');inventory={x['label']:x for x in inv}
 tag_by_label={x['label']:x for x in tags}
 alias={x['label']:x['label'] for x in tags};alias.update({'tag:'+x['tag']:x['label'] for x in tags})
 by_id=collections.defaultdict(list)
 for e in events:by_id[alias.get(e['statement_id'],e['statement_id'])].append(e)
 source=R/'S6_SERIES_PUBLISH_II.tex';source_hash=sha(source.read_bytes());sts=m.statements(source)
 active={x['statement_id'] for x in sts if x['statement_id']}
 main_ids={x['statement_id'] for x in sts if x['kind']=='maintheorem'}
 owners={label:x['statement_id'] for x in sts for label in x['owned_labels']}
 subjects=active|{label for label in owners if label in tag_by_label and tag_by_label[label]['kind']=='statement'}
 graph={x['statement_id']:{owners.get(y,y) for y in x['refs']} for x in sts if x['statement_id']}
 reachable=set(main_ids);stack=list(main_ids)
 while stack:
  for x in graph.get(stack.pop(),()):
   if x in active and x not in reachable:reachable.add(x);stack.append(x)
 scopes={'cp10_printed_statements':{t['label'] for t in tags if t['paper']=='II' and t['kind']=='statement'},
  'cp10_all_tagged_targets':{t['label'] for t in tags if t['paper']=='II'},
  'current_primary_statement_identifiers':active,'current_printed_statements_and_definitions':subjects}
 stats=[]
 for scope,ids in scopes.items():
  selected=[e for e in events if alias.get(e['statement_id'],e['statement_id']) in ids]
  steps=[e for e in events if any(e['statement_id'].startswith(sid+' step ') for sid in main_ids)] if scope.startswith('current_') else []
  counts=collections.Counter(e['type'] for e in selected)
  stats.append(dict(paper='II',scope=scope,statements=len(active) if scope.startswith('current_') else len(ids),subject_identifiers=len(ids),
   event_associations=len(selected),declared_evidence_groups=len({e['evidence_group'] for e in selected}),outline_step_associations_separate=len(steps),
   **{k:counts[k] for k in ['targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found',"refuted, with the refined statement's id"]}))
 results=[];pending=[]
 for t in (t for t in tags if t['paper']=='II' and t['kind']=='statement'):
  es=by_id[t['label']];sub=[e for e in es if e['type'] in m.SUBSTANTIVE]
  groups={e['evidence_group'] for e in sub};checkers={m.checker(e) for e in sub}
  row=dict(tag=t['tag'],paper='II',number_cp10=t['number'],page_cp10=t['page'],label=t['label'],status=t['status'],
   active_current_statement=str(t['label'] in subjects).lower(),current_statement_owner=owners.get(t['label'],t['label']),
   main_dependency_reference_closure=str(owners.get(t['label'],t['label']) in reachable).lower(),
   main_or_supporting=inventory.get(t['label'],{}).get('main_or_supporting',''),substantive_associations=len(sub),
   substantive_evidence_groups=len(groups),distinct_checker_labels=len(checkers),all_associations=len(es),
   below_bar='yes' if len(groups)<2 or len(checkers)<2 else ('two_only' if len(groups)<3 else 'no'),checker_labels=' || '.join(sorted(checkers)))
  results.append(row)
  if row['below_bar']=='yes' or row['below_bar']=='two_only' and owners.get(t['label'],t['label']) in reachable:pending.append(row)
 printed=[{'paper':'II','source':str(source),**x,'labels':';'.join(x['labels']),'owned_labels':';'.join(x['owned_labels']),'refs':';'.join(x['refs'])} for x in sts]
 edges=[{'paper':'II','from':x,'to':y,'within_current_paper':str(y in active).lower(),'interpretation':'reference edge; premise status requires review'} for x,ys in graph.items() for y in sorted(ys)]
 aliases=[dict(paper='II',current_statement_id=owners.get(x,x),retained_statement_identifier=x,scope='explicit label retained in current source; event association is not duplicated') for x in sorted(subjects)]
 changes=[]
 for name,newrows in [('S6_SERIES_PUBLISH_check_counts.tsv',stats),('S6_SERIES_PUBLISH_statement_check_counts.csv',results),
  ('S6_SERIES_PUBLISH_required_check_candidates.csv',pending),('S6_SERIES_PUBLISH_printed_statements.tsv',printed),
  ('S6_SERIES_PUBLISH_reference_graph.tsv',edges),('S6_SERIES_PUBLISH_current_statement_aliases.tsv',aliases)]:
  p=R/'records'/name;before=p.read_bytes();delim=',' if p.suffix=='.csv' else '\t';old,f=read(p,delim)
  pos=next((i for i,x in enumerate(old) if x['paper']=='II'),len(old));other=[x for x in old if x['paper']!='II']
  insertion=sum(x['paper']!='II' for x in old[:pos]);merged=other[:insertion]+newrows+other[insertion:]
  out=encoded(merged,f,delim);check=list(csv.DictReader(io.StringIO(out.decode()),delimiter=delim))
  assert [x for x in check if x['paper']!='II']==other
  p.write_bytes(out);changes.append(dict(path=str(p.relative_to(R)),before_sha256=sha(before),after_sha256=sha(out),old_II_rows=sum(x['paper']=='II' for x in old),new_II_rows=len(newrows),other_paper_rows_unchanged=True))
 p=R/'records/S6_SERIES_PUBLISH_records_summary.json';before=p.read_bytes();summary=json.loads(before)
 summary['merged_rows']=len(events);summary['input_rows']=len(events)+summary['exact_duplicates_removed']
 summary['all_event_types']=dict(collections.Counter(e['type'] for e in events))
 all_results,_=read(R/'records/S6_SERIES_PUBLISH_statement_check_counts.csv',',')
 summary['below_bar_cp10_statement_scope']=dict(collections.Counter(x['below_bar'] for x in all_results))
 summary['last_refresh_scope']='Paper II only; other paper rows and sources held at their recorded state.'
 summary['updated_utc']=now;p.write_text(json.dumps(summary,indent=2)+'\n')
 changes.append(dict(path=str(p.relative_to(R)),before_sha256=sha(before),after_sha256=sha(p.read_bytes())))
 # records/CHECK_EVENTS.tsv is the current derived mirror, not a per-batch copy.
 mirror=R/'records/CHECK_EVENTS.tsv'
 mirror_before=sha(mirror.read_bytes()) if mirror.exists() else None;mirror.write_bytes(ledger)
 changes.append(dict(path='records/CHECK_EVENTS.tsv',before_sha256=mirror_before,after_sha256=sha(ledger)))
 assert (R/'CHECK_EVENTS.tsv').read_bytes()==ledger and sha(source.read_bytes())==source_hash
 completion=json.loads((R/'records/S6_SERIES_PUBLISH_required_check_completion_manifest.json').read_text())
 resolved=sum(v['paper']=='II' for v in completion['rows'].values())
 receipt=dict(created_utc=now,source_sha256=source_hash,ledger_sha256=sha(ledger),ledger_rows=len(events),ledger_unchanged=True,
  verified_cp21_prefix_rows=prefix_count,exact_appended_bundle_rows=len(tail),derived_changes=changes,other_paper_sources_opened=False,
  mathematical_events_added=0,page_reading_credit=0,required_II_resolved=resolved,required_II_open=197-resolved,
  raw_candidate_II_rows=len(pending),scope='Derived candidate flags retain their historical algorithm and are not substituted for the 197-row required-check manifest; production retirement remains authoritative.',current_II_counts=stats)
 stamp=dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
 p=R/'records'/f'S6_SERIES_PUBLISH_continuation2_refresh_II_{stamp}.json';assert not p.exists();p.write_text(json.dumps(receipt,indent=2)+'\n')
 print(json.dumps({'receipt':str(p.relative_to(R)),'ledger_rows':len(events),'II_resolved':resolved,'II_open':197-resolved,'raw_II_candidates':len(pending)},indent=2))
if __name__=='__main__':main()
