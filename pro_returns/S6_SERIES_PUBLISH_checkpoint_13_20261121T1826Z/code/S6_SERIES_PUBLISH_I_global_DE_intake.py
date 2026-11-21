from pathlib import Path
import json,hashlib,datetime
from S6_SERIES_PUBLISH_editing import block
r=Path(__file__).resolve().parents[1];p=r/'S6_SERIES_PUBLISH_I.tex';s=p.read_text()
ids=['series:I:D','series:I:E','inv:C3.8','inv:A2.2','inv:A3.1','inv:C1.1','inv:C2.1','inv:C3.3','inv:A4.1','inv:A4.2','inv:A2.4','inv:A1.0','inv:D4.1','inv:D4.2','inv:D4.3','inv:D4.4','inv:D4.5','fam:src:A.5.2','fam:src:B.4.1','push:src:E.2.1','inv:C3.2','inv:C3.1','push:src:E.1.2']
d={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':hashlib.sha256(s.encode()).hexdigest(),
 'exposure':'Root has previously read historical frontmatter and many complete cited proofs during editorial work. This intake supports a final global consistency check, not a new blind independent reproof. Current outline steps have not been reopened in this final-check pass.',
 'statements':{lab:block(s,lab,False) for lab in ids}}
out=r/'records/S6_SERIES_PUBLISH_I_global_DE_intake.json';assert not out.exists();out.write_text(json.dumps(d,indent=2)+'\n')
print(json.dumps({'path':str(out),'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'statements':len(ids)}))
