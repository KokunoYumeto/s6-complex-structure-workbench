#!/usr/bin/env python3
"""Correct two audit-prose page ranges; all source guards stay unchanged."""
import datetime,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];AREA=ROOT/'agents/continuation_infra'
sha=lambda b:hashlib.sha256(b).hexdigest()
old=AREA/'S6_SERIES_PUBLISH_I_candidate17_bibliography_audit_matrix_final.json'
data=json.loads(old.read_text());changes=[]
for r in data['rows']:
    replace={'IKN2005E':('1–36 (2005)','1–66 (2005)'), 'KKN2008Root':('1–43 (2008)','69–193 (2008)')}.get(r['key'])
    if replace:
        assert replace[0] in r['publication_review']
        r['publication_review']=r['publication_review'].replace(*replace)
        p=AREA/'candidate17_bibliography_audit'/(r['key']+'_primary.download')
        changes.append({'key':r['key'],'old_audit_prose':replace[0],'correct_audit_prose':replace[1],'primary_pdf_path':str(p.relative_to(ROOT)),'primary_pdf_sha256':sha(p.read_bytes()),'scope':'Published page range printed on official PDF first-page header; source bibliography already correct.'})
assert len(changes)==2
data.update({'revision':3,'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'supersedes':{'path':str(old.relative_to(ROOT)),'sha256':sha(old.read_bytes())},'revision_scope':'Correct two audit-prose page ranges. All45 bibliography guards, original entries, proposed entries and canonical source remain unchanged.'})
new=AREA/'S6_SERIES_PUBLISH_I_candidate17_bibliography_audit_matrix_final_v3.json';assert not new.exists();new.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
oldmd=AREA/'S6_SERIES_PUBLISH_I_candidate17_bibliography_audit_matrix_final.md'
md=oldmd.read_text().replace('12(1), 1–36 (2005)','12(1), 1–66 (2005)').replace('15(1), 1–43 (2008)','15(1), 69–193 (2008)')
newmd=AREA/'S6_SERIES_PUBLISH_I_candidate17_bibliography_audit_matrix_final_v3.md';assert not newmd.exists();newmd.write_text(md)
guard=AREA/'S6_SERIES_PUBLISH_I_candidate17_bibliography_combined_guards_final.json'
receipt={'created_utc':data['created_utc'],'source_sha256':data['source_sha256'],'superseded_matrix':data['supersedes'],'matrix_path':str(new.relative_to(ROOT)),'matrix_sha256':sha(new.read_bytes()),'matrix_markdown_path':str(newmd.relative_to(ROOT)),'matrix_markdown_sha256':sha(newmd.read_bytes()),'unchanged_guard_path':str(guard.relative_to(ROOT)),'unchanged_guard_sha256':sha(guard.read_bytes()),'changes':changes,'mathematical_events_added':0,'full_page_reading_credit_added':0,'canonical_source_unchanged':sha((ROOT/'S6_SERIES_PUBLISH_I.tex').read_bytes())==data['source_sha256']}
p=AREA/'S6_SERIES_PUBLISH_I_candidate17_bibliography_matrix_v3_receipt.json';assert not p.exists();p.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'receipt':str(p.relative_to(ROOT)),'receipt_sha256':sha(p.read_bytes()),**receipt}))
