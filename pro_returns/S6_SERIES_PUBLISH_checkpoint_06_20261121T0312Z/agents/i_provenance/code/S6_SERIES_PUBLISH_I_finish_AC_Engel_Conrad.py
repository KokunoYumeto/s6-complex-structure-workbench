from pathlib import Path
import json,hashlib,datetime
B=Path('/workspace/scratch/653608133b22');A=B/'work/agents/i_provenance';L=A/'literature';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();now=datetime.datetime.now(datetime.timezone.utc).isoformat();rows=[]
scopes={51:'Proposition7.12 statement begins: collapse c_* and its exact kernel, specialization as dual, invariant lattice bases.',52:'Proposition7.12 statement completes with degree2 orientations, long/short splitting, and proof through cellular mixed-cycle map(7.9).',53:'Complete Proposition7.12 proof: saturated kernel, degree2 and3 surjectivity, exact specialization identification; distinction from AppendixB stated explicitly.',54:'Section7.5 begins: common lattice semidirect product and finite-root meridian maps; preceding Proposition7.14 proof also visible.',55:'Section7.5 toric meridian relation(7.10), Lemma7.16 sign statement and first part of proof.',56:'Completion of the exact deck/zero-section/drift sign comparison in Lemma7.16; same global clockwise sign and determinant formula.',57:'Theorem7.17 full statement/proof ends section7.5; section7.6 begins below. Exact section7.5 span54–57 verified.',61:'Section7.7 hypotheses and Lemma7.25; Proposition7.26 statement begins. Retains4|epsilon2(v2), including the standard v2=-epsilonprime.',62:'Proposition7.26 statement and proof finish; Proposition7.27 statement and transgression/meridian proof begin.',63:'Proposition7.27 proof completes using multiplicativity and common sign; Remark7.28 and Corollary7.29 complete section7.7 before section8.',101:'TheoremB.1 full statement and strategy; specialization sheaf map is an integral isomorphism onto invariants, with exact proper-base-change identification.',102:'Nearby-cycle local models and rank-one/two sheaf restriction maps with explicit signs at both triple points.',103:'Exact sheaf resolution and E2 table; all integral groups and saturated maps displayed.',104:'Differential rank bookkeeping; LemmaB.3 exact support-specialization map and full equivariant collar-flow proof begins.',105:'Support-specialization proof finishes; degree3 Gysin image is saturated; saturation in every degree completes TheoremB.1. RemarkB.4 limits scope to invariants, not the degree2 collapse-generator normalization.'}
for n,t in scopes.items():
 p=L/'S6_SERIES_PUBLISH_I_AC26_primary.pdf';im=L/f'S6_SERIES_PUBLISH_I_AC26_p{n:03d}.png';rows.append({'source':'AC2026 primary 108-page edition','pdf':str(p),'pdf_sha256':sha(p),'primary_url':'https://alpo.ge/s6.pdf','printed_page':n,'pdf_page':n,'image':str(im),'image_sha256':sha(im),'actual_rendered_page_read':True,'scope':t})
for n,t in [(6,'Proposition2.7 complete statement/proof: exact Tate periods and holomorphic unit factors; Proposition2.8 statement and proof begin.'),(11,'Lemma3.8 full statement/proof of primitive rank-one invariant covector; preceding Lemma3.6 exact translated quotient map also read.')]:
 p=B/'work/agents/provenance/literature/S6_SERIES_PUBLISH_Engel.pdf';im=L/f'S6_SERIES_PUBLISH_I_Engel_p{n:03d}.png';rows.append({'source':'Engel arXiv2609.38442v1','pdf':str(p),'pdf_sha256':sha(p),'printed_page':n,'pdf_page':n,'image':str(im),'image_sha256':sha(im),'actual_rendered_page_read':True,'scope':t})
