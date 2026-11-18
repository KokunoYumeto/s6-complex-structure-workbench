"""Exact row-access and complete delivered-restorer integration checks."""
from pathlib import Path
import hashlib,io,json,lzma,random,shutil,struct,subprocess,sys,tarfile,tempfile,zlib
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parent
sys.path.insert(0,str(BASE/'checkpoint35_encoding'))
from checkpoint_png_codec import encode as encode_png
from checkpoint_png_rgb_dictionary import MAGIC as RGB_MAGIC,ORIGINAL_MAGIC,forward as rgb_forward
from checkpoint_rgb_constant_planes_codec import MAGIC as CONSTANT_MAGIC,forward as constant_forward
from checkpoint_png_rows_codec import MAGIC as ROW_MAGIC
from checkpoint_constant_planes_dictionary_view import store_verified_dictionary
from checkpoint_constant_planes_view_restore_patch import patch
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def digest(b):return hashlib.sha256(b).hexdigest()
def streams(rows):
 original=ORIGINAL_MAGIC+b''.join(struct.pack('>I',len(row))+row for row in rows)
 rgb=RGB_MAGIC+b''.join(struct.pack('>I',len(row))+rgb_forward(row) for row in rows)
 encoded=CONSTANT_MAGIC+b''.join(struct.pack('>I',len(row))+constant_forward(rgb_forward(row)) for row in rows)
 metadata={'codec':'png_rgb_constant_planes_v1','encoded_name':'constant/new','encoded_bytes':len(encoded),'encoded_sha256':digest(encoded),
           'original_name':'dictionary/new','original_bytes':len(original),'original_sha256':digest(original),'rows':len(rows),
           'prior_rgb_bytes':len(rgb),'prior_rgb_sha256':digest(rgb)}
 return original,rgb,encoded,metadata
