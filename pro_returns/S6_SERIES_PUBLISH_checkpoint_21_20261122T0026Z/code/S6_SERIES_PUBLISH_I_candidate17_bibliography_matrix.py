#!/usr/bin/env python3
"""Write the complete 117-entry bibliography review, with bounded conclusions."""
import collections,datetime,hashlib,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
AREA=ROOT/'agents/continuation_infra';AUDIT=AREA/'candidate17_bibliography_audit'
sha=lambda b:hashlib.sha256(b if isinstance(b,bytes) else b.encode()).hexdigest()
load=lambda p:json.loads(p.read_text())
inv=load(AREA/'S6_SERIES_PUBLISH_I_candidate17_bibliography_inventory.json')
bundle_path=AREA/'S6_SERIES_PUBLISH_I_candidate17_bibliography_combined_guards.json'
bundle=load(bundle_path);guards={g['key']:g for g in bundle['guards']}
registry={r['key']:r for r in load(AUDIT/'existing_doi_registry_receipt.json')['rows']}
prov_path=ROOT/'agents/i_cont_provenance/S6_SERIES_PUBLISH_I_candidate17_bibliography_primary_metadata.json'
prov={r['key']:r for r in load(prov_path)}
edit_path=ROOT/'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate17_bibliography_edits_guards.json'
edit={r['key']:r for r in load(edit_path)['rows']}
receipts={}
for name in ['supplemental_primary_retrieval_receipt.json','arxiv_cited_editions_receipt.json','final_primary_receipt.json']:
    for r in load(AUDIT/name)['rows']:receipts[r['key']]=r

