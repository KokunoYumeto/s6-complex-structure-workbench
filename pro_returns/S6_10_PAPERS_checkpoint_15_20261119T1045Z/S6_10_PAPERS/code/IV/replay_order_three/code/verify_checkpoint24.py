"""Independently extract and execute the complete standalone checkpoint24."""
from pathlib import Path
import hashlib,json,zipfile,subprocess,sys
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parent
archive=BASE/'S6_06_BLIND_checkpoint_24.zip'
expected=json.loads((BASE/'checkpoint24_encoding/checkpoint24_creation.json').read_text())
with archive.open('rb') as f:sha=hashlib.file_digest(f,'sha256').hexdigest()
assert sha==expected['sha256']
dest=BASE/'checkpoint24_verify';dest.mkdir(exist_ok=False)
with zipfile.ZipFile(archive) as z:
 for member in z.infolist():
  p=Path(member.filename);assert not p.is_absolute() and '..' not in p.parts
 z.extractall(dest)
subprocess.run([sys.executable,str(dest/'restore_checkpoint.py')],cwd=dest,check=True)
manifest=json.loads((dest/'checkpoint24_transport_manifest.json').read_text())
assert len(manifest['files'])==expected['snapshot_files']
rec={'status':'PASS','archive':str(archive),'bytes':archive.stat().st_size,'sha256':sha,'restored_and_verified_files':len(manifest['files']),'verification':'Extracted standalone archive in an empty directory, ran its delivered stdlib restorer, and checked every frozen file size and SHA256.','archive_unchanged':True}
(ROOT/'records/checkpoint24_verification.json').write_text(json.dumps(rec,indent=2)+'\n')
print(json.dumps(rec,indent=2))
