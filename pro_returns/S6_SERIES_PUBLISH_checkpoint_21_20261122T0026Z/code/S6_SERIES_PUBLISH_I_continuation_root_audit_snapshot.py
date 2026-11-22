#!/usr/bin/env python3
"""Preserved source of the root's inline candidate14 audit snapshot operation.

The original operation ran before the candidate15 edits. Replays validate the
saved outputs and do not attribute a new contextual or page reading.
"""
from pathlib import Path
import datetime
import hashlib
import json
import shutil

ROOT=Path(__file__).resolve().parents[1]


def main():
    for old,new in [
        ('records/S6_SERIES_PUBLISH_I_page_coverage.json','records/S6_SERIES_PUBLISH_I_candidate14_complete_coverage_snapshot.json'),
        ('records/S6_SERIES_PUBLISH_I_continuation_AG_binding.json','records/S6_SERIES_PUBLISH_I_continuation_candidate14_AG_binding.json')]:
        target=ROOT/new
        if not target.exists():
            shutil.copyfile(ROOT/old,target)
        value=json.loads(target.read_text())
        assert value['source_sha256']=='1f2d0d376f71e7843265976aeeb72cf8e1ff77aea176ff5dbb4e67446c25b36f'
    scan=ROOT/'records/S6_SERIES_PUBLISH_I_continuation_rendered_residue_scan.json'
    original=json.loads(scan.read_text())
    rows=[dict(index=i+1,**row) for i,row in enumerate(original['rows'])
          if row['type'] in {'D01','D02','D05','D11','D23'}]
    destination=ROOT/'records/S6_SERIES_PUBLISH_I_continuation_root_residue_dispositions.json'
    if not destination.exists():
        record={
            'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'scope':"Root actually read all D01 contexts and all D02/D05/D11/D23 contexts in the preserved candidate13 scan during this continuation, and the relevant current source arguments. The accompanying candidate14 exact edits remove the confirmed D02/D11/D23 instances. D05 occurrences cite mathematical requirements; D01 occurrences name original geometric data, original editions, published corrections, or the permitted methodology. Remaining positive-circuit wording at page59 has its explicit integral comparison. No automatic absence conclusion and no mathematical-check or full-page-reading credit is inferred from this contextual audit.",
            'scan_sha256':hashlib.sha256(scan.read_bytes()).hexdigest(),
            'source_after_first_round_sha256':'1f2d0d376f71e7843265976aeeb72cf8e1ff77aea176ff5dbb4e67446c25b36f',
            'rows_read':rows,
            'additional_replay_hit':{
                'page':325,'type':'D11','text':'its splitting is not asserted canonical.',
                'disposition':"Confirmed redundant assertion disclaimer. Root read the connecting-map/cokernel/extension argument and approved its exact deletion; Q=O(-1)|2p1 and Ext^1=0 and the existence of a splitting remain."},
            'mathematical_events_added':0}
        destination.write_text(json.dumps(record,indent=2)+'\n')
    saved=json.loads(destination.read_text())
    assert saved['rows_read']==rows
    assert saved['scan_sha256']==hashlib.sha256(scan.read_bytes()).hexdigest()
    print(json.dumps({'context_rows_recorded':len(rows),'candidate14_full_reading_snapshot_saved':True,
                      'scope':'Validate the saved actual-reading declaration; no new reading is performed by this program.'}))


if __name__=='__main__':
    main()
