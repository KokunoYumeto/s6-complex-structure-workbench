"""Replay both retained segmented CM derivative runs without mathematical edits."""
from pathlib import Path
import subprocess,os,hashlib,json,concurrent.futures
P=Path(__file__).resolve().parents[2];S=P.parents[1]/'sources/returns/S6_05_ARITHMETIC/code/Crank_cm_stream.cpp';D=P/'code/I/replay_arithmetic';RT=P/'build/arithmetic_runtime/root';L=RT/'usr/lib/x86_64-linux-gnu';env=dict(os.environ,LD_LIBRARY_PATH=str(L));b=S.read_bytes();p=D/S.name;p.write_bytes(b)
(P/'analysis/segmented_derivative_source.json').write_text(json.dumps({'source':str(S),'sha256':hashlib.sha256(b).hexdigest(),'receiving':str(p),'mathematical_edits':False,'precision_and_radius_parameters':[[384,128,170],[512,96,190]]},indent=2))
def run(prec,rad,cut):
 exe=P/'build/arithmetic_runtime'/('Crank_cm_stream_'+str(prec));log=P/'code/I/outputs'/('Crank_cm_stream_'+str(prec)+'.out')
 cmd=['g++','-O3','-std=c++17','-DWORK_PREC='+str(prec),'-DWORK_RAD='+str(rad),'-I'+str(RT/'usr/include'),str(p),'/lib/x86_64-linux-gnu/libmpfr.so.6','-lgmp','-o',str(exe)]
 c=subprocess.run(cmd,capture_output=True,text=True,env=env);log.with_suffix('.compile.txt').write_text(c.stdout+c.stderr)
 if c.returncode:raise RuntimeError('Compilation failed '+str(prec))
 with log.open('w') as f:r=subprocess.run([str(exe),'163','185801',str(cut)],stdout=f,stderr=subprocess.STDOUT,env=env)
 rec={'precision_bits':prec,'radius':rad,'cutoff':cut,'returncode':r.returncode,'output':str(log.relative_to(P))};log.with_suffix('.replay.json').write_text(json.dumps(rec,indent=2));print(json.dumps(rec),flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
 for f in [ex.submit(run,384,128,170),ex.submit(run,512,96,190)]:f.result()
