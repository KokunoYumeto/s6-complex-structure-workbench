#!/usr/bin/env python3
"""Create a timed lean overlay checkpoint, preserving immutable earlier ZIPs.

The attached base plus this newest overlay restores the continuation. Current
deliverables and all code are included; unchanged cp21 working files, published
downloads, rendered pages and per-batch full copies are omitted.
"""
from pathlib import Path
import argparse,csv,datetime as dt,hashlib,io,json,os,zipfile

R=Path(__file__).resolve().parents[1];BASE=R.parent
csv.field_size_limit(100_000_000)
def sha(b):return hashlib.sha256(b).hexdigest()
def main():
 p=argparse.ArgumentParser();p.add_argument('number',type=int);p.add_argument('--due',required=True);a=p.parse_args()
 due=dt.datetime.fromisoformat(a.due.replace('Z','+00:00'));now=dt.datetime.now(dt.timezone.utc)
 assert now>=due, f'Checkpoint is not due until {due.isoformat()}'
 assert (now-due).total_seconds()<600, 'Use the actual scheduled interval and record any delay explicitly.'
 out=BASE/'deliverables';out.mkdir(exist_ok=True);z=out/f'S6_SERIES_PUBLISH_checkpoint_{a.number:02d}.zip'
 assert not z.exists(), 'Earlier checkpoints are immutable.'
 with (BASE/'CP21_INDEX.tsv').open(newline='') as f:base={x['path']:x for x in csv.DictReader(f,delimiter='\t',quoting=csv.QUOTE_NONE)}
 comp=json.loads((R/'records/S6_SERIES_PUBLISH_required_check_completion_manifest.json').read_text())
 resolved=sum(x['paper']=='II' for x in comp['rows'].values())
 sourcehash=sha((R/'S6_SERIES_PUBLISH_II.tex').read_bytes());ledgerhash=sha((R/'CHECK_EVENTS.tsv').read_bytes())
 text=f'\n\n## Checkpoint {a.number:02d} snapshot — {now.isoformat()}\n\nScheduled at {due.isoformat()} under the 45-minute rule. Paper II has {resolved}/197 required rows resolved and {197-resolved} open. Paper II source SHA-256 `{sourcehash}`; event-ledger SHA-256 `{ledgerhash}`. This checkpoint contains current deliverables, all code and the changed working evidence needed with the attached base. Unchanged checkpoint-21 working files, published-source downloads and page images are excluded. Papers I and V retain their closed gates and are awaiting the five-together step. Papers III and IV have not begun. No Paper II final PDF or rendered-page reading is certified; its integrated build and complete page reading remain open. Packaging creates no progress-row movement or check event.\n'
 journals=[]
 for name in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
  q=R/name;b=q.read_bytes();assert f'## Checkpoint {a.number:02d} snapshot'.encode() not in b
  q.write_bytes(b+text.encode());journals.append({'path':name,'before_sha256':sha(b),'after_sha256':sha(q.read_bytes()),'appended_text':text})
 receiptpath=R/'records'/f'S6_SERIES_PUBLISH_checkpoint_{a.number:02d}_snapshot.json'
 assert not receiptpath.exists();receiptpath.write_text(json.dumps(dict(created_utc=now.isoformat(),scheduled_utc=due.isoformat(),
  II_required_resolved=resolved,II_required_open=197-resolved,source_sha256=sourcehash,ledger_sha256=ledgerhash,journal_appends=journals,
  scope='Lean overlay of current deliverables, code and changed necessary working files; base files remain required. No checkpoint archives or inherited unchanged working evidence copied.'),indent=2)+'\n')
 # Snapshot immutable byte payloads, then reject a concurrent change in any one
 # selected file before writing the archive. Agent-owned in-progress files may
 # be retried, but no canonical source is changed during this operation.
 excluded_dirs={'__pycache__','render','rendered','vendor','tex-runtime','source_cache','downloads','tmp'}
 excluded_suffix={'.png','.jpg','.jpeg','.gif','.webp','.pyc','.whl','.fmt','.synctex','.gz','.zip','.pending'}
 excluded=[]
 for attempt in range(5):
  files=[];stats={};excluded=[]
  for q in sorted(R.rglob('*')):
   if not q.is_file():continue
   rel=q.relative_to(R);name=rel.as_posix()
   if any(x in excluded_dirs for x in rel.parts) or q.suffix.lower() in excluded_suffix:continue
   if q.suffix.lower()=='.pdf':
    proof=R/'records'/f'{q.stem}_final_pdf_receipt.json'
    if q.parent!=R or not proof.exists():continue
    d=json.loads(proof.read_text())
    if not d.get('all_pages_read') or d.get('pdf_sha256')!=sha(q.read_bytes()):continue
   if q.parent==R and '_filelist.tsv' in q.name:continue
   st=q.stat();b=q.read_bytes();h=sha(b)
   current_deliverable=q.parent==R
   all_code=rel.parts[0]=='code'
   changed=name not in base or h!=base[name]['sha256']
   if not(current_deliverable or all_code or changed):continue
   if name.startswith('records/') and 'recomputed/' in name:continue
   files.append((name,b,'current deliverable' if current_deliverable else 'code' if all_code else 'changed working evidence'))
   stats[name]=(st.st_size,st.st_mtime_ns)
  if all((R/name).exists() and ((R/name).stat().st_size,(R/name).stat().st_mtime_ns)==s for name,s in stats.items()):break
 else:raise RuntimeError('Working files continued changing during checkpoint snapshot; no ZIP created.')
 readme=f'''# Checkpoint {a.number:02d}\n\nINCOMPLETE. This is the continuation snapshot at {now.isoformat()}.\n\nRestore the supplied S6_SERIES_PUBLISH_continue_cp21 base once and verify it with restore_cp21.py and BASE_FILELIST.tsv. Copy its S6_SERIES_PUBLISH_checkpoint_21 folder to the working directory, then overlay this ZIP at that working-directory root. The base and this ZIP alone suffice; earlier continuation checkpoint ZIPs are unnecessary.\n\nThe file list records every payload's exact size and SHA-256. It does not hash itself. The ZIP has been read back and every listed payload verified before delivery.\n\nPaper II: {resolved}/197 required rows resolved, {197-resolved} open. All 25 defect classes, restructuring, provenance, integrated typesetting and full rendered-page reading remain subject to their recorded gates. Papers III and IV follow completion of II. Papers I and V retain their closed gates until final integration. The independent E.5.3 check was admitted without changing its mathematical statement.\n\nOnly current certified PDFs are distributable; no unchecked working PDF is included. The attached base intentionally omits reconstructible PDFs. Published readings and inherited checks retain their existing credit. The posted Paper I and V sources in the base remain the texts of record for the five-together step.\n\nUnchanged base working files and prior full per-batch backups are omitted. All current code and new necessary check packets, freeze/release receipts, precise source diffs, appended check/defect rows and completion records are included. Current derived records occur once; refresh programs preserve the event ledger and the other papers' held rows.\n'''
 files.append((f'S6_SERIES_PUBLISH_checkpoint_{a.number:02d}_README.md',readme.encode(),'restore instructions'))
 rows=[dict(path=n,size=len(b),sha256=sha(b),scope=s) for n,b,s in files]
 buffer=io.StringIO(newline='');w=csv.DictWriter(buffer,fieldnames=['path','size','sha256','scope'],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
 temp=z.with_suffix('.zip.pending');assert not temp.exists()
 with zipfile.ZipFile(temp,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as archive:
  for name,b,_ in files:archive.writestr(name,b)
  archive.writestr(f'S6_SERIES_PUBLISH_checkpoint_{a.number:02d}_filelist.tsv',buffer.getvalue())
 assert temp.stat().st_size<500_000_000
 with zipfile.ZipFile(temp) as archive:
  assert archive.testzip() is None
  assert len(archive.namelist())==len(rows)+1
  for row in rows:
   b=archive.read(row['path']);assert len(b)==row['size'] and sha(b)==row['sha256']
 os.link(temp,z);temp.unlink()
 result=dict(path=str(z),created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),scheduled_utc=due.isoformat(),
  files=len(files),bytes=z.stat().st_size,sha256=sha(z.read_bytes()),all_payload_hashes_verified=True,
  required_II_resolved=resolved,required_II_open=197-resolved,base_required=True)
 (R/'records'/f'S6_SERIES_PUBLISH_checkpoint_{a.number:02d}_zip_receipt.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
