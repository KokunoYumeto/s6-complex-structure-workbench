"""Exact reference dispositions for the final stable/cooperation chapter pass."""
from pathlib import Path
import hashlib,json,re
D=Path(__file__).resolve().parents[2];W=D/'work/maps_audit';C=D/'editorial/III_course'
M={'reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date':'2026-11-17'}
def lab(stem,key):return 'courseIII:'+stem+':'+key
def cref(*keys):return r'\cref{'+','.join(keys)+'}'
def secs(stem,*nums):return cref(*(lab(stem,'section-'+str(n)) for n in nums))
def eq(stem,n):return r'\eqref{'+lab(stem,'eq:'+n)+'}'
co='coefficient-rings-and-the-original-degree-six-class';res='the-actual-mod-two-adams-resolution-and-cooperation-maps';d8='the-actual-mod-two-cooperation-comparison-through-degree-eight';ad='the-adams-tower-and-exact-inverse-limits';cb='the-degree-six-milnor-cobar-calculation';formal='the-exact-characteristic-two-coordinate-calculation';ar='the-original-adams-tower-and-arithmetic-completion';st='the-original-integral-stable-group-and-its-completion-maps';odd='the-original-odd-prime-cooperations-and-degree-six-adams-calculation';proj='the-original-projective-coordinate-and-actual-cooperations';thom='thom-euler-for-lesson11'
plain=json.loads((W/'III_course_residual_plain_number_locators.json').read_text())
section=json.loads((W/'III_course_remaining_local_section_reference_candidates.json').read_text())
rows=[]
def add(kind,n,replacements,reason):
    source=plain if kind=='plain' else section
    r=dict(source[n-1]);r['input_kind']=kind;r['record_number']=n
    r['full_context_read']=True;r['status']='Exact mappings supplied' if replacements else 'Reference retained at its actual local target or statement title'
    r['reason']=reason;r['mappings']=[]
    for before,after in replacements:
        assert before in r['paragraph'],(kind,n,before)
        labels=[k for v in re.findall(r'\\(?:c|C|eq|auto)?ref\{([^}]+)\}',after) for k in v.split(',')]
        r['mappings'].append({'exact_original_phrase':before,'suggested_tex':after,'target_labels':labels,'matched_target_content':reason})
    rows.append(r)
add('plain',27,[('Section 1',secs(co,1))],'The local full coefficient algebra and exact polynomial-subalgebra image are proved in section1.')
add('plain',28,[('Section 6',secs(co,6))],'The local complete bidegree(2,8) torsion certificate retains the stated monomial and word orders.')
add('plain',127,[('Section 7',secs(res,7))],'The receiving exact degree-range argument is the local section7, following both cobar comparison maps.')
add('plain',128,[('Section 6',secs(d8,6))],'The local section6 distinguishes group-addition products from the spectrum multiplication and proves all powers of the actual first coefficient nonzero.')
add('plain',129,[('Sections 2--7',secs(d8,*range(2,8)))],'The range is the local full bar, suspension, graded-dimension, product and primitive-comparison proof.')
add('plain',130,[('Sections 8--11',secs(ad,*range(8,12))),('Section 4',secs(ad,4))],'The restored producer addition tail states a mathematical finiteness dependence: local coefficient construction8–11 supplies the finite-stage hypothesis of local convergence4. The original addition date stays verbatim.')
add('plain',131,[('Section 2',secs(ad,2))],'The local finite-group inverse-limit argument gives the compatible tuple used by convergence.')
add('plain',132,[('Sections 2--4',secs(ad,2,3,4))],'The local exact difference map, tower pages and finite-group convergence replace reliance on the source vanishing inequality. Source line locators remain external.')
add('plain',133,[('Section 3',secs(ad,3))],'The long exact sequences feed the local exact-couple/tower-page construction.')
add('plain',134,[('Section 1',secs(ad,1))],'The original H F_p used in the local tower is exactly the coefficient spectrum just constructed.')
add('plain',135,[],'This is the statement heading Theorem1.1, not a prose citation to a distinct target; its full statement and proof remain printed.')
add('plain',136,[('Sections 2--5',secs(cb,2,3,4,5))],'The complete all-length weight filtration and correcting-cochain proof is local sections2–5.')
add('plain',137,[],'This is the local odd-prime theorem statement heading, not a prose reference to be redirected.')
add('plain',138,[('Section 3',secs(cb,3))],'The full R=F2[x] module and first differential are in the local section3.')
add('plain',139,[('projective-cooperation Sections 3--5',secs(proj,3,4,5))],'The shared illustration caption cites the projective-cooperation additive-series, full three-factor coproduct and integer-two sections, not the receiving formal-coordinate sections.')
add('plain',140,[('Section 2',secs(ar,2))],'The local universal completion map proves the corrected p-invertible conclusion; original author line1264 stays an external locator.')
add('plain',141,[('Lemma 5.1 of the included Thom/Euler chapter',cref(lab(thom,'CG-S6-CHAIN-LEMMA-5.1')))],'The fully printed well-ordered subgroup-of-free proof gives the finite-rank specialization used here.')
add('plain',142,[('Section 1',secs(st,1))],'The local finite-chain comparison preserves finite generation under tensor products and finite filtered extensions.')
add('plain',143,[('the Thom/Euler companion, Theorem 5.2',cref(lab(thom,'CG-S6-CHAIN-THEOREM-5.2')))],'The exact universal-coefficient theorem printed in the characteristic provider gives the evaluation isomorphism when the preceding homology group vanishes.')
add('plain',144,[('Section 4',secs(st,4))],'The local finite-range homology-to-homotopy comparison is applied to the actual loop-space calculation.')
add('plain',145,[('Sections 5--6',secs(odd,5,6))],'The odd-prime actual cooperation cobar and signed Adams-resolution sections prove the completed degree-six vanishing.')
add('plain',146,[('Sections 1--7',secs(st,*range(1,8)))],'The illustration summarizes the local finite-generation and exact unit/completion proof.')
add('plain',147,[('Sections 1--5 here',secs(st,*range(1,6))+' here'),('Sections 6--7',secs(st,6,7))],'The source-credit paragraph distinguishes Strickland original lines from the present finite-generation and exact unit proofs; only the latter local locators change.')
add('plain',148,[('Sections 1--6',secs(odd,*range(1,7))),('human source context and immutable proof links appear in Section 8',r'the original-source context is credited to Peterson \cite[\texttt{cooperations.tex}, lines~269--277]{mapsPetersonPinned}')],'The local actual bar/cooperation proof range is printed. Source section8 was a terminal source/provenance section, already moved with exact retention record; its Peterson original-author context is now cited directly, without an unavailable source-section pointer.')
add('plain',149,[('Section 3',secs(odd,3))],'The complete odd-prime homology-algebra induction retains each generator degree used by the excess estimate.')
add('plain',150,[('Section 5',secs(odd,5))],'The exercise uses the actual t,x cobar classes and signed differential of local section5.')
add('plain',151,[('projective-cooperation Sections 3--5',secs(proj,3,4,5))],'This second occurrence of the shared illustration caption refers to the same actual projective-cooperation maps and factor order.')
for n in [15,16,17,50,51,54,55,56,57,58,59,60,61,62,64,65,66,67,68]:
    add('section',n,[],'The full paragraph was read with the nearby construction; its local section target has the stated algebra, filtration, coefficient-space, tensor, or inverse-limit content. No foreign-source antecedent changes this target.')
