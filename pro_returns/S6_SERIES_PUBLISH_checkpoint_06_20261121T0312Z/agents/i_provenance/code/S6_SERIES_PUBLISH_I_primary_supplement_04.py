from pathlib import Path
import json,hashlib,datetime
B=Path('/workspace/scratch/653608133b22'); A=B/'work/agents/i_provenance'; L=A/'literature'; now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
items=[]
for name,url,pages,scope in [
 ('Douady1974','https://www.numdam.org/article/ASENS_1974_4_7_4_569_0.pdf',[597,598,599,600],{'597':'Finite-dimensional transversal construction preceding VII.8.','598':'VII.8 principal theorem: existence of a finite-dimensional versal deformation of every compact complex analytic space; beginning of proof.','599':'Completion of principal theorem proof; VIII.1 setup and preliminary lemmas.','600':'VIII.1 Theorem 1 and following corollary: a trivial pullback has constant classifying germ, and isomorphic deformations give the same tangent map; dual-number deformation/tangent bijection in proof.'}),
 ('Stein2007','https://www.wstein.org/books/modform/stein-modform.pdf',[171,172,173,174],{'171':'Theorem 9.18 statement: Sturm vanishing modulo a prime ideal, with its degree/index bound; proof begins.','172':'Continuation of full proof of Theorem 9.18.','173':'End of Theorem 9.18 proof; Corollary 9.19 begins.','174':'Completion of Corollary 9.19 and Corollary 9.20 for a fixed character on Gamma0(N); explicit index formula.'})]:
 p=L/f'S6_SERIES_PUBLISH_I_{name}.pdf'
 for n in pages:
  im=L/f'S6_SERIES_PUBLISH_I_{name}_p{n}.png'
  items.append({'source':name,'primary_url':url,'pdf':str(p),'pdf_sha256':sha(p),'printed_page':n,'pdf_page':n-568+1 if name=='Douady1974' else n+14,'image':str(im),'image_sha256':sha(im),'actual_rendered_page_read':True,'read_scope':scope[str(n)]})
p=L/'S6_SERIES_PUBLISH_I_Waldschmidt1988theta.pdf'
for n,scope in [('15-03','The CM, non-torsion algebraic-point normalized sigma value sigma(u) exp(-s2(Omega)u^2/2) is stated transcendental, explicitly attributed to Bertrand. Algebraic g2,g3 are retained hypotheses. This page also states related third-kind sigma values.'),('15-05','The unnumbered periodic-functional-equation theorem: q=exp(i*pi*tau) belongs to the number field K; f(u+1)=f(u), f(u+tau)=P(exp(-2*pi*i*u))*f(u)+Q(exp(-2*pi*i*u)); F analytic at zero and algebraic independence are explicit assumptions; the point-count bound is displayed.')]:
 im=L/f'S6_SERIES_PUBLISH_I_Wald1988_p{n}.png';items.append({'source':'Waldschmidt1988theta','primary_url':'https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/GDL/SemBxFTNT.pdf','pdf':str(p),'pdf_sha256':sha(p),'printed_page':n,'pdf_page':4 if n=='15-03' else 6,'image':str(im),'image_sha256':sha(im),'actual_rendered_page_read':True,'read_scope':scope})
receipt={'created_utc':now,'reading_dates_utc':['2026-11-21'],'pages':items,'mathematical_events_added':0,'scope_notes':{'Douady':'The paper supplies the Cech identification with H1(T_X) and the nonzero Kodaira-Spencer parameter. Douady supplies the finite-dimensional versal germ and its tangent universality. Smoothness of the receiving one-dimensional germ follows from its displayed injective substitution argument; no general unobstructedness is attributed to Douady. Metadata independently opened at the Numdam primary landing page: Ann. Sci. ENS(4)7(4)(1974),569–602, DOI10.24033/asens.1280.','Stein':'Theorem9.18 is a congruence theorem. For an integral-coefficient difference, apply it at every prime ideal: each coefficient belongs to every prime ideal and hence is zero. This exact characteristic-zero passage must remain in the receiving application; the source is not described as directly stating that passage.','Waldschmidt':'This current-run receipt covers exactly the two named rendered pages, not the whole paper or Bertrand1982 proof.'}}
(L/'S6_SERIES_PUBLISH_I_Douady_Stein_Wald_primary_scope_receipt.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n')
sp=B/'work/S6_SERIES_PUBLISH_I.tex';s=sp.read_text();changes=[]
def guard(id,old,new,reason):
 assert s.count(old)==1,(id,s.count(old));changes.append({'id':id,'old':old,'new':new,'expected_count':1,'reason':reason})
