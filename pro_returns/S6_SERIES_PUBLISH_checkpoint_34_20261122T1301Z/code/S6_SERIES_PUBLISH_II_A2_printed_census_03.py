#!/usr/bin/env python3
"""Read-only visible-text candidate census; no claim that every candidate is a defect."""
from bisect import bisect_right
from collections import Counter
from datetime import datetime, timezone
import hashlib, json, re
from pathlib import Path

R=Path(__file__).resolve().parents[1]
W=R/'agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_printed_census_03'
W.mkdir(exist_ok=True)
p=R/'S6_SERIES_PUBLISH_II.tex'; raw=p.read_bytes(); s=raw.decode()
sha=hashlib.sha256(raw).hexdigest()
start=s.index('\\begin{document}'); end=s.index('\\section*{Programs}')
masked=list(s); exclusions=[]
def mask(a,b,kind):
    exclusions.append({'kind':kind,'start':a,'end':b})
    for k in range(a,b):
        if masked[k]!='\n': masked[k]=' '
def group(a):
    while a<len(s) and s[a].isspace(): a+=1
    assert s[a]=='{',(a,s[a:a+100])
    depth=1; k=a+1
    while depth:
        if s[k]=='\\': k+=2; continue
        if s[k]=='{': depth+=1
        elif s[k]=='}': depth-=1
        k+=1
    return a,k
mask(0,start,'preamble_macro_definitions_and_series_table')
mask(end,len(s),'Programs_and_bibliography')
for m in re.finditer(r'(?<!\\)%[^\n]*',s): mask(m.start(),m.end(),'TeX_comment')
for m in re.finditer(r'\\begin\{comment\}.*?\\end\{comment\}|\\iffalse.*?\\fi\b',s,re.S):
    mask(m.start(),m.end(),'nonprinting_environment')
for m in re.finditer(r'\\StatementRecord\b',s):
    if not start<=m.start()<end: continue
    a=m.end()
    for j in range(4): a,b=group(a); a=b
    mask(m.start(),b,'StatementRecord_four_arguments_only_tag_prints')
for m in re.finditer(r'\\(?:label|ref|cref|Cref|eqref|pageref|autoref|nameref|cite|citep|citet|SeriesRef|SeriesRefText|tag)\b\*?(?:\[[^\]]*\])?',s):
    if not start<=m.start()<end: continue
    try: a,b=group(m.end())
    except (AssertionError,IndexError): continue
    kind='equation_tag_reserved_D19' if m.group().startswith('\\tag') else 'reference_or_label_argument'
    mask(a,b,kind)
for m in re.finditer(r'\\(?:href|hyperlink|hypertarget)\b',s):
    if not start<=m.start()<end: continue
    try:a,b=group(m.end())
    except (AssertionError,IndexError):continue
    mask(a,b,'nonprinting_link_target')
for m in re.finditer(r'\\hyperref\[([^\]]*)\]',s):
    if start<=m.start()<end: mask(m.start(1),m.end(1),'nonprinting_hyperref_optional_target')
v=''.join(masked)
proofs=list(re.finditer(r'\\begin\{proof\}.*?\\end\{proof\}',s,re.S))
headers=list(re.finditer(r'\\begin\{(?:maintheorem|theorem|proposition|lemma|corollary|definition|remark|example|cited|refuted|computed|openq)\}[^\n]*',s))
heads=[]
for i,h in enumerate(headers):
    stop=headers[i+1].start() if i+1<len(headers) else end
    label=re.search(r'\\label\{([^}]+)\}',s[h.start():min(stop,h.end()+1200)])
    tag=re.search(r'\\hypertarget\{tag-([^}]+)\}',s[h.start():min(stop,h.end()+1500)])
    heads.append({'start':h.start(),'end':stop,'owner':label.group(1) if label else None,'tag':tag.group(1) if tag else None})
