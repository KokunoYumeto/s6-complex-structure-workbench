from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re

ROOT=Path('/workspace/scratch/08a92fb2355d/S6_SERIES_PUBLISH')
D=Path(__file__).parent; BASE=D.parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def bind(p):
 assert p.exists(),p
 return {'path':str(p.relative_to(ROOT)),'sha256':sha(p)}
def dump(p,obj):
 assert not p.exists(),('immutable output already exists',p)
 p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
now=datetime.now(timezone.utc).isoformat()
I=ROOT/'S6_SERIES_PUBLISH_I.tex';s=I.read_text()
primary=D/'primary';contexts=D/'bound_inputs';contexts.mkdir(exist_ok=True)
ac=BASE/'primary_inputs/AC2026_current_primary.pdf'
act=BASE/'primary_inputs/AC2026_for_group10.txt';pages=act.read_text().split('\f')
pagebind=[]
for n in [2,53,54,61,62,63,99,100,101,102,103,104,105]:
 p=contexts/f'AC2026_printed_{n:03d}.txt';p.write_text(pages[n-1])
 pagebind.append({'printed_page':n,'pdf_page_1_based':n,'text':bind(p)})

def owning_span(label,proof=True):
 pos=s.index('\\label{'+label+'}')
 envs=list(re.finditer(r'\\begin\{(definition|lemma|proposition|theorem|corollary)\}',s[:pos]))
 start=envs[-1].start();env=envs[-1].group(1)
 end=s.index('\\end{'+env+'}',pos)+len('\\end{'+env+'}')
 if proof:
  p=s.index('\\begin{proof}',end);end=s.index('\\end{proof}',p)+len('\\end{proof}')
 return start,end

spans=[]
for label,proof in [('def:common-conventions',False),('fam:src:A.1.2',True),('mapsI:src:A.1.2',True),('inv:B3.1',True)]:
 a,b=owning_span(label,proof);text=s[a:b]
 p=contexts/('current_I_'+label.replace(':','_').replace('.','_')+'.tex');p.write_text(text)
 spans.append({'label':label,'source':bind(I),'start_offset':a,'end_offset':b,'excerpt':bind(p),'reading_scope':'Complete named statement and complete attached proof actually read; common-conventions is a definition without an attached proof.','use_scope': 'For inv:B3.1, only its explicit zero-section/base relation and cusp regluing construction is used; its separate n>1 covering conclusion is not specialized to n=1.' if label=='inv:B3.1' else 'The exact formulas, maps and hypotheses in this excerpt.'})
a,b=owning_span('fam:src:A.3.1',True)
proofpos=s.index('\\begin{proof}',a)
items=list(re.finditer(r'\\item',s[proofpos:b]));third=proofpos+items[2].start()
# Retain the entire first two proof items and the first three glue sentences.
end=s.index('The distinguished base',third)
p=contexts/'current_I_fam_A31_construction_items.tex';p.write_text(s[a:end])
spans.append({'label':'fam:src:A.3.1','source':bind(I),'start_offset':a,'end_offset':end,'excerpt':bind(p),'reading_scope':'Complete proposition plus the full first two construction proof items, and the first two sentences of the third glue item, actually read. No new claim to reread the later even-shift proof.','use_scope':'Current period covariance, finite root action PD7, connector PD8, full cusp matrix PD9 and Psi action PD11, proved free/proper cusp action, and the same period overlap.'})

imgs=[]
for name in ['AC2026_printed062.png','AC2026_printed099.png','AC2026_printed101.png','AC2026_printed105.png','Cartan1957_printed080.png','SchnellLecture3_p004.png']:
 imgs.append({'image':bind(primary/'images'/name),'actual_whole_image_viewed_and_read':True,'scope':'Primary-source page only; no Paper II rendered-page credit.'})

