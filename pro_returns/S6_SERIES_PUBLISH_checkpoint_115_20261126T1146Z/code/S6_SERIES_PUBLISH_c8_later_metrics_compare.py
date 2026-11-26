#!/usr/bin/env python3
"""Read-only full-proof comparison with admitted metric receivers."""
from pathlib import Path
import difflib

ROOT = Path(__file__).resolve().parents[1]
source = (ROOT / 'agents/continuation8_iii_integration/units/later/fixed_target_metrics.tex').read_text()
owners = [
    ('03DG', 'continuation5_iii_root', 'sphere-metric-uniform-collapse', 'receiving_proof'),
    ('03D6', 'continuation5_iii_carriers', 'sphere-metric-fixed-realization', 'receiving'),
    ('03DC', 'continuation5_iii_carriers', 'sphere-metric-scaling-trichotomy', 'receiving'),
    ('03DH', 'continuation5_iii_root', 'sphere-metric-unit-volume', 'receiving'),
    ('03DF', 'continuation5_iii_root', 'sphere-metric-tangent-scope', 'receiving'),
    ('037J', 'continuation6_iii_carriers', 'cusp-cone-sharp-global-R4-scope', 'receiving'),
]
for tag, folder, tail, suffix in owners:
    receiver = (ROOT / 'agents' / folder / ('S6_SERIES_PUBLISH_III_' + tag + '_' + suffix + '.tex')).read_text()
    start = source.index(r'\label{wb:' + tail + '}')
    a = source.index(r'\begin{proof}', start)
    b = source.index(r'\end{proof}', a) + len(r'\end{proof}')
    c = receiver.index(r'\begin{proof}')
    d = receiver.index(r'\end{proof}', c) + len(r'\end{proof}')
    actual, expected = source[a:b], receiver[c:d]
    print(tag, 'source_lines', len(actual.splitlines()), 'admitted_lines', len(expected.splitlines()), 'identical', actual == expected)
    if actual != expected:
        print(''.join(difflib.unified_diff(expected.splitlines(True), actual.splitlines(True), fromfile=tag + '_admitted', tofile=tag + '_repaired_source')), end='')
print('Read-only proof comparison; no manuscript or central writes; no independent proof credit.')
