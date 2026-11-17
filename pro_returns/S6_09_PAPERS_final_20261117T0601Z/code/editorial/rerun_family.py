"""Re-run the selected mathematical verifiers without changing input sources."""
from pathlib import Path
import concurrent.futures, hashlib, json, shutil, subprocess, sys, time

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / 'sources/returns/S6_02_FAMILY/code'
TARGET = ROOT / 'deliverables/code/family'
TARGET.mkdir(parents=True, exist_ok=True)
NAMES = ['ab_exact', 'ab_geometry', 'ab_deformation', 'cd_exact', 'cd_bounds',
         'cd_periods', 'cd_special_intervals', 'cd_torsion_independent', 'f_exact',
         'e_degeneration', 'cd_local_bound', 'cd_multiples_initial', 'f_interval_verify']
for name in NAMES + ['f_interval_cert', 'f_interval_parallel']:
    shutil.copy2(SOURCE / (name + '.py'), TARGET / (name + '.py'))
shutil.copy2(SOURCE / 'f_interval_parallel_certificate.json', TARGET / 'f_interval_parallel_certificate.json')

def run(name):
    start = time.monotonic()
    p = subprocess.run([sys.executable, str(TARGET/(name+'.py'))], cwd=TARGET,
                       capture_output=True, text=True, timeout=480)
    (TARGET/(name+'.rerun.stdout.txt')).write_text(p.stdout)
    (TARGET/(name+'.rerun.stderr.txt')).write_text(p.stderr)
    return {'program': name+'.py', 'command': 'python code/family/'+name+'.py',
            'exit_code': p.returncode, 'seconds': time.monotonic()-start,
            'source_sha256': hashlib.sha256((SOURCE/(name+'.py')).read_bytes()).hexdigest(),
            'stdout_sha256': hashlib.sha256(p.stdout.encode()).hexdigest(),
            'stdout_bytes': len(p.stdout.encode()), 'stderr_bytes': len(p.stderr.encode())}

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        records = list(pool.map(run, NAMES))
    (TARGET/'rerun_manifest.json').write_text(json.dumps(records, indent=2))
    for r in records:
        print(r['program'], 'exit', r['exit_code'], 'seconds', round(r['seconds'],2))
