from pathlib import Path
from collections import defaultdict,Counter
import hashlib,json,zipfile,subprocess,csv,datetime,zlib
ROOT=Path.cwd();D=ROOT/'deliverables'; Z=ROOT/'S6_09_PAPERS_checkpoint_06.zip'; OUT=ROOT/'delivery_compression_audit'
EXT={'.png','.jpg','.jpeg','.gif','.bmp','.webp','.svg','.tif','.tiff','.avif'}
sha=lambda b:hashlib.sha256(b).hexdigest()
current_roots=[]
for roman in ['I','II','III']:
 p=D/f'S6_09_PAPERS_{roman}.pdf'
 current_roots.append(f'validation/{roman}_{sha(p.read_bytes())[:12]}/')
def priority(path):
 return (0 if path.startswith('code/') else 1 if any(path.startswith(p)for p in current_roots) else 2 if 'final_visual_review' in path else 3,path)
checkpoint_groups=defaultdict(list); fs_groups=defaultdict(list); records=[]
with zipfile.ZipFile(Z)as z:
 infos=z.infolist(); info_by={i.filename:i for i in infos}; image_infos=[i for i in infos if Path(i.filename).suffix.lower() in EXT]
 for i in image_infos:
  b=z.read(i); h=sha(b)
  checkpoint_groups[(len(b),h)].append({'path':i.filename,'bytes':i.file_size,'compressed_bytes':i.compress_size,'sha256':h,'crc32':f'{i.CRC:08x}','filename_bytes':len(i.filename.encode('utf-8')),'zip_extra_bytes':len(i.extra),'zip_comment_bytes':len(i.comment)})
 removed=[]; kept=[]; duplicate_groups=[]
 for (n,h),rows in sorted(checkpoint_groups.items()):
  rows.sort(key=lambda r:priority(r['path'])); first=rows[0]; ref=z.read(first['path'])
  for r in rows[1:]:assert z.read(r['path'])==ref,(first['path'],r['path'])
  kept.append(first)
  if len(rows)>1:duplicate_groups.append({'sha256':h,'bytes':n,'kept_path':first['path'],'alias_count':len(rows)-1,'members':rows,'all_members_compared_byte_for_byte':True})
  for r in rows:
   rec={**r,'kept_path':first['path'],'is_alias':r['path']!=first['path'],'exact_byte_comparison_to_representative':True}
   records.append(rec)
   if rec['is_alias']:removed.append(rec)
 png=[r for r in records if Path(r['path']).suffix.lower()=='.png']
 nonimages=[i for i in infos if Path(i.filename).suffix.lower()not in EXT]
 aliases=[{'path':r['path'],'stored_path':r['kept_path'],'bytes':r['bytes'],'sha256':r['sha256']}for r in removed]
 manifest={'format':'exact-image-aliases-v1','source_archive':Z.name,'source_archive_sha256':sha(Z.read_bytes()),'scope':'Original uncompressed member bytes and original relative paths are all recoverable. This does not itself reproduce the original ZIP container byte stream.','restoration':'For every alias, verify the stored_path length and SHA-256, then copy its exact bytes to path; reject an existing differing target. Never decode or recompress image pixels.','kept_image_count':len(kept),'alias_count':len(aliases),'aliases':aliases}
 manifest_bytes=(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n').encode()
 (OUT/'checkpoint06_image_alias_manifest.json').write_bytes(manifest_bytes)
 c=zlib.compressobj(6,zlib.DEFLATED,-15); manifest_compressed=len(c.compress(manifest_bytes)+c.flush())
 threshold=536870912
 conservative=Z.stat().st_size-sum(r['compressed_bytes']for r in removed)+manifest_compressed+65536
 exact_same_metadata_estimate=Z.stat().st_size-sum(r['compressed_bytes']+76+2*r['filename_bytes']+2*r['zip_extra_bytes']+r['zip_comment_bytes']for r in removed)+manifest_compressed+76+2*len('records/image_aliases.json')
 summary={'created_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_archive':str(Z),'source_archive_sha256':manifest['source_archive_sha256'],'archive_bytes':Z.stat().st_size,'archive_entries':len(infos),'library_limit_bytes':threshold,'image_extensions':sorted(EXT),'current_validation_roots_preferred_as_representatives':current_roots,'checkpoint_image_files':len(records),'checkpoint_image_uncompressed_bytes':sum(r['bytes']for r in records),'checkpoint_image_compressed_bytes':sum(r['compressed_bytes']for r in records),'unique_image_files':len(kept),'unique_image_uncompressed_bytes':sum(r['bytes']for r in kept),'unique_image_compressed_bytes':sum(r['compressed_bytes']for r in kept),'duplicate_image_groups':len(duplicate_groups),'duplicate_image_alias_paths':len(removed),'removed_alias_uncompressed_bytes':sum(r['bytes']for r in removed),'removed_alias_compressed_bytes':sum(r['compressed_bytes']for r in removed),'nonimage_files_all_retained':len(nonimages),'nonimage_compressed_bytes':sum(i.compress_size for i in nonimages),'image_alias_manifest_uncompressed_bytes':len(manifest_bytes),'image_alias_manifest_raw_deflate6_bytes':manifest_compressed,'conservative_archive_bytes_if_existing_compressed_streams_retained_plus_64KiB_tools_allowance':conservative,'conservative_headroom_below_limit':threshold-conservative,'same_metadata_zip_size_estimate_plus_manifest_no_restoration_tool':exact_same_metadata_estimate,'deduplication_rule':'SHA-256 and length identify candidates; each duplicate payload was then explicitly compared byte-for-byte with its representative.','format_recommendation':'Standard DEFLATE ZIP: preserve every nonimage member at its original path, preserve one original-path image per exact byte group, include alias JSON and a safe Python restoration script. Keep current validation images and code images preferentially. No symlink or filesystem hardlink dependency.','byte_preservation_scope':'Every original archive member payload can be reconstructed at its original relative path. The original checkpoint06 ZIP stays immutable and separate.','png_files':len(png),'png_duplicate_alias_paths':sum(r['is_alias']for r in png),'groups_by_original_top_directory':dict(Counter(r['path'].split('/')[0]for r in records)),'alias_paths_by_original_top_directory':dict(Counter(r['path'].split('/')[0]for r in removed)),'largest_duplicate_groups':sorted([{'sha256':g['sha256'],'kept_path':g['kept_path'],'count':len(g['members']),'bytes_each':g['bytes'],'compressed_bytes_removed':sum(r['compressed_bytes']for r in g['members'][1:]),'alias_paths':[r['path']for r in g['members'][1:]]}for g in duplicate_groups],key=lambda r:r['compressed_bytes_removed'],reverse=True)[:20]}
 # No directory mutation: compare present filesystem images with archived members.
 names=subprocess.run(['rg','--files',str(D)],check=True,capture_output=True,text=True).stdout.splitlines()
 fs_images=[Path(p)for p in names if Path(p).suffix.lower()in EXT]
 fs_differences=[]
 for p in fs_images:
  rel=p.relative_to(D).as_posix();b=p.read_bytes();h=sha(b);fs_groups[(len(b),h)].append(rel)
  if rel in info_by:
   if rel in {r['path']for r in records}:
    saved=next(r for r in records if r['path']==rel)
    if saved['sha256']!=h:fs_differences.append({'path':rel,'status':'different_bytes_from_checkpoint'})
  else:fs_differences.append({'path':rel,'status':'not_in_checkpoint'})
 summary['current_deliverables_image_files']=len(fs_images)
 summary['current_deliverables_unique_image_files']=len(fs_groups)
 summary['current_deliverables_duplicate_image_alias_paths']=sum(len(v)-1 for v in fs_groups.values())
 summary['current_deliverables_duplicate_image_bytes']=sum(n*(len(paths)-1)for(n,h),paths in fs_groups.items())
 summary['current_image_changes_relative_to_checkpoint']=fs_differences
 summary['deliverables_mutated']=False;summary['checkpoint_mutated']=False
 (OUT/'image_duplicate_audit_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
 (OUT/'checkpoint06_image_duplicate_groups.json').write_text(json.dumps(duplicate_groups,ensure_ascii=False,indent=2)+'\n')
 (OUT/'current_deliverables_image_duplicate_groups.json').write_text(json.dumps([{'bytes':n,'sha256':h,'paths':sorted(paths)}for(n,h),paths in fs_groups.items()if len(paths)>1],ensure_ascii=False,indent=2)+'\n')
 with(OUT/'checkpoint06_image_path_map.csv').open('w',newline='')as f:
  w=csv.DictWriter(f,fieldnames=['path','kept_path','bytes','sha256','compressed_bytes','is_alias']);w.writeheader();w.writerows({k:r[k]for k in w.fieldnames}for r in sorted(records,key=lambda r:r['path']))
 print(json.dumps({k:v for k,v in summary.items()if k!='largest_duplicate_groups'},indent=2))
