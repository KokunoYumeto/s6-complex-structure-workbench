"""Run unchanged K107 exact programs in an isolated copy; retain scoped receipts.
No success here is substituted for a reading of the mathematical proof.
"""
from pathlib import Path
import datetime,hashlib,json,subprocess,shutil,time,gzip
B=Path('/workspace/scratch/490d8ca4e928')
SRC=B/'sources/newer_night/checkpoint29'
WORK=Path('/tmp/s6_k107_replay_20261118')
OUT=B/'work/S6_10_PAPERS/analysis/IV_K107/replays'
OUT.mkdir(parents=True,exist_ok=True)
programs=[
'part3_root/e6_order_three_m2.py',
'part3/e6_order_three_m2_peer.py',
'part3_root/e6_order_three_m2_common_periods.py',
'part3/e6_order_three_m2_zero_fan.py',
'part3_root/e6_order_three_m2_one_fan.py',
'part3_root/e6_order_three_m2_infinity_fan.py',
'part3/e6_order_three_m2_atlas_peer.py',
'part3/e6_order_three_m2_zero_common_lift.py',
'part3_fourfold/e6_order_three_m2_fixed_faces.py',
'part3_fourfold/e6_order_three_m2_point_graph.py',
'part3/e6_order_three_m2_point_graph_peer.py',
'part3_fourfold/e6_order_three_m2_surface_stars.py',
'part3/e6_order_three_m2_surface_aux_peer.py',
'part3_fourfold/e6_order_three_m2_corner_normals.py',
'part3_root/e6_order_three_m2_corner_peer.py',
'part3/e6_order_three_m2_fixed_curve_normals.py',
'part3_fourfold/e6_order_three_m2_curve_peer.py',
'part3_fourfold/e6_order_three_m2_lower_normals.py',
'part3/e6_order_three_m2_reference_square.py',
'part3_fourfold/e6_order_three_m2_reference_peer.py',
'part3_fourfold/e6_order_three_m2_outer_transfer.py',
'part3/e6_order_three_m2_outer_transfer_peer.py',
'part3_fourfold/e6_order_three_m2_all_fans.py',
'part3_root/e6_order_three_m2_all_fans_peer.py',
]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
started=now();WORK.mkdir(parents=True,exist_ok=True)
for name in ['code','notes','records']:
 if (WORK/name).exists():shutil.rmtree(WORK/name)
 subprocess.run(['cp','-a','--reflink=auto',str(SRC/name),str(WORK/name)],check=True)
base={str(p.relative_to(WORK)):(p.stat().st_mtime_ns,p.stat().st_size) for d in ['code','notes','records'] for p in (WORK/d).rglob('*') if p.is_file()}
rows=[]
for ix,prog in enumerate(programs,1):
 path=WORK/'code'/prog
 assert sha(path)==sha(SRC/'code'/prog)
 t0=time.time();ts=now();tag=f'{ix:02d}_{Path(prog).stem}'
 log=OUT/(tag+'.log')
 with log.open('w') as f:
  run=subprocess.run(['python',str(path)],cwd=WORK,stdout=f,stderr=subprocess.STDOUT)
 outputs=[]
 for d in ['code','notes','records']:
  for p in (WORK/d).rglob('*'):
   if not p.is_file():continue
   rel=str(p.relative_to(WORK));st=(p.stat().st_mtime_ns,p.stat().st_size)
   if rel in base and st==base[rel]:continue
   if '__pycache__' not in rel and p.suffix in ['.json','.txt','.md','.tex','.tsv','.csv']:
    data=p.read_bytes();record={'path':rel,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
    if p.suffix=='.json':
     try:
      obj=json.loads(data)
      if isinstance(obj,dict):
       record['summary']={k:obj[k] for k in ['status','checks','check_count','total_checks','seconds','scope','source_sha256','initial_physical_pair','initial_native_pair','image_mod28','sum_scoped_physical_pair'] if k in obj}
     except (ValueError,TypeError):pass
    saved=OUT/(tag+'__'+rel.replace('/','__')+'.gz')
    with gzip.open(saved,'wb') as f:f.write(data)
    record['saved']=str(saved.relative_to(B/'work/S6_10_PAPERS'))
    outputs.append(record)
   original=SRC/rel
   if original.exists():shutil.copy2(original,p)
   else:p.unlink()
 row={'program':'code/'+prog,'script_sha256':sha(SRC/'code'/prog),'started_at':ts,'completed_at':now(),'exit_code':run.returncode,'seconds':time.time()-t0,'stdout':str(log.relative_to(B/'work/S6_10_PAPERS')),'outputs':outputs,'source_preserved':sha(path)==sha(SRC/'code'/prog)}
 rows.append(row)
 receipt={'checkpoint':29,'started_at':started,'last_updated':now(),'status':'running' if ix<len(programs) else 'completed','programs_requested':len(programs),'completed':len(rows),'passed':sum(r['exit_code']==0 for r in rows),'runs':rows,'proof_credit':'Computation only; full geometric review is recorded separately.'}
 (OUT/'replay_manifest.json').write_text(json.dumps(receipt,indent=2)+'\n')
 print(json.dumps({'program':prog,'exit_code':run.returncode,'seconds':round(row['seconds'],2),'completed':ix,'outputs':len(outputs)}),flush=True)
print('COMPLETE',flush=True)
