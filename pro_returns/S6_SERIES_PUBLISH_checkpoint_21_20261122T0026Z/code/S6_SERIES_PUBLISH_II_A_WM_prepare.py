from pathlib import Path
import hashlib
import json
from datetime import datetime, timezone

B = Path('/workspace/scratch/08a92fb2355d/S6_SERIES_PUBLISH')
R = Path('agents/ii_checks_A/recovery_20261121T195642Z')
G = R / 'group09_WM'
(B / G).mkdir(exist_ok=True)

def digest(s):
    return hashlib.sha256(s.encode()).hexdigest()

original = (B / 'agents/ii_infra/released_proofs/02WM/230b85aca88a0ae7/S6_SERIES_PUBLISH_full_owning_block.tex').read_text()
old_path = G / 'S6_SERIES_PUBLISH_II_02WM_full_original.tex'
new_path = G / 'S6_SERIES_PUBLISH_II_02WM_full_proposed.tex'
(B / old_path).write_text(original)
current = original
guards = []

def replace(old, new, defects, reason, transport):
    global current
    assert current.count(old) == 1, (reason, current.count(old))
    before = current
    pos = current.index(old)
    current = current[:pos] + new + current[pos+len(old):]
    guards.append({
        'tag': '02WM', 'guard_id': f'A_REC_02WM_{len(guards)+1:03d}',
        'defect_types': defects, 'literal_old': old, 'literal_new': new,
        'reason': reason, 'mathematical_transport': transport,
        'offset_before': pos, 'intermediate_before_sha256': digest(before),
        'intermediate_after_sha256': digest(current),
        'full_original_path': str(old_path), 'full_proposed_path': str(new_path)
    })

replace('[P4.15]', '[Finite rank drop of a normalization]', ['D04', 'D16'],
        'Give the statement its mathematical title.',
        'The owner, tag, numerical identity and three surface alternatives keep their identities.')
replace(r'\SeriesRef{night:P4.12}, \SeriesRef{night:P4.13}, \SeriesRef{night:P4.8}',
        r'\SeriesRef{cdp:st:A.5.3}, \SeriesRef{night:P4.12}, \SeriesRef{night:P4.13}', ['D06', 'D25'],
        'Bind the conductor identity and the two local support inputs; replace the global normal-crossing citation.',
        'A.5.3 is used with the identity resolution of the smooth normalization. The finite-cover and no-curves steps are supplied below by exact primary citations, so no use of the stronger all-supports hypothesis of P4.8 remains.')
replace(r'''Let $mS$ be an irreducible singular fibre in the setting of 4.2.
Suppose its normalization $T$ is smooth and $d\nu:T_T\to\nu^*T_X$
has rank two away from finitely many points. Let $\ell$ be the
length of its maximal-minor scheme. Then''', r'''Let $f:Y\to B$ be a proper surjective holomorphic map with
connected fibres from a connected smooth compact complex threefold
with $b_1(Y)=b_2(Y)=0$ to a smooth compact curve, and suppose that
its smooth general fibre is a complex two-torus. Let $mS$ be a full
fibre whose reduced support $S$ is irreducible and singular.
Suppose its normalization $\nu:T\to S$ has smooth domain $T$. Set
$j:T\xrightarrow{\nu}S\hookrightarrow Y$ and assume that
$dj:T_T\to j^*T_Y$ has rank two away from finitely many points.
Let $\ell$ be the length of its maximal-minor scheme. Then''',
        ['D05', 'D20', 'D25'],
        'State the ambient hypotheses and require a singular reduced support; declare the differential map.',
        'The old ambient X is the same standing threefold now denoted Y, and its written dnu is the derivative of j=iota composed with nu. The additional word singular is attached explicitly to S. The frozen actual examples 3S1 and 4S2 have smooth reduced support, rank-two identity normalization and elliptic-product covers of degrees 9 and 8; they refute the broader full-fibre reading. This is an explicit statement-scope repair, not an unchanged-statement claim.')
replace(r'''The reduced conductor and singular locus are disjoint unions of
smooth elliptic curves, and their normalization maps are finite
and unramified.''', r'''In those last two alternatives, the reduced conductor $R\subset T$
and $C=\operatorname{Sing}(S)_{\mathrm{red}}$ are disjoint unions of
smooth elliptic curves, and the restriction $\nu|_R:R\to C$ is
finite and unramified.''', ['D20', 'D25'],
        'Give the conductor conclusion its proved range and exact restriction map.',
        'The same nu restricts to R over C. The frozen rational witness nu:dP6 to W has the six rational boundary curves as R and unit differential minors; its Euler number 6 excludes the former universal elliptic-conductor assertion. The last-two-alternatives conclusion is proved by the unchanged local branch argument, now with named R and C.')

