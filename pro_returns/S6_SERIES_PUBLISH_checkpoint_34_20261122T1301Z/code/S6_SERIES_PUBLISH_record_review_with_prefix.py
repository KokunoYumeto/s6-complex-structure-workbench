"""Record one completed review and certify the two exact old byte prefixes."""
from pathlib import Path
import datetime
import hashlib
import json
import runpy
import sys

root = Path(__file__).resolve().parents[1]
number = int(sys.argv[1])
paths = ['PROGRESS_LEDGER.md', 'S6_SERIES_PUBLISH_report.md']
before = {name: (root / name).read_bytes() for name in paths}
insert = (root / f'agents/continuation_infra/S6_SERIES_PUBLISH_progress_review_{number:02d}_insert.md').read_bytes()
journal = root / f'records/S6_SERIES_PUBLISH_progress_review_{number:02d}_journal.json'
assert not journal.exists()
runpy.run_path(str(root / 'code/S6_SERIES_PUBLISH_record_continuation_review.py'), run_name='__main__')
sha = lambda data: hashlib.sha256(data).hexdigest()
changes = []
for name in paths:
    after = (root / name).read_bytes()
    assert after == before[name] + insert
    changes.append(dict(path=name, before_sha256=sha(before[name]), after_sha256=sha(after),
                        prefix_preserved=True, appended_sha256=sha(insert)))
record = dict(recorded_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
              review=f'records/S6_SERIES_PUBLISH_progress_review_{number:02d}.json',
              changes=changes, mathematical_events_added=0)
journal.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(dict(journal=str(journal.relative_to(root)), sha256=sha(journal.read_bytes()),
                      exact_old_prefixes_preserved=True)))
