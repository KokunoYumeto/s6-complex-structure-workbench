# This module is executed in the roots builder's namespace before final cleaning.
# All edits are guarded replacements in standalone proposals; no shared source writes.

# The repeated real period determinant has its single earlier owner in UN73.
old73=block(main,'cdp:st:C.2.UN.73')
old_tx7=display(old73,'cdp:eq:C.TX.7')
hook=r'\hypertarget{tag-016E}{}\SsixEquationAliases{\label{cdp:eq:C.WF.18}}'
new_tx7=old_tx7.replace(r'\[', '\\[\n'+hook, 1)
pkg.equations.append(dict(old_tag='C.WF.18',label='cdp:eq:C.WF.18',owner='cdp:st:C.2.UN.73'))
pkg.record('D12,D19,D20','cdp:st:C.2.UN.73','C.WF.18 / tag016E','C.TX.7 with C.WF.18 alias and tag016E','The exact same real determinant is consolidated here; UN76 gives the full real basis transport and its positive determinant factor.')
new_tx7=pkg.clean(new_tx7,'cdp:st:C.2.UN.73',prose=False).strip()
old_det76=part(new76,'Changing the logarithm adds an angular period.',r'Thus \eqref{cdp:eq:C.WF.17}')
new76=pkg.edit(new76,old_det76,r'''Changing the logarithm adds an angular period. Write
$\Lambda=P\Z^2$ with $P\in\operatorname{GL}_2(\R)$ and first
use this finite-index sublattice of $\Lambda_0$ for the angular
generators. Right-multiplication of the four real period columns
by $\operatorname{diag}(P^{-1},P^{-1})$ gives the columns in
\eqref{cdp:eq:C.TX.4}, with $(t,b')=(s,B')$. Subtracting their
real angular combinations gives precisely
\eqref{cdp:eq:C.TX.6} with $A'=\operatorname{Im}B'$.
Thus the determinant is $(\det P)^2$ times
\eqref{cdp:eq:C.WF.18}, where
$\operatorname{Im}B'=S+aJ$, $r=|s|^k$,
$x=\operatorname{Re}(s^k)$ and $y=-\log|s|/(2\pi)$.
The factor $(\det P)^2$ is positive, and restoring the finite
angular enlargement $\Lambda\subset\Lambda_0$ preserves rank.
''','D12,D19,D20','cdp:st:C.2.UN.76','The exact real-basis transport identifies the period matrix with UN73 TX6; retain WF18/tag016E at the single TX7 owner, including the fixed positive determinant factor.')
pkg.guard('UN73-period-determinant-alias',old_tx7,new_tx7,'Bounded equation alias and section numbering only. The complete current and receiving UN73 proof has been read; the full real determinant proof stays here and UN76 gives its exact basis map.')
(OUT/'S6_SERIES_PUBLISH_II_sec11_roots_UN73_input.tex').write_text(old73+'\n',newline='\n')
(OUT/'S6_SERIES_PUBLISH_II_sec11_roots_UN73_receiving.tex').write_text(old73.replace(old_tx7,new_tx7,1)+'\n',newline='\n')

pkg.record('D20','prop:II:cyclic-root-normalization',r'Curve centres C_\alpha and finite component covers C_\alpha',r'Curve centres B_\beta; finite component covers C_\alpha','Rename only the smooth centres in the finite blowup list: B_beta is the curve formerly called C_alpha in Delta_pi. The original normalized root covers keep their original notation; every Euler term is unchanged.')

def edits(text,owner,changes):
    for old,new,kinds,reason in changes:
        text=pkg.edit(text,old,new,kinds,owner,reason)
    return text

