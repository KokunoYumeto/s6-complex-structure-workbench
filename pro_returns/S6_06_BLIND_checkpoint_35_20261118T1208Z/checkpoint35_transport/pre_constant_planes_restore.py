"""Restore the exact checkpoint35 bytes, consuming closed dependency groups.

Every original dictionary, member and final file is hash-checked. Only the
order of temporary extraction/decoding changes; no research payload is edited.
"""
from pathlib import Path
import hashlib,json,tarfile,tempfile,shutil,lzma
from checkpoint_copy_add import decode as decode_copy
from checkpoint_png_codec import decode as decode_png
from checkpoint_gzip_exact_codec import decode_file as decode_gzip
from checkpoint_zlib_object_codec import decode_file as decode_zlib
from checkpoint_png_rows_codec import decode_file as decode_png_rows,close_dictionaries

BASE=Path(__file__).resolve().parent
M=json.loads((BASE/'checkpoint35_transport_manifest.json').read_text())
def sha(path):
 with path.open('rb')as f:return hashlib.file_digest(f,'sha256').hexdigest()
def target(root,name):
 p=(root/name).resolve()
 if not p.is_relative_to(root.resolve()):raise ValueError('Unsafe archive path')
 return p
def verified(p,size,digest):
 assert p.is_file()and p.stat().st_size==size,(str(p),'size')
 assert sha(p)==digest,(str(p),'SHA256')
for support in M.get('transport_support_files',[]):verified(target(BASE,support['file']),support['bytes'],support['sha256'])

