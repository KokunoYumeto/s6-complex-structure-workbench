"""Run one unchanged source certificate in an isolated tree.

This receipt records execution only.  It neither imports historical audit
claims from program output nor certifies historical physical signs.
"""
from pathlib import Path
import datetime
import hashlib
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
TREE = ROOT / 'analysis/IV_sign_third_replays'
relative, *arguments = sys.argv[1:]
program = TREE / 'code' / relative
source = Path('/workspace/scratch/490d8ca4e928/sources/newer_night/checkpoint29/code') / relative
assert program.read_bytes() == source.read_bytes(), 'Copied program changed'
name = program.stem + ('_' + '_'.join(arguments) if arguments else '')
name = name.replace(',', '_').replace('--', '')
log = TREE / 'logs' / (name + '.txt')
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
with log.open('w') as stream:
    result = subprocess.run([sys.executable, str(program), *arguments], cwd=TREE,
                            stdout=stream, stderr=subprocess.STDOUT)
receipt = {
    'started': started,
    'finished': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'source': str(source),
    'unchanged_copy': str(program),
    'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'arguments': arguments,
    'returncode': result.returncode,
    'stdout': str(log),
    'stdout_sha256': hashlib.sha256(log.read_bytes()).hexdigest(),
    'scope': 'Execution of the exact source program only. Mathematical use, '
             'historical central-sign inputs and any bounded enumeration '
             'are assessed separately in the current review.',
}
(TREE / 'receipts' / (name + '.json')).write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps(receipt, indent=2))
print(log.read_text()[-1600:])
raise SystemExit(result.returncode)
