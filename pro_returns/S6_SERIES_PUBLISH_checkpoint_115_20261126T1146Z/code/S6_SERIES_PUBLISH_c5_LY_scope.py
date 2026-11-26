"""Record the actual LY exposure and transfer fresh-check ownership."""
from pathlib import Path
import csv

ROOT=Path(__file__).resolve().parents[1]
path=ROOT/'S6_SERIES_PUBLISH_required_progress_III.tsv'
with path.open(newline='') as f:
    reader=csv.DictReader(f,delimiter='\t')
    fields=reader.fieldnames
    rows=list(reader)
original=[dict(r) for r in rows]
row=next(r for r in rows if r['tag']=='02LY')
assert row['status']=='open' and row['proof_status']=='embargoed'
note=('2026-11-23 continuation5: D.2 checker encountered a labelled D.2.8 '
      'auxiliary computation block in the 149-line historical LX program '
      'before any complete LY fresh derivation. Root separately read Wang v2 '
      'Appendix B lines 1618–1678 while bounding general classification inputs. '
      'Neither checker may claim fresh independence for the exposed LY steps. '
      'Strict LY fresh ownership transferred to the unexposed finite-family checker; '
      'only the statement, established LX fresh inputs, and bounded general '
      'classification sources may be used before individual release.')
assert note not in row['checker_exposure_note']
row['checker_exposure_note']=(row['checker_exposure_note']+' '+note).strip()
row['assigned_checker']='continuation5_finite'
for before,after in zip(original,rows):
    if before['tag']!='02LY':assert before==after
with path.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n')
    w.writeheader();w.writerows(rows)
print('Recorded actual LY source/program exposure; transferred strict fresh ownership to the unexposed finite checker.')
print('LY stays open and proof-embargoed; every other required row is unchanged.')
