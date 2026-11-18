"""Select a fully verified exact dictionary representation for checkpoint35.

The complete preserved oversize ZIP is the input. Only its selected original
dictionary bundle, one transform, the corresponding stream dispatcher and
the added decoder/provenance entries change. Every other member is copied
and independently rehashed byte for byte. The frozen research manifest,
content table, original dictionary and all original PNG row indices remain.
"""
from pathlib import Path
from datetime import datetime, timezone
import copy, hashlib, json, shutil, time, zipfile
from checkpoint_constant_planes_view_restore_patch import patch

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT.parent
STAGE = BASE/'checkpoint35_encoding'
TARGET = BASE/'S6_06_BLIND_checkpoint_35.zip'
LIMIT = 536870912

def sha(path):
    with Path(path).open('rb') as source:
        return hashlib.file_digest(source, 'sha256').hexdigest()

def identity(path):
    path = Path(path)
    return {'bytes': path.stat().st_size, 'sha256': sha(path)}

def atomic_json(path, value):
    temporary = path.with_suffix(path.suffix+'.pending')
    temporary.write_text(json.dumps(value, indent=2)+'\n')
    temporary.replace(path)

def bytes_identity(value):
    return {'bytes': len(value), 'sha256': hashlib.sha256(value).hexdigest()}

assert not TARGET.exists(), 'A completed archive must remain immutable'
view_checks_path=ROOT/'records/checkpoint35_dictionary_view_checks.json'
view_checks=json.loads(view_checks_path.read_text())
assert view_checks['status']=='PASS'
for name,digest in view_checks['source_locks'].items():assert sha(ROOT/name)==digest
view_audit_path=ROOT/'records/root_audit_checkpoint35_dictionary_view.json'
view_audit=json.loads(view_audit_path.read_text())
assert str(view_audit['status']).startswith('PASS')
for lock in view_audit['source_locks']:
    assert identity(ROOT/lock['path'])=={k:lock[k] for k in ('bytes','sha256')}

result_path = BASE/'checkpoint35_constant_planes_complete/result.json'
result = json.loads(result_path.read_text())
assert result['status'] == 'PASS_FULL_CONSTANT_PLANES_AND_ORIGINAL_DICTIONARY'
assert result['selected'] is False and result['live_manifest_modified'] is False
assert result['original_row_order_and_indices_unchanged'] is True
assert result['filters'] == [{'id': 33, 'preset': 6, 'dict_size': 67108864}]
candidate = Path(result['bundle']['local_path'])
assert identity(candidate) == {k: result['bundle'][k] for k in ('bytes','sha256')}
old_bundle = result['original_bundle']
assert identity(old_bundle['local_path']) == {k: old_bundle[k] for k in ('bytes','sha256')}
assert result['saving'] == old_bundle['bytes']-result['bundle']['bytes'] > 0
assert sha(ROOT/'code/checkpoint_rgb_constant_planes_codec.py') == result['codec_sha256']
assert sha(ROOT/'code/checkpoint_png_rgb_dictionary.py') == result['prior_rgb_codec_sha256']
assert sha(ROOT/'code/checkpoint35_constant_planes_complete.py') == result['program_sha256']

audit_path = ROOT/'records/root_audit_checkpoint35_constant_planes_format.json'
audit = json.loads(audit_path.read_text())
assert audit['status'] == 'PASS_FULL_FORMAT_AND_INVERSE_READING_PENDING_COMPLETE_CANDIDATE'
for lock in audit['source_locks']:
    assert identity(ROOT/lock['path']) == {k: lock[k] for k in ('bytes','sha256')}

measurement = json.loads((STAGE/'checkpoint35_size_measurement.json').read_text())
original_zip = Path(measurement['preserved_oversize_candidate'])
assert original_zip.stat().st_size == measurement['candidate_archive_bytes'] == 555944571
original_zip_sha = sha(original_zip)
frozen_path = STAGE/'frozen_manifest.json'
assert sha(frozen_path) == measurement['frozen_manifest_sha256']
freeze = json.loads(frozen_path.read_text())
assert len(freeze['files']) == 15682 and freeze['snapshot']['checkpoint'] == 35

with zipfile.ZipFile(original_zip) as source_zip:
    prior_manifest_bytes = source_zip.read('checkpoint35_transport_manifest.json')
    prior_restore_bytes = source_zip.read('restore_checkpoint.py')
    prior = json.loads(prior_manifest_bytes)
    assert prior['files'] == freeze['files'] and prior['snapshot'] == freeze['snapshot']
    assert prior_manifest_bytes == (STAGE/'checkpoint35_transport_manifest.json').read_bytes()
    assert prior_restore_bytes == (STAGE/'restore_checkpoint.py').read_bytes()
    info = source_zip.getinfo(old_bundle['file'])
    assert info.file_size == old_bundle['bytes']
    with source_zip.open(info) as original_dictionary_member:
        assert hashlib.file_digest(original_dictionary_member,'sha256').hexdigest()==old_bundle['sha256']

