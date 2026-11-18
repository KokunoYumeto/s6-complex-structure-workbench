"""Measure the complete exact constant-plane outer dictionary representation.

No live transport manifest is changed. Every other retained member, the
complete prior RGB stream and the complete original row dictionary are
independently checked through the closed candidate's streaming inverse.
"""
from pathlib import Path
from datetime import datetime,timezone
import copy,hashlib,json,lzma,resource,struct,tarfile,time
from checkpoint_rgb_constant_planes_codec import MAGIC,RGB_MAGIC,forward,RGBReader
from checkpoint_png_rgb_dictionary import decode_stream as decode_original
R=Path(__file__).resolve().parents[1];BASE=R.parent;OUT=BASE/'checkpoint35_constant_planes_complete';OUT.mkdir(exist_ok=False)
SRC=BASE/'checkpoint33_dictionary_rgb_complete/checkpoint33_rgb_original_dictionary.tar.xz';DST=OUT/'checkpoint35_constant_original_dictionary.tar.xz'
OLD='rgb_dictionary_33/png_filtered_rows_31';NEW='rgb_constant_dictionary_35/png_filtered_rows_31'
RGBSIZE=5533013867;RGBSHA='5cfaf1bbcd269b6210b7708aaa72939a9658c4f8e8d22b24755a042eb964e8aa'
ORIGSIZE=5533013871;ORIGSHA='a1c39525e573980a1cc3b8e593f9d887ddf49997f338c4c4a70140bb7180daa1'
START=time.monotonic()
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
class HashReader:
 def __init__(self,f):self.f=f;self.n=0;self.h=hashlib.sha256()
 def read(self,n=-1):
  b=self.f.read(n);self.n+=len(b);self.h.update(b);return b
class HashSink:
 def __init__(self):self.n=0;self.h=hashlib.sha256()
 def write(self,b):self.n+=len(b);self.h.update(b);return len(b)
assert SRC.stat().st_size==273095952 and sha(SRC)=='55c4bf4430348a414c3a130b1c7ab360a19f3bb180f4ce941d272bde6bcf2709'
expected={};encoded_size=len(MAGIC);rows=0;constant_planes=0
with tarfile.open(SRC,'r|xz') as tf:
 for ti in tf:
  assert ti.isfile() and ti.name not in expected;f=HashReader(tf.extractfile(ti))
  if ti.name==OLD:
   assert ti.size==RGBSIZE and f.read(len(RGB_MAGIC))==RGB_MAGIC
   while True:
    h=f.read(4)
    if not h:break
    n=struct.unpack('>I',h)[0];row=f.read(n);assert len(row)==n;changed=forward(row);encoded_size+=4+len(changed);rows+=1;constant_planes+=changed[n%3].bit_count()
   assert f.n==RGBSIZE and f.h.hexdigest()==RGBSHA and rows==1901249
  else:
   while f.read(1024*1024):pass
  assert f.n==ti.size;expected[ti.name]={'name':ti.name,'bytes':f.n,'sha256':f.h.hexdigest()}
assert len(expected)==3601
print(json.dumps({'stage':'FULL_SIZE_SCAN_PASS','rows':rows,'encoded_bytes':encoded_size,'constant_planes':constant_planes,'seconds':time.monotonic()-START}),flush=True)
class ConstantReader:
 def __init__(self,f):
  self.f=HashReader(f);assert self.f.read(len(RGB_MAGIC))==RGB_MAGIC;self.buffer=MAGIC;self.finished=False;self.rows=0;self.mark=0
 def read(self,n=-1):
  assert n>=0;parts=[self.buffer];amount=len(self.buffer)
  while amount<n and not self.finished:
   h=self.f.read(4)
   if not h:self.finished=True;break
   length=struct.unpack('>I',h)[0];row=self.f.read(length);assert len(row)==length;changed=h+forward(row);parts.append(changed);amount+=len(changed);self.rows+=1
   if self.f.n-self.mark>=256*1024*1024:
    print(json.dumps({'stage':'ENCODING','original_rgb_bytes':self.f.n,'rows':self.rows,'compressed_bytes':DST.stat().st_size,'seconds':time.monotonic()-START}),flush=True);self.mark=self.f.n
  value=b''.join(parts);self.buffer=value[n:];return value[:n]
