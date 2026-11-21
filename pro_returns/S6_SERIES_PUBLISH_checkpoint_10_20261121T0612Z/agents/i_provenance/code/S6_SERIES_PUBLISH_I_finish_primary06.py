from pathlib import Path
import json,hashlib,datetime

ROOT=Path('/workspace/scratch/653608133b22');B=ROOT/'work/agents/i_provenance';L=B/'literature'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def H(p):return hashlib.sha256(p.read_bytes()).hexdigest()
sources=[
 ('Lin--Wang published 2010',L/'S6_SERIES_PUBLISH_I_LinWang2010.pdf','https://annals.math.princeton.edu/wp-content/uploads/annals-v172-n2-p03-p.pdf',[(3,912,'Equation(1.1), theta formula and G_z critical equation.'),(4,913,'Theorem1.3: at most five Green critical points; this is not the operative derivative equation.'),(10,919,'Full Lemma2.3 statement/proof, equations(2.7)--(2.8), G_z=-(zeta-t eta1-s eta2)/(4 pi).'),(11,920,'Continuation of Corollary2.4 and equianharmonic example; bounded contextual page.')],'LinWang2010'),
 ('Viaclovsky logarithmic arXiv2610.39102v1',L/'S6_SERIES_PUBLISH_I_Viaclovsky_log.pdf','https://arxiv.org/pdf/2610.39102v1',[(14,14,'Proposition4.7 statement and intrinsic-base/multiplicity proof.'),(15,15,'Completion of Proposition4.7: nonconstant period, countable markings and positive Kuranishi dimension.')],'Viaclovsky_log'),
 ('Viaclovsky two-parameter arXiv2609.33785v1',L/'S6_SERIES_PUBLISH_I_Viaclovsky_two_v1.pdf','https://arxiv.org/pdf/2609.33785v1',[(3,3,'Section2 elliptic model, nodal values and Lemma2.1 begins.'),(4,4,'Lemma2.1 completion and Lemma2.2 linearization proof.'),(5,5,'Lemma2.2 completion, explicit bundle-map orientation and Proposition2.3.'),(6,6,'Section3.1 equation(3.1), Proposition3.1 and full rank-one normalization quotient(3.3)--(3.4); c=lambda delta(0).'),(7,7,'Proposition3.1 completion, central translation and primitive specialization; beginning of the infinity root chart.'),(17,17,'Proposition6.1 and proof: canonical pullback, local nodal volume(6.2), root-coordinate cancellation.'),(18,18,'Proposition6.1 completion and anticanonical pencil; displayed coherent cohomology and deformation context.')],'Viaclovsky_two_v1'),
 ('Yang arXiv2609.29666v1',L/'S6_SERIES_PUBLISH_I_Yang_v1.pdf','https://arxiv.org/pdf/2609.29666v1',[(31,31,'Lemma6.6 full centralizer proof, Lemma6.7 affine-lift statement.'),(32,32,'Lemma6.7 proof, Remark6.8 (not a lemma), full Lemma6.9 norm-conjugacy proof and actual norm matrices.'),(37,37,'Proposition6.15 statement and parameter/shear/cusp/root collar proof begins.'),(38,38,'Proposition6.15 complete gluing and converse norm proof; Corollary6.16 automorphism group.'),(39,39,'Full Lemma6.17 and Theorem6.18: pair and absolute KS classes, exact critical-point forgetting argument.')],'Yang_v1'),
 ('AC2026 primary 108-page edition',L/'S6_SERIES_PUBLISH_I_AC26_primary.pdf','https://alpo.ge/s6.pdf',[(14,14,'Definition3.1 complete affine laws and cusp conditions; Theorem3.4(i) statement.'),(15,15,'Theorem3.4 remainder; Section3.1 modular zero facts, Lemma3.5 starts.'),(16,16,'Lemma3.5 proof and Proposition3.6 proof of Theorem3.4(i) begins.'),(17,17,'Proposition3.6 proof completes, including local orders, parabolic rigidity, uniqueness and cusp unit; Corollary3.7; Section3.2 begins.'),(39,39,'Section6.4, Definition6.6 positive cusp defect and Proposition6.7 statement.'),(40,40,'Proposition6.7 full surjectivity/gluing proof and Remark6.8; Section7 begins.')],'AC26'),
 ('Engel arXiv2609.38442v1',ROOT/'work/agents/provenance/literature/S6_SERIES_PUBLISH_Engel.pdf','https://arxiv.org/pdf/2609.38442v1',[(22,22,'Full Remark8.1 punctured-u family wording and Conjecture8.2 untwisted central-space statement.')],'Engel')
]
pages=[]
for name,pdf,url,ps,stem in sources:
 for n,printed,scope in ps:
  image=L/(f'S6_SERIES_PUBLISH_I_AC26_p{n:03d}.png' if stem=='AC26' else f'S6_SERIES_PUBLISH_I_{stem}_pdfp{n:03d}.png')
  assert image.exists(),image
  pages.append(dict(source=name,primary_url=url,pdf=str(pdf),pdf_sha256=H(pdf),pdf_page=n,printed_page=printed,image=str(image),image_sha256=H(image),actual_rendered_page_read=True,scope=scope))
