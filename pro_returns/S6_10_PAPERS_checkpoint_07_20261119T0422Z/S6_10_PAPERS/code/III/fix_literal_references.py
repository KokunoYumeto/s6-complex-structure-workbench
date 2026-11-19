"""Replace manually compared legacy statement locators in generated Paper III.

The legacy counters are used only after the inventory owner compared each target
statement with the actual calling text. No proof-check credit is created.
"""
from pathlib import Path
import re,json
B=Path(__file__).resolve().parents[2]
M=json.loads((B/'analysis/inventory_legacy_numbers.json').read_text())
CONFIRMED={'I:17.1','I:17.2','I:17.3','I:17.4','I:20.12','I:20.2','I:20.3','I:20.4','I:23.1','I:23.2','I:23.4','I:23.5','I:3.4','I:4.5','I:4.8','I:5.5','I:B.2','I:B.6','I:B.9','I:C.1','I:D.6','I:H.1','II:16.32','II:16.33','II:16.34'}
log=[]
for p in (B/'papers/III').glob('*.tex'):
 s=p.read_text()
 def replace(m):
  key=m[1]+':'+m[2]
  if key not in CONFIRMED: return m[0]
  label=M[key]['label'];log.append({'file':p.name,'old':m[0],'label':label,'source_file':M[key]['file'],'source_line':M[key]['source_line'],'scope':'Original target statement compared to the actual calling formula or assertion; this changes only the locator.'})
  return r'\cref{'+label+'}'
 s=re.sub(r'Paper~([IV]+), (?:Proposition|Theorem|Lemma|Corollary)~([A-Z0-9]+\.[0-9]+)',replace,s)
 # Both range endpoints are explicit source labels from the same local chain.
 def range_replace(m):
  full=m[1];pref,n=full.rsplit('.',1);end=pref+'.'+m[2]
  return r'\ref{'+full+'}--'+r'\ref{'+end+'}'
 s=re.sub(r'\\ref\{((?:maps:src:)[A-Z]\.\d+\.\d+)\}--(\d+)',range_replace,s)
 # The source replay files shipped in this paper have a paper-specific path.
 def codepath(m):
  name=m[1]
  return r'\path{code/III/'+name+'}' if (B/'code/III'/name).exists() else m[0]
 s=re.sub(r'\\path\{code/([^{}]+)\}',codepath,s)
 if p.name=='06_collision.tex':
  a=s.find(r'\begin{split}'+'\n (VHV^{-1},VT^3V^{-1},-V)')
  if a>=0:
   z=s.find(r'\end{split}',a)+len(r'\end{split}')
   t=s[a:z].replace(r'\begin{split}',r'\begin{aligned}').replace(r'\end{split}',r'\end{aligned}')
   t=t.replace('\n (VHV^{-1}', '\n &(VHV^{-1}').replace('\n (BCB^{-1}', '\n &(BCB^{-1}')
   t=t.replace('\n &=\\left(', '\\\\[-1pt]\n &\\quad=\\left(')
   s=s[:a]+t+s[z:]
 p.write_text(s)
(B/'analysis/III_literal_reference_reconciliation.json').write_text(json.dumps(log,indent=2)+'\n')
print('Replaced',len(log),'verified legacy locators; source-range endpoints and existing code paths updated.')
