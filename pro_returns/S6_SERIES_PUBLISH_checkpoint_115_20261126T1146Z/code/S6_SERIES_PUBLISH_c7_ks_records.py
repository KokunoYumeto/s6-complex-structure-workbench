"""Write proposed 02KS defects and one accurately scoped check event.

These are local proposals, not global table edits or an admission.
All quoted old/new text is checked against the two released originals
and the receiving proof.  No canonical manuscript is read.
"""
from pathlib import Path
import csv
from datetime import datetime,timezone

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation7_iii_ks'
reps=list(csv.DictReader((OUT/'S6_SERIES_PUBLISH_III_02KS_replacements.tsv').open(),delimiter='\t'))
old='\n\n'.join(r['old_text'] for r in reps)
new=(OUT/'S6_SERIES_PUBLISH_III_02KS_receiving.tex').read_text()
cols=['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status']
rows=[]
def cut(s,a,b,include_end=False):
    i=s.index(a);j=s.index(b,i)
    return s[i:j+len(b) if include_end else j]
def add(suffix,kind,label,where,before,after,reason):
    assert before in old,(suffix,'old')
    assert not after or after in new,(suffix,'new')
    rows.append(dict(zip(cols,[
      'c7-III-02KS-'+suffix,kind,label,where,'',
      'agents/continuation7_iii_ks/S6_SERIES_PUBLISH_III_02KS_receiving.tex','',
      before,after,reason,
      'complete local original/receiving comparison; root admission, canonical application and final page review pending'])))

add('smooth-classification','D27','maps:eq:D.V3','S6_SERIES_PUBLISH_III.tex; maps:eq:D.V3',
    r''' X\cong \#^3(S^2\times S^4)\#(S^3\times S^3)
                          \#\widetilde\Sigma_0N_m''',
    r''' X\cong\operatorname{Fl}(\mathbb C^3)\#(S^2\times S^4)
       \#(S^3\times S^3)\#\widetilde\Sigma_0N_m.''',
    'The embedded dP6 component has normal line K_D and integral divisor cube 6. On the old target the suspension has H1=0,H2=(Z/m)^2,H^2=0, and all degree-two cubes vanish. The free allowed log m=1,v=gamma is simply connected. The complete refinement with the retained statement id maps:src:D.2.18 and display maps:eq:D.V3 follows from the exact quotient kernel, linked localization, geometric torsion separation, primitive cubic -3ab(a+b), spin and p1 on the torsion-free flag block, and framed reconstruction. Both signs n=±1 and every m>0 are proved.')

add('period-fan-transport','D25','maps:eq:D.V4','S6_SERIES_PUBLISH_III.tex:11231--11241',
    r''' \Gamma=\langle(3,0),(2,1)\rangle,
 \qquad
 \begin{pmatrix}1&1\\0&-1\end{pmatrix}
 \begin{pmatrix}3&2\\0&1\end{pmatrix}
       =\begin{pmatrix}3&3\\0&-1\end{pmatrix}.''',
    r''' \Gamma=\langle(3,0),(4,1)\rangle
        =\ker\bigl(\rho:\mathbb Z^2\to\mathbb Z/3\bigr),
 \qquad \rho(x,y)=x-y\pmod3.''',
    'The defining angular periods are (3,0),(4,1). Coordinate inversion (X1,X2,q)->(X1^-1,X2,q), with inverse itself and reciprocal first unit, maps this lattice to the printed one but also reflects the fan. Keeping the original triangular fan omits that morphism. The neighbor-lattice counts 0 and 2 obstruct an unchanged-fan symmetry; the original displayed multiplication is arithmetically true on its substituted lattice. D.V4/026C now carries the literal lattice, residue and inverse coordinates.')

add('fixed-curve-classes','D25','maps:src:D.2.18','S6_SERIES_PUBLISH_III.tex:11328--11348',
    '''Their classes in the free cusp defect are zero, as the
following integral computation shows.''',
    r''' V=\begin{pmatrix}-1&-1&2\\2&-1&-1\\-1&2&-1\end{pmatrix}.''',
    'Actual colours x-y give endpoints c,c-1 and two third vertices of colour c+1. The three nonzero columns are (-1,2,-1),(-1,-1,2),(2,-1,-1). Their classes are F0,F1,-F0-F1, spanning a primitive rank-two summand of H2(X) when n=±1. The original zero columns compute the substituted unchanged-fan model. The receiver separately proves that the orbit-map images, rather than the upstairs classes, vanish.')

