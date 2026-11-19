"""Replay fully read exact programs on copies, with byte-level provenance."""
from pathlib import Path
import concurrent.futures, hashlib, json, shutil, subprocess, sys, time

OUT = Path(__file__).resolve().parents[2]
BASE = OUT.parents[1]
DEST = OUT / 'code/I/replay_family_applications'
DEST.mkdir(exist_ok=True)
PROGRAMS = [
    ('S6_02_FAMILY', 'cd_exact.py'),
    ('S6_02_FAMILY', 'cd_torsion_independent.py'),
    ('S6_02_FAMILY', 'e_degeneration.py'),
    ('S6_02_PUSH', 'ab_push_local_checks.py'),
    ('S6_02_PUSH', 'ab_push_fan.py'),
]
manifest = []
for run, name in PROGRAMS:
    source = BASE / 'sources/returns' / run / 'code' / name
    target = DEST / name
    shutil.copy2(source, target)
    manifest.append({'source': str(source.relative_to(BASE)), 'copy': str(target.relative_to(OUT)),
                     'sha256': hashlib.sha256(source.read_bytes()).hexdigest(), 'edits': []})
(DEST / 'source_manifest.json').write_text(json.dumps(manifest, indent=2))

def run(record):
    path = OUT / record['copy']
    started = time.monotonic()
    proc = subprocess.run([sys.executable, str(path)], cwd=DEST, capture_output=True, text=True)
    path.with_suffix('.current.stdout.txt').write_text(proc.stdout + proc.stderr)
    return {'program': path.name, 'returncode': proc.returncode,
            'elapsed_seconds': round(time.monotonic()-started, 3),
            'stdout_sha256': hashlib.sha256(proc.stdout.encode()).hexdigest()}

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(run, manifest))
(DEST / 'results.json').write_text(json.dumps(results, indent=2))
for result in results:
    print(json.dumps(result), flush=True)
assert all(r['returncode'] == 0 for r in results)
