"""Retain and make two precise wording changes in the LS receiver only."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import difflib

W = Path(__file__).resolve().parents[1]
lane = W / 'agents/continuation7_iii_vertical_correction_receiving'
path = lane / 'S6_SERIES_PUBLISH_III_02LS_receiving.tex'
old = path.read_bytes()
assert sha256(old).hexdigest() == 'd4c66a5e1229ad09472334871803f083678a8c985504627f3f75762369c52f57'
backup = lane / 'S6_SERIES_PUBLISH_III_02LS_receiving_draft_v001.tex'
assert not backup.exists()
backup.write_bytes(old)
text = old.decode()
changes = [
    (r'For a local elliptic matrix $B$, choose $z_G$ with $(B-I)z_G=g$' + '\n'
     r'and put $J=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$.',
     r'For a local elliptic matrix $B$, choose a solution $z_G$ of' + '\n'
     r'$(B-I)z_G=g$ with least positive denominator, and put' + '\n'
     r'$J=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$.'),
    (r'Lift a signed basis word for $x$ by the ordered images of its' + '\n'
     r'generators under $T$. Its central correction $f_T(x)$ is the' + '\n'
     r'difference from $\Lambda^2T\sum_{i<j}x_ix_je_{ij}$.',
     r'Lift a signed basis word for $x$ by the ordered images of its' + '\n'
     r'generators under $T$, and denote the central coordinate of that' + '\n'
     r'lifted word by $z_T(x)$. With this literal word convention,' + '\n'
     r'\[' + '\n'
     r' f_T(x)=\Lambda^2T\sum_{i<j}x_i x_j e_{ij}-z_T(x).' + '\n'
     r'\]'),
]
for before, after in changes:
    assert text.count(before) == 1
    text = text.replace(before, after, 1)
new = text.encode()
diff = ''.join(difflib.unified_diff(old.decode().splitlines(True),
                                  text.splitlines(True),
                                  fromfile=backup.name, tofile=path.name))
diffpath = W / 'code/S6_SERIES_PUBLISH_c7_ls_receiver_edit_v001.diff'
assert not diffpath.exists()
diffpath.write_text(diff, newline='\n')
path.write_bytes(new)
print('COMPLETE', datetime.now(timezone.utc).isoformat())
print('OLD', sha256(old).hexdigest(), 'BYTES', len(old))
print('NEW', sha256(new).hexdigest(), 'BYTES', len(new), 'LINES', len(text.splitlines()))
print('DIFF', diffpath.relative_to(W), 'SHA256', sha256(diff.encode()).hexdigest())
print(diff, end='')
print('SCOPE two wording changes; no canonical, global, historical or frozen fresh mutation.')