add('null-link-surgery','D25','maps:src:D.2.18','S6_SERIES_PUBLISH_III.tex:11351--11357',
    '''The three-component embedded link is isotopic to three
unknotted spheres: apply the dimension-six embedding
isotopy theorem of \\ref{maps:src:D.2.14} to the disjoint union.
The same orientation-preserving equivariant surgeries
produce
$Y=X\\#^3(S^3\\times S^3)$ with a projectably spin free
circle action.''',
    '',
    'Removed the false nullhomotopy input and its connected-sum conclusion. The actual surgery trace attaches three three-handles with primitive image ZF0+ZF1 and kernel Z(1,1,1); its reverse trace has four-handles. Thus pi1(Y)=0, H2(Y)=Z+(Z/m)^2 and H3(Y)=Z^4+(Z/m)^2. H2 obstructs the asserted connected sum. The local normal and projectable-spin constructions stand. No separate failure of an external disconnected-source isotopy theorem is alleged. The complete receiver instead localizes the quotient link while preserving its linking and reconstructs X directly.')

add('surgery-orbit-rank','D25','maps:src:D.2.18','S6_SERIES_PUBLISH_III.tex:11357--11370',
    cut(old,'Its simply connected spin orbit has\n$H_2(B_5)',r'proves \eqref{maps:eq:D.V3}.',True),
    '',
    'The genuine free surgery manifold has H2(Y)=Z+(Z/m)^2. The bundle sequence gives H2(B5)=Z^2+(Z/m)^2 with primitive Euler class; local spin lifts prove B5 spin. Barden realizes the pair as (#^2(S2×S3)#N_m,(x,0,0)). The original rank-four pair and the subsequent bundle/cancellation application therefore use an incorrect input. The post-exposure note proves these corrected auxiliary statements. The receiver uses the independently derived flag-block reconstruction; it does not infer a failure of the cited external recognition theorems.')

add('original-cap-maps','D22','maps:src:D.2.18','S6_SERIES_PUBLISH_III.tex:11248--11252',
    '''The original $I_1^*$ filling has the order-four translation
model of \\ref{maps:src:D.2.16}, with two component orbits and free
specialization defect one. The original $II$ filling has
the product model of \\ref{maps:src:D.2.17} and no defect.''',
    r''' U_*\longleftrightarrow
 S^1_\delta\times T(t_{-q_{\rm tor}}:N_*\to N_*) .''',
    'Supply the complete model on the KS germ itself, with its torsion section and identity-component logarithm, narrow-line frame, actual contraction multiplier, variable-roof map, reciprocal angular gauges, collars and boundary marking. The original II product, star orbit ranks and specialization defects stand. Equal monodromy matrices alone are not used to identify distinct surface germs.')

add('cusp-relative-map','D22','maps:eq:D.V5','S6_SERIES_PUBLISH_III.tex:11265--11281',
    '''Indeed this quotient is the kernel of a surjection from
$\\mathbb Z^3$ to $\\mathbb Z\\oplus\\mathbb Z/3$, hence is
free of rank two.''',
    r''' (h_0,h_1,h_2)\longmapsto
       (h_0+h_1+h_2,\ h_1+2h_2\pmod3).''',
    'The conclusion stands. Give the exact normal boundary homomorphism, kernel basis (-1,2,-1),(-1,-1,2), inverse coordinates, normal sweeps, and integral fixed-curve splitting. D.V5/026D retains the quotient with its explicit isomorphism and inverse.')

add('canonical-descent','D22','maps:src:D.2.18','S6_SERIES_PUBLISH_III.tex:11322--11327',
    '''Both canonical lines
are locally trivial, by the Mumford volume form and
the translation-invariant form used in \\ref{maps:src:D.2.16}.
Hence $c_1(X)=0$ and $X$ is spin.''',
    cut(new,r'The manifold \(X\) is spin.',r'Hence \(c_1(X)=0\) and \(w_2(X)=0\).',True),
    'The assertion stands. The receiver evaluates c1 on the primitive fixed curves and constructs the invariant canonical form on the KS star, including frame independence and contraction descent. The post-exposure note additionally proves the original cusp volume-form claim directly. Integral H2 torsion is separated from the Hom description of H^2.')

