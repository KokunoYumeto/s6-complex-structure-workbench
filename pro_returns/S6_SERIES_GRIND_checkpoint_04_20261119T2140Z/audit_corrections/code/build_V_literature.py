"""Source comparison and proposed edits only; never edits shared manuscripts."""
from pathlib import Path
import csv, hashlib, json

here = Path(__file__).resolve().parents[1]
actor = 'GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited from root (not separately exposed), S6_SERIES_GRIND/corrections_audit'

patches = [
 dict(label='night:P1.9', operation='replace_complete_proof', status='known, cited specialization',
      source='Yang2026, Theorem 8.7 and Corollary 8.8, attached source lines 4674–4848; unmodified-body aux pp.56–58',
      tex=r'''\begin{proof}
\begin{enumerate}[label=\arabic*.]
\item Apply \cite[Theorem~8.7 and Corollary~8.8, pp.~57--59, attached-source edition]{Yang2026}
with $n=3$, $t=q$, $D(q)=C(q)$, $B=I_3$, and the displayed
periodic Kuhn triangulation.  These substitutions give exactly the
action
\[
 (z,q)\longmapsto
 \bigl(q^\lambda\exp(2\pi iC(q)\lambda)z,q\bigr)
\]
and the period order $[I_3\mid sI_3+C(q)]$, where
$q=\exp(2\pi i s)$.  Thus the identity on the dense torus, with
the same integral monomial charts, identifies our quotient with
the cited quotient.  The source theorem supplies its smoothness,
Hausdorffness, properness, and the reduced local equations
$q=x_0\cdots x_k$.  Flatness follows since this nonconstant
function is a nonzero divisor in each smooth chart.
\item For an index-$d$ period sublattice $\Gamma=B\mathbb Z^3$,
the same substitutions give the source's quotient map induced
by $\Gamma\subset\mathbb Z^3$.  It has degree $d$, and
Corollary~8.8 gives $\chi(W)=3!d=6d$ for this marked Kuhn fan.
\end{enumerate}
\end{proof}'''),
 dict(label='maps:src:F.1.1', operation='replace_complete_proof', status='known local formula, short global specialization',
      source='Yang2026, Corollary 8.8, attached source lines 4827–4848; aux p.58',
      tex=r'''\begin{proof}
\begin{enumerate}[label=\arabic*.]
\item The specified rank-three Kuhn fibre is the case $n=3$
of \cite[Corollary~8.8, p.~59, attached-source edition]{Yang2026}: the identical
height-one fan and the inclusion $\Gamma\subset\mathbb Z^3$
identify its index-$d$ quotient, and give central Euler number
$3!d=6d$.
\item The regular fibre has Euler number $\chi(T^6)=0$.
Each other reduced fibre is a free finite quotient of $T^6$,
so its Euler number is also zero.  Euler additivity for the
stated proper triangulable map therefore gives $\chi(M)=6d$.
\end{enumerate}
\end{proof}'''),
]
(here/'V_known_result_proof_patches.json').write_text(json.dumps(patches,indent=2,ensure_ascii=False)+'\n')
(here/'V_known_result_proof_patches.tex').write_text('\n\n'.join('% '+p['label']+'\n'+p['tex'] for p in patches)+'\n')

