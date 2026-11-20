"""Extract current main-outline statement targets, including the refuted environment."""
from pathlib import Path
import hashlib
import json
import re
A=Path(__file__).resolve().parents[1]
W=A.parent
m=json.loads((A/'frontmatter_II_map.json').read_text())
b=(W/'parts/II.body.tex').read_text()
labels=sorted(set(x for v in m['main_theorems'] for x in v['body_labels']+[t for s in v['steps'] for t in s['body_targets']]))
parts=[]
out=[]
for lab in labels:
    pos=b.index('\\label{'+lab+'}')
    starts=list(re.finditer(r'\\begin\{(theorem|proposition|lemma|corollary|problem|remark|refuted)\}',b[:pos]))
    match=starts[-1]
    env=match.group(1)
    end=b.index('\\end{'+env+'}',pos)+len('\\end{'+env+'}')
    txt=b[match.start():end]
    assert len(txt.splitlines())<200,(lab,len(txt.splitlines()))
    parts.append('\n% TARGET '+lab+'\n'+txt)
    out.append({'label':lab,'source_start_line':b[:match.start()].count('\n')+1,'source_end_line':b[:end].count('\n')+1,'statement':txt,'sha256':hashlib.sha256(txt.encode()).hexdigest()})
(A/'II_main_current_statements_06.tex').write_text('\n'.join(parts))
(A/'II_main_current_statements_06.json').write_text(json.dumps({'source_body_sha256':hashlib.sha256(b.encode()).hexdigest(),'records':out},indent=2)+'\n')
print(json.dumps({'targets':len(out),'lines':sum(x.count('\n') for x in parts)}))
