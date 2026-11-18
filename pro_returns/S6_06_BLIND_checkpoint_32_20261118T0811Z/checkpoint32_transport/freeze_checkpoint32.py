"""One complete hourly frozen file list, with exact immutable-file sharing.

Unchanged bytes may share an inode only with the already immutable31
freeze. Current research files are always copied. No live source is linked.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,re,shutil,time

ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parent
STAGE=BASE/'checkpoint32_encoding';FROZEN=STAGE/'frozen'
DUE=datetime.fromisoformat('2026-11-18T07:49:44+00:00')

def sha(path):
    with path.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def atomic(path,value):
    tmp=path.with_name(path.name+'.pending')
    tmp.write_text(json.dumps(value,indent=2)+'\n');tmp.replace(path)
def excluded(rel):
    source=any(rel.startswith(prefix) for prefix in (
        'records/primary_sources/','records/external_source_cache/',
        'records/sources/','records/part5_comparison/'))
    return ((source and Path(rel).suffix.lower() in
        ('.pdf','.txt','.png','.jpg','.jpeg','.tif','.tiff','.html'))
        or rel=='records/AC26_original_extracted.txt'
        or bool(re.fullmatch(r'records/web_\d+\.json',rel))
        or rel=='code/part1/ocr_wall.out')

assert datetime.now(timezone.utc)>=DUE,'Hourly freeze is not yet due'
STAGE.mkdir(exist_ok=True)
prior_path=BASE/'checkpoint31_encoding/frozen_manifest.json'
prior=json.loads(prior_path.read_text())
initial=STAGE/'freeze_initial.json';manifest=STAGE/'frozen_manifest.json'
if manifest.exists():
    d=json.loads(manifest.read_text())
    print(json.dumps({'status':'ALREADY_FROZEN','files':len(d['files']),
                      'utc':d['snapshot']['frozen_utc']}),flush=True)
    raise SystemExit
if not initial.exists():
    part5={p:sha(ROOT/p) for p in ['notes/part5.tex','notes/part5_blind.md']}
    assert part5=={'notes/part5.tex':'f7b2188bbd5fc453780421599b65168141c8ed09480b1396794f02f41a680e0f',
                  'notes/part5_blind.md':'ffdac7780a3d5c35565e31e6bb1bebf459e0f7dc75355e19fc216b5ba4b9a1e4'}
    snapshot={'checkpoint':32,'due_utc':DUE.isoformat(),
      'created_utc':datetime.now(timezone.utc).isoformat(),
      'prior_immutable_freeze':31,'prior_frozen_manifest_sha256':sha(prior_path),
      'blind_part5_sha256':part5,
      'scope':'One hourly complete project snapshot. Unchanged predecessor frozen bytes may share immutable inodes; no live research source is linked. All originals remain byte-hashed.'}
    receipt=ROOT/'records/checkpoint31_verification.json'
    if receipt.exists():
        verification=json.loads(receipt.read_text())
        assert verification['status']=='PASS'
        snapshot.update(verified_predecessor=31,predecessor_sha256=verification['sha256'])
    atomic(ROOT/'records/checkpoint_32.json',snapshot)
    marker='| S6_06_BLIND_checkpoint_32.zip |'
    log=ROOT/'S6_06_BLIND_literature_log.md'
    if marker not in log.read_text():
        with log.open('a') as out:
            out.write(f"\n| {snapshot['created_utc']} {marker} Complete hourly main-question snapshot | Every proof/code/log/attempt, exact rendered byte and immutable blind Part5 retained. |\n")
    names=[p.relative_to(ROOT).as_posix() for p in sorted(ROOT.rglob('*'))
           if p.is_file() and not excluded(p.relative_to(ROOT).as_posix())]
    atomic(initial,{'record':snapshot,'root_relative_file_list':names})
d=json.loads(initial.read_text());snapshot=d['record'];files={}
journal=STAGE/'freeze_journal.jsonl'
if journal.exists():
    for line in journal.read_text().splitlines():
        e=json.loads(line);files[e['name']]=e['info']
linked=copied=0
with journal.open('a') as log:
    for index,rel in enumerate(d['root_relative_file_list']):
        name='S6_06_BLIND/'+rel;source=ROOT/rel;dest=FROZEN/name
        if name in files:
            assert dest.stat().st_size==files[name]['bytes'] and sha(dest)==files[name]['sha256']
            continue
        dest.parent.mkdir(parents=True,exist_ok=True)
        for retry in range(8):
            before={'bytes':source.stat().st_size,'sha256':sha(source)}
            previous=BASE/'checkpoint31_encoding/frozen'/name
            tmp=dest.with_name(dest.name+'.freezing')
            if tmp.exists():tmp.rename(STAGE/f'interrupted_freeze_{index}_{retry}_{time.time_ns()}')
            sharing=(prior['files'].get(name)==before and previous.is_file())
            if sharing:
                assert previous.stat().st_size==before['bytes'] and sha(previous)==before['sha256']
                os.link(previous,tmp)
            else:shutil.copy2(source,tmp)
            after={'bytes':tmp.stat().st_size,'sha256':sha(tmp)}
            if before==after and source.stat().st_size==before['bytes'] and sha(source)==before['sha256']:
                tmp.replace(dest);linked+=int(sharing);copied+=int(not sharing);break
            tmp.rename(STAGE/f'changed_during_freeze_{index}_{retry}_{time.time_ns()}')
        else:raise RuntimeError('Continuously changed source: '+rel)
        files[name]=before
        log.write(json.dumps({'name':name,'info':before,'immutable_predecessor_link':sharing})+'\n')
        log.flush();os.fsync(log.fileno())
        if index%1500==0:print(json.dumps({'status':'FREEZING','files':index+1}),flush=True)
snapshot['frozen_utc']=datetime.now(timezone.utc).isoformat()
snapshot['completed_freeze_sharing']={'linked_this_invocation':linked,'copied_this_invocation':copied}
atomic(manifest,{'snapshot':snapshot,'files':files})
print(json.dumps({'status':'FROZEN','files':len(files),'utc':snapshot['frozen_utc'],
                  'linked':linked,'copied':copied}),flush=True)