front = {
'series:V:A':r'''\textit{Relation to literature.}
The threefold factor is the construction of
\cite[Theorems~7.17 and 7.22, pp.~57 and 60]{AC26}, and the
elliptic equation is the one in \cite[\S2, initial construction]{E26}.
The local Kuhn quotient is the $n=3$, $D=C_3$ specialization of
\cite[Theorem~8.7 and Corollary~8.8, pp.~57--59, attached-source edition]{Yang2026}.
The additional global construction is the small crepant resolution
with the integral period morphism
$AZ_3B^{-1}=\operatorname{diag}(Z_2,s+c_E)$ in
\cref{maps:src:E.1.2}; its invariants are calculated in
\cref{maps:src:E.2.1}.  The characteristic polynomials are the
known identities \cite[equations~(1.2)--(1.4), pp.~3--4]{ffEsoleKang},
and the class-$\mathcal C$ obstruction uses
\cite[Theorem~1.1 and Remark~1.2, p.~2]{ffJiaMeng}.''',
'series:V:B':r'''\textit{Relation to literature.}
The local toroidal filling and its Euler number are the marked
$n=3$ specialization of \cite[Theorem~8.7 and Corollary~8.8,
pp.~57--59, attached-source edition]{Yang2026}.  The global integral specialization
method extends the calculation in \cite[\S7.7]{AC26}.
Here the displayed rank-six restriction maps and order-four
norm/prism map supply the integral groups and the form $I_{3,1}$.
These specific lattice and boundary maps are the additional
calculation asserted in this theorem.''',
'series:V:C':r'''\textit{Relation to literature.}
The construction uses the explicit morphism
$\ell_0\otimes(\mathcal H_{\mathrm{dR}}/\ell_0)
\to\bigwedge^2\mathcal H_{\mathrm{dR}}/\mathbb C\omega$,
$u\otimes[v]\mapsto[u\wedge v]$, and the index-two integral
map in \cref{night:P1.2}.  These formulas specify the
relation to the polarized genus-two variation.  The cited
toroidal quotient is applied through \cref{night:P1.9};
the particular pencil, integral quotient, and split rank-three
plane are the constructions proved here.''',
'series:V:D':r'''\textit{Relation to literature.}
The oriented extended-form classification and Kramer--Stolz
absorption theorem are the known results cited in
\cref{maps:src:F.4.1}.  The almost-complex compatibility is
also known from \cite[Theorems~1--2, pp.~2--3]{Yang2012AC}
and \cite[Theorem~1.3 and Corollary~1.4, pp.~3--4]{ffMandal}.
Explicitly, transporting the constructed integrable structure
by the oriented diffeomorphism gives a complex vector bundle
$(TN,J)$ whose realification is $TN$, with
$c_2=-\sum x_i$, $c_4=6u$, and $p_2=14u$.
In Mandal's normalization $x_i^2=\epsilon_i u$,
$\epsilon=(1,1,1,-1)$, his two conditions are
$14\equiv2\pmod4$ and $14-2=2\cdot6$.
The theorem here supplies the compact integrable realization
and its explicit normal-data comparison.''',
'series:V:E':r'''\textit{Relation to literature.}
The root-base and direct-image method is the one in
\cite[Lemmas~6.1--6.2 and Proposition~6.10]{DGKX2026v1};
\cref{night:P1A.1} applies its cup-product and base-change
maps to the displayed rank-three bundle on the $(5,4)$ root curve.
The coefficient $c_*$, the rank-six cohomology and
isomorphism calculations, and the two endpoint assertions are
the specific results proved here.  The torus-deformation input
for \cref{night:P1A.5} is \cite[Theorem~2.1, p.~264]{Catanese2004};
its application is to the smooth compact torus fibres produced
inside that argument.  The punctured-disc filling of
\cref{night:P1A.6} uses its interior parameter limit and
the explicit $\mathbb C\times\mathbb Z/2$ torsor reduction.
The full splitting translation
$\xi_b=\xi_{\rm original}-a_{\rm split}$ is retained.'''
}
(here/'V_literature_front_patches.json').write_text(json.dumps([dict(label=k,operation='replace_relation_to_literature_paragraph',tex=v) for k,v in front.items()],indent=2,ensure_ascii=False)+'\n')

bridge=r'''% Suggested Known and new subsection addition; no new theorem.
\paragraph{The exact root-curve comparison.}
Let $\lambda_*=-256/3125$ and set
$t=\lambda_*/(\lambda_*-\lambda)$, sending the order-five,
order-four, and cusp points to $0,1,\infty$.  Let $\mathcal R$
have root orders $15,4$ at $0,1$, with reduced root divisors
$D_1,D_2$, and put $T=\mathcal O(4D_1-D_2)$.
There are root maps $q_3:\mathcal R\to\mathcal B_{3,4}$ and
$q_5:\mathcal R\to\widehat B_{5,4}$; their first root
coordinates are $s_3=s_{15}^5$ and $s_5=s_{15}^3$ and their
order-four coordinate is unchanged.  Thus
\[
 q_5^*L_{5,4}=\mathcal O(12D_1-3D_2)=T^3,
 \qquad q_3^*L_{3,4}\simeq T^5.
\]
For the second identity the two divisors differ by
$15D_1-4D_2=\operatorname{div}(t/(t-1))$; multiplication by $t/(t-1)$ gives the explicit map
$T^5\to q_3^*L_{3,4}$.
Consequently the pullbacks of the two first direct images are
$\mathcal O\oplus T^{-5}$ and
$\mathcal O\oplus T^{-3}\oplus T^{-6}$, respectively.
The exterior-power identifications in both calculations are
the actual cup-product morphisms after these pullbacks.
This states the shared sheaf calculation and all base and
line transports used in the comparison.
'''
(here/'V_root_curve_comparison.tex').write_text(bridge)

