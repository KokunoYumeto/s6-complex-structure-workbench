#!/usr/bin/env python3
"""Guarded source corrections and bounded records for main C's exposed comparison."""
from pathlib import Path
from datetime import datetime, timezone
import csv,re
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation4_horizontal'
s=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
WHO='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited reasoning effort not separately exposed; fourth continuation, horizontal/global-C review'
STAMP=datetime.now(timezone.utc).isoformat(timespec='seconds')
rows=[]
def guard(ident,old,new,owner,reason):
 assert s.count(old)==1,(ident,s.count(old))
 rows.append(dict(change_id=ident,old_text=old,new_text=new,owner=owner,reason=reason))
guard('II-C4-C-SOURCE',r'''\StatementRecord{series:II:C}{proved}{03K4}{\SeriesRef{cdp:st:D.2.7}, \SeriesRef{cdp:st:C.2.G.1}, \SeriesRef{night:P4.58}, \SeriesRef{cdp:st:D.2.5}}''',r'''\StatementRecord{series:II:C}{proved}{03K4}{\SeriesRef{cdp:st:D.2.7}, \SeriesRef{cdp:st:C.2.G.1}, \SeriesRef{night:P4.6}, \SeriesRef{cdp:st:D.2.5}}''','series:II:C','P4.6 is the exact single-divisor owner under b2(Y)=0, applied by (X,F)=(Y,S). P4.58 states its full theorem with every support irreducible or normal crossing, an additional global hypothesis absent from C.')
guard('II-C4-C-MAPS',r'''These are the normalization and conductor maps of
the full fibre, including its multiplicities.''',r'''For $Y_b=f^*(b)=\sum_i m_iS_i$ and $S=(Y_b)_{\rm red}$,
the normalization is $\nu:\coprod_iT_i\to S$ and its map
to the full fibre is $j\circ\nu$, where $j:S\hookrightarrow Y_b$
is the reduction inclusion. The scheme conductor is defined by
$\operatorname{Ann}_{\OO_S}(\nu_*\OO_{\coprod_iT_i}/\OO_S)$.
''','series:II:C','Match the criterion to G1/INT3 using the exact reduction inclusion and normalization composite. The full divisor and the scheme conductor are explicit; no multiplicity or equality case is removed.')
guard('II-C4-C-OUTLINE-1',r'''\item\hypertarget{step-II-C-1}{} Connected-fibre Leray makes the
base rational. Finite-character support comparison and local
conductor maps give the irreducible values zero and two and their
normalization descriptions; the normal-crossing calculation gives
the triple-point count
(\cref{night:P4.58},
\cref{cdp:st:C.2.MH.2}).''',r'''\item\hypertarget{step-II-C-1}{} Connected-fibre Leray makes the
base rational. The finite-character comparison for the same full
irreducible fibre and its normalization gives the values zero and
two; the normalization analysis gives their stated geometric forms.
For a normal-crossing support $S$, the divisor calculation applied
to $(X,F)=(Y,S)$ gives the triple-point count
(\cref{cdp:st:C.2.MH.2,cdp:st:C.2.G.1,night:P4.6}).''','series:II:C','Supply the exact global owner for the unrestricted irreducible classification and the exact single-support NC substitution, without applying P4.58 outside its stated global domain.')
guard('II-C4-G1-MAPS',r'''These are the normalization
and resolution maps of each full fibre, with its given
component and conductor multiplicities.''',r'''For $Y_b=f^*(b)=\sum_i m_iS_i$ and $S=(Y_b)_{\rm red}$,
these are the normalization $\nu:\coprod_iT_i\to S$ and the
conductor defined by
$\mathfrak c=\operatorname{Ann}_{\OO_S}
 (\nu_*\OO_{\coprod_iT_i}/\OO_S)$.
Their maps to $Y_b$ compose with the reduction inclusion
$j:S\hookrightarrow Y_b$.''','cdp:st:C.2.G.1','Replace the ambiguous full-fibre map wording by the actual reduced-support normalization, annihilator conductor and explicit reduction composite used by the proof.')
guard('II-C4-G1-MAP-PROOF',r'''\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item \textbf{The base and the finite character.}''',r'''\begin{proof}
For each full fibre $Y_b=f^*(b)=\sum_i m_iS_i$, its reduction
$S=(Y_b)_{\rm red}$ and normalization $\nu:\coprod_iT_i\to S$
give the structure-sheaf maps
\[
 \OO_{Y_b}\twoheadrightarrow j_*\OO_S
       \hookrightarrow(j\circ\nu)_*\OO_{\coprod_iT_i}.
\]
Their composite defines $j\circ\nu:\coprod_iT_i\to Y_b$.
The conductor ideal $\mathfrak c$ in the statement defines
$\Gamma=V(\mathfrak c)\subset S$ and its inverse image
$A=V(\mathfrak c\OO_{\coprod_iT_i})$.
The reduced curves used below are $C=\Gamma_{\rm red}$ and
$A_i=(A\cap T_i)_{\rm red}$.

\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item \textbf{The base and the finite character.}''','cdp:st:C.2.G.1','Prove the exact map between the full fibre, its reduction and its normalization via the quotient/inclusion of structure sheaves; identify scheme and reduced conductor loci used in INT3.')
def write(path,data,fields):
 with path.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(data)
