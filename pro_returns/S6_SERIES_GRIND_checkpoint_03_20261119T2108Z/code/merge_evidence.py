"""Merge received evidence with exact event provenance and no new check credit."""
from pathlib import Path
import csv,hashlib,json,re
from collections import Counter,defaultdict
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parent/'S6_SERIES_GRIND_source'
CP=BASE/'S6_GRIND_1_papers_cp15'
csv.field_size_limit(10**9)
FIELDS=['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group']

def read(path,sep='\t'):
    with path.open() as f:return list(csv.DictReader(f,delimiter=sep))

def main():
    inventory=read(ROOT/'S6_SERIES_GRIND_inventory.csv',',')
    bysource=defaultdict(set)
    known={r['label'] for r in inventory}
    for row in inventory:bysource[(row['source_run'],row['source_id'])].add(row['label'])
    events=read(CP/'CHECK_EVENTS.tsv')
    for n,e in enumerate(events,2):
        e.update(source_file='S6_GRIND_1_papers_cp15/CHECK_EVENTS.tsv',source_row=str(n),source_event_type=e['type'],evidence_group=e['event_id'])
    receipt=[];unmatched=[]
    files=['S6_10_INTAKE_CHECK_EVENTS.tsv','INTAKE_S6_06_BLIND_cp36_20261119_CHECK_EVENTS.tsv','sweep1_s6/CHECK_EVENTS.tsv']
    # This map changes only the ledger's controlled-vocabulary field. The
    # original type remains in source_event_type, so the transport is lossless.
    typemap={'computation':'computation or formal certificate','used and rechecked':'used and rechecked in this run',
             'targeted proof check and source comparison':'targeted proof check',
             'targeted proof comparison with scoped dependencies':'targeted proof check',
             'correction':'targeted proof check'}
    for filename in files:
        path=BASE/'S6_GRIND_2_checks_and_plan'/filename
        for number,raw in enumerate(read(path),2):
            sid=raw.get('statement_id',raw.get('statement tag',''))
            candidates=[]
            if sid in known:candidates=[sid]
            elif sid.startswith('S6_') and ':' in sid:
                run,identifier=sid.split(':',1)
                candidates=sorted(bysource.get((run,identifier),set()))
                if not candidates and run=='S6_06_BLIND':candidates=['night:'+identifier]
            else:
                ids=re.findall(r'\bP[1-5][A-Z]?(?:K|F|R)?\.\d+\b',sid)
                candidates=['night:'+x for x in dict.fromkeys(ids)]
            if not candidates:
                candidates=['series:night-intake-cp36' if 'all 299 rows' in sid else sid]
                unmatched.append({'source_file':filename,'source_row':number,'statement_id':sid})
            payload=json.dumps(raw,sort_keys=True,ensure_ascii=False)
            group='received:'+hashlib.sha256((filename+'\n'+str(number)+'\n'+payload).encode()).hexdigest()[:20]
            for label in candidates:
                eid='ce:'+hashlib.sha256((group+'\n'+label).encode()).hexdigest()[:20]
                outcome=raw['outcome']
                locator=raw.get('where',raw.get('what was read',''))
                if locator:outcome+=' [Received locator: '+locator+']'
                events.append({'statement_id':label,'date':raw.get('date',raw.get('date_utc','')),'who':raw['who'],
                    'type':typemap.get(raw['type'],raw['type']),'outcome':outcome,'event_id':eid,'phase':'received',
                    'source_file':'S6_GRIND_2_checks_and_plan/'+filename,'source_row':str(number),
                    'source_event_type':raw['type'],'evidence_group':group})
            receipt.append({'source_file':filename,'source_row':number,'original_statement_id':sid,'resolved_labels':candidates,'evidence_group':group})
    # Agent events are imported only from explicit TSV event files, with raw data retained.
    agent_files=[]
    for folder in sorted(ROOT.glob('audit_*')):
        for path in sorted(p for p in folder.rglob('*.tsv') if 'events' in p.name.lower()):
            if path.name.endswith('received_events.tsv'):continue
            agent_files.append(path)
    for path in agent_files:
        for number,raw in enumerate(read(path),2):
            if not raw.get('statement_id'):continue
            payload=json.dumps(raw,sort_keys=True,ensure_ascii=False)
            eid=raw.get('event_id') or 'ce:'+hashlib.sha256((str(path.relative_to(ROOT))+payload).encode()).hexdigest()[:20]
            events.append({'statement_id':raw['statement_id'],'date':raw.get('date',raw.get('date_utc','2026-11-19')),
                'who':raw.get('who','GPT-6 Astra (OpenAI), ChatGPT Pro mode, S6_SERIES_GRIND'),
                'type':typemap.get(raw.get('type',''),raw.get('type','')),'outcome':raw.get('outcome',''),
                'event_id':eid,'phase':'S6_SERIES_GRIND','source_file':str(path.relative_to(ROOT)),
                'source_row':str(number),'source_event_type':raw.get('type',''),'evidence_group':raw.get('evidence_group',eid)})
    # Preserve an event identity exactly once; distinct alias placements share evidence_group.
    unique={}
    for event in events:
        key=event['event_id']
        if key in unique and unique[key]!=event:raise ValueError('conflicting event id '+key)
        unique[key]=event
    events=list(unique.values())
    with (ROOT/'CHECK_EVENTS.tsv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=FIELDS,delimiter='\t',extrasaction='ignore');writer.writeheader();writer.writerows(events)
    (ROOT/'analysis/evidence_imports.json').write_text(json.dumps({'receipts':receipt,'unmatched':unmatched,'agent_files':[str(p.relative_to(ROOT)) for p in agent_files]},indent=2))
    result={'received_base_events':len(read(CP/'CHECK_EVENTS.tsv')),'attached_new_event_rows':len(receipt),
            'combined_event_rows':len(events),'evidence_groups':len({e['evidence_group'] for e in events}),
            'type_counts':dict(Counter(e['type'] for e in events)),'unmatched':unmatched}
    (ROOT/'code/outputs/evidence_merge.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result))

if __name__=='__main__':main()