bib=r'''@article{Yang2012AC,
  author = {Yang, Huijun},
  title = {Almost Complex Structures on $(n-1)$-Connected $2n$-Manifolds},
  journal = {Topology and its Applications},
  volume = {159},
  year = {2012},
  pages = {1361--1368},
  doi = {10.1016/j.topol.2011.12.013},
  eprint = {1110.1798},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/pdf/1110.1798},
  verification = {verified at listed scope},
  source_note = {Opened the primary arXiv v1 full PDF in this run, Theorems 1--2 on preprint pages 2--3 and the realification map on page 1. Used for the stable/almost-complex compatibility of the specified oriented manifold; the integrable realization is supplied by the receiving construction.}
}
'''
(here/'V_reference_addition.bib').write_text(bib)

rows=[]
def row(label,classification,prior,relation,evidence,risk=''):
    rows.append(dict(statement_id=label,literature_status=classification,opened_prior_locators=prior,explicit_relation=relation,search_evidence=evidence,remaining_risk=risk))
common='AC26 original PDF §§3–8; E26 attached §2; DGKX v1 §§2,6,7 and v2 §§2–3; bounded searches V-L01–V-L12'
row('night:P1.9','known and cited specialization','Yang2026 Thm8.7 and Cor8.8, source 4674–4848, aux pp56–58','n=3, t=q, D=C, Gamma=BZ^3; same fan and period order, identity on dense torus extends in the identical monomial charts','Attached full statement and complete proof opened','Compiler map issue does not affect source reading; exact source labels retained.')
row('maps:src:F.1.1','known local formula plus short global specialization','Yang2026 Cor8.8, source 4827–4848, aux p58','central Euler n!d=6d; regular and free finite-quotient torus fibres have Euler zero; Euler additivity','Attached full source opened')
row('maps:src:F.4.1','new integrable realization in searched corpus; known classification inputs','Wall extended-form theorem as CCPS Def3.6/Thm3.7; Kramer–Stolz ThmA p178; Mandal Thm1.3/Cor1.4 pp3–4; Huijun Yang Thms1–2 preprint pp2–3','Oriented q,p1-preserving normal-clutch isometry; homotopy-sphere absorption; actual realification (TN,J) -> TN, c2=-sum xi,c4=6u,p2=14u',common,'A bounded search records what was opened; it proves no worldwide absence.')
row('night:P1.18','specific exact threshold not found in the recorded corpus','AC26 original §3 and DGKXv1 §2 supply marked-period family method; Yang2026 Thm8.7 supplies local filling','Full splitting transport xi_b=xi_original-a_split; F planes agree exactly; original real line has both translated real and imaginary components',common,'Independent Arb reconstruction is owned by paper_i_audit; missing original certificate files are not certified by this source comparison.')
for lab,claim in [('night:P1A.1','direct images, canonical line and h0q'),('night:P1A.2','5-by-5 Hodge table'),('night:P1A.3','tangent tuple and one-dimensional smooth Kuranishi germ'),('night:P1A.4','algebraic dimension one, C x Z/2 automorphisms, exact parameter classification')]:
    row(lab,'specific rank-six calculation not found in the recorded corpus; shared method credited','DGKXv1 Lems6.1–6.2 and Prop6.10 (source8541,8631,9151); tangent Thm6.12, Kuranishi Prop6.16, classification Thm7.14','Common (15,4) root curve: q3*L34=T^5, q5*L54=T^3; first direct images O+T^-5 and O+T^-3+T^-6; cup-product maps identify exterior powers. Receiving claim: '+claim,common,'No equivalence of the full families is asserted from this sheaf comparison.')
