"""Lossless delta display of the complete first LS readback.

Every matrix is the named earlier same-shape matrix (or zero/identity)
with the listed entries replaced by the listed integers. Copying the base
and applying those replacements is the explicit inverse. Every vector is
handled identically. The reconstructed first readback is byte-identical;
that first readback already reconstructs the mathematical stdout and JSON.
No mathematical computation, original stdout or previous source is changed.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import re

ROOT = Path(__file__).resolve().parents[1]
source = ROOT/'code/S6_SERIES_PUBLISH_c7_ls_output_readback_v001.out'
blob = source.read_bytes()
text = blob.decode()
matrices = {}
vectors = {}
reconstructed = []
matrix_entries = matrix_replacements = 0

def compact(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'))

print('DELTA_READ_START', datetime.now(timezone.utc).isoformat(), flush=True)
print('INPUT_SHA256', sha256(blob).hexdigest(), 'BYTES', len(blob), flush=True)
print('INVERSE: copy BASE, then replace each stated entry; all unstated entries retain their BASE value. ZERO is all zero; IDENTITY has ones on its rectangular diagonal. Record indices are the exact input line numbers.', flush=True)
for number, line in enumerate(text.splitlines(), 1):
    match = re.fullmatch(r'(M[0-9]+|V[0-9]+)=(.*)', line)
    if match is None:
        print('SOURCE_LINE', number, line, flush=True)
        reconstructed.append(line)
        continue
    name, payload = match.groups()
    value = json.loads(payload)
    if name.startswith('M'):
        rows, cols = value['shape']
        current = {(i, j): x for i, j, x in value['entries']}
        assert len(current) == len(value['entries'])
        candidates = [('ZERO', {}),
                      ('IDENTITY', {(i, i): 1 for i in range(min(rows, cols))})]
        candidates += [(key, obj) for key, (shape, obj) in matrices.items()
                       if shape == (rows, cols)]
        possible = []
        for base, previous in candidates:
            changes = [(i, j, current.get((i, j), 0))
                       for i, j in sorted(current.keys() | previous.keys())
                       if current.get((i, j), 0) != previous.get((i, j), 0)]
            possible.append((len(changes), base, previous, changes))
        _, base, previous, changes = min(possible, key=lambda x: (x[0], x[1]))
        decoded = previous.copy()
        for i, j, x in changes:
            if x:
                decoded[i, j] = x
            else:
                decoded.pop((i, j), None)
        assert decoded == current
        restored = dict(shape=[rows, cols],
                        entries=[[i, j, x] for (i, j), x in sorted(decoded.items())])
        assert restored == value and name+'='+compact(restored) == line
        matrices[name] = ((rows, cols), current)
        matrix_entries += len(current)
        matrix_replacements += len(changes)
        rendered = ';'.join(f'{i},{j}:{x}' for i, j, x in changes)
        print(f'SOURCE_LINE {number} {name} SHAPE {rows}x{cols} BASE {base} REPLACE {rendered}', flush=True)
    else:
        size = len(value)
        candidates = [('ZERO', [0]*size)]
        candidates += [(key, obj) for key, obj in vectors.items() if len(obj) == size]
        options = []
        for base, previous in candidates:
            changes = [(i, x) for i, x in enumerate(value) if x != previous[i]]
            options.append((len(changes), base, previous, changes))
        _, base, previous, changes = min(options, key=lambda x: (x[0], x[1]))
        decoded = previous.copy()
        for i, x in changes:
            decoded[i] = x
        assert decoded == value and name+'='+compact(decoded) == line
        vectors[name] = value
        rendered = ';'.join(f'{i}:{x}' for i, x in changes)
        print(f'SOURCE_LINE {number} {name} LENGTH {size} BASE {base} REPLACE {rendered}', flush=True)
    reconstructed.append(name+'='+compact(value))
assert ('\n'.join(reconstructed)+'\n').encode() == blob
print('EXACT_RECONSTRUCTION', len(reconstructed), 'first-readback lines; all bytes identical.', flush=True)
print('MATRIX_OBJECTS', len(matrices), 'VECTOR_OBJECTS', len(vectors),
      'ORIGINAL_NONZERO_ENTRIES', matrix_entries, 'EXPLICIT_REPLACEMENTS', matrix_replacements, flush=True)
print('DELTA_READ_COMPLETE', datetime.now(timezone.utc).isoformat(), flush=True)
