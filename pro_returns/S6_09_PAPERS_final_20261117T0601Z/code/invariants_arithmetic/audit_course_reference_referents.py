from pathlib import Path
import json,re,hashlib
ROOT=Path(__file__).resolve().parents[3]
D=ROOT/'deliverables'
WORK=D/'work/invariants_arithmetic'
COURSE=D/'editorial/III_course'
A='almost-complex-structures-and-integrability.tex'
C='integral-chern-classes-for-lesson11.tex'
U='manifold-duality-the-diagonal-and-wu-classes.source.tex'
P='projective-splitting-for-lesson11.tex'
S='spin-six-and-the-framing-comparison.tex'
F='the-original-six-dimensional-framing-invariant.tex'
T='thom-euler-for-lesson11.tex'
FILES={A,C,U,P,S,F,T}
def slug(f):return f[:-4]
def label(f,n): return 'courseIII:'+slug(f)+':section-'+str(n)
def cref(*labels):return r'\cref{'+','.join(labels)+'}'
def loc(f,*ns):return cref(*(label(f,n) for n in ns))
L=lambda n:'courseIII:thom-euler-for-lesson11:CG-S6-CHAIN-'+n
maps={}
def put(f,n,before,after,reason,targets=()):
 maps.setdefault((f,n),[]).append(dict(before=before,after=after,reason=reason,target_labels=list(targets) or re.findall(r'\\(?:c|C|eq)?ref\{([^}]+)\}',after)))
