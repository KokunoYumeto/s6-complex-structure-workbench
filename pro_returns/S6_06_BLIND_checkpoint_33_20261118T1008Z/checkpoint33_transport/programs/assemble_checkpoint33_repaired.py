"""Assemble independently verified member substitutions for immutable33.

This program changes only transport representations. Every frozen file entry,
every predecessor content identity, and every inherited decoder is retained.
"""
from pathlib import Path
from datetime import datetime, timezone
import copy, hashlib, json, shutil, sys, time, zipfile

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parent
OLD=BASE/'checkpoint33_encoding'
OUT=BASE/'checkpoint33_final_encoding'
OUT.mkdir(exist_ok=True)
def sha(p):
    with p.open('rb') as f: return hashlib.file_digest(f,'sha256').hexdigest()
def read(p): return json.loads(p.read_text())
def verified(p,n,h):
    assert p.stat().st_size==n and sha(p)==h,(str(p),n,h)
def dump(p,d):
    q=p.with_suffix(p.suffix+'.pending');q.write_text(json.dumps(d,indent=2)+'\n');q.replace(p)

original_manifest=OLD/'checkpoint33_transport_manifest.json'
assert sha(original_manifest)=='35494e4332a53f533e24f9993043b2107cffd808bf1ea4b7eca03b0e7c19b2fb'
m=read(original_manifest); inherited=copy.deepcopy(m)
freeze=OLD/'frozen_manifest.json'
assert sha(freeze)=='6db797412be4473f5410a8b56332660cab057dc5def4f1ac7c017898101906e7'
assert m['files']==read(freeze)['files'] and len(m['files'])==14467
rp=BASE/'checkpoint33_member_repair/result.json'
r=read(rp);assert r['status']=='PASS_COMPLETE_EXACT_MEMBER_SUBSTITUTIONS'
assert r['manifest_sha256']==sha(original_manifest) and r['frozen_manifest_sha256']==sha(freeze)
pp=BASE/'checkpoint33_png_rows_candidate/object_transforms.json';p=read(pp)
zp=BASE/'checkpoint33_zlib_complete_candidate/result.json';z=read(zp)
jp=ROOT/'records/checkpoint33_json_copy_candidates.json';j=read(jp)
ip=BASE/'checkpoint33_member_index/result.json';idx=read(ip)
assert p['status']=='PASS_ALL_NEW_PNG_MEMBER_AND_ARCHIVE_BYTES'
assert z['status']=='PASS_ALL_ORIGINAL_MEMBERS_AND_INDEPENDENT_BUNDLE_DECODE'
assert j['status']=='PASS_ALL_FOUR_EXACT_FROZEN_JSON_PATCHES'
assert all(sha(Path(path))==h for path,h in r['input_receipts'].items())
changes={x['original']['file']:x for x in r['residuals']}
local={x['bundle']['file']:Path(x['local_path']) for x in idx['bundle_records']}
dictionary=m['dictionary_representation']['candidate']['file']
local[dictionary]=BASE/'checkpoint32_png_repack/bundles'/dictionary
new_bundles=[];paths={};recompressions=[]
rgb_path=BASE/'checkpoint33_dictionary_rgb_complete/result.json'
rgb=None
if rgb_path.exists():
    rgb=read(rgb_path)
    assert rgb['status']=='PASS_COMPLETE_ORIGINAL_DICTIONARY_AND_ALL_RETAINED_MEMBERS'
    assert rgb['saving']>0
choices={}
for q in [BASE/'checkpoint33_new_repack/new_repack_manifest.json',BASE/'checkpoint33_extra_repack/extra_repack_manifest.json']:
    if q.exists():
        a=read(q)
        for name,v in a['entries'].items():
            if v['use_candidate'] and v['saving']>0:choices[name]=(q,v)
for b in m['bundles']:
    name=b['file'];src=local[name];verified(src,b['bytes'],b['sha256'])
    if name in changes:
        c=changes[name];assert c['original']==b
        if c['candidate'] is None:continue
        b=dict(c['candidate']);src=Path(b.pop('local_path'))
    elif rgb is not None and name==dictionary:
        assert b['bytes']==rgb['original_bundle']['bytes'] and b['sha256']==rgb['original_bundle']['sha256']
        b=dict(rgb['bundle']);src=Path(b.pop('local_path'))
    elif name in choices:
        q,v=choices[name];assert v['original']==b and v['status']=='PASS_IDENTICAL_UNCOMPRESSED_TAR'
        src=q.parent/v['candidate_file'];b=dict(v['bundle']);recompressions.append(v)
    verified(src,b['bytes'],b['sha256']);new_bundles.append(b);paths[b['file']]=src
