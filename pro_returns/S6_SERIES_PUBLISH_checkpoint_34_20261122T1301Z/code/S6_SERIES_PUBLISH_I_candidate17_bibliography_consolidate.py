#!/usr/bin/env python3
"""Assemble source-bound bibliography guards and a 117-entry evidence matrix.

This writes proposals only. It never changes canonical source, defect logs,
CHECK_EVENTS, certification, or page-reading records.
"""
import datetime, hashlib, importlib.util, json, re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
AREA=ROOT/'agents/continuation_infra'
AUDIT=AREA/'candidate17_bibliography_audit'
SOURCE=ROOT/'S6_SERIES_PUBLISH_I.tex'
EXPECTED='5b74359a048b1eab3e478a65eab35f35b45474c4c65aadaedd639315c19a9379'
sha=lambda b:hashlib.sha256(b if isinstance(b,bytes) else b.encode()).hexdigest()
inventory=json.loads((AREA/'S6_SERIES_PUBLISH_I_candidate17_bibliography_inventory.json').read_text())
entries={x['key']:x for x in inventory['entries']}
source=SOURCE.read_text()
assert sha(SOURCE.read_bytes())==EXPECTED==inventory['source_sha256']
assert len(entries)==117
guards=[]
own_notes={}

def add(key,after,reason,evidence,kind='D18',extra=None):
    e=entries[key];before=e['original_entry']
    assert source.count(before)==1,key
    assert before!=after,key
    assert re.findall(r'\\bibitem\[[\s\S]*?\]\{([^}]+)\}',before)==re.findall(r'\\bibitem\[[\s\S]*?\]\{([^}]+)\}',after)==[key]
    # Complete-entry parsing avoids a known whole-file inline-dollar offset.
    assert re.findall(r'(?<!\\)\$[^$]*\$',before)==re.findall(r'(?<!\\)\$[^$]*\$',after),key
    g={'id':f'I17-infra-bib-{len(guards)+1:02d}','key':key,'type':kind,
       'statement_id':'bib:'+key,'line':e['start_line'],
       'before':before,'after':after,'original_entry':before,'proposed_entry':after,
       'reason':reason,'source_sha256':EXPECTED,'original_entry_sha256':sha(before),
       'proposed_entry_sha256':sha(after),'citation_key_preserved':True,
       'primary_evidence':evidence,'publication_evidence':evidence,'status':'proposed; root review pending',
       'mathematical_events_added':0,'full_page_reading_credit_added':0}
    if extra:g.update(extra)
    guards.append(g);own_notes[key]=reason

def path(name):return 'agents/continuation_infra/candidate17_bibliography_audit/'+name
def ev(name,url=None):
    p=ROOT/path(name);r={'path':path(name),'sha256':sha(p.read_bytes())}
    if url:r['url']=url
    return r

# New formal publication records, retaining every cited manuscript edition.
key='AbateBracciSuwaTovena2010Atiyah';b=entries[key]['original_entry']
a=b.replace('et~al.(2010)','et~al.(2013)').replace(r'\emph{Localization of Atiyah classes}.','Localization of Atiyah classes.')
a=a.replace(r'\newblock Author manuscript dated 7 May 2010.',r'''\newblock \emph{Revista Matem\'atica Iberoamericana}, 29\penalty0 (2):\penalty0
  547--578, 2013.

\newblock \doi{10.4171/RMI/730}.

\newblock The cited edition is the author manuscript dated 7 May 2010;
  page and statement references use that edition.''')
add(key,a,'Add the verified 2013 journal publication and DOI while preserving the cited author manuscript of 7 May 2010 and its page/statement locators.',[ev('Abate2013_publisher_primary.download','https://ems.press/journals/rmi/articles/11948'),ev('AbateBracciSuwaTovena2010Atiyah_primary.download')])

key='CrDarmon2009';b=entries[key]['original_entry']
a=b.replace('  2009.',r'''  2009.

\newblock In \emph{Explicit Methods in Number Theory}, \emph{Oberwolfach
  Reports}, 6\penalty0 (3):\penalty0 1871--1885, 2009.

\newblock Report DOI: \doi{10.4171/OWR/2009/33}.''',1)
add(key,a,'Add the published contribution pages 1871–1885 and explicitly identify the enclosing report DOI; preserve the linked author notes dated 31 July 2009 and their cited pagination.',[ev('Darmon2009_publisher_primary.download','https://ems.press/journals/owr/articles/4076'),ev('Darmon2009_final_publisher_report.pdf','https://ems.press/content/serial-article-files/46233?nt=1'),ev('CrDarmon2009_primary.download')],extra={'publisher_page_evidence':'Final publisher PDF p.29 begins printed p.1871 with the Darmon title; PDF p.43, printed p.1885, ends its references before the next contribution. The DOI identifies the full report, pp.1843–1920.'})

