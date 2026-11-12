"""Preserve supplied bytes; repair only the two replay receipts per intake.

The two archives are authoritative bytes. Existing source mismatches are
permitted only for the documented LF/CRLF replay-output mutation.
"""
from pathlib import Path
import argparse
from datetime import datetime, timezone
import gzip
import hashlib
import json
import zipfile

HERE=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--packet-dir',type=Path,required=True)
parser.add_argument('--intake-dir',type=Path,required=True)
parser.add_argument('--literature-dir',type=Path,required=True)
args=parser.parse_args()
INTAKE=args.intake_dir
PACKETS=args.packet_dir
NAMES={
 'Triality_4-4-4-1_Dynamic_Completion_20260904':'0e873c627aa1ee0abedd1fafa16c5638f5d56540bb554783e27189725013aa3d',
 'Quaternionic_4441_Continuation_20260904':'ea19821b7d252b1b097dd808a4f3587ac5b0e4d4a2bba21c6bb845ff418f5654',
}
def sha(b): return hashlib.sha256(b).hexdigest()
rows=[]; restored=[]; archives=[]
for name,expected in NAMES.items():
    archive=PACKETS/(name+'.zip')
    raw=archive.read_bytes()
    assert sha(raw)==expected
    archives.append({'file':archive.name,'bytes':len(raw),'sha256':sha(raw)})
    with zipfile.ZipFile(archive) as z:
        for info in z.infolist():
            if info.is_dir(): continue
            rp=Path(info.filename)
            assert not rp.is_absolute() and '..' not in rp.parts
            # These supplied ZIPs have flat members.
            assert len(rp.parts)==1,info.filename
            original=z.read(info)
            dest=HERE/'source'/name/rp
            if dest.exists(): assert dest.read_bytes()==original
            else:
                dest.parent.mkdir(parents=True,exist_ok=True)
                dest.write_bytes(original)
            old=INTAKE/name/rp
            if old.exists() and old.read_bytes()!=original:
                previous=old.read_bytes()
                assert rp.name in ('verification_output.txt','verification_results.json')
                assert previous.replace(b'\r\n',b'\n')==original.replace(b'\r\n',b'\n')
                save=HERE/'replay_output_before_receipt_restoration'/name/rp
                save.parent.mkdir(parents=True,exist_ok=True)
                if save.exists(): assert save.read_bytes()==previous
                else: save.write_bytes(previous)
                old.write_bytes(original)
                restored.append({'path':name+'/'+rp.as_posix(),'before_sha256':sha(previous),'original_sha256':sha(original)})
            rows.append({'path':dest.relative_to(HERE).as_posix(),'bytes':len(original),'sha256':sha(original)})
manifest_rows=0
for name in NAMES:
    parent=HERE/'source'/name
    for line in (parent/'MANIFEST.sha256').read_text(encoding='utf-8').splitlines():
        if not line.strip(): continue
        digest,rel=line.split(maxsplit=1)
        assert sha((parent/rel.lstrip('*')).read_bytes())==digest.lower()
        manifest_rows+=1

# arXiv serves this version as a gzip-compressed single TeX source, not a tar.
lit=args.literature_dir
compressed=(lit/'source.tar').read_bytes()
assert compressed[:2]==b'\x1f\x8b'
tex=gzip.decompress(compressed)
assert b'\\documentclass' in tex[:150]
(lit/'source.tex').write_bytes(tex)
literature={'url':'https://arxiv.org/src/1805.07759v1',
 'format':'gzip-compressed single TeX source, not tar',
 'download_sha256':sha(compressed),'tex_sha256':sha(tex),
 'tex_bytes':len(tex),'used_sections':'Propositions 2.1-2.3; complex representation (1.2)'}
receipt={'recorded_utc':datetime.now(timezone.utc).isoformat(),
 'archives':archives,'original_files':rows,'verified_manifest_rows':manifest_rows,
 'restored_replay_receipts':restored,'literature':literature,
 'scope':'Bounded reconciliation and dynamics audit; not whole-packet certification.'}
target=HERE/'INTAKE_RECEIPT.json'
if target.exists():
    # Preserve the first receipt, including the actual restoration events.
    first=json.loads(target.read_text(encoding='utf-8'))
    assert first['original_files']==rows
else: target.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'original_files':len(rows),'manifest_rows':manifest_rows,
 'restored_receipts':len(restored),'literature':literature},indent=2))
