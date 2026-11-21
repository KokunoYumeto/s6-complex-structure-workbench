"""One-shot exact locators after primary page-image inspection."""
from pathlib import Path
import datetime,hashlib,json
from S6_SERIES_PUBLISH_editing import Editor,block
r=Path(__file__).resolve().parents[1];d=r/'agents/root_primary';ed=Editor('I')
assert hashlib.sha256(ed.before.encode()).hexdigest()=='6a4ccd4a3928324802883187d77b6a5ad33fa7f0f0462ea369bdd5e7a06ff879'
sources=[
 {'key':'BS76','locator':'Chapter III, Theorem4.1 p124; Theorem4.12(ii),(iii) pp134--135',
  'images':['S6_SERIES_PUBLISH_I_BS76_p124.webp','S6_SERIES_PUBLISH_I_BS76_p134.webp','S6_SERIES_PUBLISH_I_BS76_p135.webp'],
  'scope':'Actual original printed page images read. Theorem4.1 statement gives a finite-rank free complex, bounded under relative flatness, with functorial base-tensor comparison. Theorem4.12(ii),(iii) statement and full proof give constant cohomology/local freedom over reduced base and constant Euler characteristic. The direct HTML fetch returned an anti-bot challenge, not book content; it supplies no source evidence. Images were retrieved from the public image links returned by web-open/click, without solving a challenge.',
  'receiving':['push:src:E.2.3','push:src:E.3.1','push:src:B.4.28']},
 {'key':'Knudson2004','locator':'Theorem4.1(1), p10','images':['S6_SERIES_PUBLISH_I_Knudson2004_pdf010.png'],
  'scope':'Actual complete theorem and proof read. Finite-dimensional G-CW hypothesis and mod-p homology-sphere fixed-set conclusion match the triangulated involution on S6 in the receiving proof.','receiving':['mapsI:src:A.3.1']},
 {'key':'Buchdahl1999','locator':'Theorem11, p297; preceding proof continuation p296','images':['S6_SERIES_PUBLISH_I_Buchdahl1999_pdf011.png','S6_SERIES_PUBLISH_I_Buchdahl1999_pdf012.png'],
  'scope':'Actual pages296--297 read, including the complete theorem statement and the end of its proof. Compact complex surface with even first Betti number admits a Kähler metric. Receiving proof establishes b1=6. Existing p297 locator is correct; no claim to a newly independent proof or full reading of all earlier proof pages.','receiving':['push:src:B.3.8']},
 {'key':'Levy08','locator':'Section3.1, Lemmas3.1--3.2, pp588--590','images':['S6_SERIES_PUBLISH_I_Levy08_pdf018.png','S6_SERIES_PUBLISH_I_Levy08_pdf019.png','S6_SERIES_PUBLISH_I_Levy08_pdf020.png','S6_SERIES_PUBLISH_I_Levy08_pdf021.png'],
  'scope':'Actual pp587--590 read. Both lemma statements and complete proofs read, plus Section3.1 beginning/end: exact functors produce topological K maps, homotopic functors agree, and local transversal finite bundle complexes stabilize to global complexes. Receiving analytic perfect cotangent complex uses this precise forgetful/stabilization comparison.','receiving':['push:src:A.3.1']},
 {'key':'FG10','locator':'Theorem5.8 and Remark5.9, p102','images':['S6_SERIES_PUBLISH_I_FG10_pdf020.png'],
  'scope':'Actual published p102 read, including complete theorem/proof and remark. Proper lci schemes with natural obstruction theory have virtual Euler equal to degree of the Fulton class, invariant under lci deformation; virtual Chern numbers of smoothings agree. Receiving analytic assertion has its own full topological K/cycle proof and cites this precise proper-scheme statement.','receiving':['push:src:A.3.1']},
 {'key':'AKMW02AB','locator':'Theorem1.6.1 p543; Theorem2.7.1 pp551--552; Section5.5 pp564--565; Section5.6 pp565--566',
  'images':['S6_SERIES_PUBLISH_I_AKMW02AB_pdf013.png','S6_SERIES_PUBLISH_I_AKMW02AB_pdf021.png','S6_SERIES_PUBLISH_I_AKMW02AB_pdf022.png','S6_SERIES_PUBLISH_I_AKMW02AB_pdf034.png','S6_SERIES_PUBLISH_I_AKMW02AB_pdf035.png','S6_SERIES_PUBLISH_I_AKMW02AB_pdf036.png'],
  'scope':'Actual six published pages read. Theorem1.6.1 and its preceding argument, complete Theorem2.7.1 statement/proof, and Sections5.5--5.6 analytic toric-chart/subdivision correspondence and equivariant factorization were read. Receiving proof supplies finite strict cone complexes, original unit gluings and proper monomial blow-ups near a compact central set; the separate cited Matsuki correction remains unchanged.','receiving':['push:src:A.4.8']}
]
retrieval=json.loads((d/'S6_SERIES_PUBLISH_I_root_primary_retrieval.json').read_text())
for row in sources:
 row['actual_image_reads']=[{'file':f,'sha256':hashlib.sha256((d/f).read_bytes()).hexdigest()} for f in row.pop('images')]
 row['retrieval']=next(x for x in retrieval['rows'] if x['key']==row['key'])
 if row['key']=='BS76':row['retrieval']['primary_content']=False
 else:row['retrieval']['primary_content']=True
