#!/usr/bin/env python3
"""Prepare ten-entry bibliography audit and nine exact proposals; no canonical writes."""
from pathlib import Path
import collections
import datetime
import difflib
import gzip
import hashlib
import importlib.util
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/i_cont_edits'
EVID = OUT / 'bibliography_candidate17'
SOURCE_SHA = '5b74359a048b1eab3e478a65eab35f35b45474c4c65aadaedd639315c19a9379'
PDF_SHA = '3c9f15b28d768f305ab09dfb86ef98365aeb4659329b33e6faedb91864094ab0'
sha = lambda b: hashlib.sha256(b).hexdigest()
spec = importlib.util.spec_from_file_location('guard_helpers', ROOT / 'code/S6_SERIES_PUBLISH_I_candidate16_edits_guards.py')
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)

DOIS = {
    'MazurSteinTate2006': '10.4171/DMS/4/17',
    'nguyen2023': '10.1007/s00208-022-02465-x',
    'CrRubin1999': '10.1007/BFb0093455',
    'SchroeerSiebert2002Root': '10.1007/978-3-642-56202-0_14',
    'Shin2015': '10.4134/JKMS.2015.52.5.907',
    'CgzStein2007': '10.1090/gsm/079',
    'waldschmidt1988periodrank': '10.1017/CBO9780511897184.025',
}
KEYS = ['MazurSteinTate2006', 'McHugh2018', 'nguyen2023', 'CrRubin1999',
        'SchroeerSiebert2002Root', 'Shin2015', 'CgzStein2007',
        'waldschmidt1979sigma', 'waldschmidt1988periodrank', 'waldschmidt1988theta']
WEB = {
    'MazurSteinTate2006': [
        ('https://ems.press/books/dms/254/contents', 'turn537212026view5', 'The EMS contents lists the article on pages 577–614 and DOI 10.4171/DMS/4/17. Crossref confirms author order Mazur, Stein, Tate and print year 2006.')],
    'McHugh2018': [
        ('https://www.rivmat.unipr.it/vols/2019-10-1/02-mchugh.html', 'turn821789202view1', 'The journal record confirms Andrew McHugh, title, volume 10, number 1, year 2019 and pages 25–62. No DOI is displayed on this record.'),
        ('https://arxiv.org/abs/1708.03251v4', None, 'Direct HTTP retrieval confirms v4 on 15 November 2018. The existing body citations explicitly use arXiv v4. The current bibliography note is retained exactly.')],
    'nguyen2023': [
        ('https://link.springer.com/article/10.1007/s00208-022-02465-x', 'turn821789202view6', 'The publisher record confirms Khoa D. Nguyen, title, volume 387, pages 1–15 and issue year 2023; the online version-of-record date is 26 August 2022. Crossref supplies issue 1–2.'),
        ('https://arxiv.org/abs/2112.14937v1', 'turn898155408view1', 'The archive identifies v1 dated 30 December 2021. The existing body citation explicitly uses arXiv v1, page 3.')],
    'CrRubin1999': [
        ('https://link.springer.com/chapter/10.1007/BFb0093455', 'turn821789202view4', 'The publisher chapter citation confirms Karl Rubin, the chapter title, print year 1999, LNM volume 1716, pages 167–234 and chapter DOI. The separate lecture-note URL and its 1–68 locator note remain exact.')],
    'SchroeerSiebert2002Root': [
        ('https://link.springer.com/chapter/10.1007/978-3-642-56202-0_14', 'turn821789202view5', 'The publisher confirms Schröer and Siebert, the chapter title, Complex Geometry, year 2002, pages 193–222 and chapter DOI. The existing conference qualifier and author-hosted source URL remain exact.')],
    'Shin2015': [
        ('https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART002022386', 'turn839904261view1', 'The Korean journal registry confirms author, title, journal, volume 52, issue 5, year 2015 and pages 907–928.'),
        ('https://arxiv.org/abs/1009.2253', 'turn839904261view2', 'The archive history dates v6 to 18 October 2014. The downloaded v6 source is byte-identical to the immutable attached source; no latest-version inference is used.')],
    'CgzStein2007': [
        ('https://www.ams.org/books/gsm/079/gsm079-endmatter.pdf', 'turn839904261search0', 'The primary AMS book search record supplies book DOI 10.1090/gsm/079. Direct Crossref metadata confirms William Stein, the title, series and print year 2007. The author-hosted PDF and existing volume 79 are retained.')],
    'waldschmidt1979sigma': [
        ('https://mathreports.ca/article/nombres-transcendants-et-fonctions-sigma-de-weirstrass/', 'turn291123743view5', 'The journal archive confirms M. Waldschmidt, volume 1, issue 2, year 1979 and pages 111–114; its title metadata misspells Weierstrass. The author-hosted first-page image actually reads WEIERSTRASS, supporting retention of the existing article title. The journal masthead supplies accents in mathématiques and Académie. No DOI is displayed.'),
        ('https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/GDL/SigmaNoteCanada1979-fr.pdf', 'turn821789202view2', 'The first full page was actually viewed locally: printed page 111, volume 1, number 2, year 1979, article title and author agree with the existing entry.')],
    'waldschmidt1988periodrank': [
        ('https://www.cambridge.org/core/books/abs/new-advances-in-transcendence-theory/on-the-transcendence-methods-of-gelfond-and-schneider-in-several-variables/B3B9B78FE083CA74FC9C1D874D4CA25D', 'turn291123743view4', 'The publisher confirms chapter 24, author M. Waldschmidt, editor Alan Baker, chapter title, pages 375–398, print year 1988 and DOI 10.1017/CBO9780511897184.025. The later online date is not substituted for the print year.')],
    'waldschmidt1988theta': [
        ('https://webusers.imj-prg.fr/~michel.waldschmidt/texts.html', 'turn537212026search0', 'The author bibliography identifies the Bordeaux 1987–1988 seminar, exposé 15, seven pages.'),
        ('https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/PPN320141322_0016__0_0.pdf', 'turn821789202view3', 'The digitization has nine PDF pages: archive cover, seven article pages and a trailing blank. The title page, printed page 15–07 and following blank were actually viewed locally. The title page identifies exposé 15 and 5 February 1988. Retain existing bibliographical pages 1–7; the cover metadata 1–8 counts the trailing blank. No DOI is displayed.')],
}

