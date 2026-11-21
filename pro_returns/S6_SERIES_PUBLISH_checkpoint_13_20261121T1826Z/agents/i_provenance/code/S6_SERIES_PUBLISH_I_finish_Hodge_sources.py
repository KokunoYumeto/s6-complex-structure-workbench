from pathlib import Path
import json,hashlib,datetime,re
B=Path('/workspace/scratch/653608133b22');A=B/'work/agents/i_provenance';L=A/'literature';now=datetime.datetime.now(datetime.timezone.utc).isoformat();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();rows=[]
scopes={20:'Theorem6.3 and preceding real pluriharmonic exact sequence: hBC11=2h01-b1+dim_R H11(R); beginning of the BC12 derivation.',21:'Continuation of the BC12 derivation, vanishing of g21 and reduction to l02; exact kernel/image maps read.',22:'Frolicher E2 kernel/image dimension calculation giving l02=h31-h2(3,1).',23:'Proposition6.4: hBC12=h12+h2(3,1)-k20; equation(7) and full displayed BC22 dimension expression.',24:'Complete general BC table and section7.1 complex-S6 specialization, including k(p,q)=0 in intermediate total degree and the BC22 relation.',25:'Section7.1 final S6 BC table; section7.2 begins below and is outside this requested scope.'}
for n,t in scopes.items():
 p=L/'S6_SERIES_PUBLISH_I_McHugh2018v4.pdf';im=L/f'S6_SERIES_PUBLISH_I_McHugh2018v4_p{n:03d}.png';rows.append({'source':'McHugh arXiv1708.03251v4','pdf':str(p),'pdf_sha256':sha(p),'image':str(im),'image_sha256':sha(im),'printed_page':n,'pdf_page':n,'actual_rendered_page_read':True,'scope':t})
scopes={13:'Section4 beginning, Bott–Chern/Aeppli definitions and duality; exact boundary entries hBC00=1,hBC10=0.',14:'All displayed boundary-entry maps, real/conjugate comparison, hBC11=2h01, hBC20=h20, hBC13=h02; exact sequence proving hBC11+hBC22=2hBC21+2.',15:'Completion of the alternating-sum calculation, remaining BC23/32/33 entries and section4 conclusion; section5 begins below.',16:'Figure5 full BC and Aeppli tables with explicit horizontal p/vertical q convention.'}
for n,t in scopes.items():
 p=L/'S6_SERIES_PUBLISH_I_Angella2017v2.pdf';im=L/f'S6_SERIES_PUBLISH_I_Angella2017v2_p{n:03d}.png';rows.append({'source':'Angella arXiv1705.10518v2','pdf':str(p),'pdf_sha256':sha(p),'image':str(im),'image_sha256':sha(im),'printed_page':n,'pdf_page':n,'actual_rendered_page_read':True,'scope':t})