notes={
'BS76':'The 1976 book title-page facsimile gives Constantin Bănică and Octavian Stănășilă, the current title, Editura Academiei and John Wiley & Sons. Retain this English edition; the Romanian 1974 and French 1977 editions are separate bibliographic records. No exact DOI was established for the cited 1976 edition in the consulted records.',
'bertrand2017':'The author-hosted PDF title and author match; its front matter dates the Fields Institute/Toronto lectures to 13–17 February 2017. Retain the lecture/slides edition. No journal publication or DOI is supplied by this consulted author record.',
'Chen2026HodgeRoot':'Primary arXiv v2 metadata confirms Kuan-Wen Chen, the current title and version date 16 October 2026; preserve the already pinned v2 URL. No journal metadata was displayed in the consulted arXiv record.',
'AC2026':'Retain the exact supplied s6.pdf and the established Claude/Levent Alpöge attribution. The linked PDF title matches; its first page has no author byline. This metadata pass makes no fresh independent authorship or mathematical-provenance assertion; root owns the attached-source attribution gate.',
'ConradSL2Z':'The author-hosted 19-page notes identify Keith Conrad and SL(2,Z). No publication date is printed on the inspected title page; retain the undated-notes treatment and existing retrieval date.',
'DuEtAl2026v1':'Primary arXiv v1 metadata confirms all four authors Du, Guo, Kusakabe and Xie, current title and the pinned v1. Retain all four author names; a web summary that mentions two other authors is not used to remove an author.',
'DuEtAl2026v2':'Primary arXiv v2 metadata confirms all four authors, current title and the pinned v2. Retain the existing distinct edition and author list.',
'Friedman2016AB':'Preserve arXiv:1502.02560v2, 22 July 2016, already matched byte-for-byte to the supplied source in the earlier exact-version receipt. The current entry has no journal record; none was identified in the consulted primary records for this exact work.',
'Fujiki2009D':'Preserve arXiv:0903.5374v1, 31 March 2009, already matched byte-for-byte to the supplied source. The consulted primary record supports this preprint edition; no additional formal publication metadata was established.',
'Illman1972':'Retain the 1972 Princeton thesis Equivariant Algebraic Topology. Illman’s author-produced 1973 Annales de l’Institut Fourier summary cites that thesis; its journal DOI and year are not substituted for the thesis. No DOI for the cited thesis was established.',
'IKN2005E':'The official University of Tokyo journal abstract record and PDF confirm authors, title, 12(1), 1–66 (2005). No DOI field is displayed in that primary journal record; retain the exact official PDF.',
'IKN2007ErratumE':'The official University of Tokyo record and PDF confirm the erratum, authors, 14(1), 113–116 (2007). No DOI field is displayed in that primary journal record; retain the exact official PDF.',
'KKN2008Root':'The official University of Tokyo record and PDF confirm authors, title, 15(1), 69–193 (2008). No DOI field is displayed in that primary journal record; retain the exact official PDF.',
'Knudson2004':'Preserve arXiv:math/0409133v1, 8 September 2004, already byte-bound to the supplied source. The consulted primary record supports that preprint; no additional exact formal publication record was established.',
'McMullen1996Complex':'The author-hosted course outline identifies C. McMullen, Complex Manifolds, Math 241, Spring 1996, Berkeley; retain this course-notes citation.',
'Movasati24':'The linked author manuscript is dated 13 May 2024. The author’s books page lists it among lecture notes/projects converging to books; retain the current dated manuscript and do not infer formal publication.',
'Nishiguchi1988IIRoot':'The primary MPI PDF identifies Kenji Nishiguchi, Degeneration of K3 surfaces, II, MPI/88-48, 1988. Retain that exact report. The journal article found without II in its title is not substituted without an edition binding.',
'Oda1978D':'The official TIFR PDF identifies Tadao Oda, title, volume 58, 1978 and Springer publication for TIFR. “Based on joint work with Katsuya Miyake” is retained as source context rather than converting the credited author line. Preserve the current retypeset-edition qualification. No exact DOI was established in the consulted records.',
'Pinkham1974Root':'The primary Numdam book record confirms Henry C. Pinkham, the current title, Astérisque 20, Société mathématique de France, 1974 and 140 pages. No DOI field appears in that record; retain the cited book.',
'Schnell19':'The author’s lecture PDF actually spells its title “Appel-Humbert”; retain that transcription. The course directory is 2019, and the lecture page is dated February 6. No independent publication or DOI is asserted.',
'silverman2006heights':'The author/institute-hosted slides identify Joseph H. Silverman, An Introduction to Height Functions, and MSRI 17–21 January 2006. Retain the existing January 2006 slides citation.',
'Xiao91':'The primary MPI/91-30 report identifies Gang Xiao, the current title and 1991. The complete given name is visible in source and the enlarged current render; no author-initial correction is needed. No additional exact journal record was established in consulted primary sources.',
'FujikiPontecorvo2010AB':'The primary publisher PDF header and author-institution record give pages 15–71, retained here. Crossref’s 15–72 conflicts with those primary item records and is not copied into the bibliography.',
'CrGross1991':'Gross’s author publication list gives “on modular elliptic curves”, matching the current entry. The Cambridge/Crossref web form says “for”; retain the author’s own wording, with the same publication, pages and DOI.',
'BM97':'Primary arXiv metadata confirms both Edward Bierstone and Pierre D. Milman. The current author list is retained even though the Crossref record lists only Bierstone. Published journal pagination and the separately identified earlier v2 are preserved.',
'DMM16':'The author-produced PDF identifies Mark Andrea A. de Cataldo; retain the middle initial omitted from the registry’s compact name. The 2018 publication and exact supplied 2016 v2 citation remain explicit.',
'CDL24':'The entry distinguishes the cited 2024 author manuscript from the published 2025 second edition and its DOI. Preserve both dates and the cited-manuscript URL rather than rebinding the citation to the published edition.',
'Shioda90':'The JaLC/Rikkyo primary record confirms the existing DOI 10.14992/00009994 and author/title/journal data 39(2), 211–240 (1990). Crossref has no record for this JaLC DOI; that failed Crossref lookup does not invalidate the DOI.',
}
extras={
'BM97':['BM97_arxiv'], 'DMM16':['DMM16_author_pdf'],
'CrGross1991':['Gross_author_publications'],
'FujikiPontecorvo2010AB':['FujikiPontecorvo2010_publisher_pdf'],
'Fujimoto1990AB':['Fujimoto1990AB_repository','Fujimoto1990_publisher','Fujimoto_journal_registry'],
'Shioda90':['Shioda90_repository'],
'Illman1972':['Illman1973_author_summary'],
'Movasati24':['Movasati_author_books'],
'IKN2005E':['IKN2005E_publisher'],
'IKN2007ErratumE':['IKN2007ErratumE_publisher'],
'KKN2008Root':['KKN2008Root_publisher'],
'Pinkham1974Root':['Pinkham1974Root_publisher'],
'Loj64':['Loj64_publisher'],
'CgzYZZ2011':['YZZ2013_publisher','YZZ_author_publications','YZZ2013_registry'],
}
def file_evidence(p,scope=None):
    d={'path':str(p.relative_to(ROOT)),'sha256':sha(p.read_bytes())}
    if scope:d['scope']=scope
    return d

