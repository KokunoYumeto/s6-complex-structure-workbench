"""Create an immutable complete hourly checkpoint. Upload is a separate tool step."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,sys,zipfile
root=Path(__file__).resolve().parents[1]
n=int(sys.argv[1]); target=root.parent/f'S6_06_BLIND_checkpoint_{n:02d}.zip'
if target.exists():raise SystemExit('Refusing to overwrite an earlier checkpoint')
now=datetime.now(timezone.utc).isoformat()
part5={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest()
       for p in (root/'notes/part5.tex',root/'notes/part5_blind.md')}
record={'checkpoint':target.name,'created_utc':now,'blind_part5_sha256':part5,
        'comparison_paper_opened_before_this_checkpoint':False if n==1 else 'see chronological log'}
# Preserve our proofs and provenance, without redistributing complete external
# books/articles, their OCR copies, or page-image reproductions.  The original
# working files remain available locally; the bibliography and download logs
# identify their sources.  Earlier immutable checkpoints are not modified.
source_roots=('records/primary_sources/','records/external_source_cache/',
              'records/sources/','records/part5_comparison/')
excluded=[]
for p in sorted(root.rglob('*')):
    if not p.is_file():continue
    rel=p.relative_to(root).as_posix()
    external=any(rel.startswith(prefix) for prefix in source_roots)
    raw_retrieval=bool(re.fullmatch(r'records/web_\d+\.json',rel))
    source_ocr=bool(re.fullmatch(r'code/part1/ocr_wall\.out',rel))
    if (external and p.suffix.lower() in ('.pdf','.txt','.png','.jpg','.jpeg','.tif','.tiff','.html')) or rel=='records/AC26_original_extracted.txt' or raw_retrieval or source_ocr:
        excluded.append({'path':rel,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
                         'reason':'External full-source payload or supplied-source duplicate; our proofs, source citations, read log and retrieval records are retained.'})
omitted={x['path'] for x in excluded}
(root/'records/source_payload_exclusions.json').write_text(json.dumps(excluded,indent=2)+'\n')
(root/f'records/checkpoint_{n:02d}.json').write_text(json.dumps(record,indent=2)+'\n')
with (root/'S6_06_BLIND_literature_log.md').open('a') as f:
    f.write(f'\n| {now} | {target.name} | Hourly checkpoint; complete independent Part 5 proof included | Part 5 hashes in records/checkpoint_{n:02d}.json. Comparison paper remains unopened before checkpoint 01. |\n')
with zipfile.ZipFile(target,'x',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in sorted(root.rglob('*')):
        if p.is_file() and p.relative_to(root).as_posix() not in omitted:
            z.write(p,p.relative_to(root.parent))
print(json.dumps({'path':str(target),'bytes':target.stat().st_size,'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'record':record}))
