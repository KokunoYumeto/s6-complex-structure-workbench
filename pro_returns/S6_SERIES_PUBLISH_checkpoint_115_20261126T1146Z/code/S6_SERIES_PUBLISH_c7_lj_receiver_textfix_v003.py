"""Apply the final bounded LJ receiver presentation changes; no global writes."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import difflib
import re

root = Path(__file__).resolve().parents[1]
lane = root / 'agents/continuation7_iii_mixed_three_receiving'
path = lane / 'S6_SERIES_PUBLISH_III_02LJ_receiving.tex'
old = path.read_text()
assert sha256(path.read_bytes()).hexdigest() == '387291cff814f9f5cc30df0480a09cc275a3a5b767a3bcfc4c2e32e4c56cc003'
start = old.index(r'\paragraph{10a. Relative equivariant injection and the complete three-primary bordism class.}')
end = old.index('For completeness the three-primary spin-bordism map is', start)
new = old[:start] + r'\paragraph{10a. The complete three-primary bordism class.}' + '\n\n' + old[end:]
oldline = next(line for line in new.splitlines() if r'\rightleftarrows}}' in line)
assert oldline.endswith('\\')
new = new.replace(oldline, oldline[:-1], 1)
marker = '\\end{proof}\n\nThe exact calculation uses'
assert new.count(marker) == 1
new = new.replace(marker, '\\paragraph{14. Exact arithmetic checks.}\n\nThe exact calculation uses', 1)
new = new.rstrip() + '\n\\end{proof}\n'
for pattern in (r'\\label\{([^}]+)\}', r'\\hypertarget\{([^}]+)\}', r'\\tag\{([^}]+)\}'):
    assert sorted(re.findall(pattern, old)) == sorted(re.findall(pattern, new))
assert new.count('\\begin{proof}') == new.count('\\end{proof}') == 1
assert 'Relative equivariant injection' not in new
path.write_text(new, newline='\n')
diffpath = root / 'code/S6_SERIES_PUBLISH_c7_lj_receiver_textfix_v003.diff'
diffpath.write_text(''.join(difflib.unified_diff(old.splitlines(True), new.splitlines(True),
    fromfile='LJ_receiver_before_v003', tofile='LJ_receiver_after_v003')), newline='\n')
print('Completed UTC:', datetime.now(timezone.utc).isoformat())
print('Receiver lines:', len(new.splitlines()))
print('Receiver SHA256:', sha256(path.read_bytes()).hexdigest())
print('Diff SHA256:', sha256(diffpath.read_bytes()).hexdigest())
print('Changes: moved the alternate whole-circle argument to the post-exposure checking scope; retained the used bordism map; removed one stray TeX backslash; moved the computation paragraph inside the single proof.')
print('Permanent label/hypertarget/tag multisets unchanged; one proof environment; fresh files untouched.')
