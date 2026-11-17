#!/usr/bin/env python3
"""Log a permitted source read and retain the exact displayed excerpt."""
from pathlib import Path
from datetime import datetime,timezone
import argparse
p=argparse.ArgumentParser()
p.add_argument('source');p.add_argument('--start',type=int,default=1)
p.add_argument('--end',type=int);p.add_argument('--reason',required=True)
a=p.parse_args();root=Path(__file__).resolve().parents[2]
now=datetime.now(timezone.utc);src=(root/a.source).resolve()
with (root/'records/literature_fourfold.md').open('a') as f:
 f.write('\n- '+now.isoformat()+' — Opened `'+str(src)+'`; reason: '+a.reason+'; material: displayed lines '+str(a.start)+'–'+str(a.end or 'end')+'.\n')
lines=src.read_text().splitlines();end=a.end or len(lines)
out='\n'.join(f'{i+1}: {lines[i]}' for i in range(a.start-1,min(end,len(lines))))+'\n'
dest=root/'code/part3_fourfold/reads';dest.mkdir(exist_ok=True)
(dest/(now.strftime('%Y%m%dT%H%M%S%f')+'_'+src.name+'.out')).write_text(out)
print(out,end='')
