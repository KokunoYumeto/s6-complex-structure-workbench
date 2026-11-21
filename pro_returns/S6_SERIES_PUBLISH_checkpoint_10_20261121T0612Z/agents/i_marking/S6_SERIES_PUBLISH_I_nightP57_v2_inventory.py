#!/usr/bin/env python3
"""New documentary inventory: scan TeX environment boundaries after removing comments.
This inventories printed statement environments and relevant whole-source contexts;
it does not infer mathematical nonexistence from keyword absence.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,re,hashlib
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
SOURCE=Path('/workspace/scratch/653608133b22/source/S6_GRIND_6_literature/papers/arXiv_2610.00250v2_Du_Guo_Kusakabe_Xie_src/submited-tams.tex')
raw=SOURCE.read_text()
chars=list(raw);i=0
while i<len(chars):
    if chars[i]=='%':
        j=i-1;slashes=0
        while j>=0 and chars[j]=='\\':slashes+=1;j-=1
        if slashes%2==0:
            j=raw.find('\n',i)
            if j<0:j=len(chars)
            for k in range(i,j):chars[k]=' '
            i=j;continue
    i+=1
clean=''.join(chars)
end=clean.find(r'\end{document}')
assert end>=0
clean=clean[:end+len(r'\end{document}')]
statement_envs={'theorem','proposition','lemma','corollary','definition','remark'}
stack=[];blocks=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',clean):
    kind,env=m.groups()
    if kind=='begin':stack.append((env,m.start()))
    else:
        assert stack and stack[-1][0]==env, (m.start(),env,stack[-1:] )
        name,start=stack.pop()
        if name in statement_envs:
            body=clean[start:m.end()]
            labels=re.findall(r'\\label\{([^}]+)\}',body)
            blocks.append({'environment':name,'source_start_line':raw[:start].count('\n')+1,'source_end_line':raw[:m.end()].count('\n')+1,'labels':labels,'text':body})
assert not stack
blocks.sort(key=lambda x:x['source_start_line'])
patterns={
'kuranishi':r'Kuranishi',
'miniversality':r'miniversal|miniversality',
'cohomology':r'cohomolog',
'full_automorphisms':r'\\(?:operatorname|mathrm|text)\{Aut\}|\\Aut|automorphism',
'exact_period_syntax':r'2\s*\\(?:Z|mathbb\{Z\})|biholomorph|isomorph.*paramet|paramet.*isomorph',
'hodge_dimensions':r'h\s*\^\s*(?:\{[0-3]\}|[0-3])|T_X|T_\{X',
'deformations':r'deformation',
}
contexts={}
for name,pattern in patterns.items():
    hits=[]
    for m in re.finditer(pattern,clean,re.I):
        a=clean.rfind('\n',0,max(0,m.start()-220))+1
        b=clean.find('\n',min(len(clean),m.end()+220))
        if b<0:b=len(clean)
        hits.append({'line':raw[:m.start()].count('\n')+1,'matched':m.group(0),'context':clean[a:b]})
    contexts[name]=hits
report={'created_utc':datetime.now(timezone.utc).isoformat(),'source':str(SOURCE),'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'method':'Exact environment-boundary scan after replacing unescaped-percent comments by spaces, preserving source offsets. All six declared mathematical statement environments inventoried. Whole-source concept contexts supplied for manual review.','statement_environment_count':len(blocks),'environment_counts':{e:sum(x['environment']==e for x in blocks) for e in sorted(statement_envs)},'statements':blocks,'whole_source_concept_contexts':contexts,'limitations':'Inventory and context review establish which assertions are printed in this supplied version. This does not make a claim that no mathematical relationship exists, or independently check the proofs of the printed statements.'}
(OUT/'S6_SERIES_PUBLISH_I_nightP57_v2_inventory.json').write_text(json.dumps(report,indent=2)+'\n')
text=[]
for b in blocks:text.append(f"SOURCE LINES {b['source_start_line']}–{b['source_end_line']} [{b['environment']}] "+','.join(b['labels'])+'\n'+b['text']+'\n')
(OUT/'S6_SERIES_PUBLISH_I_nightP57_v2_statement_inventory.txt').write_text('\n'.join(text))
print(json.dumps({'statement_environment_count':len(blocks),'environment_counts':report['environment_counts'],'concept_hit_counts':{k:len(v) for k,v in contexts.items()}},indent=2))
