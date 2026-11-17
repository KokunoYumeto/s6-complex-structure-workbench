"""Retry the already frozen sixth checkpoint with exact PNG deduplication.

This is a transport encoding of the same hourly snapshot, not a new capture.
The original ZIP is immutable. Every original member's complete bytes are
verified against the retry ZIP through its explicit restoration map.
"""
from pathlib import Path
import hashlib, json, zipfile
D=Path(__file__).resolve().parents[2];root=D.parent
original=root/'S6_09_PAPERS_checkpoint_06.zip'
folder=root/'repacked_checkpoints';folder.mkdir(exist_ok=True)
target=folder/original.name
assert not target.exists()
plan=json.loads((D/'records/visual_asset_deduplication.json').read_text())
aliases={x['original_path']:x['retained_path'] for x in plan['aliases']}
sha=lambda b:hashlib.sha256(b).hexdigest()
old_sha=sha(original.read_bytes())
assert old_sha=='13d04426c8832adf4fa4bdc5d198851f45afaeb2abcaff1e4aafa3ef21d800d0'
members=[]
with zipfile.ZipFile(original) as source:
    names=set(source.namelist())
    assert all(k in names and v in names for k,v in aliases.items())
    with zipfile.ZipFile(target,'x',zipfile.ZIP_DEFLATED,compresslevel=6) as out:
        for info in source.infolist():
            assert not info.is_dir()
            data=source.read(info.filename);stored=aliases.get(info.filename,info.filename)
            members.append({'original_path':info.filename,'stored_path':stored,'bytes':len(data),'sha256':sha(data)})
            if info.filename not in aliases:out.writestr(info,data,compress_type=zipfile.ZIP_DEFLATED,compresslevel=6)
        metadata={'logical_checkpoint':6,'capture_utc':'2026-11-17 05:47:53 UTC','original_archive_name':original.name,'original_archive_bytes':original.stat().st_size,'original_archive_sha256':old_sha,'original_archive_unchanged':True,'reason':'The save service rejected the original787828278-byte file at its536870912-byte limit. This lossless transport encoding preserves every original member byte, shares only identical PNG payloads, and adds the restoration map and helper. No new mathematical/work snapshot is taken.','members':members,'original_members':len(members),'image_aliases':len(aliases),'restore_command':'python3 code/editorial/restore_duplicate_visual_assets.py --restore','archive_container_bytes_differ':'ZIP framing/compression differs from the immutable original; every complete member payload is preserved exactly. The original archive hash above remains the original capture identity.'}
        manifest=json.dumps(metadata,ensure_ascii=False,indent=2)+'\n'
        (D/'records/checkpoint_06_transport_manifest.json').write_text(manifest)
        for path in ['records/visual_asset_deduplication.json','code/editorial/restore_duplicate_visual_assets.py','records/checkpoint_06_transport_manifest.json']:
            assert path not in names
            out.write(D/path,path)
        out.writestr('READ_THIS_CHECKPOINT.txt','This is the complete frozen hourly checkpoint06. Every paper, code file, text record and unique image is present. Identical PNG copies share stored bytes to meet the file-size limit. After extraction run:\n\n  python3 code/editorial/restore_duplicate_visual_assets.py --restore\n\nThe script recreates every duplicate original path, checks full SHA256 values, and refuses to overwrite different files. records/checkpoint_06_transport_manifest.json records every original checkpoint member and its retained payload. The original checkpoint ZIP remains unchanged; this is a smaller lossless representation of that same snapshot, not a later checkpoint.\n')
with zipfile.ZipFile(target) as out:
    assert out.testzip() is None
    verified={}
    for item in members:
        name=item['stored_path']
        if name not in verified:
            data=out.read(name);verified[name]=(len(data),sha(data))
        assert verified[name]==(item['bytes'],item['sha256']),item['original_path']
assert target.stat().st_size<=536870912
assert sha(original.read_bytes())==old_sha
receipt={'passed':True,'logical_checkpoint':6,'capture_utc':metadata['capture_utc'],'path':str(target),'bytes':target.stat().st_size,'sha256':sha(target.read_bytes()),'original_archive_sha256':old_sha,'original_archive_unchanged':True,'all_original_member_payloads_verified':len(members),'image_aliases':len(aliases),'new_logical_checkpoint_created':False,'transport_manifest':'records/checkpoint_06_transport_manifest.json'}
(D/'records/checkpoint_06_lossless_repack.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
