#!/usr/bin/env python3
"""Reversible layout repair for one nested optional proof heading."""
from pathlib import Path
import hashlib,json,datetime
ROOT=Path(__file__).resolve().parents[2]
old=r'\begin{proof}[Supplied source argument; continuation review in progress][Complete original-source attachment and directed physical transfer]\mbox{}\par'
new=(r'\begin{proof}[Supplied source argument; continuation review in progress]\mbox{}\par'+'\n'
     +r'\noindent\textbf{Complete original-source attachment and directed physical transfer.}\par\smallskip')
changes=[]
for rel in ['papers/IV/body.tex','papers/IV/body_source.tex','papers/IV/continuation_night36.tex']:
 p=ROOT/rel;s=p.read_text()
 if old not in s:
  assert new in s,rel
  continue
 assert s.count(old)==1,rel
 t=s.replace(old,new)
 changes.append({'path':rel,'before_sha256':hashlib.sha256(s.encode()).hexdigest(),'after_sha256':hashlib.sha256(t.encode()).hexdigest(),'old':old,'new':new})
 p.write_text(t)
receipt=ROOT/'analysis/continuation_IV/proof_heading_layout_patch.json'
if changes:receipt.write_text(json.dumps({'patched_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reason':'One3.91232pt overflow was caused by a second bracketed proof title appended after the receiving optional title. The original source title is retained as its own breakable bold paragraph.','mathematical_text_changed':False,'changes':changes},indent=2)+'\n')
print(json.dumps({'files_changed':len(changes),'receipt':str(receipt)}))
