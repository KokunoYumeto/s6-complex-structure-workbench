#!/usr/bin/env python3
"""Record the bounded source scan that prompted complete-context review."""
from pathlib import Path
import hashlib,json,re
R=Path(__file__).resolve().parents[1]
p=R/'agents/i_cont_provenance/candidate19_review_blocks/S6_SERIES_PUBLISH_I_candidate19_source_snapshot.tex'
s=p.read_text();assert hashlib.sha256(p.read_bytes()).hexdigest()=='f9e40fb592eb7f5c6d48070ba207e93d5b48ca71432176202041b88dd01278f7'
pat=r'(?:This|this) (?:also )?proves (?:the (?:last |remaining |first |second )?assertion|every|all|the asserted strict inequality|nonextension\.)'
rx=re.compile(pat);lines=s.splitlines();hits=[]
for i,line in enumerate(lines):
 if rx.search(line):hits.append({'source_line':i+1,'context':'\n'.join(lines[max(0,i-4):i+5])})
assert [h['source_line'] for h in hits]==[10609,14253,22979,24466,26744,29020,29883]
record={'source':str(p.relative_to(R)),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'pattern':pat,'contexts':hits,'scope':'Seven contextual candidates from one bounded vague-ending scan. Each was read in its full owning statement/proof by the assigned reader. Six exact deletions and the retained A_t inference were resolved in the bound manual records. The page66 F.3.2 finding arose from actual whole-page reading and is separate. This scan is a locator and supplies no proof-reading credit or general absence conclusion.','deletions_bound_by':'records/S6_SERIES_PUBLISH_I_candidate19_root_approved_inputs.json','retained_context':'agents/continuation_infra/S6_SERIES_PUBLISH_I_candidate19_ariC61_recap_disposition.json','mathematical_events_added':0}
out=R/'records/S6_SERIES_PUBLISH_I_candidate19_recap_scan.json';assert not out.exists();out.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps({'record':str(out.relative_to(R)),'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'contexts':len(hits),'dispositions':{'deleted':6,'retained':1}},indent=2))
