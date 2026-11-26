#!/usr/bin/env python3
"""Replay the exact released LQ historical program with bounded helper bodies.
No entire imported target program is executed. Every imported definition
comes from the pinned source bytes retained by the cache steps.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
from itertools import combinations
import ast,contextlib,json,runpy,shutil,sys,tempfile,types
import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
from sympy.matrices.normalforms import smith_normal_form
ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/'agents/continuation7_iii_star_logs_receiving'
P='S6_SERIES_PUBLISH_III_02LQ_'
CODE=ROOT/'code'
print('START',datetime.now(timezone.utc).isoformat(),flush=True)
raw=(LANE/(P+'historical_manifolds_rankone_families.py')).read_text()
tree=ast.parse(raw)
assignment=next(node for node in tree.body if isinstance(node,ast.Assign)
                and any(isinstance(t,ast.Name) and t.id=='PAIRS' for t in node.targets))
pair_source='\n'.join(raw.splitlines()[assignment.lineno-1:assignment.end_lineno])+'\n'
(LANE/(P+'historical_helper_PAIRS.py')).write_text(pair_source)
print('EXACT_PAIRS',assignment.lineno,assignment.end_lineno,pair_source.strip(),flush=True)
module=types.ModuleType('manifolds_rankone_families')
module.__dict__.update(s=s,DomainMatrix=DomainMatrix,smith_normal_decomp=smith_normal_decomp,
                       combinations=combinations)
exec(compile(pair_source,'retained_exact_PAIRS','exec'),module.__dict__)
for name in ['decomp','ikernel','wedge','biv','bezout']:
    source=(LANE/(P+'historical_helper_'+name+'.py')).read_text()
    exec(compile(source,'retained_exact_'+name,'exec'),module.__dict__)
sys.modules[module.__name__]=module
for module_name,names,environment in [
    ('manifolds_general_initial',['integer_solution'],{'s':s,'decomp':module.decomp}),
    ('manifolds_weighted_profiles',['group'],{'s':s,'smith_normal_form':smith_normal_form})]:
    m=types.ModuleType(module_name);m.__dict__.update(environment)
    for name in names:
        source=(LANE/(P+'historical_helper_'+name+'.py')).read_text()
        exec(compile(source,'retained_exact_'+name,'exec'),m.__dict__)
    sys.modules[module_name]=m
runtime=Path(tempfile.mkdtemp(prefix='S6_SERIES_PUBLISH_c7_lq_replay_v1_'))
main=runtime/'manifolds_star_log_caps.py'
source=LANE/(P+'historical_manifolds_star_log_caps.py')
shutil.copyfile(source,main)
shutil.copyfile(LANE/(P+'historical_manifolds_sphere_monodromies.json'),runtime/'manifolds_sphere_monodromies.json')
assert main.read_bytes()==source.read_bytes()
stdout=CODE/'S6_SERIES_PUBLISH_c7_lq_historical_main_v1.out'
stderr=CODE/'S6_SERIES_PUBLISH_c7_lq_historical_main_v1.err'
print('RUNTIME',runtime,flush=True)
with stdout.open('w') as out,stderr.open('w') as err:
    with contextlib.redirect_stdout(out),contextlib.redirect_stderr(err):
        runpy.run_path(str(main),run_name='__main__')
generated=runtime/'manifolds_star_log_caps.json'
dest=LANE/(P+'historical_replay_v1.generated.json')
shutil.copyfile(generated,dest)
reference=(LANE/(P+'historical_manifolds_star_log_caps.json')).read_bytes()
actual=dest.read_bytes()
print('GENERATED',len(actual),sha256(actual).hexdigest(),flush=True)
print('SAVED',len(reference),sha256(reference).hexdigest(),flush=True)
assert actual==reference
data=json.loads(actual)
print('COUNTS',len(data['markings']),len(data['cases']),len(data['one_star']),flush=True)
print('MAIN_STDOUT_LINES',len(stdout.read_text().splitlines()),'MAIN_STDERR_BYTES',stderr.stat().st_size,flush=True)
print('PASS byte-identical pinned historical output',datetime.now(timezone.utc).isoformat(),flush=True)