old="Douady's principal theorem in \\S VII.8 and Theorem~1 and its\ncorollary in \\S VIII.1 give a minimal versal analytic germ with\ntangent space $H^1(T_X)$."
new="By \\cite[\\S VII.8, principal theorem, pp.~598--599;\n\\S VIII.1, Theorem~1 and its corollary, p.~600]{Douady1974},\nthere is a minimal versal analytic germ with tangent space $H^1(T_X)$."
guard('I-Douady-operative-exact-locator',old,new,'Primary printed pp597–600 actually read; the receiving explicit Cech maps and smoothness proof are retained.')
anchor='\\bibitem[Duke and Imamo{\\u g}lu(2008)]{DukeImamoglu2008}'
bib='''\\bibitem[Douady(1974)]{Douady1974}
Adrien Douady.

\\newblock Le probl\\`eme des modules locaux pour les espaces
  $\\mathbf C$-analytiques compacts.

\\newblock \\emph{Annales scientifiques de l'\\'Ecole Normale Sup\\'erieure},
  (4) 7(4):569--602, 1974.

\\newblock \\doi{10.24033/asens.1280}.
\\newblock URL
  \\url{https://www.numdam.org/article/ASENS_1974_4_7_4_569_0.pdf}.

'''
guard('I-Douady-inline-bibliography',anchor,bib+anchor,'The operative primary citation requires its bibliography entry; primary Numdam metadata and PDF verified.')
guard('I-Stein-author-host-url','\\newblock URL \\url{https://wstein.org/books/modform/stein-modform.pdf}.','\\newblock URL \\url{https://www.wstein.org/books/modform/stein-modform.pdf}.','The www author-host endpoint returned the exact primary PDF; the no-www endpoint returned403 during this retrieval.')
(A/'S6_SERIES_PUBLISH_I_primary_citation_guards_03.json').write_text(json.dumps({'source':str(sp),'source_sha256':sha(sp),'created_utc':now,'mathematical_events_added':0,'receipt':str(L/'S6_SERIES_PUBLISH_I_Douady_Stein_Wald_primary_scope_receipt.json'),'changes':changes},indent=2,ensure_ascii=False)+'\n')
bp=B/'work/S6_SERIES_PUBLISH_references.bib';bs=bp.read_text();ch=[]
for key,field in [('Douady1974','Current run21November2026: actual rendered primary pp597--600 read. VII.8 principal theorem statement p598 and proof598--599; VIII.1 Theorem1 and following corollary p600. Finite-dimensional versality and tangent universality only; the receiving Cech map and analytic inverse-function argument supply its exact H1 identification and smoothness. DOI10.24033/asens.1280 verified at the Numdam primary landing page.'),('CgzStein2007','Current run21November2026: actual rendered author-hosted pp171--174 read. Theorem9.18 is modulo a prime ideal; Corollary9.20 gives the fixed-character bound and index formula. The receiving integral-coefficient characteristic-zero equality uses reduction at every prime ideal, which must be stated separately.'),('waldschmidt1988theta','Current run21November2026: actual rendered author-hosted printed pp15-03 and15-05 read. Page15-03 states the CM non-torsion algebraic-point normalized sigma transcendence and credits Bertrand; page15-05 retains algebraic q and its other exact periodic-equation hypotheses. No current full-paper or Bertrand-proof reading is claimed.')]:
 pos=bs.index('{'+key+',');a=bs.rfind('@',0,pos);b=bs.find('\n@',pos);b=len(bs) if b<0 else b;old=bs[a:b];new=old
 if key=='Douady1974':new=new.replace('https://numdam.org/item/10.24033/asens.1280.pdf','https://www.numdam.org/article/ASENS_1974_4_7_4_569_0.pdf')
 if key=='CgzStein2007':new=new.replace('https://wstein.org/books/modform/stein-modform.pdf','https://www.wstein.org/books/modform/stein-modform.pdf')
 i=new.rfind('}');new=new[:i]+'  current_run_verification = {'+field+'},\n'+new[i:]
 ch.append({'id':'I-bib-current-primary-'+key,'old':old,'new':new,'expected_count':1,'reason':'Append the exact current-run source-reading scope while retaining the historical attached verification fields.'})
(A/'S6_SERIES_PUBLISH_I_shared_bib_guards_03.json').write_text(json.dumps({'source':str(bp),'source_sha256':sha(bp),'created_utc':now,'mathematical_events_added':0,'changes':ch},indent=2,ensure_ascii=False)+'\n')
print('saved 10-page scope receipt, 3 main-source guards, 3 shared-bib guards')
