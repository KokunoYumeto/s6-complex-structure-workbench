"""Package the verified final deliverables with the saved-checkpoint file map.

This is the final ZIP, not an extra hourly checkpoint. It runs only after the
explicit completion decision, current canonical hashes and final log gates.
"""
from pathlib import Path
import csv
import hashlib
import io
import json
import re
import zipfile

from make_checkpoint import KEEP_PROBLEM_IMAGES

OUT=Path(__file__).resolve().parents[1]


def main():
    decision=json.loads((OUT/'analysis/final_completion_decision.json').read_text())
    assert decision['state']=='complete', 'The six-paper completion decision is still open.'
    assert (OUT/'S6_10_PAPERS_report.md').read_text().startswith('COMPLETE'), 'Final report is not complete.'
    snapshot=json.loads((OUT/'analysis/final_deliverable_snapshot.json').read_text())
    assert {r['paper'] for r in snapshot}=={'I','II','III','IV','V','VI'}
    for r in snapshot:
        for key in ['overfull_hbox_above_2pt','overfull_vbox_above_2pt',
                    'missing_characters','font_warnings','undefined_reference_messages',
                    'undefined_citation_messages','multiply_defined_labels']:
            assert r['log'][key]==0,(r['paper'],key,r['log'][key])
        for suffix in ['tex','pdf']:
            p=OUT/f"S6_10_PAPERS_{r['paper']}.{suffix}"
            assert hashlib.sha256(p.read_bytes()).hexdigest()==r[suffix+'_sha256'],p
    name='S6_10_PAPERS_final.zip'
    destination=OUT.parents[1]/'deliverables'
    destination.mkdir(exist_ok=True)
    archive=destination/name
    if archive.exists():raise SystemExit('Refusing to overwrite the final ZIP.')
    saved=json.loads((OUT/'analysis/checkpoint_saved_state.json').read_text())
    rows=[];payload={};excluded=[]
    for f in sorted(OUT.rglob('*')):
        if not f.is_file() or f.is_symlink():continue
        n=f.relative_to(OUT).as_posix()
        reason=None
        if '__pycache__' in f.parts or (f.suffix in ('.png','.jpg','.jpeg','.webp','.zip','.deb') and n not in KEEP_PROBLEM_IMAGES):
            reason='Rendered image, cache, external runtime package or archive; only the documented problem images are retained.'
        elif n.startswith(('build/arithmetic_runtime/root/','build/arithmetic_runtime/packages/',
                           'build/tex_runtime/packages/','build/tex_runtime/cache/')):
            reason='Reproducible external runtime files.'
        elif n.startswith('build/literature/') and f.name not in ('edition_record.json','build.stdout.txt'):
            reason='Compiled external literature; exact source and edition records are retained.'
        elif f.suffix=='.pdf' and not (f.name.startswith('S6_10_PAPERS_') or 'preview' in f.parts or f.name=='preview.pdf'):
            reason='External source PDF; exact locator, source identity and read scope remain in the records.'
        elif 'references_build' in f.parts and f.suffix in ('.tex','.out','.aux','.log'):
            reason='External literature build intermediate.'
        if reason:
            excluded.append({'path':n,'reason':reason});continue
        before=f.stat();data=f.read_bytes();after=f.stat()
        if before.st_size!=after.st_size or before.st_mtime_ns!=after.st_mtime_ns or len(data)!=after.st_size:
            raise RuntimeError('Source changed during the final freeze: '+n)
        digest=hashlib.sha256(data).hexdigest()
        mandatory=n.startswith(('S6_10_PAPERS_','papers/','records/','code/')) or n in ('CHECK_EVENTS.tsv','PROGRESS_LEDGER.md','preamble.tex')
        prior=saved.get('files',{}).get(n,{})
        include=mandatory or prior.get('sha256')!=digest
        holder=name if include else prior['checkpoint']
        rows.append({'path':n,'size_bytes':len(data),'sha256':digest,
                     'included':str(include).lower(),'checkpoint':holder})
        if include:payload[n]=data
    filelist=io.StringIO()
    writer=csv.DictWriter(filelist,['path','size_bytes','sha256','included','checkpoint'],delimiter='\t')
    writer.writeheader();writer.writerows(rows)
    payload['FINAL_FILES.tsv']=filelist.getvalue().encode()
    payload['FINAL_EXCLUSIONS.json']=(json.dumps(excluded,indent=2)+'\n').encode()
    payload['README_FINAL.txt']=(
        'S6_10_PAPERS — final six-paper package\n\n'
        'All six current standalone TeX files and PDFs, the inventory, notation sheet, bibliography, report, '
        'check-event ledger, progress ledger, receiving fragments, programs and outputs are included. '
        'The main report gives the final proof scopes and the explicitly open mathematical questions.\n\n'
        'Each top-level TeX file contains its bibliography and resolved cross-paper theorem numbers. '
        'Compile with LuaLaTeX, repeating until its local labels are stable. The supplied PDF is the verified final rendering.\n\n'
        'FINAL_FILES.tsv records every retained project file. An unchanged auxiliary file omitted here names '
        'the previously saved checkpoint that holds it. No prior ZIP is nested in this ZIP. '
        'FINAL_EXCLUSIONS.json explains omitted runtime/source/rendering intermediates.\n\n'
        'The supplied S6_09_PAPERS compendium remains byte-for-byte unchanged; its fresh integrity comparison '
        'is analysis/final_compendium_integrity.json. Its eight original files remain in the attached '
        'S6_10_PAPERS_1_s6_09(1).zip, as required by the instruction to omit supplied archives and sources.\n\n'
        'The night-run intake reaches checkpoint30. The exact main and companion source hashes, '
        'current mathematical reviews and source-change guards are retained in the inventory and analysis records. '
        'The final account-search scope is recorded separately; bounded Space results are not exhaustive.\n\n'
        'The papers are AI-produced. No human has checked their mathematics. The text is dedicated under CC0 1.0.\n'
    ).encode()
    with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for n,data in payload.items():z.writestr('S6_10_PAPERS/'+n,data)
    size=archive.stat().st_size
    if size>=500_000_000:raise RuntimeError('Final archive exceeds 500 MB; split before upload.')
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        for roman in ['I','II','III','IV','V','VI']:
            for suffix in ['tex','pdf']:
                n=f'S6_10_PAPERS/S6_10_PAPERS_{roman}.{suffix}'
                assert z.read(n)==(OUT/n.split('/',1)[1]).read_bytes()
    result={'archive':str(archive),'size_bytes':size,'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),
            'included_files':len(payload),'unchanged_auxiliary_files':sum(r['included']=='false' for r in rows),
            'excluded_intermediates':len(excluded),'zip_crc_check':'passed','canonical_payload_identity':'all twelve passed'}
    (OUT/'analysis/final_archive_record.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