p342=edits(p342,'prop:II:cyclic-root-normalization',[
 (r'''Each step is the normalized blowup
of its actual monomial ideal.''',r'''To describe one step, write the ray in a simplicial cone
as $v=\sum_i c_i v_i$, with $c_i\ge0$, and let $\ell_i$
be the rational dual basis to its primitive generators $v_i$.
Choose $L>0$ such that every $L\ell_i/c_i$ with $c_i>0$
is an integral character. Blow up the monomial ideal
$(\chi^{L\ell_i/c_i}:c_i>0)$ and normalize.
Its $i$-th chart adjoins all ratios
$\chi^{L\ell_j/c_j}/\chi^{L\ell_i/c_i}$ and then saturates
the character semigroup. Its cone is the region
$\langle\ell_i,w\rangle/c_i\le\langle\ell_j,w\rangle/c_j$
for all $j$ with $c_j>0$, namely the cone spanned by $v$
and the old rays other than $v_i$. These are exactly the
star-subdivision charts and their coarsening maps.''','D20','Give the exact ideal, saturated chart algebras and valuation inequalities realizing each chosen star subdivision.'),
 (r'''those transitions have not been
replaced by constant torus maps.''',r'''the maps use those same holomorphic transition units.''','D02','State the unit-dependent gluing maps positively.'),
 (r'''None has Hopf minimal
model.''',r'''Their minimal models are ruled or rational.''','D08','Use the already proved surface types in the conclusion.'),
 (r'''is holomorphic and generates the
canonical direct image on the reduced
semistable family. Its component
orders have minimum zero.''',r'''is holomorphic and has minimum component order zero.
By \cref{cdp:st:C.2.UN.17}, the canonical direct image of
this proper torus family is free of rank one. Relative to
its frame the displayed form is a holomorphic base function.
A zero of that function at the origin would add at least one
to every component order, since the full central fibre is
reduced. The coefficient is therefore a unit, proving that
$\Omega_Z$ is a generator.''','D20,D25','Give the exact reduced-fibre base-coefficient argument for primitivity rather than leave the generator assertion implicit.'),
 (r'''The invariants
of its total ring of fractions are
$\operatorname{Frac}(A)$.''',r'''Put $K=\operatorname{Frac}(A)$. The total fraction algebra
is $K[s]/(s^N-f\pi)$; it is reduced and has basis
$1,s,\ldots,s^{N-1}$, on which $G$ acts with the distinct
characters $1,\zeta,\ldots,\zeta^{N-1}$. Its invariant
subalgebra is therefore exactly $K$.''','D20','The eigenbasis gives the exact invariant map even when the local normalization has split branches.'),
 (r'''This argument applies to the
normalization on the connected
total space; the local split
branches are permuted by $G$
and give the same invariant
ring equality.''',r'''The same fraction algebra includes every local split branch;
the group permutes them, and the displayed invariant equality
is the local finite-quotient map.''','D02,D08','State directly how split normalization branches enter the quotient proof.'),
 (r'''an
\emph{actual} finite etale cover''',r'''a finite etale cover''','D08','Remove process emphasis while retaining the finite cover and degree.'),
 (r'''This proves the formula and
integrality of $\nu_I$ without
a choice of triangulation.''',r'''This determinant computes $\nu_I$ for every unimodular
triangulation and proves its integrality.''','D02','State the triangulation independence through the proved determinant.'),
 (r'''No global meromorphic frame for
that normal line is chosen.''',r'''The local Cartier frames and their displayed cocycle define
this cover globally.''','D02','Express the frame-free construction by its actual cocycle.'),
 (r'''Such
root components cannot have
Hopf minimal model.''',r'''Their minimal models are projective, whereas a Hopf surface
has odd first Betti number and hence is not K\"ahler;
the point-blowup invariance of $b_1$ in
\cref{lem:II:blowup-topology} excludes a Hopf minimal
model for these projective resolutions.''','D20','Give the precise birational and Betti obstruction behind the stated exceptional-cover exclusion.'),
 (r'''accounts for every Hopf root
component, with no exceptional
ones omitted.''',r'''accounts for every Hopf root component.''','D02','The preceding projective/ruled comparison proves exhaustiveness.'),
 (r'''Apply the preceding root
resolution and modification maps there,
retaining the actual identity comparisons
on its annulus and on the complement.''',r'''Apply the preceding root resolution near that fibre.
Its coarsening is an isomorphism off the fibre and glues
to the identity on the unchanged annulus and complement.''','D12,D14','The general owner constructs the root and its resolution only; later core modifications remain in their own consumers.')
])

