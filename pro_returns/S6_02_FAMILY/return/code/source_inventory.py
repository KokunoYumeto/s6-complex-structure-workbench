"""Verify the user-supplied archive manifest and record source identities.

Usage: python3 code/source_inventory.py /path/to/extracted/background
The source archive is intentionally not duplicated in the deliverable.
"""
from pathlib import Path
import csv, hashlib, json, subprocess, sys

ROOT=Path(__file__).resolve().parents[1]
SOURCE=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else ROOT.parent/'background'
records=[]
with (SOURCE/'MANIFEST.tsv').open(encoding='utf-8') as f:
    for row in csv.DictReader(f,delimiter='\t'):
        p=SOURCE/row['path_in_zip']
        data=p.read_bytes()
        digest=hashlib.sha256(data).hexdigest()
        assert len(data)==int(row['bytes']),str(p)
        assert digest==row['sha256'],str(p)
        record={'path':row['path_in_zip'],'bytes':len(data),'sha256':digest}
        if p.suffix.lower()=='.pdf':
            info=subprocess.run(['pdfinfo',str(p)],text=True,capture_output=True,check=True).stdout
            record['pages']=int(next(s.split(':',1)[1] for s in info.splitlines() if s.startswith('Pages:')))
        records.append(record)
        print('MATCH',record['path'],record['bytes'],record.get('pages',''))
out={'manifest_verified':True,'source_files':records,
     'scope':'File identity verification; substantive reading locations are separately recorded in the report.'}
(ROOT/'evidence/source_manifest_verified.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print('TOTAL_FILES',len(records))
print('PDF_FILES',sum('pages' in r for r in records))
print('TOTAL_PDF_PAGES',sum(r.get('pages',0) for r in records))