def local(f,n,before,*ns):put(f,n,before,loc(f,*ns),'The context refers to this chapter’s displayed construction, with this exact section heading.',[label(f,x) for x in ns])
for n,b,ns in [(594,'Sections 7--9',(7,8,9)),(796,'Section 7',(7,)),(947,'Section 1',(1,)),(947,'Sections 7--8',(7,8)),(950,'Section 7',(7,)),(950,'Sections 6--9',(6,7,8,9)),(962,'Sections 10.1--10.3',('10.1','10.2','10.3')),(1068,'Section 10.5',('10.5',))]:local(A,n,b,*ns)
put(C,108,'lesson 11, Section 10.3',loc(A,'10.3'),'The integral Chern character is applied in the almost-complex chapter’s product-of-spheres calculation.',[label(A,'10.3')])
put(C,108,'Sections 10.4--10.5',loc(A,'10.4','10.5'),'These are the almost-complex degree-one map/factorial and tangent-bundle sections.',[label(A,'10.4'),label(A,'10.5')])
for n,b,t in [(125,'Lemma 2.1','2.1'),(193,'Lemma 3.1','3.1'),(220,'Lemma 3.1','3.1'),(241,'Theorem 3.2','3.2'),(244,'Corollary 2.3','2.3'),(336,'Corollary 2.3','2.3')]:put(U,n,b,cref('courseIII:duality:'+t),'The named duality lemma/theorem is the exact receiving premise; its statement and relevant application were read.',['courseIII:duality:'+t])
put(U,279,'as proved in Theorem 4.1 and Exercise 6.4','as follows from '+cref('courseIII:duality:4.1')+r' with cohomology basis \(1,a\) and cup-dual basis \(a,1\)','Original Exercise 6.4 is in the omitted original section 6. Its circle specialization follows directly from the complete printed signed-diagonal formula; the explicit basis substitution makes this caption self-contained. Original exercise read at sources/codex_workspace/courses/CG-S6/sources/manifold-duality-the-diagonal-and-wu-classes.source.txt:335–345.',['courseIII:duality:4.1'])
put(P,93,'lesson 11, Section 10.1',loc(A,'10.1'),'The finite embedding and projection formula T(T*T)^(-1)T* are in the almost-complex chapter, source lines 964–966.',[label(A,'10.1')])
local(S,324,'Section 2',2)
for n,b,ns in [(9,'Sections 1--3',(1,2,3)),(483,'Sections 5--6',(5,6)),(670,'Section 3',(3,)),(670,'Sections 5--6',(5,6)),(681,'Section 11',(11,)),(718,'Section 2',(2,)),(742,'Section 1',(1,)),(839,'Section 1',(1,)),(1105,'Section 2',(2,)),(1230,'Section 4',(4,)),(1262,'Section 4',(4,)),(1314,'Section 6.1',('6.1',)),(1346,'Section 2',(2,)),(1513,'Section 1',(1,)),(1758,'Sections 5--8',(5,6,7,8))]:local(F,n,b,*ns)
for n,f in [(1329,'whitney-moves-in-the-receiving-dimensions.tex'),(1489,'realizing-framed-handles-and-middle-cancellation.tex')]:put(F,n,'Sections 2--5',loc(f,2,3,4,5),'This is a named companion, not the framing chapter. CDP independently reopened its exact section headers and operative passages and confirmed this range on 17 November 2026 UTC; retained in work/cdp_audit/course_reference_locator_review.json.',[label(f,k) for k in (2,3,4,5)])
for n,b,t in [(39,'Lemma 5.1','LEMMA-5.1'),(57,'Theorem 5.2','THEOREM-5.2'),(117,'Proposition 6.1','PROPOSITION-6.1'),(146,'Theorem 5.2','THEOREM-5.2'),(152,'Theorem 7.1','THEOREM-7.1')]:put(T,n,b,cref(L(t)),'The exact complete retained Thom/coefficient statement is the receiving premise. Root owns moving its pre-environment label into the correct environment.',[L(t)])
for n,b,t in [(48,'Section 1','section-1'),(61,'Lemma 4.1','lemma:4.1'),(119,'Section 3','section-3'),(121,'Section 4','section-4'),(196,'Lemma 1.1','lemma:1.1'),(219,'Section 4','section-4')]:put(T,n,b,cref('mapsI:chain:'+t),'The source’s earlier chain sections were moved in full to the common Paper I foundations. The exact retained Paper I label, statement or section text was checked.',['mapsI:chain:'+t])
local(T,219,'Section 6',6)
put(A,1128,r'Konstantis--Parton \cref{courseIII:almost-complex-structures-and-integrability:section-6}',r'Konstantis--Parton, Section~6','The explicit author antecedent refers to the external paper arXiv:1707.03883v1 §6. It is not the local coordinate-change section. Retain the existing original source attribution; this is a locator-ownership check, not a new primary-theorem verification.')
# Disambiguate the two separate providers of the projective product calculation.
put(P,111,'The product chain equivalence and free even homology of '+loc(P,2),'The product chain equivalence in '+cref('mapsI:chain:lemma:4.1')+' and the free even homology in '+loc(P,2),'The local section 2 proves the free even projective homology; the chain product equivalence itself is the full common Paper I lemma. The original sentence can misleadingly assign both premises to the local section.',['mapsI:chain:lemma:4.1',label(P,2)])
external={
 (A,7): [('Section 2.2','Baez, The Octonions, arXiv:math/0105155v4, §2.2'),('Sections 2--4','Hill–Taylor, arXiv:0710.2310v2, §§2–4')],
 (A,152): [('Section 2.2','Baez, The Octonions, arXiv:math/0105155v4, §2.2')],
 (A,419): [('Section 2.2','Baez, The Octonions, arXiv:math/0105155v4, §2.2')],
 (A,950): [('Sections 2--4','Hill–Taylor, arXiv:0710.2310v2, §§2–4')],
 (A,957): [('Sections 3--6','Konstantis–Parton, Almost complex structures on spheres, arXiv:1707.03883v1, §§3–6')],
 (U,279): [('Section 11','Milnor–Stasheff, Characteristic Classes (1974), §11')],
 (S,7): [('Sections 2--3','Michel–Weber, Michel Kervaire work on knots in higher dimensions, arXiv:1409.0704v1, §§2–3')]
}
heads={(A,945):'Theorem 9.1 is the source’s theorem heading, not a reference. Root owns converting it into a theorem environment and attaching a stable label while retaining its whole proof.',(T,193):'Proposition 8.1 is the source’s proposition heading, not a reference. Root owns closing the preceding Thom theorem/proof at its actual boundary, then giving this proposition its own environment.'}
inputs=[D/'work/maps_audit/III_course_residual_plain_number_locators.json',D/'work/maps_audit/III_course_remaining_local_section_reference_candidates.json']
records=[]
texs={p:(D/('S6_09_PAPERS_'+p+'.tex')).read_text() for p in ('I','II','III')}
labels={}
for p,s in texs.items():
 for lab in re.findall(r'\\label\{([^}]+)\}',s):labels.setdefault(lab,[]).append(p)