receipt=dict(created_utc=now,reader='S6_SERIES_PUBLISH/provenance_inventory',mathematical_check_events=0,scope='Only the rendered pages listed were read. Source/page verification adds no independent mathematical check or full-article claim.',pages=pages)
rp=L/'S6_SERIES_PUBLISH_I_common_primary_locator_receipt.json';rp.write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n')

main=ROOT/'work/S6_SERIES_PUBLISH_I.tex';bib=ROOT/'work/S6_SERIES_PUBLISH_references.bib';s=main.read_text();bs=bib.read_text()
inline=r'''\bibitem[Lin and Wang(2010)]{LinWang2010}
Chang-Shou Lin and Chin-Lung Wang.
\newblock Elliptic functions, Green functions and the mean field equations on tori.
\newblock \emph{Annals of Mathematics}, 172(2):911--954, 2010.
\newblock \doi{10.4007/annals.2010.172.911}.
\newblock URL
\url{https://annals.math.princeton.edu/wp-content/uploads/annals-v172-n2-p03-p.pdf}.

'''
anchor=r'\bibitem[Viaclovsky(2026{\natexlab{a}})]{ViaclovskyLog2026}'
assert s.count(anchor)==1 and '{LinWang2010}' not in s[s.index('\\begin{thebibliography}'):]
mainchanges=[dict(id='I-LinWang-inline-entry',old=anchor,new=inline+anchor,expected_count=1,reason='Add exact opened publisher metadata and primary PDF. Critical equation is equation1.1 p912 / Lemma2.3 p919; Theorem1.3 p913 has the separate at-most-five scope.')]
for cid,old,new in [
 ('I-invA21-AC-def31','AC26 Definition 3.1',r'\cite[Definition~3.1, p.~14]{AC2026}'),
 ('I-invA21-AC-thm34','AC26 Theorem 3.4(i)',r'\cite[Theorem~3.4(i), p.~14; Proposition~3.6, pp.~16--17]{AC2026}'),
 ('I-invA21-AC-sec31','AC26 Section 3.1',r'\cite[Section~3.1, pp.~15--17]{AC2026}')]:
 assert s.count(old)==1,(cid,s.count(old));mainchanges.append(dict(id=cid,old=old,new=new,expected_count=1,reason='Replace plain source prose by the exact actually opened primary locator; no mathematical wording changes.'))
(B/'S6_SERIES_PUBLISH_I_primary_citation_guards_06.json').write_text(json.dumps(dict(source=str(main),source_sha256=H(main),created_utc=now,receipt=str(rp),changes=mainchanges),indent=2,ensure_ascii=False)+'\n')

