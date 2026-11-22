from pathlib import Path
import datetime as dt, hashlib, json, urllib.request

R=Path(__file__).resolve().parents[1]
out=R/'records/S6_SERIES_PUBLISH_II_bibliography_primary_04.json'
assert not out.exists()
rows=[]
for doi in ['10.1007/s10455-020-09744-3','10.2969/aspm/06010051']:
    url='https://api.crossref.org/works/'+doi
    item=dict(url=url,utc=dt.datetime.now(dt.timezone.utc).isoformat())
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'S6-bibliography-verification/1.0'})
        with urllib.request.urlopen(req,timeout=30) as response:
            b=response.read()
        m=json.loads(b)['message']
        item.update(response_sha256=hashlib.sha256(b).hexdigest(),response_bytes=len(b),
                    fields={k:m[k] for k in ['DOI','title','author','container-title','volume','issue','page','publisher','published','published-print','published-online','URL','type','editor'] if k in m})
    except Exception as e:
        item.update(error=type(e).__name__+': '+str(e),metadata_credit=False)
    rows.append(item)
record=dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),crossref=rows,
 primary_web_metadata_actually_read=[
  dict(url='https://link.springer.com/article/10.1007/s10455-020-09744-3',ref='turn403931273view0',scope='Title, author Michael Albanese, online publication6November2020, volume59 pages179--195 journal year2021. Only these visible metadata fields are credited; the combined long return was truncated elsewhere.'),
  dict(url='https://www.mathe8.uni-bayreuth.de/en/team/prof-fabrizio-catanese/pdf/index.html',ref='turn403931273view2',scope='Author publication list item92: Deformation types of real and complex manifolds; Chen--Chow Memorial Conference, Contemporary trends in algebraic geometry and algebraic topology(Tianjin2000), pp195--238, Nankai Tracts Math5, World Scientific, River EdgeNJ,2002.'),
  dict(url='https://www.iag.uni-hannover.de/en/forschung/publikationen/publikation-detail/publications/elliptic-surfaces',ref='turn776370547view2',scope='Author institution publication metadata: M.Schuett and T.Shioda, Elliptic Surfaces, Advanced Studies in Pure Mathematics60(2010),51--160, arXiv0907.0298.'),
  dict(url='https://www.math.ru.nl/onderzoek/reports/reports1999.html',ref='turn756153350view1',scope='Official institute catalogue entry9907: J.H.M.Steenbrink, Cup products and mixed Hodge structures, February1999. Catalogue metadata only; no assertion that the report file was read or byte-compared.'),
  dict(url='https://arxiv.org/abs/1912.09719v1',ref='turn756153350view2',scope='Exact v1 submitted20December2019; authorsChristianLehn,SoenkeRollenske,CarenSchinko; journal reference Differential Geometry and its Applications57(2018),121--137; related DOI10.1016/j.difgeo.2017.10.015. Exact attached-source/v1 byte identity is separately proved in primary03.')],
 prior_exact_version_identification=dict(path='records/S6_SERIES_PUBLISH_II_bibliography_primary_03.json',sha256=hashlib.sha256((R/'records/S6_SERIES_PUBLISH_II_bibliography_primary_03.json').read_bytes()).hexdigest()),
 limitations=['DOI resolver for Albanese failed in the web tool; direct Springer article metadata was accessible.',
              'DOI resolver for Schuett--Shioda redirected to inaccessible Project Euclid in the web tool; author institution metadata and the direct Crossref lookup are recorded independently.',
              'Numdam Greb landing page returned502; exact DOI metadata was already obtained in primary03.',
              'An initial read used the wrong local master-bibliography filename and failed before reading or changing a file; the actual S6_SERIES_PUBLISH_references.bib was then read.',
              'The five attached TeX edition identities are exact source-byte comparisons from primary03, not inferred from titles. Published-edition metadata does not substitute for the actually read preprint loci.'],
 source_changes=0,events_added=0,required_checks_completed=0,downloaded_primary_publications_retained=False)
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