guards=[
 (r'\cite[Chapter III, Theorem 4.1]{BS76}',r'\cite[Chapter~III, Theorem~4.1, p.~124]{BS76}',2),
 (r'\citet[Chapter III, Theorem 4.12(ii)]{BS76}',r'\citet[Chapter~III, Theorem~4.12(ii), pp.~134--135]{BS76}',2),
 (r'\citep[Chapter III, Theorem 4.12(iii)]{BS76}',r'\citep[Chapter~III, Theorem~4.12(iii), pp.~134--135]{BS76}',2),
 (r'\cite[Theorem 4.1(1)]{Knudson2004}',r'\cite[Theorem~4.1(1), p.~10]{Knudson2004}',2),
 (r'\cite[Lemmas 3.1--3.2 and Section 3.1]{Levy08}',r'\cite[Section~3.1, Lemmas~3.1--3.2, pp.~588--590]{Levy08}',2),
 (r'; \cite{FG10}}',r'; \cite[Theorem~5.8 and Remark~5.9, p.~102]{FG10}}',1),
 ('directly. The algebraic counterpart is Theorem 5.8 and\nRemark 5.9 of \\cite{FG10}.','directly. The proper-scheme counterpart is\n\\cite[Theorem~5.8 and Remark~5.9, p.~102]{FG10}.',1),
 (r'\cite[Theorems 1.6.1 and 2.7.1]{AKMW02AB}',r'\cite[Theorem~1.6.1, p.~543; Theorem~2.7.1, pp.~551--552]{AKMW02AB}',2),
 (r'\cite[Section 5.5]{AKMW02AB}',r'\cite[Section~5.5, pp.~564--565]{AKMW02AB}',2),
 ('described in Section 5.5 of that paper.','described in \\cite[Section~5.5, pp.~564--565]{AKMW02AB}.',1)
]
for old,new,count in guards:ed.replace(old,new,'D18','Exact edition and printed-page locator read in primary page images; receiving hypothesis/scope compared; no new mathematical check credit.','root primary locator closure',count=count)
ed.save()
receipt={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_before_sha256':hashlib.sha256(ed.before.encode()).hexdigest(),'source_after_sha256':hashlib.sha256(ed.text.encode()).hexdigest(),'sources':sources,'guards':[{'old':a,'new':b,'count':c} for a,b,c in guards],'math_events_added':0,'scope':'Primary citation verification only; no new theorem or independent proof claim.'}
(d/'S6_SERIES_PUBLISH_I_root_primary_locator_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'sources_closed':len(sources),'locator_guards':len(guards),'math_events_added':0}))