start = current.index(r'\item The differential')
end = current.index(r'\item We now compute')
old_item1 = current[start:end]
new_item1 = r'''\item The differential is injective as a sheaf map: its kernel vanishes
on a dense open set, and its locally free source is torsion-free.
Its rank-one cokernel $Q$ is locally free away from finitely many
points. The depth lemma applied to the length-one locally free
resolution gives depth at least one at those points. Hence $Q$
has no finite-length subsheaf, and all its possible torsion would
be supported there. Thus $Q$ is torsion-free, and $L=Q^{**}$ is a
line bundle. In local frames the signed maximal-minor row of $dj$
annihilates its two columns. Its determinant transition functions
give a map to $L=\det(j^*T_Y)\otimes\det(T_T)^{-1}$.
The induced map $Q\to L$ is generically injective, hence injective
because $Q$ is torsion-free. Its image is the ideal generated by
those minors, tensored with $L$. We obtain the exact sequence
\[
 0\longrightarrow T_T\xrightarrow{dj}j^*T_Y
   \longrightarrow\mathcal I_Z\otimes L\longrightarrow0,
 \qquad L=K_T\otimes j^*(\det T_Y),\qquad
 \operatorname{length}(Z)=\ell.
\]
Poincar\'e duality gives $b_4(Y)=b_2(Y)=0$, so
$c_1(T_Y)=c_2(T_Y)=0$ in rational cohomology. Writing $k=c_1(K_T)$,
the Chern-character identity for this sequence is
\[
 3=\left(2-k+\frac{k^2-2c_2(T_T)}2\right)
     +\left(1+k+\frac{k^2}2-[Z]\right).
\]
Its degree-four part gives $e(T)=K_T^2-\ell$, and Noether's formula
gives $2e(T)+\ell=12\chi(\mathcal O_T)$.

Let $D$ be the full conductor divisor on $T$, and put $R=D_{\mathrm{red}}$.
Propositions~\ref{cdp:st:A.5.3} and~\ref{night:P4.12}, with the
identity as the resolution of $T$, give
$\omega_T(D)\simeq\nu^*\omega_S$ and $\omega_S^{\otimes m}\simeq\mathcal O_S$.
In particular $K_T+D\equiv0$. Proposition~\ref{night:P4.12}
also gives $\kappa(T)=-\infty$ and nonnormality of the singular $S$.
Since the hypersurface $S$ satisfies $S_2$, its nonnormal locus
contains a curve; thus $D$ is nonempty.
Let $q:T\to T_0$ contract $r$ point blowups to a minimal model.
Pluricanonical sections descend across each blowup by Hartogs'
extension on the complement of its centre, so $\kappa(T_0)=-\infty$
and $p_g(T_0)=0$.

For a K\"ahler $T_0$, the equality $p_g=0$ makes every real
degree-two cohomology class of type $(1,1)$. A sufficiently close
rational perturbation of a K\"ahler class, followed by integral
scaling, gives an integral K\"ahler class. Kodaira's embedding
theorem \cite[Main Theorem, p.~314]{Kodaira1954} therefore gives an
embedding $\Phi:T_0\hookrightarrow\mathbb P^N$. Apply
\cite[VI.17--VI.18, pp.~111--112; V.10, pp.~79--80; III.10, p.~40]{Beauville1978}
to $\Phi(T_0)$ and pull its ruling back by $\Phi$: the model is
rational or a projective-line bundle over a positive-genus curve.

For a non-K\"ahler $T_0$, \cite[Theorem~5.1, pp.~27--29]{OVV2020}
gives an isotrivial elliptic surface or a class-VII surface, with
overlap permitted. In the elliptic alternative, the local maps in
\cite[Theorem~4.2 and Remark~4.4, pp.~17--21]{OVV2020} are
\[
 (E\times\Delta_s)/\langle(z,s)\mapsto(z+e,\zeta_m s)\rangle
 \longrightarrow\Delta_t,\qquad t=s^m,
\]
where $e$ has exact order $m$. The elliptic action of
\cite[Proposition~4.5, pp.~21--22]{OVV2020} gives a nowhere-zero
vertical vector field. For its ruling $p:T_0\to B_0$, the quotient
of $T_{T_0}$ by this vector field maps to $p^*T_{B_0}$ with divisor
$R_p=\sum(m_i-1)E_i$, as follows from $dt=m_i s^{m_i-1}ds$.
Consequently $K_{T_0}=p^*K_{B_0}+R_p$, so $K_{T_0}^2=0$;
the vector field gives $c_2(T_0)=0$. Noether's formula and $p_g=0$
give $h^1(\mathcal O_{T_0})=1$.
The identity $b_1=2h^1(\mathcal O)-1$ in
\cite[Theorem~2.5, pp.~7--9]{OVV2020} gives $b_1(T_0)=1$.
Thus this elliptic alternative also has the class-VII invariants
$b_1=1$ and $\kappa=-\infty$.

For a projective-line bundle over a genus-$g$ curve, followed by
$r$ point blowups, the bundle and blowup formulas
\cite[II.3, pp.~17--18; III.18, pp.~46--47]{Beauville1978} give
\[
 e(T)=4(1-g)+r,\qquad K_T^2=8(1-g)-r.
\]
The Chern identity becomes $2r+\ell=4(1-g)$. For $g\ge1$ it forces
$g=1$ and $r=\ell=0$.
For a class-VII minimal model, write $b_2(T_0)=k_0\ge0$.
The equalities $b_1=1$, $p_g=0$ and
$b_1=2h^1(\mathcal O)-1$ give $\chi(\mathcal O_{T_0})=0$.
Thus $e(T)=k_0+r$ and $K_T^2=-k_0-r$, and the Chern identity gives
$2(k_0+r)+\ell=0$. Hence $T$ is minimal with $b_2=0$ and $\ell=0$.
By \cite[Theorem~1, p.~1]{BBK2019} it has a finite \emph{\'etale}
cover $a:T'\to T$ with $T'$ Hopf or Inoue. The inverse image
$a^{-1}(R)$ is a nonempty curve. Inoue surfaces contain no curves
by \cite[Proposition~2(i), pp.~274--275; Proposition~3(i), p.~277;
paragraph following (21), p.~279]{Inoue1974}, so $T'$ is Hopf.
The composite of its universal cover
$\mathbb C^2\setminus\{0\}\to T'$ with $a$ is the universal cover
of $T$, since $\mathbb C^2\setminus\{0\}$ is simply connected.
Therefore $T$ is Hopf.

For rational $T$, $\chi(\mathcal O_T)=1$ and $e(T)\ge3$ by the
same rational minimal-model and blowup formulas. Hence
$e(T)=6-\ell/2$ and $0\le\ell\le6$.
When $\ell=0$, the maximal-minor ideal is the unit ideal, so $dj$
has rank two everywhere.

'''
replace(old_item1, new_item1, ['D04', 'D06', 'D17', 'D18', 'D20', 'D22', 'D25'],
        'Complete the differential, classification and finite-cover arguments with their exact maps and opened primary locators.',
        'The signed-minor row identifies the same finite scheme Z and its colength. Additivity of ch gives the same e=K^2-ell. The identity resolution supplies D. The map Phi carries the Kahler model to the projective surface to which Beauville applies; the explicit elliptic local quotient and tangent quotient place the OVV elliptic overlap in class VII. The finite etale cover a pulls back R to a curve, and composition with the Hopf universal cover proves the assertion about T. Both original scope failures are excluded precisely by the revised statement, not by an unstated replacement of the fibration.')

