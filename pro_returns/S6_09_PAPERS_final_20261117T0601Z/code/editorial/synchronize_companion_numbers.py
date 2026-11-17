"""Give the Paper I overview exact numbered companion destinations.

This is the final common-reference pass, not a change in mathematical claims.
"""
from pathlib import Path
import re,json,hashlib
D=Path(__file__).resolve().parents[2]
refs={}
for paper in ['I','II','III']:
    p=D/f'S6_09_PAPERS_{paper}.aux';s=p.read_text()
    numbers=dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]*)\}',s))
    kinds=dict(re.findall(r'\\newlabel\{([^}]+)@cref\}\{\{\[([^\]]+)\]',s))
    refs[paper]={'numbers':numbers,'kinds':kinds,'aux_sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def number(p,key):
    assert key in refs[p]['numbers'],(p,key)
    return refs[p]['numbers'][key]
long_form=(r'Paper~II, Proposition~'+number('II','cdp:st:A.1.1')+
     r' and Propositions~'+number('II','cdp:st:C4a')+', '+number('II','cdp:st:C4c')+
     ' and '+number('II','cdp:st:C4f')+r', gives the general analysis and replacement vanishing criteria. '+
     r'Paper~III, Theorems~'+number('III','maps:src:B.2.1')+' and '+number('III','maps:src:F.4.1')+
     r' and Corollary~'+number('III','push:src:C.3.27')+
     ', gives the map, framing and manifold results.')
new=(r'Paper~II, Propositions~'+number('II','cdp:st:A.1.1')+' and '+number('II','cdp:st:C4a')+
     r', gives the general analysis and replacement criteria; Paper~III, Theorems~'+
     number('III','maps:src:B.2.1')+' and '+number('III','maps:src:F.4.1')+
     r' and Corollary~'+number('III','push:src:C.3.27')+
     ', gives the map, framing and manifold results.')
old=r'''Paper~II gives the general
analysis and the replacement vanishing criteria; Paper~III gives the map,
framing and manifold results.'''
manifest=[]
for p in [D/'S6_09_PAPERS_I.tex',D/'editorial/I_front.tex']:
    if not p.exists():continue
    s=p.read_text()
    prior=next((x for x in [old,long_form] if x in s),None)
    if prior:
        assert s.count(prior)==1
        before=hashlib.sha256(s.encode()).hexdigest();s=s.replace(prior,new)
        p.write_text(s);manifest.append({'file':str(p.relative_to(D)),'before':prior,'after':new,
            'before_sha256':before,'after_sha256':hashlib.sha256(s.encode()).hexdigest()})
    elif new not in s:raise AssertionError(('Companion overview pattern changed',p))
record={'reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro),17November2026,/root',
 'scope':'Concrete numbered destinations in the introductory comparison; proof text unchanged',
 'targets':{'II':{k:refs['II']['numbers'][k] for k in ['cdp:st:A.1.1','cdp:st:C4a','cdp:st:C4c','cdp:st:C4f']},
            'III':{k:refs['III']['numbers'][k] for k in ['maps:src:B.2.1','maps:src:F.4.1','push:src:C.3.27']}},
 'changes':manifest}
out=D/'records/common_numbered_companion_overview.json'
if out.exists():record['previous_events']=json.loads(out.read_text()).get('previous_events',[])+[json.loads(out.read_text())['changes']]
if manifest or not out.exists():out.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(record['targets']))
