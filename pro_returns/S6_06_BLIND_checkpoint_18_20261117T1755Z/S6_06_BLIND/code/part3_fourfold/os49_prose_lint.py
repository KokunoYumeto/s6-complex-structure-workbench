#!/usr/bin/env python3
"""Locate math tokens left in prose in the K65 working source."""
from pathlib import Path
import re,json
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'notes/part3_os49_corrected_returns_working.md';s=p.read_text()
masked=re.sub(r'\\\([\s\S]*?\\\)|\\\[[\s\S]*?\\\]',lambda m:'\n'*m.group(0).count('\n'),s)
issues=[dict(line=i,text=line) for i,line in enumerate(masked.splitlines(),1) if '_' in line]
(ROOT/'code/part3_fourfold/os49_prose_lint.json').write_text(json.dumps(issues,indent=2)+'\n')
print(json.dumps(issues,indent=2))