write(OUT/'S6_SERIES_PUBLISH_main_C_guards.tsv',[{k:r[k] for k in ['change_id','old_text','new_text']} for r in rows],['change_id','old_text','new_text'])
defects=[]
for n,r in enumerate(rows,1):
 defects.append(dict(change_id=f'II-C4-C-D24-{n:02d}',type='D24',statement_id=r['owner'],old_location=r['owner'],old_page='checkpoint 44 source; final page concordance pending',new_location=r['owner'],new_page='receiving source; integrated PDF pending',old_text=r['old_text'],new_text=r['new_text'],reason=r['reason'],review_status='complete current-form main-C/body comparison; guarded correction ready for central admission'))
write(OUT/'S6_SERIES_PUBLISH_main_C_defects.tsv',defects,['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status'])
checks=[
('series:II:C','Exposed global current-form comparison of the complete main C, all six outline steps and the C-related abstract clauses against complete current G1 and all its final receiving P360/UN7/UN12/INT1–3 scope data. Complete supporting owners D1.9, MH2, P4.6/.26/.32/.36/.37/.58, D2.3/.5/.7 were read. Exact full-fibre reduction and normalization maps, full compact versus proper-tube substitutions, rational equality, stronger global minimal-Hopf maps, reducible equality in both directions, monodromy and construction clauses all match after the five bounded D24 guards. This is the global comparison for C only; no all-main-theorem, final-PDF, independent, literature-search or program-execution credit.'),
('cdp:st:C.2.G.1','Read the entire seven-step proof and statement in current form. Checked Leray D1.9 tube class, exact smooth root cover, conductor canonical divisor, finite-character rational/ruled values, global Hopf Chern and blowup isomorphisms, INT1–3 domains, conductor complement isomorphism, Euler sum, Poincare/skew-pairing bound and both equality directions. Added the explicit structure-sheaf quotient/inclusion proving the composite to the full fibre and conductor definitions; read these additions against the unchanged proof.'),
('cdp:st:D.1.9','Read complete statement and proof. Rational b1=b2=0 gives H1(Y,Z)=0 and finite H2(Y,Z), hence nonzero dZ transgression; the local meridian argument preserves nonzero support and nearby-fibre restrictions. Coherent base change and coefficient injection justify the simultaneous irrational-parameter lines. Thus C requires no unspoken integral H2 vanishing.'),
('cdp:st:C.2.MH.2','Read complete statement and proof. The same D1.9 class lifts through the disc Leray isomorphism to the identical full-fibre tube and normalization resolution; P289 gives e=2 in the rational case and 2-2g in the ruled case. This is the compact specialization used in G1 and C.'),
('night:P4.6','Read the complete single-divisor statement and proof. Applied (X,F)=(Y,S) under b2(Y)=0; checked normalization immersion normal bundle, zero ambient Chern classes, nodal conductor and degree-two branch cover, sign line in the coherent normalization complex, HRR and pointwise Euler alternating count. Gives e(S)=number of triple points and parity without restrictions on other fibre supports.'),
('night:P4.58','Read the complete statement and proof. Its global hypothesis is that every support is irreducible or normal crossing. Replaced its main-C local-source role by P4.6 and the unrestricted classification owner G1; no statement or proof of P4.58 changed.'),
('night:P4.26','Read the complete statement and proof. Its single irreducible and single NC conclusions apply in C; only its final global implication has the all-supports NC/irreducible requirement. Checked exact same-map conductor, boundary blowup, pushout and trace applications and its local/global separation.'),
('night:P4.32','Read complete statement and proof. The first irreducible zero-Euler classification has C scope and gives exact minimal-normalization and unramified-map descriptions through the same nu,pi. The last global NC conclusion is not imported into unrestricted C.'),
('night:P4.36','Read complete statement and proof. Checked primary Hopf finite cover and pulled-back blowups, two saturated derivative sheaf sequences, integer completion identity, equality forcing every exceptional curve to be contracted, descent, last-blowup minimality, negative-definite exceptional exclusion, nonvanishing foliation derivative and finite unramified elliptic conductor maps. These exact isomorphisms supply the stronger global minimal-Hopf claim used in C.'),
('night:P4.37','Read complete statement and proof. Checked reduced-boundary NC exclusion, intermediate Kato foliation blowdown substitutions, initial negative-definite completion, strict inequality after k blowups and zero-Betti Hopf conclusion. Same full compact normalization maps as G1; no general proper-tube minimal-Hopf conclusion inferred.'),
('cdp:st:D.2.3','Read complete statement and proof. Checked relative logarithmic restriction map dividing the normal residue by m_i, two period-growth alternatives, coefficient-ideal Koszul eigenvalues a/e, invertible connecting endomorphism and zero residue map, primitive generator division by t, and equivariant exterior-square map. All positive full multiplicities retained; source theorems remain at their already recorded literature provenance.'),
('cdp:st:D.2.5','Read complete statement and proof. Checked fixed positive-index obstruction, rational-Betti smooth-support root cover and Cartier layers, finite analytic-locus selection, Gauduchon all-powers degree, nonzero divisorial conductor giving pg=0, embedded vertical resolution and connectedness, exact q over punctured disc, and D2.3 monodromy contradiction. Combined with G1 gives C equality under identity H1 monodromy.'),
('cdp:st:D.2.7','Read complete statement and proof. Checked the three inverse holomorphic marking maps and integral matrices, clutching contribution to degree two, Mayer–Vietoris quotient maps and displayed unimodular relation matrices, van Kampen relations, fibre Euler calculation, integral duality and E1 function-field specialization. Identity integral monodromy implies the rational-monodromy instance required by C. Printed Smith data were read; no program execution credited.')]
checks.extend([('cdp:st:D.2.2','Read complete statement and proof in the final Euler section. The same Y,f satisfy G1 and, after its base identification, D2.5; the exact Euler sum gives every support zero. D2.7 supplies the integral-homology, identity-monodromy, normal-crossing instance and algebraic dimension. The unrestricted nonemptiness and equality statements match main C.'),('cdp:st:D.2.4','Read the complete common D2.2/D2.4 statement and proof. D2.4 is its preserved alias; the same-base G1/D2.5 application and D2.7 construction prove its full equality and nonemptiness conclusion. No second proof or independent event type is claimed.')])
fields=['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group','publish_input_file','publish_input_row','date_utc','where']
events=[]
for n,(owner,outcome) in enumerate(checks,1):
 event=f'publish:c4:global-C:{n:03d}'
 events.append(dict(statement_id=owner,date=STAMP[:10],who=WHO,type='used and rechecked in this run',outcome=outcome,event_id=event,phase='exposed final current-form global comparison of main C' if n==1 else 'complete current supporting proof comparison for main C',source_file='agents/continuation4_horizontal/S6_SERIES_PUBLISH_main_C_comparison.md',source_row='',source_event_type='used and rechecked in this run',evidence_group=event,publish_input_file='',publish_input_row='',date_utc=STAMP,where='Current main C/abstract/outline and G1 with the final horizontal receiver; five exact D24 guards'))
