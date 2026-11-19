"""Verify the frozen transfer with an exact decompression seek cache.

The packaged restoration script is executed unchanged. Its compressed-tar
reader is backed by that same tar stream decompressed once, avoiding repeated
XZ decoding when standard tar hardlink records seek to earlier images.
"""
from pathlib import Path
from datetime import datetime,timezone
import contextlib,hashlib,io,json,lzma,runpy,shutil,tarfile,zipfile

root=Path(__file__).resolve().parents[1]
archive=root.parent/'checkpoint17_transfer/S6_06_BLIND_checkpoint_17.zip'
dest=root.parent/'checkpoint17_restore_cached_verification'
dest.mkdir(exist_ok=False)
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    for info in z.infolist():
        assert (dest/info.filename).resolve().is_relative_to(dest.resolve())
    z.extractall(dest)
bundle=dest/'checkpoint17_qa_images.tar.xz'
cache=dest/'lossless_decompression_seek_cache.tar'
with lzma.open(bundle,'rb') as source,cache.open('xb') as target:
    shutil.copyfileobj(source,target,1024*1024)
original_open=tarfile.open
def cached_open(name=None,mode='r',*args,**kwargs):
    if name is not None and Path(name).resolve()==bundle.resolve() and mode=='r:xz':
        return original_open(cache,'r:',*args,**kwargs)
    return original_open(name,mode,*args,**kwargs)
tarfile.open=cached_open
output=io.StringIO()
try:
    with contextlib.redirect_stdout(output):
        runpy.run_path(str(dest/'restore_checkpoint.py'),run_name='__main__')
finally:
    tarfile.open=original_open
manifest=json.loads((dest/'checkpoint17_transport_manifest.json').read_text())
count=0
for name,expected in manifest['files'].items():
    p=dest/name
    assert p.stat().st_size==expected['bytes'],name
    assert hashlib.sha256(p.read_bytes()).hexdigest()==expected['sha256'],name
    count+=1
record={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS',
 'transfer_archive':str(archive),'transfer_bytes':archive.stat().st_size,
 'transfer_sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),
 'original_archive_sha256':manifest['original_archive_sha256'],
 'original_files_verified':count,'restore_output':output.getvalue(),
 'packaged_restore_script_sha256':hashlib.sha256((dest/'restore_checkpoint.py').read_bytes()).hexdigest(),
 'verification_directory':str(dest),
 'scope':'Full outer ZIP CRC check and extraction; complete XZ decoding; unchanged packaged restore script run with a byte-identical uncompressed seek cache; every original file independently checked for size and SHA256. No later project file is added to the archive.',
 'cache_scope':'Only tarfile.open on the exact extracted image bundle in r:xz mode is redirected to the complete tar bytes decoded from that bundle. All member parsing, hardlink resolution, write/refusal logic and manifest checking are the unchanged packaged script.'}
(root/'records/checkpoint17_transfer_validation_cached.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
