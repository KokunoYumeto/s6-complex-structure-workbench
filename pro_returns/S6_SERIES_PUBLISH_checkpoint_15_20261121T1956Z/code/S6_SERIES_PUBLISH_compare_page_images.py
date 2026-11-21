#!/usr/bin/env python3
"""Compare complete candidate page PNG hashes with an archived reading coverage.

This records exact equality only. It creates no page reading or check event.
"""
from pathlib import Path
import argparse
import datetime as dt
import hashlib
import json

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('coverage', type=Path)
p.add_argument('manifest', type=Path)
p.add_argument('--output', type=Path, required=True)
a = p.parse_args()
old = json.loads(a.coverage.read_text())
new = json.loads(a.manifest.read_text())
prior = {row['page']: row['image_sha256'] for row in old['pages']}
identical, changed = [], []
for page in new['rendered_pages']:
    image = Path(page['image'])
    assert hashlib.sha256(image.read_bytes()).hexdigest() == page['image_sha256']
    (identical if prior.get(page['page']) == page['image_sha256'] else changed).append(page['page'])
record = dict(recorded_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
              old_source_sha256=old.get('source_sha256'), old_pdf_sha256=old['pdf_sha256'],
              current_pdf_sha256=new['pdf_sha256'], pages=new['pages'], scale=new['scale'],
              identical_entire_png_pages=identical, different_pages=changed,
              coverage_sha256=hashlib.sha256(a.coverage.read_bytes()).hexdigest(),
              manifest_sha256=hashlib.sha256(a.manifest.read_bytes()).hexdigest(),
              scope='Entire PNG comparison only. Inheritance also requires the archived hash-bound actual reading record. No reading event or mathematical event is generated.')
assert not a.output.exists(), 'Refusing to overwrite a comparison receipt.'
a.output.parent.mkdir(parents=True, exist_ok=True)
a.output.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(dict(output=str(a.output), identical=len(identical), changed=len(changed), different_pages=changed)))
