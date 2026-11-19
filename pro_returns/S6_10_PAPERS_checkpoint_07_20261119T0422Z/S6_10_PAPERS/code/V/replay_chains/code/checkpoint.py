"""Freeze one hourly research snapshot, then package only after QA.

Usage: python code/checkpoint.py freeze NUMBER
       python code/checkpoint.py package NUMBER
The two steps allow a clean LuaLaTeX build and visual inspection of the
frozen copy while research continues in the working project. Existing
snapshots and archives are never overwritten.
"""
from pathlib import Path
import sys,shutil,datetime,hashlib,json,zipfile

root=Path(__file__).resolve().parents[1]
parent=root.parent
mode,number=sys.argv[1],int(sys.argv[2])
stage=parent/f'checkpoint_build_{number:02}'
copy=stage/root.name
if mode=='freeze':
    if stage.exists():raise SystemExit('Snapshot already exists; refusing overwrite.')
    stage.mkdir()
    shutil.copytree(root,copy,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
    (stage/'tex_runtime').symlink_to(parent/'tex_runtime',target_is_directory=True)
    record={'checkpoint':number,'source_frozen_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'source_project':root.name,'excludes':['original supplied attachments','downloaded external full-text PDFs','reserved external database','Python bytecode'],
            'build_status':'Frozen copy requires build and visual QA before packaging.'}
    (copy/'records'/f'checkpoint_{number:02}_manifest.json').write_text(json.dumps(record,indent=2))
    print(json.dumps(record,indent=2))
elif mode=='package':
    archive=parent/f'{root.name}_checkpoint_{number:02}.zip'
    if archive.exists():raise SystemExit('Archive already exists; refusing overwrite.')
    qa=json.loads((copy/'records/pdf_qa/qa.json').read_text())
    if qa['overflows_over_2pt'] or qa['unresolved_citations']:
        raise SystemExit('Unresolved typesetting defects prevent packaging.')
    if 'Awaiting' in qa['visual_review']:
        raise SystemExit('Visual review has not yet been recorded.')
    manifest=copy/'records'/f'checkpoint_{number:02}_manifest.json'
    data=json.loads(manifest.read_text())
    data['build_status']='LuaLaTeX/BibTeX clean; sampled pages visually reviewed.'
    data['pdf_qa']=qa
    manifest.write_text(json.dumps(data,indent=2))
    files=sorted(p for p in copy.rglob('*') if p.is_file() and '__pycache__' not in p.parts)
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in files:z.write(p,p.relative_to(stage))
    record={'checkpoint':number,'archive':str(archive),'bytes':archive.stat().st_size,
            'files':len(files),'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),
            'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    (root/'records'/f'checkpoint_{number:02}_archive.json').write_text(json.dumps(record,indent=2))
    print(json.dumps(record,indent=2))
else:raise SystemExit('Use freeze or package.')