row('night:P1A.5','specific endpoint nonextension not found in the recorded corpus; torus-deformation input credited','Catanese2004 definition p261 and Thm2.1 p264; proof pp267–268; E26 §4 first Additional remarks item source1647–1683','Catanese applies to the smooth compact torus subfamilies extracted in the proof; root/source periodic quotient is the n=3 specialization above. E26 stated untwisted filling as conjectural and then asked about transformed members.',common,'This event compares the cited source scope; it does not re-prove the full endpoint argument.')
row('night:P1A.6','specific disc classification not found in the recorded corpus','P1A.3 local completeness and P1A.4 exact isomorphism/automorphism input; Catanese2004 source-scope comparison','Holomorphic class map to half-plane extends to an interior point; additive torsor killed by H1(Delta*,O)=0 and component torsor by at most double cover. Thus this is an interior filling of the class map; P1A.5 concerns a full disc across its boundary.',common,'The source comparison does not certify the complete torsor proof.')
row('maps:src:E.1.1','correction of attached proposed normalization','Attached MAPS Lead6; receiving complete proof; DGKXv2 §3 normalized reduced fibre product at source2195–2214','A finite normalization cannot contract the seven IV* or two III components that dominate the original central components; the suggested good-reduction quotient central fibre is irreducible. DGKX reduced-root normalization instead unwraps its already free affine quotient charts.',common,'Refutes the named literal normalization only; no assertion that the models have no birational relation.')
row('maps:src:E.1.2','new global resolution in searched corpus; local quotient known','E26 §2 equation y²=x³−3t³(t−1)x+2t⁴(t−1)²; AC26 Thms7.17/7.22; Yang2026 Thm8.7','A Z3 B^-1=diag(Z2,s+cE), with A=(P;r), B=(B0^-1 P;r), det A=det B=1. The n=3 quotient is a Yang specialization; the toric fan map via (P,r) refines triangle×interval without new rays, giving the small crepant morphism.',common)
row('maps:src:E.1.3','specific integral central calculation not found in recorded corpus','Yang2026 Thm8.7/Cor8.8 local model; Chen2021 ThmB and Deligne weight input retained from attached bibliography','Exact cellular quotient uses same rank-three Kuhn fan; rational invariant-cycle surjectivity alone supplies no integral saturation',common,'Chen exact primary source not newly opened in this comparison; historical verified locator retained only.')
for lab in ['maps:src:E.1.4','maps:src:E.1.5']:
    row(lab,'specific global topology calculation not found in recorded corpus','AC26 Thms7.17/7.22; Yang2026 §8.3; receiving actual boundary maps','Finite-root and rank-three central maps are glued through the explicit E.1.2 period/fan morphism; finite-fibre torsion cancellation is the receiving integral calculation',common,'No blanket reduction of the torsion computation to rational invariant cycles.')
row('maps:src:E.2.1','new invariants of the constructed resolution in searched corpus; universal formulas credited','Esole–Kang1807.08755v1 eqs1.2–1.4 pp3–4; Jia–Meng2201.06748v1 Thm1.1/Rem1.2 p2','Substitute c1=0,c2²=2,c4=6 into Todd and Pontryagin polynomials: p1²=8,p2=14,sigma=2. A Kahler modification would preserve H1 and H1(O); its equality b1=2h01 contradicts 0=2.',common,'Only the displayed universal polynomials are used; no unproved extension of algebraic crepant-invariance claims is inferred.')
row('maps:src:E.2.2','known and cited base change / Kunneth specialization','Receiving statement already titled Credited re-derivation','The actual map ((x,(b,n))) -> (x,n), inverse (x,n)->(x,(f(x),n)), identifies X×_B(B×N) with X×N holomorphically; oriented X≅S6 then gives the two Kunneth summands',common)
for lab in ['maps:src:E.2.'+str(i) for i in range(3,22)]:
    row(lab,'supporting shifted-product statements: retain existing credit; bounded comparison only','AC26 threefold input; E.2.2 base-change morphism; receiving shifted cusp/cap maps','The dimension is dim_C(Y)+2 for X×_B Y; the shifted product of two threefolds is complex dimension five. No fourfold characteristic formula is transported to it merely by matching a title.',common,'This broad source-comparison pass is not a fresh complete proof audit of these long supporting statements.')
