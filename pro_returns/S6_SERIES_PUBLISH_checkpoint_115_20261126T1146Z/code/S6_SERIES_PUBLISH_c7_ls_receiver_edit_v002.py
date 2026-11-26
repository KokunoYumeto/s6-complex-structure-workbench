"""Make the graph-basis inverse explicit in the stable LS receiver.

Refresh its local comparison references. All previous versions and all
actual streams are retained; no frozen fresh or global file is changed.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import difflib

W = Path(__file__).resolve().parents[1]
lane = W / 'agents/continuation7_iii_vertical_correction_receiving'
prefix = 'S6_SERIES_PUBLISH_III_02LS'
paths = [lane / f'{prefix}_receiving.tex',
         lane / f'{prefix}_post_exposure_auxiliaries.md',
         lane / f'{prefix}_comparison.md']
old = [path.read_bytes() for path in paths]
expected = ['51e26023340cbb59099c02bacdd2db510caba3262c0d5b1a5fa079b16d9e10b2',
            '3ce5fb7e09f1e666b80d16819e528d2052fd9b7370444583259341707af768a4',
            '490336c2f915b4fa26d2a081cd71ba253c728d2c8cb2fdfe1b4d2f1df29ebeb1']
assert [sha256(data).hexdigest() for data in old] == expected
backups = [lane / f'{prefix}_receiving_draft_v002.tex',
           lane / f'{prefix}_post_exposure_auxiliaries_draft_v003.md',
           lane / f'{prefix}_comparison_draft_v002.md']
for backup, data in zip(backups, old):
    assert not backup.exists()
    backup.write_bytes(data)
receiver = old[0].decode()
anchor = r'''On the23 generators its additional central term is
'''
addition = r'''Write $J$ for this ambient graph map. Its integral inverse is
\[
 J^{-1}(v_0,\ldots,v_4)
       =(-v_4,v_0-P_0v_4,\ldots,v_3-P_3v_4).
\]
The two composites cancel term by term, and the ordered product
identity gives $D_{\rm new}J=D_{\rm old}$.
Let $K_{\rm old},K_{\rm new}$ be the matrices of the chosen
primitive kernel bases, with their coordinate inverses on those
kernels. The graph coordinate maps are therefore exactly
\[
 Q=K_{\rm new}^{-1}JK_{\rm old},\qquad
 Q^{-1}=K_{\rm old}^{-1}J^{-1}K_{\rm new}.
\]
They are integral and inverse on the graph-kernel coordinates.
'''
assert receiver.count(anchor) == 1
receiver = receiver.replace(anchor, addition + anchor, 1)
new_receiver_hash = sha256(receiver.encode()).hexdigest()
new_receiver_lines = len(receiver.splitlines())
new_receiver_bytes = len(receiver.encode())
post, comparison = old[1].decode(), old[2].decode()
for text in (post, comparison):
    assert expected[0] in text
post = post.replace(expected[0], new_receiver_hash)
comparison = comparison.replace(expected[0], new_receiver_hash)
post = post.replace('The 772-line current receiver', f'The {new_receiver_lines}-line current receiver')
post = post.replace('Its initial whole reread plus the exact two-hunk reread covers every\nfinal line.',
                    'Its initial whole reread plus the two retained exact edit diffs covers\nevery final line.')
comparison = comparison.replace('772 lines,34453 bytes,', f'{new_receiver_lines} lines,{new_receiver_bytes} bytes,')
comparison = comparison.replace('* receiver_v001, receiver_edit_v001;',
                                '* receiver_v001, receiver_edit_v001, receiver_edit_v002;')
comparison = comparison.replace('`code/S6_SERIES_PUBLISH_c7_ls_receiver_edit_v001.diff`,',
                                '`code/S6_SERIES_PUBLISH_c7_ls_receiver_edit_v001.diff`,\n'
                                '`code/S6_SERIES_PUBLISH_c7_ls_receiver_edit_v002.diff`,', 1)
scope = r'''

Root's complete receiver reading requested the explicit graph-basis
definition in its70/59 comparison. The final addition writes the ambient
inverse J^{-1}(v_0,...,v_4)=(-v_4,v_0-P_0v_4,...,v_3-P_3v_4), then
Q=K_new^{-1}J K_old and Q^{-1}=K_old^{-1}J^{-1}K_new on the primitive
kernel lattices. The two ambient composites cancel term by term;
D_new J=D_old follows from the ordered product identity. The retained
source, actual stdout/stderr and exact change are
`code/S6_SERIES_PUBLISH_c7_ls_receiver_edit_v002.py`, `.out`, `.err`
and `.diff`. Only the receiver and these local comparison references
changed; all frozen fresh and previous execution evidence stayed fixed.
'''
post += scope
comparison += scope
new = [receiver, post, comparison]
diff = ''
for path, backup, before, after in zip(paths, backups, old, new):
    path.write_text(after, newline='\n')
    diff += ''.join(difflib.unified_diff(before.decode().splitlines(True), after.splitlines(True),
                                       fromfile=backup.name, tofile=path.name))
diffpath = W / 'code/S6_SERIES_PUBLISH_c7_ls_receiver_edit_v002.diff'
assert not diffpath.exists()
diffpath.write_text(diff, newline='\n')
fresh = W / 'agents/continuation7_iii_vertical_correction' / f'{prefix}_fresh_derivation.md'
assert sha256(fresh.read_bytes()).hexdigest() == 'ee6cbed56c156a8f590c0f7926121a9a3baf5ba4fdbccf9302d56a7df126ef7d'
print('COMPLETE', datetime.now(timezone.utc).isoformat())
for path in paths + [diffpath]:
    data = path.read_bytes()
    print('FILE', path.relative_to(W), 'LINES', len(data.splitlines()),
          'BYTES', len(data), 'SHA256', sha256(data).hexdigest())
print(diff, end='')
print('SCOPE explicit inverse maps and local references only; frozen fresh and global files unchanged.')
