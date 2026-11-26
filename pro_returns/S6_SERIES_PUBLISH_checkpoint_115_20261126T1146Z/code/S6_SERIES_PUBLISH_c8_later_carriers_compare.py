#!/usr/bin/env python3
"""Read-only comparison of the complete admitted carrier proof inputs."""
from pathlib import Path
import difflib

ROOT = Path(__file__).resolve().parents[1]
source = (ROOT / 'agents/continuation8_iii_integration/units/later/further_cusp_carriers.tex').read_text()
owners = [
    ('0370', 'continuation5_iii_carriers', 'native-descent', 'proof'),
    ('035X', 'continuation5_iii_carriers', 'S12-route', 'proof'),
    ('0365', 'continuation5_iii_carriers', 'S24-local-route', 'proof'),
    ('036A', 'continuation5_iii_carriers', 'S24-route', 'proof'),
    ('037N', 'continuation5_iii_finite', 'target-slice-embeddings', 'definition'),
    ('036W', 'continuation5_iii_root', 'metric-scope', 'proof'),
    ('0374', 'continuation5_iii_finite', 'obstructions', 'proof'),
    ('0375', 'continuation5_iii_finite', 'optimal-exponents', 'proof'),
    ('036J', 'continuation5_iii_root', 'angle-forgotten-sphere-carriers', 'proof'),
    ('035Z', 'continuation6_iii_carriers', 'S12-sphere-map-null', 'remark'),
    ('036E', 'continuation5_iii_finite', 'S24-sphere-map-null', 'proof'),
    ('036V', 'continuation5_iii_carriers', 'literal-R4-open-cells', 'proof'),
    ('036Z', 'continuation6_iii_carriers', 'moving-S4-null-homotopy', 'proof'),
    ('037K', 'continuation6_iii_carriers', 'sphere-map-homotopy-status', 'remark'),
    ('036O', 'continuation5_iii_carriers', 'explicit-carriers', 'proof'),
    ('037M', 'continuation5_iii_root', 'target-homotopy-types', 'proof'),
    ('036N', 'continuation5_iii_carriers', 'exact-decompactification-space', 'proof'),
    ('037J', 'continuation6_iii_carriers', 'sharp-global-R4-scope', 'proof'),
]
for tag, folder, tail, env in owners:
    suffix = 'receiving_proof' if tag in {'036W', '037M'} else 'receiving'
    path = ROOT / 'agents' / folder / ('S6_SERIES_PUBLISH_III_' + tag + '_' + suffix + '.tex')
    receiver = path.read_text()
    label = r'\label{wb:cusp-cone-' + tail + '}'
    start = source.index(label)
    a = source.index(r'\begin{proof}', start) if env == 'proof' else source.rfind(r'\begin{' + env + '}', 0, start)
    end = r'\end{' + env + '}'
    b = source.index(end, a) + len(end)
    c = receiver.index(r'\begin{' + env + '}')
    d = receiver.index(end, c) + len(end)
    actual, expected = source[a:b], receiver[c:d]
    print(tag, env, 'source_lines', len(actual.splitlines()), 'admitted_lines', len(expected.splitlines()), 'identical', actual == expected)
    if actual != expected:
        print(''.join(difflib.unified_diff(expected.splitlines(True), actual.splitlines(True), fromfile=tag + '_admitted', tofile=tag + '_repaired_source')), end='')
print('Read-only proof comparison; no manuscript or central-record writes; no new proof credit.')
