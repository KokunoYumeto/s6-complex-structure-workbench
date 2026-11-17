#!/usr/bin/env python3
"""Record the fifth-hour QA and current outcome table without creating a ZIP."""
from pathlib import Path
import datetime, json, re

root = Path(__file__).resolve().parents[1]
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
logs = {}
for stage in range(1, 5):
    p = root / 'build_logs' / f'draft19_{stage}.txt'
    logs[str(stage)] = [float(x) for x in re.findall(
        r'Overfull \\[hv]box \(([0-9.]+)pt', p.read_text())]
assert all(not values for values in logs.values())
qa = {'build': 'draft19', 'pdf_pages': 140, 'numbered_statements': 112,
      'bibliography_entries': 88, 'stage_overfull_pt': logs,
      'visually_inspected_pages': [1, 2, 3, 12, 21, 41, 48, 50, 61, 80, 90, 93, 94, 100, 120, 121, 140],
      'method': 'Two rendered contact sheets and enlarged pages1,41,120 inspected by root.',
      'observed_issues': [], 'scope': 'Visual sample and complete final-log audit, not every-page visual inspection.',
      'recorded_utc': now}
(root / 'qa' / 'draft19' / 'visual_inspection.json').write_text(json.dumps(qa, indent=2) + '\n')
assessment = {'assessment_utc': now, 'hour': 5, 'decision': 'CONTINUE',
              'main_progress': ['Actual monodromy zero by two specified methods with shared geometric pairings.',
                                'B4.8 excludes every stated semistable good-reduction Hopf interface.',
                                'B4.9 identifies the actual cusp torsor class as zero by an explicit section.',
                                'E2.5/6 prove central pencil persistence and positive-slope relative fibration.',
                                'A concrete parabolic Kato cap family is under geometric review.'],
              'unresolved': ['Actual global S6 analytic filling and least semistable exponent.',
                             'Topology and Chern numbers of that unconstructed filling.',
                             'Arbitrary deformation chains through unknown smooth members.'],
              'reason': 'The main construction and smooth-limit questions are still advancing; work is not limited to presentation or peripheral source collection.'}
(root / 'code' / 'progress_assessment_05.json').write_text(json.dumps(assessment, indent=2) + '\n')
p = root / 'code' / 'refresh_report.py'
s = p.read_text()
s = s.replace('| B.4 | B.4.1–B.4.7 |', '| B.4 | B.4.1–B.4.9 |')
s = s.replace('No actual global filling, descent resolution or least exponent is established.',
              'The direct Hopf interface is excluded by a mixed normal Chern class after every finite base change. The actual cusp torsor class is explicitly zero; nonzero abstract torsors change its germ. A parabolic Kato alternative is under review. No actual global filling, descent resolution or least exponent is established.')
s = s.replace('| E.2 | E.2.1–E.2.4 | Partial | Local deformation theory and irreducible-family separation proved; arbitrary chains open. |',
              '| E.2 | E.2.1–E.2.6 | Partial | Local deformation theory and irreducible-family separation are proved. Every smooth fixed-pair specialization has a holomorphic central pencil; positive canonical slope preserves the relative torus fibration and separates common smooth junctions. Arbitrary chains remain open. |')
s = s.replace('The fifth hourly checkpoint and progress assessment are due at17:38:56 UTC.',
              'The fifth-hour assessment continues work: the actual cusp class, normal-line obstruction and concrete parabolic-cap candidate advance the main filling problem, while smooth-limit persistence advances E.2. The fifth hourly checkpoint is scheduled for17:38:56 UTC.')
needle = 'External copyrighted PDFs and private OCR extracts are not republished.'
paragraph = ('Draft19 is the current clean140-page paper with112 registered statements and88 bibliography entries. All four build stages succeeded with zero overfull boxes. The final log has no unresolved references, citations or rerun warnings, and the full source/registry/bibliography audit passes. Seventeen pages were rendered and visually inspected: eleven spread across the paper and six additional pages carrying the fifth-hour propositions. The exact record is qa/draft19/visual_inspection.json. Intermediate assembly-timing mismatches and the corrected duplicate-heading audit parser are documented in root_fifth_hour_audit.md.\n\n')
assert 'Draft19 is the current clean140-page paper' not in s
s = s.replace(needle, paragraph + needle)
s = s.replace('"root_fifth_hour_audit.md","retention_record.md"',
              '"root_fifth_hour_audit.md","root_B48_referee.md","root_E25_E26_referee.md","retention_record.md"')
p.write_text(s)
print(json.dumps({'qa': qa, 'assessment': assessment}, indent=2))
