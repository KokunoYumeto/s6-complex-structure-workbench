"""Retain the exact bytes of every superseded hourly-checkpoint member.

This is not a new checkpoint. The hash-indexed history is part of the final
deliverable so every former file/passage is recoverable. Current byte-identical
files are reused; older bytes are retained once with all original path aliases.
"""
from pathlib import Path, PurePosixPath
import hashlib, json, zipfile, collections, re

ROOT=Path(__file__).resolve().parents[3]
D=ROOT/'deliverables'
history=D/'history'/'checkpoint_versions'
history.mkdir(parents=True,exist_ok=True)
current={}
mutable_final_records={
    'records/checkpoint_retention.json',
    'S6_09_PAPERS_report.md',
    'records/final_package_gate.json',
    'records/final_payload_manifest.json',
    'records/final_archive_verification.json',
    'work/root/RESUME.md',
}
for p in D.rglob('*'):
    if (p.is_file() and 'history/checkpoint_versions/' not in str(p.relative_to(D))
            and str(p.relative_to(D)) not in mutable_final_records):
        current[str(p.relative_to(D))]=hashlib.sha256(p.read_bytes()).hexdigest()
members=[];archives=[];retained=set();reused=0
archive_paths=sorted(ROOT.glob('S6_09_PAPERS_checkpoint_*.zip'))+sorted((ROOT/'repacked_checkpoints').glob('S6_09_PAPERS_checkpoint_*.zip'))
for zpath in archive_paths:
    archive_name=str(zpath.relative_to(ROOT))
    logical_checkpoint=int(re.search(r'_checkpoint_(\d+)\.zip$',zpath.name)[1])
    archives.append({'archive':archive_name,'logical_checkpoint':logical_checkpoint,'bytes':zpath.stat().st_size,
                     'sha256':hashlib.sha256(zpath.read_bytes()).hexdigest()})
    with zipfile.ZipFile(zpath) as z:
        for info in z.infolist():
            if info.is_dir():continue
            name=info.filename;p=PurePosixPath(name)
            assert not p.is_absolute() and '..' not in p.parts,name
            data=z.read(info);sha=hashlib.sha256(data).hexdigest()
            if current.get(name)==sha:
                target=name;state='Retained unchanged at original path';reused+=1
            else:
                ext=''.join(Path(name).suffixes)[-32:]
                target=str((history/(sha+ext)).relative_to(D))
                f=D/target
                if f.exists():assert hashlib.sha256(f.read_bytes()).hexdigest()==sha
                else:f.write_bytes(data)
                retained.add(target)
                state=('Superseded at original path by the current version; exact earlier bytes retained here'
                       if name in current else
                       'No current file at the original path; exact earlier bytes retained here')
            members.append({'checkpoint':archive_name,'original_path':name,
                'sha256':sha,'bytes':len(data),'retained_path':target,'disposition':state})
record={'scope':'Every file in each actual hourly ZIP; no checkpoint file or passage discarded',
 'logical_checkpoint_count':len({x['logical_checkpoint'] for x in archives}),
 'physical_archive_representation_count':len(archives),
 'retry_encoding_rule':'The repacked sixth checkpoint is the same frozen hourly snapshot encoded losslessly after the observed size-limit rejection. Both the immutable original and the successful retry representation are retained by their actual members; it is not a seventh logical checkpoint.',
 'always_archive_old_versions_of':sorted(mutable_final_records),
 'self_reference_rule':'A checkpoint retention manifest cannot retain its own earlier bytes at its current path because writing the new manifest changes those bytes. Every earlier manifest and other final mutable record is therefore retained under its content hash.',
 'archives':archives,'members':members,'current_path_reuses':reused,
 'distinct_retained_older_files':len(retained),'omitted_checkpoint_members':[],
 'reason_for_not_embedding_whole_checkpoint_ZIPs':'Every member is retained by original path or exact hash-indexed version; nesting the ZIP files would duplicate the same bytes.'}
(D/'records/checkpoint_retention.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'archives':len(archives),'member_occurrences':len(members),
                  'current_path_reuses':reused,'distinct_retained_older_files':len(retained)}))
