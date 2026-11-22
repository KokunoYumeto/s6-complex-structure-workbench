#!/usr/bin/env python3
"""Prepare bibliography metadata proposals; never alter the canonical source.

The exact cited arXiv source versions were established by decoded payload byte
equality. Four journal records are taken from saved publisher-deposited Crossref
metadata. The remaining three retain their identified preprint editions; the
search record makes no assertion that no publication can exist.
"""
from pathlib import Path
import datetime as dt
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation_infra'
PUB=OUT/'publisher_metadata'
SOURCE=ROOT/'S6_SERIES_PUBLISH_I.tex'
EXPECTED='61ffa2e316814c140fc69723e080b4414ea4016ba27e0ac84bd2d9347fbc93fc'


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def load(p):return json.loads(p.read_text())


def main():
    assert sha(SOURCE)==EXPECTED
    source=SOURCE.read_text()
    bound_path=OUT/'S6_SERIES_PUBLISH_I_candidate16_arxiv_version_bindings.json'
    bound=load(bound_path)
    versions={x['bibliography_key']:x for x in bound['records']}
    for item in versions.values():
        for match in item['exact_attached_source_matches']:
            assert sha(Path(match['local']))==match['sha256'] and match['exact_byte_equality']
    specifications=[
      dict(key='DMM16',page=337,old_year='2016',year='2018',doi='10.1515/crelle-2015-0104',
           journal=r'Journal f{\"u}r die reine und angewandte Mathematik',journal_locus='744:133--163',
           date='18 January 2016',version='1407.3497v2',url_kind='pdf'),
      dict(key='Dloussky2005AB',page=337,old_year='2005',year='2006',doi='10.1353/ajm.2006.0021',
           journal='American Journal of Mathematics',journal_locus='128(3):639--670',
           date='13 April 2005',version='math/0406387v3',url_kind='pdf'),
      dict(key='EH2024E',page=338,old_year='2024',year='2025',doi='10.1090/tran/9365',
           journal='Transactions of the American Mathematical Society',journal_locus='378(11):7667--7688',
           date='12 October 2024',version='2404.05124v3',url_kind='pdf'),
      dict(key='Friedman2016AB',page=338,old_year='2016',year='2016',doi=None,
           date='22 July 2016',version='1502.02560v2',url_kind='pdf'),
      dict(key='Fujiki2009D',page=339,old_year='2009',year='2009',doi=None,
           date='31 March 2009',version='0903.5374v1',url_kind='pdf'),
      dict(key='Knudson2004',page=341,old_year='2004',year='2004',doi=None,
           date='8 September 2004',version='math/0409133v1',url_kind='pdf'),
      dict(key='Matsuki00ErrAB',page=341,old_year='2000',year='2000',doi='10.2748/tmj/1178207758',
           journal='Tohoku Mathematical Journal',journal_locus='52(4):629--631',
           date='5 June 2000',version='math/0006038v1',url_kind='abs')]
    bibliostart=source.index(r'\begin{thebibliography}')
    proposed=source
    guards=[]
    dispositions=[]
    for index,s in enumerate(specifications,1):
        key=s['key']
        b=versions[key]
        assert b['arxiv_identifier']+b['version']==s['version']
        keypos=source.index('{'+key+'}',bibliostart)
        start=source.rfind(r'\bibitem',bibliostart,keypos)
        end=source.find(r'\bibitem',keypos)
        if end<0:end=source.index(r'\end{thebibliography}',keypos)
        before=source[start:end]
        title_start=before.index(r'\newblock')
        title_end=before.index(r'\newblock',title_start+1)
        header=before[:title_start]
        title=before[title_start:title_end].strip()
        assert title.endswith(', '+s['old_year']+'.')
        title=title[:-(len(s['old_year'])+3)]+'.'
        if s['year']!=s['old_year']:
            old='('+s['old_year']+')'
            assert header.count(old)==1
            header=header.replace(old,'('+s['year']+')')
        if key=='Matsuki00ErrAB':
            assert title.startswith(r'\newblock Erratum to the paper ``a note')
            title=title.replace(r'\newblock Erratum to the paper ``a note',r'\newblock Correction: ``A note',1)
        after=header+title+'\n\n'
        evidence=[]
        if s['doi']:
            path=PUB/(s['doi'].replace('/','_')+'.json')
            d=load(path)['message']
            assert d['DOI'].lower()==s['doi'].lower()
            assert d['page']==s['journal_locus'].split(':',1)[1].replace('--','-')
            print_year=(d.get('published-print') or d['published'])['date-parts'][0][0]
            assert print_year==int(s['year'])
            after+=r'\newblock {\em '+s['journal']+'}, '+s['journal_locus']+', '+s['year']+'.\n'
            after+=r'\newblock \url{https://doi.org/'+s['doi']+'}.\n'
            evidence.append(dict(path=str(path.relative_to(ROOT)),sha256=sha(path),
                                 primary_registry_url='https://api.crossref.org/works/'+s['doi'],
                                 publisher_resource_url=d['resource']['primary']['URL']))
            disposition='Journal publication data verified from the publisher-deposited registry record; the cited source edition remains the byte-matched arXiv version.'
        else:
            search=PUB/(key+'_search_receipt.json')
            search_record=load(search)
            assert len(search_record['returned_items'])>0
            evidence.append(dict(path=str(search.relative_to(ROOT)),sha256=sha(search),
                                 primary_registry_query_url=search_record['url']))
            disposition='The verified cited arXiv edition is retained. No exact corresponding journal publication record was identified in the consulted arXiv/registry/search records; this is not an assertion that publication is impossible or has never occurred.'
            if key=='Knudson2004':
                disposition+=' The author\'s current University of Florida publication list expressly calls this title a preprint (2004).'
                evidence.append(dict(primary_author_url='https://people.clas.ufl.edu/kknudson/publications/',
                                     web_reference='turn793138159view0',locator='Miscellaneous Topology Papers, final item'))
        after+=r'\newblock Cited edition (page and statement numbering): arXiv:'+s['version']+', '+s['date']+'.\n'
        after+=r'\newblock URL \url{https://arxiv.org/'+s['url_kind']+'/'+s['version']+'}.\n\n'
        assert re.findall(r'\]\{([^}]+)\}',before)==re.findall(r'\]\{([^}]+)\}',after)==[key]
        assert source.count(before)==1
        proposed=proposed.replace(before,after,1)
        gid=f'I16-infra-D18-{index:02d}'
        full=OUT/(gid+'_publication_proposed_bibliography_entry.tex')
        assert not full.exists();full.write_text(after)
        guard=dict(id=gid,revision=2,page=s['page'],type='D18',statement_id='bibliography:'+key,
                   line=source[:start].count('\n')+1,before=before,after=after,
                   reason=disposition,source_sha256=EXPECTED,citation_key_preserved=True,
                   printed_author_year_before=s['old_year'],printed_author_year_after=s['year'],
                   cited_arxiv_version=s['version'],cited_version_date=s['date'],
                   source_version_binding_receipt=str(bound_path.relative_to(ROOT)),source_version_binding_receipt_sha256=sha(bound_path),
                   publication_evidence=evidence,proposed_entry=str(full.relative_to(ROOT)),proposed_entry_sha256=sha(full),
                   supersedes_guard_file='agents/continuation_infra/S6_SERIES_PUBLISH_I_candidate16_infra_D18_guards.json',
                   status='proposed, not applied',mathematical_events_added=0)
        guards.append(guard)
        dispositions.append(dict(key=key,doi=s['doi'],year=s['year'],version=s['version'],disposition=disposition,evidence=evidence))
    assert proposed[:bibliostart]==source[:bibliostart]
    assert re.findall(r'\]\{([^}]+)\}',proposed[bibliostart:])==re.findall(r'\]\{([^}]+)\}',source[bibliostart:])
    guard_path=OUT/'S6_SERIES_PUBLISH_I_candidate16_infra_D18_publication_guards.json'
    receipt_path=OUT/'S6_SERIES_PUBLISH_I_candidate16_bibliography_publication_evidence.json'
    assert not guard_path.exists() and not receipt_path.exists()
    guard_path.write_text(json.dumps(guards,indent=2)+'\n')
    receipt=dict(recorded_utc=dt.datetime.now(dt.timezone.utc).isoformat(),paper='I',candidate=16,source_sha256=EXPECTED,
                 guards=str(guard_path.relative_to(ROOT)),guards_sha256=sha(guard_path),rows=dispositions,
                 source_after_seven_bibliography_guards_sha256=hashlib.sha256(proposed.encode()).hexdigest(),
                 entire_source_before_bibliography_byte_identical=True,all_bibliography_keys_identical=True,
                 canonical_source_unchanged=sha(SOURCE)==EXPECTED,mathematical_events_added=0,
                 page_reading_events_added=0,
                 relation_to_prior_guard_file='These seven complete-entry guards replace the earlier seven version-only proposals. Apply one set, not both.',
                 dmm_publication_notation='The publisher-deposited record has volume2018, issue744, pp.133-163. The author institutional publication record https://cris.unibo.it/handle/11585/624618 cites744(2018),133-163; that printed journal-number form is used.',
                 proof_scope='Bibliographic metadata and exact source-version binding only. No journal/preprint mathematical equivalence, new proof check, or new mathematical credit is claimed.')
    receipt_path.write_text(json.dumps(receipt,indent=2)+'\n')
    md='# Candidate16 bibliography publication proposals\n\n'
    md+='The seven full-entry guards replace the earlier version-only guard set. Four entries gain verified journal data and DOIs. Every entry explicitly identifies the exact arXiv edition used for page and statement numbering; the source-byte matches are retained. Citation keys are unchanged. Three printed author-year labels change to the journal years (2018,2006,2025). No canonical source is changed by this program.\n\n'
    md+='| Citation key | Journal record | Exact cited edition |\n|---|---|---|\n'
    for s in specifications:
        publication=(s['journal']+' '+s['journal_locus']+' ('+s['year']+'), DOI '+s['doi']) if s['doi'] else 'Verified preprint retained; no exact journal record located in the consulted sources'
        md+='| '+s['key']+' | '+publication+' | '+s['version']+', '+s['date']+' |\n'
    md+='\nThe Knudson author publication list expressly identifies the cited work as a preprint. Friedman and Fujiki remain identified by their verified arXiv editions; the evidence makes no universal nonpublication claim. All query results and publisher-deposited metadata are saved under `publisher_metadata/`.\n\n'
    md+='The complete paper source before the bibliography is byte-identical in the seven-edit proposal. The new bibliography years will update rendered author-year citations through the existing citation keys, so a new build and whole-image comparison remain required.\n'
    (OUT/'S6_SERIES_PUBLISH_I_candidate16_bibliography_publication_proposals.md').write_text(md)
    print(json.dumps(dict(guards=str(guard_path),guards_sha256=sha(guard_path),evidence=str(receipt_path),evidence_sha256=sha(receipt_path),canonical_source_unchanged=sha(SOURCE)==EXPECTED),indent=2))


if __name__=='__main__':main()