for n,t in [(1,'Exact matrices S,T and Theorem1.1; entire algebraic Euclidean-algorithm proof on this page, not the following geometric proof.'),(17,'AppendixC setup: R=ST,S²=R³=-I and lifted normal form; preceding hyperbolic-distance material is outside the cited scope.'),(18,'TheoremC.1 statement and free-product interpretation; proof of trivial-word and uniqueness begins.'),(19,'Complete uniqueness proof of TheoremC.1 and references.')]:
 p=L/'S6_SERIES_PUBLISH_I_ConradSL2Z.pdf';im=L/f'S6_SERIES_PUBLISH_I_ConradSL2Z_p{n:03d}.png';rows.append({'source':'Keith Conrad, SL2(Z), undated author-hosted19-page notes','pdf':str(p),'pdf_sha256':sha(p),'primary_url':'https://kconrad.math.uconn.edu/blurbs/grouptheory/SL(2,Z).pdf','printed_page':n,'pdf_page':n,'image':str(im),'image_sha256':sha(im),'actual_rendered_page_read':True,'scope':t})
rec={'created_utc':now,'pages':rows,'mathematical_events_added_for_source_reading':0,'AC_exact_locators':{'section7.5':'pp54–57, meridian relation(7.10)p55','Proposition7.12':'pp51–53','Proposition7.26':'pp61–62','Proposition7.27':'pp62–63','TheoremB.1':'statementp101,complete proofpp101–105'},'AC_scope':'TheoremB.1 supplies the integral invariant specialization. The identification with c* and degree2 generator normalization belongs to Proposition7.12. Propositions7.26–27 retain the stated4|epsilon2(v2) hypothesis; the standard v2=-epsilonprime satisfies it.','Conrad_exact_application':'Paper a=-ST, so its projective image is exactly Conrad R=ST. The short central-kernel calculation transfers the cited free-product presentation to the paper a,S generators; no unspecified generator identification.'}
(L/'S6_SERIES_PUBLISH_I_AC_Engel_Conrad_locator_receipt.json').write_text(json.dumps(rec,indent=2,ensure_ascii=False)+'\n')
p=B/'work/S6_SERIES_PUBLISH_I.tex';s=p.read_text();ch=[]
def add(id,old,new,reason):
 assert s.count(old)==1,(id,s.count(old));ch.append({'id':id,'old':old,'new':new,'expected_count':1,'reason':reason})
