from pathlib import Path
import json,os,subprocess
root=Path(__file__).resolve().parents[1]
env={**os.environ,**json.loads((root/'code/tex_runtime_environment.json').read_text())}
p=subprocess.run(['texlua',str(root/'code/tex_runtime_diagnostic.lua')],env=env,capture_output=True,text=True)
print(p.stdout+p.stderr)
print('RETURN',p.returncode)
rt=root.parent/'tex_runtime'
tex=rt/'cache_diagnostic.tex'
tex.write_text('\\catcode123=1 \\catcode125=2 \\directlua{dofile("'+str(root/'code/tex_runtime_diagnostic.lua')+'")}\\end\n')
p=subprocess.run(['luahbtex','--ini','--interaction=nonstopmode','--halt-on-error',tex.name],cwd=rt,env=env,capture_output=True,text=True)
print(p.stdout+p.stderr)
print('ENGINE_RETURN',p.returncode)
