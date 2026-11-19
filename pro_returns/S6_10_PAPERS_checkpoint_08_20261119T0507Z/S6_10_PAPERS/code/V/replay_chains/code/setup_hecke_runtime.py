"""Install the pinned public Hecke package in this task's disposable cache."""
from pathlib import Path
import os,subprocess
root=Path(__file__).resolve().parents[1]
cache=root.parent/'external_cache/integral_conjugacy_runtime'
tmp=cache/'tmp';tmp.mkdir(parents=True,exist_ok=True)
env=os.environ.copy()
env.update({'TMPDIR':str(tmp),'JULIA_DEPOT_PATH':str(cache/'depot'),'JULIA_NUM_THREADS':'2','JULIA_NUM_PRECOMPILE_TASKS':'2'})
cmd=[str(cache/'julia-1.10.10/bin/julia'),'--startup-file=no','--project='+str(cache/'env'),'-e','using Pkg; Pkg.add(PackageSpec(name="Hecke", version="0.41.1")); Pkg.status()']
raise SystemExit(subprocess.run(cmd,env=env,cwd=root).returncode)
