#!/usr/bin/env python3
"""Record the final orientation correction and replace the checkpoint build tag."""
from pathlib import Path
import json,sys
root=Path(__file__).resolve().parents[1]
tag=sys.argv[1]
audit=json.loads((root/'code'/f'deliverable_audit_{tag}.json').read_text())
qa=json.loads((root/'qa'/tag/'visual_inspection.json').read_text())
assert audit['passed'] and not qa['observed_issues']
pages=qa['pdf_pages'];visual=len(qa['visually_inspected_pages'])
old=('The seventh-hour checkpoint build is draft26: 182 pages, 134 statement rows and 102 bibliography entries.')
new=(f'The seventh-hour checkpoint build is {tag}: {pages} pages, 134 statement rows and 102 bibliography entries.')
for p in [root/'code'/'refresh_report.py',root/'sections'/'root_seventh_hour_audit.md']:
    s=p.read_text().replace(old,new).replace('qa/draft26/visual_inspection.json',f'qa/{tag}/visual_inspection.json')
    s=s.replace('29 distinct pages were rendered and visually inspected',f'{visual} distinct pages were rendered and visually inspected')
    p.write_text(s)
p=root/'sections'/'root_seventh_hour_audit.md'
s=p.read_text()
s+='''

## Last orientation correction before checkpoint07

A final global-marking check found that B.4.18 had selected the negative affine deck for a positive q-loop while comparing it with the clockwise convention of B.3.1--2. The actual required choice is +b,+F for the positive q-root generator: its component shift is +1, and the inverse clockwise generator has shift minus one. Both-sign local constructions exist; this correction selects the one compatible with the finite shifts plus four and minus three. The source, CSV and report were corrected, and the map direction is now explicit: the Jacobian maps to the +b torsor by zeta plus F, and the retained actual family maps by zeta minus sigma plus F. Root, limits_ab and boundary_d checked the orientation. The old auxiliary-gauge obstruction is marked as inapplicable to that retained comparison, because its first-coordinate log-r term cancels.

The corrected build was made before saving checkpoint07. This necessary last correction delayed the archive by a few minutes beyond its19:38:56 target; no extra or earlier checkpoint was created. The earlier clean draft26 build and its visual record are retained as intermediate verification, and the current PDF is the corrected build stated above.
'''
p.write_text(s)
p=root/'code'/'record_checkpoint07.py'
s=p.read_text().replace('draft26',tag).replace('182',str(pages)).replace('==29',f'=={visual}').replace('a29-page',f'a{visual}-page')
p.write_text(s)
print(json.dumps({'corrected_build':tag,'pages':pages,'visual_pages':visual,'orientation':'positive q +1; clockwise q -1'},indent=2))