manifest = copy.deepcopy(prior)
old_matches = [i for i, item in enumerate(prior['bundles']) if item['file']==old_bundle['file']]
assert len(old_matches) == 1
index = old_matches[0]
assert all(prior['bundles'][index][k] == old_bundle[k] for k in ('file','bytes','sha256'))
manifest['bundles'][index] = {k: result['bundle'][k] for k in ('file','bytes','sha256','members')}
old_transform_matches = [i for i, row in enumerate(prior['object_transforms'])
                         if row['codec']=='png_rgb_dictionary_v1'
                         and row['original_name']==result['object_transform']['original_name']]
assert len(old_transform_matches) == 1
transform_index = old_transform_matches[0]
old_transform = prior['object_transforms'][transform_index]
new_transform = result['object_transform']
for key in ('original_name','original_bytes','original_sha256','rows'):
    assert old_transform[key] == new_transform[key]
for before, after in [('encoded_name','prior_rgb_name'),('encoded_bytes','prior_rgb_bytes'),('encoded_sha256','prior_rgb_sha256')]:
    assert old_transform[before] == new_transform[after]
manifest['object_transforms'][transform_index] = new_transform
codec = ROOT/'code/checkpoint_rgb_constant_planes_codec.py'
codec_entry = {'file': codec.name, **identity(codec)}
assert codec_entry['file'] not in {row['file'] for row in prior['transport_support_files']}
manifest['transport_support_files'].append(codec_entry)
view_codec=ROOT/'code/checkpoint_constant_planes_dictionary_view.py'
view_entry={'file':view_codec.name,**identity(view_codec)}
assert view_entry['file'] not in {row['file'] for row in prior['transport_support_files']}
manifest['transport_support_files'].append(view_entry)
manifest['restore_bundle_order'] = [result['bundle']['file'] if name==old_bundle['file'] else name
                                    for name in prior['restore_bundle_order']]
assert len(set(manifest['restore_bundle_order'])) == len(manifest['bundles'])
assert manifest['restore_bundle_order'][0] == result['bundle']['file']
representation = {
    'status':'PASS_FULL_CONSTANT_PLANES_AND_ORIGINAL_DICTIONARY',
    'receipt_sha256':sha(result_path), 'root_format_audit_sha256':sha(audit_path),
    'previous_bundle':old_bundle, 'selected_bundle':manifest['bundles'][index],
    'previous_transform':old_transform, 'selected_transform':new_transform,
    'original_dictionary_sha256':new_transform['original_sha256'],
    'original_row_order_and_indices_unchanged':True,
    'scope':'Exact constant-plane inverse, then the unchanged RGB-plane inverse, restores the original dictionary bytes before every inherited PNG-row decoder. All original research bytes, row indices and prior representation metadata are retained.'}
manifest['checkpoint35_dictionary_constant_planes_representation'] = representation
manifest['checkpoint35_dictionary_access']={
 'status':'PASS_EXACT_ROW_VIEW_WITH_COMPLETE_DICTIONARY_VERIFICATION',
 'decoder':view_entry,'restorer_patch_sha256':sha(ROOT/'code/checkpoint_constant_planes_view_restore_patch.py'),
 'checks_sha256':sha(view_checks_path),'root_audit_sha256':sha(view_audit_path),
 'original_dictionary_bytes':new_transform['original_bytes'],
 'encoded_view_bytes':new_transform['encoded_bytes'],
 'original_row_order_and_indices_unchanged':True,
 'scope':'Before the first PNG row access the entire encoded, intermediate RGB and original dictionary identities pass; original row IDs then use the same two exact row inverses. The encoded temporary file is closed and removed after its last dependent row object.'}
for field in ('files','contents','patch_order','direct_files','predecessor_files',
              'inherited_transport_repairs','dictionary_representation',
              'checkpoint33_exact_member_repair','checkpoint33_dictionary_outer_representation'):
    assert manifest.get(field) == prior.get(field)
assert manifest['transport_support_files'][:-2] == prior['transport_support_files']
assert [row for i,row in enumerate(manifest['object_transforms']) if i!=transform_index] == [row for i,row in enumerate(prior['object_transforms']) if i!=transform_index]