key='Parusinski1990E';b=entries[key]['original_entry']
a=b.replace("ski(1990)","ski(1994)")
a=a.replace(r'''\newblock Technical Report MPI/90-58, Max-Planck-Institut f{\"u}r Mathematik,
  1990.''',r'''\newblock \emph{Transactions of the American Mathematical Society},
  344\penalty0 (2):\penalty0 583--595, 1994.

\newblock \doi{10.1090/S0002-9947-1994-1160156-4}.

\newblock The cited edition is Technical Report MPI/90-58,
  Max-Planck-Institut f{\"u}r Mathematik, 1990; manuscript page and statement
  references use that edition.''')
add(key,a,'Add the verified 1994 journal publication and DOI; retain the exact cited MPI/90-58 manuscript and its page/statement references.',[ev('Parusinski1994_registry_primary.download','https://api.crossref.org/works/10.1090%2FS0002-9947-1994-1160156-4'),ev('Parusinski_author_publications_primary.download','https://math.univ-cotedazur.fr/u/parus/publications.html'),ev('Parusinski1990E_primary.download')])

key='CgzYZZ2011';b=entries[key]['original_entry']
a=b.replace('et~al.(2011)','et~al.(2013)').replace(r'''\newblock Gross--Zagier formula on Shimura curves.
\newblock Preprint, 6 November 2011.''',r'''\newblock \emph{The Gross--Zagier Formula on Shimura Curves}, volume~184 of
  \emph{Annals of Mathematics Studies}.

\newblock Princeton University Press, Princeton, 2013.

\newblock \doi{10.1515/9781400845644}.

\newblock The cited edition is the preprint dated 6 November 2011;
  page and statement references use that edition.''')
add(key,a,'Add the formal book, series, publisher, published/copyright year and DOI. Preserve the exact dated 6 November 2011 preprint already cited in the frozen source.',[ev('YZZ2013_publisher_primary.download','https://www.degruyterbrill.com/document/doi/10.1515/9781400845644/html'),ev('YZZ_author_publications_primary.download','https://math.mit.edu/~wz2113/math/pub.html'),ev('YZZ2013_registry_primary.download')],extra={'edition_scope':'Publisher citation and copyright year are 2013; its ebook release date is 11 November 2012. The source body cites the 6 November 2011 preprint, whose date is retained rather than replaced by either publication date.'})

key='Fujimoto1990AB';b=entries[key]['original_entry']
a=b.replace(r'\newblock \doi{10.14943/5135}.',r'''\newblock Collection DOI: \doi{10.14943/5135}.

\newblock Journal publication under the same title: \emph{Mathematische
  Annalen}, 288:\penalty0 559--570, 1990; \doi{10.1007/BF01444550}.

\newblock Page and statement references use the conference contribution
  on pp.~81--102 in the linked collection.''')
add(key,a,'Identify the existing DOI as the collection DOI, supply the verified same-author/same-title journal record and its article DOI, and preserve the conference pp.81–102 as the cited edition. No theorem-number or textual equivalence between editions is asserted.',[ev('Fujimoto1990AB_repository_primary.download'),ev('Fujimoto1990_publisher_primary.download','https://link.springer.com/article/10.1007/BF01444550'),ev('Fujimoto_journal_registry_primary.download')])

# Transcription and bibliographic-field corrections.
key='CrCastella2025';b=entries[key]['original_entry']
add(key,b.replace('Francesco Castella.','Francesc Castella.'),'Correct the author given name to Francesc, as on the author and publisher records; retain the title, citation key, journal DOI and dated cited edition.',[ev('CrCastella2025_crossref.json'),ev('Castella_author_publications_primary.download','https://web.math.ucsb.edu/~castella/')],kind='D23')
key='ErbanVanGorder2021';b=entries[key]['original_entry']
add(key,b.replace(r'7\penalty0 (25), 2021.',r'7, Article~25, 2021.'),'Represent 25 as the article number, matching the publisher citation, instead of placing it in the journal issue position.',[ev('Erban2021_publisher_primary.download','https://link.springer.com/article/10.1007/s40993-021-00240-6'),ev('ErbanVanGorder2021_crossref.json')])
key='Loj64';b=entries[key]['original_entry']
add(key,b.replace('  Scienze}, 18','  Scienze}, Series~3, 18'),'Supply the journal series number shown on the publisher archive and article title page; preserve volume, issue, pages, year and the exact article URL.',[ev('Loj64_publisher_primary.download','https://www.numdam.org/item/ASNSP_1964_3_18_4_449_0/'),ev('Loj64_primary.download')])
key='huber2022';b=entries[key]['original_entry']
add(key,b.replace(r'\href{https://doi.org/10.1017/9781009019729}{doi:10.1017/9781009019729}',r'\doi{10.1017/9781009019729}'),'Render the already verified DOI through the existing bibliography DOI macro, preserving the explicit separately paginated arXiv v8 theorem citation.',[ev('huber2022_crossref.json')],kind='D23')