with tempfile.TemporaryDirectory(prefix='.checkpoint35_restore_',dir=BASE)as temporary:
 stage=Path(temporary);seen=set();completed=set();decoded_png=set();dict_left={};dict_verified={}
 for row in M.get('object_transforms',[]):
  if row['codec']=='png_filtered_rows_v1':dict_left[row['dictionary_name']]=dict_left.get(row['dictionary_name'],0)+1
 rows=M.get('object_transforms',[])
 streaming={row['encoded_name']:(i,row)for i,row in enumerate(rows)if row['codec']=='png_rgb_dictionary_v1'}
 class HashReader:
  def __init__(self,source):self.source=source;self.hash=hashlib.sha256();self.bytes=0
  def read(self,n=-1):
   data=self.source.read(n);self.hash.update(data);self.bytes+=len(data);return data
 def ready():
  changed=True
  while changed:
   changed=False
   for index,row in enumerate(rows):
    if index in completed:continue
    packed=target(stage,row['encoded_name'])
    if not packed.exists():continue
    if row['codec']=='png_filtered_rows_v1'and not target(stage,row['dictionary_name']).exists():continue
    verified(packed,row['encoded_bytes'],row['encoded_sha256'])
    original=target(stage,row['original_name']);original.parent.mkdir(parents=True,exist_ok=True);assert not original.exists()
    if row['codec']=='zlib_object_v1':decode_zlib(packed,original)
    elif row['codec']=='png_filtered_rows_v1':
     name=row['dictionary_name'];dictionary=target(stage,name);identity=(row['dictionary_bytes'],row['dictionary_sha256'])
     if name not in dict_verified:verified(dictionary,*identity);dict_verified[name]=identity
     else:assert dict_verified[name]==identity
     decode_png_rows(packed,original,dictionary)
    else:raise ValueError('Unknown member codec '+row['codec'])
    verified(original,row['original_bytes'],row['original_sha256']);packed.unlink();completed.add(index);changed=True
    if row['codec']=='png_filtered_rows_v1':
     h=row['original_content_sha256'];info=M['contents'][h]
     assert info['storage']=='png'and info['encoded_name']==row['original_name']and info['encoded_sha256']==row['original_sha256']
     out=target(stage,'content/'+h);out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(decode_png(original.read_bytes()));verified(out,info['bytes'],h);original.unlink();decoded_png.add(h)
     dict_left[name]-=1
     if not dict_left[name]:close_dictionaries();dictionary.unlink();print('Consumed verified dictionary '+name,flush=True)
     if len(decoded_png)%200==0:print('Restored exact original PNG '+str(len(decoded_png)),flush=True)
   for h,info in M['contents'].items():
    out=target(stage,'content/'+h)
    if out.exists():continue
    if info['storage']in('gzip_exact','png'):
     packed=target(stage,info['encoded_name'])
     if not packed.exists():continue
     assert sha(packed)==info['encoded_sha256'];out.parent.mkdir(parents=True,exist_ok=True)
     if info['storage']=='gzip_exact':decode_gzip(packed,out,info['gzip_metadata'])
     else:out.write_bytes(decode_png(packed.read_bytes()));decoded_png.add(h)
     verified(out,info['bytes'],h);packed.unlink();changed=True
   for h in M['patch_order']:
    info=M['contents'][h];out=target(stage,'content/'+h)
    if out.exists():continue
    reference=target(stage,'content/'+info['base_sha256']);patch=target(stage,info['patch_name'])
    if not reference.exists()or not patch.exists():continue
    assert sha(reference)==info['base_sha256']and sha(patch)==info['patch_sha256']
    out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(decode_copy(reference.read_bytes(),patch.read_bytes()));verified(out,info['bytes'],h);patch.unlink();changed=True
 names=M.get('restore_bundle_order',[b['file']for b in M['bundles']]);bundles={b['file']:b for b in M['bundles']}
 assert len(names)==len(bundles)and set(names)==set(bundles)
 for index,name in enumerate(names):
  bundle=bundles[name];archive=target(BASE,name);verified(archive,bundle['bytes'],bundle['sha256'])
  with lzma.open(archive,'rb')as stream,tarfile.open(fileobj=stream,mode='r|')as tar:
   for member in tar:
    if not member.isfile()or member.name in seen:raise ValueError('Invalid/repeated member '+member.name)
    seen.add(member.name);out=target(stage,member.name);out.parent.mkdir(parents=True,exist_ok=True)
    source=tar.extractfile(member)
    if source is None:raise ValueError('Missing packed bytes')
    if member.name in streaming:
     from checkpoint_png_rgb_dictionary import decode_stream as decode_rgb_dictionary
     rowindex,row=streaming[member.name];assert member.size==row['encoded_bytes']
     original=target(stage,row['original_name']);original.parent.mkdir(parents=True,exist_ok=True)
     reader=HashReader(source)
     with source,original.open('xb')as sink:decoded_rows=decode_rgb_dictionary(reader,sink)
     assert decoded_rows==row['rows']and reader.bytes==row['encoded_bytes']and reader.hash.hexdigest()==row['encoded_sha256']
     verified(original,row['original_bytes'],row['original_sha256']);completed.add(rowindex)
     print('Streamed exact original dictionary '+row['original_name'],flush=True)
    else:
     with source,out.open('xb')as sink:shutil.copyfileobj(source,sink,1024*1024)
     assert out.stat().st_size==member.size
  ready();print('Extracted and consumed dependency group '+str(index+1)+'/'+str(len(names)),flush=True)
 ready();assert len(completed)==len(rows)and all(n==0 for n in dict_left.values());close_dictionaries()
 for h,info in M['contents'].items():verified(target(stage,'content/'+h),info['bytes'],h)
 for name,info in M['predecessor_files'].items():verified(target(stage,'content/'+info['sha256']),info['bytes'],info['sha256'])
 locations={h:target(stage,'content/'+h)for h in M['contents']}
 for index,(name,info)in enumerate(M['files'].items()):
  h=info['sha256'];source=locations[h];out=target(BASE,name);verified(source,info['bytes'],h);out.parent.mkdir(parents=True,exist_ok=True)
  if out.exists():verified(out,info['bytes'],h)
  elif source.is_relative_to(stage):source.replace(out);locations[h]=out
  else:shutil.copyfile(source,out)
  if index%2000==0:print('Restored research file '+str(index+1)+'/'+str(len(M['files'])),flush=True)
for name,info in M['files'].items():verified(target(BASE,name),info['bytes'],info['sha256'])
print('PASS: restored and verified all '+str(len(M['files']))+' checkpoint35 files; every retained predecessor content object also verified.',flush=True)
