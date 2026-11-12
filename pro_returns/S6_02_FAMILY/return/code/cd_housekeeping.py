"""Label stopped exploratory output and verify final C-D status wording."""
from pathlib import Path
base=Path(__file__).resolve().parent
out=base/'cd_interval_cover.out'
label=(
 '\nEXPLORATORY RUN STOPPED: interrupted after the corrected independent '
 'global certificate passed.\n'
 'This output is a partial search log, not a completed interval certificate.\n'
 'The proof uses f_interval_parallel_certificate.json and '
 'f_interval_verify.out.txt.\n'
)
text=out.read_text()
if 'EXPLORATORY RUN STOPPED:' not in text:
 out.write_text(text+label)
print('Labelled cd_interval_cover.out as stopped, partial, and non-certifying.')
root=base.parent
tex=(root/'sections/CD.tex').read_text()
report=(root/'sections/CD_report.md').read_text()
for stale in ['C.2.3; Open','unknown maximum','Global maximum awaits','Pending the final global']:
 assert stale not in tex+report, stale
assert 'C.2.3; Proved, with interval certificate' in tex
assert '| C.2 | C.2.1--C.2.3 | (a)' in report
assert 'C.3.3; Open' in tex
print('Verified: C.2 proved; no stale open-maximum wording; only C.3 compact replacement remains open in C-D.')
print('Exploratory execution session was interrupted and returned exit code130.')