filters=[{'id':lzma.FILTER_LZMA2,'preset':6,'dict_size':64*1024*1024}];transform=None
with tarfile.open(SRC,'r|xz') as tin,lzma.open(DST,'xb',format=lzma.FORMAT_XZ,check=lzma.CHECK_CRC64,filters=filters) as z,tarfile.open(fileobj=z,mode='w|',format=tarfile.PAX_FORMAT) as tout:
 for ti in tin:
  source=tin.extractfile(ti);new=copy.copy(ti)
  if ti.name==OLD:
   native=ConstantReader(source);reader=HashReader(native);new.name=NEW;new.size=encoded_size;tout.addfile(new,reader);assert native.read(1)==b''
   assert reader.n==encoded_size and native.f.n==RGBSIZE and native.f.h.hexdigest()==RGBSHA and native.rows==rows
   transform={'codec':'png_rgb_constant_planes_v1','original_name':'dictionary/png_filtered_rows_31','original_bytes':ORIGSIZE,'original_sha256':ORIGSHA,'encoded_name':NEW,'encoded_bytes':reader.n,'encoded_sha256':reader.h.hexdigest(),'prior_rgb_name':OLD,'prior_rgb_bytes':RGBSIZE,'prior_rgb_sha256':RGBSHA,'rows':rows}
  else:
   reader=HashReader(source);tout.addfile(new,reader);assert {'name':ti.name,'bytes':reader.n,'sha256':reader.h.hexdigest()}==expected[ti.name]
print(json.dumps({'stage':'CLOSED_CANDIDATE_FULL_INVERSE_NEXT','bytes':DST.stat().st_size,'saving':SRC.stat().st_size-DST.stat().st_size,'seconds':time.monotonic()-START}),flush=True)
assert transform;seen=set()
with tarfile.open(DST,'r|xz') as tf:
 for ti in tf:
  reader=HashReader(tf.extractfile(ti))
  if ti.name==NEW:
   rgb=RGBReader(reader);middle=HashReader(rgb);sink=HashSink();count=decode_original(middle,sink)
   assert count==rgb.rows==rows and sink.n==ORIGSIZE and sink.h.hexdigest()==ORIGSHA
   assert middle.n==RGBSIZE and middle.h.hexdigest()==RGBSHA
   assert reader.n==encoded_size and reader.h.hexdigest()==transform['encoded_sha256'];seen.add(OLD)
  else:
   while reader.read(1024*1024):pass
   assert {'name':ti.name,'bytes':reader.n,'sha256':reader.h.hexdigest()}==expected[ti.name];seen.add(ti.name)
assert seen==set(expected) and sha(SRC)=='55c4bf4430348a414c3a130b1c7ab360a19f3bb180f4ce941d272bde6bcf2709'
rec={'status':'PASS_FULL_CONSTANT_PLANES_AND_ORIGINAL_DICTIONARY','utc':datetime.now(timezone.utc).isoformat(),'original_bundle':{'file':SRC.name,'local_path':str(SRC),'bytes':SRC.stat().st_size,'sha256':sha(SRC)},'bundle':{'file':DST.name,'local_path':str(DST),'bytes':DST.stat().st_size,'sha256':sha(DST),'members':len(expected)},'object_transform':transform,'retained_members':list(expected.values()),'saving':SRC.stat().st_size-DST.stat().st_size,'constant_planes':constant_planes,'filters':filters,'seconds':time.monotonic()-START,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'codec_sha256':sha(R/'code/checkpoint_rgb_constant_planes_codec.py'),'prior_rgb_codec_sha256':sha(R/'code/checkpoint_png_rgb_dictionary.py'),'program_sha256':sha(__file__),'selected':False,'original_row_order_and_indices_unchanged':True,'live_manifest_modified':False}
(OUT/'result.json').write_text(json.dumps(rec,indent=2)+'\n');(R/'records/checkpoint35_constant_planes_complete.json').write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps({k:v for k,v in rec.items() if k!='retained_members'}),flush=True)
