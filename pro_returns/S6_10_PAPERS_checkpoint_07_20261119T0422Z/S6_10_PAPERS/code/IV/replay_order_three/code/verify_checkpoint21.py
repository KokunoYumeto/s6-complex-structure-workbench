"""Independently unpack the delivered full ZIP and execute its restore program."""
from pathlib import Path
import hashlib,json,zipfile,subprocess,sys
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parent
archive=BASE/'S6_06_BLIND_checkpoint_21.zip'
expected=json.loads((BASE/'checkpoint21_create.out').read_text())
with archive.open('rb') as f:sha=hashlib.file_digest(f,'sha256').hexdigest()
assert sha==expected['sha256']
destination=BASE/'checkpoint21_verify'
destination.mkdir(exist_ok=False)
with zipfile.ZipFile(archive) as z:
    for member in z.infolist():
        p=Path(member.filename)
        assert not p.is_absolute() and '..' not in p.parts
    z.extractall(destination)
subprocess.run([sys.executable,str(destination/'restore_checkpoint.py')],cwd=destination,check=True)
manifest=json.loads((destination/'checkpoint21_transport_manifest.json').read_text())
assert len(manifest['files'])==expected['snapshot_files']==7812
rec={'status':'PASS','archive':str(archive),'bytes':archive.stat().st_size,'sha256':sha,'restored_and_verified_files':len(manifest['files']),'verification':'Extracted the complete standalone ZIP into an empty independent directory, executed its delivered restore script, and verified every final size and SHA-256.','original_immutable_archive_changed':False}
(ROOT/'records/checkpoint21_verification.json').write_text(json.dumps(rec,indent=2)+'\n')
print(json.dumps(rec,indent=2))
