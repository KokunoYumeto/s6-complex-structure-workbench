"""Complete the exposed conductor-owner comparisons and exact applications."""
from S6_SERIES_PUBLISH_c3_edit import *

old=r'The finite-duality ideal of \cref{lem:II:conductor-duality} and its quotient are pure in the required dimensions, so $D$ has no isolated component.'
new=r'The finite-duality identity of \cref{lem:II:conductor-duality} makes the conductor ideal on the normal surface a maximal Cohen--Macaulay module. The exact sequence from that ideal to $\mathcal O_N$ makes its nonzero quotient Cohen--Macaulay of dimension one by the depth lemma. Thus its reduced support $D$ has no isolated component.'
apply_edit(old,new,'II-C3-CONDUCTOR-CYCLE-DEPTH',['D08','D25'],'night:P4.35','First proof item',
 'State the exact depth-two ideal and depth-one quotient on the same normal surface, replacing an unspecified purity phrase.')

path=ROOT/'agents/continuation3_provenance/refined_consumers/S6_SERIES_PUBLISH_refined_owner_transfer_guards.tsv'
_,guards=read_tsv(path)
for row in guards:
    apply_edit(row['old_text'],row['new_text'],row['change_id'],row['type'].split(';'),row['statement_id'],
        row['old_location'],row['reason'],row['review_status']+' Root read all four exact old/new guards and the full current P254/P255 owners.')

# The finite normalization of a reduced compact curve is a disjoint union.
# Every local derivative lattice and every local defect stays identical.
replacements=[
 (r'Let $C$ be a compact irreducible reduced curve in a smooth complex threefold $Y$, with normalization $\nu_C:E\to C$, inclusion $i:C\hookrightarrow Y$ and $j=i\nu_C$. Let $g$ be the genus of $E$, and suppose $\deg j^*\Omega_Y=0$.',
  r'Let $C$ be a compact reduced curve in a smooth complex threefold $Y$, with normalization $\nu_C:E=\coprod_{a=1}^c E_a\to C$, inclusion $i:C\hookrightarrow Y$ and $j=i\nu_C$. Let $g_a$ be the genus of $E_a$, and suppose $\deg(j|_{E_a})^*\Omega_Y=0$ for every $a$. Put $\gamma=\sum_{a=1}^c(1-g_a)$.'),
 (r'\chi(\mathcal O_Y/P^{(2)})=5(1-g)-\sum_p d_p.',r'\chi(\mathcal O_Y/P^{(2)})=5\gamma-\sum_p d_p.'),
 (r'\deg K=2-2g+\deg R.',r'\deg(K|_{E_a})=2-2g_a+\deg(R|_{E_a}).'),
 (r'Riemann--Roch on $E$ gives',r'Write $j_a=j|_{E_a}$ and $K_a=K|_{E_a}$. The direct image is the finite direct sum $j_*K=\bigoplus_a(j_a)_*K_a$. Riemann--Roch on each $E_a$, followed by addition of these Euler characteristics, gives'),
 (r'\chi(Q)=4(1-g)+\deg R-\tau.',r'\chi(Q)=4\gamma+\deg R-\tau.'),
 (r'The normalization sequence gives $\chi(\mathcal O_C)=1-g-\sum_p\delta(C,p)$.',r'The normalization sequence for this same $\nu_C$ gives $\chi(\mathcal O_C)=\gamma-\sum_p\delta(C,p)$.'),
 (r'proves the formula. For $E=\mathbb P^1$ it reads $5-\sum_p d_p$; for an elliptic $E$ its constant term is zero.',
  r'proves the formula. For $E=\mathbb P^1$ it reads $5-\sum_p d_p$; for a connected elliptic $E$ its constant term is zero; for two rational normalized components its constant term is ten. All local lengths below are computed from the same map $Q\hookrightarrow j_*K$, including branches which belong to different global components.')]
s=SOURCE.read_text(); start=s.index(r'\begin{lemma}[Conormal defects of compact curves]');end=s.index(r'\begin{lemma}[Primary ordinary-triple conductor schemes]',start)
old=s[start:end];new=old
for a,b in replacements:
    assert new.count(a)==1,a
    new=new.replace(a,b,1)
apply_edit(old,new,'II-C3-CONORMAL-DISJOINT-NORMALIZATION',['D12','D25'],
 'lem:II:rational-conormal-defects','Full conormal owner',
 'Extend the common owner to the finite disjoint normalization already used in P4.46, through the displayed direct-sum pushforward and componentwise Riemann--Roch. Every local lattice, minor, conductor residue and colength proof is unchanged; the original connected cases are the substitutions c=1, g_1=g.')

