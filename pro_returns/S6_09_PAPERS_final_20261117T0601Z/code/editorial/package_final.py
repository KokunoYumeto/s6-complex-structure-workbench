"""Create the single final ZIP and verify every archived payload byte.

The manifest excludes itself and the verification receipt to avoid circular
hashes. Both are included in the ZIP and separately checked before returning
the final archive's SHA256. Existing final archives are never overwritten.
"""
from pathlib import Path
import argparse, hashlib, json, zipfile
D=Path(__file__).resolve().parents[2]
a=argparse.ArgumentParser();a.add_argument('--time',required=True);args=a.parse_args()
out=D.parent/'S6_09_PAPERS_final.zip'
assert not out.exists(), 'Refusing to overwrite an existing final archive'
gate=json.loads((D/'records/final_package_gate.json').read_text())
assert gate['passed']
assert (D/'S6_09_PAPERS_report.md').read_text().startswith('COMPLETE\n')
manifest_path=D/'records/final_payload_manifest.json'
receipt_path=D/'records/final_archive_verification.json'
sha=lambda data:hashlib.sha256(data).hexdigest()
files=sorted(p for p in D.rglob('*') if p.is_file() and p not in {manifest_path,receipt_path})
dedup=json.loads((D/'records/visual_asset_deduplication.json').read_text())
aliases={x['original_path']:x['retained_path'] for x in dedup['aliases']}
entries=[{'path':str(p.relative_to(D)),'stored_path':aliases.get(str(p.relative_to(D)),str(p.relative_to(D))),'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())} for p in files]
stored_files=[p for p in files if str(p.relative_to(D)) not in aliases]
manifest={'scope':'Every final deliverable, code file, computation output, review record and retained checkpoint byte version under deliverables/. Only exact duplicate PNG payloads share the stored path explicitly given for every alias.','created_at_utc':args.time,'files':entries,'logical_payload_file_count':len(entries),'stored_payload_file_count':len(stored_files),'payload_bytes':sum(e['bytes'] for e in entries),'duplicate_image_paths':len(aliases),'restoration_map':'records/visual_asset_deduplication.json','restore_command':'python3 code/editorial/restore_duplicate_visual_assets.py --restore','excluded_from_own_hash_list':['records/final_payload_manifest.json','records/final_archive_verification.json'],'supplied_source_archives_included':False,'runtime_binary_caches_included':False}
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
with zipfile.ZipFile(out,'x',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in stored_files+[manifest_path]:z.write(p,p.relative_to(D))
with zipfile.ZipFile(out) as z:
    assert len(z.namelist())==len(stored_files)+1
    verified={}
    for e in entries:
        name=e['stored_path']
        if name not in verified:
            data=z.read(name);verified[name]=(len(data),sha(data))
        assert verified[name]==(e['bytes'],e['sha256']),e['path']
    assert z.read('records/final_payload_manifest.json')==manifest_path.read_bytes()
receipt={'passed':True,'verified_at_utc':args.time,'logical_payload_files_verified':len(entries),'stored_payload_files_verified':len(stored_files),'payload_bytes_verified':sum(e['bytes'] for e in entries),'manifest_sha256':sha(manifest_path.read_bytes()),'method':'Each archived payload member was decompressed, CRC checked by the ZIP reader, and compared with its exact byte count and SHA256 in the payload manifest. Every duplicate-image original path was independently matched to the same exact stored payload. The manifest itself was compared byte for byte. This receipt was then appended and the complete ZIP CRC tested again.','final_stored_file_count_including_manifest_and_receipt':len(stored_files)+2,'final_logical_file_count_including_manifest_and_receipt':len(entries)+2,'final_zip_sha256_location':'Returned by the packager after the final CRC pass and supplied with the download; not embedded in the archive whose bytes it hashes.'}
receipt_path.write_text(json.dumps(receipt,indent=2)+'\n')
with zipfile.ZipFile(out,'a',zipfile.ZIP_DEFLATED,compresslevel=6) as z:z.write(receipt_path,receipt_path.relative_to(D))
with zipfile.ZipFile(out) as z:
    assert len(z.namelist())==len(stored_files)+2
    assert z.testzip() is None
    assert z.read('records/final_archive_verification.json')==receipt_path.read_bytes()
assert out.stat().st_size<=536870912,'Final ZIP exceeds the observed per-file saving limit'
result={'path':str(out),'stored_files':len(stored_files)+2,'logical_files':len(entries)+2,'bytes':out.stat().st_size,'sha256':sha(out.read_bytes()),'crc_and_payload_sha256_passed':True,'completed_at_utc':args.time}
(D.parent/'S6_09_PAPERS_final_integrity.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