with (here/'V_literature_comparison.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)

queries=[
('V-L01','system2','"3" "quaternionic projective planes" "complex" Mandal','Mandal2609.27929 located; attached full source opened.'),
('V-L02','system2','"almost complex structures" "(n-1)-connected" "Yang" 2012; domains arxiv','Huijun Yang1110.1798 located and primary full PDF opened.'),
('V-L03','system2','"complex fourfold" "genus two" "half-plane" torus; domains arxiv','No matching exact rank-six family theorem in returned results.'),
('V-L04','system2','"complex fourfold" "quaternionic" "connected sum"; domains arxiv','No additional exact integrable construction in returned results.'),
('V-L05','system1','"complex fourfold" "3HP" OR "quaternionic"','Returned broad catalogue/secondary results; no exact primary theorem adopted.'),
('V-L06','system1','"genus two" "fourfold" "torus" "complex"','Returned unrelated broad results; no exact primary theorem adopted.'),
('V-L07','system1','"complex fourfold" "half-plane"','Returned broad half-plane/catalogue results; no exact primary theorem adopted.'),
('V-L08','system2','"Characteristic Numbers of Crepant Resolutions of Weierstrass Models" pdf','Primary arXiv1807.08755 PDF opened; v1 eqs1.2–1.4 matched.'),
('V-L09','system2','"Equivariant Kähler Model for Fujiki" pdf','Primary arXiv2201.06748 PDF opened; v1 Thm1.1/Remark1.2 matched.'),
('V-L10','system2','"y^2=x^5" "lambda" "complex fourfold"','No exact theorem match in returned results.'),
('V-L11','system2','"3HP" "complex"','No additional primary exact analytic-construction result in returned results.'),
('V-L12','attached full-text searches','fourfold|eight-dimensional|quaternionic|genus two|genus-two|rank-six in AC26 original, E26, DGKXv1/v2','No direct statement of the target rank-six theorem found by these terms; positive source relations separately recorded.'),
]
with (here/'V_literature_searches.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['search_id','date','engine_or_corpus','query','observed_outcome','scope']);
    for id,engine,q,out in queries:w.writerow([id,'2026-11-19',engine,q,out,'Bounded search only; no worldwide absence assertion.'])

opened=[
dict(key='Yang2012AC',url='https://arxiv.org/pdf/1110.1798',ref='turn315964924view0',locator='Theorems1–2 pp2–3; realification p1',status='primary full PDF opened'),
dict(key='Catanese2004',url='https://www.mathe8.uni-bayreuth.de/de/team/prof-fabrizio-catanese-old/pdf/085.pdf',ref='turn875696222view0',locator='definition p261; Theorem2.1 p264; Theorem2.7 and proof pp267–268',status='primary full PDF opened'),
dict(key='ffEsoleKang',url='https://arxiv.org/pdf/1807.08755',ref='turn711525144view0',locator='v1 eqs1.2–1.4 pp3–4',status='primary full PDF opened; version-suffixed URL initially DisabledError'),
dict(key='ffJiaMeng',url='https://arxiv.org/pdf/2201.06748',ref='turn841575312view1',locator='v1 Theorem1.1 and Remark1.2 p2',status='primary full PDF opened; version-suffixed URL initially DisabledError'),
dict(key='ffMandal',url='https://arxiv.org/abs/2609.27929',ref='turn694321972view0',locator='attached FINAL.tex Thms1.1/1.3/Cor1.4; source223–309; aux pp3–4',status='attached full source opened; public exact URL DisabledError'),
dict(key='ffMandalLater',url='https://arxiv.org/abs/2610.02147',ref='turn694321972view3',locator='none',status='full text unverified; exact abs and v1 URL DisabledError; no proof support'),
]
(here/'V_opened_primary_sources.json').write_text(json.dumps(opened,indent=2,ensure_ascii=False)+'\n')

events_path=here/'CHECK_EVENTS.tsv'
with events_path.open(newline='') as f:
    rr=csv.DictReader(f,delimiter='\t');fields=rr.fieldnames;events=list(rr)
for r in rows:
    if r['statement_id'].startswith('maps:src:E.2.') and int(r['statement_id'].split('.')[-1])>=3:continue
    outcome='Literature comparison: '+r['literature_status']+'. Opened/matched: '+r['opened_prior_locators']+'. Exact relationship: '+r['explicit_relation']+'. '+r['remaining_risk']+' Source details and bounded searches: audit_corrections/V_literature_comparison.tsv and V_literature_searches.tsv. This is a source-scope check, not a fresh complete re-proof.'
    eid='s6sg:'+hashlib.sha256((r['statement_id']+'V_lit'+outcome).encode()).hexdigest()[:20]
    if not any(x['event_id']==eid for x in events):events.append(dict(statement_id=r['statement_id'],date='2026-11-19',who=actor,type='targeted proof check',outcome=outcome,event_id=eid,phase='S6_SERIES_GRIND'))
with events_path.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(events)
print(json.dumps({'comparison_rows':len(rows),'total_audit_events':len(events),'proof_patches':len(patches),'front_patches':len(front)}))
