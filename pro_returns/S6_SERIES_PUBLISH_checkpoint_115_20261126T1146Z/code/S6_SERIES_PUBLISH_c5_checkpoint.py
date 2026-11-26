#!/usr/bin/env python3
"""Scheduled lean continuation checkpoints, relative to the attached cp52 base."""
import argparse,csv,hashlib,io,json
from collections import Counter
from datetime import datetime,timedelta,timezone
from pathlib import Path
import zipfile

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parent
START=datetime(2026,11,23,18,26,17,tzinfo=timezone.utc)

def sha(b):return hashlib.sha256(b).hexdigest()
def table(p):
    with p.open(newline='') as f:return list(csv.DictReader(f,delimiter='\t'))

def changed():
    index=table(BASE/'BASE_FILELIST.tsv');prefix=ROOT.name+'/'
    old={r['path'][len(prefix):]:r['sha256'] for r in index if r['path'].startswith(prefix)}
    old_bytes={r['sha256'] for r in index}
    data={}
    for p in sorted(ROOT.rglob('*')):
        if not p.is_file():continue
        rel=p.relative_to(ROOT)
        if any(x in {'__pycache__','.git','build','renders','rendered','tmp','downloads'} for x in rel.parts):continue
        if p.suffix in {'.pyc','.aux','.fls','.fdb_latexmk','.toc','.synctex','.zip'}:continue
        b=p.read_bytes();h=sha(b)
        if old.get(str(rel))==h or h in old_bytes:continue
        data[str(rel)]=b
    return data

def main():
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['inspect','pack']);ap.add_argument('--number',type=int,default=53)
    args=ap.parse_args()
    if args.mode=='inspect':
        data=changed()
        for p,b in data.items():print(len(b),p)
        print('Changed/new files:',len(data),'uncompressed bytes:',sum(map(len,data.values())))
        return
    assert args.number>=53
    due=START+timedelta(minutes=45*(args.number-52));now=datetime.now(timezone.utc)
    assert now>=due,('Scheduled checkpoint is not due',due.isoformat())
    output=BASE.parent/'output';output.mkdir(exist_ok=True)
    dest=output/f'S6_SERIES_PUBLISH_checkpoint_{args.number}.zip'
    assert not dest.exists(),'Checkpoint already exists; retain its identity and advance the number.'
    rows=table(ROOT/'S6_SERIES_PUBLISH_required_progress_III.tsv')
    done=[r for r in rows if r['status']=='done']
    new=[r['tag'] for r in done if r['check_event_id'].startswith('publish:c5:')]
    pending=[r['tag'] for r in rows if r['status']!='done' and r['proof_status']=='released_after_derivation']
    next_review=START+timedelta(hours=int((now-START).total_seconds()//3600)+1)
    section=f'''\n\n## Checkpoint {args.number} — {now.isoformat()}\n\nPaper III has {len(done)} of {len(rows)} required checks complete; {len(rows)-len(done)} remain open.\nRequired rows closed during this continuation: {', '.join(new)}.\nThe separate 02KD integral-homology comparison is recorded without movement\ncredit in the 128-row table. The completed repairs remain in exact guarded\npackets; the manuscript source is unchanged at 9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0.\nAll 756 III unit criteria remain open. Individually released comparisons\nstill pending: {', '.join(pending) or 'none'}. Other assigned fresh derivations\nremain recorded in their checker folders and the required-progress table.\nPaper II's gate remains closed; I and V are reserved for the joint step.\nThis checkpoint contains only changed/new files relative to the attached\nbase, with no downloaded primary sources or unchanged attached bytes.\nNext scheduled checkpoint: {(due+timedelta(minutes=45)).isoformat()}.\nThe next hourly progress review is due at {next_review.isoformat()}.\n'''
    for name in ['S6_SERIES_PUBLISH_report.md','PROGRESS_LEDGER.md']:
        p=ROOT/name
        with p.open('a',newline='') as f:f.write(section)
    data=changed()
    readme=f'''# S6_SERIES_PUBLISH checkpoint {args.number}\n\nSaved {now.isoformat()}, on the 45-minute schedule begun at {START.isoformat()}.\n\nUnpack the attached S6_SERIES_PUBLISH_continue_cp52 base once and run its\nrestore_cp52.py verification before applying this checkpoint. Extract this\nZIP directly into the merged S6_SERIES_PUBLISH_checkpoint_52 working folder,\nreplacing the same relative paths. The attached base and this newest ZIP\nrestore the current workspace; earlier continuation checkpoints are unnecessary.\n\nRead the last sections of S6_SERIES_PUBLISH_report.md and PROGRESS_LEDGER.md.\nContinue the open III checks, then apply the guarded repairs in the unit\nrevision. Every source unit, build and page gate retains its recorded status.\nThe live required-progress table gives each frozen derivation, authorized\nproof release and admitted comparison. Do not treat a pending comparison as\na completed check. Current III count: {len(done)}/{len(rows)}.\n\nThe file list gives exact bytes for every payload file; it omits itself.\nOnly our changed/new work is included. Original attachments, downloaded\npublications, extracted primary text, source page images, old checkpoint ZIPs,\nand byte-identical base copies are excluded. Primary readings retain URLs,\nversions, hashes and precise loci in the checking records.\n'''
    data[f'S6_SERIES_PUBLISH_checkpoint_{args.number}_README.md']=readme.encode()
    out=io.StringIO(newline='');w=csv.writer(out,delimiter='\t',lineterminator='\n');w.writerow(['path','size','sha256'])
    for name,b in sorted(data.items()):w.writerow([name,len(b),sha(b)])
    data[f'S6_SERIES_PUBLISH_checkpoint_{args.number}_filelist.tsv']=out.getvalue().encode()
    with zipfile.ZipFile(dest,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for name,b in sorted(data.items()):z.writestr(name,b)
    with zipfile.ZipFile(dest) as z:
        assert z.testzip() is None
        for name,b in data.items():assert z.read(name)==b
    print(json.dumps(dict(path=str(dest),files=len(data),size=dest.stat().st_size,sha256=sha(dest.read_bytes()),required_done=len(done),required_open=len(rows)-len(done),closed_this_continuation=new,pending_released=pending),indent=2))

if __name__=='__main__':main()
