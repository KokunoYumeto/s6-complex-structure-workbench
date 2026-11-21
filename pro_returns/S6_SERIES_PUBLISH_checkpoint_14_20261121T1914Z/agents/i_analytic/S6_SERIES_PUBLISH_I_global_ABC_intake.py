"""Freeze the three current main statements before detailed outline review."""
from pathlib import Path
import re,json,hashlib,datetime
B=Path(__file__).parent;p=Path('/workspace/scratch/653608133b22/work/S6_SERIES_PUBLISH_I.tex');s=p.read_text()
rows=[]
for label in ['series:I:A','series:I:B','series:I:C']:
 i=s.index(r'\label{'+label+'}');a=s.rfind(r'\begin{maintheorem}',0,i);b=s.index(r'\end{maintheorem}',i)+len(r'\end{maintheorem}')
 text=s[a:b]
 deps=sorted(set(z.strip() for m in re.findall(r'\\(?:SeriesRef|cref|Cref|ref|eqref)\{([^}]+)\}',text) for z in m.split(',') if z.strip()!=label))
 rows.append({'label':label,'line_start':s.count('\n',0,a)+1,'line_end':s.count('\n',0,b)+1,'text':text,'cited_labels':deps})
j={'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source':str(p),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
 'method':'Statement-directed global comparison with extensive disclosed prior related-proof exposure. No blind reproof claim. Detailed current outlines and literature-status table not yet opened for this comparison.',
 'statements':rows}
(B/'S6_SERIES_PUBLISH_I_global_ABC_statement_intake.json').write_text(json.dumps(j,indent=2)+'\n')
for x in rows:
 print('MAIN STATEMENT',x['label']);print(x['text']);print('INPUT_LABELS',x['cited_labels'])
