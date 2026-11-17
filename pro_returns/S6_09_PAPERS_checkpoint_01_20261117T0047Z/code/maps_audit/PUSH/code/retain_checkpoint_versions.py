#!/usr/bin/env python3
"""Retain every changed checkpoint byte stream, without altering checkpoint ZIPs.

An unchanged file is already retained at its current path.  Any changed or
removed one is copied to retained/checkpoint_NN/<original path>.  Nested
retained paths are already durable and are verified rather than duplicated.
"""
from pathlib import Path
import zipfile,hashlib,json

root=Path(__file__).resolve().parents[1]
records=[]
def sha(data): return hashlib.sha256(data).hexdigest()
for archive in sorted(root.parent.glob('S6_02_PUSH_checkpoint_*.zip')):
    number=archive.stem.rsplit('_',1)[1]
    with zipfile.ZipFile(archive) as z:
        for item in z.infolist():
            if item.is_dir():continue
            prefix=root.name+'/'
            assert item.filename.startswith(prefix),item.filename
            relative=Path(item.filename[len(prefix):])
            assert '..' not in relative.parts
            old=z.read(item)
            current=root/relative
            if current.exists() and current.read_bytes()==old:
                continue
            if relative.parts[0]=='retained':
                raise AssertionError('An already retained historical file changed: '+str(relative))
            target=root/'retained'/('checkpoint_'+number)/relative
            target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists():assert target.read_bytes()==old
            else:target.write_bytes(old)
            records.append({'checkpoint':archive.name,'original_path':str(relative),
                            'retained_path':str(target.relative_to(root)),
                            'bytes':len(old),'sha256':sha(old),
                            'current_path':str(relative) if current.exists() else None,
                            'reason':'Superseded by the named current file; previous bytes retained in full.' if current.exists() else 'Removed from current presentation; previous bytes retained in full.'})
(root/'code'/'retention_record.json').write_text(json.dumps(records,indent=2)+'\n')
lines=['## Checkpoint retention record','',
       'No checkpointed file or passage is discarded. Unchanged files remain at their original paths; every changed version is retained byte for byte below. The current source supersedes its historical counterpart. A prior Open statement may therefore remain in an archived version even when the current numbered statement has been resolved. The original ZIPs are never modified.','',
       '| Checkpoint | Previous file | Retained full version | Current replacement |',
       '|---|---|---|---|']
for r in records:
    lines.append('| '+r['checkpoint']+' | '+r['original_path']+' | '+r['retained_path']+' | '+(r['current_path'] or 'Historical version retained only')+' |')
lines+=['','Exact byte counts and SHA256 digests are in code/retention_record.json.']
(root/'sections'/'retention_record.md').write_text('\n'.join(lines)+'\n')
print(json.dumps({'checkpoint_archives':len(list(root.parent.glob('S6_02_PUSH_checkpoint_*.zip'))),
                  'changed_versions_retained':len(records),'all_previous_bytes_retained':True},indent=2))