for b0 in [p['bundle'],z['bundle'],r['json_patch_bundle']]:
    b=dict(b0);src=Path(b.pop('local_path'));verified(src,b['bytes'],b['sha256'])
    assert b['file'] not in paths;new_bundles.append(b);paths[b['file']]=src

# A larger-window candidate is used only after its complete decoded-TAR proof.
outer=BASE/'checkpoint33_dictionary_window_candidate/result.json'
if outer.exists():
    d=read(outer)
    if d.get('status')=='PASS_IDENTICAL_COMPLETE_TAR' and d['candidate']['bytes']<d['original']['bytes']:
        raise RuntimeError('Read the final dictionary receipt schema before selecting it.')

m['bundles']=new_bundles
m['object_transforms']=inherited['object_transforms']+p['objects']+z['object_transforms']
if rgb is not None:
    m['object_transforms'].append(rgb['object_transform'])
    codec=ROOT/'code/checkpoint_png_rgb_dictionary.py'
    assert sha(codec)==rgb['codec_sha256']
    m['transport_support_files'].append({'file':codec.name,'bytes':codec.stat().st_size,'sha256':sha(codec)})
    m['checkpoint33_dictionary_outer_representation']={
        'status':'PASS_EXACT_ORIGINAL_DICTIONARY_AND_INDEX_MEMBERS',
        'receipt_sha256':sha(rgb_path),'original_bundle':rgb['original_bundle'],
        'selected_bundle':rgb['bundle'],'original_dictionary_sha256':rgb['object_transform']['original_sha256'],
        'scope':'An additional reversible byte-plane layer reconstructs the identical original dictionary before every unchanged inherited PNG-row decoder. Original row indices, all inherited representation records, and the immutable32 ZIP remain unchanged.'}
assert m['object_transforms'][:len(inherited['object_transforms'])]==inherited['object_transforms']
for row in j['objects']:
    h=row['target_sha256'];assert inherited['contents'][h]['storage']=='raw'
    assert m['contents'][row['base_sha256']]['bytes']==row['base_bytes']
    m['contents'][h]=row['proposed_content'];assert h not in m['patch_order'];m['patch_order'].append(h)
assert m['predecessor_files']==inherited['predecessor_files']
for h,c in inherited['contents'].items():assert m['contents'][h]['bytes']==c['bytes']
assert m['files']==inherited['files'] and m['dictionary_representation']==inherited['dictionary_representation']
assert m['inherited_transport_repairs']==inherited['inherited_transport_repairs']
assert m['transport_support_files'][:len(inherited['transport_support_files'])]==inherited['transport_support_files']
dict_groups=[rgb['bundle']['file']if rgb is not None else dictionary,p['bundle']['file']]
m['restore_bundle_order']=dict_groups+[b['file'] for b in new_bundles if b['file'] not in dict_groups]
m['checkpoint33_exact_member_repair']={
    'status':'PASS_INDIVIDUAL_ORIGINAL_MEMBER_BYTES_AND_RESIDUAL_STREAMS',
    'original_manifest_sha256':sha(original_manifest),'frozen_manifest_sha256':sha(freeze),
    'receipt_sha256':{str(q):sha(q) for q in [rp,pp,zp,jp,ip]},
    'new_png_objects':len(p['objects']),'new_zlib_objects':len(z['object_transforms']),
    'new_copy_add_objects':len(j['objects']),
    'scope':'Every original member reconstructs byte-for-byte through delivered unchanged codecs; each retained residual member was independently rehashed. The complete standalone restore remains a separate gate.'}
manifest=OUT/'checkpoint33_transport_manifest.json';dump(manifest,m)
restore=OUT/'restore_checkpoint.py'
code=(ROOT/'code/restore_checkpoint33_streamed.py').read_text()
# Only codecs actually present are delivered. No unused experimental decoder.
unused="""    elif row['codec']=='stream_copy_v1':
     from checkpoint_stream_copy import decode_stream
     with packed.open('rb')as stream:decode_stream(stream,original)
"""
assert unused in code;code=code.replace(unused,'');compile(code,str(restore),'exec');restore.write_text(code)
for s in m['transport_support_files']:
    src=(ROOT/'code'/s['file'])if s['file']=='checkpoint_png_rgb_dictionary.py'else OLD/s['file']
    verified(src,s['bytes'],s['sha256']);shutil.copyfile(src,OUT/s['file'])