prim={
 'schema_version':1,'paper':'II','created_utc':now,'checker':'i_provenance_recovery',
 'timing':'Additional precise input-source checks after all ten target derivations were frozen and released. These checks do not alter prereading timestamps or supply an extra event.',
 'download_receipt':bind(primary/'download_receipt.json'),
 'AC2026':{'url':'https://alpo.ge/s6.pdf','pdf':bind(ac),'edition':'The exact 108-page 2026 manuscript already attached and separately downloaded with identical bytes in group09.','actual_reading':'Setup p.2; complete Lemma7.13/Proposition7.14 on pp.53–54; complete Lemma7.25/Propositions7.26–7.27 on pp.61–63; complete LemmaA.4 on pp.99–100; complete TheoremB.1 proof on pp.101–105. The initially truncated p.62 and p.101–102 outputs were separately reread in full before this receipt. No whole-manuscript reading is claimed.','page_text_bindings':pagebind,
   'inputs':[
    {'locator':'Proposition7.26, pp.61–62','use':'Common invariant two-forms Zq, global coinvariants Z[delta], H0(R2)=Z(2q), H2(R1)=Z omega[delta].'},
    {'locator':'Proposition7.27, pp.62–63','use':'d2(2q)=epsilon p omega_AC[delta], with one common epsilon in {+1,-1} and p=12ell0−4ell1−3ell2. The standard values give p=−1.'},
    {'locator':'LemmaA.4, pp.99–100','use':'The degree-four finite cover has injective integral pullback with image {a gamma eta2+bq : a=b mod2}; the full parity proof was read.'},
    {'locator':'TheoremB.1, pp.101–105','use':'Integral specialization is an isomorphism onto monodromy invariants. Its degree-two injectivity and natural nearby-cycle unit, not an unproved identification of an H1 result with H2, are used.'}]},
 'Schnell':{'url':'https://www.math.stonybrook.edu/~cschnell/mat615/lectures/lecture3.pdf','pdf':bind(primary/'Schnell_lecture3.pdf'),'edition':'Lecture3, February4; no year specified in the document.','actual_reading':'All seven text pages reread; p.4 also actually viewed. Example3.5 p.4 gives the left-module crossed/principal quotient. Equations3.3–3.4 p.3 and3.8–3.10 pp.6–7 give the factor, logarithmic connecting cocycle, and Chern alternation.'},
 'Cartan1957':{'url':'https://www.numdam.org/article/BSMF_1957__85__77_0.pdf','pdf':bind(primary/'Cartan1957.pdf'),'doi':'10.24033/bsmf.1481','actual_reading':'Section2 fundamental TheoremB on printedp.80, including coherent sheaf scope and q>=1, read in text and the complete page image. The neighbourhoods used are explicitly Stein.'},
 'Stacks':{'pages':[{'tag':tag,'url':'https://stacks.math.columbia.edu/tag/'+tag,'html':bind(primary/('Stacks_'+tag+'.html'))} for tag in ['09V6','012O','012U','012W']], 'actual_reading':'09V6 proper topological base change and its proof, and012O/012U/012W filtered-complex functoriality/convergence statements and proofs, actually read. The underlying proper topological map of the constructed proper holomorphic family meets09V6. Tags011N/011O are used only for the standard spectral-sequence definitions already read.'},
 'CLS2010':{'url':'https://pi.math.cornell.edu/~tsh/cornell-only/cox-little-schenck-toric.pdf','edition':'2010 text, preface September2010; the publication entry remains AMS2011, DOI10.1090/gsm/124.','access_scope':'The exact primary PDF is indexed and its text was opened through the retrieval service. Direct PDF download returned403; no successful local PDF download or page-image reading is claimed.','actual_reading':'Full Example1.2.21 p.31, Propositions4.1.1–4.1.2 and proofs p.171, Theorem4.2.8 and proof p.181, Theorem4.2.12 and proof p.184. These passages were reopened by exact earlier source references and line contexts after the broad fresh search failed to return the desired loci.','retrieval_refs':['turn171257621view0','turn147949148view0','turn147949148view1','turn147949148view2'],'use':'The basis-change character ring gives C^r times (C*)^(n-r); character orders are primitive-ray pairings. Cartier local characters and their face congruences determine an integral support function with negative divisor coefficients. The proposal retains the exact local characters and their signs.'},
 'unverified_redundant_book_locators':{'Brown1982':'The precise cited book pages were not opened. Replace the crossed/principal quotient citation with the actually read Schnell Example3.5, while retaining the graph cochain proof.','BirkenhakeLange1999':'The precise Theorem2.1p.7 text was not opened. Remove this redundant locator from this owning block; use the actually read Schnell factor computation.','Dimca2004':'The precise Theorem2.3.26 text was not opened. Replace this locator with the actually read Stacks09V6, retaining the actual proper-base-change square.'},
 'actual_page_images':imgs,'current_I_bound_inputs':spans,'canonical_mutations':0,'events_added':0
}
dump(D/'S6_SERIES_PUBLISH_II_clean_group10_primary_receipt.json',prim)

