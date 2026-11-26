"""Hold the actual containing unit for the newly read02KD role cases."""
from pathlib import Path
from datetime import datetime,timezone
import csv
ROOT=Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
path=ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv'
with path.open(newline='') as f:
    reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
row,=[r for r in rows if r['paper']=='III' and r['unit_id']=='maps:src:D.1.1' and r['defect_type']=='D20']
assert row['status']=='done'
row.update(status='open',date_utc=datetime.now(timezone.utc).isoformat(),
    evidence=row['evidence']+'; agents/continuation9_root/S6_SERIES_PUBLISH_c9_02KD_current_roles.md',
    detail=row['detail']+' Root reread the complete current formal02KD/maps:src:D.1.4 statement/proof. Formal coefficient arguments are retained with their actual binders; concrete q(base/circle), C(homology/period matrix), C2(cohomology/trace map), and resolution a,b roles require exact source repair and downstream-import comparison. The named reader owns that bounded packet. Required mathematical conclusions and raw check scopes are unchanged.')
with path.open('w',newline='') as f:
    writer=csv.DictWriter(f,fields,delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(rows)
print('Reopened existing maps:src:D.1.1 D20 for the complete actual02KD source readback; no new unit or event was created.')
