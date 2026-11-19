"""Replay the five bounded CP30 theta-unit programs without changing sources.

The source/root and common-period programs are fresh prerequisite executions.
Their outputs are installed under the bridge's dedicated replay filenames in
the isolated tree; legacy output bytes are then restored before the bridge.
No large fan/normal replay or mathematical proof credit is inferred.
"""
from pathlib import Path
import datetime, hashlib, json, subprocess, shutil, time, gzip

B = Path('/workspace/scratch/490d8ca4e928')
SRC = B / 'sources/newer_night/checkpoint30'
WORK = Path('/tmp/s6_k107_cp30_replay_20261118')
OUT = B / 'work/S6_10_PAPERS/analysis/IV_K107_cp30/replays'
OUT.mkdir(parents=True, exist_ok=True)
programs = [
    'part3_root/e6_order_three_m2.py',
    'part3_root/e6_order_three_m2_common_periods.py',
    'part3/e6_order_three_m2_peer.py',
    'part3_fourfold/e6_m2_theta_unit_repair.py',
    'part3_root/e6_m2_theta_unit_bridge.py',
]
fresh_prerequisites = {
    programs[0]: ('code/part3_root/e6_order_three_m2.json',
                  'code/part3_root/e6_order_three_m2_after_unit_replay.json'),
    programs[1]: ('code/part3_root/e6_order_three_m2_common_periods.json',
                  'code/part3_root/e6_order_three_m2_common_periods_after_unit_replay.json'),
}

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()

started = now()
WORK.mkdir(parents=True, exist_ok=True)
for name in ['code', 'notes', 'records']:
    if (WORK/name).exists(): shutil.rmtree(WORK/name)
    subprocess.run(['cp', '-a', '--reflink=auto', str(SRC/name), str(WORK/name)], check=True)
rows = []
for ix, prog in enumerate(programs, 1):
    base = {str(p.relative_to(WORK)): (p.stat().st_mtime_ns, p.stat().st_size)
            for d in ['code', 'notes', 'records'] for p in (WORK/d).rglob('*') if p.is_file()}
    path = WORK/'code'/prog
    assert sha(path) == sha(SRC/'code'/prog)
    t0, ts = time.time(), now()
    tag = f'{ix:02d}_{Path(prog).stem}'
    log = OUT/(tag+'.log')
    with log.open('w') as f:
        run = subprocess.run(['python', str(path)], cwd=WORK, stdout=f, stderr=subprocess.STDOUT)
    prerequisite = None
    if prog in fresh_prerequisites and run.returncode == 0:
        source, target = fresh_prerequisites[prog]
        data = (WORK/source).read_bytes()
        prerequisite = {'path': target, 'sha256': hashlib.sha256(data).hexdigest(), 'data': data}
    outputs = []
    for d in ['code', 'notes', 'records']:
        for p in (WORK/d).rglob('*'):
            if not p.is_file(): continue
            rel = str(p.relative_to(WORK))
            if '__pycache__' in rel: continue
            st = (p.stat().st_mtime_ns, p.stat().st_size)
            if rel in base and st == base[rel]: continue
            data = p.read_bytes()
            record = {'path': rel, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}
            if p.suffix == '.json':
                obj = json.loads(data)
                if isinstance(obj, dict):
                    record['summary'] = {k: obj[k] for k in ['status', 'checks', 'source_sha256',
                        'corrected_OG_sha256', 'scope', 'execution_scope'] if k in obj}
            saved = OUT/(tag+'__'+rel.replace('/', '__')+'.gz')
            with gzip.open(saved, 'wb') as f: f.write(data)
            record['saved'] = str(saved.relative_to(B/'work/S6_10_PAPERS'))
            outputs.append(record)
            original = SRC/rel
            if original.exists(): shutil.copy2(original, p)
            else: p.unlink()
    if prerequisite:
        (WORK/prerequisite['path']).write_bytes(prerequisite.pop('data'))
    row = {'program': 'code/'+prog, 'script_sha256': sha(SRC/'code'/prog),
           'started_at': ts, 'completed_at': now(), 'exit_code': run.returncode,
           'seconds': time.time()-t0, 'stdout': str(log.relative_to(B/'work/S6_10_PAPERS')),
           'outputs': outputs, 'fresh_bridge_prerequisite': prerequisite,
           'source_preserved': sha(path) == sha(SRC/'code'/prog)}
    rows.append(row)
    receipt = {'checkpoint': 30, 'started_at': started, 'last_updated': now(),
               'status': 'running' if ix < len(programs) else 'completed',
               'programs_requested': len(programs), 'completed': len(rows),
               'passed': sum(r['exit_code'] == 0 for r in rows), 'runs': rows,
               'proof_credit': 'Computation only. Exact CP30 mathematical delta review is separate.',
               'scope': 'Five bounded theta/source/period/bridge programs. No large fan/normal rerun is claimed.'}
    (OUT/'replay_manifest.json').write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps({'program': prog, 'exit_code': run.returncode,
                      'seconds': round(row['seconds'], 2), 'completed': ix}), flush=True)
    if run.returncode: raise RuntimeError('Replay failed: '+prog)
