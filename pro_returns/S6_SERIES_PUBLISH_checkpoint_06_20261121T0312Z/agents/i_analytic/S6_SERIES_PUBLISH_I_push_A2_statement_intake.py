"""Extract target/input statements only, never their following printed proofs."""
from pathlib import Path
import re,json,hashlib,datetime
B=Path(__file__).parent
p=Path('/workspace/scratch/653608133b22/source/S6_SERIES_GRIND_I.tex')
s=p.read_text()
environments='theorem|proposition|lemma|corollary|definition|remark|cited'
starts=list(re.finditer(r'\\begin\{('+environments+r')\}',s))
def extract(label):
 needle=r'\label{'+label+'}'
 assert s.count(needle)==1,(label,s.count(needle))
 i=s.index(needle)
 m=max((m for m in starts if m.start()<i),key=lambda x:x.start())
 endtoken=r'\end{'+m.group(1)+'}'
 e=s.index(endtoken,m.end())+len(endtoken)
 assert i<e,(label,'label does not lie in selected statement')
 text=s[m.start():e]
 assert r'\begin{proof}' not in text,(label,'unexpected proof inside statement')
 deps=sorted(set(re.findall(r'\\(?:SeriesRef|cref|Cref|ref)\{([^}]+)\}',text)))
 deps=[x for dep in deps for x in dep.split(',') if x!=label]
 return dict(label=label,environment=m.group(1),line_start=s.count('\n',0,m.start())+1,
  line_end=s.count('\n',0,e)+1,text=text,dependencies=deps)
targets=[extract(x) for x in ['push:src:A.2.1','push:src:A.2.2']]
out=dict(source=str(p),source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),
 extracted_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
 exposure='No recalled or recorded prior exposure to these target proofs. Earlier generic filename scans displayed isolated program-reference lines, not these targets\' printed proof steps; exact target spans will be compared with that output after derivation. Only statement text is emitted by this script.',targets=targets)
(B/'S6_SERIES_PUBLISH_I_push_A2_statement_intake.json').write_text(json.dumps(out,indent=2)+'\n')
for x in targets:
 print('TARGET',x['label'],'LINES',x['line_start'],x['line_end'])
 print(x['text'])
 print('INPUT_LABELS',x['dependencies'])
