#!/usr/bin/env python3
"""Freeze exact tree inputs and complete shared owners; no central writes."""
from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
out=root/'agents/continuation3_conductor'
stem='S6_SERIES_PUBLISH_c3_conductor_18'
s=(root/'S6_SERIES_PUBLISH_II.tex').read_text()
def block(label):
 p=s.index(r'\label{'+label+'}')
 starts=list(re.finditer(r'\\begin\{(?:proposition|lemma|theorem|definition|corollary)\}',s[:p]))
 a=starts[-1].start();b=s.index(r'\end{proof}',p)+len(r'\end{proof}');return s[a:b]
owners={**{f'UN{n}':f'cdp:st:C.2.UN.{n}' for n in (17,54,58,60,61,62,63,80,83)},
 'P306':'lem:II:identity-monodromy-elliptic','P350':'def:II:elliptic-star-data',
 'P351':'lem:II:elliptic-star-boundary','P337':'lem:II:hopf-curve-restriction'}
for key,label in owners.items():
 v=block(label);p=out/(stem+'_'+key+'_input.tex')
 if p.exists():assert p.read_text()==v,key
 else:p.write_text(v,newline='\n')
 print(key,len(v.splitlines()),len(v))
