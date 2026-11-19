"""Create the requested 45-minute incremental archive, under 500 MB.

Only run at a scheduled 45-minute boundary. Save receipt is recorded separately after
the write succeeds. Supplied material and external runtimes remain outside.
"""
from pathlib import Path
import argparse,csv,hashlib,io,json,time,zipfile
OUT=Path(__file__).resolve().parents[1]
KEEP_PROBLEM_IMAGES={'analysis/continuation_root/visual/V_p0065_interval_before.png',
 'analysis/continuation_root/visual/V_p0032_overflow_before.png',
 'analysis/continuation_root/visual/V_p0036_overflow_before.png',
 'analysis/continuation_root/visual/IV_p0996_transport_display_before.png',
 'analysis/continuation_root/visual/IV_p1169_heading_before.png',
 'analysis/I_sources/source_page_checks/SS00_014.png',
 'analysis/standalone_visual_checkpoint04/III_rung_before.png',
 'analysis/standalone_visual_checkpoint04/IV_title_before.png',
 'analysis/standalone_visual_checkpoint04/V_title_before.png',
 'analysis/sign_opening_II_page3.png',
 'analysis/final_root_visual/I_p0096.png',
 'analysis/final_root_visual/I_p0097.png'}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('number',type=int);args=ap.parse_args()
 name=f'S6_10_PAPERS_checkpoint_{args.number:02d}.zip'
 dest=OUT.parents[1]/'checkpoints';dest.mkdir(exist_ok=True)
 archive=dest/name
 if archive.exists():raise SystemExit('Refusing to overwrite an existing checkpoint')
 statepath=OUT/'analysis/checkpoint_saved_state.json'
 old=json.loads(statepath.read_text()) if statepath.exists() else {'files':{}}
 rows=[];payload={};excluded=[]
 for f in sorted(OUT.rglob('*')):
  if not f.is_file() or f.is_symlink():continue
  n=f.relative_to(OUT).as_posix()
  reason=None
  if n in {'CHECKPOINT_FILES.tsv','CHECKPOINT_EXCLUSIONS.json','CHECKPOINT_README.txt','analysis/checkpoint_pending_state.json'}:reason='checkpoint control file regenerated after the payload snapshot; manifest does not hash itself'
  elif '__pycache__' in f.parts or (f.suffix in ('.png','.jpg','.jpeg','.webp','.zip','.deb') and n not in KEEP_PROBLEM_IMAGES):reason='rendered image, cache, external package or archive'
  elif n.startswith(('build/arithmetic_runtime/root/','build/arithmetic_runtime/packages/','build/tex_runtime/packages/','build/tex_runtime/cache/')):reason='reproducible external runtime files'
  elif n.startswith('build/continuation_numeric/'):reason='reproducible installed numerical dependencies; version and file hashes retained in the numeric runtime receipt'
  elif n.startswith('build/literature/') and f.name not in ('edition_record.json','build.stdout.txt'):reason='compiled external literature; source supplied separately'
  elif f.suffix=='.pdf' and not (f.name.startswith('S6_10_PAPERS_') or 'preview' in f.parts or f.name=='preview.pdf'):reason='external literature PDF'
  elif 'references_build' in f.parts and f.suffix in ('.tex','.out','.aux','.log'):reason='external literature build intermediate'
  if reason:excluded.append({'path':n,'reason':reason});continue
  # Stable read protects against a simultaneous writer replacing a fragment.
  for attempt in range(5):
   before=f.stat();data=f.read_bytes();after=f.stat()
   if before.st_size==after.st_size==len(data) and before.st_mtime_ns==after.st_mtime_ns:break
  else:raise RuntimeError('File kept changing during checkpoint: '+n)
  digest=hashlib.sha256(data).hexdigest()
  mandatory=n.startswith(('S6_10_PAPERS_','papers/','records/','code/')) or n in ('CHECK_EVENTS.tsv','PROGRESS_LEDGER.md','preamble.tex')
  prior=old.get('files',{}).get(n,{})
  include=mandatory or prior.get('sha256')!=digest
  holder=name if include else prior['checkpoint']
  rows.append({'path':n,'size_bytes':len(data),'sha256':digest,'included':str(include).lower(),'checkpoint':holder})
  if include:payload[n]=data
 filelist=io.StringIO();writer=csv.DictWriter(filelist,['path','size_bytes','sha256','included','checkpoint'],delimiter='\t');writer.writeheader();writer.writerows(rows)
 payload['CHECKPOINT_FILES.tsv']=filelist.getvalue().encode()
 payload['CHECKPOINT_EXCLUSIONS.json']=json.dumps(excluded,indent=2).encode()
 payload['CHECKPOINT_README.txt']=(name+'\nINCOMPLETE: active writing and proof review.\nThe full current deliverable sources, draft PDFs available at this boundary, inventories, event records, code and documentation are included.\nThe unchanged supplied compendium and source archives are already attached to the conversation.\nSource assembly and preview compilation confer no mathematical check.\n').encode()
 with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
  for n,data in payload.items():z.writestr('S6_10_PAPERS/'+n,data)
 size=archive.stat().st_size
 if size>=500_000_000:raise RuntimeError('Archive exceeds 500 MB; split before upload')
 pending={'checkpoint':name,'archive':str(archive),'size_bytes':size,'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'files':{r['path']:{'sha256':r['sha256'],'checkpoint':r['checkpoint']} for r in rows}}
 (OUT/'analysis/checkpoint_pending_state.json').write_text(json.dumps(pending,indent=2))
 print(json.dumps({k:v for k,v in pending.items() if k!='files'},indent=2))
 print('included',len(payload),'unchanged omitted',sum(r['included']=='false' for r in rows),'excluded external/intermediate',len(excluded))
if __name__=='__main__':main()