candidate=OUT/'checkpoint33_repaired.partial'
if candidate.exists():candidate.rename(OUT/f'checkpoint33_preserved_{time.time_ns()}.zip')
receipts=[rp,pp,zp,jp,ip]
if rgb is not None:receipts.append(rgb_path)
programs=[Path(__file__),ROOT/'code/restore_checkpoint33_streamed.py',ROOT/'code/checkpoint33_repair_residuals.py',ROOT/'code/checkpoint33_png_rows_candidate.py',ROOT/'code/checkpoint33_zlib_complete_candidate.py',ROOT/'code/part3_fourfold/checkpoint33_json_copy_candidates.py']
if rgb is not None:programs.append(ROOT/'code/checkpoint33_dictionary_rgb_complete.py')
readme=f'''# Complete immutable checkpoint33\n\nExtract this ZIP and run `python3 restore_checkpoint.py`. All {len(m['files']):,} frozen files and retained predecessor content objects are reconstructed and checked against their exact original size and SHA-256. Every required bundle and decoder is included; no earlier checkpoint is needed.\n\nThe current paper/registers are directly readable. Exact PNG-row, zlib-object, historical PDF copy/add, and four additional JSON copy/add representations preserve original bytes. All old dictionary bytes, row indices, transform entries and support modules remain unchanged. Additional row IDs use a separate dictionary. The restorer consumes closed dependency groups and releases only verified temporary codec objects. Standard-library LZMA requires at most64MiB for the selected bundles.\n\nThe complete freeze, predecessor representation and every new proof receipt are retained under checkpoint33_transport. Full proofs, code, data, failed attempts and rendered pages are retained in the frozen project. The report remains INCOMPLETE.\n'''
with zipfile.ZipFile(candidate,'x',zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
    for name in m['direct_files']:
        src=OLD/'frozen'/name;v=m['files'][name];verified(src,v['bytes'],v['sha256']);archive.write(src,name)
    for b in new_bundles:archive.write(paths[b['file']],b['file'],compress_type=zipfile.ZIP_STORED)
    archive.write(manifest,manifest.name,compress_type=zipfile.ZIP_LZMA)
    archive.write(restore,'restore_checkpoint.py')
    for s in m['transport_support_files']:archive.write(OUT/s['file'],s['file'])
    archive.write(original_manifest,'checkpoint33_transport/original_transport_manifest.json',compress_type=zipfile.ZIP_LZMA)
    for name in ['freeze_initial.json','freeze_journal.jsonl','frozen_manifest.json']:
        archive.write(OLD/name,'checkpoint33_transport/'+name,compress_type=zipfile.ZIP_LZMA)
    for q in receipts:archive.write(q,'checkpoint33_transport/'+q.parent.name+'_'+q.name,compress_type=zipfile.ZIP_LZMA)
    for q in programs:archive.write(q,'checkpoint33_transport/programs/'+q.name)
    archive.writestr('READ_FIRST.md',readme)
size=candidate.stat().st_size;digest=sha(candidate)
record={'status':'MEASURED_COMPLETE_REPAIRED_ARCHIVE','path':str(candidate),'bytes':size,'sha256':digest,'size_limit':536870912,'over_limit_bytes':max(0,size-536870912),'snapshot_files':len(m['files']),'frozen_manifest_sha256':sha(freeze),'manifest_sha256':sha(manifest),'bundle_bytes':sum(b['bytes'] for b in new_bundles),'bundles':len(new_bundles),'selected_original_tar_recompressions':recompressions,'bundle_paths':{n:str(p) for n,p in paths.items()},'utc':datetime.now(timezone.utc).isoformat(),'full_restore_pending':True}
if size>536870912:
    q=OUT/f'checkpoint33_repaired_oversize_{time.time_ns()}.zip';candidate.rename(q);record['path']=str(q)
else:
    q=OUT/'checkpoint33_repaired_candidate.zip';assert not q.exists();candidate.rename(q);record['path']=str(q)
dump(OUT/'checkpoint33_measurement.json',record)
print(json.dumps({k:v for k,v in record.items() if k not in ['bundle_paths','selected_original_tar_recompressions']},indent=2),flush=True)
