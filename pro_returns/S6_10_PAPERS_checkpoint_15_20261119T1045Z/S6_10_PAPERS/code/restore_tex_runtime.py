"""Restore the four archived CTAN dependencies and build a local LuaLaTeX format."""
from pathlib import Path
import hashlib,json,os,subprocess,tarfile,zipfile

ROOT=Path(__file__).resolve().parents[3]
PROJECT=ROOT/'work/S6_10_PAPERS'
RUNTIME=PROJECT/'build/tex_runtime'
RUNTIME.mkdir(parents=True,exist_ok=True)
PACKAGES=RUNTIME/'packages';PACKAGES.mkdir(exist_ok=True)
ARCHIVE=ROOT/'sources/newer_night/S6_06_BLIND_checkpoint_25.zip'

with zipfile.ZipFile(ARCHIVE) as z:
    manifest=json.loads(z.read('checkpoint25_transport_manifest.json'))
    wanted={v['sha256']:(k,v) for k,v in manifest['files'].items() if k.startswith('S6_06_BLIND/records/tooling/') and k.endswith('.zip')}
    for bundle in manifest['bundles']:
        if not wanted: break
        with tarfile.open(fileobj=z.open(bundle['file']),mode='r|xz') as t:
            for member in t:
                sha=member.name.removeprefix('content/')
                if sha not in wanted:continue
                name,record=wanted.pop(sha)
                data=t.extractfile(member).read()
                assert len(data)==record['bytes'] and hashlib.sha256(data).hexdigest()==sha
                path=RUNTIME/Path(name).name;path.write_bytes(data)
                with zipfile.ZipFile(path) as package:
                    for entry in package.infolist():
                        target=PACKAGES/entry.filename
                        assert target.resolve().is_relative_to(PACKAGES.resolve())
                        if entry.is_dir():target.mkdir(parents=True,exist_ok=True)
                        else:
                            target.parent.mkdir(parents=True,exist_ok=True)
                            target.write_bytes(package.read(entry))
                print('Restored',path.name,flush=True)
    assert not wanted

env=os.environ.copy()
env['TEXMF']='{/usr/share/texlive/texmf-dist,/usr/share/texmf}'
env['TEXFORMATS']=str(RUNTIME)
env['TEXINPUTS']=str(PACKAGES)+'//:'
env['LUAINPUTS']=str(PACKAGES)+'//:'
env['TEXMFCACHE']=str(RUNTIME/'cache')
env['TEXMFVAR']=str(RUNTIME/'cache')
env['TEXMFOUTPUT']=str(RUNTIME/'cache')
Path(env['TEXMFCACHE']).mkdir(exist_ok=True)

commands=[
 (RUNTIME,['luahbtex','-ini','-interaction=nonstopmode','-halt-on-error','-jobname=lualatex','-progname=lualatex','lualatex.ini']),
 (PACKAGES/'lualibs',['luahbtex','--ini','--interaction=nonstopmode',r'\input plain \input lualibs.dtx']),
 (PACKAGES/'luatexbase',['luahbtex','--fmt=lualatex','--interaction=nonstopmode','luatexbase.ins'])]
for index,(cwd,command) in enumerate(commands):
    p=subprocess.run(command,cwd=cwd,env=env,capture_output=True,text=True)
    (RUNTIME/f'restore_{index}.log').write_text(p.stdout+'\n'+p.stderr)
    print(command[0],index,'exit',p.returncode,flush=True)
    if p.returncode:
        print(p.stdout[-4000:]);raise SystemExit(p.returncode)
(RUNTIME/'environment.json').write_text(json.dumps({k:env[k] for k in ['TEXMF','TEXFORMATS','TEXINPUTS','LUAINPUTS','TEXMFCACHE','TEXMFVAR','TEXMFOUTPUT']},indent=2))
print('Runtime prepared at',RUNTIME,flush=True)
