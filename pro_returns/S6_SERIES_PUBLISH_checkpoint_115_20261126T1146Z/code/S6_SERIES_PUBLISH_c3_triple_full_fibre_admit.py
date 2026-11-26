"""Admit the complete weighted cubic proof and its current subsection review."""
from S6_SERIES_PUBLISH_c3_edit import *

folder=ROOT/'agents/continuation3_provenance/p445'
prefix='S6_SERIES_PUBLISH_p445_'
_,guards=read_tsv(folder/(prefix+'guards.tsv'));assert len(guards)==1
before=SOURCE.read_text();after=before
for row in guards:
    assert after.count(row['old_text'])==1
    after=after.replace(row['old_text'],row['new_text'],1)
preserve_identifiers(before,after)
for oldids,newids in zip(identifiers(before),identifiers(after)):
    for name,count in oldids.items():assert newids[name]==count,name
    for name,count in (newids-oldids).items():assert newids[name]==1,name
SOURCE.write_text(after,newline='\n')
for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
    _,items=read_tsv(folder/(prefix+suffix));print(suffix,append_rows(ROOT/target,items,key))
apply_edit(r'''Let $f\in\C\{u,x,y\}$ be reduced, with reduced critical locus
$C=\{u=h(x,y)=0\}$, where $h$ is reduced.''',
 r'''Let $f\in\C\{u,x,y\}$ be reduced, with $f(0)=0$ and reduced
critical locus $C=\{u=h(x,y)=0\}$, where $h$ is a nonzero
reduced germ with $h(0)=0$.''',
 'II-C3-TRIPLE-FACTOR-GERM-DOMAIN',['D25'],'lem:II:ordinary-triple-factor-lifts','Opening germ data',
 'Make the nonempty pointed hypersurface and curve germs explicit, as in the complete original P4.45 input. The zero-cubic and factor-block cases retain their entire proved scope.')

s=SOURCE.read_text();start=s.index(r'\begin{proposition}[The contracted section and three-branch critical point]');end=s.index(r'\begin{lemma}[Cubic normalization and factor lifts]',start)
old=s[start:end];new=old
a=r'''In the remaining positive ruled case with generic transverse
type $A_3$ on every conductor component, the horizontal
section of the pole divisor is contracted by the resolution
map. The point-identification cycle occurs at a single
three-branch point of the critical curve.'''
b=r'''In the setting of \cref{lem:II:positive-ruled-conductor-graph},
suppose that the generic transverse type along every image-conductor
component is $A_3$. Then the horizontal section $H$ of the pole
divisor is contracted by the minimal normalization resolution
$\sigma:T\to N$. The point-identification cycle of the reduced
image conductor $C$ occurs at a single three-branch point.'''
assert a in new;new=new.replace(a,b,1)
a=r'''\item P4.42 excludes a cycle at two two-branch points. The
remaining graph has two rational normalized components
and one cycle, so its cycle occurs at one three-branch
point $p$.'''
b=r'''\item Apply \cref{lem:II:positive-ruled-conductor-graph} to this
same full fibre $mS$ and the maps $T\xrightarrow{\sigma}N\xrightarrow{\nu}S$.
It gives two rational normalized conductor components and
$\sum_{p\in C}(r_p-1)=2$. The one cycle therefore occurs either
at two two-branch points or at one three-branch point.
Proposition~\ref{night:P4.42}, with this same conductor and
its uniform transverse type $A_3$, excludes the first case.
Thus the cycle occurs at one three-branch point $p$.'''
assert a in new;new=new.replace(a,b,1)
for a,b in [('P4R.14',r'\cref{night:P4R.14}'),('P4R.6',r'\cref{night:P4R.6}'),
            ('By (4.42a) and P4.33',r'By \eqref{eq:II:refined-4-42a} and \cref{night:P4.33}'),
            ('estimate in P4.42',r'estimate in \cref{night:P4.42}')]:
    # Bound every replacement to body prose, never the existing stable keys.
    head,body=new.split(r'\begin{proof}',1)
    body=body.replace(a,b);new=head+r'\begin{proof}'+body
