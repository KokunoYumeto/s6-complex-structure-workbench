from pathlib import Path
import subprocess,json,os,time,hashlib
base=Path(__file__).resolve().parent/'arithmetic'
env=os.environ.copy();env['PYTHONPATH']=str(base.parent/'dependencies')+os.pathsep+env.get('PYTHONPATH','')
programs=['Cspecial_division.py','Cspecial_relations.py','Cspecial_reflection.py','Cspecial_torsion_numerics.py','Cspecial_expansion_checks.py','C_ladder_algebra.py','C_ladder_estimates.py','C_local_analytic_bounds.py','C_padic_example.py','C7_cm_enlargement_check.py','C7_complexified_check.py','Ccritical_rational_certificate.py','C_cm_height_arb.py','C_height_coarse_certificate.py','B_C6_exact_factors.py']
records=[]
for name in programs:
 p=base/'code'/name;log=base/'outputs'/('writing_rerun_'+name+'.txt');start=time.time()
 with log.open('w') as h:
  try:r=subprocess.run(['python',str(p.resolve())],cwd=base,env=env,stdout=h,stderr=subprocess.STDOUT,timeout=900);code=r.returncode
  except subprocess.TimeoutExpired:code='timeout_after_900_seconds'
 rec={'program':str(p.relative_to(base.parent.parent)),'command':['python',str(p.relative_to(base))],'cwd':str(base),'pythonpath_dependency':'python-flint 0.9.0 under ../dependencies','sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'started_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime(start)),'seconds':round(time.time()-start,3),'exit_code':code,'output':str(log.relative_to(base.parent.parent)),'output_sha256':hashlib.sha256(log.read_bytes()).hexdigest()}
 records.append(rec);(base/'writing_reruns.json').write_text(json.dumps(records,indent=2)+'\n');print(name,code,rec['seconds'],flush=True)
print('FINISHED',len(records),'arithmetic programs',flush=True)
