from pathlib import Path
import re,json,datetime
from S6_SERIES_PUBLISH_editing import Editor,block
r=Path(__file__).resolve().parents[1];ed=Editor('I')
def with_credit(label):
    b=block(ed.text,label,proof=False);a=ed.text.index(b)
    q=ed.text.index(r'\begin{proof}',a+len(b));e=ed.text.index(r'\end{proof}',q)+len(r'\end{proof}')
    return ed.text[a:e]
p1=with_credit('inv:D1.1');p2=with_credit('inv:D1.2')
a=ed.text.index(r'\subsection{Re-derivation of Theorem~\ref{fam:src:A.5.2}}')
b=ed.text.index(r'\section{Tangent cohomology and deformations}',a)
old_a52=ed.text[a:b]
assert len(old_a52.strip())>15000
core=old_a52[old_a52.index('Let $\\nu:E\\to W$'):old_a52.index(r'\item \emph{Vertical fields')].strip()
core=core.replace(r'\label{fam:eq:ab-cusp-resolution}',
 r'\label{fam:eq:ab-cusp-resolution}\hypertarget{tag-01OJ}{}\label{eq:P5normalization}')
core=core.replace('actual boundary maps','boundary maps')
old_p52=block(ed.text,'night:P5.2')
new_p52=old_p52.replace(r'\hypertarget{tag-01OJ}{}\label{eq:P5normalization}','')
ed.replace(old_p52,new_p52,'D12','Place the normalization-resolution identity at its unique foundational proof; the later duplicate proof is being consolidated separately.','night:P5.2:resolution-anchor')
foundation=block(ed.text,'push:src:E.3.1')
i=foundation.index('For the cusp fibre $W$');j=foundation.index('Thus the three dimensions are constant',i)
newfoundation=foundation[:i]+core+'\n'+foundation[j:]
newp1=p1
i=newp1.index('The root-curve Picard group and graded cohomology are');j=newp1.index(r'\begin{proof}',i)
newp1=newp1[:i]+newp1[j:]
newp1=newp1.replace(r'\begin{proof}',r'''\begin{proof}
The Picard group and graded cohomology are those of
\cite[Lemma~6.1]{DuEtAl2026v1}; the following chart maps specify
the coarse invariant direct image used here.''',1)
newp1=newp1.replace('cohomology comparison in the direction used here, not merely equality\nof Euler characteristics.','cohomology comparison with its canonical invariant map.')
i=newp1.index('The two calculations agree exactly for every integer $n$;');j=newp1.index(r'\end{enumerate}',i)
newp1=newp1[:i]+newp1[j:]
newp1=newp1.replace(r'\rho_*\OO_{\mathcal B}(n)=\OO_B(d(n)),',
 r'\hypertarget{tag-01P3}{}\label{fam:eq:ab-root-degree}'+'\n'+r'\rho_*\OO_{\mathcal B}(n)=\OO_B(d(n)),',1)
newp1=newp1.replace('Here and below additive notation for this presentation means tensor\nproduct.',r'''The weighted quotient presentation is
\[
 \mathcal B\simeq[(\mathbb C^2\setminus\{0\})/\mathbb C^*],
 \quad\lambda(x,y)=(\lambda^3x,\lambda^4y),\qquad
 t=\frac{y^3}{y^3-x^4}.
\]
The root sections are $(\mathcal O(4),y)$ and $(\mathcal O(3),x)$.
They give isomorphisms on each root chart, and the same coarse
coordinate on their ordinary overlap makes those isomorphisms glue.
Additive notation in the Picard presentation means tensor product.''')
newp2=p2
i=newp2.index('The root lift, vertical splitting');j=newp2.index(r'\begin{proof}',i)
newp2=newp2[:i]+newp2[j:]
newp2=newp2.replace(r'\begin{proof}',r'''\begin{proof}
These bundles and maps are the standard-data calculation of
\cite[Lemmas~6.2 and~6.7; Propositions~6.6 and~6.10]{DuEtAl2026v1}.''',1)
i=newp2.index(r'\item The divisors');j=newp2.index(r'\item On a smooth torus chart',i)
newp2=newp2[:i]+r'''\item The fibre-divisor root objects and their proper flat
atlas comparison are those of \cref{push:src:E.3.1} with $k=l=1$.
'''+newp2[j:]
i=newp2.index(r'\item For completeness the structure-sheaf computation');j=newp2.index(r'\item On all other geometric fibres',i)
newp2=newp2[:i]+newp2[j:]
i=newp2.index(r'\item On all other geometric fibres');j=newp2.index('The determinant of (D.3)',i)
newp2=newp2[:i]+r'''\item Proposition~\ref{push:src:E.3.1} gives local freeness,
geometric-fibre comparison and trace duality on the root atlas.
'''+newp2[j:]
newp2=newp2.replace('the actual bundle identity','the bundle identity')
newp2=newp2.replace(r'R^0\bar f_*\OO_X=\OO,\qquad R^2\bar f_*\OO_X=\OO(-1),',
 r'\hypertarget{tag-01OZ}{}\label{fam:eq:ab-direct-images}'+'\n'+r'R^0\bar f_*\OO_X=\OO,\qquad R^2\bar f_*\OO_X=\OO(-1).\tag{D.2a}',1)