headpos=[x['start'] for x in heads]
paras=[]
for m in re.finditer(r'\S(?:.*?\S)?(?=\n\s*\n|\Z)',s,re.S):
    if m.start()<start or m.start()>=end:continue
    paras.append((m.start(),m.end()))
ppos=[x[0] for x in paras]
patterns={
 'D09_filename_or_program':r'\.(?:py|jsonl?|out|csv|tsv|md|tex|pdf)\b|\bcode/|SHA[- ]?256|\b(?:script|program|programs|saved output|recorded output|computer[- ]assisted|symbolic check|computational check|machine check|certificate file)\b',
 'D04_raw_run_reference':r'(?<![A-Za-z0-9:{])P[1-4](?:[A-Z]|R)?\.\d+(?:\.\d+)?\b|\b(?:inv|night|maps|push|ari|cdp):|\bsupplied correction note\b|\b(?:C\.2\.(?:UN|NC)\.\d+|NC\.\d+)\b',
 'D05_prompt_reference':r'\b(?:the prompt|requested|asked for|Lead\s+\d+|as required by|(?-i:Parts?[\s~]+[A-E0-9][A-Za-z0-9.]*)|F\.[234](?:\.\d+)*)\b',
 'D06_external_numbering':r'\bcompendium\b|\\CompendiumRef\{[^}]+\}\{[^}]+\}|\[S6[_\\]|\b(?:B\.5\.\d+|E\.2\.\d+)\b',
 'D07_run_or_worker':r'\b(?:worker|workers|independently authored|night run|this run|SERIES[_\\]GRIND|S6(?:\\?_)[0-9][A-Za-z0-9_\\]*)\b',
}
rows={}; allmatches=[]
for kind,pat in patterns.items():
    for m in re.finditer(pat,v,re.I):
        k=bisect_right(ppos,m.start())-1
        if k<0:continue
        a,b=paras[k]
        if not a<=m.start()<b: raise AssertionError((m.start(),a,b))
        h=heads[bisect_right(headpos,m.start())-1] if headpos and headpos[0]<=m.start() else {}
        pr=next((p for p in proofs if p.start()<=m.start()<p.end()),None)
        rec=rows.setdefault((a,b),{'id':f'PAR-{s.count(chr(10),0,a)+1:05d}','source_character_span':[a,b],
            'source_line_span':[s.count('\n',0,a)+1,s.count('\n',0,b)+1],
            'owner':h.get('owner'),'tag':h.get('tag'),'inside_proof':bool(pr),
            'owner_proof_bytes':len(pr.group().encode()) if pr else None,
            'source_paragraph':s[a:b],'masked_paragraph':v[a:b],'matches':[]})
        mr={'kind':kind,'text':m.group(),'character_span':[m.start(),m.end()]}
        rec['matches'].append(mr);allmatches.append(mr)
result={'created_utc':datetime.now(timezone.utc).isoformat(),'source_sha256':sha,
 'scope':'Document body before Programs. Candidates are paragraph-scoped after explicit nonprinting-argument masks; manual context disposition is separate. All equation-tag conversion belongs to root D19.',
 'canonical_mutations':0,'exclusion_kind_counts':dict(Counter(x['kind'] for x in exclusions)),
 'candidate_match_counts':dict(Counter(x['kind'] for x in allmatches)),
 'candidate_paragraph_count':len(rows),'candidate_owner_count':len({x['owner'] for x in rows.values()}),
 'rows':sorted(rows.values(),key=lambda x:x['source_character_span'][0])}
(W/'S6_SERIES_PUBLISH_II_A2_printed_candidates_03.json').write_text(json.dumps(result,indent=2)+'\n')
assert p.read_bytes()==raw
print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
for r in result['rows']:
    print(r['id'],r['owner'],r['tag'],'proof' if r['inside_proof'] else 'outside',
          ','.join(sorted({m['kind'][:3] for m in r['matches']})),
          repr(' | '.join(m['text'] for m in r['matches'])))