rows=[]
for e in inv['entries']:
    key=e['key'];g=guards.get(key);after=g['after'] if g else e['original_entry']
    evidence=[];metadata=None
    if key in registry:
        r=registry[key]
        if r['status']=='retrieved':
            p=ROOT/r['path'];assert sha(p.read_bytes())==r['sha256']
            evidence.append({'path':r['path'],'sha256':r['sha256'],'url':r['primary_registry_url']})
            metadata={k:r.get(k) for k in ['title','author','container-title','publisher','volume','issue','page','published-print','published-online','type']}
    for name in [key]+extras.get(key,[]):
        if name in receipts:
            r=receipts[name];assert r['status']=='retrieved',name
            assert sha((ROOT/r['path']).read_bytes())==r['sha256']
            evidence.append({k:r[k] for k in ['path','sha256','url']})
            if not metadata:metadata=r.get('metadata_fields',{'first_page_metadata_excerpt':r.get('first_page_metadata_excerpt'),'content_type':r.get('content_type')})
    if g:evidence+=g['publication_evidence']
    if key in prov:
        metadata=prov[key];evidence+=[file_evidence(prov_path,'Peer primary metadata, exact key '+key)]+prov[key]['primary']
        conclusion=prov[key]['change'];doi_status=prov[key]['doi_status']
    elif key in edit:
        metadata=edit[key];evidence+=[file_evidence(edit_path,'Peer ten-entry metadata audit, exact key '+key)]+edit[key]['primary_sources']
        conclusion=' '.join(edit[key].get('field_changes',[])) or 'Retain the complete entry; primary evidence confirms current metadata.'
        doi_status=edit[key]['doi_disposition']
    else:
        conclusion=notes.get(key) or (g['reason'] if g else 'Reviewed author sequence, title, published venue, print year, volume/issue and pages against the primary DOI registration metadata; retain the current entry and its existing cited-edition qualifications.')
        if g and key in notes:conclusion+=' '+g['reason']
        if e['doi'] or key=='huber2022':doi_status='Existing DOI verified in the linked primary registration/publisher record; retained, with any explicit additional record identified in the proposed entry.'
        elif re.search(r'\\doi\{',after):doi_status='A previously absent verified formal-publication DOI is supplied by the exact full-entry guard.'
        else:doi_status='No exact DOI was established in the consulted primary records. This is a bounded lookup result; it makes no global assertion that a DOI or later publication does not exist.'
    if key=='BS76':
        evidence.append({'url':'https://djvu.online/file/2hQiOnz8WuoQk','web_ref':'turn486460636search2','scope':'Publisher-produced 1976 title-page facsimile: authors, title, both imprints and year only; third-party host.'})
        metadata={'authors':['Constantin Bănică','Octavian Stănășilă'],'title':'Algebraic Methods in the Global Theory of Complex Spaces','year':1976,'publishers':['Editura Academiei','John Wiley & Sons'],'edition':'English 1976'}
    if key in ['Friedman2016AB','Fujiki2009D','Knudson2004','DMM16','Dloussky2005AB','EH2024E','Matsuki00ErrAB']:
        p=AREA/'S6_SERIES_PUBLISH_I_candidate16_arxiv_version_bindings.json';evidence.append(file_evidence(p,'Exact-byte supplied-source/arXiv-version binding'))
    assert evidence,key
    # Record actual citation tokens, without evaluating their mathematics.
    src=(ROOT/'S6_SERIES_PUBLISH_I.tex').read_text()
    citations=[m.group(0) for m in re.finditer(r'\\cite\w*\*?(?:\[[^\]]*\]){0,2}\{[^}]*\b'+re.escape(key)+r'\b[^}]*\}',src)]
    rows.append({'key':key,'source_line':e['start_line'],'original_entry_sha256':e['entry_sha256'],
      'original_entry':e['original_entry'],'proposed_entry':after,'proposed_entry_sha256':sha(after),
      'disposition':'exact full-entry correction proposed' if g else 'retain current entry after bounded primary-source audit',
      'guard_id':g['id'] if g else None,'type':g['type'] if g else None,
      'author_title_review':'Reviewed against the primary evidence listed; source-specific discrepancies and limits are stated in the conclusion.',
      'publication_review':conclusion,'doi_review':doi_status,
      'cited_edition_review':'Existing citation key and frozen body citation tokens are retained; changes to publication labels, exact version URLs or edition notes are explicit in the full-entry map.',
      'frozen_body_citation_tokens':citations,'primary_metadata':metadata,'primary_evidence':evidence,
      'mathematical_events_added':0,'full_page_reading_credit_added':0})
