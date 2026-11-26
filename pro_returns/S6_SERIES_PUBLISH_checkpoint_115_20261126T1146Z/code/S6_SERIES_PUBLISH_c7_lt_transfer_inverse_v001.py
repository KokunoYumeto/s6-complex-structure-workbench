"""Prove exact inverse reading maps for the retained LT transfer and audit."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha1, sha256
import base64
import copy
import json

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT / 'agents/continuation7_iii_invariant_chern_receiving'
P = 'S6_SERIES_PUBLISH_III_02LT_'
transfer = ROOT / 'code/S6_SERIES_PUBLISH_c7_lt_historical_fetch_v1.tool_result.json'
audit = ROOT / 'code/S6_SERIES_PUBLISH_c7_lt_post_audit_v2.out'
saved = LANE / (P + 'historical_III_invariant_chern_cone_fresh.json')
source = LANE / (P + 'historical_III_invariant_chern_cone_fresh.py')
saved_raw = saved.read_bytes()
assert sha256(saved_raw).hexdigest() == '6f825c4560032d4ec5aa7d792f095a6cb9d5051c86ed66227633845f263ce407'
assert sha256(source.read_bytes()).hexdigest() == '6e401c84a466445c4b4c377d0e7c9704090fd984222daf3d6507d8682b7a029e'
lines = audit.read_text().splitlines()
assert len(lines) == 488
decoder = json.JSONDecoder()
top = None
arrays = {'CASE': [], 'AREA': [], 'COMPONENT': []}
for line in lines:
    if line.startswith('TOP '):
        assert top is None
        top = json.loads(line[4:])
    for tag, values in arrays.items():
        if line.startswith(tag + ' '):
            _, index, payload = line.split(' ', 2)
            assert int(index) == len(values)
            value, end = decoder.raw_decode(payload)
            tail = payload[end:]
            assert tail in (' WANG_SPLIT True', ' WANG_SPLIT False', ' WANG_SPLIT None') if tag == 'CASE' else tail == ''
            assert json.dumps(value, separators=(',', ':')) == payload[:end]
            values.append(value)
assert [len(value) for value in arrays.values()] == [390, 54, 19]
assert list(top) == ['status', 'assertions', 'counts', 'sympy_version', 'scope']
reconstructed = dict(top)
for key, tag in [('cases', 'CASE'), ('multiplicity_cycles', 'AREA'), ('component_class_models', 'COMPONENT')]:
    reconstructed[key] = arrays[tag]
assert (json.dumps(reconstructed, indent=2) + '\n').encode() == saved_raw
# The forward projection returns precisely every original field with its order.
original = json.loads(saved_raw)
assert list(original) == list(reconstructed)
assert json.dumps({key: original[key] for key in top}, separators=(',', ':')) == next(line[4:] for line in lines if line.startswith('TOP '))
for key, tag in [('cases', 'CASE'), ('multiplicity_cycles', 'AREA'), ('component_class_models', 'COMPONENT')]:
    assert original[key] == arrays[tag]

raw = transfer.read_bytes()
calls = json.loads(raw)
assert len(calls) == 2
skeleton = copy.deepcopy(calls)
for index, call in enumerate(calls):
    assert call['status'] == 'fulfilled'
    item = call['value']
    response = item['response']
    assert response['isError'] is False
    data = response['structuredContent']
    assert data['encoding'] == 'base64'
    path = LANE / (P + 'historical_' + Path(item['request']['path']).name)
    payload = path.read_bytes()
    assert base64.b64decode(data['content']) == payload
    encoded = base64.b64encode(payload).decode('ascii')
    wrapped = '\n'.join(encoded[start:start + 60] for start in range(0, len(encoded), 60)) + '\n'
    assert wrapped == data['content']
    assert sha1(b'blob ' + str(len(payload)).encode() + b'\0' + payload).hexdigest() == data['sha']
    skeleton[index]['value']['response']['structuredContent']['content'] = {
        'payload_ref': str(path.relative_to(ROOT)),
        'base64_line_width': 60,
        'final_lf': True,
        'decoded_bytes': len(payload),
        'sha256': sha256(payload).hexdigest(),
    }
# Invert only the stated two content substitutions; preserve every other field.
inverse = copy.deepcopy(skeleton)
for call in inverse:
    data = call['value']['response']['structuredContent']
    descriptor = data['content']
    payload = (ROOT / descriptor['payload_ref']).read_bytes()
    assert len(payload) == descriptor['decoded_bytes']
    assert sha256(payload).hexdigest() == descriptor['sha256']
    encoded = base64.b64encode(payload).decode('ascii')
    width = descriptor['base64_line_width']
    data['content'] = '\n'.join(encoded[start:start + width] for start in range(0, len(encoded), width)) + '\n'
assert (json.dumps(inverse, ensure_ascii=False, indent=2) + '\n').encode() == raw
print('START', datetime.now(timezone.utc).isoformat())
print('AUDIT_TO_JSON_EXACT_BYTES', len(saved_raw), sha256(saved_raw).hexdigest())
print('FORWARD_FIELD_PROJECTION_AND_BYTE_INVERSE', '390 cases; 54 areas; 19 components; all top-level fields and order')
print('TRANSFER_METADATA_WITH_EXACT_PAYLOAD_REFERENCES')
print(json.dumps(skeleton, ensure_ascii=False, indent=2))
print('TRANSFER_INVERSE_EXACT_BYTES', len(raw), sha256(raw).hexdigest())
print('READING_SCOPE', 'Whole decoded source; every stored JSON field through the wholly read actual audit; all transfer metadata above. No manual whole-base64 display is claimed.')
print('END', datetime.now(timezone.utc).isoformat())
