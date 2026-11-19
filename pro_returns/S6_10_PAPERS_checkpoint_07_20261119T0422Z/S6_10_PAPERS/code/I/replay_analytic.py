"""Recompute exact Fourier coefficients and directed L-value certificates.

Every numerical claim remains tied to the explicit source algorithm, interval
arithmetic and tail printed in its output. Exact coefficient files are new
outputs; no previous numerical enclosure is fed to the executable.
"""
from pathlib import Path
import concurrent.futures,hashlib,json,os,subprocess,shutil,re
OUT=Path(__file__).resolve().parents[2];BASE=OUT.parents[1]
SRC=BASE/'sources/returns/S6_05_ARITHMETIC'
CODE=OUT/'code/I/replay_arithmetic';LOG=OUT/'code/I/outputs';REC=OUT/'code/I/records'
RT=OUT/'build/arithmetic_runtime/root';LIB=RT/'usr/lib/x86_64-linux-gnu'
ENV=dict(os.environ);ENV['LD_LIBRARY_PATH']=str(LIB)

def run(cmd,name):
 with (LOG/name).open('w') as f:
  result=subprocess.run([str(x) for x in cmd],cwd=OUT,env=ENV,stdout=f,stderr=subprocess.STDOUT)
 text=(LOG/name).read_text()
 if result.returncode or any('***' in line and 'Warning:' not in line for line in text.splitlines()):raise RuntimeError(name+' failed')
 print(json.dumps({'job':name,'exit_code':result.returncode,'bytes':len(text)}),flush=True)
 return text

def main():
 manifest=[]
 for name in ('Crank_coefficients.gp','Crank_derivatives.cpp','B_C6_central_stream.cpp'):
  raw=(SRC/'code'/name).read_text();text=raw
  if name.endswith('.gp'):text=text.replace('S6_05_ARITHMETIC/records/','code/I/records/')
  (CODE/name).write_text(text)
  manifest.append({'source':str((SRC/'code'/name).relative_to(BASE)),'sha256':hashlib.sha256(raw.encode()).hexdigest(),'receiving_sha256':hashlib.sha256(text.encode()).hexdigest(),'edit':'output directory only' if raw!=text else 'unchanged'})
 (CODE/'analytic_source_manifest.json').write_text(json.dumps(manifest,indent=2))
 for name in ('Crank_derivatives','B_C6_central_stream'):
  cmd=['g++','-O3','-std=c++17','-I'+str(RT/'usr/include'),str(CODE/(name+'.cpp')),'/lib/x86_64-linux-gnu/libmpfr.so.6','-lgmp','-o',str(OUT/'build/arithmetic_runtime'/name)]
  run(cmd,name+'.compile.txt')
 gp=RT/'usr/bin/gp';ex=OUT/'build/arithmetic_runtime'
 # Fresh coefficient files: GP write() appends, so remove only this driver's
 # previous outputs before a deliberate rerun.
 for i in range(1,11):(REC/f'Crank_coeff_{i}.dat').unlink(missing_ok=True)
 run([gp,'-f','-q',CODE/'Crank_coefficients.gp'],'Crank_coefficients.stdout.txt')
 # The auxiliary twist identities were separately checked exactly. Generate
 # its central-value coefficients directly from the displayed model.
 aux='''default(parisizemax,1000000000);\nJ=[54000,16581375,-32768,-884736000,-147197952000];\nidx=[2,4,6,9,10];D=[-23,-31,-19,-19,-3];\nfor(k=1,5,t=J[k]/1728;E=ellminimalmodel(ellinit([0,0,0,-3/4*t^3*(t-1),1/4*t^4*(t-1)^2]));A=ellminimalmodel(elltwist(E,D[k]));N=ellglobalred(A)[1];M=ceil(60*sqrt(N)/(2*Pi));aa=ellan(A,M);fn=Str("code/I/records/B_C6_aux_coeff_",idx[k],".dat");write(fn,N," ",M);for(n=1,M,write(fn,aa[n]));print(idx[k]," ",N," ",M));\nquit;\n'''
 (CODE/'auxiliary_coefficients.gp').write_text(aux)
 for i in (2,4,6,9,10):(REC/f'B_C6_aux_coeff_{i}.dat').unlink(missing_ok=True)
 run([gp,'-f','-q',CODE/'auxiliary_coefficients.gp'],'B_C6_auxiliary_coefficients.stdout.txt')
 jobs=[]
 # These ten sums re-evaluate the displayed derivative values. The six
 # rank-one rational-factor claims also receive directed interval sums.
 for i in range(1,11):jobs.append(([ex/'Crank_derivatives',REC/f'Crank_coeff_{i}.dat'],f'Crank_derivative_{i}.stdout.txt'))
 for i in (2,4,6,9,10):
  jobs.append(([ex/'B_C6_central_stream','--file',REC/f'B_C6_aux_coeff_{i}.dat'],f'B_C6_central_file_{i}.out'))
  jobs.append(([ex/'B_C6_central_stream','--dfile',REC/f'Crank_coeff_{i}.dat'],f'B_C6_derivative_{i}.out'))
 jobs.append(([ex/'B_C6_central_stream',163,-557403,60],'B_C6_central_11.out'))
 jobs.append(([ex/'B_C6_central_stream','--derivative',163,185801,60],'B_C6_derivative_11.out'))
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
  futures=[pool.submit(run,*job) for job in jobs]
  for future in concurrent.futures.as_completed(futures):future.result()

if __name__=='__main__':main()
