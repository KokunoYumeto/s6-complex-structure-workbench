from pathlib import Path
import re,json
r=Path(__file__).resolve().parents[1];s=(r/'S6_SERIES_PUBLISH_I.tex').read_text()
def strip_macro(t,name,n):
 while True:
  m=re.search(r'\\'+name+r'\{',t)
  if not m:return t
  j=m.end()-1
  for _ in range(n):
   while t[j].isspace():j+=1
   assert t[j]=='{';j+=1;level=1
   while level:
    if t[j]=='{' and t[j-1]!='\\':level+=1
    elif t[j]=='}' and t[j-1]!='\\':level-=1
    j+=1
  t=t[:m.start()]+t[j:]
lo=s.index('\\section{The marked family and its coordinates}')
hi=s.index('\\part{Results not yet established}',lo)
starts=list(re.finditer(r'\\begin\{(?:theorem|proposition|lemma|corollary|definition|remark|maintheorem|cited|computed)\}',s))
rows=[]
for m in re.finditer(r'\\end\{proof\}',s[lo:hi]):
 a=lo+m.end();nxt=next((x.start() for x in starts if x.start()>a),hi);seg=s[a:nxt];probe=seg
 for name,n in [('Uses',1),('UsedBy',1),('StatementRecord',4)]:probe=strip_macro(probe,name,n)
 for pattern in [r'(?m)^\s*%[^\n]*',r'\\(?:clearpage|newpage|medskip|smallskip|bigskip)\b',r'\\hypertarget\{[^}]*\}\{\}',r'\\label\{[^}]*\}',r'\\(?:part|section|subsection|subsubsection)\*?\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}']:
  probe=re.sub(pattern,'',probe)
 if probe.strip():
  prior=re.findall(r'\\label\{([^}]+)\}',s[lo:a]);post=re.search(r'\\label\{([^}]+)\}',s[nxt:])
  rows.append({'line':s[:a].count('\n')+1,'previous':prior[-1] if prior else '', 'next':post[1] if post else '', 'text':seg,'visible':probe})
(r/'records/S6_SERIES_PUBLISH_I_orphan_candidates.json').write_text(json.dumps(rows,indent=2)+'\n')
print('candidates',len(rows))
for x in rows:print(x['line'],x['previous'],x['next'],x['visible'][:260].replace('\n',' '))
