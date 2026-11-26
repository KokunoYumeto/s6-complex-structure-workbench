"""Record the verified scheduled archive and its successful download identity."""
from pathlib import Path
import argparse, datetime, hashlib, json

p = argparse.ArgumentParser()
p.add_argument('number', type=int)
a = p.parse_args()
root = Path(__file__).resolve().parents[1]
stem = f'S6_SERIES_PUBLISH_checkpoint_{a.number:02d}'
r = json.loads((root / 'code' / (stem + '.out')).read_text())
u = json.loads((root / 'records' / (stem + '_upload.json')).read_text())['results'][0]
assert u['status'] == 'succeeded'
archive = Path(r['path'])
assert archive.stat().st_size == r['size']
assert hashlib.sha256(archive.read_bytes()).hexdigest() == r['sha256']
start = datetime.datetime.fromisoformat(json.loads((root / 'records/S6_SERIES_PUBLISH_continuation_restore.json').read_text())['continuation_started_utc'])
next_checkpoint = start + datetime.timedelta(minutes=45 * (a.number + 1 - 10))
record = dict(checkpoint=a.number, **r,
              upload_receipt=f'records/{stem}_upload.json',
              library_file_id=u['library_file_id'],
              delivery='Download link provided in conversation commentary; work continues.',
              next_checkpoint_utc=next_checkpoint.isoformat())
out = root / 'records' / (stem + '_delivery.json')
assert not out.exists()
out.write_text(json.dumps(record, indent=2) + '\n')
entry = f'\n## Checkpoint {a.number:02d} delivered — {r["created_utc"]}\n\n'
entry += f'The scheduled archive contains {r["files"]} manifest-listed files, preserving all {r["restored_files_preserved"]} inherited checkpoint paths including the original manifest. Size: {r["size"]} bytes; SHA-256 `{r["sha256"]}`. Every archive member passed its size/hash verification. The downloadable checkpoint was delivered and work continues. The next checkpoint is due at {next_checkpoint.isoformat()}. Packaging creates no mathematical-check or page-reading credit. Receipt: `records/{stem}_delivery.json`.\n'
for name in ['PROGRESS_LEDGER.md', 'S6_SERIES_PUBLISH_report.md']:
    path = root / name
    assert f'## Checkpoint {a.number:02d} delivered' not in path.read_text()
    path.write_bytes(path.read_bytes() + entry.encode())
print(json.dumps({'record': str(out.relative_to(root)), 'checkpoint_verified': True,
                  'library_file_id': u['library_file_id']}))
