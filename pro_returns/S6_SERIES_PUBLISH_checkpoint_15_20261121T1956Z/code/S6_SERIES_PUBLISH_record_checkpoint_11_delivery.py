from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parents[1]
r=json.loads((root/'code/S6_SERIES_PUBLISH_checkpoint_11.out').read_text());u=json.loads((root/'records/S6_SERIES_PUBLISH_checkpoint_11_upload.json').read_text())['results'][0]
assert u['status']=='succeeded'
p=Path(r['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256']
record={'checkpoint':11,**r,'upload_receipt':'records/S6_SERIES_PUBLISH_checkpoint_11_upload.json','library_file_id':u['library_file_id'],'delivery':'Download link provided in conversation commentary; work continues.','next_checkpoint_utc':'2026-11-21T17:41:17+00:00','next_review_utc':'2026-11-21T17:11:17+00:00'}
out=root/'records/S6_SERIES_PUBLISH_checkpoint_11_delivery.json';assert not out.exists();out.write_text(json.dumps(record,indent=2)+'\n')
entry=f'\n## Checkpoint 11 delivered — {r["created_utc"]}\n\nThe scheduled archive contains {r["files"]} manifest-listed files, preserving all {r["restored_files_preserved"]} inherited checkpoint paths including the original manifest. Size: {r["size"]} bytes; SHA-256 `{r["sha256"]}`. Every archive member passed its size/hash verification. The archive was made available as a downloadable conversation file, and work continues. The next checkpoint is due at 17:41:17 UTC (18:41:17 Europe/Berlin); review06 is due at 17:11:17 UTC (18:11:17 Europe/Berlin). This packaging creates no mathematical check or page-reading credit. Receipt: `records/S6_SERIES_PUBLISH_checkpoint_11_delivery.json`.\n'
for name in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
 p=root/name;p.write_text(p.read_text()+entry)
print(json.dumps({'record':str(out.relative_to(root)),'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'checkpoint_verified':True}))
