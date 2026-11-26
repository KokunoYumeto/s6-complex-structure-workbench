#!/usr/bin/env python3
"""Freeze only the current remaining section10 statement/proof units."""
from pathlib import Path
root=Path(__file__).resolve().parents[1]
text=(root/'S6_SERIES_PUBLISH_II.tex').read_text()
out=root/'agents/continuation3_conductor'
for n in (52,54,56,58,59,60,61,62,63):
 p=text.index(r'\label{cdp:st:C.2.UN.'+str(n)+'}')
 a=text.rfind(r'\begin{proposition}',0,p)
 b=text.index(r'\end{proof}',p)+len(r'\end{proof}')
 block=text[a:b]
 path=out/f'S6_SERIES_PUBLISH_c3_conductor_tail_UN{n}_input.tex'
 if path.exists():assert path.read_text()==block,n
 else:path.write_text(block,newline='\n')
 print(f'UN{n}: {len(block.splitlines())} lines; complete input frozen, no central write.')