# Versioned URLs match editions explicitly pinned in the frozen body.
versions={
'AbashevaDeev2024AB':('2303.10764','v1','19 March 2023'),
'Angella2018':('1705.10518','v2','10 November 2017'),
'BourdonClarkStankewicz2017':('1411.2742','v3','25 September 2015'),
'DlousskyTeleman2012AB':('1012.5247','v2','5 October 2011'),
'DlousskyTeleman2020D':('1803.07631','v2','28 February 2020'),
'HondaViaclovsky2025D':('2504.14420','v1','19 April 2025'),
'STW2017':('1503.04491','v2','8 December 2017'),
'xie2024algebraicity':('2202.09032','v1','18 February 2022'),
'miller2011':('1010.2431','v3','21 December 2011'),
}
for key,(arxiv,version,date) in versions.items():
    b=entries[key]['original_entry'];a=re.sub(r'(https://arxiv.org/(?:pdf|abs)/'+re.escape(arxiv)+r')(?:v\d+)?(?=\})',lambda m:m[1]+version,b)
    if key=='HondaViaclovsky2025D':
        note=r'\newblock Theorem~1.1 on p.~553 is cited from the journal edition; references marked arXiv version~1 use arXiv:'+arxiv+version+', '+date+'.'
    elif key=='STW2017':
        note=None
        a=a.replace('Earlier manuscript: arXiv:1503.04491v2, with separate pagination.','Earlier manuscript: arXiv:1503.04491v2, '+date+', with separate pagination.')
    else:note=r'\newblock Cited preprint edition: arXiv:'+arxiv+version+', '+date+'; preprint page and statement references use that edition.'
    if note:a+='\n\n'+note
    add(key,a,'Pin the bibliography URL to the arXiv edition explicitly cited in the frozen body and record its primary version-history date; preserve the published metadata and all existing citation locators.',[ev(key+'_cited_arxiv_primary.download','https://arxiv.org/abs/'+arxiv+version),ev(key+'_crossref.json')],extra={'edition_evidence_basis':'The frozen body explicitly names this arXiv version. This change binds the URL to that existing citation, and does not infer an edition from the newest version.'})

for key,arxiv in [('Engel2026','2609.38442'),('ViaclovskyLog2026','2610.39102'),('ViaclovskyTwo2026','2609.33785'),('Yang2026','2609.29666')]:
    b=entries[key]['original_entry'];a=b.replace('https://arxiv.org/abs/'+arxiv+'}', 'https://arxiv.org/abs/'+arxiv+'v1}')
    add(key,a,'Pin the URL to the v1 edition already explicitly named in this entry and in the supplied-source scope.',[ev(key+'_primary.download')])

dated={
'Demailly2012E':r'\newblock Cited author edition dated 21 June 2012; page and statement references use that edition.',
'herblot2012meromorphic':r'\newblock Cited author manuscript dated 18 April 2012; page and statement references use that edition.',
'EGFS25':r'\newblock Cited edition: arXiv:2507.15695v3, 27 March 2026; the first version appeared in 2025.',
}
for key,note in dated.items():
    b=entries[key]['original_entry'];name=key+('_cited_arxiv' if key=='EGFS25' else '')+'_primary.download'
    add(key,b+'\n\n'+note,'Make the exact dated linked edition explicit without changing its established citation key or the cited page/statement locators.',[ev(name)])
key='DLMFTheta2026';b=entries[key]['original_entry']
a=b.replace('  2026.', '  Version~1.2.8, released 15 September 2026. Accessed 21 November 2026.')
add(key,a,'Specify the exact current NIST release displayed in the consulted primary source and the access date; retain the cited chapter and equation identifiers.',[ev('DLMFTheta2026_primary.download','https://dlmf.nist.gov/')])
key='Sutherland2023CM';b=entries[key]['original_entry']
add(key,b.replace('Lecture 20, November 2023.','Lecture 20, 21 November 2023.'),'Complete the lecture date from the linked author/institution PDF front matter.',[ev('Sutherland2023CM_primary.download')])

def write_new(p,text):
    assert not p.exists(),p
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(text)

def dump(p,data):write_new(p,json.dumps(data,ensure_ascii=False,indent=2)+'\n')

