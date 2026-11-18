"""Bounded new-PNG row dictionary, preserving every32 decoder and object.

This encodes only the305 previously untransformed PNG members of the fixed33
manifest. The existing, byte-locked png_filtered_rows_v1 decoder already
supports a separate named dictionary. Every match is byte compared, then
each full original member and PNG is independently decoded and compared.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import OrderedDict
import array,base64,gc,hashlib,json,lzma,os,struct,sys,tarfile,time

ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parent
STAGE=BASE/'checkpoint33_png_rows_candidate'
STAGE.mkdir(exist_ok=True);OBJECTS=STAGE/'objects';OBJECTS.mkdir(exist_ok=True)
MANIFEST=BASE/'checkpoint33_encoding/checkpoint33_transport_manifest.json'
FROZEN=BASE/'checkpoint33_encoding/frozen'
FROZEN_MANIFEST=BASE/'checkpoint33_encoding/frozen_manifest.json'
SUPPORT=BASE/'checkpoint32_encoding'
sys.path.insert(0,str(SUPPORT))
from checkpoint_png_rows_codec import MAGIC,DICT_MAGIC,decode_file,close_dictionaries
from checkpoint_png_codec import decode as decode_png

def sha(path):
    with Path(path).open('rb')as f:return hashlib.file_digest(f,'sha256').hexdigest()
def atomic(path,value):
    pending=path.with_suffix(path.suffix+'.pending');pending.write_text(json.dumps(value,indent=2)+'\n');pending.replace(path)
def emit(value):print(json.dumps(value),flush=True)

start=time.monotonic();m=json.loads(MANIFEST.read_text())
initial_sha=sha(MANIFEST);freeze_sha=sha(FROZEN_MANIFEST)
assert freeze_sha=='6db797412be4473f5410a8b56332660cab057dc5def4f1ac7c017898101906e7'
transformed={r['original_name']for r in m['object_transforms']}
names={r['sha256']:n for n,r in m['files'].items()}
selected=sorted((names[h],h,c)for h,c in m['contents'].items()
                if c['storage']=='png' and c['encoded_name']not in transformed)
assert len(selected)==305
dictionary=STAGE/'png_filtered_rows_33.bin'
assert not dictionary.exists(),'Preserve a prior candidate before a separate restart'
atomic(STAGE/'input_manifest_lock.json',{'source_manifest_sha256':initial_sha,
    'frozen_manifest_sha256':freeze_sha,'selected_pngs':len(selected),
    'predecessor_dictionary_unchanged':True,'scope':'New named dictionary using unchanged delivered32 decoder.'})
index={};offsets=array.array('Q');lengths=array.array('I');rows=[]
cache=OrderedDict();cache_bytes=0;total_rows=duplicates=raw_total=0
with dictionary.open('x+b',buffering=0)as store:
    store.write(DICT_MAGIC)
    for number,(name,h,info)in enumerate(selected):
        path=BASE/'checkpoint33_encoding/encoded_objects'/(h+'.pngcodec')
        data=path.read_bytes();assert hashlib.sha256(data).hexdigest()==info['encoded_sha256']
        assert data[:8]==b'S6PNG01\0'
        size=struct.unpack('>I',data[8:12])[0];prefix=data[:12+size]
        meta=json.loads(data[12:12+size]);raw=memoryview(data)[12+size:]
        ihdr=None
        for item in meta['chunks']:
            if 'bytes'in item:
                block=base64.b64decode(item['bytes'])
                if block[4:8]==b'IHDR':ihdr=struct.unpack('>IIBBBBB',block[8:21]);break
        width,height,depth,color,compression,filter_method,interlace=ihdr
        assert depth==8 and interlace==0 and color in {0,2,4,6}
        stride=width*{0:1,2:3,4:2,6:4}[color]+(0 if meta.get('layout')=='pixels'else 1)
        assert len(raw)==stride*height
        encoded=OBJECTS/(h+'.pngrows')
        with encoded.open('xb')as out:
            out.write(MAGIC+struct.pack('>Q',len(data))+hashlib.sha256(data).digest()
                      +struct.pack('>I',len(prefix))+prefix+struct.pack('>I',height))
            for y in range(height):
                row=bytes(raw[y*stride:(y+1)*stride]);key=hashlib.blake2b(row,digest_size=16).digest()
                candidates=index.get(key,[]);found=None
                for rid in candidates:
                    previous=cache.get(rid)
                    if previous is None:previous=os.pread(store.fileno(),lengths[rid],offsets[rid])
                    if previous==row:found=rid;break
                if found is None:
                    found=len(offsets);assert found<2**32
                    position=store.tell();store.write(struct.pack('>I',len(row))+row)
                    offsets.append(position+4);lengths.append(len(row))
                    index.setdefault(key,[]).append(found)
                else:duplicates+=1
                if found not in cache:
                    cache[found]=row;cache_bytes+=len(row)
                    while cache_bytes>8*1024*1024:
                        _,old=cache.popitem(last=False);cache_bytes-=len(old)
                else:cache.move_to_end(found)
                out.write(struct.pack('>I',found));total_rows+=1
        raw_total+=len(data)
        rows.append({'codec':'png_filtered_rows_v1','original_name':info['encoded_name'],
          'original_bytes':len(data),'original_sha256':info['encoded_sha256'],
          'encoded_name':'png_rows_33/'+h,'encoded_local_path':str(encoded),
          'encoded_bytes':encoded.stat().st_size,'encoded_sha256':sha(encoded),
          'original_content_sha256':h,'original_file':name,'height':height,'stride':stride})
        if number%25==0:emit({'status':'SCANNED_NEW_PNG_ROWS','objects':number+1,
          'dictionary_bytes':store.tell(),'unique_rows':len(offsets),'duplicate_rows':duplicates})
dict_sha=sha(dictionary);dict_size=dictionary.stat().st_size;unique_count=len(offsets)
for row in rows:row.update(dictionary_name='dictionary/png_filtered_rows_33',
                          dictionary_bytes=dict_size,dictionary_sha256=dict_sha)
del index,offsets,lengths,cache,data,raw;gc.collect()
metadata={'status':'SCANNED','source_manifest_sha256':initial_sha,'frozen_manifest_sha256':freeze_sha,
  'objects':rows,'dictionary_local_path':str(dictionary),'dictionary_bytes':dict_size,
  'dictionary_sha256':dict_sha,'unique_rows':unique_count,'total_rows':total_rows,
  'duplicate_rows':duplicates,'original_encoded_bytes':raw_total,
  'predecessor_dictionary_unchanged':True,'all_predecessor_transforms_unchanged':True}
atomic(STAGE/'object_transforms.json',metadata)
emit({'status':'VERIFYING_ALL_NEW_MEMBER_AND_PNG_BYTES','objects':len(rows),'dictionary_bytes':dict_size})
probe=STAGE/'decoded_member.tmp'
for i,row in enumerate(rows):
    decode_file(row['encoded_local_path'],probe,dictionary)
    original=BASE/'checkpoint33_encoding/encoded_objects'/(row['original_content_sha256']+'.pngcodec')
    assert probe.read_bytes()==original.read_bytes()
    assert sha(probe)==row['original_sha256'] and probe.stat().st_size==row['original_bytes']
    png=decode_png(probe.read_bytes());source=FROZEN/row['original_file']
    assert png==source.read_bytes() and hashlib.sha256(png).hexdigest()==row['original_content_sha256']
    if i%50==0:emit({'status':'PASS_EXACT_NEW_PNG','objects':i+1})
close_dictionaries();probe.unlink()
metadata.update(status='PASS_ALL_ORIGINAL_NEW_MEMBER_AND_PNG_BYTES',verified_objects=len(rows))
atomic(STAGE/'object_transforms.json',metadata)

bundle=STAGE/'checkpoint33_new_png_rows.tar.xz'
emit({'status':'COMPRESSING_SEPARATE_NEW_DICTIONARY','dictionary_bytes':dict_size})
with lzma.open(bundle,'xb',filters=[{'id':lzma.FILTER_LZMA2,'preset':6,'dict_size':64*1024*1024}])as stream:
    with tarfile.open(fileobj=stream,mode='w|',format=tarfile.USTAR_FORMAT)as tar:
        for name,path in [(r['encoded_name'],Path(r['encoded_local_path']))for r in rows]+[('dictionary/png_filtered_rows_33',dictionary)]:
            member=tarfile.TarInfo(name);member.mode=0o644;member.mtime=0;member.size=path.stat().st_size
            with path.open('rb')as source:tar.addfile(member,source)
expect={r['encoded_name']:(r['encoded_bytes'],r['encoded_sha256'])for r in rows}
expect['dictionary/png_filtered_rows_33']=(dict_size,dict_sha)
with lzma.open(bundle,'rb')as stream,tarfile.open(fileobj=stream,mode='r|')as tar:
    for member in tar:
        f=tar.extractfile(member);digest=hashlib.sha256();amount=0
        while block:=f.read(1024*1024):digest.update(block);amount+=len(block)
        assert expect.pop(member.name)==(amount,digest.hexdigest())
assert not expect
metadata.update(status='PASS_ALL_NEW_PNG_MEMBER_AND_ARCHIVE_BYTES',
  bundle={'file':bundle.name,'local_path':str(bundle),'bytes':bundle.stat().st_size,'sha256':sha(bundle),'members':len(rows)+1},
  codec={'file':'checkpoint_png_rows_codec.py','sha256':sha(SUPPORT/'checkpoint_png_rows_codec.py')},
  program_sha256=sha(__file__),seconds=round(time.monotonic()-start,2))
atomic(STAGE/'object_transforms.json',metadata)
atomic(ROOT/'records/checkpoint33_new_png_rows_candidate.json',{k:v for k,v in metadata.items()if k!='objects'})
emit({k:v for k,v in metadata.items()if k not in {'objects','codec'}})
