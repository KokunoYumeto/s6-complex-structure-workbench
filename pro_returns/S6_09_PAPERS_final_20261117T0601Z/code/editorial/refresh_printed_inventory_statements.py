"""Refresh only the literal printed-statement field after the common pass.

No historical check, proof outcome, credit classification or result identity is
changed. The source-to-print proof audits are separate evidence.
"""
from pathlib import Path
import csv,json,re,bisect,hashlib
D=Path(__file__).resolve().parents[2]
p=D/'S6_09_PAPERS_inventory.csv'
with p.open(newline='') as f:rd=csv.DictReader(f);fields=rd.fieldnames;rows=list(rd)
assert len(fields)==17
changes=[]
for paper in ['I','II','III']:
    text=(D/f'S6_09_PAPERS_{paper}.tex').read_text()
    ranges=[];stack=[]
    envs='theorem|proposition|lemma|corollary|claim|statement|remark|question|problem|conjecture|definition|example|computed|test'
    for t in re.finditer(r'\\(begin|end)\{('+envs+r')\}',text):
        if t[1]=='begin':stack.append((t[2],t.start()))
        elif stack and stack[-1][0]==t[2]:
            env,start=stack.pop();ranges.append((start,t.end(),env))
    ranges.sort();starts=[r[0] for r in ranges]
    labels={m[1]:m.start() for m in re.finditer(r'\\label\{([^}]+)\}',text)}
    for r in rows:
        if r['paper']!=paper:continue
        key=r['printed_label'];assert key in labels,(paper,key)
        pos=labels[key];i=bisect.bisect_right(starts,pos)-1
        if i>=0 and pos<ranges[i][1]:
            start,end,_=ranges[i];actual=text[start:end]
        else:
            tail=text[pos:];m=re.search(r'\n\\(?:sub)*section\*?(?:\[[^\]]*\])?\{',tail)
            assert m,(paper,key,'No complete next unit boundary')
            actual=tail[:m.start()]
        if actual!=r['statement_as_printed']:
            before=r['statement_as_printed']
            changes.append({'source_run':r['source_run'],'source_id':r['source_id'],
                'paper':paper,'printed_label':key,'before':before,'after':actual,
                'before_sha256':hashlib.sha256(before.encode()).hexdigest(),
                'after_sha256':hashlib.sha256(actual.encode()).hexdigest(),
                'reason':'The canonical standalone paper after the final common-reference and exact source-locator pass controls the literal printed field; the complete proof/wording transforms remain separately recorded.'})
            r['statement_as_printed']=actual
            note='Final literal printed field refreshed from the actual complete labelled statement/unit; see records/common_printed_statement_refresh.json. Proof outcomes and historical events unchanged.'
            if note not in r['wording_vs_source']:r['wording_vs_source']=(r['wording_vs_source']+' | '+note).strip(' |')
with p.open('w',newline='') as f:wr=csv.DictWriter(f,fields);wr.writeheader();wr.writerows(rows)
out=D/'records/common_printed_statement_refresh.json'
record={'rows':len(rows),'fields':fields,'changed_rows':len(changes),'changes':changes,
        'proof_outcomes_changed':False,'historical_events_changed':False}
if out.exists():record['previous_events']=json.loads(out.read_text()).get('previous_events',[])+[json.loads(out.read_text())['changes']]
if changes or not out.exists():out.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'rows':len(rows),'literal_fields_refreshed':len(changes)}))