apply_edit(old,new,'II-C3-THREE-BRANCH-CONTRACTED-SECTION',['D04','D08','D12','D25'],
 'night:P4.44','Full contracted-section proposition',
 'Spell out the existing positive ruled hypotheses through P314 and the identical full fibre and normalization maps. Its branch-count equality supplies the exhaustive cycle alternatives. Resolve all printed run/formula names. Preserve the degree-two cover, both R14 germs, every defect estimate and the exact Riemann--Hurwitz contradiction.')

add_event('lem:II:ordinary-triple-factor-lifts; night:P4.45; night:P4.46',
 'II-C3-ROOT-TRIPLE-FULL-FIBRE-ADMISSION','used and rechecked in this run',
 'Root read the complete old P4.45 proof, complete receiving P280/P4.45 proof, full comparison, and the editorial algebra program at its bounded scope. P280 proves the cubic ideal membership through the CM filtration, identifies the exact normalization by its determinant presentation and depth-two extension, distinguishes the local square-zero fibre through its algebra, and gives irreducible factor lifts by the displayed localization isomorphism and factorial descent. The full unit and all positive m_j remain in G_tau. Root checked the positive-weight logarithmic derivative and simple critical root, the variable-coefficient Psi equation, both Lambda inverse identities, the exact critical value hhat_s^N and Schur determinant. The triple-branch coordinate maps and degree-N unit inverse verify full-function boundary charts; inner and outer transports are explicitly composed. Its sole outward mathematical consumer P4.46 has the entire planar nodal critical curve and D4 along each branch. The original P4.45 scope is preserved. This resolves the last of the four full-fibre multiplicity premises opened at review25. R14, R15 and P4.41 were already resolved; UN9 is separately resolved. Protected E.5.2/E.5.3 statements are unchanged. No independent proof or final-page credit.',
 'S6_SERIES_PUBLISH_II.tex: ordinary-triple factor algebra and full weighted deformation',source=__file__)
add_event('night:P4.44; lem:II:ordinary-triple-factor-lifts; night:P4.45; night:P4.46',
 'II-C3-ROOT-UNIFORM-TRANSVERSE-UNIT','used and rechecked in this run',
 'Root read the entire current Further uniform transverse sectors subsection, every original proof replaced here and every receiving proof. The four owners are P4.44, P280, P4.45 and P4.46. P4.44 now explicitly applies P314 on the same maps and preserves its full degree-two cover and branch-value bound. P4.46 retains all three-branch colength bounds and uses the exact two-component normalization in P254 and the unmixed primary conductor intersection from P256. Its final P4.45 premise is now proved at the original full-multiplicity scope. The comparison records all local defects; final placement, bibliography-wide verification and final rendered pages remain open.',
 'S6_SERIES_PUBLISH_II.tex: Further uniform transverse sectors',source=__file__)
for number in range(1,26):
    kind=f'D{number:02}'
    if kind in ['D10','D16']:continue
    status='open' if kind in ['D14','D18','D23'] else 'done'
    set_unit_status('night:P4.44',kind,status,
      'Complete old/receiving subsection read; final whole-paper placement, bibliography or rendered typography remains.' if status=='open' else
      'Complete current subsection read against this defect type; all instances recorded and no local residue found.',
      'CHECK_EVENTS.tsv: II-C3-ROOT-UNIFORM-TRANSVERSE-UNIT')
for unit in ['night:P4R.18','night:P4.55','night:P4.58']:
    set_unit_status(unit,'D25','done',
      'The complete refined-consumer comparison already reviewed the unit. Its remaining full-fibre premise is now resolved by P280/P4.45 through the identical P4.46 application; no statement or hypothesis is weakened.',
      'CHECK_EVENTS.tsv: II-C3-ROOT-TRIPLE-FULL-FIBRE-ADMISSION; II-C3-ROOT-REFINED-CONSUMERS-ADMISSION')
print('All four review25 full-fibre multiplicity premises resolved; full uniform-transverse unit read. Final paper gate remains open.')
