#!/usr/bin/env python3
"""Read-only proof-body lexical census for a bounded editorial audit.

Matches locate candidates; they do not certify defects or proof readings.
No canonical source is changed.
"""
from pathlib import Path
import hashlib
import json
import re

root=Path(__file__).resolve().parents[1]
paper=root/'S6_SERIES_PUBLISH_II.tex'
text=paper.read_text()
headers=list(re.finditer(r'\\begin\{(theorem|proposition|lemma|corollary|definition|remark|example)\}[^\n]*',text))
proofs=list(re.finditer(r'\\begin\{proof\}.*?\\end\{proof\}',text,re.S))
hard=re.compile(r'\.py\b|\.json(?:l)?\b|\.out\b|code/|SHA[- ]?256|\bsaved output\b|\bexecuted independent\b|\b(?:the|attached) program\b',re.I)
raw=re.compile(r'(?<![A-Za-z0-9:{])P[1-4](?:[A-Z]|R)?\.\d+(?:\.\d+)?\b|\bsupplied correction note\b|\b(?:night run|worker|S6_[0-9A-Z_]+)\b')
rows=[]
for i,proof in enumerate(proofs):
    previous=[h for h in headers if h.start()<proof.start()]
    header=previous[-1].group(0) if previous else ''
    labels=re.findall(r'\\label\{([^}]+)\}',header)
    tag=re.search(r'\\hypertarget\{tag-([^}]+)\}',header)
    body=proof.group(0)
    hits=[]
    for kind,pattern in [('D09_candidate',hard),('D04_candidate',raw)]:
        for m in pattern.finditer(body):
            line_start=body.rfind('\n',0,m.start())+1
            line_end=body.find('\n',m.end())
            if line_end<0:line_end=len(body)
            hits.append({'kind':kind,'proof_offset':m.start(),
                'source_line':text.count('\n',0,proof.start()+m.start())+1,
                'match':m.group(0),'line':body[line_start:line_end]})
    if hits:
        rows.append({'proof_number':i+1,'owner':labels[0] if labels else None,
           'tag':tag.group(1) if tag else None,
           'start':proof.start(),'end':proof.end(),
           'start_line':text.count('\n',0,proof.start())+1,
           'proof_bytes':len(body.encode()),
           'proof_sha256':hashlib.sha256(body.encode()).hexdigest(),'hits':hits})
data={'source':str(paper.relative_to(root)),
      'source_sha256':hashlib.sha256(text.encode()).hexdigest(),
      'scope':'Lexical proof-body candidate census only; every hit still requires complete owning-proof reading and exact disposition.',
      'proof_count':len(proofs),'candidate_proofs':len(rows),
      'D09_candidate_proofs':sum(any(h['kind']=='D09_candidate' for h in r['hits']) for r in rows),
      'D09_hits':sum(h['kind']=='D09_candidate' for r in rows for h in r['hits']),
      'D04_hits':sum(h['kind']=='D04_candidate' for r in rows for h in r['hits']),
      'rows':rows,'canonical_mutations':0}
out=root/'agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_D09_D04_census_01.json'
out.write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps({k:v for k,v in data.items() if k!='rows'},indent=2))
for r in rows:
    dh=[h for h in r['hits'] if h['kind']=='D09_candidate']
    if dh:
        print(json.dumps({'owner':r['owner'],'tag':r['tag'],'proof_bytes':r['proof_bytes'],
                          'line':r['start_line'],'D09_hits':len(dh),
                          'D04_hits':len(r['hits'])-len(dh),
                          'examples':[h['line'] for h in dh[:2]]}))
