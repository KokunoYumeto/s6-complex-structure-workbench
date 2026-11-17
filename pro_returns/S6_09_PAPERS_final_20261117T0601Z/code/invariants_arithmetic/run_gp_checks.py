from pathlib import Path
import subprocess,os,time,json,hashlib,re
ROOT=Path(__file__).resolve().parents[3]
AR=ROOT/'deliverables/code/invariants_arithmetic/arithmetic'
DEP=ROOT/'sources/audit_cache/inv_ari/deps/root'
ENV=dict(os.environ);ENV['LD_LIBRARY_PATH']=str(DEP/'usr/lib/x86_64-linux-gnu')
OUT=AR/'outputs';OUT.mkdir(exist_ok=True)
GP=DEP/'usr/bin/gp'
NAMES=['C_cm_class_polynomials.gp','C_cm_models.gp','C_cm_local_heights.gp','Crank_torsion_local.gp','Crank_torsion_final.gp','C7_cm_explicit.gp','Crank_cm_theta_test.gp','B_C6_gz_exact_metadata.gp','Crank_torsion_descent.gp']
rows=[]
for name in NAMES:
 source=AR/'code'/name
 text=source.read_text().replace('/workspace/scratch/552e69abcf1e/.apt/runtime/usr/share/pari',str(DEP/'usr/share/pari')).replace('S6_05_ARITHMETIC/',str(AR)+'/')
 runfile=AR/'code'/('writing_'+name);runfile.write_text(text)
 started=time.time();print('RUN',name,flush=True)
 try:
  proc=subprocess.run([str(GP),'-fq',str(runfile)],cwd=AR,env=ENV,text=True,capture_output=True,timeout=600)
  stdout=proc.stdout+'\nSTDERR\n'+proc.stderr;rc=proc.returncode
 except subprocess.TimeoutExpired as e:stdout=str(e.stdout)+str(e.stderr);rc=124
 path=OUT/('writing_'+name+'.txt');path.write_text(stdout)
 errors=[line for line in stdout.splitlines() if '***' in line and not any(x in line for x in ['Warning: new maximum stack size','Warning: increasing stack size'])]
 row={'name':name,'runtime':'PARI/GP 2.15.2','exit_code':rc,'stderr_errors':errors,'elapsed_seconds':time.time()-started,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'execution_input_sha256':hashlib.sha256(runfile.read_bytes()).hexdigest(),'changes':'Only absolute runtime datadir and project-root paths replaced. Mathematical instructions unchanged.','output':str(path.relative_to(ROOT)),'output_sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
 rows.append(row);(AR/'writing_gp_reruns.json').write_text(json.dumps(rows,indent=2)+'\n');print('FINISH',name,rc,'errors',len(errors),'seconds',round(row['elapsed_seconds'],2),flush=True)
