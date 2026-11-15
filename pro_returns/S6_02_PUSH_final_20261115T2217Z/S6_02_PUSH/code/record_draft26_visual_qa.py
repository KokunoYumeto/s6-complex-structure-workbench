#!/usr/bin/env python3
"""Record root's completed inspection of the draft26 rendered sample."""
from pathlib import Path
import datetime,json
root=Path(__file__).resolve().parents[1]
folder=root/'qa'/'draft26'
spread=[1,2,3,12,27,53,79,104,130,156,182]
extra=json.loads((folder/'additional_render_record.json').read_text())
pages=sorted(set(spread+extra['additional_pages']))
record={
 'build':'draft26','pdf_pages':182,
 'inspected_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'reviewer':'GPT-6 Astra root agent; AI visual inspection',
 'visually_inspected_pages':pages,
 'viewed_contact_sheets':['contact_sheet.jpg','seventh_hour_new_statements_1.jpg',
                          'seventh_hour_new_statements_2.jpg','seventh_hour_new_statements_3.jpg'],
 'observed_issues':[],
 'finding':'First-page conventions, spread across all parts and bibliography, and seventh-hour proofs fit their pages. No clipping, overlapping text, broken display or visible overflow was observed in this sample.',
 'compiler_overfull_boxes':0,
 'scope':'Rendered sample plus compiler-log audit, not a claim to have visually read every page.'
}
(folder/'visual_inspection.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
