#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timezone
import json
root=Path(__file__).resolve().parents[2]
src=root/'code/part3/source_zero_regular_fan_2_1_6.json'
with (root/'records/literature_fourfold.md').open('a') as f:
 f.write('\n- '+datetime.now(timezone.utc).isoformat()+' — Opened '
         +str(src.relative_to(root))+'. Reason: exact physical-delta fixed-stratum '
         'computation on the supplied audited regular fan. Material: schema, '
         'primitive rays, cone and face-period data; no external source used.\n')
d=json.loads(src.read_text())
def shape(x):
 if isinstance(x,dict): return {'type':'dict','keys':list(x)}
 if isinstance(x,list): return {'type':'list','length':len(x),'first':shape(x[0]) if x else None}
 return x
out={k:shape(v) for k,v in d.items()}
print(json.dumps(out,indent=2))
(root/'code/part3_fourfold/source_zero_fan_schema.json').write_text(json.dumps(out,indent=2)+'\n')
for k,v in d.items():
 if isinstance(v,list) and v and isinstance(v[0],dict):
  print('SAMPLE',k,json.dumps(v[0],indent=2)[:18000])
 if isinstance(v,dict):
  for kk,vv in v.items():
   if isinstance(vv,list) and vv and isinstance(vv[0],dict):
    print('SAMPLE',k,kk,json.dumps(vv[0],indent=2)[:18000])
