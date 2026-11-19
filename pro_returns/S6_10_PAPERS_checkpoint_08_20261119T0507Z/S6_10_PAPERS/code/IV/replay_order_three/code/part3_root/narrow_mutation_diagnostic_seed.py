"""Retain the exploratory two-seed search and run only the proved seed."""
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json,shutil

root=Path(__file__).resolve().parents[2]
target=root/'code/part3_root/source_cusp_mutation_diagnostic.py'
archive=root/'code/part3_root/attempts/mutation_two_seed_diagnostic'
archive.mkdir(parents=True,exist_ok=False)
files={}
for ext in ['py','json','out','err']:
    name='source_cusp_mutation_diagnostic.'+ext
    p=target.parent/name
    if p.exists():
        shutil.copy2(p,archive/name)
        files[name]=hashlib.sha256(p.read_bytes()).hexdigest()
(archive/'scope.json').write_text(json.dumps({
 'utc':datetime.now(timezone.utc).isoformat(),
 'reason':'The original exploratory search seeded P1 with a fixed-star pair not yet proved. The formal CF.1-5 proof uses only the proved P0 seed. This copy retains all exploratory results; the active diagnostic is narrowed to P0.',
 'files':files},indent=2)+'\n')
text=target.read_text()
old="""P1=S.Matrix([[1,0],[1,1]])
V1,d1=solve(P1,0,S.Integer(0),S.Integer(-12))
queue=deque([(P0,initial_V,initial_delta,1,()),(P1,V1,d1,1,())])"""
new="""queue=deque([(P0,initial_V,initial_delta,1,())])"""
assert old in text
text=text.replace(old,new)
text=text.replace("'basis_states':len(visited),'fan_states':len(fans),'depth':max_depth,",
 "'basis_states':len(visited),'fan_states':len(fans),'depth':max_depth,\n 'seeds':['P0=I, with K51/K52 full invariants'],")
text=text.replace("'The exact Cox and native-framing maps require their written proof. No unproved matrix reset or full-fan return is assigned.'",
 "'Only the proved P0 seed is used. The exact maps are proved in CF.1-5; this finite certificate checks their identities without assigning values to skipped targets.'")
target.write_text(text)
print('Preserved the exploratory two-seed diagnostic and restricted the active search to the proved P0 seed.')
