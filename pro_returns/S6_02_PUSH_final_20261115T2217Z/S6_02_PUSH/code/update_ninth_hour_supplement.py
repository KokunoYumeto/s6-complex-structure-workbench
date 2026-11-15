#!/usr/bin/env python3
"""Update the report only after B.4.28 and B.4.29 are integrated."""
from pathlib import Path
import csv
root = Path(__file__).resolve().parents[1]
registry = {r['id']: r for r in csv.DictReader((root/'S6_02_PUSH_results.csv').open())}
assert all(registry[key]['status'] == 'Proved' for key in ['B.4.28', 'B.4.29'])
p = root/'code'/'refresh_report.py'
s = p.read_text()
lines = s.splitlines()
for index, line in enumerate(lines):
    if line.startswith(('| B.3 |', '| B.4 |', '| Lead 5 |')):
        line = line.replace('B.4.1–B.4.27', 'B.4.1–B.4.29').replace('B.4.19–B.4.27', 'B.4.19–B.4.29')
        if line.startswith('| B.4 |'):
            line = line.replace('A general cap need not be a log torsor;', 'Under the additional trivial-central-dualizing hypothesis, maximal torus degenerations have toric normalization pairs and torus dual complex. An explicit full-rank counterexample shows that invariant forms alone do not control an affine origin. A general cap need not be a log torsor;')
        lines[index] = line
s = '\n'.join(lines)+'\n'
needle = "'root_ninth_hour_audit.md']"
replacement = "'root_ninth_hour_audit.md', 'D_B4428_referee.md', 'D_B4429_referee.md', 'B_forms_translation_report.md', 'E_B_fullrank_completion_audit.md', 'D_vertical_kato_base_attempts.md']"
assert needle in s
s = s.replace(needle, replacement, 1)
p.write_text(s)
print('Report table and detailed records updated for the conditional B.4.28 theorem and the precise B.4.29 counterexample.')
