"""Add the literal v002 round-trip scope and complete local source locators."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import difflib

W = Path(__file__).resolve().parents[1]
lane = W / 'agents/continuation7_iii_vertical_correction_receiving'
prefix = 'S6_SERIES_PUBLISH_III_02LS'
post = lane / f'{prefix}_post_exposure_auxiliaries.md'
comparison = lane / f'{prefix}_comparison.md'
old_post, old_comparison = post.read_bytes(), comparison.read_bytes()
assert sha256(old_post).hexdigest() == 'c386ddc9c79a4445c73322c8caf645f07976ec17027cb0f359831913e61b29a5'
assert sha256(old_comparison).hexdigest() == 'd7611d15a5b218a57d7763d75a26ff95082c6f74e326efbc4e163ab39afba4ed'
backups = [lane / f'{prefix}_post_exposure_auxiliaries_draft_v002.md',
           lane / f'{prefix}_comparison_draft_v001.md']
for path, data in zip(backups, (old_post, old_comparison)):
    assert not path.exists()
    path.write_bytes(data)
post_text = old_post.decode()
anchor = 'proved inverse. Root chose v001 as the canonical reading form.\n'
assert post_text.count(anchor) == 1
addition = r'''

At root's request the118-line formatting-only program
`code/S6_SERIES_PUBLISH_c7_ls_post_readback_roundtrip_v001.py` then
read the actual v002 stdout. It parsed every actual replacement back
to v001, and independently regenerated every v002 byte from v001
plus six retained metadata lines. Both compositions were checked
against the actual files. The six metadata coordinates, including
START2026-11-25T10:04:29.498936+00:00 and
COMPLETE2026-11-25T10:04:32.078365+00:00, are printed literally in
its13-line actual `.out`. The run completed at
2026-11-25T10:41:06.871597+00:00, with an existing zero-byte `.err`.
The entire118-line source and all13 stdout lines were read. Thus
root can account for every v002 byte by the exact inverse map and
the literal extra metadata, without duplicate manual display of its
2044 lines. This was a formatting check; no finite mathematical
validator was rerun.
'''
post_text = post_text.replace(anchor, anchor + addition, 1)
post_text += r'''

The complete local comparison was written by
`code/S6_SERIES_PUBLISH_c7_ls_notes_v001.py` (559 lines), whose
successful six-line stdout is retained with its actual empty stderr.
Its exact109-line change to the previous post-exposure note is in
`code/S6_SERIES_PUBLISH_c7_ls_notes_v001.diff`. The present metadata
addition and all-source locator addition have their retained source,
actual streams and exact diff under
`code/S6_SERIES_PUBLISH_c7_ls_notes_edit_v002`.
The prior423-line and515-line post-exposure notes and the prior418-line
comparison are preserved as draft files; their bytes are not rewritten.
'''
comparison_text = old_comparison.decode()
anchor = 'The complete execution table, exact timestamps, all limitations, the\n'
assert comparison_text.count(anchor) == 1
addition = r'''At root's request the formatting-only118-line
`code/S6_SERIES_PUBLISH_c7_ls_post_readback_roundtrip_v001.py`
also parsed the actual v002 stdout back to v001 and independently
regenerated all v002 bytes from v001 plus its six literal metadata
coordinates. Its13-line successful stdout prints all six, including
the actual START/COMPLETE values; its actual stderr exists and is empty.
This run completed2026-11-25T10:41:06.871597+00:00 and was wholly read.
It supplies exact mapped coverage of all v002 output without a duplicate
manual whole-reading claim or another mathematical execution.

All post-exposure execution basenames are listed here. Each has the
prefix `code/S6_SERIES_PUBLISH_c7_ls_` and the actual `.py`, `.out`
and `.err` files:

* historical_retrieve_v001, historical_retrieve_v002,
  historical_retrieve_v003;
* historical_retain_v001, historical_inspect_v001,
  historical_extract_v002;
* post_local_v001, post_relations_v001, post_obstructions_v001;
* post_readback_v001, post_readback_v002,
  post_readback_roundtrip_v001;
* receiver_v001, receiver_edit_v001;
* notes_v001, notes_edit_v002;
* receive_records_v001, the local guard/defect/event proposal preparation.

Exact textual changes are retained as
`code/S6_SERIES_PUBLISH_c7_ls_receiver_edit_v001.diff`,
`code/S6_SERIES_PUBLISH_c7_ls_notes_v001.diff` and
`code/S6_SERIES_PUBLISH_c7_ls_notes_edit_v002.diff`.
The receiver and note drafts before those changes are retained in this
receiving lane. The proposed record writer has no canonical/global
mutation; its actual output supplies the final exact guard and proposal
readback.

The frozen fresh source versions are separately preserved under the
same code prefix: os45_bar_v001, output_readback_v001,
output_readback_v002, star_order_v001, finish_edit_v001,
finish_v001 and finish_edit_v002, with every actual stream. The earlier
finish_v001_preexecute.py is a retained unexecuted version and has no
invented output. The two finish-edit diff files remain present. Root's
primary_pages_v001 source and actual streams record its seven primary
image renders. These completed fresh records were not rerun or changed
during the post-exposure work.

'''
comparison_text = comparison_text.replace(anchor, addition + anchor, 1)
post.write_text(post_text, newline='\n')
comparison.write_text(comparison_text, newline='\n')
diff = ''.join(difflib.unified_diff(old_post.decode().splitlines(True), post_text.splitlines(True),
                                  fromfile=backups[0].name, tofile=post.name))
diff += ''.join(difflib.unified_diff(old_comparison.decode().splitlines(True), comparison_text.splitlines(True),
                                   fromfile=backups[1].name, tofile=comparison.name))
diffpath = W / 'code/S6_SERIES_PUBLISH_c7_ls_notes_edit_v002.diff'
assert not diffpath.exists()
diffpath.write_text(diff, newline='\n')
print('COMPLETE', datetime.now(timezone.utc).isoformat())
for path in (post, comparison, diffpath):
    data = path.read_bytes()
    print('FILE', path.relative_to(W), 'LINES', len(data.splitlines()),
          'BYTES', len(data), 'SHA256', sha256(data).hexdigest())
print('SCOPE exact actual-output coverage and source locators only; receiver and frozen fresh unchanged.')
