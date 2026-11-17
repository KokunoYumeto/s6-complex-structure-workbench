#!/usr/bin/env python3
"""Build the research paper and retain every compiler transcript and overflow count."""
from pathlib import Path
import subprocess,sys,re,json,os
root=Path(__file__).resolve().parents[1]
tag=sys.argv[1] if len(sys.argv)>1 else "draft"
logdir=root/"build_logs"
logdir.mkdir(exist_ok=True)
name="S6_02_PUSH_paper"
if "--clean" in sys.argv[2:]:
    for suffix in ["aux","bbl","blg","toc","out"]:
        cached=root/(name+"."+suffix)
        if cached.exists():
            (logdir/(tag+"_previous_"+suffix+".txt")).write_bytes(cached.read_bytes())
            cached.unlink()
    print("Retained and cleared generated auxiliary files for a clean build.")
env=os.environ.copy()
local_env=root/"code"/"tex_runtime_environment.json"
if local_env.exists():
    values=json.loads(local_env.read_text())
    format_dir=Path(values.get("TEXFORMATS","").split("//")[0])
    if (format_dir/"lualatex.fmt").is_file():
        env.update(values)
        print("TEX_RUNTIME_ENV",local_env)
    else:
        print("Recorded runtime is not present at this location; using the system TeX installation. Run code/tex_runtime_setup.py only if needed.")
else:
    print("No local TeX runtime environment found; run code/tex_runtime_setup.py if the system format is unavailable.")
commands=[
 ["lualatex","-interaction=nonstopmode","-halt-on-error",name+".tex"],
 ["bibtex",name],
 ["lualatex","-interaction=nonstopmode","-halt-on-error",name+".tex"],
 ["lualatex","-interaction=nonstopmode","-halt-on-error",name+".tex"]
]
record=[]
for i,cmd in enumerate(commands):
    r=subprocess.run(cmd,cwd=root,capture_output=True,text=True,env=env)
    out=r.stdout+r.stderr
    path=logdir/f"{tag}_{i+1}.txt"
    path.write_text(out)
    print("COMMAND",cmd,"RETURN",r.returncode,"LOG",path.name)
    over=[float(x) for x in re.findall(r"Overfull \\[hv]box \(([0-9.]+)pt too (?:wide|high)\)",out)]
    record.append({"command":cmd,"returncode":r.returncode,"overfull_pt":over})
    if r.returncode:
        print(out[-6000:])
        break
(logdir/f"{tag}_summary.json").write_text(json.dumps(record,indent=2))
sys.exit(0 if all(r["returncode"]==0 for r in record) and len(record)==4 else 1)
