"""Validate or restore exact duplicate image paths after extracting the ZIP.

Run without arguments to verify every retained payload and any existing
aliases. Add --restore to recreate missing original image paths. Existing
different files are never overwritten; all paths stay within this archive.
"""
from pathlib import Path, PurePosixPath
import argparse, hashlib, json, shutil
D=Path(__file__).resolve().parents[2]
a=argparse.ArgumentParser();a.add_argument('--restore',action='store_true');args=a.parse_args()
r=json.loads((D/'records/visual_asset_deduplication.json').read_text())
def safe(rel):
    parts=PurePosixPath(rel)
    assert not parts.is_absolute() and '..' not in parts.parts,rel
    path=D/rel
    assert path.resolve().is_relative_to(D.resolve()),rel
    return path
verified={};restored=0;missing=0
for item in r['unique_payloads']:
    p=safe(item['path']);assert p.is_file(),str(p)
    digest=hashlib.sha256(p.read_bytes()).hexdigest()
    assert digest==item['sha256'] and p.stat().st_size==item['bytes'],str(p)
    verified[item['path']]=digest
for item in r['aliases']:
    source=safe(item['retained_path']);target=safe(item['original_path'])
    assert verified[item['retained_path']]==item['sha256']
    if target.exists():
        assert target.is_file() and hashlib.sha256(target.read_bytes()).hexdigest()==item['sha256'],str(target)
    elif args.restore:
        target.parent.mkdir(parents=True,exist_ok=True)
        with target.open('xb') as output, source.open('rb') as data:shutil.copyfileobj(data,output)
        assert hashlib.sha256(target.read_bytes()).hexdigest()==item['sha256']
        restored+=1
    else:missing+=1
print(json.dumps({'passed':True,'unique_payloads_verified':len(verified),'duplicate_paths_restored':restored,'duplicate_paths_available_to_restore':missing,'all_original_bytes_preserved':True}))
