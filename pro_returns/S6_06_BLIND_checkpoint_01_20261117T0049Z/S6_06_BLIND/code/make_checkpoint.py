"""Create an immutable complete hourly checkpoint. Upload is a separate tool step."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys,zipfile
root=Path(__file__).resolve().parents[1]
n=int(sys.argv[1]); target=root.parent/f'S6_06_BLIND_checkpoint_{n:02d}.zip'
if target.exists():raise SystemExit('Refusing to overwrite an earlier checkpoint')
now=datetime.now(timezone.utc).isoformat()
part5={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest()
       for p in (root/'notes/part5.tex',root/'notes/part5_blind.md')}
record={'checkpoint':target.name,'created_utc':now,'blind_part5_sha256':part5,
        'comparison_paper_opened_before_this_checkpoint':False if n==1 else 'see chronological log'}
(root/f'records/checkpoint_{n:02d}.json').write_text(json.dumps(record,indent=2)+'\n')
with (root/'S6_06_BLIND_literature_log.md').open('a') as f:
    f.write(f'\n| {now} | {target.name} | Hourly checkpoint; complete independent Part 5 proof included | Part 5 hashes in records/checkpoint_{n:02d}.json. Comparison paper remains unopened before checkpoint 01. |\n')
with zipfile.ZipFile(target,'x',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in sorted(root.rglob('*')):
        if p.is_file():z.write(p,p.relative_to(root.parent))
print(json.dumps({'path':str(target),'bytes':target.stat().st_size,'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'record':record}))