entry=r'''@article{LinWang2010,
  author = {Lin, Chang-Shou and Wang, Chin-Lung},
  title = {Elliptic functions, Green functions and the mean field equations on tori},
  journal = {Annals of Mathematics},
  volume = {172},
  number = {2},
  pages = {911--954},
  year = {2010},
  doi = {10.4007/annals.2010.172.911},
  url = {https://annals.math.princeton.edu/wp-content/uploads/annals-v172-n2-p03-p.pdf},
  source_note = {Publisher metadata and official PDF opened 21 November 2026. Actual rendered pages 912,913,919,920 read; equation1.1 p912 and full Lemma2.3 p919 supply the Green critical equation. Theorem1.3 p913 states at most five critical points. No full-article or independent mathematical check is claimed. PDF SHA256 f3b3798d234400c81d5a9e1e1ab79931938d5f3438d992af555e92175e42f16f.},
  verification = {verified at listed scope}
}

'''
assert 'LinWang2010' not in bs
ba='@misc{ViaclovskyLog2026,';assert bs.count(ba)==1
bchanges=[dict(id='I-LinWang-shared-entry',old=ba,new=entry+ba,expected_count=1,reason='Exact primary publication record and bounded current reading scope.')]
notes={
'AC2026':'21 November 2026: actual primary PDF pages14--17 and39--40 read. Definition3.1 p14; Theorem3.4(i) p14; Section3.1 pp15--17 and full Proposition3.6 proof pp16--17; Section6.4, Definition6.6 and Proposition6.7 pp39--40. Receipt S6_SERIES_PUBLISH_I_common_primary_locator_receipt.json. No new mathematical event.',
'ViaclovskyLog2026':'21 November 2026: actual arXiv2610.39102v1 rendered pages14--15 read, full Proposition4.7 intrinsic-base/multiplicity and nonconstant-period/countability argument. Separate previous receipt covers Section2 equations2.1--2.2 p3 and2.7,2.11--2.12 p4. No new mathematical event.',
'ViaclovskyTwo2026':'21 November 2026: actual arXiv2609.33785v1 rendered pages3--7,17--18 read. Section2 elliptic/linearization maps; Proposition3.1 pp6--7 with equation3.1 and exact rank-one quotient c=lambda delta(0); full Proposition6.1 pp17--18 with local nodal volume6.2. The actual received PDF SHA256 is effd22502f2eb17619036fa60dd81f2df0c960e8a20af5bb43d77135892c4578; earlier historical source-build hashes are retained separately. No new mathematical event.',
'Yang2026':'21 November 2026: actual arXiv2609.29666v1 pages31,32,37,38,39 read. Lemmas6.6--6.7 and6.9 pp31--32;6.8 is a remark, p32; Proposition6.15 pp37--38; Lemma6.17 and Theorem6.18 p39. Exact centralizer, affine, norm, collar and KS scopes only. PDF SHA2563c982a29d95439e1a9aafe3ea96d5bd0dd02c8e86a0925f6ba560d5feef024e6. No new mathematical event.',
'Engel2026':'21 November 2026: actual rendered p22 read again, including full Remark8.1 and Conjecture8.2. The punctured-u family wording and the specified untwisted ruled-surface central model are recorded separately from the receiving fixed-sphere-data double-cover obstruction. No new mathematical event.'}
for k,note in notes.items():
 old='@misc{'+k+',\n';assert bs.count(old)==1
 new=old+'  current_run_common_locators = {'+note+'},\n'
 bchanges.append(dict(id='I-'+k+'-common-locators',old=old,new=new,expected_count=1,reason='Insert a bounded current-run reading field before existing metadata, with a trailing comma; preserve historical verification notes.'))
# The LinWang insertion shares the Viaclovsky header with the scope insertion.
# Sequential order is intentional: the old header remains unique after insertion.
(B/'S6_SERIES_PUBLISH_I_shared_bib_guards_06.json').write_text(json.dumps(dict(source=str(bib),source_sha256=H(bib),created_utc=now,changes=bchanges,application_order='Sequential; insertion retains the unique Viaclovsky header for its following metadata guard.'),indent=2,ensure_ascii=False)+'\n')
print(json.dumps(dict(actual_pages=len(pages),main_guards=len(mainchanges),shared_guards=len(bchanges),receipt=str(rp)),indent=2))