checks=0;rng=random.Random(3537);outcomes=[]
with tempfile.TemporaryDirectory(prefix='checkpoint35_dictionary_view_') as td:
 temporary=Path(td)
 rows=[b'',b'\0',b'\x01\x02']+[bytes([17])*n for n in range(3,40)]
 rows += [bytes(rng.randrange(256) for _ in range(n)) for n in range(1,130)]
 rows += [b'']*8200
 original,rgb,encoded,meta=streams(rows)
 for budget in (0,1,31,32*1024*1024):
  path=temporary/f'view-{budget}.bin'
  view=store_verified_dictionary(io.BytesIO(encoded),path,meta,cache_bytes=budget)
  for index in list(range(len(rows)))+list(range(170,-1,-1)):
   assert view.row(index)==rows[index];checks+=1
   assert view.cache_bytes<=budget and len(view.cache)<=8192;checks+=1
  view.check_unchanged();view.close();view.close();assert view.closed;checks+=1
  try:view.row(0)
  except AssertionError:checks+=1
  else:raise AssertionError('Closed descriptor accepted a row')
  assert path.read_bytes()==encoded;checks+=1

 def chunk(kind,payload):
  body=kind+payload;return struct.pack('>I',len(payload))+body+struct.pack('>I',zlib.crc32(body)&0xffffffff)
 scanlines=[b'\0'+bytes([10,20,30,40,50,60]),b'\0'+bytes([255]*6),b'\0'+bytes(6),b'\0'+bytes([10,20,30,40,50,60])]
 png=b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>IIBBBBB',2,4,8,2,0,0,0))+chunk(b'IDAT',zlib.compress(b''.join(scanlines),6))+chunk(b'IEND',b'')
 png_member=encode_png(png);assert png_member is not None;checks+=1
 header_size=12+struct.unpack('>I',png_member[8:12])[0];prefix=png_member[:header_size]
 dictionary_rows=[b'',b'x',b'xy']+list(dict.fromkeys(scanlines))
 original,rgb,encoded,meta=streams(dictionary_rows);ids=[dictionary_rows.index(row) for row in scanlines]
 row_object=ROW_MAGIC+struct.pack('>Q',len(png_member))+hashlib.sha256(png_member).digest()+struct.pack('>I',len(prefix))+prefix+struct.pack('>I',len(ids))+b''.join(struct.pack('>I',i) for i in ids)
 old=(BASE/'checkpoint35_encoding/restore_checkpoint.py').read_text();new=patch(old)
 for failure in ('none','intermediate_hash','original_hash','row_id'):
  dest=temporary/failure;dest.mkdir();supports=[]
  for name in ('checkpoint_copy_add.py','checkpoint_png_codec.py','checkpoint_gzip_exact_codec.py',
               'checkpoint_zlib_object_codec.py','checkpoint_png_rows_codec.py','checkpoint_png_rgb_dictionary.py',
               'checkpoint_rgb_constant_planes_codec.py','checkpoint_constant_planes_dictionary_view.py'):
   source=ROOT/'code'/name
   if not source.is_file():source=BASE/'checkpoint35_encoding'/name
   shutil.copy2(source,dest/name);supports.append({'file':name,'bytes':(dest/name).stat().st_size,'sha256':sha(dest/name)})
  h=digest(png);row=dict(meta)
  if failure=='intermediate_hash':row['prior_rgb_sha256']='0'*64
  if failure=='original_hash':row['original_sha256']='0'*64
  obj=row_object if failure!='row_id' else row_object[:-4]+struct.pack('>I',len(dictionary_rows)+1)
  png_transform={'codec':'png_filtered_rows_v1','encoded_name':'rows/png','encoded_bytes':len(obj),'encoded_sha256':digest(obj),
                 'original_name':'png/'+h,'original_bytes':len(png_member),'original_sha256':digest(png_member),
                 'dictionary_name':'dictionary/new','dictionary_bytes':len(original),'dictionary_sha256':digest(original),'original_content_sha256':h}
  payload=b'Original nonimage bytes.\x00\xff\n';hp=digest(payload)
  bundle=dest/'literal.tar.xz'
  with lzma.open(bundle,'xb',preset=1) as stream,tarfile.open(fileobj=stream,mode='w|') as tar:
   for name,value in [('constant/new',encoded),('rows/png',obj),('content/'+hp,payload)]:
    info=tarfile.TarInfo(name);info.size=len(value);tar.addfile(info,io.BytesIO(value))
  manifest={'transport_support_files':supports,'object_transforms':[row,png_transform],
            'contents':{h:{'storage':'png','encoded_name':'png/'+h,'encoded_sha256':digest(png_member),'bytes':len(png)},
                        hp:{'storage':'raw','name':'content/'+hp,'bytes':len(payload)}},
            'patch_order':[],'bundles':[{'file':bundle.name,'bytes':bundle.stat().st_size,'sha256':sha(bundle)}],
            'restore_bundle_order':[bundle.name],'predecessor_files':{'old.bin':{'bytes':len(payload),'sha256':hp}},
            'files':{'restored/exact.png':{'bytes':len(png),'sha256':h},'restored/duplicate.png':{'bytes':len(png),'sha256':h},'restored/exact.bin':{'bytes':len(payload),'sha256':hp}}}
  (dest/'checkpoint35_transport_manifest.json').write_text(json.dumps(manifest))
  (dest/'restore_checkpoint.py').write_text(new)
  run=subprocess.run([sys.executable,str(dest/'restore_checkpoint.py')],cwd=dest,capture_output=True,text=True)
  if failure=='none':
   assert run.returncode==0,run.stderr;checks+=1
   assert (dest/'restored/exact.png').read_bytes()==(dest/'restored/duplicate.png').read_bytes()==png;checks+=1
   assert (dest/'restored/exact.bin').read_bytes()==payload;checks+=1
   assert 'Consumed verified dictionary dictionary/new' in run.stdout;checks+=1
  else:
   assert run.returncode!=0;checks+=1
   assert not (dest/'restored/exact.png').exists();checks+=1
  outcomes.append({'failure_case':failure,'returncode':run.returncode,'stdout':run.stdout,'stderr_sha256':digest(run.stderr.encode())})
record={'status':'PASS','checks':checks,'exact_row_cases':len(rows),'cache_budgets':[0,1,31,32*1024*1024],
        'source_locks':{name:sha(ROOT/name) for name in ['code/checkpoint_constant_planes_dictionary_view.py','code/checkpoint_constant_planes_view_restore_patch.py','notes/checkpoint35_constant_planes_dictionary_view.md']},
        'old_restorer_sha256':digest(old.encode()),'new_restorer_sha256':digest(new.encode()),'program_sha256':sha(__file__),
        'outcomes':outcomes,'scope':'Actual exact-row access for original IDs under bounded caches and closed descriptors; actual delivered restorer restores original PNG bytes and duplicate files through the unchanged PNG codec, and rejects wrong intermediate/original hashes and invalid row IDs. Whole large frozen checkpoint recovery remains separate.'}
(ROOT/'records/checkpoint35_dictionary_view_checks.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