new76=edits(new76,'cdp:st:C.2.UN.76',[
 (r'''The lifted \(g\) need not have order \(M\) on this developed
cover.  Instead it normalizes the actual period maps''',r'''The lifted $g$ normalizes the period maps''','D02','State the exact developed-cover relation g^M=g_gamma0 directly.'),
 (r'''curve of an old strict root component which dominates \(C\);
boundary curves supported over an original triple point
are not used here.''',r'''curve of an old strict root component which dominates $C$.''','D02','The domination condition specifies exactly which boundary curves enter the map.'),
 (r'''Choose \(k\ge1\) with \(\zeta^k=\det D\).''',r'''Since $(\det D)^M=1$, choose $k\ge1$ with
$\zeta^k=\det D$.''','D22','The determinant of D^M=I proves that the stated cyclic character and exponent exist.'),
 (r'''The exact original nonreduced fibre and its entire neighbourhood
are recovered by the original coarsening and quotient morphisms.
The compact occurrence assertion preserves the marked reduced
log support and multiplicity cycle; it does not identify an
arbitrary original higher infinitesimal thickening or full
degeneration germ with the new compact realization.''',r'''For the given family the coarsening and quotient morphisms
recover its nonreduced fibre and analytic neighbourhood.
For the compact realization the isomorphism of marked weighted
supports is the one of \cref{def:II:marked-weighted-toric-support}.''','D02,D11,D13','State both exact map scopes once using the complete numbered marking datum.'),
 (r'''The original support is already SNC. Its local coordinates and''',r'''Write $\rho_{\rm tot}=\rho\circ q:\widetilde X\to X$
for the composite finite-root and resolution map.
The original support is already SNC. Its local coordinates and''','D20,D25','Define the previously undeclared pullback map in WF7/WF8, identifying it exactly with the general q and rho arrows.'),
 (r'\rho^*\Omega',r'\rho_{\rm tot}^*\Omega','D20','Use the explicitly defined composite map on the smooth semistable root.'),
 (r'''is a nowhere-zero holomorphic three-form on \(\widetilde X\).''',r'''and is nowhere zero on $\widetilde X$.''','D23','Join the displayed primitive form to its preceding verb without a second ungrammatical is.'),
 (r'''\item  Notice the normalization of \eqref{cdp:eq:C.WF.1}.  In a weighted fibre it
is not necessary that some \(k_i\) be zero.  Positivity of
the \(k_i+1\) gives \(\lambda>0\).''',r'''\item Positivity of the $k_i+1$ in \eqref{cdp:eq:C.WF.1}
gives $\lambda>0$.''','D02,D11','Retain the weighted generator argument and its resulting ratio bound without an unneeded contrast.'),
 (r'''log atlas.  It is a central-log comparison; no conjugacy of
the arbitrary original whole germ has been asserted.''',r'''log atlas, with the component maps and normal-product sections
of \cref{def:II:marked-weighted-toric-support}.''','D02,D11','Identify exactly the marked central maps proved by the character calculation.'),
 (r'''SNC stratification now proves \eqref{cdp:eq:C.WF.3}.  This argument
uses the retained old cells, rather than the Euler number
of the subdivided root fibre.''',r'''SNC stratification proves \eqref{cdp:eq:C.WF.3} on the original
coarse cells.''','D02,D08','The proved stratum calculation directly states its support.'),
 (r'''images.  In particular no integral lattice is
replaced by the abstract standard lattice in this step.''',r'''images. Thus each integral subgroup is carried by that same
invertible real map, with its lattice inclusion preserved.''','D02,D20','State the exact basis transport positively.'),
 (r'''is kept outside.  No complex-linearity of \(V_s\)
is presumed.''',r'''is kept outside, as in the displayed period and action maps.''','D02','The explicit real-linear formulas retain the needed scalar placement.'),
 (r'''We check the local smoothness assertion rather than
inferring it from an abstract quotient.  At a point''',r'''At a point''','D02','Begin with the finite point-stabilizer and invariant chart calculation.'),
 (r'''neighbourhood of this point.  A stabilizer of a
lower-dimensional cone which moves points on its
torus stratum is not used as a point stabilizer.''',r'''neighbourhood of this point; the group in the calculation
consists exactly of the elements fixing that point.''','D02','Specify the stabilizer subgroup directly.'),
 (r'''change fixes \(s\).  Averaging has only been used for
this finite chart stabilizer, not for the developed
lift with \(g^M=g_{\gamma_0}\).''',r'''change fixes $s$. This averaging is over the finite point
stabilizer of order $d$ in the chart.''','D02','Retain the exact averaging group, whose finite order is the premise of the formula.'),
 (r'''The constructed compact family instead
uses the explicit variable period units
in \eqref{cdp:eq:C.WF.17}.  Their higher \(s\)-jets were
not identified with those of an arbitrary
original germ.  No such identification is
needed for the stated compact occurrence
of the marked reduced log support and
full multiplicity cycle.  This completes
all the asserted comparisons.''',r'''The compact family uses the variable period units in
\eqref{cdp:eq:C.WF.17}. At its two ends, the exponential maps,
base rescalings, torus inversion and invariant-chart maps above
give the asserted isomorphisms of marked weighted supports.''','D02,D08,D11','Conclude with the complete constructed maps and the exact marking scope already stated.'),
 (r'''nonreduced fibre by its actual invariant
analytic algebra, not just by a cycle.''',r'''nonreduced fibre by its invariant analytic algebra.''','D02','Keep the precise recovery algebra.'),
 (r'''Its finite action is the actual
\eqref{cdp:eq:C.WF.19}''',r'''Its finite action is \eqref{cdp:eq:C.WF.19}''','D08,D23','Remove a process adjective and ungrammatical article.')
])

