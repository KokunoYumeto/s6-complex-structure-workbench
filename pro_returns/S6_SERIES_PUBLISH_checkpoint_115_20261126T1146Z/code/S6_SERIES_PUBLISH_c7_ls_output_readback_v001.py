"""Lossless LS output reading format; no mathematical calculation is rerun.

Every original stdout line is reconstructed with its exact order, scalar
values and metadata. Identical sparse matrices and integer vectors are
printed once and referred to thereafter. All JSON data values are also
matched against the original stdout's geometry/context and result records.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'code/S6_SERIES_PUBLISH_c7_ls_os45_bar_v001.out'
data_path = ROOT / 'agents/continuation7_iii_vertical_correction/S6_SERIES_PUBLISH_III_02LS_fresh_os45_data_v001.json'
original = source.read_bytes()
source_text = original.decode()
assert b'\r' not in original and source_text.endswith('\n')
objects = {}
lookup = {}
records = []
matrix_count = vector_count = 0

def compact(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'))

def encode(obj):
    global matrix_count, vector_count
    kind = None
    if isinstance(obj, dict) and set(obj) == {'entries', 'shape'}:
        kind = 'M'
        rows, cols = obj['shape']
        assert type(rows) is int and type(cols) is int
        seen = set()
        for i, j, value in obj['entries']:
            assert 0 <= i < rows and 0 <= j < cols and type(value) is int and value
            assert (i, j) not in seen
            seen.add((i, j))
    elif isinstance(obj, list) and len(obj) >= 4 and all(type(x) is int for x in obj):
        kind = 'V'
    if kind:
        key = (kind, compact(obj))
        if key not in lookup:
            if kind == 'M':
                matrix_count += 1
                name = f'M{matrix_count:03}'
            else:
                vector_count += 1
                name = f'V{vector_count:03}'
            lookup[key] = name
            objects[name] = obj
            print(name+'='+compact(obj), flush=True)
        return {'$ref': lookup[key]}
    if isinstance(obj, dict):
        assert '$ref' not in obj
        return {key: encode(value) for key, value in obj.items()}
    if isinstance(obj, list):
        return [encode(value) for value in obj]
    return obj

def decode(obj):
    if isinstance(obj, dict):
        if set(obj) == {'$ref'}:
            return objects[obj['$ref']]
        return {key: decode(value) for key, value in obj.items()}
    if isinstance(obj, list):
        return [decode(value) for value in obj]
    return obj

print('READBACK_START', datetime.now(timezone.utc).isoformat(), flush=True)
print('SOURCE_SHA256', sha256(original).hexdigest(), 'BYTES', len(original), flush=True)
print('FORMAT: every M has its full shape and all nonzero entries; all other entries are zero. Every V is an exact vector. Repeated references have identical content.', flush=True)
reconstructed = []
context = None
vertical = None
local = []
exterior = None
computed_cases = []
for lineno, line in enumerate(source_text.splitlines(), 1):
    if '=' not in line:
        print('LINE', lineno, 'TEXT', compact(line), flush=True)
        reconstructed.append(line)
        if line.startswith('GEOMETRY '):
            _, aa, bb, zz = line.split()
            context = tuple(map(int, (aa, bb, zz)))
            local = []
        continue
    label, payload = line.split('=', 1)
    value = json.loads(payload)
    reduced = encode(value)
    recovered = decode(reduced)
    assert recovered == value
    rebuilt = label+'='+compact(recovered)
    assert rebuilt == line
    reconstructed.append(rebuilt)
    print('LINE', lineno, label+'='+compact(reduced), flush=True)
    if label == 'VERTICAL':
        vertical = {key: item for key, item in value.items() if key not in ('a', 'b')}
    elif label == 'LOCAL':
        local.append(value)
    elif label == 'EXTERIOR':
        exterior = value
    elif label == 'FULL_RESULT':
        a, b, zero = context
        assert (value['a'], value['b'], value['zero']) == context
        computed_cases.append(dict(a=a, b=b, zero=zero, e=value['e'],
            torsion=value['torsion'], H2_free=value['cokernel_free_rank'],
            H3_free=0, pi1='trivial', vertical=vertical,
            local_maps=local.copy(), exterior=exterior, full=value))
restored = ('\n'.join(reconstructed)+'\n').encode()
assert restored == original
data = json.loads(data_path.read_bytes())
assert data == computed_cases and len(data) == 16
print('EXACT_RECONSTRUCTION', len(reconstructed), 'original lines; source bytes identical; all16 JSON records equal their full rendered stdout data.', flush=True)
print('UNIQUE_OBJECTS', matrix_count, 'matrices', vector_count, 'vectors', flush=True)
print('DATA_SHA256', sha256(data_path.read_bytes()).hexdigest(), flush=True)
print('READBACK_COMPLETE', datetime.now(timezone.utc).isoformat(), flush=True)
