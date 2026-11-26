#!/usr/bin/env python3
"""Preserve LM attempt001 and repair duplicated serialization keywords."""
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
source = ROOT/'code/S6_SERIES_PUBLISH_c7_lm_fresh_geometry_v001.py'
target = ROOT/'code/S6_SERIES_PUBLISH_c7_lm_fresh_geometry_v002.py'
text = source.read_text()
assert text.count('                    extra = cusp\n') == 1
text = text.replace('                    extra = cusp\n',
    "                    extra = {k:v for k,v in cusp.items() if k not in ('index','degree')}\n"
    "                    extra['fixed_curve_degree'] = cusp['degree']\n")
text = text.replace('02LM_fresh_geometry_v001.json','02LM_fresh_geometry_v002.json')
assert not target.exists()
target.write_text(text, newline='\n')
print('Preserved attempt001 source, partial stdout and complete traceback.')
print('Wrote version002: separate critical-cycle degree and fixed-curve degree; omit repeated index keyword.')
