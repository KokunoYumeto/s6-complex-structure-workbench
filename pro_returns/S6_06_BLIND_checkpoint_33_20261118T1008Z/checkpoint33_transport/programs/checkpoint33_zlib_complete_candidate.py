"""Complete the measured existing-codec candidate with recovered old patches."""
from pathlib import Path
import json,hashlib,lzma,tarfile,sys,time
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parent;oldpath=BASE/'checkpoint33_zlib_additions_candidate/result.json';old=json.loads(oldpath.read_text());mp=BASE/'checkpoint33_encoding/checkpoint33_transport_manifest.json';m=json.loads(mp.read_text());out=BASE/'checkpoint33_zlib_complete_candidate';out.mkdir(exist_ok=True)
sys.path.insert(0,str(BASE/'checkpoint32_encoding'));from checkpoint_zlib_object_codec import encode_bytes,decode_bytes
sha=lambda p:hashlib.file_digest(p.open('rb'),'sha256').hexdigest()
assert old['status']=='PASS_ALL_ORIGINAL_MEMBERS_AND_INDEPENDENT_BUNDLE_DECODE';rows=list(old['object_transforms']);stats=list(old['full_stream_records']);paths={r['encoded_name']:BASE/'checkpoint33_zlib_additions_candidate'/(r['encoded_name'].split('/')[-1]+'.encoded')for r in rows};present={r['original_name']for r in rows};pre={r['original_name']for r in m['object_transforms']};t=time.time()
for h,d in m['contents'].items():
 if d['storage']!='copy_add'or d['patch_name']in present|pre:continue
 p=BASE/'checkpoint33_member_index'/(h+'.copyadd');original=p.read_bytes();assert hashlib.sha256(original).hexdigest()==d['patch_sha256'];encoded,info=encode_bytes(original);assert decode_bytes(encoded,chunk_size=8191)==original
 if not info['stream_count']:continue
 key=hashlib.sha256(d['patch_name'].encode()).hexdigest();name='zlib_objects33/'+key;dest=out/(key+'.encoded');dest.write_bytes(encoded);paths[name]=dest
 row={'codec':'zlib_object_v1','original_name':d['patch_name'],'original_bytes':len(original),'original_sha256':d['patch_sha256'],'encoded_name':name,'encoded_bytes':len(encoded),'encoded_sha256':sha(dest)};rows.append(row);stats.append({'name':d['patch_name'],'input':str(p),**info});print(json.dumps({'status':'PASS_EXACT_RECOVERED_PATCH','name':d['patch_name'],'streams':info['stream_count']}),flush=True)
bundle=out/'checkpoint33_zlib_complete.tar.xz'
with lzma.open(bundle,'xb',filters=[{'id':lzma.FILTER_LZMA2,'preset':6,'dict_size':64*1024*1024}])as sink,tarfile.open(fileobj=sink,mode='w|')as tar:
 for r in rows:
  p=paths[r['encoded_name']];assert p.stat().st_size==r['encoded_bytes']and sha(p)==r['encoded_sha256'];i=tarfile.TarInfo(r['encoded_name']);i.size=r['encoded_bytes'];i.mode=420;i.mtime=0
  with p.open('rb')as f:tar.addfile(i,f)
with lzma.open(bundle,'rb')as source,tarfile.open(fileobj=source,mode='r|')as tar:
 lookup={r['encoded_name']:r for r in rows};seen=set()
 for member in tar:
  r=lookup[member.name];b=tar.extractfile(member).read();assert len(b)==r['encoded_bytes']and hashlib.sha256(b).hexdigest()==r['encoded_sha256'];a=decode_bytes(b,chunk_size=65537);assert len(a)==r['original_bytes']and hashlib.sha256(a).hexdigest()==r['original_sha256'];seen.add(member.name)
 assert seen==set(lookup)
r={'status':'PASS_ALL_ORIGINAL_MEMBERS_AND_INDEPENDENT_BUNDLE_DECODE','manifest_sha256':sha(mp),'objects':len(rows),'original_bytes':sum(r['original_bytes']for r in rows),'encoded_bytes':sum(r['encoded_bytes']for r in rows),'bundle':{'file':bundle.name,'local_path':str(bundle),'bytes':bundle.stat().st_size,'sha256':sha(bundle),'members':len(rows)},'object_transforms':rows,'encoded_paths':{k:str(v)for k,v in paths.items()},'full_stream_records':stats,'prior_candidate_sha256':sha(oldpath),'program_sha256':sha(Path(__file__)),'seconds':time.time()-t};(out/'result.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items()if k not in ['object_transforms','encoded_paths','full_stream_records']}),flush=True)
