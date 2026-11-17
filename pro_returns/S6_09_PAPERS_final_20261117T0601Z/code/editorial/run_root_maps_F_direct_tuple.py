"""Run the original positional CLI on one exact documented finite-stratum input."""
from pathlib import Path
import json,subprocess,hashlib,time,shutil
ROOT=Path(__file__).resolve().parents[3];D=ROOT/'deliverables';R=ROOT/'runtime_maps_F';O=D/'code/root_maps_F'
classes=json.loads((R/'records/fourfolds_involution_classes.json').read_text())['classes']
fixture={'matrices':classes[0]['matrices']}
inp=R/'records/writing_direct_tuple_input.json';out=R/'records/writing_direct_tuple_output.json'
inp.write_text(json.dumps(fixture,indent=2)+'\n')
cmd=['python3','code/fourfolds_tuple_classification.py',str(inp.relative_to(R)),str(out.relative_to(R))]
t=time.monotonic();p=subprocess.run(cmd,cwd=R,capture_output=True,text=True);elapsed=time.monotonic()-t
log=O/'direct_tuple_cli.rerun.txt';log.write_text(p.stdout+p.stderr)
assert p.returncode==0,(p.returncode,p.stdout,p.stderr)
value=json.loads(out.read_text());assert value['key']==classes[0]['key'] and value['representative']==classes[0]['matrices']
for f in [inp,out]:shutil.copy2(f,O/'runtime/records'/f.name)
r={'command':cmd,'working_directory':'code/root_maps_F/runtime','exit_code':p.returncode,'seconds':round(elapsed,3),
 'program':'code/root_maps_F/runtime/code/fourfolds_tuple_classification.py','program_sha256':hashlib.sha256((R/'code/fourfolds_tuple_classification.py').read_bytes()).hexdigest(),
 'input':'code/root_maps_F/runtime/records/'+inp.name,'input_sha256':hashlib.sha256(inp.read_bytes()).hexdigest(),
 'certificate':'code/root_maps_F/runtime/records/'+out.name,'certificate_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
 'output':str(log.relative_to(D)),'output_sha256':hashlib.sha256(log.read_bytes()).hexdigest(),
 'scope':'One direct positional CLI invocation, exact comparison against its known finite involution representative. The independent test runner additionally checked all56 conjugated representatives; the infinite height-box search is proved, not claimed executed.',
 'reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro)','date':'2026-11-17'}
(O/'direct_tuple_execution_record.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r))
