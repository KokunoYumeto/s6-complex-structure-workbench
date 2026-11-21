#!/usr/bin/env python3
"""Version the reviewed bibliography batch with the resolved YZZ edition link."""
import datetime,hashlib,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
AREA=ROOT/'agents/continuation_infra';AUDIT=AREA/'candidate17_bibliography_audit'
sha=lambda b:hashlib.sha256(b if isinstance(b,bytes) else b.encode()).hexdigest()
def load(p):return json.loads(p.read_text())
def dump(p,x):
    assert not p.exists(),p
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
old=AREA/'S6_SERIES_PUBLISH_I_candidate17_bibliography_combined_guards.json'
bundle=load(old);assert sha(old.read_bytes())=='a0308928f4b6f281a97e8b6b2c4eeb128210eb30dffa4b294dbf3bbf3e59d6ba'
source=(ROOT/'S6_SERIES_PUBLISH_I.tex').read_text()
assert sha(source)==bundle['source_sha256']
rg='https://www.researchgate.net/publication/267551160_Gross-Zagier_Formula_On_Shimura_Curves'
front='https://www.degruyterbrill.com/document/doi/10.1515/9781400845644.fm/pdf'
primary={
 'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'key':'CgzYZZ2011','scope':'Bibliographic identity, edition date and citation-locator binding only. No new proof or mathematical verification.',
 'publisher_frontmatter':{'url':front,'web_refs':['turn372457304view1','turn852686367view0'],'retrieval':'Web tool opened and parsed the primary four-page PDF; direct HTTP attempt produced an empty file and is excluded.','series':'Annals of Mathematics Studies','series_number':184,'title_page_pdf_page':3,'title_page_year':2013,'copyright_page_pdf_page':4,'copyright_year':2013,'publisher':'Princeton University Press','authors':['Xinyi Yuan','Shou-Wu Zhang','Wei Zhang']},
 'publisher_product_record':{'url':'https://www.degruyterbrill.com/document/doi/10.1515/9781400845644/html','web_refs':['turn367980899view0','turn852686367view1'],'published_copyright_year':2013,'ebook_release_date':'2012-11-11','doi':'10.1515/9781400845644'},
 'registry_record':{'path':str((AUDIT/'YZZ2013_registry_primary.download').relative_to(ROOT)),'sha256':sha((AUDIT/'YZZ2013_registry_primary.download').read_bytes()),'published':'2012-12-31','published_print':'2012-12-31','published_online':'2012-12-31','issued':'2012-12-31'},
 'author_publication_list':{'path':str((AUDIT/'YZZ_author_publications_primary.download').relative_to(ROOT)),'sha256':sha((AUDIT/'YZZ_author_publications_primary.download').read_bytes()),'url':'https://math.mit.edu/~wz2113/math/pub.html','year':2012},
 'year_resolution':'Use 2013 as the formal book title-page/copyright citation year, directly printed on the publisher front matter. Record 2012 as the author-list and registry release-year data; the product record gives an ebook release in November 2012. These records are documented separately rather than silently replacing one date with another.',
 'cited_preprint':{'url':rg,'web_refs':['turn372457304view0','turn439542573view0','turn439542573view1'],'author_upload_attribution':'Xinyi Yuan','upload_date':'2014-12-15','manuscript_date':'2011-11-06','title':'Gross–Zagier Formula On Shimura Curves','authors':['Xinyi Yuan','Shou-Wu Zhang','Wei Zhang'],'locator_identity':'The contents identifies section7.1.1 at printed p.218; the author-upload text places Theorem7.1.2 before the printed p.219 marker. This confirms the identity of the already cited edition/locators; no mathematical claim is reverified.','inherited_receipt_path':'records/S6_SERIES_PUBLISH_I_bibliography_link_receipt.json','inherited_receipt_sha256':sha((ROOT/'records/S6_SERIES_PUBLISH_I_bibliography_link_receipt.json').read_bytes())},
 'unusable_direct_downloads':[{'path':str((AUDIT/n).relative_to(ROOT)),'bytes':0,'sha256':sha((AUDIT/n).read_bytes()),'status':'failed/unusable: zero bytes; supplies no primary evidence'} for n in ['YZZ2013_publisher_primary.download','YZZ_publisher_frontmatter.pdf']],
 'superseded_retrieval_status':'The final_primary_receipt.json entry YZZ2013_publisher labeled HTTP200 as retrieved despite an empty body. This receipt corrects that status to failed/unusable. All other supplementary/arXiv/final retrieval bodies were checked and are nonempty.',
 'mathematical_events_added':0,'full_page_reading_credit_added':0}
rp=AUDIT/'YZZ_publication_and_cited_edition_resolution.json';dump(rp,primary)
new_evidence={'path':str(rp.relative_to(ROOT)),'sha256':sha(rp.read_bytes()),'scope':'Current primary publisher front matter, release-year resolution, and exact author-upload cited edition'}
for g in bundle['guards']:
    if g['key']=='CrCastella2025':g['type']='D18/D23'
    if g['key']=='CgzYZZ2011':
        g['after']+='\n\n'+r'\newblock Cited preprint: \url{'+rg+'}.'
        g['proposed_entry']=g['after'];g['proposed_entry_sha256']=sha(g['after'])
        g['reason']='Add the formal book, series, publisher, title-page/copyright year 2013 and DOI, while retaining the exact 6 November 2011 cited preprint and adding its currently verified primary author-upload URL. The separate 2012 author-list/registry release dates are recorded in the publication evidence.'
        g['edition_scope']=primary['year_resolution']+' The existing body locator remains section7.1.1, pp.218–219, Theorem7.1.2 in the 6 November 2011 preprint. No edition-to-edition mathematical equivalence is asserted.'
        for field in ['primary_evidence','publication_evidence']:
            g[field]=[e for e in g[field] if not (e.get('path','').endswith('YZZ2013_publisher_primary.download'))]+[new_evidence]
        p=AREA/'candidate17_bibliography_full_entries/CgzYZZ2011_after_final.tex';assert not p.exists();p.write_text(g['after']+'\n');g['after_full_entry_path']=str(p.relative_to(ROOT))
    assert source.count(g['before'])==1
    assert re.findall(r'(?<!\\)\$[^$]*\$',g['before'])==re.findall(r'(?<!\\)\$[^$]*\$',g['after'])
