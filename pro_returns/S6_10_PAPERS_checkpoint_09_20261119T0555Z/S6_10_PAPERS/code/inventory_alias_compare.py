#!/usr/bin/env python3
"""Report source-block identity and overlap without transferring proof credit."""
from pathlib import Path
import csv, hashlib, json
from collections import defaultdict
from inventory_current_events import events

OUT=Path(__file__).resolve().parents[1]
ROOT=OUT.parents[1]
rows=list(csv.DictReader((OUT/'S6_10_PAPERS_inventory.csv').open()))
index=json.loads((OUT/'analysis/inventory_source_index.json').read_text())
by_label=defaultdict(list)
for event in events(): by_label[event['label']].append(event)
texts={}
blocks=[]
for row in rows:
    key=row['source_run']+':'+row['source_id']
    loc=index.get(key,{})
    if not loc.get('found') or 'start' not in loc or 'end' not in loc: continue
    file=loc['file']
    if file not in texts:
        path=Path(file)
        if not path.is_absolute(): path=ROOT/path
        texts[file]=path.read_text()
    exact=texts[file][loc['start']:loc['end']]
    blocks.append({'label':row['label'],'paper':row['paper'],'source_key':key,
                   'file':file,'start':loc['start'],'end':loc['end'],
                   'sha256':hashlib.sha256(exact.encode()).hexdigest(),
                   'current_events':len(by_label[row['label']]),
                   'labels_in_block':loc.get('all_labels_in_block',[]),
                   'text':exact})
checked=[b for b in blocks if b['current_events']]
report=[]
for target in blocks:
    if target['paper'] not in {'II','VI'} or target['current_events']: continue
    matches=[]
    for canonical in checked:
        if canonical['label']==target['label']: continue
        same_interval=(target['file']==canonical['file'] and target['start']==canonical['start'] and target['end']==canonical['end'])
        same_bytes=target['sha256']==canonical['sha256']
        overlap=(target['file']==canonical['file'] and max(target['start'],canonical['start'])<min(target['end'],canonical['end']))
        if not (same_interval or same_bytes or overlap): continue
        kind='exact shared interval' if same_interval else ('identical bytes at a separate interval' if same_bytes else 'overlapping interval; text differs')
        item={k:canonical[k] for k in ['label','source_key','file','start','end','sha256','current_events']}
        item.update(match_kind=kind,same_bytes=same_bytes)
        if not same_bytes:
            a,b=target['text'],canonical['text'];prefix=0
            while prefix<min(len(a),len(b)) and a[prefix]==b[prefix]:prefix+=1
            suffix=0
            while suffix<min(len(a),len(b))-prefix and a[-1-suffix]==b[-1-suffix]:suffix+=1
            item['differing_text']={'common_prefix_chars':prefix,'common_suffix_chars':suffix,
                'target':a[prefix:len(a)-suffix if suffix else len(a)],
                'canonical':b[prefix:len(b)-suffix if suffix else len(b)]}
        matches.append(item)
    if matches:
        target={k:v for k,v in target.items() if k!='text'}
        target['matches']=sorted(matches,key=lambda x:(x['match_kind']!='exact shared interval',not x['label'].startswith('cdp:'),x['label']))
        report.append(target)
result={'rule':'Exact source comparison only. No mathematical check or credit is transferred. Any differing text is retained verbatim in this report.','targets_with_current_events_excluded':True,'candidates':report}
(OUT/'analysis/inventory_II_VI_alias_block_comparison.json').write_text(json.dumps(result,indent=2))
flat=[]
for target in report:
    for m in target['matches']:
        flat.append({'alias_label':target['label'],'canonical_event_label':m['label'],'match_kind':m['match_kind'],
                     'target_source_key':target['source_key'],'canonical_source_key':m['source_key'],
                     'target_file':target['file'],'target_start':target['start'],'target_end':target['end'],
                     'target_sha256':target['sha256'],'canonical_start':m['start'],'canonical_end':m['end'],
                     'canonical_sha256':m['sha256'],'canonical_current_event_count':m['current_events']})
with (OUT/'analysis/inventory_II_VI_alias_block_comparison.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(flat[0]) if flat else ['alias_label'],delimiter='\t');w.writeheader();w.writerows(flat)
counts=defaultdict(int)
for row in flat:counts[row['match_kind']]+=1
(OUT/'analysis/inventory_II_VI_alias_block_comparison.md').write_text('# Paper II/VI exact alias comparison\n\n'+result['rule']+'\n\n'+
    f"Targets with a checked-block match: {len(report)}. Pair counts: {dict(counts)}.\n\n"+
    '| Unreviewed alias | Label with a current event | Source comparison |\n|---|---|---|\n'+
    '\n'.join('| '+x['alias_label']+' | '+x['canonical_event_label']+' | '+x['match_kind']+' |' for x in flat)+'\n')
print(json.dumps({'target_candidates':len(report),'pairs':dict(counts)}))
