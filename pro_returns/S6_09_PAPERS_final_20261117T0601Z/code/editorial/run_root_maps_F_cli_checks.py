"""Replay original F programs with their actual CLI fixtures and pinned runtime.

Initial no-argument failures and the 300-second topology timeout remain in
the first manifest. This pass supplies the documented arguments and permits
the complete exact chain calculation to finish. It changes no mathematics.
"""
from pathlib import Path
import json,shutil,subprocess,hashlib,time,sys

D=Path(__file__).resolve().parents[2];ROOT=D.parent
S=ROOT/'sources/returns/S6_04_MAPS_MANIFOLDS';R=ROOT/'runtime_maps_F'
P=D/'code/root_maps_F';DEST=P/'runtime';DEST.mkdir(exist_ok=True)
for sub in ['code','records']:(R/sub).mkdir(parents=True,exist_ok=True)
for p in P.glob('*.py'):shutil.copy2(p,R/'code'/p.name)
extras=['test_fourfolds_tuple_classification.py','fourfolds_identity_classification_test.py',
 'fourfolds_total_homology_checks.py','test_fourfolds_conjugacy_actual.jl',
 'test_fourfolds_integral_conjugacy.jl','fourfolds_integral_conjugacy.jl']
for name in extras:
 shutil.copy2(S/'code'/name,R/'code'/name);shutil.copy2(S/'code'/name,P/name)
fixtures=['fourfolds_marked_involution_input.json','fourfolds_marked_order_one_input.json',
 'fourfolds_marked_survivor_input.json','fourfolds_marked_k3_2_input.json',
 'fourfolds_conjugacy_actual_inputs.toml']
for name in fixtures:
 shutil.copy2(S/'records'/name,R/'records'/name)
q=P/'input';q.mkdir(exist_ok=True)
for name in fixtures:shutil.copy2(S/'records'/name,q/name)
tasks=[
 ['python3','code/fourfolds_cusp_boundary.py'],
 ['python3','code/fourfolds_involution_classes.py'],
 ['python3','code/test_fourfolds_tuple_classification.py'],
 ['python3','code/fourfolds_identity_classification_test.py'],
 ['python3','code/fourfolds_total_homology.py','--fresh'],
 ['python3','code/fourfolds_total_homology.py','2','--fresh'],
 ['python3','code/fourfolds_marked_gluing.py','records/fourfolds_marked_involution_input.json',
  'records/fourfolds_marked_involution_output.json','--fresh'],
 ['python3','code/fourfolds_classify_gluing.py','records/fourfolds_marked_order_one_input.json',
  'records/fourfolds_classified_order_one_output.json'],
 ['python3','code/fourfolds_total_homology_checks.py'],
 ['python3','code/run_hecke.py','code/test_fourfolds_conjugacy_actual.jl']]
records=[]
for i,cmd in enumerate(tasks):
 name=Path(cmd[1]).name+('_'+Path(cmd[2]).stem if len(cmd)>2 else '')
 output=P/(f'cli_{i+1:02d}_'+name+'.rerun.txt');start=time.monotonic()
 with output.open('w') as f:
  try:
   run=subprocess.run(cmd,cwd=R,stdout=f,stderr=subprocess.STDOUT,timeout=3600)
   rc=run.returncode;status='completed'
  except subprocess.TimeoutExpired:rc=None;status='timed out after 3600 seconds'
 rec={'command':cmd,'working_directory':'runtime_maps_F (reconstructed from retained code and input fixtures)',
      'actual_working_directory':str(R),'exit_code':rc,'status':status,'seconds':round(time.monotonic()-start,3),
      'output':str(output.relative_to(D)),
      'program_sha256':hashlib.sha256((R/cmd[1]).read_bytes()).hexdigest(),
      'output_sha256':hashlib.sha256(output.read_bytes()).hexdigest()}
 records.append(rec)
 for sub in ['records','code']:
  target=DEST/sub;target.mkdir(exist_ok=True)
  for p in (R/sub).glob('*'):
   if p.is_file() and (sub=='records' or p.suffix in ['.json','.toml']):shutil.copy2(p,target/p.name)
 (P/'cli_execution_manifest.json').write_text(json.dumps(records,indent=2)+'\n')
 print(json.dumps(rec),flush=True)
print('Documented CLI replay completed; failures, if any, remain explicit.',flush=True)
