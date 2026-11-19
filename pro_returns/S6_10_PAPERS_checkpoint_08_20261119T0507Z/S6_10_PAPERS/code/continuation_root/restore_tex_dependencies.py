"""Restore exact archived TeX dependencies from the received night checkpoint36.

This is tooling restoration only. It awards no mathematical check. Supplied
archives and extracted dependencies stay outside checkpoint payloads.
"""
from pathlib import Path
import hashlib,io,json,os,subprocess,tarfile,zipfile
P=Path(__file__).resolve().parents[2]
W=P.parents[1]
R=P/'build/tex_runtime'
K=R/'packages';K.mkdir(parents=True,exist_ok=True)
archive=W/'restored_downloads/S6_06_BLIND_checkpoint_36.zip'
receipts=[]
with zipfile.ZipFile(archive) as z:
    manifest=json.loads(z.read('checkpoint36_transport_manifest.json'))
    wanted={v['sha256']:(k,v) for k,v in manifest['files'].items()
       if k.startswith('S6_06_BLIND/records/tooling/') and k.endswith('.zip')}
    for bundle in manifest['bundles']:
        if not wanted:break
        with tarfile.open(fileobj=z.open(bundle['file']),mode='r|xz') as t:
            for member in t:
                sha=member.name.removeprefix('content/')
                if sha not in wanted:continue
                name,record=wanted.pop(sha)
                data=t.extractfile(member).read()
                assert len(data)==record['bytes']
                assert hashlib.sha256(data).hexdigest()==sha
                with zipfile.ZipFile(io.BytesIO(data)) as package:
                    for entry in package.infolist():
                        target=K/entry.filename
                        assert target.resolve().is_relative_to(K.resolve())
                        if entry.is_dir():target.mkdir(parents=True,exist_ok=True)
                        else:
                            target.parent.mkdir(parents=True,exist_ok=True)
                            target.write_bytes(package.read(entry))
                receipts.append({'source':name,'bytes':len(data),'sha256':sha})
                print('Restored',Path(name).name,flush=True)
    assert not wanted,wanted
env=os.environ.copy();env.update(json.loads((R/'environment.json').read_text()))
Path(env['TEXMFCACHE']).mkdir(parents=True,exist_ok=True)
commands=[
 (R,['luahbtex','-ini','-interaction=nonstopmode','-halt-on-error','-jobname=lualatex','-progname=lualatex','lualatex.ini']),
 (K/'lualibs',['luahbtex','--ini','--interaction=nonstopmode',r'\input plain \input lualibs.dtx']),
 (K/'luatexbase',['luahbtex','--fmt=lualatex','--interaction=nonstopmode','luatexbase.ins'])]
for n,(cwd,command) in enumerate(commands):
    r=subprocess.run(command,cwd=cwd,env=env,capture_output=True,text=True)
    (R/f'continuation_restore_{n}.log').write_text(r.stdout+'\n'+r.stderr)
    receipts.append({'command':command,'returncode':r.returncode})
    print('Tooling command',n,'exit',r.returncode,flush=True)
    if r.returncode:raise SystemExit(r.stdout[-3000:])
(P/'analysis/continuation_root/tex_runtime_restoration.json').write_text(json.dumps(receipts,indent=2)+'\n')
