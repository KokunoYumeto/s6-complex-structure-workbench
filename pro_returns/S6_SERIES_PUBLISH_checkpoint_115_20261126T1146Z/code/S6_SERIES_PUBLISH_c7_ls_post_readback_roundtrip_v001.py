"""Check actual LS readback-v002 bytes in both directions.

The six extra metadata lines are retained as explicit coordinates.  Thus
the maps are v002 <-> (v001, metadata), not an inference of timestamps
from v001.  This verifies formatting only; no mathematical run is repeated.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import re

W = Path(__file__).resolve().parents[1]
first = W / 'code/S6_SERIES_PUBLISH_c7_ls_post_readback_v001.out'
second = W / 'code/S6_SERIES_PUBLISH_c7_ls_post_readback_v002.out'
blob1, blob2 = first.read_bytes(), second.read_bytes()
assert sha256(blob1).hexdigest() == '38eeaf8832ab34f54a5f2895b068cdf5fc3cdc77e05f3f32a90b747c1d442531'
assert sha256(blob2).hexdigest() == '73157d74bb9279e89234bf3e6b1618a0a33d85e9995ba526b1bba3199fcd585a'
lines1, lines2 = blob1.decode().splitlines(), blob2.decode().splitlines()
assert len(lines1) == 2038 and len(lines2) == 2044
metadata = lines2[:3] + lines2[-3:]
assert metadata[1] == f'INPUT_SHA256 {sha256(blob1).hexdigest()} BYTES {len(blob1)} LINES {len(lines1)}'
assert metadata[2].startswith('INVERSE: MATRIX/VECTOR lines are unchanged first-readback lines.')
assert metadata[3] == ('EXACT_FIRST_READBACK_RECONSTRUCTION 2038 lines, every byte identical; '
                       'preceding reader reconstructs all three stdout streams and both historical JSON outputs.')
assert metadata[4] == 'RECORD_COUNT 773'
start = datetime.fromisoformat(metadata[0].removeprefix('START '))
end = datetime.fromisoformat(metadata[5].removeprefix('COMPLETE '))
assert start <= end

def compact(value):
    return json.dumps(value, separators=(',', ':'))

def expand(flat, path=()):
    kind, value = flat[path]
    if kind == 'dict':
        return {key: expand(flat, path + (key,)) for key in value}
    if kind == 'list':
        return [expand(flat, path + (key,)) for key in range(value)]
    assert kind == 'value'
    return value

def flatten(value, path=(), result=None):
    if result is None:
        result = {}
    if isinstance(value, dict) and not ('$matrix' in value or '$vector' in value):
        result[path] = ['dict', list(value)]
        for key, item in value.items():
            flatten(item, path + (key,), result)
    elif isinstance(value, list):
        result[path] = ['list', len(value)]
        for key, item in enumerate(value):
            flatten(item, path + (key,), result)
    else:
        result[path] = ['value', value]
    return result

# The inverse reads the actual output, including every actual replacement.
decoded_records, decoded_lines = {}, []
record_pattern = re.compile(r'^RECORD (R\d+) PREFIX ("(?:[^"\\]|\\.)*") BASE (ZERO|R\d+) REPLACE (.*)$')
for number, actual in enumerate(lines2[3:-3], 1):
    prefix = f'SOURCE_LINE {number} '
    assert actual.startswith(prefix)
    body = actual[len(prefix):]
    match = record_pattern.fullmatch(body)
    if match is None:
        decoded_lines.append(body)
        continue
    ident, quoted_prefix, base, replacements = match.groups()
    assert ident == f'R{len(decoded_records) + 1}'
    flat = {} if base == 'ZERO' else decoded_records[base].copy()
    for path, node in json.loads(replacements):
        key = tuple(path)
        if node is None:
            flat.pop(key)
        else:
            flat[key] = node
    decoded_records[ident] = flat
    decoded_lines.append(json.loads(quoted_prefix) + compact(expand(flat)))
assert len(decoded_records) == 773
assert ('\n'.join(decoded_lines) + '\n').encode() == blob1

# The forward map independently recomputes the specified minimal earlier
# base and every absolute replacement, then restores the retained metadata.
records, labels, rebuilt = {}, {}, lines2[:3].copy()
for number, line in enumerate(lines1, 1):
    match = re.fullmatch(r'(LINE \S+ \d+ )([A-Z_]+)=(.*)', line)
    if match is None:
        rebuilt.append(f'SOURCE_LINE {number} {line}')
        continue
    line_prefix, label, payload = match.groups()
    current = flatten(json.loads(payload))
    options = []
    for base in ['ZERO'] + labels.get(label, []):
        previous = {} if base == 'ZERO' else records[base]
        changes = [[list(path), current.get(path)]
                   for path in sorted(current.keys() | previous.keys(),
                                      key=lambda item: compact(list(item)))
                   if current.get(path) != previous.get(path)]
        options.append((len(compact(changes)), base, changes))
    _, base, changes = min(options, key=lambda item: (item[0], item[1]))
    ident = f'R{len(records) + 1}'
    records[ident] = current
    labels.setdefault(label, []).append(ident)
    rebuilt.append(f'SOURCE_LINE {number} RECORD {ident} PREFIX '
                   f'{json.dumps(line_prefix + label + "=")} BASE {base} REPLACE {compact(changes)}')
rebuilt.extend(lines2[-3:])
assert ('\n'.join(rebuilt) + '\n').encode() == blob2

print('COMPLETE', datetime.now(timezone.utc).isoformat())
print('INVERSE actual v002 -> v001 plus six metadata lines: every byte recovered.')
print('FORWARD v001 plus the same metadata -> actual v002: every byte recovered.')
print('COUNTS', len(lines1), len(lines2), len(records), 'BYTES', len(blob1), len(blob2))
for number, line in enumerate(metadata, 1):
    print('ACTUAL_V002_METADATA', number, line)
print('V001_SHA256', sha256(blob1).hexdigest())
print('V002_SHA256', sha256(blob2).hexdigest())
print('SCOPE complete v001 mathematical reading plus exact inverse maps and all six literal extra metadata lines; no duplicate manual v002 whole-reading claim and no mathematical rerun.')
