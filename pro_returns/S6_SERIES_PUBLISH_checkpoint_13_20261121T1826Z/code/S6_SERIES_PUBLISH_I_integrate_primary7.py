from pathlib import Path
import json,hashlib,datetime
from S6_SERIES_PUBLISH_editing import Editor
r=Path(__file__).resolve().parents[1];ed=Editor('I')
p=r/'agents/i_provenance/S6_SERIES_PUBLISH_I_primary_citation_guards_07.json'
for x in json.loads(p.read_text())['changes']:
 new=x['new'].replace(r'\emph{Verified at the cited loci}',r'\emph{Verified}')
 ed.replace(x['old'],new,'D16',x['reason'],x['id'])
bib=r/'S6_SERIES_PUBLISH_references.bib';before=bib.read_text();text=before
bp=r/'agents/i_provenance/S6_SERIES_PUBLISH_I_shared_bib_guards_07.json'
for x in json.loads(bp.read_text())['changes']:
 assert text.count(x['old'])==1,x['id'];text=text.replace(x['old'],x['new'])
ed.save();bib.write_text(text)
(r/'records/S6_SERIES_PUBLISH_I_primary7_integration.json').write_text(json.dumps({'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':hashlib.sha256(ed.text.encode()).hexdigest(),'shared_bib_before':hashlib.sha256(before.encode()).hexdigest(),'shared_bib_after':hashlib.sha256(text.encode()).hexdigest(),'guard_files':[str(p.relative_to(r)),str(bp.relative_to(r))],'variation':'Keep the original bare printed Verified marker until the analytic bibliography-wide cleanup removes it; retain the new Oda edition/pagination information as bibliographic content.','scope':'Primary title and edition pagination metadata only; no mathematical check event.'},indent=2)+'\n')