header=next(line for line in old.splitlines() if line.startswith('\\StatementRecord'))
add('machine-header','D10','maps:src:D.2.18','S6_SERIES_PUBLISH_III.tex; theorem header',header,
    r'\textnormal{\small tag02KS.}',
    'Remove the production-status/dependency header, retain every permanent identity and print the small theorem tag. Dependencies are cited at their mathematical use.')
add('generated-enumeration','D10','maps:src:D.2.18','S6_SERIES_PUBLISH_III.tex:11223',
    r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]','',
    'Replace generated step apparatus by connected mathematical proof paragraphs. All eight original items have been compared in full.')
add('mathematical-title','D23','maps:src:D.2.18','S6_SERIES_PUBLISH_III.tex; theorem title',
    r'\begin{theorem}[the remaining profile with a three-component cusp]',
    r'\begin{theorem}[Three-component cusp with original additive fillings]',
    'Use an intrinsic mathematical title in place of a title depending on the order of preceding profiles. The profile and construction hypotheses are unchanged.')
add('group-notation','D20','maps:src:D.2.18','S6_SERIES_PUBLISH_III.tex; theorem group definitions',
    '''Define $t$ and $G$ as in \\ref{maps:src:D.2.16} with
$p=12$.''',
    r''' t=\gcd(m,n,a,b')\gcd(m,n,12,c),\qquad
 \mathcal G=\mathbb Z/t\oplus\mathbb Z/m\oplus\mathbb Z/(m|n|/t)
 \quad(n\ne0).''',
    'Distinguish the torsion group from the Mordell-Weil generator G, and display its parameter definition. The identification is identity on the three cyclic coordinates; use calligraphic T for the same two zero-normal factors.')
add('torsion-defensive-clause','D02','maps:src:D.2.18','S6_SERIES_PUBLISH_III.tex:11289--11290',
    'They must not be discarded beforehand.','',
    'State the unit torsion map and its inverse positively; the calculation already includes it.')
add('certificate-reference','D09','maps:src:D.2.18','S6_SERIES_PUBLISH_III.tex:11287--11289',
    '''the exact integral
vector and its image are retained in the certificate.''',
    r'''torsion generator \(\lambda\) maps to \(-16\delta=2\delta\),
an isomorphism of the order-three groups.''',
    'Replace an external certificate reference by the exact vector, induced torsion map and inverse in the mathematical proof.')
add('historical-program','D09','maps:src:D.2.18','S6_SERIES_PUBLISH_III.tex:11371--11377',
    cut(old,r'\item The program \texttt{manifolds\_star\_i3\_cusp.py}',r'\end{enumerate}').rstrip(),
    '',
    'Remove the historical filename and 731/97 execution counts from the proof. Historical code and outputs remain unopened and these counts are neither verified nor credited. The new unrestricted mathematical calculation and the separately recorded independent code/output establish the claimed groups and the corrected cubic.')

