"""Replay exact CM models, local heights, algebraic ranks and saturation.

Only runtime-path and output-path edits are applied. The rank-only variant
disables the separate non-certified analytic-rank evidence; certified analytic
claims use the other explicitly truncated programs.
"""
from pathlib import Path
import concurrent.futures,hashlib,json,os,subprocess

OUT=Path(__file__).resolve().parents[2];BASE=OUT.parents[1]
SRC=BASE/'sources/returns/S6_05_ARITHMETIC/code'
CODE=OUT/'code/I/replay_arithmetic';CODE.mkdir(exist_ok=True)
LOG=OUT/'code/I/outputs';LOG.mkdir(exist_ok=True)
RT=OUT/'build/arithmetic_runtime/root';LIB=RT/'usr/lib/x86_64-linux-gnu'
ENV=dict(os.environ);ENV['LD_LIBRARY_PATH']=str(LIB)

def prepare(name,change=lambda s:s):
 data=(SRC/name).read_text();data2=change(data);dest=CODE/name;dest.write_text(data2)
 return {'source':str((SRC/name).relative_to(BASE)),'source_sha256':hashlib.sha256(data.encode()).hexdigest(),'receiving':str(dest.relative_to(OUT)),'receiving_sha256':hashlib.sha256(data2.encode()).hexdigest(),'changed':data!=data2}

def paths(s):
 return '\n'.join(x for x in s.splitlines() if not x.startswith('default(datadir'))+'\n'

def gp_job(name):
 with (LOG/(name+'.stdout.txt')).open('w') as f:
  r=subprocess.run([str(RT/'usr/bin/gp'),'-f','-q',str(CODE/name)],env=ENV,cwd=OUT,stdout=f,stderr=subprocess.STDOUT)
 text=(LOG/(name+'.stdout.txt')).read_text()
 return {'job':name,'exit_code':r.returncode,'gp_error':bool('\n  ***' in text),'output':str((LOG/(name+'.stdout.txt')).relative_to(OUT))}

def main():
 records=[]
 records.append(prepare('C_cm_models.gp',lambda s:paths(s).replace('if(G[1]<=500000,print("database ",ellidentify(M)));','')))
 records.append(prepare('C_cm_local_heights.gp',paths))
 records.append(prepare('C_cm_rank_lvalues.gp',lambda s:paths(s).replace('if(k<=10,','if(k<=0,')))
 records.append(prepare('Crank_saturation.cpp'))
 (CODE/'source_manifest.json').write_text(json.dumps(records,indent=2))
 exe=OUT/'build/arithmetic_runtime/Crank_saturation'
 cmd=['g++','-O2','-std=c++17','-I'+str(RT/'usr/include'),'-I'+str(RT/'usr/include/x86_64-linux-gnu'),str(CODE/'Crank_saturation.cpp'),'-L'+str(LIB),'-lec','-lntl','-lpari','-lgmp','-o',str(exe)]
 compiled=subprocess.run(cmd,capture_output=True,text=True,env=ENV)
 (LOG/'Crank_saturation.compile.txt').write_text(compiled.stdout+compiled.stderr)
 if compiled.returncode:raise RuntimeError('Compilation failed; see compile output')
 def saturate():
  with (LOG/'Crank_saturation.stdout.txt').open('w') as f:
   r=subprocess.run([str(exe)],stdout=f,stderr=subprocess.STDOUT,env=ENV)
  return {'job':'Crank_saturation','exit_code':r.returncode,'output':'code/I/outputs/Crank_saturation.stdout.txt'}
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
  jobs=[pool.submit(gp_job,name) for name in ('C_cm_models.gp','C_cm_local_heights.gp','C_cm_rank_lvalues.gp')]+[pool.submit(saturate)]
  for fut in concurrent.futures.as_completed(jobs):
   rec=fut.result();print(json.dumps(rec),flush=True)

if __name__=='__main__':main()
