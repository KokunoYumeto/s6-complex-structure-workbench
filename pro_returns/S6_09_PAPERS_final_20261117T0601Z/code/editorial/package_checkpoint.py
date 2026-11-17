"""Create one immutable full hourly checkpoint; never use for extra snapshots."""
from pathlib import Path
import argparse, datetime, hashlib, json, zipfile
P=Path(__file__).resolve().parents[3]
D=P/'deliverables'
p=argparse.ArgumentParser();p.add_argument('number',type=int);p.add_argument('--time',required=True);a=p.parse_args()
name=f'S6_09_PAPERS_checkpoint_{a.number:02d}.zip'
out=P/name
if out.exists():raise SystemExit('Refusing to overwrite an existing checkpoint')
rec={'checkpoint':a.number,'utc':a.time,'name':name,'state':'INCOMPLETE; all three complete canonical papers are frozen with clean final LuaLaTeX logs; final changed-page visual records, global companion-reference/evidence consistency, checkpoint-byte retention and final archive gate are closing','restore':'Restore this archive into the task directory, re-extract the eight attached archives under sources/ with their existing paths, then read work/root/RESUME.md and S6_09_PAPERS_report.md. The archive contains all deliverables and every writing/audit/computation record written so far.'}
(D/'records'/f'checkpoint_{a.number:02d}.json').write_text(json.dumps(rec,indent=2)+'\n')
files=sorted(x for x in D.rglob('*') if x.is_file())
with zipfile.ZipFile(out,'x',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for f in files:z.write(f,f.relative_to(D))
with zipfile.ZipFile(out) as z:
    bad=z.testzip()
    if bad:raise SystemExit('CRC failure: '+bad)
print(json.dumps({'path':str(out),'bytes':out.stat().st_size,'files':len(files),'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'utc':a.time}))
