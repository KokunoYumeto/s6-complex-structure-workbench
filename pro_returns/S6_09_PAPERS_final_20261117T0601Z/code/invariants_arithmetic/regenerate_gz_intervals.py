from pathlib import Path
import subprocess,os,hashlib,time,json
ROOT=Path(__file__).resolve().parents[3];AR=ROOT/'deliverables/code/invariants_arithmetic/arithmetic';DEP=ROOT/'sources/audit_cache/inv_ari/deps/root';ENV=dict(os.environ);ENV['LD_LIBRARY_PATH']=str(DEP/'usr/lib/x86_64-linux-gnu');EXE=AR/'code/B_C6_central_stream'
rows=[]
CASES=[(2,54000,-23),(4,16581375,-31)]
for i,j,D in CASES:
 for derivative in [False,True]:
  dat=AR/'records'/('writing_gz_'+str(i)+('_derivative' if derivative else '_central')+'.dat')
  source='default(parisizemax,1000000000);\nt='+str(j)+'/1728; E=ellminimalmodel(ellinit([0,0,0,-3/4*t^3*(t-1),1/4*t^4*(t-1)^2])); '
  if not derivative:source+='E=ellminimalmodel(elltwist(E,'+str(D)+')); '
  source+='N=ellglobalred(E)[1]; M=ceil(60*sqrt(N)/(2*Pi)); A=ellan(E,M); write("'+str(dat)+'",N," '+('1 ' if derivative else '')+'",M); for(n=1,M,write("'+str(dat)+'",A[n])); print(N," ",M); quit;'
  gp=AR/'code'/('writing_gz_coeff_'+str(i)+('_d' if derivative else '_c')+'.gp');gp.write_text(source)
  if dat.exists():dat.unlink()
  start=time.time();print('COEFFICIENTS',i,derivative,flush=True)
  proc=subprocess.run([str(DEP/'usr/bin/gp'),'-fq',str(gp)],env=ENV,capture_output=True,text=True,check=True)
  assert not [line for line in (proc.stdout+proc.stderr).splitlines() if '***' in line and 'Warning:' not in line],proc.stderr
  name='B_C6_derivative_'+str(i)+'.out' if derivative else 'B_C6_central_file_'+str(i)+'.out'
  out=AR/'code'/name
  with out.open('w') as f:p=subprocess.run([str(EXE),'--dfile' if derivative else '--file',str(dat)],stdout=f,stderr=subprocess.STDOUT)
  rows.append({'index':i,'kind':'derivative' if derivative else 'central','command':[str(EXE),'--dfile' if derivative else '--file',str(dat)],'exit_code':p.returncode,'seconds':time.time()-start,'coefficient_sha256':hashlib.sha256(dat.read_bytes()).hexdigest(),'output_sha256':hashlib.sha256(out.read_bytes()).hexdigest()})
  (AR/'writing_gz_regeneration.json').write_text(json.dumps(rows,indent=2));print('FINISHED',name,p.returncode,flush=True)
for i,D,tw,aux in [(6,11,21,-399),(9,43,21,-399),(10,67,217,-651),(11,163,185801,-557403)]:
 for derivative in [False,True]:
  name='B_C6_derivative_'+str(i)+'.out' if derivative else ('B_C6_central_11.out' if i==11 else 'B_C6_central_file_'+str(i)+'.out')
  args=[str(EXE)]+(['--derivative'] if derivative else [])+[str(D),str(tw if derivative else aux),'60']
  out=AR/'code'/name;start=time.time();print('STREAM',name,flush=True)
  with out.open('w') as f:p=subprocess.run(args,stdout=f,stderr=subprocess.STDOUT)
  rows.append({'index':i,'kind':'derivative' if derivative else 'central','command':args,'exit_code':p.returncode,'seconds':time.time()-start,'output_sha256':hashlib.sha256(out.read_bytes()).hexdigest()});(AR/'writing_gz_regeneration.json').write_text(json.dumps(rows,indent=2));print('FINISHED',name,p.returncode,round(time.time()-start,2),flush=True)
ENV['PYTHONPATH']=str(ROOT/'deps/python');p=subprocess.run(['python',str(AR/'code/B_C6_exact_factors.py')],cwd=AR,env=ENV,text=True,capture_output=True);out=AR/'outputs/writing_B_C6_exact_factors_regenerated.txt';out.write_text(p.stdout+'\nSTDERR\n'+p.stderr);print('VERIFIER',p.returncode,p.stdout[-250:],p.stderr,flush=True)
