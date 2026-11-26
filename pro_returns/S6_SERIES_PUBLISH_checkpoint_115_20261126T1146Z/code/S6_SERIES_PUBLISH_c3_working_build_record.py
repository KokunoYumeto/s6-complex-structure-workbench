"""Record a completed integrated working build without final-page credit."""
from S6_SERIES_PUBLISH_c3_edit import *
import sys

assert len(sys.argv)==2
result=(ROOT/'code/S6_SERIES_PUBLISH_c3_build_latest.out').read_text()
for turn in range(1,4):assert f'pdfLaTeX pass {turn}: exit 0' in result
for key in ['exceeding 2pt','undefined references/citations','undefined summary',
            'missing glyphs','missing fonts','multiply defined labels',
            'duplicate destinations','rerun requests']:
    assert re.search(re.escape(key)+r': 0\b',result),key
log=(ROOT/'build/II_c3_working/S6_SERIES_PUBLISH_II.log').read_text(errors='replace')
boxes=[float(x) for x in re.findall(r'Overfull \\[hv]box \(([0-9.]+)pt too (?:wide|high)\)',log)]
pages=re.search(r'\(([0-9]+) pages, ([0-9]+) bytes\)',result)
assert pages
outcome=(f'Three integrated pdfLaTeX passes completed with shell escape disabled. Working PDF: {pages[1]} pages, {pages[2]} bytes. '
 f'{len(boxes)} overfull boxes, maximum {max(boxes,default=0)}pt; none above 2pt. '
 'No undefined reference/citation, missing glyph/font, duplicate label/destination or rerun request. '
 'This is a working-build check while the manuscript is still being revised; final text, final build gate and every final rendered-page row remain open. No page reading or mathematical-check credit.')
add_event('II',sys.argv[1],'used and rechecked in this run',outcome,
 'code/S6_SERIES_PUBLISH_c3_build_latest.out; build/II_c3_working/S6_SERIES_PUBLISH_II.log',
 source='code/S6_SERIES_PUBLISH_c3_working_build_record.py')
print(outcome)