write(OUT/'S6_SERIES_PUBLISH_main_C_CHECK_EVENTS.tsv',events,fields)
print(f'{len(rows)} guards; {len(defects)} compact D24 rows; {len(events)} honest events; {STAMP}')
for r in rows:print(r['change_id'],len(r['old_text']),len(r['new_text']))

unit_rows=[]
for unit,title,detail in [('series:II:main-theorems','The main theorems','Main C complete and exact after these guards. Combine this exposed C comparison with the separately recorded parent A/B/D/E/F/G comparisons before closing this existing whole-unit row.'),('series:II:outline','The proofs in outline','All six C steps compared completely; step 1 corrected to the exact single-divisor P4.6 application. Combine with the parent A/B/D/E/F/G outline comparisons before closing this existing whole-unit row.'),('sec:II:all:12','Euler sign and equality for arbitrary torus fibres','The complete G1 and D2.2/D2.4 final section was read. The two normalization/conductor statements now have their exact reduction morphism and structure-sheaf proof; the whole section agrees with main C and its abstract clauses.')]:
 unit_rows.append(dict(paper='II',unit_id=unit,unit_title=title,row_kind='defect',defect_type='D24',prior_status='open',proposed_status='done after guarded admission and parent whole-unit comparison' if unit!='sec:II:all:12' else 'done after guarded admission',date_utc=STAMP,evidence='agents/continuation4_horizontal/S6_SERIES_PUBLISH_main_C_comparison.md; S6_SERIES_PUBLISH_main_C_guards.tsv; CHECK_EVENTS.tsv publish:c4:global-C:001',detail=detail))
write(OUT/'S6_SERIES_PUBLISH_main_C_unit_proposals.tsv',unit_rows,['paper','unit_id','unit_title','row_kind','defect_type','prior_status','proposed_status','date_utc','evidence','detail'])
