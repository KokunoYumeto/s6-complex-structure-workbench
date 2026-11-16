"""Package the final manuscript and audit records; omit supplied inputs and build debris."""
from pathlib import Path
import csv, hashlib, json, zipfile

ROOT=Path(__file__).resolve().parents[3]
D=ROOT/'deliverables'
required=['S6_07_PAPER_paper.tex','S6_07_PAPER_paper.pdf','S6_07_PAPER_source_table.csv',
          'S6_07_PAPER_notation_sheet.md','S6_07_PAPER_references.bib','S6_07_PAPER_report.md']
for name in required:
    if not (D/name).is_file():raise FileNotFoundError(name)
selected=[D/name for name in required]
excluded=[]
for p in sorted((D/'records').rglob('*')):
    if not p.is_file():continue
    rel=p.relative_to(D)
    if any(s in rel.parts for s in ['__pycache__','tex-cache','qa','work']):
        excluded.append((str(rel),'reproducible isolated build/cache; superseded by final master and retained QA records'))
    elif p.name.startswith('fragment_check.') and p.suffix != '.log':
        excluded.append((str(rel),'isolated preview/wrapper; superseded by S6_07_PAPER_paper.tex and PDF'))
    elif p.suffix in ['.aux','.out','.pyc','.luc','.gz']:
        excluded.append((str(rel),'transient build artifact'))
    else:selected.append(p)
exclusions=D/'records/package_exclusions.json'
exclusions.write_text(json.dumps({'excluded_files':[{'path':a,'reason':b} for a,b in excluded],
    'not_materialized_into_deliverable':['the supplied attachment archives and extracted source files','temporary reading extraction of the supplied Duke–Imamoglu PDF','upstream runtime package archives and font caches','full-resolution reproducible page PNGs; overview sheets and rendering script retained']},indent=2))
if exclusions not in selected:selected.append(exclusions)
manifest=D/'S6_07_PAPER_manifest.csv'
with manifest.open('w',newline='') as f:
    w=csv.writer(f);w.writerow(['path','bytes','sha256'])
    for p in sorted(selected):w.writerow([str(p.relative_to(D)),p.stat().st_size,hashlib.sha256(p.read_bytes()).hexdigest()])
selected.append(manifest)
target=ROOT/'S6_07_PAPER.zip'
with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in sorted(selected):z.write(p,p.relative_to(D))
with zipfile.ZipFile(target) as z:
    assert z.testzip() is None
    assert [x for x in z.namelist() if x.endswith('.pdf')]==['S6_07_PAPER_paper.pdf']
print(json.dumps({'zip':str(target),'files':len(selected),'bytes':target.stat().st_size,
                  'sha256':hashlib.sha256(target.read_bytes()).hexdigest()},indent=2))
