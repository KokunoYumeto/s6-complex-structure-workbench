#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[2]
with (ROOT/'records/literature_fourfold.md').open('a') as f:
 f.write('\n- '+datetime.now(timezone.utc).isoformat()+' — Opened own K37 witness source, promoted note and promotion script. Reason: repair JavaScript string escaping in the newly added witness section after standalone TeX detected it. Material: unchanged exact mathematical witnesses, literal preserved LaTeX backslashes.\n')
witness=(ROOT/'code/part3_fourfold/os49_shorter_loop_witnesses.md').read_text()
note=ROOT/'notes/part3_os49_shorter_loop_working.md'
source=note.read_text().split('## 7.',1)[0].rstrip()+'\n\n'+witness
note.write_text(source)
promotion=ROOT/'code/part3_fourfold/promote_os49_shorter_loop.py'
p=promotion.read_text()
start=p.index("text += r'''")
end=p.index("(ROOT/rel).write_text(text)",start)
p=p[:start]+"text = text.split('## 7.',1)[0].rstrip()+'\\n\\n'+(ROOT/'code/part3_fourfold/os49_shorter_loop_witnesses.md').read_text()\n"+p[end:]
promotion.write_text(p)
print('Repaired witness escaping in source and reproducible promotion script.')