add('I-F11-generation-primary',r'''$\operatorname{SL}_2(\mathbb Z)$ because $Sa=T$ and $S,T$ perform the
Euclidean algorithm on primitive integral columns.''',r'''$\operatorname{SL}_2(\mathbb Z)$ because $Sa=T$ and $S,T$ generate that
group by \cite[Theorem~1.1, p.~1]{ConradSL2Z}.''','Replace the textbook generation proof by its actually opened primary theorem and the exact displayed matrix map.')
a=s.index('\\item The presentation of the Levi group follows');b=s.index('\\begin{equation}',a);old=s[a:b]
new=r'''\item Since $a=-ST$, its image in $\operatorname{PSL}_2(\mathbb Z)$
is the image of the generator $R=ST$ in
\cite[Theorem~C.1, pp.~18--19]{ConradSL2Z}. That theorem gives
$\operatorname{PSL}_2(\mathbb Z)=\langle\bar a,\bar S\mid
\bar a^3=\bar S^2=1\rangle$. Lifting through the central kernel
$\{I,-I\}$ gives
'''
add('I-F11-known-free-product-citation',old,new,'Full primary normal-form theorem and proof actually read; removed ping-pong reproof is preserved in old/new records; exact a=-ST generator morphism and subsequent central-kernel proof retained.')
add('I-F11-cited-central-kernel-wording','just-proved free product','cited free product','The short central-kernel application remains; only its source description changes.')
old='\\cite[Lemma~3.8]{Engel2026}'
if s.count(old)==1:add('I-circle-Engel-covector-page',old,'\\cite[Lemma~3.8, p.~11]{Engel2026}','Actual rendered statement/proof read.')
anchor='\\bibitem[Cornulier(2011)]{Cornulier2011}'
entry=r'''\bibitem[Conrad(n.d.)]{ConradSL2Z}
Keith Conrad.

\newblock $\operatorname{SL}_2(\mathbb Z)$.
\newblock Author's notes, undated, 19-page version retrieved
  21 November 2026.
\newblock URL
  \url{https://kconrad.math.uconn.edu/blurbs/grouptheory/SL(2,Z).pdf}.

'''
add('I-Conrad-inline-bibliography',anchor,entry+anchor,'Add the exact author-hosted edition; no publication date invented.')
(A/'S6_SERIES_PUBLISH_I_primary_citation_guards_05.json').write_text(json.dumps({'source':str(p),'source_sha256':sha(p),'created_utc':now,'changes':ch,'proof_comparison':'Read complete old F1.1 Step3 and proposed replacement against primary TheoremC.1; formulas, labels, short central-kernel proof and alpha values retained. This is exposed editorial comparison in the existing famF group, with no new independent credit.','evidence_group':'existing famF editorial group; see editorial_famF_reread_receipt.json'},indent=2,ensure_ascii=False)+'\n')
p=B/'work/S6_SERIES_PUBLISH_references.bib';s=p.read_text();entry=r'''@misc{ConradSL2Z,
  author = {Conrad, Keith},
  title = {$\operatorname{SL}_2(\mathbb Z)$},
  year = {n.d.},
  howpublished = {Author's notes, 19-page version retrieved 21 November 2026},
  url = {https://kconrad.math.uconn.edu/blurbs/grouptheory/SL(2,Z).pdf},
  current_run_verification = {Actual rendered p1 and pp17--19 read. Theorem1.1 and its algebraic proof p1; TheoremC.1 statementp18 and full proofpp18--19. The receiving generator a=-ST has the same projective image as the source R=ST; its short central-kernel lift is retained. Exact PDF SHA2566b973d1a42817a113977d27bd5353ad7f674c1f09847b6e978c6c67cc1ff5870.},
}

''';anchor='@article{Cornulier2011,';assert s.count(anchor)==1;ch=[{'id':'I-bib-Conrad-primary','old':anchor,'new':entry+anchor,'expected_count':1,'reason':'Author-hosted primary19-page edition actually opened; source date unknown and explicitly undated.'}]
for key,field in [('AC2026','Current21November2026 actual rendered source pages51--57,61--63,101--105 read. Exact locators: Proposition7.12pp51--53; section7.5pp54--57 with meridian relation7.10p55; Proposition7.26pp61--62; Proposition7.27pp62--63; TheoremB.1statementp101/full proof101--105. TheoremB.1 gives integral invariant specialization only; the c* identification and degree2 generator normalization are in Proposition7.12. Retain4|epsilon2(v2) in7.26--27; standard data satisfy it.'),('Engel2026','Current21November2026 actual rendered Proposition2.7 complete statement/proofp6 and Lemma3.8 complete statement/proofp11 read, in addition to the separate previously recorded section2 and section8 readings.')]:
 pos=s.index('{'+key+',');a=s.rfind('@',0,pos);b=s.find('\n@',pos);b=len(s) if b<0 else b;old=s[a:b];i=old.rfind('}');new=old[:i]+'  current_run_additional_locators = {'+field+'},\n'+old[i:];ch.append({'id':'I-bib-current-topology-'+key,'old':old,'new':new,'expected_count':1,'reason':'Append exact current actual-page scope without changing historical source readings.'})
(A/'S6_SERIES_PUBLISH_I_shared_bib_guards_05.json').write_text(json.dumps({'source':str(p),'source_sha256':sha(p),'created_utc':now,'changes':ch},indent=2,ensure_ascii=False)+'\n')
print('saved21page receipt,',len(ch),'shared guards; main guard count5')
