#!/usr/bin/env python3
"""Record the root agent's actual visual inspection of draft23 on 15 Nov 2026."""
from pathlib import Path
import datetime, json

root = Path(__file__).resolve().parents[1]
folder = root / 'qa' / 'draft23'
spread = json.loads((folder / 'render_record.json').read_text())
new = json.loads((folder / 'additional_render_record.json').read_text())
pages = sorted(set(spread['rendered_pages'] + new['additional_pages']))
record = {
    'build': 'draft23', 'pdf_pages': spread['pdf_pages'],
    'inspected_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'visually_inspected_pages': pages,
    'method': 'Root viewed the spread contact sheet and both new-statement contact sheets individually; page 139 was additionally viewed at full rendered resolution.',
    'contact_sheets': [spread['contact_sheet']] + new['contact_sheets'],
    'enlarged_pages': [139],
    'observed_issues': [],
    'observations': 'Sampled pages have consistent margins, legible mathematical displays and bibliography, clear hierarchy, and no observed clipping or overflow. The new normal-bundle table remains within the text area. This is a sample visual inspection, not a claim that every page was visually read.',
    'build_overfull_boxes': 0,
}
(folder / 'visual_inspection.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
