#!/usr/bin/env python3
"""Capture primary bibliography metadata without reading target proofs."""
import concurrent.futures,datetime,hashlib,json,pathlib,re,urllib.request
import fitz
ROOT=pathlib.Path(__file__).resolve().parents[1]
AREA=ROOT/'agents/continuation_infra/candidate17_bibliography_audit'
DELEGATED=set('agboola2006 bertolin2022 bost2009 callSilverman1993 Cartan1952B_AB CrCremonaSiksek2006 demarco2017 Gauduchon1985 Grauert1963ErratumD CrJetchev2008 MazurSteinTate2006 McHugh2018 nguyen2023 CrRubin1999 SchroeerSiebert2002Root Shin2015 CgzStein2007 waldschmidt1979sigma waldschmidt1988periodrank waldschmidt1988theta'.split())
EXTRA={
'Darmon2009_publisher_report':'https://publications.mfo.de/bitstream/handle/mfo/3134/OWR_2009_33.pdf?isAllowed=y&sequence=1',
'Fujimoto1990_publisher':'https://link.springer.com/article/10.1007/BF01444550',
'Parusinski1994_registry':'https://api.crossref.org/works/10.1090%2FS0002-9947-1994-1160156-4',
'Abate2013_registry':'https://api.crossref.org/works/10.4171%2FRMI%2F730',
'YZZ2013_registry':'https://api.crossref.org/works/10.1515%2F9781400845644',
'Illman1973_author_summary':'https://www.numdam.org/item/AIF_1973__23_2_87_0/',
'IKN2005E_publisher':'https://www.ms.u-tokyo.ac.jp/journal/abstract_e/jms120101_e.html',
'IKN2007ErratumE_publisher':'https://www.ms.u-tokyo.ac.jp/journal/abstract_e/jms140105_e.html',
'KKN2008Root_publisher':'https://www.ms.u-tokyo.ac.jp/journal/abstract_e/jms150104_e.html',
'Loj64_publisher':'https://www.numdam.org/item/ASNSP_1964_3_18_4_449_0/',
'Pinkham1974Root_publisher':'https://www.numdam.org/item/AST_1974__20__1_0/',
'Shioda90_repository':'https://rikkyo.repo.nii.ac.jp/records/10027',
'Fujimoto1990AB_repository':'https://eprints.lib.hokudai.ac.jp/repo/huscap/all/5450/16.pdf',
'Herblot_author_publications':'https://webusers.imj-prg.fr/~mathilde.herblot/recherche.html',
'Movasati_author_books':'https://w3.impa.br/~hossein/books.html',
'Darmon_author_publications':'https://www.math.mcgill.ca/darmon/pub/pub.html',
'Castella_author_publications':'https://web.math.ucsb.edu/~castella/',
}
def fetch(item):
    key,url=item
    target=AREA/(key+'_primary.download')
    receipt={'key':key,'url':url,'purpose':'Bibliographic title, author, edition and publication metadata only; mathematical events added0.'}
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (bibliography metadata verification)'})
        with urllib.request.urlopen(req,timeout=25) as r:
            raw=r.read(50_000_001)
            if not raw:raise ValueError('empty response body: HTTP success alone supplies no primary evidence')
            if len(raw)>50_000_000:raise ValueError('source exceeds50MB metadata retrieval limit')
            receipt.update({'http_status':r.status,'resolved_url':r.url,'content_type':r.headers.get('Content-Type')})
        if target.exists():raise FileExistsError(target)
        target.write_bytes(raw)
        receipt.update({'status':'retrieved','bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'path':str(target.relative_to(ROOT))})
        if raw.startswith(b'%PDF-'):
            d=fitz.open(stream=raw,filetype='pdf');receipt['pdf_pages']=len(d)
            receipt['first_page_metadata_excerpt']=d[0].get_text()[:420]
        elif 'json' in (receipt.get('content_type') or ''):
            data=json.loads(raw);msg=data.get('message',data)
            receipt['metadata_fields']={k:msg.get(k) for k in ['title','author','container-title','publisher','volume','issue','page','published','published-print','published-online','DOI']}
    except Exception as e:receipt.update({'status':'unresolved','error':str(e)})
    return receipt
def main():
    inventory=json.loads((ROOT/'agents/continuation_infra/S6_SERIES_PUBLISH_I_candidate17_bibliography_inventory.json').read_text())
    items=[]
    for e in inventory['entries']:
        if e['key'] in DELEGATED or e['doi'] or e['key']=='huber2022':continue
        if e['urls']:items.append((e['key'],e['urls'][0]))
    items.extend(EXTRA.items())
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:rows=list(pool.map(fetch,items))
    out=AREA/'supplemental_primary_retrieval_receipt.json'
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps({'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':inventory['source_sha256'],'rows':rows,'mathematical_events_added':0},ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'retrieved':sum(x['status']=='retrieved' for x in rows),'count':len(rows),'unresolved':[{k:v for k,v in x.items() if k in ['key','error']} for x in rows if x['status']!='retrieved'],'receipt':str(out.relative_to(ROOT))}))
if __name__=='__main__':main()
