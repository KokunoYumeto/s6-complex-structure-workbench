"""Run the real LuaLaTeX engine using the workspace-local repaired format."""
from pathlib import Path
import os,json,subprocess,sys,time

ROOT=Path(__file__).resolve().parents[2]
env={**os.environ,**json.loads((ROOT/'code/editorial/tex_runtime_environment.json').read_text())}
stem='S6_09_PAPERS_'+(sys.argv[1] if len(sys.argv)>1 else 'I')
stage=sys.argv[2] if len(sys.argv)>2 else '01'
cmd=['lualatex','-interaction=nonstopmode','-halt-on-error','-file-line-error',stem+'.tex']
start=time.time()
with (ROOT/'editorial'/(stem+'_build_'+stage+'.stdout.txt')).open('w') as f:
    result=subprocess.run(cmd,cwd=ROOT,env=env,stdout=f,stderr=subprocess.STDOUT)
print('Return code',result.returncode,'elapsed',round(time.time()-start,2))
if result.returncode:
    print((ROOT/'editorial'/(stem+'_build_'+stage+'.stdout.txt')).read_text()[-4500:])
else:
    print((ROOT/'editorial'/(stem+'_build_'+stage+'.stdout.txt')).read_text()[-1200:])
sys.exit(result.returncode)
