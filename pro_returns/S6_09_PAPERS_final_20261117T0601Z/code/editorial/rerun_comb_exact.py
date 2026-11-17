"""Run the original exact comb program; retain its stale status as provenance."""
from pathlib import Path
import json,subprocess,time,hashlib
OUT=Path(__file__).resolve().parents[2]
cwd=OUT/'code/invariants_arithmetic/invariants'
src=cwd/'code/d_comb.py'
start=time.monotonic()
p=subprocess.run(['python3','code/d_comb.py'],cwd=cwd,capture_output=True,text=True)
log=cwd/'outputs/writing_rerun_d_comb.py.txt'
log.write_text(p.stdout+'\nSTDERR\n'+p.stderr)
record={'program':str(src.relative_to(OUT)),'command':['python3','code/d_comb.py'],
 'working_directory':str(cwd.relative_to(OUT)),'exit_code':p.returncode,
 'seconds':time.monotonic()-start,'sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
 'output':str(log.relative_to(OUT)),'output_sha256':hashlib.sha256(log.read_bytes()).hexdigest(),
 'role':'Exact root-character degrees and all nonnegative coarse splitting pairs for m=12,13,20,100; no period section is numerically constructed.',
 'scope':'The original output retains a historical unresolved Kuranishi string. CDP E15 settles that separate question; the program does not compute its bracket. The K_m kernel remains separate.',
 'reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November2026'}
(OUT/'work/root/comb_exact_execution.json').write_text(json.dumps(record,indent=2)+'\n')
print(p.stdout);print('Exit',p.returncode)
assert p.returncode==0
