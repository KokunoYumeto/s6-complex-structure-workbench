#!/usr/bin/env python3
"""Record the ninth-hour progress assessment and an actually inspected build."""
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
assert len(rows) == audit['registry_rows'] and pages == qa['pdf_pages']
registry = {row['id']: row for row in rows}
assert all(registry[f'B.4.{i}']['status'] == 'Proved' for i in range(22, 28))
record = {
    'assessment_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'hour': 9,
    'decision': 'CONTINUE',
    'main_progress': [
        'B4.22 resolves the local fourfold corner and identifies its overlap with the actual linearized Tate collar.',
        'B4.23 proves exceptional-curve nonclosure and the exact rational-curve persistence obstruction to the fixed-base Kato replacement.',
        'B4.24 proves nonextension of the actual associated logarithmic torsor in its stated category, with all finite root changes retained.',
        'B4.25 excludes every proper analytic completion of the proposed unblown one-eigenvalue Hopf family by accumulating anticanonical resonances.',
        'B4.26 forces every component of a fixed-bidisc origin fibre to be a vertical threefold, by a finite-multisection trace argument.',
        'B4.27 proves that all finite point blowups of the base preserve the logarithmic obstruction.'
    ],
    'unresolved': [
        'Existence or nonexistence of an arbitrary analytic cap with the required vertical components.',
        'The implication from such a cap to an extending logarithmic torsor; a two-extending-sections comparison is under investigation.',
        'A construction of a model with trivial central dualizing bundle from an arbitrary transverse torus degeneration.',
        'The comparison between an arbitrary filling on the rank-one r-axis and the prescribed B4.19 axial model; the graph of the intrinsic marked map does not supply that identification.',
        'Global S6 filling, descent, least semistable exponent, central topology and the specified analytic component Chern numbers.'
    ],
    'reason': 'The ninth hour proves new necessary conditions on every fixed-bidisc cap and excludes whole proposed repair categories. The remaining unrestricted cap is being attacked through exact geometric and cohomological comparisons, so the user progress rule calls for continued work.'
}
if registry.get('B.4.28', {}).get('status') == 'Proved':
    record['main_progress'].append('B4.28 proves toric normalizations and torus dual complex under the explicit additional hypothesis of trivial central dualizing bundle; a rejected free-product argument is replaced by the marked hyperbolic-link and nonzero-period proof.')
if registry.get('B.4.29', {}).get('status') == 'Proved':
    record['main_progress'].append('B4.29 gives an explicit proper full-rank Tate example showing that invariant forms and the Gauss–Manin connection alone do not bound an affine origin; the stronger two-extending-sections question remains separate.')
(root/'code'/'progress_assessment_09.json').write_text(json.dumps(record, indent=2)+'\n')
build = (
    f'The ninth-hour checkpoint build is {tag}: {pages} pages, {len(rows)} statement rows and '
    f'{audit["bibliography_entries"]} bibliography entries. All four compiler stages succeeded with zero overfull boxes; '
    'the integration audit passes without unresolved references, citations or rerun warnings. '
    f'{len(qa["visually_inspected_pages"])} distinct rendered pages were visually inspected, including all ninth-hour proof pages. '
    f'The exact record is qa/{tag}/visual_inspection.json. Draft31 had no overfull box but failed its citation audit on an obsolete Grauert key; '
    'the alias was corrected and its failed audit is retained. The ninth-hour assessment is CONTINUE. '
    'Checkpoint09 is scheduled for 21:38:56 UTC and is not created earlier.'
)
p = root/'code'/'refresh_report.py'
s = p.read_text()
assert 'The ninth-hour checkpoint build is ' not in s
s = s.replace('External copyrighted PDFs and private OCR extracts are not republished.', build+'\n\nExternal copyrighted PDFs and private OCR extracts are not republished.')
p.write_text(s)
p = root/'sections'/'root_ninth_hour_audit.md'
p.write_text(p.read_text()+'\n\n## Inspected checkpoint build and hourly decision\n\n'+build+'\n')
print(json.dumps({'build':tag,'pages':pages,'rows':len(rows),'references':audit['bibliography_entries'],
                  'visual_pages':len(qa['visually_inspected_pages']),'assessment':record},indent=2))
