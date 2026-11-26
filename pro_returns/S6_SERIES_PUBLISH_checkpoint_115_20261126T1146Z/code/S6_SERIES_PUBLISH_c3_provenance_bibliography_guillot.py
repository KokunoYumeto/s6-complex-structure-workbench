#!/usr/bin/env python3
"""Exact Guillot metadata additions, IDs 147–148; no shared writes."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation3_provenance'
main=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
def block(key):
    match=re.search(r'\\bibitem(?:\[[^\]]*\])?\{'+re.escape(key)+r'\}',main)
    assert match,key
    a=match.start()
    b=main.index(r'\bibitem',a+1)
    return main[a:b].rstrip()
def tsv(name,rows):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,list(rows[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
old2019=block('Guillot2019')
new2019=old2019.replace(r'\newblock URL \url{https://arxiv.org/pdf/1603.02288}.',r'\newblock arXiv:1603.02288v2, 5 August 2019.'+'\n'+r'\newblock URL \url{https://arxiv.org/pdf/1603.02288v2}.')
assert old2019!=new2019
old2024=block('Guillot2024')
new2024=r'''\bibitem[Guillot(2024)]{Guillot2024}
Adolfo Guillot.
\newblock On the singularities of complete holomorphic vector fields in
dimension two.
\newblock In F.~Cano, J.~L.~Cisneros-Molina, L\^e D\~ung Tr\'ang,
and J.~Seade, editors, \emph{Handbook of Geometry and Topology of
Singularities VI: Foliations}, pages 1--37. Springer, Cham, 2024.
\newblock \doi{10.1007/978-3-031-54172-8_1}.
\newblock Author preprint, 32 pages; theorem numbers and page citations
refer to this preprint.
\newblock URL
\url{https://www.matem.unam.mx/~guillot/guillot-singularities.pdf}.'''
rows=[]
for num,key,old,new,reason in [(147,'Guillot2019',old2019,new2019,'Pin the exact arXiv v2 source whose margin gives 5 August 2019; retain the published journal, article number and DOI.'),(148,'Guillot2024',old2024,new2024,'The publisher lists the chapter as pp.1–37, first online 21 June 2024. The opened author preprint has 32 pages and its own theorem numbering; name that layout for the body locators and complete the publisher/editor data.')]:
    rows.append(dict(change_id=f'II-C3-PROV-{num}',type='D18',statement_id='bib:'+key,old_location=key+' bibliography entry',old_page='source; final page pending',new_location='same entry',new_page='integrated build pending',old_text=old,new_text=new,reason=reason,review_status='Publisher and exact-version metadata read; mathematical loci separately opened/read by continuation3 conductor; parent admission pending.'))
tsv('S6_SERIES_PUBLISH_c3_provenance_bibliography_guillot_edits.tsv',rows)
now=datetime.now(timezone.utc).isoformat()
sources=[]
for key,filename,url,version,loc,scope in [
 ('Guillot2019','Guillot2019_arxiv_v2.pdf','https://arxiv.org/pdf/1603.02288v2','arXiv:1603.02288v2, 5 August 2019','Main Theorem and clarification p.2; Definition 5 and Lemma 6/proof pp.4–5; Proposition 22 p.25','The conductor agent read the complete curve-pole lemma and its proof, the main theorem/clarification and the classification proposition statement. The bibliography change pins that exact layout.'),
 ('Guillot2024','Guillot2024_author.pdf','https://www.matem.unam.mx/~guillot/guillot-singularities.pdf','32-page author preprint of the 2024 chapter; PDF metadata creation date 4 July 2024, not a printed version date','Definition 2.3 p.7; Propositions 2.1–2.2/proofs pp.4–7; Theorem 3.3/proof p.9; Theorem 9.2 statement p.28','The conductor agent read the complete semicompleteness statements and proofs specified here and the theorem statement at p.28. Publisher metadata identifies the published 37-page chapter and the author first page expressly identifies the file as a preprint of it.')]:
    p=Path('/tmp/S6_SERIES_PUBLISH_c3_conductor_primary')/filename
    sources.append(dict(source_id='II-C3-BIB-'+key,url=url,publisher_url='https://link.springer.com/chapter/10.1007/978-3-031-54172-8_1' if key=='Guillot2024' else 'https://doi.org/10.1016/j.aim.2019.106742',version=version,exact_locus=loc,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size,own_paraphrase=scope,reader='Provenance agent: title margin, author preprint statement and metadata; conductor agent: complete specified mathematical loci.',date_utc=now))
tsv('S6_SERIES_PUBLISH_c3_provenance_bibliography_guillot_sources.tsv',sources)
hopf=ROOT.parents[1]/'tmp/c3_provenance_primary/AbashevaDeev_v1.pdf'
tsv('S6_SERIES_PUBLISH_c3_provenance_hopf_curve_source.tsv',[dict(source_id='II-C3-HOPF-CURVES',url='https://arxiv.org/pdf/2303.10764v1',version='arXiv:2303.10764v1, 19 March 2023',exact_locus='§2.2.2 p.4; §2.2.6 p.5; §2.3.1 p.8',sha256=hashlib.sha256(hopf.read_bytes()).hexdigest(),bytes=hopf.stat().st_size,established_scope='The nondiagonal primary case has exactly the axis curve; the nonresonant diagonal case has exactly the two square-zero elliptic axes; the resonant diagonal case has an elliptic fibration with smooth possibly multiple fibres. Every secondary Hopf surface is a free finite quotient of a primary one.',precise_limit='In the resonant paragraph the source states that all elliptic curves are fibres. It does not phrase the assertion for every compact irreducible curve, so the horizontal-intersection application remains explicit.',application='For the resonant fibration, a horizontal curve has positive intersection with a general fibre, contrary to b2=0, so each irreducible curve is a reduced smooth elliptic fibre. For the finite étale quotient π:H′→H, inverse images are disjoint unions of those elliptic curves; quotient by a component stabilizer gives an étale elliptic cover of C. Disjointness descends, and (π*C)^2=deg(π)C^2=0 gives square zero.',reading_extent='Read the complete three cited numbered paragraphs and their surrounding cases; root P248 integration is separate.',date_utc=now)])
print('Prepared bibliography IDs 147–148 and exact Hopf source/application record; shared source unchanged.')
