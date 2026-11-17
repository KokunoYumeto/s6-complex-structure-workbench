from pathlib import Path
import zipfile,json,io,copy,hashlib,datetime
ROOT=Path.cwd(); OUT=ROOT/'delivery_compression_audit'
manifest_path=OUT/'checkpoint06_image_alias_manifest.json'
manifest=json.loads(manifest_path.read_text()); omitted={r['path']for r in manifest['aliases']}
assert len(omitted)==1015
assert not any(r['stored_path']in omitted for r in manifest['aliases'])
class CountingSeekable(io.RawIOBase):
 def __init__(self):self.pos=0;self.extent=0
 def writable(self):return True
 def seekable(self):return True
 def tell(self):return self.pos
 def seek(self,offset,whence=0):
  self.pos=offset if whence==0 else self.pos+offset if whence==1 else self.extent+offset
  if self.pos<0:raise ValueError('negative position')
  return self.pos
 def write(self,data):self.pos+=len(data);self.extent=max(self.extent,self.pos);return len(data)
 def flush(self):pass
sink=CountingSeekable(); kept_count=0
with zipfile.ZipFile(ROOT/'S6_09_PAPERS_checkpoint_06.zip')as src,zipfile.ZipFile(sink,'w',zipfile.ZIP_DEFLATED,compresslevel=6)as dst:
 for info in src.infolist():
  if info.filename in omitted:continue
  dst.writestr(copy.copy(info),src.read(info),compress_type=zipfile.ZIP_DEFLATED,compresslevel=6);kept_count+=1
 dst.writestr('records/image_aliases.json',manifest_path.read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=6)
record={'timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_archive_sha256':manifest['source_archive_sha256'],'method':'Every retained member was actually read and recompressed with ordinary ZIP DEFLATE level 6 into a seekable counting sink. This is an exact output length calculation, not a claim that a delivery ZIP was created. Original ZipInfo metadata was copied; aliases were omitted and one exact manifest entry was added.','retained_original_members':kept_count,'added_manifest_members':1,'standard_zip_bytes_with_manifest_no_restoration_script':sink.extent,'headroom_below_536870912':536870912-sink.extent,'image_aliases':1015,'original_payload_paths_recoverable':kept_count+1015,'alias_manifest_sha256':hashlib.sha256(manifest_path.read_bytes()).hexdigest(),'no_alias_points_to_an_omitted_alias':True,'all_code_and_nonimage_paths_retained':True,'archive_or_deliverables_mutated':False}
(OUT/'standard_zip_exact_size_dry_run.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
