"""Exact residual TARs after independently reversible member substitutions."""
from pathlib import Path
import hashlib,json,lzma,tarfile,time,sys
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parent;OUT=BASE/'checkpoint33_member_repair';OUT.mkdir(exist_ok=True)
sha=lambda p:hashlib.file_digest(p.open('rb'),'sha256').hexdigest()
mp=BASE/'checkpoint33_encoding/checkpoint33_transport_manifest.json';m=json.loads(mp.read_text());ip=BASE/'checkpoint33_member_index/result.json';index=json.loads(ip.read_text());assert index['status']=='PASS_COMPLETE_NONDICTIONARY_MEMBER_HASHES'and index['manifest_sha256']==sha(mp)
pp=BASE/'checkpoint33_png_rows_candidate/object_transforms.json';png=json.loads(pp.read_text())
zp=BASE/'checkpoint33_zlib_complete_candidate/result.json'
while not zp.exists():time.sleep(10)
z=json.loads(zp.read_text());assert z['status']=='PASS_ALL_ORIGINAL_MEMBERS_AND_INDEPENDENT_BUNDLE_DECODE'
jp=ROOT/'records/checkpoint33_json_copy_candidates.json';j=json.loads(jp.read_text());assert j['status']=='PASS_ALL_FOUR_EXACT_FROZEN_JSON_PATCHES'
prows=png['object_transforms']if'object_transforms'in png else png['objects']
assert isinstance(prows,list)
rows=prows+z['object_transforms'];removed={r['original_name']:{'bytes':r['original_bytes'],'sha256':r['original_sha256'],'replacement':'member_codec'}for r in rows}
for r in j['objects']:
 assert r['raw_member_name']not in removed;removed[r['raw_member_name']]={'bytes':r['target_bytes'],'sha256':r['target_sha256'],'replacement':'copy_add'}
records=[];all_removed=set();start=time.time()
for bidx,b in enumerate(index['bundle_records']):
 old=b['bundle'];members=b['members'];names={r['name']for r in members};drop=names&removed.keys()
 if not drop:continue
 for r in members:
  if r['name']in drop:assert r['bytes']==removed[r['name']]['bytes']and r['sha256']==removed[r['name']]['sha256']
 keep=[r for r in members if r['name']not in drop];candidate=OUT/f'checkpoint33_residual_{bidx:04d}.tar.xz';receipt=candidate.with_suffix(candidate.suffix+'.json')
 if receipt.exists():
  rec=json.loads(receipt.read_text());assert rec['original']==old and rec['retained_members']==keep and rec['removed_members']==sorted(drop)
  if keep:assert candidate.stat().st_size==rec['candidate']['bytes']and sha(candidate)==rec['candidate']['sha256']
  records.append(rec);all_removed.update(drop);continue
 original=Path(b['local_path']);assert original.stat().st_size==old['bytes']and sha(original)==old['sha256']
 if keep:
  expected={r['name']:r for r in members};seen=[]
  with lzma.open(original,'rb')as src,tarfile.open(fileobj=src,mode='r|')as tin,lzma.open(candidate,'xb',filters=[{'id':lzma.FILTER_LZMA2,'preset':6,'dict_size':64*1024*1024}])as dest,tarfile.open(fileobj=dest,mode='w|')as tout:
   for member in tin:
    assert member.name in expected and member.size==expected[member.name]['bytes'];f=tin.extractfile(member)
    if member.name not in drop:tout.addfile(member,f)
    f.close();seen.append(member.name)
  assert set(seen)==set(expected)
  check=[]
  with lzma.open(candidate,'rb')as src,tarfile.open(fileobj=src,mode='r|')as tar:
   for member in tar:
    f=tar.extractfile(member)
    with f:digest=hashlib.file_digest(f,'sha256').hexdigest()
    check.append({'name':member.name,'bytes':member.size,'sha256':digest})
  assert check==keep
  selected={'file':candidate.name,'local_path':str(candidate),'bytes':candidate.stat().st_size,'sha256':sha(candidate),'members':len(keep)}
 else:selected=None
 rec={'status':'PASS_EXACT_RETAINED_MEMBERS','original':old,'original_path':str(original),'candidate':selected,'retained_members':keep,'removed_members':sorted(drop),'removed_bytes':sum(removed[n]['bytes']for n in drop),'scope':'Every removed member has an independently verified inverse codec/patch; every retained original member is byte-hash identical in the residual TAR.'}
 receipt.write_text(json.dumps(rec,indent=2)+'\n');records.append(rec);all_removed.update(drop);print(json.dumps({'status':rec['status'],'bundle':old['file'],'old_bytes':old['bytes'],'retained_members':len(keep),'residual_bytes':selected['bytes']if selected else 0}),flush=True)
assert all_removed==set(removed),(set(removed)-all_removed)
# The four existing-decoder JSON patches are a separate tiny delivered bundle.
patchbundle=OUT/'checkpoint33_json_patches.tar.xz'
with lzma.open(patchbundle,'xb',filters=[{'id':lzma.FILTER_LZMA2,'preset':6,'dict_size':64*1024*1024}])as sink,tarfile.open(fileobj=sink,mode='w|')as tar:
 for r in j['objects']:
  p=Path(r['patch_local_path']);assert sha(p)==r['patch_sha256']and p.stat().st_size==r['patch_bytes'];info=tarfile.TarInfo(r['proposed_content']['patch_name']);info.size=p.stat().st_size;info.mtime=0;info.mode=420
  with p.open('rb')as f:tar.addfile(info,f)
res={'status':'PASS_COMPLETE_EXACT_MEMBER_SUBSTITUTIONS','manifest_sha256':sha(mp),'frozen_manifest_sha256':sha(BASE/'checkpoint33_encoding/frozen_manifest.json'),'input_receipts':{str(p):sha(p)for p in [ip,pp,zp,jp]},'substitutions':removed,'residuals':records,'json_patch_bundle':{'file':patchbundle.name,'local_path':str(patchbundle),'bytes':patchbundle.stat().st_size,'sha256':sha(patchbundle),'members':len(j['objects'])},'program_sha256':sha(Path(__file__)),'seconds':time.time()-start};(OUT/'result.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps({'status':res['status'],'changed_bundles':len(records),'replaced_members':len(removed),'removed_bundle_bytes':sum(r['original']['bytes']for r in records),'residual_bundle_bytes':sum(r['candidate']['bytes']if r['candidate']else 0 for r in records),'seconds':res['seconds']}),flush=True)
