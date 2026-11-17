#!/usr/bin/env python3
"""Record the eighth-hour progress decision and the inspected checkpoint build."""
from pathlib import Path
import csv, datetime, json, sys
import fitz

root = Path(__file__).resolve().parents[1]
tag = sys.argv[1]
audit = json.loads((root/'code'/f'deliverable_audit_{tag}.json').read_text())
qa = json.loads((root/'qa'/tag/'visual_inspection.json').read_text())
stages = json.loads((root/'build_logs'/f'{tag}_summary.json').read_text())
assert audit['passed'] and not qa['observed_issues']
assert len(stages) == 4 and all(x['returncode'] == 0 and not x['overfull_pt'] for x in stages)
pages = len(fitz.open(root/'S6_02_PUSH_paper.pdf'))
rows = list(csv.DictReader((root/'S6_02_PUSH_results.csv').open()))
assert len(rows) == audit['registry_rows']
registry = {x['id']: x for x in rows}
assert all(registry[x]['status'] == 'Proved' for x in ['B.4.19','B.4.20','E.2.4','E.2.20','E.2.21','E.2.22','E.2.23','E.2.24'])
record = {
    'assessment_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'hour': 8, 'decision': 'CONTINUE',
    'main_progress': [
        'B4.19 constructs the actual global partial filling, including all finite and cusp overlaps, over (P1 x Delta_r) minus the single missing origin.',
        'B4.20 embeds the actual varying Tate interface and its exact normal factor into a proper Kato family and proves the precise limits of a direct plumbing.',
        'E2.20 and E2.21 identify the actual analytic cusp and every smooth full punctured-disc specialization with the prescribed interior family.',
        'E2.22 and E2.23 prove propagation from a known open subset and separation under arbitrary connected holomorphic deformation chains.',
        'E2.24 gives clopen fixed-pair loci in the C-infinity space of integrable structures, resolving the continuous-family interpretation of E2.',
        'The degree-one Kato repair and its normal-restored local period model are being tested as a new route to the missing origin; no full cap is inferred.'
    ],
    'unresolved': [
        'A proper analytic completion at the missing origin, the global S6 filling, descent and least semistable exponent.',
        'Topology and component-derived Chern numbers of the unconstructed analytic filling.',
        'Exact generic-fibre and second-period identification for the new Kato repair and local plumbing candidates.'
    ],
    'reason': 'The eighth hour resolves the remaining deformation-class item and constructs the actual global partial family. The main missing-origin construction is still advancing through explicit geometric comparisons, so the user progress rule calls for continued work.'
}
if 'B.4.21' in registry and registry['B.4.21']['status'] == 'Proved':
    record['main_progress'].append('B4.21 provides the reviewed degree-one Kato repair and its actual relative Tate-line neighbourhood, with the full cap explicitly still open.')
(root/'code'/'progress_assessment_08.json').write_text(json.dumps(record, indent=2)+'\n')
build = (
    f'The eighth-hour checkpoint build is {tag}: {pages} pages, {len(rows)} statement rows and '
    f'{audit["bibliography_entries"]} bibliography entries. All four compiler stages succeeded with zero overfull boxes; '
    f'the final integration audit passes without unresolved references, citations or rerun warnings. '
    f'{len(qa["visually_inspected_pages"])} distinct rendered pages were visually inspected, including all listed new proof pages. '
    f'The exact record is qa/{tag}/visual_inspection.json. Draft28 had one overfull box of83.39786pt in an unbreakable code path; '
    'the path was made breakable and the later clean build has no overfull boxes. The eighth-hour assessment is CONTINUE. '
    'Checkpoint08 is scheduled for20:38:56UTC and is not created earlier.'
)
p = root/'code'/'refresh_report.py'
s = p.read_text()
assert 'The eighth-hour checkpoint build is ' not in s
s = s.replace('External copyrighted PDFs and private OCR extracts are not republished.', build+'\n\nExternal copyrighted PDFs and private OCR extracts are not republished.')
p.write_text(s)
p = root/'sections'/'root_eighth_hour_audit.md'
p.write_text(p.read_text()+'\n\n## Inspected checkpoint build and hourly decision\n\n'+build+'\n')
print(json.dumps({'build':tag,'pages':pages,'rows':len(rows),'references':audit['bibliography_entries'],
                  'visual_pages':len(qa['visually_inspected_pages']),'assessment':record},indent=2))
