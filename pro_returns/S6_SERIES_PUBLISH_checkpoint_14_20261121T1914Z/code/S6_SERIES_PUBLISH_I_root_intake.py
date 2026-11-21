#!/usr/bin/env python3
"""Extract only target statements for derivation before target-proof reading."""
from pathlib import Path
import datetime, hashlib, json, re

ROOT = Path(__file__).resolve().parents[1]
source = ROOT.parent / 'source/S6_SERIES_GRIND_I.tex'
s = source.read_text()
envs = r'maintheorem|theorem|lemma|proposition|corollary|definition|remark|cited|computed|statement|auditrecord|test|refuted|openq|problem|question|conjecture|claim|example'
heads = list(re.finditer(r'\\begin\{('+envs+r')\}',s))
targets = ['ari:C.1.1','ari:C.1.2','inv:A1.1','inv:A2.3','inv:A4.2','inv:C1.2','inv:D1.2','inv:D4.2']
rows = []
for label in targets:
    pos = s.index('\\label{'+label+'}')
    h = [m for m in heads if m.start() < pos][-1]
    end = s.index('\\end{'+h[1]+'}',pos)+len('\\end{'+h[1]+'}')
    rows.append({'label':label,'environment':h[1],'source_line':s.count('\n',0,h.start())+1,
                 'statement':s[h.start():end], 'statement_sha256':hashlib.sha256(s[h.start():end].encode()).hexdigest()})
out = {'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
       'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
       'scope':'Target statements only. No target proof is included in this extraction.', 'targets':rows}
dest=ROOT/'records/S6_SERIES_PUBLISH_I_root_statement_intake.json'
dest.write_text(json.dumps(out,indent=2)+'\n')
for row in rows:
    print('\n'+row['label']+' — '+row['environment']+'\n'+row['statement'])