proposal=source
for g in bundle['guards']:proposal=proposal.replace(g['before'],g['after'])
assert source.split('\\begin{thebibliography}',1)[0]==proposal.split('\\begin{thebibliography}',1)[0]
reverse=proposal
for g in reversed(bundle['guards']):reverse=reverse.replace(g['after'],g['before'])
assert reverse==source
bundle.update({'revision':2,'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'supersedes':{'path':str(old.relative_to(ROOT)),'sha256':sha(old.read_bytes())},'revision_scope':'Add verified dated YZZ author-upload URL and publisher-title-page year evidence; exclude empty direct downloads; classify Castella D18/D23. Other43 exact entry pairs are unchanged.','status':'final proposal; root approval pending'})
new=AREA/'S6_SERIES_PUBLISH_I_candidate17_bibliography_combined_guards_final.json';dump(new,bundle)
oldmatrix=AREA/'S6_SERIES_PUBLISH_I_candidate17_bibliography_audit_matrix.json';matrix=load(oldmatrix)
matrix.update({'revision':2,'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'bibliography_guard_file':str(new.relative_to(ROOT)),'bibliography_guard_sha256':sha(new.read_bytes()),'supersedes':{'path':str(oldmatrix.relative_to(ROOT)),'sha256':sha(oldmatrix.read_bytes())}})
for r in matrix['rows']:
    if r['key']=='CrCastella2025':r['type']='D18/D23'
    if r['key']=='CgzYZZ2011':
        g=next(g for g in bundle['guards'] if g['key']==r['key'])
        r['proposed_entry']=g['after'];r['proposed_entry_sha256']=g['proposed_entry_sha256']
        r['publication_review']=g['reason']+' '+primary['year_resolution']
        r['cited_edition_review']='The currently opened Xinyi Yuan author upload is dated 6 November 2011 and matches the inherited cited locator section7.1.1, pp.218–219, Theorem7.1.2. The URL is added without changing any body citation.'
        r['primary_evidence']=[e for e in r['primary_evidence'] if not e.get('path','').endswith('YZZ2013_publisher_primary.download')]+[new_evidence]
        r['primary_metadata']=primary
mp=AREA/'S6_SERIES_PUBLISH_I_candidate17_bibliography_audit_matrix_final.json';dump(mp,matrix)
md=['# Candidate 17: final complete bibliography audit','',f'Source SHA-256: `{matrix["source_sha256"]}`. All117 entries reviewed:45 proposed complete-entry corrections and72 retained entries. Zero mathematical events and zero page-reading credit.','',
'The YZZ published book uses the year2013 printed on its title and copyright pages. The author list and registry give2012 release-year data; both are preserved in the evidence resolution. The exact cited6November2011 author-upload URL is included. Empty direct publisher downloads are explicitly excluded.','',
'| Key | Disposition | Finding / edition preservation |','|---|---|---|']
for r in matrix['rows']:md.append('| '+r['key']+' | '+(r['guard_id'] or 'Retain')+' | '+r['publication_review'].replace('|','\\|').replace('\n',' ')+' |')
md+=['','Final exact guards: `'+str(new.relative_to(ROOT))+'`, SHA-256 `'+sha(new.read_bytes())+'`.','',matrix['primary_record_limit'],'']
mdp=AREA/'S6_SERIES_PUBLISH_I_candidate17_bibliography_audit_matrix_final.md';assert not mdp.exists();mdp.write_text('\n'.join(md))
pairs=AREA/'S6_SERIES_PUBLISH_I_candidate17_bibliography_exact_pairs_final.md';assert not pairs.exists();pairs.write_text('# Final candidate17 bibliography exact entry pairs\n\n'+''.join('## '+g['key']+' — '+g['id']+'\n\n'+g['reason']+'\n\n### Original\n\n```tex\n'+g['before']+'\n```\n\n### Proposed\n\n```tex\n'+g['after']+'\n```\n\n' for g in bundle['guards']))
receipt={'revision':2,'source_sha256':bundle['source_sha256'],'entries':117,'guards':45,'retained':72,'canonical_source_unchanged':sha((ROOT/'S6_SERIES_PUBLISH_I.tex').read_bytes())==bundle['source_sha256'],'body_byte_identical':True,'exact_reverse_reconstruction':True,'per_entry_math_unchanged':True,'mathematical_events_added':0,'full_page_reading_credit_added':0,'superseded_guard':bundle['supersedes'],'superseded_matrix':matrix['supersedes'],'files':{p.name:{'path':str(p.relative_to(ROOT)),'sha256':sha(p.read_bytes())} for p in [new,mp,mdp,pairs,rp]}}
final=AREA/'S6_SERIES_PUBLISH_I_candidate17_bibliography_supersession_receipt.json';dump(final,receipt)
print(json.dumps({'receipt':str(final.relative_to(ROOT)),'receipt_sha256':sha(final.read_bytes()),**receipt}))
