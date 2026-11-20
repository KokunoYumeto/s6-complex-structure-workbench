from pathlib import Path
import re, sys
base=Path(__file__).resolve().parents[3]/'S6_SERIES_GRIND_source'/'S6_GRIND_1_papers_cp15'
for label in sys.argv[1:]:
 for p in base.glob('S6_10_PAPERS_*.tex'):
  s=p.read_text(); pos=s.find('\\label{'+label+'}')
  if pos<0: continue
  start=s.rfind('\\begin{',0,pos)
  m=re.search(r'\\end\{(theorem|proposition|lemma|corollary|cited|problem|remark|statement|test|definition)\}',s[pos:])
  end=pos+m.end() if m else pos+5000
  print('SOURCE',p.name,'LABEL',label,'LINES',s.count('\n',0,start)+1,s.count('\n',0,end)+1)
  chunk=s[start:end]
  while '\\StatementRecord' in chunk:
   i=chunk.index('\\StatementRecord'); j=i+len('\\StatementRecord')
   for _ in range(4):
    while chunk[j].isspace():j+=1
    assert chunk[j]=='{'; d=1; j+=1
    while d:
     if chunk[j]=='{' and chunk[j-1]!='\\':d+=1
     if chunk[j]=='}' and chunk[j-1]!='\\':d-=1
     j+=1
   chunk=chunk[:i]+chunk[j:]
  print(chunk); print()
