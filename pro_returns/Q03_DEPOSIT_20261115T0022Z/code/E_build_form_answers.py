#!/usr/bin/env python3
"""Produce deposit form answers from the current post and its exact record.

The abstract body is copied verbatim. Provenance/Declarations undergo only the
explicit TeX-to-text transformations below. No publication or network action.
Run: python3 code/E_build_form_answers.py > code/E_build_form_answers_output.json
"""
from pathlib import Path
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parents[1]
post=(ROOT/'Q03_DEPOSIT_post.tex').read_text()
record=json.loads((ROOT/'work/record.json').read_text())
raw=post.split('%%% POST-RECORD v1 BEGIN\n',1)[1].split('%%% POST-RECORD v1 END',1)[0]
record_text='\n'.join(line[2:] for line in raw.splitlines() if line.startswith('% '))
from_post={}
for line in record_text.splitlines():
    key,value=line.split(': ',1)
    from_post[key]=json.loads(value)
assert from_post==record,'Post record and work/record.json differ.'
abstract=re.search(r'\\begin\{abstract\}\s*([\s\S]*?)\s*\\end\{abstract\}',post).group(1)
provenance_tex=post.split(r'\fixedhead{Provenance}',1)[1].split(r'\begin{thebibliography}',1)[0]
provenance_tex=r'\fixedhead{Provenance}'+provenance_tex


def prose_from_tex(s):
    # These transformations cover only the concrete prose macros occurring in
    # the extracted Provenance/Declarations. They retain every prose word.
    s='\n'.join(line for line in s.splitlines() if not line.lstrip().startswith('%'))
    s=s.replace(r'\allowbreak ','').replace(r'\allowbreak','')
    s=s.replace(r'\LaTeX{}','LaTeX').replace(r'\LaTeX','LaTeX')
    s=re.sub(r'\\fixedhead\{([^{}]*)\}',r'\n\1\n',s)
    s=re.sub(r'\\begin\{itemize\}(?:\[[^\]]*\])?','',s)
    s=s.replace(r'\end{itemize}','')
    s=s.replace(r'\item','\n- ')
    for cmd in ('path','texttt','textbf','emph'):
        s=re.sub(r'\\'+cmd+r'\{([^{}]*)\}',r'\1',s)
    s=re.sub(r'\\cite\[([^\]]*)\]\{([^{}]*)\}',lambda m:'['+m.group(2)+', '+m.group(1)+']',s)
    s=re.sub(r'\\cite\{([^{}]*)\}',lambda m:'['+m.group(1)+']',s)
    s=s.replace(r'\_', '_').replace(r'\&','&').replace(r'\%','%')
    s=s.replace('---','—').replace('--','–').replace('~',' ')
    # Collapse source line wraps within each bullet, retaining paragraph order.
    s=re.sub(r'(?<!\n)\n(?!\n|- |Provenance|Declarations)',' ',s)
    s=re.sub(r'[ \t]+',' ',s)
    s=re.sub(r'\n[ \t]+','\n',s)
    s=re.sub(r'\n{3,}','\n\n',s).strip()
    assert not re.search(r'\\[A-Za-z]+',s),'Unconverted prose macro.'
    return s

provenance=prose_from_tex(provenance_tex)
hexagon=record['hexagon']
limits={'title':(len(record['title']),240),'abstract':(len(abstract),8000),
        'provenance_statement':(len(provenance),12000),'comments':(len(hexagon['comments']),2000),
        'cross_lists':(len(hexagon['cross_lists']),8),'msc':(len(hexagon['msc']),5),
        'tags':(len(hexagon['tags']),12),'tools':(len(hexagon['tools']),10)}
assert all(n<=limit for n,limit in limits.values())
assert 1<=len(hexagon['msc'])<=5
assert record['human_understanding']=='none'
assert record['text_origin']=='primarily AI-generated'
assert record['licence']=='CC0-1.0'
assert any(x.get('role')=='deposit-task author' and x.get('model')=='Claude Opus 5.5' and x.get('effort')=='max' for x in record['produced_by'])
assert 'Present audit request: Claude Opus 5.5, effort max.' in provenance

