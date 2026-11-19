"""Prepare a lossless deduplicated base for the next standalone full snapshot.

Each packed member is identified by the bytes actually read. The final hourly
builder compares its current file hash before reusing any such member. Work can
therefore continue while this compression-only preparation runs.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,io,json,lzma,re,tarfile,time

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parent
target=BASE/'checkpoint22_base_artifacts.tar.xz'
partial=target.with_suffix('.xz.partial')
manifest=BASE/'checkpoint22_base_manifest.json'
assert not target.exists() and not partial.exists() and not manifest.exists()

def excluded(rel):
    source=any(rel.startswith(x) for x in ('records/primary_sources/','records/external_source_cache/','records/sources/','records/part5_comparison/'))
    return (source and Path(rel).suffix.lower() in ('.pdf','.txt','.png','.jpg','.jpeg','.tif','.tiff','.html')) or rel=='records/AC26_original_extracted.txt' or bool(re.fullmatch(r'records/web_\d+\.json',rel)) or rel=='code/part1/ocr_wall.out'

paths=[]
for p in sorted(ROOT.rglob('*')):
    if not p.is_file():continue
    rel=p.relative_to(ROOT).as_posix()
    if excluded(rel):continue
    if p.suffix.lower() in {'.png','.pdf','.log','.out','.err','.aux','.toc'} and rel!='S6_06_BLIND_paper.pdf':paths.append(p)

files={};seen={};total=0;started=time.monotonic()
filters=[{'id':lzma.FILTER_LZMA2,'preset':6,'dict_size':32*1024*1024}]
with lzma.open(partial,'xb',filters=filters) as packed:
    with tarfile.open(fileobj=packed,mode='w|',format=tarfile.PAX_FORMAT) as tar:
        for i,p in enumerate(paths):
            data=p.read_bytes();digest=hashlib.sha256(data).hexdigest()
            name=p.relative_to(BASE).as_posix()
            files[name]={'bytes':len(data),'sha256':digest}
            item=tarfile.TarInfo(name);item.mode=0o644;item.mtime=int(p.stat().st_mtime)
            if digest in seen:
                item.type=tarfile.LNKTYPE;item.linkname=seen[digest];tar.addfile(item)
            else:
                item.size=len(data);tar.addfile(item,io.BytesIO(data));seen[digest]=name;total+=len(data)
            if (i+1)%500==0:print(json.dumps({'packed_files':i+1,'total_files':len(paths),'unique_bytes':total,'elapsed_seconds':round(time.monotonic()-started,1)}),flush=True)
partial.rename(target)
with target.open('rb') as f:digest=hashlib.file_digest(f,'sha256').hexdigest()
result={'status':'COMPLETE','utc':datetime.now(timezone.utc).isoformat(),'base_bundle':target.name,'bytes':target.stat().st_size,'sha256':digest,'files':files,'unique_contents':len(seen),'unique_input_bytes':total,'elapsed_seconds':round(time.monotonic()-started,1),'scope':'Compression-only base; final snapshot must match each current file hash before reusing it.'}
manifest.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='files'},indent=2),flush=True)
