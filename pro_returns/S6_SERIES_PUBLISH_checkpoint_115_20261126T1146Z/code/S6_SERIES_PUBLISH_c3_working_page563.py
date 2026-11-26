"""Record the actual bounded visual reading of the repaired working page."""
from S6_SERIES_PUBLISH_c3_edit import *

record = """

## Third continuation: working page 563, 22 November 2026

The root rendered and actually read page 563 of the 801-page working PDF
after the root-surface display repair. The first attempted image output
was truncated and received no reading credit; the successful second image
was read in full. It contains the conclusion of Lemma 34.1, the heading
Elliptic root fillings, the complete statement of Lemma 34.2, and its
proof through the canonical-divisor computation. The two-line defining
display (34.8), the inverse product maps, and displays (34.9)--(34.10)
fit within the text area. No clipping, overlap, missing glyph or unresolved
reference was observed. The surrounding proof text and page break are
legible. The integrated log has three overfull boxes, maximum 1.7175 pt,
and none above 2 pt. This is a working-layout reading only; every page of
the final integrated candidate remains open.
"""
path = ROOT / 'S6_SERIES_PUBLISH_reading_II.md'
assert '## Third continuation: working page 563' not in path.read_text()
with path.open('a', newline='\n') as handle:
    handle.write(record)
add_event('lem:II:elliptic-root-surface', 'II-C3-WORKING-PAGE563',
          'used and rechecked in this run',
          'Root actually read the rendered working page 563 in full after the defining display was split. Statement, inverse product maps and canonical-divisor calculation are legible; no clipping, overlap, missing glyph or unresolved reference observed. The earlier truncated image attempt received no credit. Working-layout reading only; no final-page or independent mathematical-check credit.',
          'S6_SERIES_PUBLISH_reading_II.md; build/II_c3_working/S6_SERIES_PUBLISH_II.pdf, page 563',
          source='code/S6_SERIES_PUBLISH_c3_working_page563.py')
print('Recorded the actual full visual reading of working page 563; final-page rows stay open.')