add('section',52,[(secs(ad,2),secs(cb,2))],'The entire local Adams section5 is using the explicitly cited degree-six cobar proof. The finite weight filtration in every internal degree is the cobar section2, not the Adams finite-group inverse-limit section2.')
add('section',53,[(secs(ad,1),r'\cite[Section~1]{mapsGoerss2008}')],'The named original author Goerss/arXiv0802.1006v1 and TeX lines98–139 establish that this locator is external Section1 of the opened original. It is not local Adams section1.')
add('section',63,[(secs(st,8),secs(d8,8))],'The actual mod-two completed degree-six permanent-cycle calculation is degree-eight-cooperation section8; the receiving integral section8 is not that proof.')
for n,key,description in [(270,'3.4','complete difference-five R-basis'),(283,'4.3','seven-term correcting cochain B')]:
    source=C/(ad+'.tex');paragraph=source.read_text().splitlines()[n-1]
    before=eq(ad,key);assert before in paragraph
    rows.append({'file':source.name,'line':n,'paragraph':paragraph,'input_kind':'strict_cited_equation_antecedent','record_number':n,'full_context_read':True,'status':'Exact mapping supplied','reason':'The cited '+description+' is in the full cobar companion introduced at the start of this section.','mappings':[{'exact_original_phrase':before,'suggested_tex':eq(cb,key),'target_labels':[lab(cb,'eq:'+key)],'matched_target_content':'The cobar equation '+key+' displays the '+description+' verbatim; the receiving Adams equation with that number has different content.'}]})
evidence={}
for row in rows:
    for mapping in row['mappings']:
        for key in mapping['target_labels']:
            for source in list(C.glob('*.tex'))+list((D/'editorial').glob('I_paperI_course_*.tex')):
                text=source.read_text();marker=r'\label{'+key+'}'
                if marker in text:
                    pos=text.index(marker);evidence[key]={'file':str(source.relative_to(D)),'line':text[:pos].count('\n')+1,'source_sha256':hashlib.sha256(text.encode()).hexdigest(),'actual_target_excerpt':text[max(0,pos-450):pos+900]};break
            else:raise AssertionError(key)
result={**M,'scope':'27 residual plain-locator paragraphs,22 remaining local-section-reference paragraphs, and2 explicitly cited foreign equations in the stable/cooperation chapters; actual target content and source antecedents read. No new full proof or code execution claimed.','rows':rows,'target_evidence':evidence,'counts':{'paragraphs':len(rows),'mappings':sum(len(r['mappings']) for r in rows)},'valid_source_statement_titles_retained':[135,137],'provenance_move':'The odd-prime source-section8 availability clause is replaced by the exact opened Peterson citation; the entire original paragraph is retained above and in the conversion metadata/source-move record.'}
(W/'III_course_stable_locator_review.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(result['counts'])
