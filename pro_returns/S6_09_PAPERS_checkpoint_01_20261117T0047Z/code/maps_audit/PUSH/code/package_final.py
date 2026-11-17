#!/usr/bin/env python3
"""Publish one final archive only after payload and final-manifest verification.

The outer archive digest is recorded beside the ZIP, avoiding a self-referential
digest inside it. The complete payload verification, manifest and this program's
stable output are included in the ZIP.
"""
from pathlib import Path
import datetime, hashlib, json, zipfile

root = Path(__file__).resolve().parents[1]
dest = root.parent / "S6_02_PUSH.zip"
partial = root.parent / "S6_02_PUSH.zip.partial"
assert not dest.exists() and not partial.exists(), "Never replace an earlier final archive"
preflight = json.loads((root/"code/final_preflight.json").read_text())
assert preflight["passed"]
metadata = {"code/final_manifest.json", "code/final_package_verification.json", "code/package_final.out"}
paths = sorted(path for path in root.rglob("*") if path.is_file()
               and "__pycache__" not in path.parts and str(path.relative_to(root)) not in metadata)

def entry(path):
    data = path.read_bytes()
    return {"path":str(path.relative_to(root)),"bytes":len(data),"sha256":hashlib.sha256(data).hexdigest()}

records = [entry(path) for path in paths]
with zipfile.ZipFile(partial,"x",compression=zipfile.ZIP_DEFLATED,compresslevel=6) as archive:
    for path in paths:
        archive.write(path,Path(root.name)/path.relative_to(root))
with zipfile.ZipFile(partial) as archive:
    assert archive.testzip() is None
    for record in records:
        data = archive.read(root.name+"/"+record["path"])
        assert len(data) == record["bytes"]
        assert hashlib.sha256(data).hexdigest() == record["sha256"]

verification = {"payload_verified_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
                "payload_files_verified":len(records),"all_payload_bytes_and_sha256_match":True,
                "payload_crc_passed":True,"publication_condition":"After adding these metadata files, every manifest entry and final ZIP CRC is verified again; rename to S6_02_PUSH.zip occurs only if every assertion passes.",
                "checkpoint_retention":"All nine archives and every historical file version were verified in code/final_preflight.json.",
                "excluded":"Supplied inputs, external article scans/OCR and reproducible runtime caches; Python __pycache__.",
                "archive_prefix":root.name+"/"}
verification_path = root/"code/final_package_verification.json"
verification_path.write_text(json.dumps(verification,indent=2)+"\n")
output = (f"Verified {len(records)} payload files by byte count and SHA-256.\n"
          "All nine checkpoint archives are preserved byte for byte at current or retained paths.\n"
          "Final manifest entries and ZIP CRCs passed; published S6_02_PUSH.zip.\n"
          "The outer ZIP size and SHA-256 are recorded in the adjacent S6_02_PUSH_final_receipt.json.\n")
output_path = root/"code/package_final.out"
output_path.write_text(output)
records.extend([entry(verification_path),entry(output_path)])
manifest = {"created_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "files":records,"manifest_self_exclusion":"This manifest is the only archive entry not listed inside itself."}
manifest_path = root/"code/final_manifest.json"
manifest_path.write_text(json.dumps(manifest,indent=2)+"\n")
with zipfile.ZipFile(partial,"a",compression=zipfile.ZIP_DEFLATED,compresslevel=6) as archive:
    for path in [verification_path,output_path,manifest_path]:
        archive.write(path,Path(root.name)/path.relative_to(root))
with zipfile.ZipFile(partial) as archive:
    assert archive.testzip() is None
    names = archive.namelist()
    assert len(names) == len(set(names)) == len(records)+1
    assert set(names) == {root.name+"/"+row["path"] for row in records} | {root.name+"/code/final_manifest.json"}
    for record in records:
        data = archive.read(root.name+"/"+record["path"])
        assert len(data) == record["bytes"] and hashlib.sha256(data).hexdigest() == record["sha256"]
partial.rename(dest)
receipt = {"completed_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
           "archive":str(dest),"files":len(records)+1,"bytes":dest.stat().st_size,
           "sha256":hashlib.sha256(dest.read_bytes()).hexdigest(),
           "all_manifest_entries_verified":True,"zip_crc_passed":True,
           "pdf_pages":preflight["pdf_pages"],"statement_rows":preflight["statement_rows"],
           "bibliography_entries":preflight["bibliography_entries"],"visual_pages":preflight["visual_pages"],
           "current_open_rows":0,"retained_changed_versions":preflight["retained_changed_versions"]}
(root.parent/"S6_02_PUSH_final_receipt.json").write_text(json.dumps(receipt,indent=2)+"\n")
print(output,end="")
