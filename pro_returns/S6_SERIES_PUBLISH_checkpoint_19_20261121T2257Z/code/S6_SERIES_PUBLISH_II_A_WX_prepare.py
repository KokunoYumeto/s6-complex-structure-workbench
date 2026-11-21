"""Prepare reviewable WX guards; never write canonical source or ledger."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re

BASE=Path('agents/ii_checks_A/recovery_20261121T195642Z')
OUT=BASE/'group10_WX'
OUT.mkdir(exist_ok=True)
source=Path('agents/ii_infra/released_proofs/02WX/165aa156c61940fe/S6_SERIES_PUBLISH_full_owning_block.tex')
original=source.read_text()
oldpath=OUT/'S6_SERIES_PUBLISH_II_02WX_full_original.tex'
newpath=OUT/'S6_SERIES_PUBLISH_II_02WX_full_proposed.tex'
oldpath.write_text(original)
text=original
guards=[]
def sha(s): return hashlib.sha256(s.encode()).hexdigest()
def edit(old,new,types,why,transport):
    global text
    assert text.count(old)==1, (len(guards), old[:120], text.count(old))
    before=text
    at=text.index(old)
    text=text.replace(old,new,1)
    guards.append({'tag':'02WX','guard_id':f'A_REC_02WX_{len(guards)+1:03}',
        'defect_types':types,'literal_old':old,'literal_new':new,'reason':why,
        'mathematical_transport':transport,'offset_before':at,
        'intermediate_before_sha256':sha(before),'intermediate_after_sha256':sha(text),
        'full_original_path':str(oldpath),'full_proposed_path':str(newpath)})

edit('[P4.25]','[Semi-log-canonical fibre supports]',['D04','D16'],
     'Use a mathematical title.','Owner, tag and all labels retain their exact identities.')

old=r'''Every semi-log-canonical reduced fibre support in
Part~4.2 has normal crossings. In particular, let
$\rho:T\to N\to S$ be a resolution of the normalization
of an irreducible support, and let $D$ be the integral
divisor defined by
$\omega_T(D)\simeq\rho^*\omega_S$. When this actual
divisor is reduced and has normal crossings, $S$
has normal crossings, its normalization is smooth,
and P4.6--P4.8 apply.'''
new=r'''Let $f:Y\to B$ be a proper surjective holomorphic map with connected
fibres from a connected smooth compact complex threefold to a smooth
compact curve. Assume $b_1(Y)=b_2(Y)=0$ and that the smooth general
fibre is a complex two-torus. Every semi-log-canonical reduced fibre
support of $f$ has normal crossings.

For an irreducible reduced support $S$, let $\nu:N\to S$ be its
normalization, let $\pi:T\to N$ be a resolution, and put
$\rho=\nu\circ\pi$. For local residue generators $\Omega$ of $\omega_S$,
define the integral divisor $D=-\operatorname{div}(\rho^*\Omega)$, so that
$\omega_T(D)\simeq\rho^*\omega_S$ with this identification.
A reduced normal-crossing divisor $D$ gives normal crossings on $S$
and a smooth normalization $N$. Proposition~\ref{night:P4.6} applies
to each such support. Propositions~\ref{night:P4.7}--\ref{night:P4.8}
apply to fibrations whose reduced supports are all semi-log-canonical.'''
edit(old,new,['D05','D08','D20','D25'],
     'State the standing map, specify the residue divisor and supply the all-supports domain of the global invocation.',
     'The exact standing domain is the safe named-input packet. rho=nu o pi and D=-div(rho*Omega) specify the intended identity. The local NC conclusions and full reducible-support scope are retained; the final global invocation now carries its existing all-supports hypothesis. Root receiver SHA9531e0ac… binds its retained local uses.')

edit(r'''\item We first explain why the stated resolved-conductor
case is semi-log-canonical.''',r'''\item At a generic point of the conductor,''',['D08','D22'],
     'Start the proof with its mathematical locus.',
     'The same resolution and conductor are used; the subsequent generic-branch calculation supplies the assertion.')
edit('At a generic conductor\npoint, an exponent one on every normalization\nbranch','an exponent one on every normalization\nbranch',['D20'],
     'Join the unchanged generic-branch calculation to the preceding locus.',
     'No branch, exponent or quantifier changes.')
edit('On its normal\nnormalization $N$, the pair consisting of $N$','On its normalization $N$, the pair consisting of $N$',['D08'],
     'Remove the repeated adjective.', 'The normalization morphism is the already specified nu.')
edit(r'''This is precisely the
semi-log-canonical definition of
Liu--Rollenske, Definition~2.3 and Lemma~2.2,
which explicitly applies to complex analytic
spaces.''',r'''Definition~2.3 and Lemma~2.2 of
\cite[p.~189]{LiuRollenske2012SLC} give semi-log-canonicity in
the complex analytic category.''',['D06','D18','D22'],
     'Bind the analytic definition and crepant comparison to the opened published edition.',
     'Published pp188–190 were read completely; the same pair (N,D_N) is related to (T,D) by K_T+D=pi*(K_N+D_N).')

edit(r'''\item We now treat all local semi-log-canonical
hypersurface germs. We use the complete analytic
classification in Liu--Rollenske,
\emph{Two-dimensional semi-log-canonical
hypersurfaces}, main Theorem, Table~1,
Propositions~3.1 and~4.1. The normal singular
germs are isolated.''',r'''\item The analytic classification is
\cite[Theorem~1.1, p.~186; Table~1, p.~187;
Propositions~3.1 and~4.1, pp.~192--200]{LiuRollenske2012SLC}.
An isomorphism of the singular hypersurface germs lifts to an ambient
biholomorphism: lift its three coordinate classes to convergent functions;
the induced cotangent isomorphism makes their linear part invertible.
Thus, in the displayed coordinates, the full local fibre function is
$U\prod_i g_i^{m_i}$, with $U$ a unit and the original component
multiplicities $m_i$. The normal singular germs in the table are isolated.
Each is irreducible, since distinct surface branches would meet along
a singular curve. Write its full function as $Ug^m$, choose a holomorphic
$m$th root of $U$, and set $h=U^{1/m}g$, so that $f=h^m$.''',
     ['D06','D18','D20','D25'],
     'Supply the exact ambient map and full multiplicity at the classification input.',
     'The cotangent map lifts the same analytic hypersurface isomorphism to the smooth ambient germ. f=h^m keeps the original unit and multiplicity; the isolated normal cases are unchanged.')

edit('perturbation of its reduced equation has\nMorse critical points, the number counted\nwith multiplicity being the positive\ncolength of its gradient ideal. The equality\nof this number before and after perturbation\nfollows by conservation of the local\nintersection multiplicity of the three\ngradient equations.',r'''perturbation $h-c\cdot z$ has Morse critical points.
Their number is the positive multiplicity of the gradient map
\cite[Appendix~B, Lemmas~B.1--B.3 and the positivity proof,
pp.~111--114]{Milnor1968}. It is also the colength of the gradient ideal:
the map $\mathbb C\{u\}\to\mathbb C\{z\}$,
$u_i\mapsto h_{z_i}$, is finite; its three parameters form a regular
sequence, so its target is a free module of that colength. A regular
nearby fibre consists of that many reduced points, each of local degree
one. The boundary degree is unchanged under the small perturbation.''',
     ['D06','D18','D20','D22'],
     'Give the primary locus and exact module/degree transport for the printed multiplicity count.',
     'The comparison proves finite free module rank=colength=boundary degree, retaining the printed positive number and all Morse critical points.')
edit('transport proved in P4.20 carries a','transport in the proof of Proposition~\\ref{night:P4.20} carries a',['D04'],
     'Resolve the internal boundary-transport reference.', 'The same local boundary horizontal-flow construction is used.')

edit(r'''\item For the nonnormal germs we give the exact
deformations and check their boundary strata.
The ordinary double point and $xyz=0$
already have normal crossings. A pinch point
$x^2+y^2z=0$ is excluded by P4.16.''',r'''\item The ordinary double point and $xyz=0$ have normal crossings.
The change $z\mapsto-z$ identifies the pinch point $x^2+y^2z=0$
with the case $n=2$ of Proposition~\ref{night:P4.16}.
For a weighted homogeneous full function $G$ of positive weights
$(w_1,w_2,w_3)$ and degree $W$, the unit is absorbed by the
biholomorphism
\[
 (z_1,z_2,z_3)\longmapsto
 (U(z)^{w_1/W}z_1,U(z)^{w_2/W}z_2,U(z)^{w_3/W}z_3),
\]
using one local logarithm of $U$; it satisfies $G\circ\Psi=UG$.
The weights used below are positive. Scaling the coordinates by
$\lambda^{w_i}$ places every compact cycle in $G^{-1}(1)$ in
$G^{-1}(\lambda^W)$ inside an arbitrarily small neighborhood.
For a deformation $G_s$ of an irreducible reduced equation with full
multiplicity $m$, use the full map $G_s^m$. At nonzero values its
levels are the disjoint union of the levels $G_s=\zeta t^{1/m}$,
where $\zeta^m=1$, and
$d(G_s^m)=mG_s^{m-1}dG_s$. Thus the boundary transport on these
levels carries the original full multiplicity.''',
     ['D04','D08','D20','D25'],
     'Resolve the pinch reference and make the unit and local-fibre maps explicit.',
     'The coordinate map has invertible diagonal derivative and the exact equation G o Psi=UG. Positive scaling preserves the oriented normal bundle and actual component multiplicities.')

edit(r'''The local proof of P4.20
therefore supplies a vanishing sphere after
a deformation retaining its boundary
ordinary-double strata.''',r'''Put $U_1=x-iyz$ and $U_2=x+iyz$, and let their full fibre
multiplicities be $a,b>0$. For $d=\gcd(a,b)$ write
$a'=a/d$, $b'=b/d$. On the component $U_1^{a'}U_2^{b'}=1$
of $U_1^aU_2^b=1$, set
\[
 U_1=t^{b'},\qquad U_2=t^{-a'},\qquad
 yz=\frac{t^{-a'}-t^{b'}}{2i}.
\]
The inverse parameter is $t=U_1^rU_2^s$ for integers
$rb'-sa'=1$. The last equation has $a'+b'\ge2$ simple nonzero
zeros in its right-hand side. Over an arc joining two of them,
the circles $|y|=|z|$ collapse at the endpoints and form a smooth
embedded sphere. The circle action $(y,z)\mapsto(e^{i\theta}y,
e^{-i\theta}z)$ has moment map proportional to $|y|^2-|z|^2$,
so the sphere is Lagrangian. Its oriented normal Euler number is
$-\chi(S^2)=-2$: the order $(e_1,e_2,Je_1,Je_2)$ differs by one
transposition from the complex orientation $(e_1,Je_1,e_2,Je_2)$.
Weights $(2,1,1)$ place this sphere in the full nearby fibre with
the original multiplicities. Every sphere in a complex two-torus
lifts to $\mathbb C^2$ and contracts there, so its homology class,
and hence its self-intersection, is zero. This excludes the germ.''',
     ['D20','D22','D25'],
     'Fill the untracked unequal-component-multiplicity case of the tangent-sheet exclusion.',
     'The exact monomial map and Bezout inverse identify a component of the same full U1^a U2^b fibre with the displayed conic bundle. It produces the required sphere for every positive pair a,b; the theorem is not weakened.')

edit(r'''\item For finite $q$ put''',r'''\item For finite $q$, the equation is analytically irreducible:
its weighted homogeneous polynomial of weights $(q,2,q-2)$ is
irreducible, and lowest weighted terms of an analytic factorization
would factor that polynomial. Thus its full multiplicity is a common
integer $m$. After the unit map above, put''',['D20','D25'],
     'Bind the common multiplicity needed by the finite-q deformation transport.',
     'The quadratic in x factors only when z²+y^(q−2) is a square in the fraction field; its reduced divisor has odd valuations. The exact weights and initial-form argument are in the frozen derivation.')
edit('by the detailed P4.20 construction, to','by the boundary transport in Proposition~\\ref{night:P4.20}, to',['D04'],
     'Resolve the internal proof reference.', 'Same deformed pinch class and same boundary flow.')
edit('The actual equation there is exactly','The reduced equation in these coordinates is',['D08','D20'],
     'Identify the reduced equation while the full map retains its stated power.',
     'The coordinate Z is unchanged; the full local map is the mth power as specified above.')

edit(r'''The local argument of P4.20 on
the deformed germ supplies a compact
spherical class of nonzero square, and
the same boundary transport gives the
contradiction.''',r'''For full component multiplicities $a,b$, weights $(2,p-1,p-1)$
give degree $2a+2(p-1)b$ and absorb the original unit. Use the deformation
$x^a(yz+x^{p-1}+sx)^b$. At its boundary double strata, free normal
coordinates $u,v$ give $u^av^b$, which is submersive at nonzero
values; thus the same boundary transport applies with these multiplicities.
For fixed nonzero $s$, the coordinate $X=x(s+x^{p-2})$ is
biholomorphic near the origin. The full deformed function becomes
a unit times $X^a(X+yz)^b$. The coordinates
\[
 x'=X+yz/2,\qquad y'=y,\qquad z'=z/(2i)
\]
satisfy $x'-iy'z'=X$ and $x'+iy'z'=X+yz$.
After absorbing the unit with weights $(2,1,1)$, the preceding
two-branch case supplies a sphere of square $-2$. Boundary transport
therefore gives the contradiction in the original full fibre.''',
     ['D20','D22','D25'],
     'Preserve the printed deformation while carrying each component multiplicity and giving the exact map to the already excluded two-branch germ.',
     'x↦X has derivative s≠0; x/X is a unit. The displayed triangular map sends the two factors exactly to x′∓iy′z′. Boundary u^a v^b is submersive away from zero, so the original proper flow carries this sphere.')

edit(r'''\item For the second equation put''',r'''\item For the second equation, positive weights
$(q,p,pq-p-q)$ and the primitive degree-one expression in $z$
show analytic irreducibility by the same initial-form argument.
It therefore has one common full multiplicity. Put''',['D20','D25'],
     'Bind the multiplicity for the finite-p finite-q deformation.',
     'g=xyz+x^p+y^q is primitive linear in z with gcd(xy,x^p+y^q)=1; positive weighted initial parts identify the same analytic germ.')
edit('P4.20 again\nproduces a spherical class, with the\nalready verified boundary transport.',r'''The local construction in Proposition~\ref{night:P4.20} produces
a spherical class of nonzero square, and its boundary transport gives
the contradiction. The transverse Hessians and the restrictions
$H(0,z)$ and $H_y(0,0)$ follow by collecting the degree-two terms
and substituting the critical equation
$yz+p\xi^{p-1}+2s\xi=0$.''',['D04','D22'],
     'Resolve the proof reference and state the method and inputs of the displayed calculations.',
     'All original Hessian, critical-remainder and normalization formulas are retained. Exact sparse-jet and implicit-recursion checks agree with each displayed quantity.')

edit('Their tangent planes coincide, so the\norigin is not a normal crossing.',
     r'''Their tangent planes coincide. The two branches of $uv=0$ have
distinct tangent planes, and an ambient biholomorphism has an invertible
derivative preserving that distinction. Hence these two tangent branches
cannot be a normal crossing.''',['D20','D22'],
     'State the differential obstruction through the exact double-crossing local model.',
     'The displayed two smooth factors keep their graph maps; their equal tangent planes cannot be the image of the two distinct coordinate planes under an invertible derivative.')
edit('differential has rank one, so this germ\nis not a normal crossing.',
     r'''differential has rank one. The normalization of a normal-crossing
germ consists of coordinate-plane inclusions, all of differential rank
two. The normalization isomorphism induced by an ambient biholomorphism
preserves these ranks, so this rank-one map excludes normal crossings.''',
     ['D20','D22'],'Supply the exact normalization-map comparison behind the rank obstruction.',
     'The finite birational map (v,y,z)↦(yv,y,z) is unchanged. Its computed rank is compared with the canonical normalization maps of the explicit NC equations.')

edit(r'''\item These calculations exhaust the analytic
classification. Thus only the smooth,
ordinary-double, and triple-normal-crossing
germs remain. Their local equations give
the claimed normal-crossing support and
smooth normalization.''',r'''\item The remaining germs in Table~1 are smooth, ordinary double,
and triple normal crossing. The linear coordinates
$(u,v)=(x+iy,x-iy)$ give $uv=0$ for the double germ;
the triple germ is $xyz=0$. Their normalization morphisms are the
inclusions of their disjoint smooth coordinate-plane branches.
Proposition~\ref{night:P4.6} applies to each compact support so obtained.
When every reduced support is semi-log-canonical, the same local
conclusion at every fibre supplies the hypotheses of
Propositions~\ref{night:P4.7}--\ref{night:P4.8}.''',['D08','D20','D25'],
     'Give the exact final local maps and the quantified global application.',
     'The same three classification entries survive. The normalization maps are explicit. The global application retains the all-supports hypotheses already present in P4.7/P4.8.')

newpath.write_text(text)
canonical=Path('S6_SERIES_PUBLISH_II.tex').read_text()
bib=canonical[canonical.index('\\begin{thebibliography}'):canonical.index('\\end{thebibliography}')]
bibs=[]
lr=r'''\bibitem[Liu and Rollenske(2012)]{LiuRollenske2012SLC}
Wenfei Liu and S{\"o}nke Rollenske.
\newblock Two-dimensional semi-log-canonical hypersurfaces.
\newblock \emph{Le Matematiche}, 67(2):185--202, 2012.
\newblock doi:\href{https://doi.org/10.4418/2012.67.2.14}{10.4418/2012.67.2.14}.

'''
assert ']{LiuRollenske2012SLC}' not in bib
anchor=r'\bibitem[Liu and Rollenske(2026)]{LiuRollenske2026}'
assert bib.count(anchor)==1
bibs.append({'key':'LiuRollenske2012SLC','literal_old':anchor,'literal_new':lr+anchor,
    'defect_types':['D06','D18'],'reason':'Add the exact published primary classification that the proof names.',
    'mathematical_transport':'Same author/title/theorem as the named input and historical preprint; current locators are the opened published pages. PDF SHAdef3c8f41… binds the complete published text.'})
m=re.search(r'\\bibitem\[Milnor\(1968\)\]\{Milnor1968\}.*?(?=\\bibitem|\Z)',bib,re.S)
assert m
mb=m.group();mn=mb.replace('\\newblock \\emph{Verified}.\n','');assert mn!=mb
bibs.append({'key':'Milnor1968','literal_old':mb,'literal_new':mn,
    'defect_types':['D08'],'reason':'Remove the production-status word from the primary bibliography entry.',
    'mathematical_transport':'Author, title, volume, publisher, year and ordinary public viewer URL stay unchanged; exact page images are bound in the primary-reading record.'})
for b in bibs:
 b['source_path']='S6_SERIES_PUBLISH_II.tex';b['source_sha256']=sha(canonical)
 b['source_character_offset']=canonical.index(b['literal_old'])

program_rows=[]
for name,scope in [
 ('S6_SERIES_PUBLISH_II_A_02WX_conic_maps.py','Conic coordinate maps, component multiplicities, weighted scalings and oriented sphere Euler numbers'),
 ('S6_SERIES_PUBLISH_II_A_02WX_deformation_jets_postrelease.py','Transverse two-jets and critical-value remainders of the double and triple deformations')]:
 program_rows.append(scope+r' (\cref{night:P4.25}) & \href{https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/\SsixRepositoryCommit/code/'+name+r'}{\nolinkurl{'+name+r'}} \\[3pt]'+'\n')
program_anchor=canonical[canonical.index('\\section*{Programs}'):canonical.index('\\end{longtable}',canonical.index('\\section*{Programs}'))+len('\\end{longtable}')]
program_new=program_anchor.replace('\\end{longtable}',''.join(program_rows)+'\\end{longtable}')
program_guard={'literal_old':program_anchor,'literal_new':program_new,
 'defect_types':['D09'],'reason':'Cite the two new computations once in the end Programs table through the common commit macro.',
 'mathematical_transport':'Each row names its exact WX mathematical scope. The new independent conic certificate and postrelease deformation certificate have separate timing records; no existing program is reassigned.',
 'source_path':'S6_SERIES_PUBLISH_II.tex','source_sha256':sha(canonical)}
manifest={'created_utc':datetime.now(timezone.utc).isoformat(),'checker':'ii_check_a','canonical_writes':False,
 'guards':guards,'blocks':[{'tag':'02WX','original_path':str(oldpath),'proposed_path':str(newpath),
 'original_sha256':sha(original),'proposed_sha256':sha(text),'statement_unchanged':False,
 'scope_repairs':['Specify the all-supports domain for the final P4.7/P4.8 invocation.'],
 'proof_repairs':['Carry arbitrary component multiplicities through the two reducible non-NC families.','Make the intended residue divisor and unit/ambient-coordinate maps explicit.']}],
 'bibliography_guards':bibs,'program_table_guard':program_guard,
 'note':'Proposal only; root integration required. Seven printed proof items and all their displayed deformation/Hessian/normalization computations are retained. Enumeration wrapper is reserved for the final global mapping.'}
(OUT/'S6_SERIES_PUBLISH_II_A_WX_editorial_proposals.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'guards':len(guards),'original_sha256':sha(original),'proposed_sha256':sha(text),'manifest':str(OUT/'S6_SERIES_PUBLISH_II_A_WX_editorial_proposals.json')}))