replace(r'''\item We now compute the image Euler number in the two latter cases.
The conductor divisor $D$ satisfies $K_T+D\equiv0$. First let
$T$ be a minimal ruled surface over an elliptic curve $E$;
it is a $\mathbb P^1$-bundle. For a ruling fibre $F$, $D\cdot F=2$.''',
        r'''\item Consider the two latter alternatives. First let $T$ be a
minimal ruled surface over an elliptic curve $E$. Its ruling
$p:T\to E$ is a $\mathbb P^1$-bundle by
\cite[III.10, p.~40]{Beauville1978}. For a ruling fibre $F$,
the equality $K_T+D\equiv0$ gives $D\cdot F=2$.''',
        ['D01', 'D08', 'D17', 'D18', 'D22'],
        'State the last-two-alternatives argument directly and identify the ruling morphism.',
        'The same minimal ruled T and conductor D are used, with p the projective-bundle map and F its fibre. The divisor intersection remains D.F=2.')
replace('The possibilities\nare one elliptic double-section or two disjoint elliptic sections.',
        'The possibilities\nare one elliptic bisection, of degree two over $E$, or two\ndisjoint elliptic sections.',
        ['D20', 'D22'], 'Specify the degree-two horizontal map without ambiguity of multiplicity.',
        'The coefficient-one component H has H.F=2 in the first case, so p|H has degree two. The multiplicity-two section belongs to the separate following case and is preserved there.')
