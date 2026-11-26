#!/usr/bin/env python3
"""Insert LF's small printed tag after removing the machine header.

This is an exact publication-format patch, with all prior sources and
outputs retained and no canonical or frozen mathematical mutation.
"""
from pathlib import Path
from hashlib import sha256

root = Path(__file__).resolve().parent.parent
target = root / 'agents/continuation7_iii_three_primary_receiving/S6_SERIES_PUBLISH_III_02LF_receiving.tex'
canonical = root / 'S6_SERIES_PUBLISH_III.tex'
canonical_before = canonical.read_bytes()
old = target.read_bytes()
assert sha256(old).hexdigest() == '93d45ec0d03b4bbfbe6bf40da50eb3cfedb05b57f78a8f7227e12eadc8a54a01'
before = '\\label{maps:src:D.2.39}\n'
after = before + '\\textnormal{\\small tag 02LF.}\n'
text = old.decode()
assert text.count(before) == 1
new = text.replace(before, after, 1).encode()
assert new.replace(after.encode(), before.encode(), 1) == old
target.write_bytes(new)
assert canonical.read_bytes() == canonical_before
print('PRINTED_TAG_ONLY_EXACT_PATCH; PERMANENT_IDENTITIES_UNCHANGED; CANONICAL_UNCHANGED')
print('RECEIVER', target.relative_to(root), 'LINES', len(new.splitlines()),
      'SHA256', sha256(new).hexdigest())