lines=[
'# Q03_DEPOSIT — deposit form answers', '',
'Date: '+record['date']+'. Record: '+record['record_id']+'. Version: '+str(record['version'])+'.','',
'These answers are prepared for the user’s review. No remote publication or form submission has been performed. The contributor enters their identity and approves the deposit after reviewing the PDF, record, and answers.','',
'## Title','', '```text',record['title'],'```','',
'## Abstract','',
'The following block is the exact abstract body from the current LaTeX source, including its mathematical notation. Copy it unchanged.','',
'```text',abstract,'```','',
'## Classification and disclosure fields','',
'| Form field | Answer |','|---|---|',
'| Primary subject | '+hexagon['subject']+' |',
'| Cross-lists | '+', '.join(hexagon['cross_lists'])+' |',
'| MSC codes | '+', '.join(hexagon['msc'])+' |',
'| Text origin | '+record['text_origin']+' (`no-human-author-claimed`) |',
'| Human understanding | '+record['human_understanding']+' |',
'| Formalizations | Leave the links field empty. '+record['formalization']+'. |',
'| Licence | CC0 1.0 (`'+record['licence']+'`) |',
'| Contributor | Entered by the human contributor at deposit. |','',
'## Tags','',
]+['- '+x for x in hexagon['tags']]+['','## Tools','']+['- '+x for x in hexagon['tools']]+[
'','## Provenance statement','',
'The following text reproduces the post’s Provenance and Declarations sections, with prose formatting and reference labels rendered as plain text.','',
'```text',provenance,'```','',
'## Comments','', '```text',hexagon['comments'],'```','',
'## Supplementary files','',
'The requested delivery is one ZIP. Its ancillary files for the deposit are:','',
'- `'+record['provenance']['prompt']+'` — supplied original prompt, preserved verbatim.',
'- `'+record['provenance']['current_request']+'` — the present audit request.',
'- `'+record['provenance']['return']+'` — supplied proof return.',
]+['- `'+x+'` — supplied referee report.' for x in record['provenance']['reports']]+[
'- `code/` — reproducible audit and verification programs, with their outputs.',
'- `Q03_DEPOSIT_report.md`, `Q03_DEPOSIT_results.csv`, `Q03_DEPOSIT_sources.md`, and `Q03_DEPOSIT_literature.md` — the current mathematical, computational, source, and literature records.','',
'Public repository status, exactly as recorded: '+record['provenance']['repository']+'.','',
'## Model and effort provenance by role','',
'| Role | Model or tool | Effort / execution setting | Date |',
'|---|---|---|---|',
]
for item in record['produced_by']:
    lines.append('| '+item['role']+' | '+item.get('model',item.get('tool',''))+' | '+item.get('effort','software version as listed')+' | '+item['date']+' |')
for item in record['checks']:
    lines.append('| Prior report '+item['id']+' | '+item['by']+' | '+item['effort']+' | '+item['date']+' |')
lines += ['','The prior question and the present audit request have separate effort records. The supplied reports record the Message Batches API mode; no API mode is assigned to the present request’s author beyond the supplied metadata.','',
'## Recorded status and qualifications','',
'- Kind: '+record['kind']+'.',
'- Claim: '+record['claim_status']+'.',
'- External results: '+record['external_results']+'.',
'- Current check: '+record['checks_of_this_text'][0]['type']+'; '+record['checks_of_this_text'][0]['by']+', '+record['checks_of_this_text'][0]['effort']+'; '+record['checks_of_this_text'][0]['date']+'; '+record['checks_of_this_text'][0]['verdict']+'.','',
'### Open points / retained qualifications','',
]+['- '+x for x in record['open_points']]+['','### Not claimed','']+['- '+x for x in record['not_claimed']]+[
'','### Literature record','',
'- Date: '+record['literature_search']['date']+'.',
'- Scope: '+record['literature_search']['scope']+'.',
'- Outcome: '+record['literature_search']['outcome']+'.',
'','## Form-limit checks','',
'| Field | Characters or entries | Limit |','|---|---:|---:|',
]+[f'| {key} | {n} | {limit} |' for key,(n,limit) in limits.items()]+[
'','## Machine-readable record','',
'The following is the post’s complete opening record, with only the LaTeX comment prefixes removed. Its values are identical to `work/record.json`.','',
'```yaml',record_text,'```','']
answer='\n'.join(lines)
assert abstract in answer
assert provenance in answer
for item in hexagon['tools']:assert '- '+item in answer
(ROOT/'Q03_DEPOSIT_form_answers.md').write_text(answer)
print(json.dumps({'date':record['date'],'record_id':record['record_id'],'version':record['version'],
 'source_post_sha256':hashlib.sha256(post.encode()).hexdigest(),
 'source_record_sha256':hashlib.sha256((ROOT/'work/record.json').read_bytes()).hexdigest(),
 'abstract_sha256':hashlib.sha256(abstract.encode()).hexdigest(),
 'abstract_copied_verbatim':True,'post_record_matches_record_file':True,
 'limits':{k:{'actual':n,'maximum':lim,'passed':n<=lim} for k,(n,lim) in limits.items()},
 'provenance_roles_checked':True,'output_file':'Q03_DEPOSIT_form_answers.md',
 'output_sha256':hashlib.sha256(answer.encode()).hexdigest(),
 'remote_publication_performed':False,'verdict':'All form content and limit checks passed.'},indent=2))