replace(r'''The reduced conductor has Euler number equal to the number $k$
of these fibres: $e(H)=0$, $e(F_j)=2$, and each meets $H$ once.
The immersive normalization identifies $T\setminus D_{\mathrm{red}}$
with $S_{\mathrm{reg}}$. Hence
\[
 e(S_{\mathrm{reg}})=e(T)-e(D_{\mathrm{red}})=-k.
\]
P4.13 forces $k=0$.''',
        r'''The normalization of $H$ maps isomorphically to $E$ by its
degree-one ruling map. Its map into $T$ is a section of $p$,
so its image $H$ is smooth elliptic.
The reduced conductor $R$ has Euler number equal to the number $v$
of these fibres: $e(H)=0$, $e(F_j)=2$, and each meets $H$ once.
The normalization restricts to an isomorphism
$T\setminus R\simeq S_{\mathrm{reg}}$. Hence
\[
 e(S_{\mathrm{reg}})=e(T)-e(R)=-v.
\]
Proposition~\ref{night:P4.13} forces $v=0$.''',
        ['D04', 'D20', 'D22'],
        'Specify the section, normalization-complement map and open-stratum sign input.',
        'The degree-one finite map from the normalization of H to E is an isomorphism; its map into the bundle is a section with image H. Each rational fibre contributes e(P1)-e(point)=1 to R, and the same nu is an isomorphism off the conductor. The old count k is renamed v to distinguish it from Chern-class notation.')
replace(r'''\item To check the image, at a singular point the finite immersive
normalization presents the germ as distinct smooth surface
branches $S_i$.''',
        r'''\item At a point of $C=\operatorname{Sing}(S)_{\mathrm{red}}$,
the finite immersive normalization presents the germ as distinct
smooth surface branches $S_i$.''', ['D08', 'D20'],
        'Name the reduced image locus and start with its local branches.',
        'Each point of the finite fibre of nu maps immersively to one embedded surface germ in Y; these are precisely the normalization sheets of the same S.')
replace(r'''Globally this map is finite and unramified. Riemann--Hurwitz
then makes every image component elliptic. Finally
\[
 e(S)=e(T)-e(D_{\mathrm{red}})+e(\operatorname{Sing}S)=0.
\]''',
        r'''Globally the restriction $\nu|_R:R\to C$ is finite and unramified.
For a component of degree $d$, Riemann--Hurwitz gives
$0=d(2g(C_i)-2)$, so every image component is elliptic.
Euler additivity for the normalization and its conductor gives
\[
 e(S)=e(T)-e(R)+e(C)=0.
\]''', ['D20', 'D22'],
        'Write the exact conductor covering and the image-genus equation.',
        'The same finite restriction nu|R has nonzero derivative because j is immersive. The compact elliptic source component has Euler number zero, and the normalization is an isomorphism away from R and C, giving the displayed Euler identity.')

(B / new_path).write_text(current)

source_path = B / 'S6_SERIES_PUBLISH_II.tex'
source_bytes = source_path.read_bytes()
source = source_bytes.decode()
begin = source.index(r'\begin{thebibliography}{99}')
end = source.index(r'\end{thebibliography}', begin)
bib = source[begin:end]

def entry(key):
    import re
    starts = list(re.finditer(r'\\bibitem(?:\[[^\n]*\])?\{[^}]+\}', bib))
    for i, m in enumerate(starts):
        if m.group().endswith('{'+key+'}'):
            return bib[m.start():starts[i+1].start() if i+1<len(starts) else len(bib)]
    raise ValueError(key)