rec={'created_utc':now,'pages':rows,'mathematical_events_added':0,'scope':'Primary formula and locator verification only. No entire-source verification or new independent proof-check credit. The receiving paper supplies its own actual Dolbeault/Frolicher and k(p,q) inputs.','specialization':'With h01=1,h20=h02=h10=0,h11=h+1,h12=h,E2(3,1)=0, intermediate k=0,b1=0,H11(R)=0, the printed formulas give hBC11=2,hBC12=h,hBC22=2h. Angella Figure5 gives the same boundary entries and conjugate/dual positions.','publication_metadata':[{'source':'McHugh','primary_url':'https://www.rivmat.unipr.it/vols/2019-10-1/02-mchugh.html','opened_current_run':True,'journal':'Rivista di Matematica della Università di Parma','volume':'10','number':'1','year':2019,'pages':'25–62','pdf_url':'https://www.rivmat.unipr.it/fulltext/2019-10-1/Riv_Parma_10-1_2019_02.pdf','locator_scope':'The current actual-page receipt is the separately paginated arXiv v4, not inferred journal pagination.'},{'source':'Angella','primary_url':'https://www.sciencedirect.com/science/article/pii/S092622451730222X','opened_current_run':True,'journal':'Differential Geometry and its Applications','volume':'57','year':2018,'pages':'105–120','doi':'10.1016/j.difgeo.2017.10.012','locator_scope':'The current actual-page receipt is arXiv v2; journal metadata verified separately.'}]}
(L/'S6_SERIES_PUBLISH_I_McHugh_Angella_locator_receipt.json').write_text(json.dumps(rec,indent=2,ensure_ascii=False)+'\n')
p=B/'work/S6_SERIES_PUBLISH_I.tex';s=p.read_text();a=s.index('\\bibitem[McHugh(2018)]{McHugh2018}');b=s.index('\\bibitem',a+10);old=s[a:b]
new=r'''\bibitem[McHugh(2019)]{McHugh2018}
Andrew McHugh.

\newblock Bott--Chern--Aeppli, Dolbeault, and Fr{\"o}licher on compact
  complex $3$-folds.

\newblock \emph{Rivista di Matematica della Universit\`a di Parma},
  10(1):25--62, 2019.

\newblock URL
  \url{https://www.rivmat.unipr.it/fulltext/2019-10-1/Riv_Parma_10-1_2019_02.pdf}.
\newblock The locators in this paper refer to the separately paginated
  arXiv:1708.03251v4, 15 November 2018.

'''
changes=[{'id':'I-McHugh-published-metadata','old':old,'new':new,'expected_count':1,'reason':'Official journal primary page and PDF confirm2019 volume10(1),pp25–62. Preserve explicitly the arXivv4 pagination actually opened.'}]
(A/'S6_SERIES_PUBLISH_I_primary_citation_guards_04.json').write_text(json.dumps({'source':str(p),'source_sha256':sha(p),'created_utc':now,'mathematical_events_added':0,'changes':changes},indent=2,ensure_ascii=False)+'\n')
p=B/'work/S6_SERIES_PUBLISH_references.bib';s=p.read_text();changes=[]
for key in ['McHugh2018','Angella2018']:
 pos=s.index('{'+key+',');a=s.rfind('@',0,pos);b=s.find('\n@',pos);b=len(s) if b<0 else b;old=s[a:b];new=old
 if key=='McHugh2018':
  new=new.replace('@misc{','@article{',1).replace('  year = {2018},','  year = {2019},').replace('  howpublished = {arXiv:1708.03251v4},','  journal = {Rivista di Matematica della Universit\\`a di Parma},\n  volume = {10},\n  number = {1},\n  pages = {25--62},\n  version = {4},').replace('  url = {https://arxiv.org/abs/1708.03251v4},','  url = {https://www.rivmat.unipr.it/fulltext/2019-10-1/Riv_Parma_10-1_2019_02.pdf},\n  preprint_url = {https://arxiv.org/abs/1708.03251v4},')
  field='Current21November2026 actual rendered arXiv1708.03251v4 pp20--25 read: Theorem6.3 p20, full derivation20--23, Proposition6.4/equation7 p23, general tablep24 and section7.1pp24--25. Official journal page and PDF identify publication in2019,10(1),25--62. No journal page locators are inferred from preprint pages.'
 else:field='Current21November2026 actual rendered arXiv1705.10518v2 section4pp13--15 and Figure5p16 read. Exact cohomology maps, alternating sum and every table position were compared with the receiving specialization. Publisher metadata independently confirms DGA57(2018),105--120,DOI10.1016/j.difgeo.2017.10.012.'
 i=new.rfind('}');new=new[:i]+'  current_run_verification = {'+field+'},\n'+new[i:];changes.append({'id':'I-bib-current-Hodge-'+key,'old':old,'new':new,'expected_count':1,'reason':'Keep historical bounded readings; append current actual-page scope and verified publication metadata.'})
(A/'S6_SERIES_PUBLISH_I_shared_bib_guards_04.json').write_text(json.dumps({'source':str(p),'source_sha256':sha(p),'created_utc':now,'mathematical_events_added':0,'changes':changes},indent=2,ensure_ascii=False)+'\n')
print('saved10page receipt,1 inline and2 shared-bib guards')
