"""Create one immutable full hourly checkpoint; upload is a separate recorded step.

Usage: python3 code/save_checkpoint.py NN
The caller enforces the user's once-per-hour schedule. Existing files are never
replaced. Supplied attachments are deliberately excluded. The preceding ZIP is
included verbatim, retaining superseded authored files and passages.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sys
import zipfile

root = Path(__file__).resolve().parents[1]
workspace = root.parent
number = int(sys.argv[1])
target = workspace / f'S6_03_CDP_checkpoint_{number:02d}.zip'
if target.exists():
    raise SystemExit(f'Refusing to replace immutable checkpoint: {target}')
stamp = datetime.now(timezone.utc).isoformat()
record = root / 'records' / 'checkpoints.md'
with record.open('a') as stream:
    stream.write(f'\n{number:02d}: {stamp}; all current authored project files and '
                 'research support included; supplied attachments excluded. '
                 'Earlier checkpoint retained verbatim under archives/.\n')
files = [(p, Path('S6_03_CDP') / p.relative_to(root))
         for p in sorted(root.rglob('*')) if p.is_file()]
for name in ['library_helpers_current', 'research_tmp', 'scratch_references']:
    directory = workspace / name
    if directory.exists():
        files.extend((p, Path('research_support') / name / p.relative_to(directory))
                     for p in sorted(directory.rglob('*')) if p.is_file())
previous = workspace / f'S6_03_CDP_checkpoint_{number-1:02d}.zip'
if number > 1 and previous.exists():
    files.append((previous, Path('archives') / previous.name))
with zipfile.ZipFile(target, 'x', compression=zipfile.ZIP_DEFLATED,
                     compresslevel=6) as archive:
    for path, member in files:
        archive.write(path, str(member))
digest = hashlib.sha256(target.read_bytes()).hexdigest()
result = {'path': str(target), 'created_utc': stamp, 'members': len(files),
          'bytes': target.stat().st_size, 'sha256': digest}
print(json.dumps(result, indent=2))
(root / 'records' / f'checkpoint_{number:02d}_manifest.json').write_text(
    json.dumps(result, indent=2) + '\n')
