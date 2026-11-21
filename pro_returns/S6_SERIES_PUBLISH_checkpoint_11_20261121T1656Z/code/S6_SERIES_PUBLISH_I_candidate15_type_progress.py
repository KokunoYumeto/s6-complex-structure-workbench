#!/usr/bin/env python3
"""Record individually reviewed defect types under continuation rule0.3.

Root read all25 dossier dispositions and the complete candidate15 reading
record. Six types have identified pending guards; the other19 close at this
exact source snapshot. This supplies no mathematical event or reading credit.
"""
from pathlib import Path
import datetime
import hashlib
import json
import re
import shutil

ROOT=Path(__file__).resolve().parents[1]
SHA=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    source=ROOT/'S6_SERIES_PUBLISH_I.tex'
    expected='45bf46fc14a50f7a148cdd34bf2be68b04cd89e1cb7d620191c6e8518f7249f8'
    assert SHA(source)==expected
    dossier_live=ROOT/'agents/i_cont_edits/S6_SERIES_PUBLISH_I_cont_defect_type_closure_preparation.json'
    dossier_path=ROOT/'records/S6_SERIES_PUBLISH_I_candidate15_type_dossier_snapshot.json'
    if not dossier_path.exists():
        shutil.copyfile(dossier_live,dossier_path)
    dossier=json.loads(dossier_path.read_text())
    coverage_path=ROOT/'records/S6_SERIES_PUBLISH_I_candidate15_complete_coverage_snapshot.json'
    coverage=json.loads(coverage_path.read_text())
    assert coverage['source_sha256']==expected and coverage['all_pages_read']
    assert coverage['covered_pages']==coverage['page_count']==345
    pending={'D01','D02','D11','D16','D18','D23'}
    closed=[]
    for row in dossier['rows']:
        if row['type_id'] in pending:
            continue
        assert row['source_clear_in_recorded_review_scope'] and not row['remaining_content_issues']
        closed.append(row['type_id'])
    assert len(closed)==19
    path=ROOT/'records/S6_SERIES_PUBLISH_I_candidate15_type_progress.json'
    now=datetime.datetime.now(datetime.timezone.utc).isoformat()
    if path.exists():
        prior=json.loads(path.read_text())
        assert prior['source_sha256']==expected and prior['types_closed']==closed
        if prior['dossier_path']!=str(dossier_path.relative_to(ROOT)):
            original=ROOT/'records/S6_SERIES_PUBLISH_I_candidate15_type_progress_initial_binding.json'
            assert not original.exists()
            shutil.copyfile(path,original)
            prior['initial_binding_record']=str(original.relative_to(ROOT))
            prior['initial_binding_record_sha256']=SHA(original)
            prior['dossier_path']=str(dossier_path.relative_to(ROOT))
            prior['dossier_sha256']=SHA(dossier_path)
            prior['rebound_utc']=now
            prior['binding_update_scope']='The live preparation was concurrently updated to name the six open types. Root reread all nineteen closed-type dispositions in the frozen updated dossier; their source-review scope and absence of remaining content issues are unchanged. The initial binding is preserved; the operative evidence now uses this immutable snapshot.'
            path.write_text(json.dumps(prior,indent=2)+'\n')
        print(json.dumps({'archival_binding_verified':True,'types_closed':closed,'dossier_sha256':SHA(dossier_path)}))
        return
    record={'recorded_utc':now,'paper':'I','source_sha256':expected,
            'pdf_sha256':coverage['pdf_sha256'],
            'defect_log_sha256':SHA(ROOT/'S6_SERIES_PUBLISH_defects_I.tsv'),
            'dossier_path':str(dossier_path.relative_to(ROOT)),'dossier_sha256':SHA(dossier_path),
            'coverage_path':str(coverage_path.relative_to(ROOT)),'coverage_sha256':SHA(coverage_path),
            'types_closed':closed,'types_open':sorted(pending),
            'root_review':'Root read every per-type disposition. Complete candidate15 page reading supplies the further contextual review. The pending content findings lie in the six explicitly open types. The nineteen closed types retain the exact source comparisons, recorded edits and positive contextual evidence in the dossier.',
            'scope':'Individual current-source defect rows under continuation rule0.3. Paper I remains incomplete while the six pending types are repaired and the changed images read.',
            'mathematical_events_added':0}
    path.write_text(json.dumps(record,indent=2)+'\n')
    ledger=ROOT/'PROGRESS_LEDGER.md'; text=ledger.read_text()
    for code in closed:
        pattern=rf'^(\| I \| {code}: .*? \|) open \|$'
        text,count=re.subn(pattern,rf'\1 done; individually reviewed at candidate15 source45bf46fc, exact evidence in records/S6_SERIES_PUBLISH_I_candidate15_type_progress.json |',text,flags=re.M)
        assert count==1,code
    text+=f'\n## Paper I individual defect rows — {now}\n\nNineteen defect types are done at candidate15 source `{expected}` after their exact source audits, logged edits and complete page review. D01, D02, D11, D16, D18 and D23 remain open for the consolidated guards from that reading. All345 current candidate15 pages have actual full-image reading; the PDF remains uncertified because those known source edits are pending. Subsequent image changes reopen the corresponding page rows. Evidence: `records/S6_SERIES_PUBLISH_I_candidate15_type_progress.json`.\n'
    ledger.write_text(text)
    print(json.dumps({'types_closed':closed,'types_open':sorted(pending),'source_sha256':expected,'mathematical_events_added':0}))


if __name__=='__main__':
    main()
