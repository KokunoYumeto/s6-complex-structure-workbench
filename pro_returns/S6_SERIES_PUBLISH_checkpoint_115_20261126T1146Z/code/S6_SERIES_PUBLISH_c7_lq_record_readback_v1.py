#!/usr/bin/env python3
"""Read every proposed LQ field; bodies refer bijectively to wholly read texts."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import csv,json,re

ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/'agents/continuation7_iii_star_logs_receiving'
P='S6_SERIES_PUBLISH_III_02LQ_'
def digest(path):
    return sha256(path.read_bytes()).hexdigest()
def env(text,name):
    start=text.index('\\begin{'+name+'}')
    end=text.index('\\end{'+name+'}',start)+len('\\end{'+name+'}')
    return text[start:end]
def output(kind,value):
    print(kind,json.dumps(value,ensure_ascii=False,sort_keys=True))
data={}
for kind,count in [('replacements',3),('defects',49),('CHECK_EVENTS',3)]:
    path=LANE/(P+kind+'.tsv')
    with path.open(newline='') as f:
        data[kind]=list(csv.DictReader(f,delimiter='\t'))
    assert len(data[kind])==count
    assert b'\r' not in path.read_bytes()
    output('FILE',{'name':path.name,'rows':count,'sha256':digest(path)})
receiver=(LANE/(P+'receiving.tex')).read_text()
old={}
for kind in ('statement','proof','following_auxiliary'):
    text=(LANE/(P+'released_'+kind+'.tex')).read_text()
    old[kind]=(env(text,'theorem' if kind=='statement' else 'proof')
               if kind!='following_auxiliary' else text.rstrip('\n'))
for kind,row in zip(old,data['replacements']):
    after=env(receiver,'theorem' if kind=='statement' else 'proof') if kind!='following_auxiliary' else ''
    assert row['old_text']==old[kind] and row['new_text']==after
    shown={k:v for k,v in row.items() if k not in ('old_text','new_text')}
    for field,value in [('old_text',old[kind]),('new_text',after)]:
        shown[field]={'exact_equality_to_wholly_read_body':kind,
                      'side':'released body' if field=='old_text' else 'receiver body or empty deletion',
                      'lines':len(value.splitlines()),'sha256_without_terminal_LF':sha256(value.encode()).hexdigest()}
    output('REPLACEMENT',shown)
for row in data['defects']:
    assert any(body.count(row['old_text'])==1 for body in old.values())
    assert receiver.count(row['new_text'])==1
    output('DEFECT',row)
paths=sorted({path for row in data['CHECK_EVENTS'] for path in row['where'].split('; ')})
indices={path:i+1 for i,path in enumerate(paths)}
for path in paths:
    assert (ROOT/path).exists(),path
    output('EVIDENCE_PATH',{'index':indices[path],'path':path})
for row in data['CHECK_EVENTS']:
    shown=dict(row)
    shown['where']={'exact_ordered_path_indices':[indices[path] for path in row['where'].split('; ')]}
    reconstructed='; '.join(paths[i-1] for i in shown['where']['exact_ordered_path_indices'])
    assert reconstructed==row['where']
    output('EVENT',shown)
assert digest(ROOT/'S6_SERIES_PUBLISH_III.tex')=='9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
output('PASS',{'scope':'All non-body fields printed exactly; replacement bodies equal the already wholly read source/receiver bodies; event where fields use the displayed reversible path dictionary.',
              'canonical_unchanged':True,'completed_utc':datetime.now(timezone.utc).isoformat()})
