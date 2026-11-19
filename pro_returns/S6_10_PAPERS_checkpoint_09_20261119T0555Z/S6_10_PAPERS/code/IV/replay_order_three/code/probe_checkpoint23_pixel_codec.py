"""Compare exact PNG transport layouts without changing any original image."""
from pathlib import Path
import hashlib,json,lzma,sys,time
from checkpoint_png_codec import encode,decode
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parent
manifest=json.loads((BASE/'checkpoint23_base22/checkpoint23_base22_manifest.json').read_text())
items=sorted(manifest['pngs'],key=lambda x:x['bytes'],reverse=True)
rows=[]
for item in items[:3]+items[-2:]:
 p=BASE/'checkpoint22_encoding/frozen'/item['target'];data=p.read_bytes();t=time.monotonic()
 a=encode(data);b=encode(data,pixels=True)
 ca=lzma.compress(a,preset=3);cb=lzma.compress(b,preset=3)
 assert decode(b)==data
 row={'name':item['target'],'original_bytes':len(data),'filtered_xz':len(ca),'pixels_xz':len(cb),'seconds':round(time.monotonic()-t,1)}
 rows.append(row);print(json.dumps(row),flush=True)
(ROOT/'records/checkpoint23_pixel_codec_probe.json').write_text(json.dumps({'status':'PASS','cases':rows},indent=2)+'\n')