restore = patch(prior_restore_bytes.decode()).encode()
manifest_bytes = (json.dumps(manifest,indent=2)+'\n').encode()
selection = {'status':'CANDIDATE_SELECTION_COMPLETE_RESTORE_PENDING',
             'utc':datetime.now(timezone.utc).isoformat(),
             'frozen_manifest_sha256':sha(frozen_path),
             'preserved_original_zip':str(original_zip),
             'preserved_original_zip_bytes':original_zip.stat().st_size,
             'preserved_original_zip_sha256':original_zip_sha,
             'previous_manifest':bytes_identity(prior_manifest_bytes),
             'selected_manifest':bytes_identity(manifest_bytes),
             'previous_restorer':bytes_identity(prior_restore_bytes),
             'selected_restorer':bytes_identity(restore),
             'dictionary_representation':representation,
             'selector_sha256':sha(__file__),
             'patcher_sha256':sha(ROOT/'code/checkpoint_constant_planes_view_restore_patch.py'),
             'preserved_prior_selector_sha256':sha(ROOT/'code/make_checkpoint35_constant_planes.py'),
             'dictionary_access':manifest['checkpoint35_dictionary_access'],
             'candidate_full_inverse_status':result['status'],
             'snapshot_files':len(freeze['files'])}
replacement = {'checkpoint35_transport_manifest.json':manifest_bytes,
               'restore_checkpoint.py':restore}
added_bytes = {
    'checkpoint35_transport/pre_constant_planes_transport_manifest.json':prior_manifest_bytes,
    'checkpoint35_transport/pre_constant_planes_restore.py':prior_restore_bytes,
    'checkpoint35_transport/constant_planes_selection.json':(json.dumps(selection,indent=2)+'\n').encode()}
added_files = {
    codec.name:codec,
    view_codec.name:view_codec,
    'checkpoint35_transport/make_checkpoint35_constant_planes_view.py':Path(__file__),
    'checkpoint35_transport/preserved_reviewed_constant_planes_selector.py':ROOT/'code/make_checkpoint35_constant_planes.py',
    'checkpoint35_transport/checkpoint_constant_planes_view_restore_patch.py':ROOT/'code/checkpoint_constant_planes_view_restore_patch.py',
    'checkpoint35_transport/constant_planes_dictionary_view.md':ROOT/'notes/checkpoint35_constant_planes_dictionary_view.md',
    'checkpoint35_transport/dictionary_view_checks.json':view_checks_path,
    'checkpoint35_transport/dictionary_view_checks.py':ROOT/'code/checkpoint35_dictionary_view_checks.py',
    'checkpoint35_transport/root_dictionary_view_audit.json':view_audit_path,
    'checkpoint35_transport/checkpoint_constant_planes_restore_patch.py':ROOT/'code/checkpoint_constant_planes_restore_patch.py',
    'checkpoint35_transport/checkpoint35_constant_planes_complete.py':ROOT/'code/checkpoint35_constant_planes_complete.py',
    'checkpoint35_transport/constant_planes_complete_result.json':result_path,
    'checkpoint35_transport/constant_planes_format.md':ROOT/'notes/checkpoint35_constant_planes_format.md',
    'checkpoint35_transport/root_constant_planes_format_audit.json':audit_path,
    'checkpoint35_transport/constant_planes_stream_fixtures.json':ROOT/'records/checkpoint35_constant_planes_stream_fixtures.json'}
partial = STAGE/'checkpoint35.constant_planes_view.partial'
if partial.exists():
    partial.rename(STAGE/('checkpoint35.constant_planes.interrupted_'+str(time.time_ns())))
copied = {}
with zipfile.ZipFile(original_zip) as source_zip, zipfile.ZipFile(partial,'x',zipfile.ZIP_DEFLATED,compresslevel=9) as target_zip:
    original_names = {item.filename for item in source_zip.infolist()}
    assert len(original_names) == len(source_zip.infolist())
    assert not original_names.intersection(added_bytes) and not original_names.intersection(added_files)
    for item in source_zip.infolist():
        name = item.filename
        if name == old_bundle['file']:
            target_zip.write(candidate,candidate.name,compress_type=zipfile.ZIP_STORED)
        elif name in replacement:
            target_zip.writestr(name,replacement[name],compress_type=item.compress_type)
        elif name == 'READ_FIRST.md':
            original_readme = source_zip.read(name)
            extra = b'\nThe checkpoint35 selected dictionary adds an exact constant-plane representation before the inherited RGB inverse. The original row dictionary, indices and every original research byte are unchanged. The previous manifest and restorer, both complete forward/inverse programs, the independent format audit and the full closed-stream inverse result are retained under checkpoint35_transport. The delivered restorer checks the entire encoded, intermediate RGB and original dictionary streams before any PNG access, then retains only the verified encoded dictionary as its temporary row view. Every unchanged original row ID is reconstructed by the same two inverses; descriptors and caches close before the temporary view is removed.\n'
            replacement[name] = original_readme+extra
            target_zip.writestr(name,replacement[name],compress_type=item.compress_type)
            added_bytes['checkpoint35_transport/pre_constant_planes_READ_FIRST.md'] = original_readme
        else:
            h=hashlib.sha256();amount=0
            with source_zip.open(item) as source, target_zip.open(copy.copy(item),'w') as target:
                while block:=source.read(1024*1024):
                    target.write(block);h.update(block);amount+=len(block)
            assert amount==item.file_size
            copied[name]={'bytes':amount,'sha256':h.hexdigest()}
    for name,value in added_bytes.items():
        target_zip.writestr(name,value,compress_type=zipfile.ZIP_LZMA if name.endswith('.json') else zipfile.ZIP_DEFLATED)
    for name,path in added_files.items():
        target_zip.write(path,name,compress_type=zipfile.ZIP_LZMA if name.endswith('.json') else zipfile.ZIP_DEFLATED)