new78=edits(new78,'cdp:st:C.2.UN.78',[
 (r'''In particular the inverse record is applied
\emph{before} the finite quotient. No quotient of
an undefined central birational action is used.''',r'''The inverse record first restores the regular action on $Z$;
the finite quotient is then taken on $Y_N$.''','D02','State the exact order of the maps positively.'),
 (r'''This gives complete finite generation for this
explicit resolution-and-root branch, without
an equivariant canonical-flat reduction assertion.''',r'''These maps give finite generation for the resolution-and-root
branch defined by \eqref{cdp:eq:C.RK.3}.''','D02,D11','Keep the full exact branch and its reconstruction maps without a repeated scope disclaimer.'),
 (r'''The original endpoint neighbourhood, not only
its central log space, is retained throughout.''',r'''The input includes the endpoint analytic neighbourhood and
all the transition maps in the inverse record.''','D02,D08','State the full analytic datum positively.'),
 (r'''record and an actual punctured
isomorphism.''',r'''record and a punctured isomorphism.''','D08,D23','Keep the actual comparison map with a grammatical article.'),
 (r'''gives exactly the character in
the preceding paragraph under
this birational action.''',r'''gives the character $\zeta^{-a_{\min}}$ from
\cref{prop:II:cyclic-root-normalization} under this birational
action.''','D04,D20','Replace a stale preceding-paragraph pointer by the exact moved character formula.')
])

p341=edits(p341,'def:II:finite-rooted-reconstruction',[
 (r'\item An actual proper smooth-total core family',r'\item A proper smooth-total core family','D08,D23','State the input family with a grammatical article.'),
 (r'''Thus it is an actual regular action of
\(G=\mu_N\) on \(Z\), not only a central action
or an action on its meromorphic function field.''',r'''These maps define a regular action of $G=\mu_N$ on $Z$.''','D02,D08','The stated holomorphic charts and cyclic composition laws are precisely the regular action datum.'),
 (r'''All quotient, contraction and overlap requirements here
are checks on the supplied finite maps. They do not
refer to the existence of an additional original family.''',r'''The quotient, contraction and overlap identities are
conditions on these finite maps and their coordinate algebras.''','D02,D08','State admissibility intrinsically in the supplied mathematical objects.')
])

