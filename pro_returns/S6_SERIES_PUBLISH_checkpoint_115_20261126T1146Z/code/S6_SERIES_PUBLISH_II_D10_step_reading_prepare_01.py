#!/usr/bin/env python3
"""Extract six complete proof pairs for removal of repeated first-item markers."""
from pathlib import Path
import datetime as dt,hashlib,json,re
R=Path(__file__).resolve().parents[1];O=R/'records/S6_SERIES_PUBLISH_II_D10_step_reading_01'
assert not O.exists();s=(R/'S6_SERIES_PUBLISH_II.tex').read_text()
sha=lambda x:hashlib.sha256(x.encode() if isinstance(x,str) else x).hexdigest()
pat=r'\\item\s*(?:\\noindent\s*)?\\textbf\{Step\s*1\.\}'
hits=list(re.finditer(pat,s));assert len(hits)==6
rows=[];O.mkdir()
for i,m in enumerate(hits,1):
 a=list(re.finditer(r'\\begin\{(proposition|lemma|theorem|corollary|remark|example)\}',s[:m.start()]))[-1].start()
 z=s.index(r'\end{proof}',m.end())+len(r'\end{proof}');old=s[a:z]
 assert old.count(r'\item')==1
 new=re.sub(pat,lambda _:r'\item',old)
 new=new.replace(r'label={$\langle1\rangle$\arabic*.}',r'label=\arabic*.')
 owner=re.search(r'\\StatementRecord\{([^}]+)',old)[1]
 names={}
 for kind,text in [('before',old),('after',new)]:
  p=O/f'proof_{i:02d}_{kind}.tex';p.write_text(text);names[kind]=dict(path=str(p.relative_to(R)),bytes=len(text.encode()),sha256=sha(text))
 rows.append(dict(owner=owner,**names,proof_items=1,mathematical_text_map='Delete the duplicate bold Step1 label immediately after the first and only item, and remove its depth1 prefix. Every remaining byte is identical.'))
d=dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),source_sha256=sha(s),proof_pairs=rows,canonical_mutations=0,reading_credit='Preparation only. Full root display and reading must follow before admission.')
(O/'index.json').write_text(json.dumps(d,indent=2)+'\n')
print(json.dumps(d,indent=2))