with (OUT/'S6_SERIES_PUBLISH_III_02KS_defects.tsv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=cols,delimiter='\t',lineterminator='\n')
    writer.writeheader();writer.writerows(rows)

event_cols=['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group','publish_input_file','publish_input_row','date_utc','where']
now=datetime.now(timezone.utc).isoformat()
paths=[
'agents/continuation7_iii_ks/S6_SERIES_PUBLISH_III_02KS_c7_fresh_derivation.md',
'agents/continuation7_iii_ks/S6_SERIES_PUBLISH_III_02KS_c7_primary_reading.md',
'agents/continuation7_iii_ks/S6_SERIES_PUBLISH_III_02KS_c7_maps.json',
'agents/continuation7_iii_ks/S6_SERIES_PUBLISH_III_02KS_released_statement.tex',
'agents/continuation7_iii_ks/S6_SERIES_PUBLISH_III_02KS_released_proof.tex',
'agents/continuation7_iii_ks/S6_SERIES_PUBLISH_III_02KS_post_exposure_derivation.md',
'agents/continuation7_iii_ks/S6_SERIES_PUBLISH_III_02KS_comparison.md',
'agents/continuation7_iii_ks/S6_SERIES_PUBLISH_III_02KS_receiving.tex',
'agents/continuation7_iii_ks/S6_SERIES_PUBLISH_III_02KS_replacements.tsv',
'agents/continuation7_iii_ks/S6_SERIES_PUBLISH_III_02KS_defects.tsv',
*['code/S6_SERIES_PUBLISH_c7_ks_'+stem+suffix for stem in ['integral','prepare','comparison','records'] for suffix in ['.py','.out']]]
event=dict(zip(event_cols,[
 'maps:src:D.2.18','2026-11-24','GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; seventh publication continuation',
 "refuted, with the refined statement's id",
 'D.V3 refuted and fully refined under the retained statement id maps:src:D.2.18, display maps:eq:D.V3/tag026B: for n=±1, X is orientation-preservingly diffeomorphic to Fl(C^3)#(S^2×S^4)#(S^3×S^3)#twisted_Sigma_0(N_m). The actual embedded dP6 divisor has integral cube 6; the old target has zero cube on every H^2 class, including the exact framed suspension with H1=0,H2=(Z/m)^2,H^2=0. Full D.V1/V2 homology stands for every free log, including n=0 and both signs. The complete fresh derivation, raw-period program and successful output were frozen and root-reviewed before individual release at 20:29:31.562852 UTC; the frozen fresh hash remains e44b377b7cc2ec20e4356dbea3196c71ee89581f8ef58d3ede56de5972059f0f. Every released theorem clause and all eight original proof items were then read and compared. D.V4 omitted the fan transport under the exact angular inversion; actual fixed-curve columns are (-1,2,-1),(-1,-1,2),(2,-1,-1), generating a primitive rank-two summand upstairs. The genuine surgery has H2=Z+(Z/m)^2,H3=Z^4+(Z/m)^2 and quotient H2=Z^2+(Z/m)^2, refuting the original surgery-rank chain. Original canonical/spin and homology assertions stand. The corrected proof constructs the actual KS original-star maps, orbit kernel, linking-preserving localization and geometric torsion separation, then the full primitive cubic -3ab(a+b), spin and p1 of the torsion-free flag block, primary Zhubr recognition and exact framed reconstruction. Literal G4, all conductor Smith diagonals/transformations/inverses, star boundary/orbit maps, symbolic log minors and 405 numerical cases pass; the new post-exposure program checks all twelve fan symmetries, both wall calculations, surgery trace, volume form and exact receiver guards. All output and the full receiving proof were read. The small receiving notation/wording corrections are checked; all six label/target pairs and five equation tags are preserved. Historical KS code and 731/97 counts remain unopened and uncredited. Primary scopes are recorded, with actual rendered inspection distinguished from textual placeholders. One proposed event only; it does not duplicate the narrower root counterexample event. No canonical edit, isolated or canonical build, page reading, unit closure or paper-gate credit is claimed; root admission is pending.',
 'publish:c7:III:02KS:refuted-refined',
 'complete blind derivation, individual authorized original exposure, full original and receiving comparison',
 'S6_SERIES_PUBLISH_III.tex','11222',"refuted, with the refined statement's id",
 'publish:c7:III:02KS:refuted-refined',
 'agents/continuation7_iii_ks/S6_SERIES_PUBLISH_III_02KS_CHECK_EVENTS.tsv','2',now,'; '.join(paths)]))
event['outcome']=event['outcome'].replace(
 'Original canonical/spin and homology assertions stand.',
 'Original canonical/spin and homology assertions stand. A focused post-exposure correction fixes the frozen fresh explanatory G-residue sentence: the actual forward -G period mu*q^4 has I3 component 1, while G is represented by alpha^2/mu*q^2 and has component 2, as the original correctly states. The receiver uses (0,2,3). The post-exposure note proves the O(G-O) local degree vector (-1,0,1), zero multidegrees of O(12G-O), exact original unit/inverse maps, and unchanged six-iterate framing, period/fan, fixed classes, cap and regular finite-log maps. Only narrowness of 12G and zero residue of 6G used the erroneous label; both corrected products remain zero. The frozen fresh file is unchanged and this correction receives no fresh credit.')
with (OUT/'S6_SERIES_PUBLISH_III_02KS_CHECK_EVENTS.tsv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=event_cols,delimiter='\t',lineterminator='\n')
    writer.writeheader();writer.writerow(event)
print('Local defect proposals',len(rows))
print('D27',sum(r['type']=='D27' for r in rows),'D25',sum(r['type']=='D25' for r in rows))
print('Proposed check events',1,'type',event['type'])
print('Original and receiving quotations verified against the exact local texts.')
print('No canonical manuscript or global table opened or changed.')
print('PASS: proposed 02KS defects and full refuted/refined check event written.')