bib_pairs = []
def bib_pair(key, new, explanation):
    old = entry(key)
    op = G / f'S6_SERIES_PUBLISH_II_{key}_bibliography_original.tex'
    np = G / f'S6_SERIES_PUBLISH_II_{key}_bibliography_proposed.tex'
    (B/op).write_text(old); (B/np).write_text(new)
    bib_pairs.append({'key': key, 'literal_old': old, 'literal_new': new,
      'defect_types': ['D08', 'D18'], 'reason': explanation,
      'mathematical_transport': 'The bibliographic key is retained. The cited theorem and page locators are bound to the explicitly opened edition in the WM primary-scope record.',
      'full_original_path': str(op), 'full_proposed_path': str(np),
      'original_sha256': digest(old), 'proposed_sha256': digest(new),
      'source_path': 'S6_SERIES_PUBLISH_II.tex',
      'source_sha256': hashlib.sha256(source_bytes).hexdigest(),
      'source_character_offset': begin+bib.index(old)})

bib_pair('BBK2019', r'''\bibitem[Buonerba et~al.(2019)Buonerba, Bogomolov, and Kurnosov]{BBK2019}
Federico Buonerba, Fedor Bogomolov, and Nikon Kurnosov.
\newblock Classifying {VII}$_0$ surfaces with $b_2=0$ via group theory.
\newblock arXiv:1709.00062v3, 20 May 2019.
\newblock URL \url{https://arxiv.org/pdf/1709.00062v3}.


''', 'Bind the finite-etale-cover theorem to the opened v3 edition and remove the process-status word.')
bib_pair('OVV2020', r'''\bibitem[Ornea et~al.(2020)Ornea, Verbitsky, and Vuletescu]{OVV2020}
Liviu Ornea, Misha Verbitsky, and Victor Vuletescu.
\newblock Classification of non-{K}{\"a}hler surfaces and locally conformally
  {K}{\"a}hler geometry.
\newblock arXiv:1810.05768v3, 26 June 2020.
\newblock URL \url{https://arxiv.org/pdf/1810.05768v3}.


''', 'Bind the analytic classification, elliptic local models and Hodge formula to the exact v3 edition whose source matches the attached text; remove the process-status word.')

assert '{Kodaira1954}' not in bib
anchor = entry('Kodaira1963II')
addition = r'''\bibitem[Kodaira(1954)]{Kodaira1954}
Kunihiko Kodaira.
\newblock On K\"ahler varieties of restricted type.
\newblock \emph{Proceedings of the National Academy of Sciences of the
United States of America}, 40\penalty0 (5):\penalty0 313--316, 1954.
\newblock \doi{10.1073/pnas.40.5.313}.


'''
op = G / 'S6_SERIES_PUBLISH_II_Kodaira1954_insertion_original.tex'
np = G / 'S6_SERIES_PUBLISH_II_Kodaira1954_insertion_proposed.tex'
(B/op).write_text(anchor); (B/np).write_text(addition+anchor)
bib_pairs.append({'key': 'Kodaira1954', 'literal_old': anchor,
  'literal_new': addition+anchor, 'defect_types': ['D18'],
  'reason': 'Add the opened original PNAS embedding theorem at its exact title, journal pages and DOI, preceding the existing Kodaira entry.',
  'mathematical_transport': 'Main Theorem on original p.314, read in the publisher collected-works reprint, is applied to the constructed integral Kahler class on T0. The resulting sections define the actual embedding Phi used in the proof.',
  'full_original_path': str(op), 'full_proposed_path': str(np),
  'original_sha256': digest(anchor), 'proposed_sha256': digest(addition+anchor),
  'source_path': 'S6_SERIES_PUBLISH_II.tex',
  'source_sha256': hashlib.sha256(source_bytes).hexdigest(),
  'source_character_offset': begin+bib.index(anchor)})

manifest = {
  'created_utc': datetime.now(timezone.utc).isoformat(), 'checker': 'ii_check_a',
  'canonical_writes': False, 'guards': guards,
  'blocks': [{'tag': '02WM', 'original_path': str(old_path),
              'proposed_path': str(new_path), 'original_sha256': digest(original),
              'proposed_sha256': digest(current),
              'statement_unchanged': False,
              'scope_repairs': ['The full fibre has singular reduced support S.',
                                'The elliptic conductor assertion is confined to the last two alternatives.']}],
  'bibliography_guards': bib_pairs,
  'note': 'Proposal only. Whole-pair comparative rereading and final event proposals are recorded separately. Existing enumeration wrappers are reserved for the root global numbering map.'
}
(B/G/'S6_SERIES_PUBLISH_II_A_WM_editorial_proposals.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'guards':len(guards),'bibliography_guards':len(bib_pairs),
                  'original_sha256':digest(original),'proposed_sha256':digest(current),
                  'manifest':str(G/'S6_SERIES_PUBLISH_II_A_WM_editorial_proposals.json')}))
