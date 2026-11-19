"""Replay nine fully read, unchanged CP29 certificates with exact input identities."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import datetime, hashlib, json, shutil, subprocess, time

P = Path(__file__).resolve().parents[2]
R = P.parents[1]
S = R / 'sources/newer_night/checkpoint29'
D = P / 'code/IV/replay_root_f47_56'
programs = [
    'code/part3_root/iii_star_ii_joint.py',
    'code/part3/weighted_extra_sites.py',
    'code/part3/os50_affine_conjugacy.py',
    'code/part3_root/expanding_action_comparison.py',
    'code/part3/generic_source_models.py',
    'code/part3/source_moduli_nodes.py',
    'code/part3_root/source_cusp_link.py',
    'code/part3_root/haefliger_normalization_bridge.py',
    'code/part3/source_cusp_trace.py',
]
manifest = []
for name in programs + ['code/part3/integer_chain.py']:
    source, target = S / name, D / name
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
    assert source.read_bytes() == target.read_bytes()
    manifest.append({'source': str(source.relative_to(R)),
                     'copy': str(target.relative_to(P)),
                     'sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
                     'identical': True,
                     'fully_read': True})

input_records = []
for name in ['i1star_boundary.json', 'i1star_iv_boundary.json',
             'i1star_iv_reduced_boundary.json', 'iv_star_iii_joint.json']:
    origin = (P / 'code/IV/replay_cp29_k106/code/part3' if name.startswith('iv_star')
              else P / 'code/IV/replay_caps_f36_40/code/part3') / name
    target = D / 'code/part3' / name
    shutil.copy2(origin, target)
    assert origin.read_bytes() == target.read_bytes()
    input_records.append({'origin': str(origin.relative_to(P)),
                          'copy': str(target.relative_to(P)),
                          'sha256': hashlib.sha256(origin.read_bytes()).hexdigest(),
                          'identity': 'Exact output of an already recorded current execution; no new execution credit for the producing program.'})

def run(name):
    p = D / name
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    tick = time.monotonic()
    result = subprocess.run(['python', str(p)], cwd=D, capture_output=True, text=True)
    p.with_suffix('.current.stdout').write_text(result.stdout)
    p.with_suffix('.current.stderr').write_text(result.stderr)
    output = p.with_suffix('.json')
    data = json.loads(output.read_text()) if result.returncode == 0 and output.exists() else {}
    return {'program': name, 'started_utc': started,
            'seconds': time.monotonic() - tick, 'returncode': result.returncode,
            'status': data.get('status'), 'output': str(output.relative_to(P)),
            'output_sha256': hashlib.sha256(output.read_bytes()).hexdigest() if output.exists() else None,
            'stdout_tail': result.stdout[-800:], 'stderr': result.stderr}

with ThreadPoolExecutor(max_workers=3) as pool:
    results = list(pool.map(run, programs))
record = {'source_checkpoint': 29, 'programs': manifest, 'input_records': input_records,
          'runs': results, 'all_pass': all(x['returncode'] == 0 and x['status'] == 'PASS' for x in results),
          'scope': 'These are execution events for exact algebra, integral chain maps, and stated arithmetic only. All nine programs and the imported integer-chain helper were fully read. Full F47–51 and F54–56 analytic/geometric proofs are recorded separately.',
          'historical_output_scope': 'The unchanged source_moduli_nodes output retains its historical unresolved field; the current return is proved separately in F56. The cusp programs assign some geometric signs as inputs; their actual orientation and primary-source comparison is checked in the separate proof event.'}
(P / 'analysis/IV/root_F47_56_certificate_replays.json').write_text(json.dumps(record, indent=2))
print(json.dumps({'all_pass': record['all_pass'],
                  'runs': [{k:x[k] for k in ['program','returncode','status','seconds']} for x in results]}, indent=2))
raise SystemExit(0 if record['all_pass'] else 1)
