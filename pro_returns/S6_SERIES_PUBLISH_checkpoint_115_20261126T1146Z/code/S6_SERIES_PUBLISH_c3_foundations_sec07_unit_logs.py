from S6_SERIES_PUBLISH_c3_foundations_sec07_helpers import *
from datetime import datetime, timezone

def write_unit_logs(name,unit,title,review,readings,specific,comparison,guard_count,new_tags='none'):
    prefix='S6_SERIES_PUBLISH_sec07_'+name
    path=OUT/(prefix+'_defects.tsv')
    with path.open(newline='') as f:
        rr=csv.DictReader(f,delimiter='\t');fields=rr.fieldnames;rows=list(rr)
    for r in rows:r['review_status']=review
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
    with (ROOT/'agents/continuation3_foundations/S6_SERIES_PUBLISH_foundations_CHECK_EVENTS.tsv').open(newline='') as f:
        ef=next(csv.reader(f,delimiter='\t'))
    now=datetime.now(timezone.utc).isoformat();events=[]
    for suffix,owner,outcome in readings:
        e=dict.fromkeys(ef,'');e.update(statement_id=owner,date=now[:10],
          who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 foundations',
          type='used and rechecked in this run',
          outcome=outcome+' Exposed reading and direct comparison only; no independent-check credit, required-check increment or integrated rendered-page reading.',
          event_id='publish:c3:foundations:sec07:'+name+':'+suffix,
          phase='publication complete '+title,
          source_file=str(path.relative_to(ROOT)),source_event_type='used and rechecked in this run',
          evidence_group='publish:c3:foundations:sec07:'+name,date_utc=now,
          where='Complete '+unit+' subsection and its explicitly bounded shared-owner guards')
        events.append(e)
    with (OUT/(prefix+'_CHECK_EVENTS.tsv')).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=ef,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(events)
    status=[]
    defaults={
      'D10':'Existing D10 closure stands; dependency records remain hidden.',
      'D14':'All local receiving premises precede their uses. Whole-paper placement remains with root.',
      'D16':'Existing D16 closure stands; every statement has a mathematical title.',
      'D23':'Full source/equation comparison done; integrated build and final page reading remain with root.',
      'D24':'Root must reconcile the final outline and contents; no global front-matter closure is claimed.',
      'restructuring':'The actual subsection is locally consolidated and guard-ready. Final whole-paper order and integration remain; bounded shared-owner applications are not counted as additional completed subsections.'
    }
    for kind in [f'D{i:02}' for i in range(1,26)]+['restructuring']:
        status.append(dict(unit=unit,row=kind,
          status='open' if kind in ['D14','D23','D24','restructuring'] else 'done',
          basis=specific.get(kind,defaults.get(kind,'Complete original/current and receiving subsection read for this class; no instance remains in this receiving text.')),
          fragment='agents/continuation3_foundations/sec07/S6_SERIES_PUBLISH_II_sec07_'+name+'.tex'))
    with (OUT/(prefix+'_unit_progress.tsv')).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['unit','row','status','basis','fragment'],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(status)
    lines=['# '+title+': status','',
      f'READY: complete original/current and receiving proofs compared; {guard_count} guards replay once with every old label and target retained. New tags: {new_tags}. Root admission pending.','',
      '| Class | Status | Basis |','|---|---|---|']
    lines += [f"| {r['row']} | {r['status']} | {r['basis']} |" for r in status]
    (OUT/(prefix+'_status.md')).write_text('\n'.join(lines)+'\n',newline='\n')
    (OUT/(prefix+'_comparison.md')).write_text(comparison,newline='\n')
    print(f'{name}: {len(rows)} defects; {len(events)} exposed events; {len(status)} actual-subsection rows; new tags {new_tags}.')