new86=edits(new86,'cdp:st:C.2.UN.86',[
 (r'\eqref{cdp:eq:C.AR.2}--\eqref{cdp:eq:C.AR.3}',r'\eqref{cdp:eq:C.AR.2}','D04,D19','Both permanent labels are aliases of the single P342 display; cite its number once and preserve both targets at the owner.'),
 (r'''degeneration. Write the original full fibre and the
primitive generator as
Use the full original divisor and generator coefficients
in \eqref{cdp:eq:C.AR.6}.''',r'''degeneration. Use the full original divisor and primitive
generator coefficients in \eqref{cdp:eq:C.AR.6}.''','D12,D23','Complete the sentence after moving its coefficient display to the common owner.'),
 (r'''Their root $Z$ is connected, smooth and full reduced SNC,
and every map is an isomorphism off the selected fibre.''',r'''Their root $Z$ is connected and smooth, with full reduced
SNC central fibre. The maps $q$ and $\pi$ are isomorphisms
off their central fibres; $\rho$ there is the finite etale
base-change map induced by $t=s^N$.''','D20,D25','Distinguish the two modification isomorphisms from the degree-N finite base-change map by their exact arrows; no theorem domain changes.'),
 (r'''been retained. In particular the finite
quotient follows the inverse record; no
central quotient of an indeterminate
birational action is taken.''',r'''been included in the input. The inverse record restores
the regular action before its equivariant coarsening and
finite quotient.''','D02,D08','State the required reconstruction order through its exact arrows.'),
 (r'''Begin with the data at the start of the
subsection, independently of any original
\(X\).''',r'''Begin with \cref{def:II:finite-rooted-reconstruction}.''','D02,D04,D13','Use the complete numbered intrinsic input.'),
 (r'''chart checks give an actual regular finite
action.''',r'''chart identities give a regular finite action.''','D08,D23','Keep the holomorphic action verified by the stated identities.'),
 (r'''No uniqueness of the reduction record is
required for this exact generation statement.''',r'''The construction associates its output to the atlas and
commuting arrows of each such record.''','D02','State the proved generation map positively.'),
 (r'''For recovery of a different given
family, its actual endpoint atlas
and higher transverse terms remain
in the input. The proof uses its
specified overlap isomorphisms and
does not transfer a contraction
through an equality of central log
data alone. This states exactly
which parameters are classified
centrally and which analytic data
the reversible reconstruction retains.''',r'''For a given family, \cref{def:II:finite-rooted-reconstruction}
includes its endpoint atlas, all transverse terms and the
overlap isomorphisms used by the inverse arrows. The diagram
\eqref{cdp:eq:C.AR.13} recovers that analytic neighbourhood
and, for compact data, its global family.''','D02,D08,D11','Conclude with the exact input and inverse diagram already proved.')
])

for name,owner,inputs in [
 ('new76','cdp:st:C.2.UN.76',r'\cref{def:II:marked-weighted-toric-support,prop:II:cyclic-root-normalization,cdp:st:C.2.UN.68,cdp:st:C.2.UN.71,cdp:st:C.2.UN.73}'),
 ('new78','cdp:st:C.2.UN.78',r'\cref{prop:II:cyclic-root-normalization,cdp:st:C.2.UN.75,cdp:st:C.2.UN.39}'),
 ('new86','cdp:st:C.2.UN.86',r'\cref{def:II:finite-rooted-reconstruction,prop:II:cyclic-root-normalization,cdp:st:C.2.UN.75,cdp:st:C.2.UN.78,cdp:st:C.2.UN.84,cdp:st:C.2.UN.85,cdp:st:C.2.UN.57,cdp:st:C.2.UN.61,cdp:st:C.2.UN.63,cdp:st:C.2.UN.71,cdp:st:C.2.UN.73}')]:
    val=locals()[name]
    oldline=next(line for line in val.splitlines() if line.startswith(r'\StatementRecord'))
    tag=re.match(r'\\StatementRecord\{[^{}]+\}\{[^{}]+\}\{([^{}]+)\}',oldline).group(1)
    new_line=r'\StatementRecord{'+owner+r'}{proved}{'+tag+'}{'+inputs+'}'
    locals()[name]=pkg.edit(val,oldline,new_line,'D10,D12,D14',owner,'Keep the existing hidden dependency record and replace the moved/repeated internal equation list by the exact earlier owning statements.')

for textname,owner in [('p342','prop:II:cyclic-root-normalization'),('new76','cdp:st:C.2.UN.76'),('new78','cdp:st:C.2.UN.78'),('new86','cdp:st:C.2.UN.86'),('p341','def:II:finite-rooted-reconstruction')]:
    val=locals()[textname]
    def current_ref(m):
        old=m.group(0); new=r'\cref{'+m.group(1)+'}'
        pkg.record('D04',owner,old,new,'Use the current statement kind and number while preserving the permanent label.')
        return new
    val=re.sub(r'\\ref\{(cdp:st:[^{}]+)\}',current_ref,val)
    locals()[textname]=val