newp2=newp2.replace(r'0\longrightarrow\bar f^*E\longrightarrow\mathcal T',
 r'\hypertarget{tag-01P0}{}\label{fam:eq:ab-log-tangent}'+'\n'+r'0\longrightarrow\bar f^*E\longrightarrow\mathcal T',1)
newp2=newp2.replace(r'\omega_{X/\mathcal B}=\bar f^*(\det E)^{-1}.',
 r'\hypertarget{tag-01P2}{}\label{fam:eq:ab-relative-dualizing}'+'\n'+r'\omega_{X/\mathcal B}=\bar f^*(\det E)^{-1}.\tag{D.3a}',1)
i=newp2.index('At the cusp $\\gamma$ vanishes on the angular sublattice');j=newp2.index('Thus\n$\\OO\\gamma\\subset G$',i)
newp2=newp2[:i]+r'''At the cusp $\gamma$ kills
$\Lambda_{\rm tor}=\mathbb Z\langle\widehat w,\widehat\delta\rangle$.
Local sections of the free toric quotient with transitions
$s_i=\Psi_{\lambda_{ij}}s_j$ give the holomorphic constant Cech
cocycle $\gamma(\lambda_{ij})$ on the whole neighbourhood.
For $B_0=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$,
the edges $e_1,e_2,e_2-e_1$ have deck vectors
$(0,1),(-1,0),(-1,-1)$, so its central values are $(0,-1,-1)$.
Their cup product with $(1,0,-1)$ is one by
\eqref{fam:eq:ab-cusp-resolution} and its displayed product.
On the punctured overlap the exponential map kills exactly
$\Lambda_{\rm tor}$, giving the same full-lattice cocycle.
The Leray edge map over the Stein cusp disc is an isomorphism,
since its positive coherent cohomology vanishes. This gives
a holomorphic nonvanishing extension of $[\gamma]$.
'''+newp2[j:]
ed.replace(old_a52,'','D12',
 'Consolidate the first tangent re-derivation with the full Koszul/direct-image, actual-gluing and Kuranishi proof already present. Its unique root map, normalization resolution, cup product, divisor maps and gamma extension are incorporated in the common foundations; every anchor is relocated.',
 'app:rederive:fam-src-A.5.2')
ed.replace(p1,'','D14','Move the full root Picard/coarse-cohomology calculation to the initial root-bundle conventions.','inv:D1.1')
ed.replace(p2,'','D14','Move the vertical/logarithmic bundle proof before cotangent and tangent uses. Repeated cusp/base-change details now cite the complete immediately preceding foundation.','inv:D1.2')
definition=block(ed.text,'I:def:root-bundles');defonly=block(ed.text,'I:def:root-bundles',proof=False)
ed.replace(definition,defonly+'\n'+newp1,'D12',
 'One proof supplies the Picard and canonical-root identities as well as all integer coarse degrees; remove the short repeated proof at the definition.',
 'I:def:root-bundles')
ed.replace(foundation,newfoundation+'\n\n'+newp2,'D12',
 'Place the exact normalization sheaf complex and Alexander–Whitney cup map once at the base-change foundation; follow it by the full vertical/logarithmic bundle proof.',
 'push:src:E.3.1')
needle=r'\begin{proof}[Koszul and direct-image proof of Theorem~\ref{fam:st:A.5.2}]'
ed.replace(needle,r'\subsection{The tangent direct images}\hypertarget{tag-000D}{}\label{app:rederive:fam-src-A.5.2}'+'\n'+needle,
 'D14','Keep the credited tangent-proof anchor at the unique remaining direct-image proof.','app:rederive:fam-src-A.5.2:anchor')
needle=r'0\longrightarrow\mathcal T\longrightarrow T_X'+'\n'+r' \longrightarrow\nu_*K_P\longrightarrow0.             \tag{D.10}'
ed.replace(needle,r'\hypertarget{tag-01P1}{}\label{fam:eq:ab-normal-quotient}'+'\n'+needle,
 'D12','The two branch-normal quotient sequences are the identical map under N_nu=K_P; keep the old formula anchor on its one proof.','fam:eq:ab-normal-quotient')
ed.save()
(r/'records/S6_SERIES_PUBLISH_I_common_root_comparison.json').write_text(json.dumps({
 'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'read_scope':'Complete 15,888-character A5.2 first appendix proof, full inv:D1.1 and seven-step inv:D1.2 proofs, full five-step Koszul direct-image proof and following KS/Kuranishi calculations read before consolidation.',
 'correspondence':{'root Picard':'D1.1 retains the complete invariant descent, weighted-quotient map, degrees and monomial comparison.',
 'cusp structure sheaf':'E3.1 retains the exact branch resolution and its multiplicative cochain map, with all original resolution anchors.',
 'vertical bundle':'D1.2 retains the exact exponential vector map, ordinary kernel divisibility, logarithmic surjection, discriminant line and trace duality.',
 'gamma':'D1.2 includes the period-row nonvanishing and the full local constant-Cech extension from A5.2.',
 'ordinary tangent':'The original Koszul proof retains its root torsion sheaf, cusp freeness and exact coarse direct images; the first alternative global-cohomology proof is archived.'},
 'scope':'Presentation and explicit correspondence; no new independent proof event is inferred.'},indent=2)+'\n')
