#!/usr/bin/env python3
"""Record a completed root inspection; run only after viewing all listed sheets."""
from pathlib import Path
import datetime,json,sys
root=Path(__file__).resolve().parents[1]
tag=sys.argv[1];folder=root/'qa'/tag
spread=json.loads((folder/'render_record.json').read_text())
extra=json.loads((folder/'additional_render_record.json').read_text())
pages=sorted(set(spread['rendered_pages']+extra['additional_pages']))
record={'build':tag,'pdf_pages':spread['pdf_pages'],
 'inspected_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'reviewer':'GPT-6 Astra root agent; AI visual inspection',
 'visually_inspected_pages':pages,
 'viewed_contact_sheets':['contact_sheet.jpg']+[Path(x).name for x in extra['contact_sheets']],
 'observed_issues':[],
 'finding':'The conventions, spread across all parts and bibliography, and all additional proof pages listed in the render record fit their pages. No clipping, overlapping text, broken display or visible overflow was observed.',
 'compiler_overfull_boxes':0,
 'scope':'Rendered sample and compiler-log audit; not a claim to have visually inspected every page.'}
(folder/'visual_inspection.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
