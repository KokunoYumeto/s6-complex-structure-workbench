from pathlib import Path
from zipfile import ZipFile
import tarfile, json, hashlib, collections, datetime

BASE=Path('/workspace/scratch/ae06852560d6')
ARCHIVE=BASE/'restored_downloads/S6_06_BLIND_checkpoint_36.zip'
DEST=BASE/'night36/S6_06_BLIND'
REPORT=BASE/'restore/S6_10_PAPERS/analysis/continuation_root/night36_text_extraction.json'
SUFFIXES={'.tex','.bib','.md','.csv','.tsv','.py','.sage','.gp','.sh','.cpp','.jl'}
with ZipFile(ARCHIVE) as z:
    m=json.loads(z.read('checkpoint36_transport_manifest.json'))
    selected={n:r for n,r in m['files'].items() if n.startswith('S6_06_BLIND/') and Path(n).suffix in SUFFIXES and not any(x in Path(n).parts for x in ('attempts','history','rendered','__pycache__'))}
    waiting=collections.defaultdict(list); records=[]
    def install(n,data,origin):
        r=selected[n]
        assert len(data)==r['bytes'] and hashlib.sha256(data).hexdigest()==r['sha256'],n
        q=DEST/Path(*Path(n).parts[1:]); assert q.resolve().is_relative_to(DEST.resolve())
        q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(data)
        records.append({'path':n,'bytes':len(data),'sha256':r['sha256'],'origin':origin})
    for n,r in selected.items():
        existing=DEST/Path(*Path(n).parts[1:])
        attached=BASE/'materials/S6_10_PAPERS_2_night_run/night_run'/Path(*Path(n).parts[1:])
        if n in z.namelist(): install(n,z.read(n),'direct current member')
        elif existing.is_file() and hashlib.sha256(existing.read_bytes()).hexdigest()==r['sha256']: install(n,existing.read_bytes(),'verified existing current member')
        elif attached.is_file() and hashlib.sha256(attached.read_bytes()).hexdigest()==r['sha256']: install(n,attached.read_bytes(),'byte-identical attached source')
        else:
            c=m['contents'][r['sha256']];assert c['storage']=='raw',n
            waiting[c['name']].append(n)
    print('Selected',len(selected),'files; raw payloads to retrieve',len(waiting),flush=True)
    for b in m['bundles']:
        if not waiting:break
        bn=b['file']
        with tarfile.open(fileobj=z.open(bn),mode='r|xz') as t:
            for member in t:
                if member.name in waiting:
                    data=t.extractfile(member).read()
                    for n in waiting.pop(member.name):install(n,data,bn)
        print('Read',bn,'remaining',len(waiting),flush=True)
    assert not waiting, list(waiting)[:10]
    REPORT.write_text(json.dumps({'checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'snapshot':m['snapshot'],'verified_files':len(records),'verified_bytes':sum(r['bytes'] for r in records),'files':records},indent=2)+'\n')
    print('VERIFIED',len(records),'files',flush=True)
