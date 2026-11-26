#!/usr/bin/env python3
"""Correct the exact printed-page locator in the final LF recognition citation.

This is a citation-only assembly step. All earlier sources and outputs
remain retained, and canonical/frozen mathematical files remain read-only.
"""
from pathlib import Path
from hashlib import sha256

root = Path(__file__).resolve().parent.parent
target = root / 'agents/continuation7_iii_three_primary_receiving/S6_SERIES_PUBLISH_III_02LF_receiving.tex'
canonical = root / 'S6_SERIES_PUBLISH_III.tex'
canonical_before = canonical.read_bytes()
old = target.read_bytes()
assert sha256(old).hexdigest() == 'f3d448b63642ea9dec0aa7cc8eeb2fc240889ccc3c0b94168495e260f6d2c991'
before = r'\cite[Theorem~3, p.~795; Theorem~5 and \S4.1, pp.~807,809--810]{manZhubr75}.'
after = r'\cite[Theorem~3, p.~795; Theorem~5, p.~796; \S4.1, pp.~809--810]{manZhubr75}.'
text = old.decode()
assert text.count(before) == 1
new = text.replace(before, after, 1).encode()
assert new.replace(after.encode(), before.encode(), 1) == old
target.write_bytes(new)
assert canonical.read_bytes() == canonical_before
print('CITATION_ONLY_EXACT_PATCH; THEOREM5_PRINTED_796; CANONICAL_UNCHANGED')
print('RECEIVER', target.relative_to(root), 'LINES', len(new.splitlines()),
      'SHA256', sha256(new).hexdigest())
