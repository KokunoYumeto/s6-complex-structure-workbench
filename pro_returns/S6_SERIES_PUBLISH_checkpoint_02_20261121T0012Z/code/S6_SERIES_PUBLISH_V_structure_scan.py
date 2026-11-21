#!/usr/bin/env python3
"""List orphan-prose candidates; this is a locator, never a page-reading claim."""
from pathlib import Path
import re,json
R=Path(__file__).resolve().parents[1];s=(R/'S6_SERIES_PUBLISH_V.tex').read_text();lo=s.index('\\part{The marked rank-six');hi=s.index('\\begin{thebibliography}')
starts=list(re.finditer(r'\\begin\{(?:theorem|proposition|lemma|corollary|definition|remark|maintheorem|cited|computed)\}',s))
rows=[]
for m in re.finditer(r'\\end\{proof\}',s[lo:hi]):
 a=lo+m.end(); nxt=next((x.start() for x in starts if x.start()>a),hi)
 seg=s[a:nxt];probe=seg
 for pattern in [r'(?m)^\s*%[^\n]*',r'\\(?:clearpage|newpage|medskip|smallskip|bigskip)\b',r'\\hypertarget\{[^}]*\}\{\}',r'\\label\{[^}]*\}',r'\\(?:part|section|subsection|subsubsection)\*?\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}']:
  probe=re.sub(pattern,'',probe)
 if probe.strip():
  prior=re.findall(r'\\label\{([^}]+)\}',s[lo:a]);post=re.search(r'\\label\{([^}]+)\}',s[nxt:])
  rows.append({'line':s[:a].count('\n')+1,'previous':prior[-1] if prior else '', 'next':post[1] if post else '', 'text':seg})
(R/'records/S6_SERIES_PUBLISH_V_orphan_candidates.json').write_text(json.dumps(rows,indent=2)+'\n')
print('candidates',len(rows))
for r in rows:print(r['line'],r['previous'],r['next'],r['text'][:1600].replace('\n',' '))