for inputp in inputs:
 for row in json.loads(inputp.read_text()):
  f=Path(row['file']).name
  if f not in FILES:continue
  n=row['line'];key=(f,n);paragraph=row['paragraph']; replacements=maps.get(key,[])
  for rep in replacements:
   assert paragraph.count(rep['before'])==1,(key,rep['before'])
   flat=[]
   for lab in rep['target_labels']:flat.extend(lab.split(','))
   rep['target_labels']=flat
   rep['target_papers']={lab:labels.get(lab,[]) for lab in flat}
   assert all(rep['target_papers'].values()),(key,rep['target_papers'])
  ext=[{'phrase':a,'external_locator':b,'disposition':'retain_named_external_locator','scope':'Exact author antecedent and source attribution checked; no new primary-theorem or full-proof verification claimed in this locator pass.'} for a,b in external.get(key,[])]
  refs=re.findall(r'\\(?:c|C|eq)?ref\{([^}]+)\}',paragraph)
  refchecks=[]
  for group in refs:
   for lab in group.split(','):
    if ':section-' in lab:refchecks.append({'label':lab,'exists_in_actual_papers':labels.get(lab,[]),'disposition':'replace_misassigned_external_antecedent' if key==(A,1128) else 'correct_local_section_antecedent'})
  status='correction_supplied' if replacements else ('source_heading_root_normalizer' if key in heads else ('retain_named_external_locator' if ext else 'correct_reference_no_change'))
  notes=[]
  if key in heads:notes.append(heads[key])
  if key==(A,957):notes.append('Coordinated with maps/root: retain the first three mathematical/credit sentences; replace only the final nonoperative supporting operator-K-theory course comparison sentence by printed polynomial clutching sections 10.1–10.3, preserving that original sentence in the move ledger. Maps implements; no duplicate edit here.')
  records.append({'file':f,'source_path':str((COURSE/f).relative_to(D)),'line':n,'input_screen':str(inputp.relative_to(D)),'paragraph_sha256':hashlib.sha256(paragraph.encode()).hexdigest(),'paragraph_before':paragraph,'status':status,'replacements':replacements,'external_locators':ext,'existing_section_reference_checks':refchecks,'notes':notes})
assert len(records)==71,len(records)
assert len({(r['file'],r['line']) for r in records})==71
missing=[]
for r in records:
 if r['input_screen'].endswith('plain_number_locators.json'):
  rr=next(x for x in json.loads(inputs[0].read_text()) if x['file']==r['file'] and x['line']==r['line'])
  for m in rr['matches']:
   if not(any(m in p['before'] for p in r['replacements']) or any(m==p['phrase'] for p in r['external_locators']) or (r['file'],r['line']) in heads):missing.append((r['file'],r['line'],m))
assert not missing,missing
reading_scopes={
 A:'All 16 screened paragraph contexts; local section headings 1–11; exact finite embedding/homotopy projection arguments 959–990, elliptic absorption 729–779, local smooth theorem 930–958, degree-one and top Chern calculations 1044–1187. Earlier full receiving proof checks remain separate.',
 C:'Screened final paragraph108 and the complete Chern-character operations §3, lines75–108; source comparison context60–74.',
 U:'All seven screened paragraphs; exact compact-support gluing lemma2.1; Poincare/finite-duality block117–155; inverse-flow/tube/finite-domination block160–244; signed diagonal formula310–345. Original exercise6.4 source335–345 checked to repair omitted-exercise pointer.',
 P:'Both screened paragraphs; finite projective groups32–57; actual flag construction89–100; line tensor product102–115; common Paper I product lemma label/text.',
 S:'Both original screened paragraphs and two local-reference contexts; unitary fibration §2; rank-six Euler computation275–309; rank-seven fibration/trivialization311–350; receiving pullback357–366; exercise430.',
 F:'All 29 screened paragraph contexts and their local section/subsection headings. Existing complete receiving audits are not duplicated. Cross-file §§2–5 targets independently confirmed by cdp_audit; exact source wording and current labels checked here.',
 T:'Complete converted retained provider1–224 read; source sections1–4 identified with complete Paper I chain foundations section1, section3, section4 and lemmas1.1/4.1. Root owns discovered statement/proof boundary formatting.'}
result={'reviewer':{'model':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date_utc':'2026-11-17'},'scope':'Exact reference antecedents and actual target labels only; no manuscript edits, no new blanket full-proof or original-literature certification. Root owns environment normalization; maps_audit owns content-reference patches.','counts':{'paragraphs':len(records),'residual_plain_number_paragraphs':50,'remaining_local_reference_paragraphs':21,'replacement_fragments':sum(len(r['replacements']) for r in records),'external_locator_occurrences_retained':sum(len(r['external_locators']) for r in records)},'input_sha256':{str(p.relative_to(D)):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs},'actual_manuscript_sha256':{p:hashlib.sha256(s.encode()).hexdigest() for p,s in texs.items()},'read_scopes':reading_scopes,'records':records}
out=WORK/'course_characteristic_reference_review.json'
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
flat=[{'file':r['file'],'line':r['line'],**x} for r in records for x in r['replacements']]
(WORK/'course_characteristic_reference_substitutions.json').write_text(json.dumps(flat,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result['counts']))
print(out)
