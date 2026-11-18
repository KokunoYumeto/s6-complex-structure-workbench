"""Full row-bijection transport of the original immutable32 dictionary.

The original complete dictionary is hashed while read. The new delivered
standard-library inverse is then independently executed on the closed bundle.
All other original TAR member bytes are independently compared by size/SHA.
"""
from pathlib import Path
import copy,hashlib,json,lzma,struct,tarfile,time,resource
from checkpoint_png_rgb_dictionary import MAGIC,ORIGINAL_MAGIC,forward,decode_stream
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parent
OUT=BASE/'checkpoint33_dictionary_rgb_complete';OUT.mkdir(exist_ok=True)
SRC=BASE/'checkpoint32_png_repack/bundles/checkpoint32_global_png_rows.tar.xz'
DST=OUT/'checkpoint33_rgb_original_dictionary.tar.xz'
OLDNAME='dictionary/png_filtered_rows_31';NEWNAME='rgb_dictionary_33/png_filtered_rows_31'
OLDSIZE=5533013871;OLDHASH='a1c39525e573980a1cc3b8e593f9d887ddf49997f338c4c4a70140bb7180daa1'
def sha(p):
    with p.open('rb')as f:return hashlib.file_digest(f,'sha256').hexdigest()
class HashReader:
    def __init__(self,source):self.source=source;self.hash=hashlib.sha256();self.bytes=0
    def read(self,n=-1):
        value=self.source.read(n);self.hash.update(value);self.bytes+=len(value);return value
class HashSink:
    def __init__(self):self.hash=hashlib.sha256();self.bytes=0
    def write(self,b):self.hash.update(b);self.bytes+=len(b)
class RGBReader:
    def __init__(self,source):
        self.source=source;self.original=hashlib.sha256();self.original_bytes=0;self.rows=0;self.buf=b'';self.finished=False
        header=self.source.read(len(ORIGINAL_MAGIC));assert header==ORIGINAL_MAGIC
        self.original.update(header);self.original_bytes=len(header);self.buf=MAGIC
        self.last=0
    def read(self,n=-1):
        assert n>=0
        parts=[self.buf];amount=len(self.buf)
        while amount<n and not self.finished:
            header=self.source.read(4)
            if not header:self.finished=True;break
            assert len(header)==4
            size=struct.unpack('>I',header)[0];row=self.source.read(size);assert len(row)==size
            self.original.update(header);self.original.update(row);self.original_bytes+=size+4;self.rows+=1
            changed=header+forward(row);parts.append(changed);amount+=len(changed)
            if self.original_bytes-self.last>=256*1024*1024:
                print(json.dumps({'status':'ENCODING_EXACT_DICTIONARY_ROWS','original_bytes':self.original_bytes,'rows':self.rows,'compressed_bytes':DST.stat().st_size,'seconds':time.time()-START,'maxrss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),flush=True);self.last=self.original_bytes
        joined=b''.join(parts);self.buf=joined[n:];return joined[:n]

START=time.time();assert SRC.stat().st_size==318965560 and sha(SRC)=='96332e53e7827ff43184d06ef94d8feb98f10abe1fdc8fdf7fafb360819ebcb9'
members=[];transform=None;filters=[{'id':lzma.FILTER_LZMA2,'preset':6,'dict_size':64*1024*1024}]
with lzma.open(SRC,'rb')as a,tarfile.open(fileobj=a,mode='r|')as tin,lzma.open(DST,'xb',filters=filters)as b,tarfile.open(fileobj=b,mode='w|',format=tarfile.PAX_FORMAT)as tout:
    for old in tin:
        assert old.isfile();source=tin.extractfile(old);new=copy.copy(old)
        if old.name==OLDNAME:
            assert old.size==OLDSIZE
            rgb=RGBReader(source);reader=HashReader(rgb);new.name=NEWNAME;new.size=old.size-len(ORIGINAL_MAGIC)+len(MAGIC)
            tout.addfile(new,reader);assert not rgb.read(1)
            assert rgb.original_bytes==OLDSIZE and rgb.original.hexdigest()==OLDHASH and rgb.rows==1901249
            assert reader.bytes==new.size
            transform={'codec':'png_rgb_dictionary_v1','original_name':OLDNAME,'original_bytes':OLDSIZE,'original_sha256':OLDHASH,'encoded_name':NEWNAME,'encoded_bytes':reader.bytes,'encoded_sha256':reader.hash.hexdigest(),'rows':rgb.rows}
            members.append({'name':OLDNAME,'bytes':OLDSIZE,'sha256':OLDHASH})
        else:
            reader=HashReader(source);tout.addfile(new,reader);assert reader.bytes==old.size
            members.append({'name':old.name,'bytes':old.size,'sha256':reader.hash.hexdigest()})
        source.close()
assert transform is not None
expected={x['name']:x for x in members};seen=set()
print(json.dumps({'status':'CLOSED_RGB_BUNDLE_INVERSE_NEXT','bytes':DST.stat().st_size,'original_members':len(members),'seconds':time.time()-START}),flush=True)
with lzma.open(DST,'rb')as a,tarfile.open(fileobj=a,mode='r|')as tar:
    for item in tar:
        source=HashReader(tar.extractfile(item))
        if item.name==NEWNAME:
            sink=HashSink();rows=decode_stream(source,sink)
            assert rows==1901249 and sink.bytes==OLDSIZE and sink.hash.hexdigest()==OLDHASH
            assert source.bytes==transform['encoded_bytes'] and source.hash.hexdigest()==transform['encoded_sha256'];seen.add(OLDNAME)
        else:
            while source.read(1024*1024):pass
            row=expected[item.name];assert source.bytes==row['bytes'] and source.hash.hexdigest()==row['sha256'];seen.add(item.name)
assert seen==set(expected)
r={'status':'PASS_COMPLETE_ORIGINAL_DICTIONARY_AND_ALL_RETAINED_MEMBERS','original_bundle':{'file':SRC.name,'local_path':str(SRC),'bytes':SRC.stat().st_size,'sha256':sha(SRC)},'bundle':{'file':DST.name,'local_path':str(DST),'bytes':DST.stat().st_size,'sha256':sha(DST),'members':len(members)},'object_transform':transform,'original_members':members,'saving':SRC.stat().st_size-DST.stat().st_size,'filters':filters,'seconds':time.time()-START,'maxrss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'codec_sha256':sha(ROOT/'code/checkpoint_png_rgb_dictionary.py'),'program_sha256':sha(Path(__file__)),'original_archive_dictionary_indices_unchanged':True}
(OUT/'result.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items()if k!='original_members'}),flush=True)
