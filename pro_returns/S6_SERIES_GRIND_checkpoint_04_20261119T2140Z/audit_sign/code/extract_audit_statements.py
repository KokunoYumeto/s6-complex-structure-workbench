from pathlib import Path
import re,json,hashlib
ROOT=Path(__file__).resolve().parents[3]
SRC=ROOT/'S6_SERIES_GRIND_source/S6_GRIND_1_papers_cp15'
OUT=Path(__file__).resolve().parents[1]

def braced(s,p):
 assert s[p]=='{'
 depth=1;i=p+1
 while depth:
  if s[i]=='{' and (i==0 or s[i-1]!='\\'):depth+=1
  if s[i]=='}' and (i==0 or s[i-1]!='\\'):depth-=1
  i+=1
 return s[p+1:i-1],i

def strip_record(s):
 pos=s.find('\\StatementRecord')
 if pos<0:return s
 i=pos+len('\\StatementRecord')
 for _ in range(4):
  while s[i].isspace():i+=1
  a,i=braced(s,i)
 return s[:pos]+s[i:]

out=[]
for paper in ['II','VI']:
 source=SRC/f'S6_10_PAPERS_{paper}.tex';s=source.read_text()
 for m in re.finditer(r'\\begin\{(proposition|theorem|lemma|corollary|refuted)\}[^\n]*\\label\{([^}]+)\}',s):
  label=m[2]
  if not (label.startswith('cdp:st:C.2.UN.') or label in ['cdp:st:D.2.5','ii:LR:covering','night:P3K.36','stmt:P3K.36']):continue
  end=s.index('\\end{'+m[1]+'}',m.end())+len('\\end{'+m[1]+'}')
  statement=strip_record(s[m.start():end])
  q=s.find('\\begin{proof}',end)
  e=s.find('\\end{proof}',q)+len('\\end{proof}')
  proof=s[q:e] if q>=0 else ''
  out.append({'paper':paper,'label':label,'line':s[:m.start()].count('\n')+1,'statement':statement,'proof':proof,'source':str(source.relative_to(ROOT))})
(OUT/'statements_only.txt').write_text('\n\n'.join(f'=== {o["paper"]}:{o["label"]} line {o["line"]} ===\n{o["statement"]}' for o in out))
(OUT/'blocks.json').write_text(json.dumps(out,indent=2))
print(f'Extracted {len(out)} statements; statement-only file excludes recorded prior proof checks and printed proofs.')
