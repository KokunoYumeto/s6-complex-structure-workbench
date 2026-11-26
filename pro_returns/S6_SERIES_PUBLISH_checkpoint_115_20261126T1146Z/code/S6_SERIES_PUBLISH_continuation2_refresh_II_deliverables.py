#!/usr/bin/env python3
"""Refresh Paper II check entries and inventory from the authoritative ledger.

Historical records and other papers' inventory values are preserved. This
derived-record operation adds no mathematical check or page-reading credit.
"""
from pathlib import Path
import collections,csv,datetime as dt,hashlib,io,json,re
R=Path(__file__).resolve().parents[1]
csv.field_size_limit(100_000_000)
def sha(b):return hashlib.sha256(b).hexdigest()
def table(p,delim):
 with p.open(newline='') as f:
  rd=csv.DictReader(f,delimiter=delim);return list(rd),rd.fieldnames
def main():
 now=dt.datetime.now(dt.timezone.utc).isoformat()
 ledger=(R/'CHECK_EVENTS.tsv').read_bytes();events,_=table(R/'CHECK_EVENTS.tsv','\t')
 by=collections.defaultdict(list)
 for e in events:by[e['statement_id']].append(e)
 assert len({e['event_id'] for e in events})==len(events)
 ip=R/'S6_SERIES_PUBLISH_inventory.csv';ib=ip.read_bytes();rows,fields=table(ip,',')
 labels_by_tag=collections.defaultdict(set)
 for row in rows:
  if row['paper']=='II':labels_by_tag[row['tag']].add(row['label'])
 cp=R/'S6_SERIES_PUBLISH_checks_II.md';before=cp.read_bytes();s=before.decode()
 starts=list(re.finditer(r'^<a id="tag-([^\"]+)"></a>\s*$',s,re.M));assert starts
 head=s[:starts[0].start()].replace('# S6_SERIES_GRIND — Paper II check file','# S6_SERIES_PUBLISH — Paper II check file')
 marker='## Current ledger binding\n'
 if marker in head:head=head[:head.index(marker)]
 head+=('## Current ledger binding\n\n'+f'Events and type counts below were regenerated from `CHECK_EVENTS.tsv` at {now}; SHA-256 `{sha(ledger)}`. Event dates, checkers, types, outcomes and evidence groups are retained exactly. Numbers and page locators are inherited from the attached checkpoint-10 tag table; they await the final build. Uses and used-by links retain the attached reference graph until the final regeneration.\n\n')
 pieces=[head];associations=0;added_ids=[];changed_owners=[];association_maps={}
 for i,m in enumerate(starts):
  block=s[m.start():starts[i+1].start() if i+1<len(starts) else len(s)]
  label=re.search(r'^Label: `([^`]+)`',block,re.M);assert label,m.group(1)
  owner=label.group(1);subjects=labels_by_tag[m.group(1)]|{owner}
  es=[e for e in events if e['statement_id'] in subjects]
  association_maps[m.group(1)]=sorted(subjects)
  old_ids=re.findall(r'Event: `([^`]+)`',block)
  new_ids=[e['event_id'] for e in es]
  assert set(old_ids)<=set(new_ids),(owner,set(old_ids)-set(new_ids))
  added_ids.extend(x for x in new_ids if x not in old_ids)
  if old_ids!=new_ids:changed_owners.append(owner)
  counts=collections.Counter(e['type'] for e in es)
  count_text=('; '.join(f'{v} {k}' for k,v in sorted(counts.items()))+'.') if es else '0 recorded events for these exact identifiers.'
  who='; '.join(dict.fromkeys(e['who'] for e in es)) if es else 'None recorded'
  block,n=re.subn(r'(### Recorded routes and present scope\n\n).*?(?=<a id="uses-)',lambda x:x[1]+count_text+f'\n\nRecorded checkers: {who}.\n\n',block,count=1,flags=re.S);assert n==1,(owner,'routes section')
  pos=block.index('### Check events');prefix=block[:pos].replace('S6_SERIES_GRIND_checks_','S6_SERIES_PUBLISH_checks_')
  body='### Check events\n\n'
  for j,e in enumerate(es,1):
   body+=f"#### {j}. {e['date']} — {e['type']}\n\nWho: {e['who']}\n\nEvent: `{e['event_id']}`; evidence group: `{e['evidence_group']}`.\n\nRecorded statement identifier: `{e['statement_id']}`.\n\n"
   body+=f"Source: `{e['source_file']}`"+(f", row {e['source_row']}" if e.get('source_row') else '')+'.\n\n'
   if e.get('date_utc'):body+=f"Recorded UTC time: {e['date_utc']}.\n\n"
   if e.get('where'):body+=f"Recorded locus: {e['where']}.\n\n"
   body+=e['outcome']+'\n\n'
  pieces.append(prefix+body);associations+=len(es)
 out=''.join(pieces).encode()
 assert len(re.findall(r'^Event: `',out.decode(),re.M))==associations
 other=[x.copy() for x in rows if x['paper']!='II']
 counts,_=table(R/'records/S6_SERIES_PUBLISH_statement_check_counts.csv',',');counts={x['label']:x for x in counts if x['paper']=='II'}
 completed=json.loads((R/'records/S6_SERIES_PUBLISH_required_check_completion_manifest.json').read_text())['rows']
 source_hash=sha((R/'S6_SERIES_PUBLISH_II.tex').read_bytes());changed_rows=0
 for row in rows:
  if row['paper']!='II':continue
  label=row['label'];es=by[label];c=collections.Counter(e['type'] for e in es)
  record=json.loads(row['check_record']) if row['check_record'].strip().startswith('{') else {'retained_source_record':row['check_record']}
  old=record.get('canonical_check_events',[])
  assert {e['event_id'] for e in old if 'event_id' in e}<={e['event_id'] for e in es},label
  record['canonical_check_events']=[{k:e.get(k,'') for k in ['event_id','date','date_utc','who','type','phase','evidence_group','source_file','source_row']} for e in es]
  record['current_ledger_sha256']=sha(ledger);record['current_ledger_refresh_utc']=now
  record['current_event_outcomes_locator']='S6_SERIES_PUBLISH_checks_II.md#tag-'+row['tag']
  row['check_record']=json.dumps(record,ensure_ascii=False)
  row['check_summary']=f"{len(es)} canonical event associations; "+'; '.join(f'{k}: {v}' for k,v in sorted(c.items()))
  if label in counts:row['current_statement_owner']=counts[label]['current_statement_owner']
  row['current_source_sha256']=source_hash
  completed_owner=completed.get(label)
  if completed_owner:row['publication_review_status']='Required-check completion is recorded in records/S6_SERIES_PUBLISH_required_check_completion_manifest.json; full paper publication gates remain in PROGRESS_LEDGER.md.'
  changed_rows+=1
 buf=io.StringIO(newline='');w=csv.DictWriter(buf,fieldnames=fields);w.writeheader();w.writerows(rows);io_bytes=buf.getvalue().encode()
 parsed=list(csv.DictReader(io.StringIO(io_bytes.decode())));assert [x for x in parsed if x['paper']!='II']==other
 assert (R/'CHECK_EVENTS.tsv').read_bytes()==ledger
 cp.write_bytes(out);ip.write_bytes(io_bytes)
 receipt=dict(created_utc=now,ledger_sha256=sha(ledger),source_sha256=source_hash,ledger_rows=len(events),check_file_associations=associations,
  new_associations_in_check_file=len(added_ids),new_event_ids_in_check_file=added_ids,owners_with_added_events=changed_owners,II_inventory_rows_refreshed=changed_rows,other_paper_inventory_values_unchanged=True,
  files=[dict(path=cp.name,before_sha256=sha(before),after_sha256=sha(out)),dict(path=ip.name,before_sha256=sha(ib),after_sha256=sha(io_bytes))],
  tag_to_recorded_statement_identifiers=association_maps,association_rule='The exact shared-tag map in the inherited inventory determines each check-file entry. Every event retains its own canonical statement identifier. This association adds no proof-transport or independence claim.',
  mathematical_events_added=0,page_reading_credit=0,source_files_changed=0,scope='Current Paper II check entries and inventory only. Historical check_record members remain; canonical event associations are regenerated from the append-only ledger. Final source graph, numbering and page locators remain pending.')
 stamp=dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ');rp=R/'records'/f'S6_SERIES_PUBLISH_continuation2_II_deliverables_refresh_{stamp}.json';assert not rp.exists();rp.write_text(json.dumps(receipt,indent=2)+'\n')
 print(json.dumps({k:v for k,v in receipt.items() if k not in ['new_event_ids_in_check_file','owners_with_added_events','tag_to_recorded_statement_identifiers']},indent=2))
if __name__=='__main__':main()
