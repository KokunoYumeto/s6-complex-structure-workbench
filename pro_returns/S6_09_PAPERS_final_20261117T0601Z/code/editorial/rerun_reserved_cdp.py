"""Copy and rerun the four original certificates in the reserved CDP proofs.

These finite checks certify only the displayed arithmetic and incidence
matrices, not the geometric identifications that are checked in the proof log.
"""
from pathlib import Path
import concurrent.futures, hashlib, json, shutil, subprocess, sys

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'deliverables/code/root_cdp'
OUT.mkdir(exist_ok=True)
names=['E_enriques_filling.py','A_enriques_support.py','A_equivariant_torus.py','root_ruled_occurrence.py']
def run(name):
    source=ROOT/'sources/returns/S6_03_CDP/code'/name
    target=OUT/name
    shutil.copy2(source,target)
    p=subprocess.run([sys.executable,name],cwd=OUT,capture_output=True,text=True,timeout=90)
    output=OUT/(name+'.output.txt')
    output.write_text(p.stdout+p.stderr)
    digest=lambda path:hashlib.sha256(path.read_bytes()).hexdigest()
    previous=list((source.parent).glob(name.replace('.py','')+'*.out'))
    return {'program':str(target.relative_to(ROOT/'deliverables')),
            'original':str(source.relative_to(ROOT)),
            'command':['python3',name],'working_directory':'code/root_cdp',
            'original_sha256':digest(source),'executed_sha256':digest(target),
            'exit_code':p.returncode,'output':str(output.relative_to(ROOT/'deliverables')),
            'output_sha256':digest(output),
            'comparison':[{'source':str(z.relative_to(ROOT)),
                           'byte_identical':z.read_bytes()==output.read_bytes()} for z in previous],
            'reader':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, 17 November 2026'}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    records=list(executor.map(run,names))
(OUT/'execution_manifest.json').write_text(json.dumps(records,indent=2)+'\n')
for r in records:print(r['program'],r['exit_code'],r['original_sha256']==r['executed_sha256'])
assert all(r['exit_code']==0 for r in records)
