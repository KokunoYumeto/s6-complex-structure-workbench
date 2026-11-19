"""Extract statements before any proof is exposed to the reviewer.
A code-generated extraction is not a proof check. The source is preserved.
"""
from pathlib import Path
import re,json,hashlib
ROOT=Path(__file__).resolve().parents[2]
s=(ROOT/'papers/VI/body.tex').read_text()
starts=list(re.finditer(r'\\begin\{(proposition|theorem|lemma|corollary|refuted|cited|computed|openq)\}',s))
units=[]
for i,m in enumerate(starts):
 end=s.find(r'\end{'+m[1]+'}',m.end())+len(r'\end{'+m[1]+'}')
 statement=s[m.start():end]
 label=re.search(r'\\label\{([^}]+)\}',statement)
 if not label: continue
 nextstart=starts[i+1].start() if i+1<len(starts) else len(s)
 after=s[end:nextstart]
 pm=re.search(r'\\begin\{proof\}',after)
 proof=after[pm.start():] if pm else ''
 units.append(dict(label=label[1],statement=statement,proof=proof,start=m.start(),end=end,nextstart=nextstart,statement_sha256=hashlib.sha256(statement.encode()).hexdigest(),proof_sha256=hashlib.sha256(proof.encode()).hexdigest()))
a=ROOT/'analysis/continuation_VI'; a.mkdir(parents=True,exist_ok=True)
(a/'review_units.json').write_text(json.dumps(units,indent=2))
(a/'statements_only.tex').write_text('\n\n'.join(u['statement'] for u in units))
print('Extracted',len(units),'statements. Proofs are held separately and not emitted.')
print('\n'.join(f"{i+1}\t{u['label']}\t{len(u['statement'])}\t{len(u['proof'])}" for i,u in enumerate(units)))
