"""Append-only permanent tags and exact source-anchor alias transport."""
from pathlib import Path
import csv,json,re
from collections import defaultdict
from tex_tools import PAPERS
ROOT=Path(__file__).resolve().parents[1]
A=ROOT/'analysis'
csv.field_size_limit(10**9)

def base36(n):
    digits='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ';s=''
    while n:n,r=divmod(n,36);s=digits[r]+s
    return s.zfill(4)

def main():
    owners=json.loads((A/'label_owners.json').read_text())
    aux={p:json.loads((A/f'baseline_labels_{p}.json').read_text()) for p in PAPERS}
    structure=json.loads((A/'source_statement_structure.json').read_text())
    primary={r['label'] for values in structure.values() for r in values}
    records=json.loads((A/'source_statement_records.json').read_text())
    record_labels={r['label'] for r in records}
    with (ROOT/'S6_SERIES_GRIND_inventory.csv').open() as stream:rows=list(csv.DictReader(stream))
    inventory_labels={r['label'] for r in rows}
    groups=defaultdict(list)
    source_for={}
    for label in owners:
        original=label.replace('sec:II:all:','sec:II:') if label.startswith('sec:II:all:') else label
        choices=[p for p in PAPERS if original in aux[p]]
        if label.startswith('sec:II:all:'):choices=['VI']
        elif len(choices)>1 and owners[label]=='II':choices=['II']
        if len(choices)!=1:raise ValueError((label,choices))
        paper=choices[0];source_for[label]=paper
        dest=aux[paper][original]['destination']
        groups[(paper,dest)].append(label)
    alias={};canon_owners={};kind={}
    for key,labels in sorted(groups.items()):
        labels.sort(key=lambda lab:(lab not in record_labels,lab not in primary,lab not in inventory_labels,len(lab),lab))
        canonical=labels[0]
        for lab in labels:alias[lab]=canonical
        canon_owners[canonical]=owners[canonical]
        kind[canonical]='statement' if any(lab in primary or lab in record_labels for lab in labels) else 'reference target'
    for row in rows:
        lab=row['label']
        if lab not in alias:
            alias[lab]=lab;canon_owners[lab]=row['paper'];kind[lab]='inventory disposition'
    registry_path=A/'permanent_tag_registry.json'
    registry=json.loads(registry_path.read_text()) if registry_path.exists() else {}
    next_number=max([int(t,36) for t in registry.values()]+[0])+1
    for label in sorted(set(alias.values())):
        if label not in registry:registry[label]=base36(next_number);next_number+=1
    assert len(set(registry.values()))==len(registry)
    registry_path.write_text(json.dumps(registry,indent=2))
    alias_path=A/'label_tags.json'
    labeltags={lab:{'tag':registry[canonical],'canonical_label':canonical,'paper':canon_owners[canonical],'kind':kind[canonical]} for lab,canonical in alias.items()}
    alias_path.write_text(json.dumps(labeltags,indent=2))
    statuses=defaultdict(set)
    for row in rows:statuses[alias[row['label']]].add(row['status'])
    for r in records:
        if r['label'] in alias:statuses[alias[r['label']]].add(r['status'])
    tagrows=[]
    for lab,tag in sorted(registry.items(),key=lambda kv:kv[1]):
        tagrows.append({'tag':tag,'paper':canon_owners.get(lab,''),'number':'','page':'','label':lab,
                        'status':' | '.join(sorted(statuses.get(lab,set()))),'kind':kind.get(lab,'reserved')})
    with (ROOT/'S6_SERIES_GRIND_tags.tsv').open('w',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=['tag','paper','number','page','label','status','kind'],delimiter='\t');writer.writeheader();writer.writerows(tagrows)
    for row in rows:row['tag']=labeltags[row['label']]['tag']
    with (ROOT/'S6_SERIES_GRIND_inventory.csv').open('w',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    print(json.dumps({'permanent_tags':len(registry),'label_aliases':len(labeltags),'printed_statements':sum(v=='statement' for v in kind.values()),'status_alias_disagreements':{k:sorted(v) for k,v in statuses.items() if len(v)>1}}))

if __name__=='__main__':main()
