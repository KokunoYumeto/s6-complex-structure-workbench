#!/usr/bin/env python3
"""Scheduled lean checkpoints relative to the supplied checkpoint62 base."""
import argparse,csv,hashlib,io,json,zipfile
from datetime import datetime,timedelta,timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parent
START=datetime(2026,11,24,11,15,57,tzinfo=timezone.utc)
def sha(data):return hashlib.sha256(data).hexdigest()
def table(path):
    with path.open(newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
def changed():
    baseline=table(BASE/'BASE_FILELIST.tsv')
    prefix=ROOT.name+'/'
    old={r['path'][len(prefix):]:r['sha256'] for r in baseline if r['path'].startswith(prefix)}
    old_hashes={r['sha256'] for r in baseline}
    old_hashes.update(r['sha256'] for r in table(BASE/'CP62_INDEX.tsv'))
    data={}
    for path in sorted(ROOT.rglob('*')):
        if not path.is_file():continue
        rel=path.relative_to(ROOT)
        if any(s in {'__pycache__','.git','build','renders','rendered','tmp','downloads'} for s in rel.parts):continue
        if path.suffix in {'.pyc','.aux','.fls','.fdb_latexmk','.toc','.synctex','.zip','.png','.jpg','.jpeg'}:continue
        b=path.read_bytes();digest=sha(b)
        if old.get(str(rel))==digest or digest in old_hashes:continue
        if path.suffix.lower() in {'.md','.tex','.tsv','.csv','.py','.json','.out','.txt','.bib'}:
            assert b'\r\n' not in b,('Non-LF text',str(rel))
        assert 'external_tmp' not in str(rel)
        data[str(rel)]=b
    return data

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('mode',choices=['inspect','pack'])
    ap.add_argument('--number',type=int,default=63)
    args=ap.parse_args()
    if args.mode=='inspect':
        data=changed()
        print(json.dumps({'changed_files':len(data),'uncompressed_bytes':sum(map(len,data.values())),
              'largest':sorted(((len(v),k) for k,v in data.items()),reverse=True)[:15]},indent=2))
        return
    assert args.number>=63
    due=START+timedelta(minutes=45*(args.number-62))
    now=datetime.now(timezone.utc)
    assert now>=due,('Checkpoint not due',due.isoformat())
    output=BASE.parent/'output';output.mkdir(exist_ok=True)
    dest=output/f'S6_SERIES_PUBLISH_checkpoint_{args.number}.zip'
    assert not dest.exists(),'Retain every earlier checkpoint without replacement.'
    rows=table(ROOT/'S6_SERIES_PUBLISH_required_progress_III.tsv')
    done=[r for r in rows if r['status']=='done']
    closed=[r['tag'] for r in done if r['check_event_id'].startswith('publish:c6:')]
    pending=[r['tag'] for r in rows if r['status']!='done' and r['proof_status']=='released_after_derivation']
    source_sha=sha((ROOT/'S6_SERIES_PUBLISH_III.tex').read_bytes())
    assert source_sha=='9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
    review=START+timedelta(hours=int((now-START).total_seconds()//3600)+1)
    section=f'''\n\n## Checkpoint {args.number} — {now.isoformat()}\n\nPaper III: {len(done)}/{len(rows)} required checks complete; {len(rows)-len(done)} open.\nRows closed in continuation six: {', '.join(closed) or 'none'}. The completed\ncomparisons and exact receiving repairs are in the continuation-six checker\nfolders; admitted repairs await the unit pass. The manuscript remains at\nSHA-256 {source_sha}; all756 unit criteria remain open.\nReleased comparisons still pending: {', '.join(pending) or 'none'}. The active\nD.2 and finite-family fresh derivations, their exact maps, and remaining\npre-exposure inputs are retained in the checker folders and required table.\nThe S8/S9 graph-line comparison has a confirmed D25 error: the projected\ncompression has an interior q=0 core meeting the source node shells. The\nfully reviewed independent sweep gives graph component degrees(0,0), while\nthe physical-dual degrees are(+1,-1), refuting that intermediate line\nidentification. Two narrow targeted events record this; both required rows\nremain open. The earlier band/core avoidance attempts are withdrawn at\nthat scope. The full corrected graph/cap/square and final return are still\nunder derivation; no final theorem conclusion is presently classified as\nrefuted. The independent incoming-boundary calculation is fully reviewed:\nits graph degree is m and the resulting cap restriction of b is2m. Both\nnarrow counterchecks have targeted events and D25 defect rows; neither\nsupplies the global square or final return. The directed period marking\nretains both integral based-period shears and their exact inverse maps.\nThe cap-normal Euler calculation remains under independent derivation.\nKQ passed full fresh review and its original was released; its complete\ncomparison remains pending. KR has fresh local/global maps and successful\nnew arithmetic; its original remains closed pending the complete fresh\nwrite-up and review. Prior KN and finite-root corrections retain their\nexact records. Paper IV retains66 required checks and729 unit criteria;\nthe disclosed cap-definition dependency reading earns no IV credit. Paper II remains\nfinal; Papers I and V retain their closed gates until the five-together step.\nThe report remains INCOMPLETE. This scheduled checkpoint includes changed/new\nwork only, with no original-source downloads or unchanged base copies.\nNext checkpoint: {(due+timedelta(minutes=45)).isoformat()}; next hourly\nreview: {review.isoformat()}. Packaging earns no movement credit.\n'''
    for name in ('S6_SERIES_PUBLISH_report.md','PROGRESS_LEDGER.md'):
        with (ROOT/name).open('a',newline='') as f:f.write(section)
    summary={'checkpoint':args.number,'scheduled_utc':due.isoformat(),'snapshot_utc':now.isoformat(),
             'required_done':len(done),'required_open':len(rows)-len(done),
             'closed_this_continuation':closed,'pending_released':pending,'path':str(dest)}
    log=json.dumps(summary,indent=2)+'\n'
    (ROOT/'code'/f'S6_SERIES_PUBLISH_c6_checkpoint_{args.number}.out').write_text(log,newline='\n')
    data=changed()
    readme=f'''# S6_SERIES_PUBLISH checkpoint {args.number}\n\nSnapshot: {now.isoformat()}; scheduled from {START.isoformat()}.\n\nUnpack the supplied S6_SERIES_PUBLISH_continue_cp62.zip once and run\npython restore_cp62.py at its root. Extract this checkpoint directly into\nthe merged S6_SERIES_PUBLISH_checkpoint_62 working directory, replacing\nthe same relative paths. The supplied base and this newest checkpoint\nrestore the workspace; no earlier return checkpoint is required.\n\nContinue Paper III's remaining required checks, then its unit restructuring,\nprovenance, build and every-page reading. Next complete Paper IV, then the\nfive-together step. I, II and V stay closed until that step. Read the latest\nreport and ledger sections and the live required-progress table. Current\nIII checks: {len(done)}/{len(rows)}; unit criteria:0/756. A saved fresh\nderivation or an authorized original release gives no completed-check credit\nuntil its full comparison and receiver are admitted.\n\nFresh proofs, individual release timestamps and exact comparison gates are\nrecorded in the checker folders. KN has a disclosed post-release correction\nto its fresh peripheral-column sign; the theorem conclusions agree. Finite\nOS49 work uses the corrected clockwise root action in its safe input packet.\nS8/S9 remain open after the compression-core and incoming-boundary\ncounterchecks refuted their intermediate graph-line and zero-cap\nidentifications. Read both root graph comparisons, the retained-shear\nperiod marking and current checker gates before using any staged S8/S9\nreceiver. The full square and return remain unresolved. KQ is released\nafter complete fresh review and its full comparison is pending. KR remains\nunexposed while its complete fresh write-up is prepared.\n\nThe file list records size and SHA256 of every payload except itself. No\nunchanged attached file, downloaded publication, extracted primary passage,\nsource-page image, old ZIP or generated inventory diff is included.\n\nNext checkpoint: {(due+timedelta(minutes=45)).isoformat()}.\nNext review: {review.isoformat()}. Continue without asking whether to proceed.\n'''
    data[f'S6_SERIES_PUBLISH_checkpoint_{args.number}_README.md']=readme.encode()
    buf=io.StringIO(newline='');writer=csv.writer(buf,delimiter='\t',lineterminator='\n')
    writer.writerow(['path','size','sha256'])
    for name,b in sorted(data.items()):writer.writerow([name,len(b),sha(b)])
    data[f'S6_SERIES_PUBLISH_checkpoint_{args.number}_filelist.tsv']=buf.getvalue().encode()
    with zipfile.ZipFile(dest,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
        for name,b in sorted(data.items()):archive.writestr(name,b)
    assert dest.stat().st_size<500_000_000
    with zipfile.ZipFile(dest) as archive:
        assert archive.testzip() is None
        for name,b in data.items():assert archive.read(name)==b
    print(log,end='')

if __name__=='__main__':main()