def main():
    # Peer guards are reviewed as complete entries and merged once per key.
    peer_files=[
      ROOT/'agents/i_cont_provenance/S6_SERIES_PUBLISH_I_candidate17_bibliography_guards.json',
      ROOT/'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate17_bibliography_edits_guards.json',
    ]
    peer_receipts=[]
    for p in peer_files:
        if not p.exists():raise FileNotFoundError('Awaiting peer frozen guards: '+str(p))
        data=json.loads(p.read_text());batch=data['guards'] if isinstance(data,dict) else data
        peer_receipts.append({'path':str(p.relative_to(ROOT)),'sha256':sha(p.read_bytes()),'count':len(batch)})
        for g in batch:
            key=g.get('key') or g.get('citation_key')
            assert key in entries,key
            assert g['before']==entries[key]['original_entry'],key
            assert g['source_sha256']==EXPECTED,key
            assert re.findall(r'(?<!\\)\$[^$]*\$',g['before'])==re.findall(r'(?<!\\)\$[^$]*\$',g['after']),key
            g=dict(g);g.update({'key':key,'statement_id':'bib:'+key,'line':entries[key]['start_line'],'original_entry':g['before'],'proposed_entry':g['after'],'original_entry_sha256':sha(g['before']),'proposed_entry_sha256':sha(g['after']),'citation_key_preserved':True,'mathematical_events_added':0,'full_page_reading_credit_added':0})
            g['publication_evidence']=g.get('publication_evidence',g.get('primary_evidence',g.get('primary_sources',[])))+[{'path':str(p.relative_to(ROOT)),'sha256':sha(p.read_bytes()),'scope':'Frozen peer full-entry guard and its primary evidence; exact key '+key}]
            if isinstance(data,dict):
                peer_row=next(x for x in data['rows'] if x['key']==key)
                g['publication_evidence']+=peer_row.get('primary_sources',[])
                if peer_row.get('crossref_record'):
                    cr=peer_row['crossref_record'];cp=Path(cr['path'])
                    if not cp.is_absolute():cp=ROOT/cp
                    assert sha(cp.read_bytes())==cr['sha256'],key
                    g['publication_evidence'].append({**cr,'path':str(cp.relative_to(ROOT))})
            else:
                mp=ROOT/'agents/i_cont_provenance/S6_SERIES_PUBLISH_I_candidate17_bibliography_primary_metadata.json'
                g['publication_evidence'].append({'path':str(mp.relative_to(ROOT)),'sha256':sha(mp.read_bytes()),'scope':'Primary metadata and URLs for '+key})
            if key=='waldschmidt1979sigma':g['type']='D18/D23'
            guards.append(g)
    assert len(set(g['key'] for g in guards))==len(guards)
    guards.sort(key=lambda g:entries[g['key']]['start_line'])
    spec=importlib.util.spec_from_file_location('synctex',ROOT/'code/S6_SERIES_PUBLISH_synctex_batch.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    with m.Scanner(ROOT/'build/I_candidate17/S6_SERIES_PUBLISH_I.pdf') as sc:
        for g in guards:
            g['before_pages']=sorted(set(p for line in range(g['line'],g['line']+g['before'].count('\n')+1) for p in sc.pages(SOURCE,line)))
            g['page']=g['before_pages'][0]
            g['before_page_scope']='candidate17: '+EXPECTED
    archivedir=AREA/'candidate17_bibliography_full_entries'
    for g in guards:
        for phase in ['before','after']:
            p=archivedir/(g['key']+'_'+phase+'.tex');write_new(p,g[phase]+'\n');g[phase+'_full_entry_path']=str(p.relative_to(ROOT))
    proposal=source
    for g in guards:
        assert proposal.count(g['before'])==1,g['key'];proposal=proposal.replace(g['before'],g['after'])
    # Entire mathematical body is identical, and all content outside exact
    # bibliography entry spans is reconstructed byte-for-byte.
    assert source.split('\\begin{thebibliography}',1)[0]==proposal.split('\\begin{thebibliography}',1)[0]
    recovered=proposal
    for g in reversed(guards):
        assert recovered.count(g['after'])==1,g['key'];recovered=recovered.replace(g['after'],g['before'])
    assert recovered==source
    bundle={'candidate':17,'source_sha256':EXPECTED,'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'guard_count':len(guards),'guards':guards,'peer_batches':peer_receipts,'body_byte_identical':True,'exact_reverse_reconstruction':True,'complete_entry_math_sequences_identical':True,'whole_file_dollar_regex_used':False,'mathematical_events_added':0,'full_page_reading_credit_added':0,'status':'proposed; canonical source remains frozen'}
    dump(AREA/'S6_SERIES_PUBLISH_I_candidate17_bibliography_combined_guards.json',bundle)
    dump(AREA/'S6_SERIES_PUBLISH_I_candidate17_bibliography_own_notes.json',own_notes)
    print(json.dumps({'guard_count':len(guards),'own_guard_count':len(own_notes),'peer_batches':peer_receipts,'guards_sha256':sha((AREA/'S6_SERIES_PUBLISH_I_candidate17_bibliography_combined_guards.json').read_bytes())}))

if __name__=='__main__':main()
