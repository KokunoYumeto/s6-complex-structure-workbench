"""Read-only frozen33 JSON copy/add measurement with exact decoder proof.

Candidate objects are separate; no live manifest, bundle, or source changes.
The sparse anchor encoder emits the existing standard-library format.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,lzma,struct,sys,time

ROOT=Path(__file__).resolve().parents[2];BASE=ROOT.parent
sys.path.insert(0,str(ROOT/'code'))
from checkpoint_copy_add import MAGIC,decode
STAGE=BASE/'checkpoint33_json_copy_candidates';STAGE.mkdir(exist_ok=True)
MANIFEST=BASE/'checkpoint33_encoding/checkpoint33_transport_manifest.json'
FROZEN=BASE/'checkpoint33_encoding/frozen'
m=json.loads(MANIFEST.read_text())

def sha_bytes(b):return hashlib.sha256(b).hexdigest()
def sha(p):
    with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def common(a,b,ia,ib):
    n=min(len(a)-ia,len(b)-ib);length=0;block=65536
    while length+block<=n and a[ia+length:ia+length+block]==b[ib+length:ib+length+block]:length+=block
    low,high=0,min(block,n-length)
    while low<high:
        mid=(low+high+1)//2
        if a[ia+length:ia+length+mid]==b[ib+length:ib+length+mid]:low=mid
        else:high=mid-1
    return length+low

def sparse_encode(base,target):
    block=64;stride=1024;index={}
    for p in range(0,len(base)-block+1,stride):
        hits=index.setdefault(base[p:p+block],[])
        if len(hits)<16:hits.append(p)
    out=bytearray(MAGIC+hashlib.sha256(base).digest()+struct.pack('>Q',len(target)))
    cursor=literal=0;copies=[]
    prefix=common(base,target,0,0)
    if prefix>=64:
        out+=b'C'+struct.pack('>QQ',0,prefix);copies.append((0,0,prefix));cursor=literal=prefix
    while cursor+block<=len(target):
        pos=amount=0
        for candidate in index.get(target[cursor:cursor+block],[]):
            length=common(base,target,candidate,cursor)
            if length>amount:pos,amount=candidate,length
        if amount<128:cursor+=1;continue
        if literal<cursor:
            data=target[literal:cursor];out+=b'L'+struct.pack('>Q',len(data))+data
        out+=b'C'+struct.pack('>QQ',pos,amount);copies.append((pos,cursor,amount))
        cursor+=amount;literal=cursor
    if literal<len(target):
        data=target[literal:];out+=b'L'+struct.pack('>Q',len(data))+data
    return bytes(out),copies

pairs=[
 ('code/part3/e6_order_three_m2_fixed_curve_normals.json',
  'records/attempts/e6_m2_curve_mcv4_comma/e6_order_three_m2_fixed_curve_normals.json'),
 ('code/part3/e6_selected_i3_fixed_curve_normals.json',
  'records/attempts/e6_selected_i3_curves_initial_proof_lock/e6_selected_i3_fixed_curve_normals.json'),
 ('code/part3/e6_selected_i3_common_fan.json',
  'records/attempts/e6_selected_i3_common_output_fraction/e6_selected_i3_common_fan.json'),
 ('code/part3_root/e6_order_three_m2_corner_lifts.json',
  'records/attempts/e6_order_three_m2_corner_volume_sign/e6_order_three_m2_corner_lifts.json')]
rows=[];start=time.monotonic()
for current,old in pairs:
    cn='S6_06_BLIND/'+current;bn='S6_06_BLIND/'+old
    target=(FROZEN/cn).read_bytes();base=(FROZEN/bn).read_bytes()
    ch,bh=sha_bytes(target),sha_bytes(base)
    assert ch==m['files'][cn]['sha256'] and bh==m['files'][bn]['sha256']
    assert m['contents'][ch]['storage']=='raw' and m['contents'][bh]['storage']=='raw'
    patch,copies=sparse_encode(base,target)
    decoded=decode(base,patch)
    assert decoded==target and sha_bytes(decoded)==ch
    pp=STAGE/(ch+'.copyadd');pp.write_bytes(patch)
    # Per-object estimates use identical compression parameters. Their sum
    # is deliberately not claimed as an actual whole-TAR saving.
    filters=[{'id':lzma.FILTER_LZMA2,'preset':6,'dict_size':16*1024*1024}]
    raw_xz=STAGE/(ch+'.raw.xz');patch_xz=STAGE/(ch+'.patch.xz')
    with lzma.open(raw_xz,'wb',filters=filters) as f:f.write(target)
    with lzma.open(patch_xz,'wb',filters=filters) as f:f.write(patch)
    assert lzma.decompress(raw_xz.read_bytes())==target
    assert lzma.decompress(patch_xz.read_bytes())==patch
    row={'target_file':cn,'base_file':bn,'target_sha256':ch,'base_sha256':bh,
         'target_bytes':len(target),'base_bytes':len(base),
         'patch_local_path':str(pp),'patch_sha256':sha(pp),'patch_bytes':len(patch),
         'copies':len(copies),'copy_bytes':sum(c[2] for c in copies),
         'literal_bytes':len(target)-sum(c[2] for c in copies),
         'copy_spans':copies,'raw_member_name':m['contents'][ch]['name'],
         'standalone_raw_xz_bytes':raw_xz.stat().st_size,
         'standalone_patch_xz_bytes':patch_xz.stat().st_size,
         'standalone_compressed_saved_bytes':raw_xz.stat().st_size-patch_xz.stat().st_size,
         'proposed_content':{'bytes':len(target),'storage':'copy_add','base_sha256':bh,
                            'patch_name':'patches/'+ch,'patch_sha256':sha(pp)},
         'exact_existing_decoder_pass':True}
    rows.append(row)
    print(json.dumps({k:v for k,v in row.items() if k not in {'copy_spans','proposed_content'}}),flush=True)
    del target,base,decoded,patch

record={'status':'PASS_ALL_FOUR_EXACT_FROZEN_JSON_PATCHES','utc':datetime.now(timezone.utc).isoformat(),
        'manifest':str(MANIFEST),'manifest_sha256':sha(MANIFEST),
        'frozen_tree':str(FROZEN),'objects':rows,
        'total_target_bytes':sum(r['target_bytes'] for r in rows),
        'total_patch_bytes':sum(r['patch_bytes'] for r in rows),
        'standalone_compressed_saved_bytes':sum(r['standalone_compressed_saved_bytes'] for r in rows),
        'measurement_scope':'Independent per-object XZ measurement. Full residual TAR saving must be measured by the reassembly owner before selection. All original target and base bytes remain untouched.',
        'decoder':'code/checkpoint_copy_add.py','decoder_sha256':sha(ROOT/'code/checkpoint_copy_add.py'),
        'program_sha256':sha(__file__),'seconds':time.monotonic()-start,
        'live_manifest_modified':False,'live_bundles_modified':False}
rp=ROOT/'records/checkpoint33_json_copy_candidates.json'
rp.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k!='objects'},indent=2),flush=True)