s=SOURCE.read_text();start=s.index(r'\begin{proposition}[Euler bound for uniform ordinary-triple ruled supports]');end=s.index(r'\subsection{The full quadratic conductor at three axes}',start)
old=s[start:end];new=old
new=new.replace(r'\SeriesRef{night:P4.34}',r'\cref{lem:II:rational-conormal-defects,lem:II:triple-conductor-symbolic-square}')
a=r'''The remaining critical curve has two rational normalized
components and one graph cycle. For the actual
conductor scheme, ordinary-triple transverse type gives
the ideal $P^{(2)}$, as in \cref{night:P4.31}. Let $Q=P/P^{(2)}$,
and let $\tau_p$ be the full colength of its differentiated
image in the direct image of the normalized rank-two
kernel $K$. This includes both the branchwise lattice
colength and the further descent colength. Riemann--Roch
on the two normalized projective lines gives'''
b=r'''The remaining critical curve $C=C_1\cup C_2$ has two rational normalized
components and one graph cycle. Let $\nu:N\to S$ be normalization,
let $P_i$ be the reduced ideal of $C_i$, and put $P=P_1\cap P_2$.
Apply \cref{lem:II:triple-conductor-symbolic-square} to this same $\nu$
and to each $C_i$. Its primary conductor ideals are $P_i^{(2)}$.
The conductor quotient is Cohen--Macaulay of dimension one by
\cref{lem:II:conductor-duality}, so it has no isolated primary component.
Its full ideal is therefore $P_1^{(2)}\cap P_2^{(2)}=P^{(2)}$;
the equality follows by imposing order two on exactly the same generic branches.
Apply \cref{lem:II:rational-conormal-defects} to this full $C$, with
$E=E_1\amalg E_2$, $E_i=\mathbb P^1$, $j_i:E_i\to Y$ the normalization
followed by inclusion, and $Q=P/P^{(2)}$. The standing first-Chern-class
vanishing gives $\deg j_i^*\Omega_Y=0$ on each component.
Let $\tau_p$ be the full colength of $Q$ in
$(j_1)_*K_1\oplus(j_2)_*K_2$. It includes the branchwise lattice
and descent colengths. The lemma's formula, with $\gamma=2$, gives'''
assert a in new;new=new.replace(a,b,1)
new=new.replace(r'the exact different calculation in \cref{night:P4.34}.',r'\cref{lem:II:rational-conormal-defects}, applied to the same local plane equation and its normalized derivative lattice.')
new=new.replace(r'Each contributes at least five by \cref{night:P4.34}; equality is',r'Apply the local estimates of \cref{lem:II:rational-conormal-defects} to the same ideal $P$ at each of these points. Each contributes at least five; equality is')
assert 'night:P4.34' not in new
apply_edit(old,new,'II-C3-TRIPLE-RULED-CONORMAL-MAP',['D08','D12','D18','D25'],
 'night:P4.46','Complete ordinary-triple ruled-support proof',
 'Keep the original statement and all three-branch estimates. Specify the two primary conductor ideals, their unmixed intersection, and the finite direct-sum conormal map before applying the single full conormal owner. The P4.45 application remains subject to its open proof gate.')

# A metadata-only dependency still pointed at the aliased special case.
s=SOURCE.read_text();m=re.search(r'\\StatementRecord\{night:P4\.42\}[^\n]+',s)
assert m
if 'night:P4.34' in m.group(0):
    apply_edit(m.group(0),m.group(0).replace(r'\SeriesRef{night:P4.34}',r'\cref{lem:II:plane-branch-conductor}'),
      'II-C3-NODAL-CONORMAL-DEPENDENCY',['D12'],'night:P4.42','Statement dependency record',
      'Resolve the planar different dependency through the same residue/conductor owner used in the receiving proof.')

add_event('lem:II:conductor-two-branch-cycle; night:P4.35',
 'II-C3-ROOT-CONDUCTOR-CYCLE-RECEIVING','used and rechecked in this run',
 'Root read the complete old P4.35 proof and the entire actual P255/P4.35 receiving unit. The exact factorization h kappa = eta phi, finite surjectivity on all normalized conductor components, height-two pairwise surface intersections and common-plus argument give sum(r_q-1)>=c and beta(D)>=b0(D). The five retained rational-resolution, formal-functions, exceptional-cohomology, quotient-fundamental-group and ruled-tree steps remain complete. The receiving first item now states the precise depth-two ideal/depth-one quotient comparison. Every local defect type was read; bibliography-wide verification, final placement and final pages remain open. No independent credit.',
 'S6_SERIES_PUBLISH_II.tex: Conductor graphs and rational Euler numbers',source=__file__)
for number in range(1,26):
    kind=f'D{number:02}'
    if kind in ['D10','D16']:continue
    status='open' if kind in ['D14','D18','D23'] else 'done'
    set_unit_status('night:P4.35',kind,status,
      'Complete original/receiving unit comparison; final placement, bibliography-wide verification and final rendered typography remain open.' if status=='open' else 'Complete current unit read for this defect type; all instances recorded and no local residue found.',
      'CHECK_EVENTS.tsv: II-C3-ROOT-CONDUCTOR-CYCLE-RECEIVING')
add_event('lem:II:rational-conormal-defects; night:P4.42; night:P4.46; night:P4R.18; night:P4.55',
 'II-C3-ROOT-CONORMAL-CONSUMER-MAPS','used and rechecked in this run',
 'Root read the complete P254 and P4.46 old/receiving proofs and all four refined-owner transfer guards. P254 extends its Euler identity through E=disjoint union E_a and j_*K=direct sum (j_a)_*K_a, retaining every local calculation. P4.46 applies P256 separately to the two global conductor components; unmixedness and the identical generic-order conditions identify their intersection with P^(2). The conormal substitution gamma=2 gives ten. Its three-branch estimate 11, singular-branch excess-one classification and two-node equality argument remain complete. The P4.45 premise remains explicitly open. P4.42 uses the exact residue order c_i=v_i-r_i; R18 uses that identical plane ideal; P4.55 uses the same rational normalization in P254 and selected conductor subcurve in P255. This is exposed comparison, with no independent or final-page credit.',
 'S6_SERIES_PUBLISH_II.tex: common conormal owner and exact applications',source=__file__)
print('Shared conductor and conormal receiving comparisons recorded; P4.45 gate remains open.')
