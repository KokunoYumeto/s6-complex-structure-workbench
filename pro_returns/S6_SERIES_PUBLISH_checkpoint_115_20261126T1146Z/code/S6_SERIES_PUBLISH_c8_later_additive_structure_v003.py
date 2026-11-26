#!/usr/bin/env python3
"""Promote the wholly reviewed additive unit to four actual subsections."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import csv
import difflib

ROOT = Path(__file__).resolve().parents[1]
UNIT = ROOT / 'agents/continuation8_iii_integration/units/later/elliptic_additive_profiles.tex'
OUT = ROOT / 'agents/continuation8_iii_later'
old = UNIT.read_text()
assert sha256(old.encode()).hexdigest() == '177248ad21f8807d63e0018f2e0f1524020719fb3682c98e6af76f41e85706d5'
changes = [
    ('maps:src:D.2.17', r'\subsection{Original additive profiles}', r'\section{Original additive profiles}'),
    ('maps:src:D.2.17', r'\subsubsection{Two additive profiles}', r'\subsection{Two additive profiles}'),
    ('maps:src:D.2.18', r'\subsubsection{The three-component cusp}', r'\subsection{The three-component cusp}'),
    ('maps:src:D.2.20', r'\subsubsection{Six primitive original families}', r'\subsection{Six primitive original families}'),
    ('maps:src:D.2.21', r'\subsubsection{A mixed original and logarithmic pair}', r'\subsection{A mixed original and logarithmic pair}')
]
table = OUT / 'S6_SERIES_PUBLISH_III_additive_publication_defects.tsv'
with table.open(newline='') as stream:
    rows = list(csv.DictReader(stream, delimiter='\t'))
assert len(rows) == 106
new = old
for sid, before, after in changes:
    assert new.count(before) == 1
    pos = new.index(before)
    rows.append(dict(change_id=f'c8-III-additive-{len(rows)+1:03}', type='D14',
        statement_id=sid, old_location='elliptic_additive_profiles.tex line ' + str(new[:pos].count('\n')+1),
        old_page='pending final page concordance', new_location='same line, promoted section level',
        new_page='pending final build', old_text=before, new_text=after,
        reason='Root requested actual section/subsection progress units after the source-local reading; promote the enclosing heading and four mathematical units without changing any statement, proof, label or target.',
        review_status='exact heading-only reopening reviewed; actual final placement and global gates remain pending'))
    new = new.replace(before, after, 1)
inverse = new
for sid, before, after in reversed(changes):
    assert inverse.count(after) == 1
    inverse = inverse.replace(after, before, 1)
assert inverse == old
with table.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, list(rows[0]), delimiter='\t', lineterminator='\n')
    writer.writeheader(); writer.writerows(rows)
(OUT / 'S6_SERIES_PUBLISH_III_additive_publication_v003.diff').write_text(
    ''.join(difflib.unified_diff(old.splitlines(True), new.splitlines(True),
                               fromfile='additive_v002', tofile='additive_v003')), newline='\n')
UNIT.write_text(new, newline='\n')
now = datetime.now(timezone.utc).isoformat()
digest = sha256(new.encode()).hexdigest()
review = OUT / 'S6_SERIES_PUBLISH_III_additive_publication_review.md'
text = review.read_text()
text = text.replace('177248ad21f8807d63e0018f2e0f1524020719fb3682c98e6af76f41e85706d5', digest, 1)
text = text.replace('Last source edit completed at 2026-11-25T16:48:28.884418+00:00.', 'Last source edit completed at ' + now + '.')
text += '\n## Heading-only reopening for the actual progress units\n\n'
text += ('At root request, the enclosing heading is now a section and its four\n'
         'mathematical units are subsections. The previous 2965-line version\n'
         'had SHA-256 177248ad21f8807d63e0018f2e0f1524020719fb3682c98e6af76f41e85706d5.\n'
         'The exact five replacements have a checked inverse recovering that\n'
         'entire version. No mathematical, label, target or proof change occurs.\n'
         'The local defect table now has 111 rows; the additional five are D14.\n'
         'The four actual subsection identities and their separate criterion\n'
         'evidence are in S6_SERIES_PUBLISH_III_additive_actual_units.md.\n'
         'Actual final placement and global publication gates still require root.\n')
review.write_text(text, newline='\n')
print('UTC', now)
print('OUTPUT', len(new.splitlines()), digest)
print('EXACT_HEADING_MAP_AND_INVERSE', len(changes), 'LOCAL_DEFECT_ROWS', len(rows))
for sid, before, after in changes[1:]:
    print('ACTUAL_SUBSECTION', sid, new[:new.index(after)].count('\n')+1, after)
print('ALL_STATEMENT_AND_PROOF_BYTES_UNCHANGED; NO_SHARED_WRITES')