def dump(path, obj):
    assert not path.exists(), path
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')

def main():
    protected = [ROOT/'S6_SERIES_PUBLISH_I.tex', ROOT/'S6_SERIES_PUBLISH_defects_I.tsv', ROOT/'CHECK_EVENTS.tsv',
                 OUT/'S6_SERIES_PUBLISH_I_final_candidate17_reading_edits.json',
                 OUT/'S6_SERIES_PUBLISH_I_candidate17_type_closure_preparation.json',
                 OUT/'S6_SERIES_PUBLISH_I_candidate17_edits_guards.json']
    frozen = {str(p.relative_to(ROOT)): p.read_bytes() for p in protected}
    s = frozen['S6_SERIES_PUBLISH_I.tex'].decode()
    assert sha(s.encode()) == SOURCE_SHA
    assert sha((ROOT/'build/I_candidate17/S6_SERIES_PUBLISH_I.pdf').read_bytes()) == PDF_SHA
    inventory_path = ROOT/'agents/continuation_infra/S6_SERIES_PUBLISH_I_candidate17_bibliography_inventory.json'
    inventory = json.loads(inventory_path.read_text())
    assert inventory['source_sha256'] == SOURCE_SHA
    entries = {r['key']: r for r in inventory['entries']}
    manifest = json.loads((EVID/'fetch_manifest.json').read_text())
    fetched = {r['key']:r for r in manifest['rows']}
    for r in fetched.values():
        assert r.get('status') == 200, r
        assert sha(Path(r['path']).read_bytes()) == r['sha256']
    download = OUT/'S6_SERIES_PUBLISH_I_candidate17_bib_shin_v6_source.download'
    shin_original = ROOT.parent/'S6_SERIES_PUBLISH_work/S6_PUBLISH_literature_arxiv/1009.2253/1009.2253.tex'
    assert gzip.decompress(download.read_bytes()) == shin_original.read_bytes()
    shin_binding = {'source_url':'https://arxiv.org/src/1009.2253v6', 'version':'v6', 'date':'18 October 2014',
                    'download_path':str(download.relative_to(ROOT)), 'download_sha256':sha(download.read_bytes()),
                    'immutable_source_path':str(shin_original), 'source_sha256':sha(shin_original.read_bytes()),
                    'source_bytes':shin_original.stat().st_size, 'exact_byte_match':True}
    mchugh_html = EVID/'McHugh2018_arxiv_v4.html'
    assert '15 Nov 2018' in mchugh_html.read_text()
    rows=[]; guards=[]; proposed=s; inverse=[]
    for key in KEYS:
        entry=entries[key]; old=entry['original_entry']; new=old
        assert sha(old.encode())==entry['entry_sha256'] and s.count(old)==1
        changes=[]
        if key=='McHugh2018':
            new+='\n\\newblock Cited edition: \\url{https://arxiv.org/pdf/1708.03251v4}.'
            changes.append('Add versioned URL for the already named cited edition; preserve the existing locator/date note and journal PDF URL exactly.')
        if key=='nguyen2023':
            new=new.replace('387:\\penalty0 1--15','387(1--2):\\penalty0 1--15')
            new=new.replace('https://arxiv.org/pdf/2112.14937','https://arxiv.org/pdf/2112.14937v1')
            new+='\n\\newblock The cited edition is arXiv:2112.14937v1, 30 December 2021.'
            changes.extend(['Add publisher issue 1–2.','Pin the existing arXiv URL to v1, matching the body locator, and add its date.'])
        if key=='Shin2015':
            new=new.replace('https://arxiv.org/pdf/1009.2253','https://arxiv.org/pdf/1009.2253v6')
            new+='\n\\newblock Page references use arXiv:1009.2253v6, 18 October 2014.'
            changes.append('Pin the existing arXiv URL to v6 and identify the page-reference edition, justified by exact immutable-source byte equality.')
        if key=='waldschmidt1979sigma':
            new=new.replace("Comptes Rendus Mathematiques de l'Academie des Sciences,", "Comptes Rendus Math\\'ematiques de l'Acad\\'emie des Sciences,")
            changes.append('Restore the two French accents in the journal title; retain article spelling, year, volume, issue, pages and URL.')
        if key in DOIS:
            doi=DOIS[key]
            metadata=json.loads((EVID/(key+'_crossref.json')).read_text())['message']
            assert metadata['DOI'].lower()==doi.lower()
            new+='\n\\newblock \\doi{'+doi+'}.'
            changes.append('Add the confirmed published DOI using the existing doi macro.')
        assert helper.math_segments(old)==helper.math_segments(new), key
        assert re.findall(r'\\bibitem(?:\[[^\n]*\])?\{([^}]+)\}',old)==re.findall(r'\\bibitem(?:\[[^\n]*\])?\{([^}]+)\}',new)
        base='S6_SERIES_PUBLISH_I_candidate17_bib_'+key
        original_path=OUT/(base+'_original.tex'); proposed_path=OUT/(base+'_proposed.tex'); diff_path=OUT/(base+'.diff')
        for p,t in [(original_path,old),(proposed_path,new),(diff_path,''.join(difflib.unified_diff(old.splitlines(keepends=True),new.splitlines(keepends=True),fromfile='original/'+key,tofile='proposed/'+key)))]:
            if p.exists():assert p.read_text()==t,p
            else:p.write_text(t)
        row={'key':key,'source_line':entry['start_line'],'original_entry':old,'proposed_entry':new,
             'original_entry_sha256':sha(old.encode()),'proposed_entry_sha256':sha(new.encode()),
             'original_path':str(original_path.relative_to(ROOT)),'proposed_path':str(proposed_path.relative_to(ROOT)),
             'diff_path':str(diff_path.relative_to(ROOT)),'diff_sha256':sha(diff_path.read_bytes()),
             'field_changes':changes,'published_doi':DOIS.get(key),
             'doi_disposition':'confirmed published DOI' if key in DOIS else 'No DOI found in the inspected primary record(s) and eight-result Crossref title/author query; no universal absence claim.',
             'primary_sources':[{'url':u,'web_ref':r,'observations':t} for u,r,t in WEB[key]],
             'crossref_record':{k:v for k,v in fetched[key].items() if k!='metadata'},
             'all_mathematical_segments_identical':True,'citation_key_and_author_year_label_identical':True,
             'complete_original_and_proposed_entries_reviewed':False,
             'mathematical_events_added':0,'source_modified':False}
        if key=='Shin2015':row['cited_edition_source_binding']=shin_binding
        if key=='McHugh2018':row['cited_edition_record']={'url':'https://arxiv.org/abs/1708.03251v4','path':str(mchugh_html.relative_to(ROOT)),'sha256':sha(mchugh_html.read_bytes()),'version':'v4','date':'15 November 2018'}
        rows.append(row)
        if new!=old:
            bid=f'I17-edits-bib-{len(guards)+1:02d}'
            typ='D23' if key=='waldschmidt1979sigma' else 'D18'
            guard={'id':bid,'type':typ,'statement_id':'bibliography:'+key,'source_line':entry['start_line'],
                   'before':old,'after':new,'reason':' '.join(changes),'key':key,
                   'source_sha256':SOURCE_SHA,'pdf_sha256':PDF_SHA,'status':'proposed for root and infrastructure review; not applied',
                   'all_mathematical_segments_identical':True,'citation_key_and_author_year_label_identical':True,
                   'command_order_qualification':'Bibliographic DOI, URL, newblock and/or accent commands are intentionally added as shown in the exact full-entry map; no unchanged-command-sequence claim is made.',
                   'original_entry_sha256':row['original_entry_sha256'],'proposed_entry_sha256':row['proposed_entry_sha256'],
                   'full_entry_archive':{k:row[k] for k in ['original_path','proposed_path','diff_path','diff_sha256']},
                   'mathematical_events_added':0}
            guards.append(guard); row['guard_id']=bid
            assert proposed.count(old)==1
            proposed=proposed.replace(old,new,1)
            inverse.append({'guard_id':bid,'before':new,'after':old})
    reconstructed=proposed
    for inv in reversed(inverse):
        assert reconstructed.count(inv['before'])==1
        reconstructed=reconstructed.replace(inv['before'],inv['after'],1)
    assert reconstructed==s
    assert s[:s.index(r'\begin{thebibliography}')]==proposed[:proposed.index(r'\begin{thebibliography}')]
    # The raw whole-file dollar regex pairs a closing bibliography dollar
    # with the next entry's opening dollar. Preserve its observed failure;
    # actual preservation follows from the byte-identical entire body,
    # the exact entry inverse map, and each complete entry's equal segments.
    raw_before=helper.math_segments(s);raw_after=helper.math_segments(proposed)
    raw_diagnostics=[]
    for pi,(aa,bb) in enumerate(zip(raw_before,raw_after)):
        assert len(aa)==len(bb)
        for j,(a,b) in enumerate(zip(aa,bb)):
            if a!=b:
                assert pi==3 and '\\bibitem' in a
                raw_diagnostics.append({'pattern_index':pi,'match_index':j,
                    'source_line':s.count('\n',0,s.index(a))+1,
                    'before':a,'after':b,
                    'diagnosis':'Raw dollar matching crosses complete bibliography entry boundaries; this is not an actual mathematical segment. The complete source body is byte-identical and each complete edited entry has identical mathematical segments.'})
    images=[]
    for n in ['waldsigma_page_01.png','waldtheta_page_02.png','waldtheta_page_08.png','waldtheta_page_09.png']:
        p=EVID/n;images.append({'path':str(p.relative_to(ROOT)),'sha256':sha(p.read_bytes()),'actual_local_image_view':True,'scope':'bibliographic title/pagination review only; zero Paper I page credit and zero mathematical events'})
    for rel,b in frozen.items():assert (ROOT/rel).read_bytes()==b
    result={'paper':'I','candidate':17,'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'source_sha256':SOURCE_SHA,'pdf_sha256':PDF_SHA,'defect_log_sha256':sha(frozen['S6_SERIES_PUBLISH_defects_I.tsv']),
            'inventory_path':str(inventory_path.relative_to(ROOT)),'inventory_sha256':sha(inventory_path.read_bytes()),
            'scope':'Ten assigned bibliography entries only. Publisher/archive/registry evidence, seven confirmed published DOIs, exact cited-edition bindings, and one journal-accent correction. No mathematical or claim-provenance rechecking credit.',
            'rows':rows,'guards':guards,'row_count':len(rows),'guard_count':len(guards),'doi_addition_count':len(DOIS),
            'exact_inverse_map':inverse,'own_proposed_source_sha256':sha(proposed.encode()),
            'exact_forward_and_inverse_verified':True,'body_byte_identical':True,'all_mathematical_segments_identical':True,
            'mathematical_preservation_basis':'Byte-identical entire body, exact outside-entry reconstruction, and identical segments within every complete edited bibliography entry.',
            'raw_whole_file_math_regex_equal':raw_before==raw_after,'raw_dollar_regex_diagnostics':raw_diagnostics,
            'existing_citation_keys_and_author_year_labels_identical':True,
            'url_preservation_qualification':'Existing non-arXiv URLs remain exact. Nguyen and Shin bare arXiv URLs are replaced by the same identifiers with the established v1 and v6 suffixes. McHugh gains an additional v4 URL; its existing journal URL and locator note remain exact.',
            'primary_pdf_images_actually_viewed':images,'shin_source_binding':shin_binding,
            'protected_files_sha256':{k:sha(v) for k,v in frozen.items()},
            'source_modified':False,'log_modified':False,'mathematical_events_added':0,'additional_paper_I_page_credit':0,
            'status':'Preparation saved for exact entry review; canonical application remains pending root approval.'}
    result_path=OUT/'S6_SERIES_PUBLISH_I_candidate17_bibliography_edits_preparation.json'
    dump(result_path,result)
    md=['# Paper I — candidate 17: ten-entry bibliography preparation','',f'Source: `{SOURCE_SHA}`. PDF: `{PDF_SHA}`.','',
        'Seven published DOIs are confirmed by primary publisher/registry records. Nine exact full-entry proposals are supplied; the theta note remains unchanged. Canonical source, defect log, check ledger and completed reading records are unchanged.','',
        '| Key | Proposed fields | DOI disposition |','|---|---|---|']
    for r in rows:md.append('| '+r['key']+' | '+(' '.join(r['field_changes']) or 'Retain complete entry.')+' | '+(r['published_doi'] or 'No DOI found in the specified bounded checks.')+' |')
    md += ['','## Edition and pagination evidence','',
           'The downloaded Shin v6 source is byte-identical to the immutable attached source (72,210 bytes; SHA-256 `'+shin_binding['source_sha256']+'`). The bibliography can therefore pin v6, dated 18 October 2014. Nguyen’s body cites v1; McHugh’s body and existing bibliography identify v4, dated 15 November 2018. Existing locator notes are preserved.','',
           'The Waldschmidt theta digitization has an archive cover, seven article pages and a trailing blank. The title page, printed page 15–07 and blank page were viewed. Existing bibliographical pages 1–7 are retained. The sigma title image spells Weierstrass correctly; the journal site’s title typo is not imported.','',
           'The exact source reconstruction, nine full-entry archives and differences, all ten dispositions, raw Crossref retrieval hashes, primary-source URLs and image hashes are in the JSON preparation. Final exact-entry visual/text review is recorded separately before this preparation is sent for approval.','']
    md_path=result_path.with_suffix('.md');assert not md_path.exists();md_path.write_text('\n'.join(md))
    print(json.dumps({'path':str(result_path.relative_to(ROOT)),'sha256':sha(result_path.read_bytes()),'rows':len(rows),'guards':len(guards),'proposed_source_sha256':sha(proposed.encode()),'canonical_unchanged':True},indent=2))

if __name__=='__main__':main()
