"""Actually restore and hash every original file of the frozen checkpoint19."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess,sys,zipfile
root=Path(__file__).resolve().parents[1]
stage=root.parent/'checkpoint19_transfer'
archive=stage/'S6_06_BLIND_checkpoint_19.zip'
dest=root.parent/'checkpoint19_restore_verification'
dest.mkdir(exist_ok=False)
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    for member in z.infolist():
        target=(dest/member.filename).resolve()
        assert target.is_relative_to(dest.resolve()),member.filename
    z.extractall(dest)
result=subprocess.run([sys.executable,str(dest/'restore_checkpoint.py')],cwd=dest,
                      capture_output=True,text=True,check=True)
manifest=json.loads((dest/'checkpoint19_transport_manifest.json').read_text())
verified=0
for name,expected in manifest['files'].items():
    p=dest/name
    assert p.stat().st_size==expected['bytes'],name
    assert hashlib.sha256(p.read_bytes()).hexdigest()==expected['sha256'],name
    verified+=1
record={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS',
        'transfer_archive':str(archive),'transfer_bytes':archive.stat().st_size,
        'transfer_sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),
        'original_archive_sha256':manifest['original_archive_sha256'],
        'original_files_verified':verified,'restore_output':result.stdout,
        'verification_directory':str(dest),
        'scope':'Actual full extraction, independent artifact restoration, and size/SHA256 verification of every original snapshot file. No later project file is added to the archive.'}
(root/'records/checkpoint19_transfer_validation.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
