from pathlib import Path
import re,json,hashlib,datetime
from S6_SERIES_PUBLISH_editing import Editor

r=Path(__file__).resolve().parents[1];ed=Editor('I')
keys=['AtiyahSinger1968IIIE','BS76','CrGross1991','HS53','Illman1972']
archive=[]
for key in keys:
    ms=list(re.finditer(r'\\bibitem\[(.*?)\]\{([^}]+)\}',ed.text,re.S))
    i=next(i for i,m in enumerate(ms) if m[2]==key);m=ms[i]
    b=ms[i+1].start() if i+1<len(ms) else ed.text.index(r'\end{thebibliography}',m.start())
    old=ed.text[m.start():b]
    new,n=re.subn(r'\\newblock URL\s*\\url\{[^}]+\}\.\s*','',old)
    assert n==1,key
    if key=='CrGross1991':new=new.rstrip()+'\n\n'+r'\newblock \doi{10.1017/CBO9780511526053.009}.'+'\n\n'
    if key=='AtiyahSinger1968IIIE':new=new.replace('The index of elliptic operators: Iii.','The index of elliptic operators. III.')
    ed.replace(old,new,'D18','Use the existing publisher/DOI or thesis imprint as the bibliography reference, and move a third-party scan URL to source-retrieval provenance. The consulted edition and all mathematical locators remain unchanged.',key)
    archive.append({'key':key,'old':old,'new':new})

key='CgzYZZ2011'
ms=list(re.finditer(r'\\bibitem\[(.*?)\]\{([^}]+)\}',ed.text,re.S));i=next(i for i,m in enumerate(ms) if m[2]==key);m=ms[i]
b=ms[i+1].start() if i+1<len(ms) else ed.text.index(r'\end{thebibliography}',m.start())
old=ed.text[m.start():b]
new=r'''\bibitem[Yuan et~al.(2011)Yuan, Zhang, and Zhang]{CgzYZZ2011}
Xinyi Yuan, Shou-Wu Zhang, and Wei Zhang.

\newblock Gross--Zagier formula on Shimura curves.
\newblock Preprint, 6 November 2011.

'''
ed.replace(old,new,'D18','Identify the exact author-upload preprint whose pages 218--219 and Theorem 7.1.2 are cited; retain the directly opened author-upload URL and later-book metadata in source provenance.',key)
archive.append({'key':key,'old':old,'new':new})
ed.save()

bp=r/'S6_SERIES_PUBLISH_references.bib';before=bp.read_text();s=before
for key in keys:
    m=re.search(r'@\w+\{'+re.escape(key)+r',',s);assert m,key
    a=m.start();end=s.find('\n}',m.end())+2;entry=s[a:end];assert end>1
    new=entry.replace('  url = {','  retrieval_url = {')
    if key=='CrGross1991' and '  doi =' not in new:
        new=new.replace('  year = {1991},','  year = {1991},\n  doi = {10.1017/CBO9780511526053.009},')
    s=s[:a]+new+s[end:]
bp.write_text(s)
receipt={
 'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'source_sha256':hashlib.sha256(ed.text.encode()).hexdigest(),
 'shared_bib_before_sha256':hashlib.sha256(before.encode()).hexdigest(),
 'shared_bib_after_sha256':hashlib.sha256(s.encode()).hexdigest(),
 'entries':archive,
 'primary_metadata':[
  {'key':'AtiyahSinger1968IIIE','url':'https://annals.math.princeton.edu/1968/87-3/p07','ref':'turn121419686view0','scope':'Publisher title, pages 546--604, volume87 issue3 and DOI10.2307/1970717 opened. Mathematical theorem loci rely on their separately recorded primary-page readings.'},
  {'key':'CrGross1991','url':'https://www.cambridge.org/core/books/abs/lfunctions-and-arithmetic/kolyvagins-work-for-modular-elliptic-curves/794AFEFA22963B8A4FC69216FF7B711C','ref':'turn624942136view2','scope':'Publisher chapter pp235--256, print1991 and DOI10.1017/CBO9780511526053.009 opened. Author bibliography confirms the supplied title form; no new mathematical theorem check.'},
  {'key':'CgzYZZ2011','url':'https://www.researchgate.net/publication/267551160_Gross-Zagier_Formula_On_Shimura_Curves','refs':['turn377743447view0','turn135062874view0','turn700623754view0'],'scope':'Explicit author-upload attribution and manuscript date6November2011 opened. Read section7.1.1 pp218--219: base-relative height divides by extension degree; bilinear height uses the sum difference; Theorem7.1.2 identifies the polarization/Poincare pairing. Receiving notation sends source base F to K and source field K to L. The diagonal pairing is twice the line height, and passing from absolute to the imaginary-quadratic relative convention multiplies by2, giving the receiving factor4.'}
 ],
 'limits':'No whole-book/article reading, new independent result check or new computation is claimed. Source scan URLs remain retrieval provenance. The later published book is not substituted for the dated preprint or its pagination.',
 'YZZ_erratum_scope':{'url':'https://faculty.bicmr.pku.edu.cn/~yxy/preprints/erratum-GZSC.pdf','ref':'turn392930873view0','scope':'Opened the author-listed June2026 erratum and inspected the correction list through its published-page219 item56. That item concerns a later local-intersection expression; no pagination identity with preprint p219 is asserted. The receiving height convention was checked directly in the cited preprint.'}
}
(r/'records/S6_SERIES_PUBLISH_I_bibliography_link_receipt.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n')
