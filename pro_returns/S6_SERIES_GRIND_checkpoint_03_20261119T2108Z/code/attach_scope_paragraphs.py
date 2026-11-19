"""Attach inherited unnumbered scope discussion to its exact preceding result."""
from pathlib import Path
import re,json
R=Path(__file__).resolve().parents[1];p=R/'parts/IV.body.linked.tex';s=p.read_text();changes=[]
for m in list(re.finditer(r'\\begin\{remark\}\[([^]]+)\](.*?)\\end\{remark\}',s,re.S))[::-1]:
 if '\\StatementRecord' in m.group():continue
 prefix=s[:m.start()];prior=re.findall(r'\\StatementRecord\{([^}]+)\}',prefix)[-1]
 body=m.group(2).strip()
 # The exact earlier check provenance is retained in the source and receipt.
 oldprose='Independent\nreferees and exact arithmetic checks are validation, not\nadditional mathematical methods.'
 body=body.replace(oldprose,'')
 new='\\paragraph{'+m.group(1)+' (\\ref{'+prior+'}).}\n'+body+'\n'
 changes.append({'preceding_statement':prior,'old':m.group(),'new':new,'reason':'Keep this explanatory scope passage with its receiving mathematical result; it carries no separate theorem or independent check status.'})
 s=s[:m.start()]+new+s[m.end():]
p.write_text(s);q=R/'analysis/scope_paragraph_receipt.json'
if changes:q.write_text(json.dumps(changes[::-1],indent=2))
print(json.dumps({'scope_passages_attached':len(changes)}))