for bundle in prior['bundles']:
    if bundle['file']!=old_bundle['file']:
        assert copied[bundle['file']]=={k:bundle[k] for k in ('bytes','sha256')}
for name in prior['direct_files']:
    assert copied[name]=={k:prior['files'][name][k] for k in ('bytes','sha256')}

with zipfile.ZipFile(partial) as closed:
    expected_count=len(original_names)+len(added_bytes)+len(added_files)
    assert len(closed.infolist())==len(set(closed.namelist()))==expected_count
    for name, expected in copied.items():
        h=hashlib.sha256();amount=0
        with closed.open(name) as source:
            while block:=source.read(1024*1024):h.update(block);amount+=len(block)
        assert {'bytes':amount,'sha256':h.hexdigest()}==expected
    for name,value in {**replacement,**added_bytes}.items():assert closed.read(name)==value
    for name,path in added_files.items():assert bytes_identity(closed.read(name))==identity(path)
    with closed.open(candidate.name) as source:
        assert hashlib.file_digest(source,'sha256').hexdigest()==result['bundle']['sha256']
assert sha(original_zip)==original_zip_sha
assert identity(candidate)=={k:result['bundle'][k] for k in ('bytes','sha256')}
for name, info in freeze['files'].items():
    assert identity(STAGE/'frozen'/name)=={k:info[k] for k in ('bytes','sha256')}

selection.update(candidate_archive_bytes=partial.stat().st_size,
                 candidate_archive_sha256=sha(partial),
                 unchanged_zip_members=len(copied),
                 unchanged_member_identities=copied,
                 exact_archive_saving=original_zip.stat().st_size-partial.stat().st_size,
                 size_limit=LIMIT,
                 over_limit_bytes=max(0,partial.stat().st_size-LIMIT))
atomic_json(STAGE/'checkpoint35_constant_planes_selection.json',selection)
atomic_json(ROOT/'records/checkpoint35_constant_planes_selection.json',selection)
if partial.stat().st_size>LIMIT:
    saved=STAGE/('checkpoint35.constant_planes.oversize_'+str(time.time_ns()))
    partial.rename(saved)
    print(json.dumps({'status':'MEASURED_CONSTANT_PLANES_SIZE_REPAIR_REQUIRED','bytes':saved.stat().st_size,'over_limit_bytes':saved.stat().st_size-LIMIT,'preserved':str(saved)}),flush=True)
    raise SystemExit(42)

preserved=ROOT/'records/attempts/checkpoint35_before_constant_planes_view_selection'
preserved.mkdir(parents=True,exist_ok=False)
for name in ('checkpoint35_transport_manifest.json','restore_checkpoint.py','checkpoint35_size_measurement.json'):
    shutil.copy2(STAGE/name,preserved/name)
(STAGE/'checkpoint35_transport_manifest.json').write_bytes(manifest_bytes)
(STAGE/'restore_checkpoint.py').write_bytes(restore)
shutil.copy2(codec,STAGE/codec.name)
shutil.copy2(view_codec,STAGE/view_codec.name)
creation={'status':'CREATED','path':str(TARGET),'bytes':partial.stat().st_size,
          'sha256':sha(partial),'snapshot_files':len(freeze['files']),
          'record':freeze['snapshot'],'new_unique_contents':measurement['new_unique_contents'],
          'closed_shards':len(manifest['bundles']),
          'constant_planes_selection_sha256':sha(STAGE/'checkpoint35_constant_planes_selection.json'),
          'full_standalone_restore_pending':True}
atomic_json(STAGE/'checkpoint35_creation.json',creation)
partial.rename(TARGET)
print(json.dumps(creation,indent=2),flush=True)
