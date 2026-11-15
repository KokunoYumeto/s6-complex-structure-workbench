#!/usr/bin/env python3
"""Preserve checkpoint provenance and package the final INCOMPLETE return."""
from pathlib import Path
import hashlib,json,zipfile,zlib,sys

root=Path(__file__).resolve().parents[1]
target=root.parent/'S6_05_ARITHMETIC_final.zip'
if target.exists():
    assert '--rebuild-undelivered' in sys.argv, 'Never overwrite a delivered archive.'
    assert not (root/'records/final_receipt.json').exists(), 'An uploaded final archive is immutable.'
    backup=target.with_name(target.stem+'_pre_preservation_fix.zip')
    assert not backup.exists(),backup
    target.rename(backup)
qa=json.loads((root/'records/pdf_qa_hour4.json').read_text())
assert qa['overfull_above_2pt']==0 and not qa['undefined_citations_or_references']
assert qa.get('visually_inspected_pages')==qa['rendered_pages']
exclusions={r['path']:r for r in json.loads((root/'records/checkpoint_omissions.json').read_text())}
keep_suffixes={'.tex','.md','.csv','.bib','.py','.gp','.sage','.cpp','.c','.h','.json','.out','.txt','.sh'}
manifest=[]
for cp in sorted(root.parent.glob('S6_05_ARITHMETIC_checkpoint_*.zip')):
    with zipfile.ZipFile(cp) as z:
        for info in z.infolist():
            if info.is_dir():continue
            rel=info.filename.removeprefix('S6_05_ARITHMETIC/')
            current=root/rel
            if current.exists() and rel not in exclusions:
                crc=0
                with current.open('rb') as f:
                    for block in iter(lambda:f.read(1048576),b''):crc=zlib.crc32(block,crc)
                if current.stat().st_size==info.file_size and crc==info.CRC:continue
            row={'checkpoint':cp.name,'path':rel,'prior_bytes':info.file_size}
            if rel in exclusions:
                row.update(disposition='omitted with explicit replacement or source link',reason=exclusions[rel]['reason'])
                if 'source_url' in exclusions[rel]:row['source_url']=exclusions[rel]['source_url']
            elif current.exists() and current.suffix.lower() not in keep_suffixes:
                row.update(disposition='superseded',replacement=rel,
                           reason='Earlier generated binary, cache or typesetting intermediate superseded by the current file at the same path; proof source versions are retained separately.')
            else:
                data=z.read(info)
                saved=root/'records/checkpoint_history'/cp.stem/rel
                saved.parent.mkdir(parents=True,exist_ok=True)
                saved.write_bytes(data)
                row.update(disposition='retained verbatim',historical_path=str(saved.relative_to(root)),
                           prior_sha256=hashlib.sha256(data).hexdigest())
            manifest.append(row)

manifest_path=root/'records/checkpoint_version_manifest.json'
manifest_path.write_text(json.dumps(manifest,indent=2)+'\n')
report=root/'S6_05_ARITHMETIC_report.md'
marker='\n## Final checkpoint preservation audit\n'
report.write_text(report.read_text().split(marker,1)[0])
with report.open('a') as f:
    f.write('\n## Final checkpoint preservation audit\n\n')
    f.write('Every earlier checkpoint was compared entry by entry with this final tree. ')
    f.write('Changed proof sources, programs, outputs, reports, registers and bibliography files ')
    f.write('are retained verbatim under records/checkpoint_history/, indexed in ')
    f.write('records/checkpoint_version_manifest.json. This preserves the superseded passages ')
    f.write('as well as the corrected current arguments. Earlier checkpoints themselves remain unchanged. ')
    f.write('The following earlier generated files or third-party copies are represented by the explicit replacement or source recorded here.\n\n')
    f.write('| Earlier checkpoint | File | Disposition and replacement |\n|---|---|---|\n')
    for r in manifest:
        if r['disposition']=='retained verbatim':continue
        detail=r['reason']
        if 'replacement' in r:detail+=' Replacement: `'+r['replacement']+'`.'
        if 'source_url' in r:detail+=' Source: '+r['source_url']+'.'
        f.write('| '+r['checkpoint']+' | `'+r['path']+'` | '+detail+' |\n')

inventory=[]
for p in sorted(root.rglob('*')):
    if not p.is_file():continue
    rel=str(p.relative_to(root))
    if rel in exclusions or rel=='records/final_inventory.json':continue
    with p.open('rb') as f:digest=hashlib.file_digest(f,'sha256').hexdigest()
    inventory.append({'path':rel,'bytes':p.stat().st_size,'sha256':digest})
(root/'records/final_inventory.json').write_text(json.dumps(inventory,indent=2)+'\n')
with zipfile.ZipFile(target,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6,allowZip64=True) as z:
    for p in sorted(root.rglob('*')):
        if p.is_file() and str(p.relative_to(root)) not in exclusions:
            z.write(p,'S6_05_ARITHMETIC/'+str(p.relative_to(root)))
with zipfile.ZipFile(target) as z:
    bad=z.testzip()
    assert bad is None,bad
    file_count=len(z.infolist())
    final_names=set(z.namelist())
    for cp in sorted(root.parent.glob('S6_05_ARITHMETIC_checkpoint_*.zip')):
        with zipfile.ZipFile(cp) as prior:
            for name in set(prior.namelist())-final_names:
                rel=name.removeprefix('S6_05_ARITHMETIC/')
                assert rel in exclusions and rel in report.read_text(), ('Unexplained checkpoint omission',cp.name,rel)
with target.open('rb') as f:digest=hashlib.file_digest(f,'sha256').hexdigest()
print(json.dumps({'file':str(target),'bytes':target.stat().st_size,'sha256':digest,
                  'files':file_count,'zip_crc_check':'PASS','checkpoint_omission_check':'PASS','checkpoint_versions':len(manifest)},indent=2))