transport={
 'schema_version':1,'paper':'II','created_utc':now,'current_I':bind(I),'primary_receipt':bind(D/'S6_SERIES_PUBLISH_II_clean_group10_primary_receipt.json'),
 'construction_morphism':[
  'Choose the AC setup functions tau,mu,beta equal to current Paper I tau,mu,beta_part+c for the standard member under consideration. The current period inequality is AC(beta3); the same transformation laws and bounded cusp extension are the displayed construction hypotheses. This selects the same admissible functions, rather than assuming that distinct period functions define the same family.',
  'On each lifted ordinary chart define F_mid(z,[zeta])=(z,[zeta]) using the same marked period matrix Pi. Pi(gz)=R_g(z)Pi(z)A_g^{-1} in both constructions, so this identity intertwines every period translation and linear deck action.',
  'On each full finite root cover define F_j(s,[zeta])=(s,[zeta]). Both actions are (s,zeta)->(g_js,R_g(s)zeta+Pi(g_js)v_j/m_j), with m1=3,m2=4 and the exact vectors (1,2,-4,0),(-1,-3,3,0). The identity therefore descends to the finite quotient and restricts to the same pi_j on its central torus.',
  'On the cusp toric cover define F_0(t,x)=(t,x), with the identity on the height-one cocharacter lattice. Both fan automorphisms send (y,y3) to(y+y3 B0 lambda,y3), and both torus multipliers are exp(2pi i C(t)lambda) for the same full C. Thus F_0 Psi_AC=Psi_current F_0 on the dense torus and every toric chart; it descends to the quotient.',
  'Both finite connectors are zeta->zeta+(log s_j)/(2pi i)Pi(s)v_j, and both cusp connectors are (z,zeta)->(exp(2pi i zeta1),exp(2pi i zeta2),exp(2pi i s)). The identities commute with these connectors and therefore glue to a base-preserving biholomorphism of the two standard constructions. The inverse is the same identity in every chart.',
  'Pullback by this glued map identifies the marked smooth fibre cohomology, the finite-cover pullbacks, and the constant-sheaf-to-nearby-cycles unit. Proper pushforward and its natural base changes consequently identify the E2 terms and differentials. This transports the cited AC inputs to the current standard family without replacing degree-two specialization by an H1-only result.'
 ],
 'orientation_and_deck_map':bind(D/'S6_SERIES_PUBLISH_II_boundary_deck_convention_addendum.json'),
 'IM_generator':{'root_scope':bind(ROOT/'records/S6_SERIES_PUBLISH_II_IM_omega_root_scope.json'),'map':'omega=epsilon*p*omega_AC, where epsilon is the actual common differential sign of AC7.27 and p=−1. Equivalently omega[delta]=d2(2q). The coefficient is a unit of Z, so this names a primitive generator and preserves the displayed d2 formula. No numerical epsilon is claimed.'},
 'IH_selected_lift':{'definition':'The root point is selected by the fixed zero-section whisker. For a chosen logarithm branch alpha, zeta0=−alpha0 Pi(s)v; H(s,zeta0)=(s,0).','endpoint':'Clockwise alpha1=alpha0−1/m and Pi(gs)v=R_g Pi(s)v imply zeta1=R_g zeta0+Pi(gs)v/m, exactly Q_log(zeta0). The same selected point is the logarithmic endpoint of the chosen whisker.','arbitrary_lift_map':'Changing the initial point to tau_lambda x translates the lifted path by tau_lambda. Its endpoint deck element is tau_lambda Q_log tau_(−lambda)=tau_((I−A)lambda) Q_log. Thus the old arbitrary-choice paragraph did not justify the unqualified point-valued endpoint. The selected lift repairs that claim; all group extensions, norm identities and final conclusions remain unchanged.','orientation':'In the chart t=rho exp(i theta), b_plus=a_u and f=m_x2−a_u. The clockwise b is −b_plus, so b wedge f=−a_u wedge m_x2. The extending-frame winding is zero in both orientations.'},
 'frozen_derivation_qualifications':[
  'The common frozen prose called A_g the actual homology parallel transport while writing the left deck dual T=A^-t. This terminology is corrected only in the dated deck addendum and current proposal; original derivation bytes remain unchanged.',
  'The frozen IL derivation deliberately uses E=nq and a real half-coefficient, proving n=0 without parity. The printed proof retains E=2nq; its stronger parity input is separately verified by complete AC LemmaA.4.',
  'The frozen ID derivation used the established cusp tube as an additional interpretation of restriction. The printed proof needs only the natural nearby-cycle unit; the complete AC TheoremB.1 supplies this exact map and integral injectivity.',
  'The frozen IH derivation obtains the norm by the explicit swept cap torus and factor commutator. The printed proof uses the filled central extension and universal-cover comparison; that longer argument was read completely, and its selected-lift and orientation qualifications are explicit.',
  'The frozen I6 derivation obtains support data from windings of analytic frames and finite differences. The printed proof uses a Cartier comparison bundle and normalized component frames. Both exact frame equations yield E_M((lambda,0),(0,m))=−B(B0 lambda,m).'
 ],'canonical_mutations':0,'events_added':0}
dump(D/'S6_SERIES_PUBLISH_II_clean_group10_exact_transport.json',transport)

