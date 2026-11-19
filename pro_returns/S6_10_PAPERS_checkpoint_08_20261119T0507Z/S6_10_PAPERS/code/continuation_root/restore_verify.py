from pathlib import Path
from zipfile import ZipFile
from collections import Counter
import csv, hashlib, json, shutil, datetime

BASE = Path('/workspace/scratch/ae06852560d6')
ROOT = BASE / 'restore/S6_10_PAPERS'
rows = list(csv.DictReader((ROOT/'CHECKPOINT_FILES.tsv').open(), delimiter='\t'))
archives = {}
records = []
for row in rows:
    rel = Path(row['path'])
    assert not rel.is_absolute() and '..' not in rel.parts
    dst = ROOT / rel
    cp = row['checkpoint']
    if cp != 'S6_10_PAPERS_checkpoint_06.zip':
        if cp == 'S6_10_PAPERS_checkpoint_01.zip':
            src = BASE/'restore/_from_earlier_checkpoints/S6_10_PAPERS_checkpoint_01_20261118T0232Z_unzipped/S6_10_PAPERS'/rel
            data = src.read_bytes()
        else:
            if cp not in archives:
                archives[cp] = ZipFile(BASE/'restored_downloads'/cp)
            z = archives[cp]
            candidates = [n for n in z.namelist() if n == 'S6_10_PAPERS/'+rel.as_posix() or n == rel.as_posix()]
            assert len(candidates) == 1, (cp, rel, candidates)
            data = z.read(candidates[0])
        assert len(data) == int(row['size_bytes']), (rel, 'restore size')
        assert hashlib.sha256(data).hexdigest() == row['sha256'], (rel, 'restore hash')
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(data)
    data = dst.read_bytes()
    ok = len(data) == int(row['size_bytes']) and hashlib.sha256(data).hexdigest() == row['sha256']
    records.append({'path':row['path'], 'checkpoint':cp, 'size_bytes':len(data), 'sha256':hashlib.sha256(data).hexdigest(), 'verified':ok})
for z in archives.values(): z.close()
assert all(r['verified'] for r in records)
report = {'timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(), 'total':len(rows), 'verified':len(records), 'origins':dict(Counter(r['checkpoint'] for r in records)), 'records':records}
(BASE/'restore_verification.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='records'},indent=2))
