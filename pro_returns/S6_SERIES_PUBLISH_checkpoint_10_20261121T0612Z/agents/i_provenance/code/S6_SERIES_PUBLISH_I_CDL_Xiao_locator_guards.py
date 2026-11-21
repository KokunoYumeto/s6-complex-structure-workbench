from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re
ROOT=Path('/workspace/scratch/653608133b22')
B=ROOT/'work/agents/i_provenance'; L=B/'literature'
source=ROOT/'work/S6_SERIES_PUBLISH_I.tex'; bib=ROOT/'work/S6_SERIES_PUBLISH_references.bib'
s=source.read_text(); bs=bib.read_text()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
now=datetime.now(timezone.utc).isoformat()
def page(key,pdfn,printed,scope):
 p=L/f'S6_SERIES_PUBLISH_I_{key}_pdf{pdfn:03d}.png'
 return dict(pdf_page=pdfn,printed_page=printed,image=str(p),image_sha256=sha(p),actually_viewed=True,scope=scope)
receipt={'created_utc':now,'kind':'Primary bibliography and exact locator verification; no mathematical check event',
 'source_sha256':sha(source),'sources':[
 {'key':'CDL24','url':'https://sites.lsa.umich.edu/idolga/wp-content/uploads/sites/1334/2024/08/EnriquesOne.pdf','pdf':str(L/'S6_SERIES_PUBLISH_I_CDL2024.pdf'),'pdf_sha256':sha(L/'S6_SERIES_PUBLISH_I_CDL2024.pdf'),'edition':'Author manuscript, 19 April 2024; title page actually viewed',
 'pages':[page('CDL2024',1,None,'Title, authors and manuscript date'),page('CDL2024',159,143,'Proposition 0.9.2: relative Picard/Brauer exact sequence and its hypotheses'),page('CDL2024',386,370,'Opening of Section 4.2: Br(C)=0 for the stated smooth-curve/local bases and Picard consequence'),page('CDL2024',461,445,'Lemma 4.7.8; exact sequence (4.7.4); Theorem 4.7.9 and opening of proof'),page('CDL2024',462,446,'Continuation of Theorem 4.7.9 proof'),page('CDL2024',463,447,'End of Theorem 4.7.9 proof and neighboring torsor interpretation')],
 'receiving_scope':'B.3.6 uses the vanishing over a complex curve function field and the localization surjection for the nontrivial Jacobian j=1728t. Sequence (4.7.4) has cokernel Tors H2(C,E); Theorem 4.7.9 kills that torsion. B.3.7 uses the relative Picard/Brauer sequence over C. No vanishing of the entire H2(C,E) is inferred.',
 'publisher_metadata':{'url':'https://link.springer.com/book/10.1007/978-981-96-1214-7','opened_web_ref':'turn737362645view0','title':'Enriques Surfaces I','authors':['François Cossec','Igor Dolgachev','Christian Liedtke'],'publisher':'Springer Singapore','edition':2,'year':2025,'doi':'10.1007/978-981-96-1214-7','ebook_date':'2025-04-19','pagination':'XXI, 681','scope':'Publisher metadata opened; no published-page locator is asserted. All operative numbered/page locators above belong to the 19 April 2024 manuscript.'}},
 {'key':'Xiao91','url':'https://archive.mpim-bonn.mpg.de/id/eprint/2953/1/preprint_1991_30.pdf','pdf':str(L/'S6_SERIES_PUBLISH_I_Xiao1991.pdf'),'pdf_sha256':sha(L/'S6_SERIES_PUBLISH_I_Xiao1991.pdf'),'edition':'Max-Planck-Institut für Mathematik preprint MPI/91-30, 1991; title/report number actually viewed',
 'pages':[page('Xiao1991',1,None,'Title, author, institution and report number'),page('Xiao1991',2,None,'Blank reverse title page; no mathematical claim'),page('Xiao1991',16,14,'Lemma 3.3 and Theorem 3.4 statement and proof opening'),page('Xiao1991',17,15,'Theorem 3.4 proof conclusion and order-refinement remark'),page('Xiao1991',23,21,'Section 4: generic torsor/finite-translation correspondence; exact sequence (4); nontrivial-Jacobian localization surjectivity; locally trivial torsor interpretation')],
 'receiving_scope':'B.3.6 uses the generic torsor interpretation, finite translating twists and the local-to-global map for a nontrivial Jacobian. Exact equation (4) and the immediately preceding/following explanation are on p.21. Theorem 3.4 is on pp.14–15. No full-paper review or p.25 verification is claimed in this current receipt.'}],
 'mathematical_check_events_added':0,'presentation_QA_events_added':0}