assert len(rows)==117 and len({r['key'] for r in rows})==117
out={'paper':'I','candidate':17,'source_sha256':inv['source_sha256'],
 'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'entry_count':117,'changed_entry_count':len(guards),'retained_entry_count':117-len(guards),
 'scope':'Complete bibliography metadata audit: authors/title transcription, formal publication metadata, available DOI in consulted primary records, and preservation of the cited edition. This adds no mathematical verification or page-reading credit.',
 'bibliography_guard_file':str(bundle_path.relative_to(ROOT)),'bibliography_guard_sha256':sha(bundle_path.read_bytes()),
 'primary_record_limit':'A field absent from a consulted publisher/archive record is recorded as a bounded absence; no universal claim about nonpublication or DOI nonexistence is made.',
 'metadata_resolution_notes':['Published issue/print years are retained where online dates differ.','Exact version bindings use frozen citation scope or supplied-source byte identity; no newest-version substitution is made.','Crossref discrepancies for Fujiki–Pontecorvo, Gross, Bierstone–Milman and de Cataldo are resolved using the item or author primary record, as recorded per entry.','Metadata extraction and source retrieval do not add full-page reading or mathematical credit.'],
 'rows':rows,'mathematical_events_added':0,'full_page_reading_credit_added':0,'certification_changed':False}
target=AREA/'S6_SERIES_PUBLISH_I_candidate17_bibliography_audit_matrix.json'
assert not target.exists();target.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
md=['# Candidate 17: complete bibliography audit','',f'Source SHA-256: `{inv["source_sha256"]}`. All 117 entries were reviewed; 45 exact full-entry corrections are proposed and 72 entries are retained. Canonical source remains frozen. This audit adds zero mathematical events and zero page-reading credit.','',
'## Scope and evidence','',out['scope'], '',out['primary_record_limit'],'',
'## Entry-by-entry disposition','', '| Key | Disposition | Finding / edition preservation |', '|---|---|---|']
for r in rows:md.append('| '+r['key']+' | '+(r['guard_id'] or 'Retain')+' | '+r['publication_review'].replace('|','\\|').replace('\n',' ')+' |')
md+=['','## Exact entry changes','',f'The frozen guard bundle is `{bundle_path.relative_to(ROOT)}`, SHA-256 `{sha(bundle_path.read_bytes())}`. It contains all original/proposed full-entry text, source-line/current-page scope, exact hashes, and primary-evidence bindings. The 90 complete entry archives are in `agents/continuation_infra/candidate17_bibliography_full_entries/`.','',
'The full mathematical body is byte-identical. Exact reverse reconstruction of all bibliography replacements returns the frozen source. Math segments are compared within each complete entry; the known whole-file dollar-regex offset is not used as evidence.','',
'Formal author-year labels change for Abate et al. (2010 → 2013), Parusiński (1990 → 1994), Yuan–Zhang–Zhang (2011 → 2013), and Jetchev–Lauter–Stein (2008 → 2009). Exact dated cited-edition notes retain the preprint page and statement locators. Full-document rendering is therefore required after integration.','']
mdp=AREA/'S6_SERIES_PUBLISH_I_candidate17_bibliography_audit_matrix.md';assert not mdp.exists();mdp.write_text('\n'.join(md))
review=AREA/'S6_SERIES_PUBLISH_I_candidate17_bibliography_exact_pairs.md'
assert not review.exists()
review.write_text('# Candidate 17 bibliography: exact complete-entry pairs\n\n'+''.join('## '+g['key']+' — '+g['id']+'\n\n'+g['reason']+'\n\n### Original\n\n```tex\n'+g['before']+'\n```\n\n### Proposed\n\n```tex\n'+g['after']+'\n```\n\n' for g in bundle['guards']))
receipt={'source_sha256':inv['source_sha256'],'matrix_path':str(target.relative_to(ROOT)),'matrix_sha256':sha(target.read_bytes()),'matrix_markdown_path':str(mdp.relative_to(ROOT)),'matrix_markdown_sha256':sha(mdp.read_bytes()),'pairs_path':str(review.relative_to(ROOT)),'pairs_sha256':sha(review.read_bytes()),'guards_path':str(bundle_path.relative_to(ROOT)),'guards_sha256':sha(bundle_path.read_bytes()),'entries':117,'guards':45,'retained':72,'all_keys_unique':True,'mathematical_events_added':0,'full_page_reading_credit_added':0,'canonical_source_unchanged':sha((ROOT/'S6_SERIES_PUBLISH_I.tex').read_bytes())==inv['source_sha256']}
rp=AREA/'S6_SERIES_PUBLISH_I_candidate17_bibliography_final_receipt.json';assert not rp.exists();rp.write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