old1=ROOT/'agents/i_provenance/programs/S6_SERIES_PUBLISH_I_primary_cusp_hexagon_exact.py'
old2=ROOT/'agents/i_analytic/programs/S6_SERIES_PUBLISH_I_root_primary_cusp_and_finite_exact.py'
method={
 'schema_version':1,'paper':'II','created_utc':now,
 'fresh_code':bind(BASE/'clean_derivations/S6_SERIES_PUBLISH_II_boundary_preproof_exact.py'),
 'fresh_output':bind(BASE/'clean_derivations/S6_SERIES_PUBLISH_II_boundary_preproof_exact.output.json'),
 'fresh_timing':'Written, executed, and completely read before the eight22:05:10–11 freezes and all ten22:05:30 releases; the already frozen IM/DR proofs remained closed throughout.',
 'fresh_method':'Pure Python integer/Fraction matrix arithmetic and Gaussian inversion; tensor-grid evaluation with proven per-variable degree bounds certifies polynomial identities by the univariate interpolation theorem applied successively. Basis tests certify the linear degree/support maps. The written proofs establish the analytic and unrestricted claims.',
 'prior_owner_search':bind(ROOT/'records/S6_SERIES_PUBLISH_II_group10_root_historical_program_associations.json'),
 'prior_scope':'The forty exact owner associations and ten current end-program rows identify no filename for a target routine. IN ce:1990761c9345c839c9d8 and I6 ce:b92aca063fdfb8162976 say unnamed program rerun. This is a bounded-record finding, not an assertion that no historical program exists.',
 'related_positive_programs':[
  {'code':bind(old1),'actual_reading':'Entire5074-byte source read after release; not executed in this group.','method':'SymPy/fan automorphism enumeration and oriented side/character transport checks for Paper I fam:C4.1.','relationship':'No IN/I6 support computation is identified by this program. It is retained as a positively located related chart program only.'},
  {'code':bind(old2),'actual_reading':'Entire6536-byte source read after release; not executed in this group.','method':'SymPy symbolic expansion/cancellation of quadratic Cartier, support-shift and cocycle identities, followed by finite Gaussian-lift and connection algebra.','relationship':'Its full C(t) character/divisor algebra overlaps the new IN/I6 finite identities. The fresh program instead uses exact tensor-grid coefficient certification and Fraction linear algebra. This is a different algorithm for the overlapping polynomial claims; it does not identify the unnamed historical owner routine.'}],
 'printed_calculation_comparison':{'03IE':'The printed proof substitutes the full real translation differential into the vertical form; the frozen derivation instead computes its cap sweep through an explicit homotopy of the periodic real correction.','03IN':'The analytic character-sheaf and exponential-cocycle identities are proved for all integral inputs in both written arguments; the independent exact polynomial/basis program corroborates the finite arithmetic by coefficient-complete interpolation.','03I6':'The frozen finite-difference derivation and printed normalized-frame/Cartier comparison both identify the actual mixed Chern map. The finite new program certifies support coefficient recovery and B0 inversion; it does not purport to prove analytic frame existence.'},
 'no_extra_computation_event':True,'canonical_mutations':0,'events_added':0}
dump(D/'S6_SERIES_PUBLISH_II_clean_group10_computation_methods.json',method)

name={
 'schema_version':1,'created_utc':now,'paper':'II','scope':'Dated clarification of the group09 bibliography reason; no new source edit or check event.',
 'original_record':bind(BASE/'clean_group09/S6_SERIES_PUBLISH_II_clean_group09_final_proposals.json'),
 'primary_author_page':{'url':'https://dacox.people.amherst.edu/toric.html','html':bind(primary/'Cox_author_page.html'),'name_form':'Hal Schenck'},
 'primary_publication_metadata':{'url':'https://experts.illinois.edu/en/publications/toric-varieties','html':bind(primary/'CLS_publication_metadata.html'),'name_form':'Henry K. Schenck','same_publication_doi':'10.1090/gsm/124'},
 'correction':'The earlier explanation should not characterize Henry K. Schenck as an incorrect author identity. Both name forms are supported by primary records for the same publication. The current Hal form is retained because it is the book authors own page form. The statement/page edition remains the explicitly identified2010 text, and the published bibliography remains2011. Original group09 evidence is not overwritten.',
 'canonical_mutations':0,'events_added':0}
dump(D/'S6_SERIES_PUBLISH_II_CLS_author_reason_dated_addendum.json',name)
for name in ['primary_receipt','exact_transport','computation_methods']:
 print(json.dumps(bind(D/f'S6_SERIES_PUBLISH_II_clean_group10_{name}.json')))
print(json.dumps(bind(D/'S6_SERIES_PUBLISH_II_CLS_author_reason_dated_addendum.json')))
