"""Extract cited input statements, without their proofs or main outlines."""
from pathlib import Path
import re,json,hashlib,sys,datetime
B=Path(__file__).parent;p=Path('/workspace/scratch/653608133b22/work/S6_SERIES_PUBLISH_I.tex');s=p.read_text()
intake=json.loads((B/'S6_SERIES_PUBLISH_I_global_ABC_statement_intake.json').read_text())
starts=list(re.finditer(r'\\begin\{(maintheorem|theorem|proposition|corollary|lemma|definition|remark|cited)\}',s))
def extract(label):
 i=s.index(r'\label{'+label+'}');m=max((m for m in starts if m.start()<i),key=lambda m:m.start())
 end=r'\end{'+m.group(1)+'}';e=s.index(end,m.end())+len(end)
 assert i<e,label
 text=s[m.start():e];assert r'\begin{proof}' not in text,label
 return {'label':label,'line_start':s.count('\n',0,m.start())+1,'line_end':s.count('\n',0,e)+1,'text':text}
rows={}
for main in intake['statements']:
 for label in main['cited_labels']:
  if label not in rows:rows[label]=extract(label)
for label in ['I:def:family-parameter','I:def:theta-height']:
 rows[label]=extract(label)
out={'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'extracted_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'inputs':rows}
(B/'S6_SERIES_PUBLISH_I_global_ABC_inputs.json').write_text(json.dumps(out,indent=2)+'\n')
which=sys.argv[1] if len(sys.argv)>1 else 'A'
labels=next(x['cited_labels'] for x in intake['statements'] if x['label']=='series:I:'+which)
if which=='A':labels=['I:def:family-parameter','I:def:theta-height']+labels
for label in labels:print('INPUT',label);print(rows[label]['text'])
