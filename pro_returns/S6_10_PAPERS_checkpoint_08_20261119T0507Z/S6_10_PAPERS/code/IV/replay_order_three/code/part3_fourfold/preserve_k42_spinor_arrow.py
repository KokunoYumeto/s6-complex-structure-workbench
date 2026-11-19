from pathlib import Path
import datetime, hashlib, json, shutil
root=Path(__file__).resolve().parents[2]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
archive=root/'records/k42_pre_antilinear_arrow'
archive.mkdir(exist_ok=True)
items=[
 'notes/part3_source_cusp_characteristic_pair_working.md',
 'notes/part3_source_cusp_characteristic_pair.tex',
 'notes/part3_source_cusp_trace_working.md',
 'code/part3/source_cusp_characteristic_pair.py',
 'code/part3/source_cusp_characteristic_pair.json',
 'code/part3/source_cusp_characteristic_pair.out',
 'code/part3/source_cusp_characteristic_pair.err',
 'code/part3/export_source_cusp_characteristic_pair.py',
 'code/part3/source_cusp_characteristic_pair_results_mapping.json',
 'code/part3/k42_standalone.pdf',
 'records/k42_standalone_visual_qa.json',
]
manifest={}
for rel in items:
 p=root/rel
 target=archive/rel
 target.parent.mkdir(parents=True,exist_ok=True)
 if not target.exists(): shutil.copy2(p,target)
 manifest[rel]=hashlib.sha256(target.read_bytes()).hexdigest()
out={'utc':now,'purpose':'Preserve exact K42/F56 source, code, output and QA before any anti-linear spinor-arrow correction.',
 'active_files_modified':False,'sha256':manifest}
(archive/'manifest.json').write_text(json.dumps(out,indent=2)+'\n')
with (root/'records/literature_fourfold.md').open('a') as f:
 f.write(f'\n## {now} — K42/F56 anti-linear-arrow audit preservation\n\n')
 f.write('Opened the files listed in records/k42_pre_antilinear_arrow/manifest.json only to preserve and hash the exact pre-correction source, certificate, outputs and QA. Reason: parent requested an immutable local audit trail for the identified SP.9/10 coefficient-map issue. Material taken: byte-for-byte copies and SHA256 values; active files unchanged.\n')
print(json.dumps(out,indent=2))
