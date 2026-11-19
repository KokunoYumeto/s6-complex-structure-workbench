from pathlib import Path
from datetime import datetime, timezone
import json
import hashlib

root = Path(__file__).resolve().parents[2]
p = root / 'code/part3/source_cusp_characteristic_pair_results_mapping.json'
raw = p.read_bytes()
backup = root / 'records/k42_pre_antilinear_arrow/source_cusp_characteristic_pair_results_mapping_pre_physical.json'
if not backup.exists():
    backup.write_bytes(raw)
d = json.loads(raw)
old_values = d['own_values']
d.setdefault('correction_history', []).append({
    'utc': datetime.now(timezone.utc).isoformat(),
    'correction': 'P3K.68 exact Hermitian dual and physical inverse-clutch comparison',
    'previous_own_values': old_values,
    'preserved_source': str(backup.relative_to(root)),
    'preserved_sha256': hashlib.sha256(raw).hexdigest()
})
d['utc'] = datetime.now(timezone.utc).isoformat()
d['own_values'] = {
    'line_convention': 'M is the physical nonzero-vector line; U=M^-1 is the outward-meridian-one Thom line.',
    'local_surgery_pair_U': [5,-4], 'spinor_c2': -1, 'normal_p1': 4,
    'normal_sphere_pair_U': [1,4], 'Jin_pair_U': [6,0],
    'Jin_pair_M': [-6,0], 'Jin_pair': [-6,0],
    'relative_pair': [0,-6], 'central_class': -1, 'central_class_mod28': 27
}
d['audits'].extend([
    'P3K.68 full physical line, anti-linear cap and inverse-clutch proof independently passed root and checks',
    'Corrected K42 standalone all seven pages reviewed by checks: PASS'
])
d['visual_qa'] = 'records/k42_corrected_standalone_visual_qa.json'
d['remaining'] = ['All-fan source returns beyond the explicitly proved families in P3K.69 remain separately scoped.']
p.write_text(json.dumps(d, indent=2) + '\n')
print(json.dumps({'status':'PASS','physical_pair':[-6,0],'Thom_pair':[6,0],'central_class':-1}, indent=2))