(L/'S6_SERIES_PUBLISH_I_CDL_Xiao_locator_receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
changes=[]
def add(id,old,new,reason):
 assert s.count(old)==1,(id,s.count(old))
 changes.append(dict(id=id,old=old,new=new,reason=reason))
add('I-CDL-H2-locator',r'''$H^2(K,E)=0$, as in
\cite[Lemma 4.7.8]{CDL24}.''',r'''$H^2(K,E)=0$, as in
\cite[Lemma~4.7.8, p.~445]{CDL24}.''','Actually viewed 19 April 2024 manuscript p.445; add exact locator only.')
add('I-CDL-localization-locator',r'''This is the combination of exact
sequence (4.7.4) and Theorem 4.7.9
of \cite{CDL24}; the same surjectivity
and its geometric fibre-twist
interpretation are given in
\cite[Section 4, equation (4)]{Xiao91}.''',r'''This is the combination of exact
sequence~(4.7.4) and Theorem~4.7.9
in \cite[p.~445]{CDL24}; the same surjectivity
and its geometric fibre-twist
interpretation are given in
\cite[Section~4, equation~(4), p.~21]{Xiao91}.''','CDL p.445 and Xiao p.21 actually viewed; the existing localization assertion and its nontrivial-Jacobian hypothesis are unchanged.')
add('I-Xiao-torsor-locator',r'''globally. The local translation gluing specifies $V$ as in
\cite[Sections 3--4]{Xiao91}.''',r'''globally. The local translation gluing specifies $V$ as in
\cite[Theorem~3.4, pp.~14--15; Section~4, p.~21]{Xiao91}.''','Replace broad section range by actually viewed theorem and torsor/cocycle pages; retain the entire receiving local-model argument.')
add('I-CDL-relative-Picard-locator',r'''relative Picard consequence of
\cite[Proposition 0.9.2 and the opening
of Section 4.2, p.370]{CDL24}.''',r'''relative Picard consequence of
\cite[Proposition~0.9.2, p.~143; Section~4.2, p.~370]{CDL24}.''','Actually viewed both separate locators; p.370 alone does not locate Proposition 0.9.2.')
add('I-CDL-exact-cited-edition',r'''\newblock Enriques surfaces {I}, 2024.

\newblock URL
  \url{https://sites.lsa.umich.edu/idolga/wp-content/uploads/sites/1334/2024/08/EnriquesOne.pdf}.''',r'''\newblock \emph{Enriques surfaces {I}}. Author manuscript, 19 April 2024
  (the cited pagination).
\newblock Second edition: Springer Singapore, 2025.
  \doi{10.1007/978-981-96-1214-7}.
\newblock Manuscript URL
  \url{https://sites.lsa.umich.edu/idolga/wp-content/uploads/sites/1334/2024/08/EnriquesOne.pdf}.''','Title-page date and cited manuscript pagination actually verified; separately identify the publisher-confirmed 2025 second edition without transferring its pages.')
(B/'S6_SERIES_PUBLISH_I_primary_citation_guards_08.json').write_text(json.dumps({'source_sha256':sha(source),'receipt':str(L/'S6_SERIES_PUBLISH_I_CDL_Xiao_locator_receipt.json'),'changes':changes,'mathematical_check_events_added':0},ensure_ascii=False,indent=2)+'\n')
bchanges=[]
for key in ['CDL24','Xiao91']:
 m=re.search(r'(?ms)^@[^\n]+\{'+key+r',\n.*?^}\n',bs)
 assert m,key
 old=m.group()
 fields=(
 '  current_run_source = {19 April 2024 author manuscript, title page and exact cited pages actually viewed on 21 November 2026},\n'
 '  current_run_additional_locators = {Proposition 0.9.2 p.143; Section 4.2 p.370; Lemma 4.7.8, sequence (4.7.4), Theorem 4.7.9 p.445; proof pp.445--447},\n'
 '  published_edition = {Second edition, Springer Singapore, 2025; DOI 10.1007/978-981-96-1214-7; publisher metadata opened, published pagination not used},\n'
 '  current_run_receipt = {S6_SERIES_PUBLISH_I_CDL_Xiao_locator_receipt.json; bibliography verification only, no mathematical check event}\n'
 if key=='CDL24' else
 '  current_run_source = {Official MPIM scan, title and report number MPI/91-30 actually viewed on 21 November 2026},\n'
 '  current_run_additional_locators = {Theorem 3.4 pp.14--15; Section 4 equation (4), generic torsor and finite-translation interpretation, nontrivial-Jacobian surjectivity p.21},\n'
 '  current_run_receipt = {S6_SERIES_PUBLISH_I_CDL_Xiao_locator_receipt.json; current scope is these pages only, not the historical full-paper or p.25 scope; no mathematical check event}\n')
 new=old[:-2].rstrip()+',\n'+fields+'}\n'
 bchanges.append(dict(id='I-bib-CDL-Xiao-'+key,old=old,new=new,reason='Add precise current-run primary scope while preserving historical receipt text in its original fields.'))
(B/'S6_SERIES_PUBLISH_I_shared_bib_guards_08.json').write_text(json.dumps({'bib_sha256':sha(bib),'changes':bchanges,'mathematical_check_events_added':0},ensure_ascii=False,indent=2)+'\n')
md='''# CDL and Xiao primary locator receipt\n\nBoth primary PDFs and the exact pages below were actually viewed on 21 November 2026. No mathematical check event was added.\n\n| Key | Cited edition | Actually viewed operative pages | Receiving use |\n|---|---|---|---|\n| CDL24 | Author manuscript dated 19 April 2024 | Proposition 0.9.2 p.143; §4.2 p.370; Lemma 4.7.8, sequence (4.7.4), Theorem 4.7.9 p.445; proof pp.445–447 | Relative Picard/Brauer obstruction and localization for the nontrivial elliptic Jacobian j=1728t |\n| Xiao91 | MPI/91-30, 1991 | Theorem 3.4 pp.14–15; §4 and equation (4) p.21 | Generic torsors, finite translating twists, locally trivial torsors and localization surjectivity |\n\nThe CDL publisher page independently confirms the second edition, Springer Singapore, 2025, DOI 10.1007/978-981-96-1214-7. All operative locators remain explicitly tied to the 2024 manuscript. The current Xiao receipt does not claim the historical full-paper or p.25 reading.\n\nPDF and image hashes, exact source URLs, and individual page scopes are in the JSON receipt. The guarded source edits add page/edition locators only; their unchanged mathematical arguments were already covered by the B1–B3 applied-proof comparison.\n'''
(L/'S6_SERIES_PUBLISH_I_CDL_Xiao_locator_receipt.md').write_text(md)
print(json.dumps({'source_sha256':sha(source),'guards':len(changes),'bib_guards':len(bchanges),'receipt':str(L/'S6_SERIES_PUBLISH_I_CDL_Xiao_locator_receipt.json')},indent=2))
