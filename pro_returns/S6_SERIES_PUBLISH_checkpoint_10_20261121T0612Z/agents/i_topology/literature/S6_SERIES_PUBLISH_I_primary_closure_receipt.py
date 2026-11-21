from pathlib import Path
import hashlib,json,datetime
p=Path(__file__).parent
h=lambda q:hashlib.sha256(q.read_bytes()).hexdigest()
def page(prefix,pdf,printed,scope):
 q=p/f'{prefix}_pdfpage_{pdf:03}.png'
 return {'pdf_page':pdf,'printed_page':printed,'image_file':str(q),'image_sha256':h(q),'actual_image_view':True,'read_scope':scope}
records=[
 {'key':'Fujimoto1990AB','title':'Logarithmic Transformations on Elliptic Fiber Spaces. II. — elliptic bundle case —','url':'https://eprints.lib.hokudai.ac.jp/repo/huscap/all/5450/16.pdf','pdf_file':str(p/'S6_SERIES_PUBLISH_I_Fujimoto1990_volume.pdf'),'pdf_sha256':h(p/'S6_SERIES_PUBLISH_I_Fujimoto1990_volume.pdf'),'pages':[
 page('S6_SERIES_PUBLISH_I_Fujimoto1990_volume',85,81,'Title and introduction; exact title authentication.'),
 page('S6_SERIES_PUBLISH_I_Fujimoto1990_volume',89,85,'Full local Cartier-divisor cocycle construction and comparison map.'),
 page('S6_SERIES_PUBLISH_I_Fujimoto1990_volume',90,86,'Definition 1.1 and Remarks 1.2–1.5, including arbitrary Cartier divisor and attribution in Remark 1.4.'),
 page('S6_SERIES_PUBLISH_I_Fujimoto1990_volume',96,92,'Proposition 1.14 begins at foot of page.'),
 page('S6_SERIES_PUBLISH_I_Fujimoto1990_volume',97,93,'Proposition 1.14 full statement and proof: codimension-at-least-three extension via the principal elliptic bundle cohomology map; Example 1.15 begins.'),
 page('S6_SERIES_PUBLISH_I_Fujimoto1990_volume',98,94,'Example 1.15 conclusion, codimension-two bundle extension obstruction and exact unresolved relative compactification/Kähler-metric questions.')], 'locator_result':'Use Definition 1.1 p.86, construction p.85, Proposition 1.14 pp.92–93, Example 1.15 pp.93–94. The earlier p.93 shorthand omitted the statement start. Current primary-page authentication supplements, and does not retroactively enlarge, the earlier carried-background event.'},
 {'key':'Cartan1952B_AB','title':'Variétés analytiques complexes et cohomologie','url':'https://www.numdam.org/article/SHC_1951-1952__4__A19_0.pdf','pdf_file':str(p/'S6_SERIES_PUBLISH_I_Cartan1952B.pdf'),'pdf_sha256':h(p/'S6_SERIES_PUBLISH_I_Cartan1952B.pdf'),'pages':[
 page('S6_SERIES_PUBLISH_I_Cartan1952B',2,'19-1','Title, exposé number 19, date 9 June 1952, written October 1952.'),
 page('S6_SERIES_PUBLISH_I_Cartan1952B',15,'19-14','Section 5, proof of Theorem A and start of Theorem B for coherent sheaves on Stein spaces; q≥1 vanishing statement.'),
 page('S6_SERIES_PUBLISH_I_Cartan1952B',16,'19-15','Completion of Theorem B proof, including q=1 approximation argument.')], 'locator_result':'Use exposé 19, §5, pp.14–15 (printed 19-14–19-15).'},
 {'key':'Fujiki2009AB','title':'Automorphisms of Parabolic Inoue Surfaces','url':'https://arxiv.org/pdf/0903.5374v1','pdf_file':str(p/'S6_SERIES_PUBLISH_I_Fujiki2009v1.pdf'),'pdf_sha256':h(p/'S6_SERIES_PUBLISH_I_Fujiki2009v1.pdf'),'pages':[
 page('S6_SERIES_PUBLISH_I_Fujiki2009v1',1,1,'Full setup and Theorem 1.1 part (1), central identity component C*. Theorem statement continues on p.2.'),
 page('S6_SERIES_PUBLISH_I_Fujiki2009v1',2,2,'Theorem 1.1 parts (2)–(3), Corollary 1.2, and the geometric toric-cover/dual-cycle action description.'),
 page('S6_SERIES_PUBLISH_I_Fujiki2009v1',4,4,'Equations (1)–(8): full toric chart transitions, torus action, fixed elliptic cover, rational curves, and cyclic deck map.'),
 page('S6_SERIES_PUBLISH_I_Fujiki2009v1',5,5,'Equations (9)–(13), exact conjugation and centralizing C* action, finite subgroup and Lemma 2.1 statement.')], 'locator_result':'Use Theorem 1.1 pp.1–2 and §2, equations (1)–(8), p.4; equation (9) p.5 verifies centralizing action. No claim of a fresh independent mathematical check.'}
]
q=p/'S6_SERIES_PUBLISH_I_Fujimoto_Cartan_Fujiki_primary_receipt.json'
q.write_text(json.dumps({'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'records':records,'event_scope':'Primary-page authentication only; no new mathematical CHECK_EVENTS.'},indent=2,ensure_ascii=False)+'\n')
print(q)
