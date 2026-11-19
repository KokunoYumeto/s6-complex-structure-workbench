"""Repack only the newest checkpoint22 bundle with exact PNG restoration.

All checkpoint22 research bytes are immutable. This prepares a transport base,
not a research snapshot. Earlier complete bundles are reused unchanged.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, io, lzma, tarfile, time, zipfile
from checkpoint_png_codec import encode, decode

ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT.parent
OUT=BASE/'checkpoint23_base22'; OUT.mkdir(exist_ok=False)
SOURCE=BASE/'checkpoint22_encoding/lossless_reencoding/checkpoint22_reencoded_artifacts.tar.xz'
TARGET=OUT/'checkpoint23_base22_artifacts.tar.xz'
with zipfile.ZipFile(BASE/'S6_06_BLIND_checkpoint_22.zip') as z:
    manifest=json.loads(z.read('checkpoint22_transport_manifest.json'))
    restore=z.read('restore_checkpoint.py').decode()
def sha(p):
    with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
assert sha(SOURCE)==manifest['bundles'][-1]['sha256']
pngs=[]; started=time.monotonic(); count=0
with lzma.open(TARGET,'xb',filters=[{'id':lzma.FILTER_LZMA2,'preset':3,'dict_size':64*1024*1024}]) as xz:
    with tarfile.open(fileobj=xz,mode='w|',format=tarfile.PAX_FORMAT) as sink:
        with tarfile.open(SOURCE,'r|xz') as source:
            for member in source:
                assert member.isfile(),member.name
                item=tarfile.TarInfo(member.name);item.size=member.size;item.mode=0o644;item.mtime=0
                stream=source.extractfile(member)
                if member.name.endswith('.png'):
                    data=stream.read();encoded=encode(data)
                    if encoded is not None:
                        packed=member.name+'.pngcodec'
                        item.name=packed;item.size=len(encoded);stream=io.BytesIO(encoded)
                        pngs.append({'target':member.name,'encoded':packed,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
                    else:stream=io.BytesIO(data)
                with stream:sink.addfile(item,stream)
                count+=1
                if count%100==0:print(json.dumps({'packed':count,'file':member.name,'pngs':len(pngs),'seconds':round(time.monotonic()-started,1),'partial_bytes':TARGET.stat().st_size}),flush=True)
manifest['bundles'][-1]={'file':TARGET.name,'sha256':sha(TARGET)}
manifest['pngs']=pngs
restore=restore.replace('from checkpoint_copy_add import decode','from checkpoint_copy_add import decode\nfrom checkpoint_png_codec import decode as decode_png')
needle=" for item in m['copies']:\n  source_name="
replacement=""" for item in m.get('pngs',[]):
  source=target(stage,item['encoded']);out=target(stage,item['target'])
  out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(decode_png(source.read_bytes()))
  assert out.stat().st_size==item['bytes'] and sha(out)==item['sha256']
 for item in m['copies']:
  source_name="""
assert needle in restore;restore=restore.replace(needle,replacement)
restore=restore.replace("m=json.loads((base/'checkpoint22_transport_manifest.json').read_text())","m=json.loads((base/'checkpoint23_base22_manifest.json').read_text())")
compile(restore,'restore_base22.py','exec')
(OUT/'restore_base22.py').write_text(restore)
(OUT/'checkpoint23_base22_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
result={'status':'COMPLETE','utc':datetime.now(timezone.utc).isoformat(),'bytes':TARGET.stat().st_size,'sha256':sha(TARGET),'pngs':len(pngs),'members':count,'seconds':round(time.monotonic()-started,1),'source_sha256':sha(SOURCE),'exact_png_roundtrips':len(pngs)}
(ROOT/'records/checkpoint23_base22_preparation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2),flush=True)
