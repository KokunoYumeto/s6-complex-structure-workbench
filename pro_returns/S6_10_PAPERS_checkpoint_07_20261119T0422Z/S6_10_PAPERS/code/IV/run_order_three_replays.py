"""Current executions of unchanged numerical certificates; no review generator.

The received outer-audit program asserts a past human proof review in its
payload. It is deliberately not executed as a current mathematical check.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import datetime, hashlib, json, subprocess, sys

ROOT=Path(__file__).resolve().parent/'replay_order_three'
jobs=[
 'code/part3/e6_order_three_source.py',
 'code/part3/e6_order_three_flop.py',
 'code/part3/e6_order_three_charged_chart.py',
 'code/part3/e6_order_three_canonical.py',
 'code/part3/e6_order_three_tate.py',
 'code/part3/e6_order_three_exceptional.py',
 'code/part3/e6_common_period_fan_peer.py',
 'code/part3/e6_common_corner_lift.py',
 'code/part3/e6_p_one_cayley_peer.py',
 'code/part3/e6_generic_fixed_curve_normals.py',
 'code/part3/e6_order_three_fixed_surfaces.py',
 'code/part3/e6_order_three_lower_surfaces.py',
 'code/part3/e6_lower_surface_blowups_peer.py',
 'code/part3/e6_collision_boundary_chain.py',
 'code/part3/e6_order_three_lower_relative.py',
 'code/part3/e6_order_three_relative_double.py',
 'code/part3_root/e6_order_three_surfaces_aux_peer.py',
 'code/part3_root/e6_order_three_fan_algebra.py',
 'code/part3/e6_order_three_native_product_peer.py',
 'code/part3/e6_order_three_all_fans_peer.py',
]
results=[]
def run(name):
 p=ROOT/name
 rec={'program':name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
      'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 with p.with_suffix('.current.stdout').open('w') as out,p.with_suffix('.current.stderr').open('w') as err:
  rec['exit_code']=subprocess.run([sys.executable,str(p)],cwd=ROOT,stdout=out,stderr=err).returncode
 rec['ended_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
 print(json.dumps(rec),flush=True)
 return rec
# Inputs written by the common-corner and fixed-surface programs are consumed
# by later programs, so the dependency chain is intentionally sequential.
with ThreadPoolExecutor(max_workers=2) as pool:
 results.extend(pool.map(run,jobs[:6]))
for name in jobs[6:]:
 results.append(run(name))
 (ROOT/'current_results.json').write_text(json.dumps(results,indent=2)+'\n')
