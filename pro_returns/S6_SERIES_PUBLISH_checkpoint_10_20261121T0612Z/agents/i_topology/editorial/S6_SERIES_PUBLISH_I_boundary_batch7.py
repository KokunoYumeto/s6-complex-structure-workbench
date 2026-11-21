from pathlib import Path
import json,hashlib,datetime,re,csv
base=Path('/workspace/scratch/653608133b22');o=base/'work/agents/i_topology';p=base/'work/S6_SERIES_PUBLISH_I.tex';source=p.read_text();s=source;patches=[];changed=set()
def add(old,new,reason,ids):
 global s
 assert s.count(old)==1,(len(patches)+1,'guard count',s.count(old),old[:120])
 patches.append({'id':f'I-topology7-{len(patches)+1:02}','old':old,'new':new,'reason':reason,'statement_ids':ids});s=s.replace(old,new,1);changed.update(ids)
def span(key):
 i=s.index('\\label{'+key+'}');a=s.rfind('\\begin{',0,i);b=s.index('\\end{proof}',i)+len('\\end{proof}');return a,b
def sub(key,old,new,reason='Replace process wording by the exact proved scope; retain all mathematical maps and hypotheses.'):
 a,b=span(key);block=s[a:b]
 if block.count(old)!=1:
  pattern=''.join(r'\s+' if part.isspace() else re.escape(part) for part in re.split(r'(\s+)',old) if part)
  matches=list(re.finditer(pattern,block));assert len(matches)==1,(key,old[:100],len(matches))
  old=matches[0].group(0)
 if s.count(old)==1:add(old,new,reason,[key])
 else:add(block,block.replace(old,new,1),reason,[key])
def item(key,marker,new=''):
 a,b=span(key);pos=s.index(marker,a,b);start=s.rfind('\\item',a,pos);end=s.find('\n\\item',pos,b)
 if end<0:end=s.index('\\end{enumerate}',pos,b)
 old=s[start:end];add(old,new,'Remove a program/report-only proof step, or retain its unique finite input/method/result without a program path.',[key])
def delete(key,old):sub(key,old,'')
# Full fan and central-space proofs were read before these rewrites.
sub('push:src:A.2.4','[exhaustive finite fan data]','[Exhaustive finite fan data]','Capitalize the statement title.')
sub('push:src:A.2.4',r'''\item The program \path{code/ab_push_all_refinements.py} enumerates
all candidate rays for $n=1,2,12$ through $H=3$, and all
four-column determinant tests at the bounds reported here:''',r'''\item Enumerating the primitive rays in (A.24a) and retaining the
four-element subsets whose column determinants have absolute value one
gives the following finite counts:''','Retain the exact enumeration inputs, determinant test and result table; move the program citation to the end-table.')
sub('push:src:A.2.4',r'''These are candidate counts, not a claim that every candidate
four-subset or collection passes the other tests. At height
one, the complete collections are the two and $n+1$ fans
already proved in \ref{push:src:A.2.1} and \ref{push:src:B.2.1}. The saved program also
certifies the first eight members of the explicit infinite
family in \ref{push:src:A.2.1}.''',r'''The table counts rays and unimodular four-subsets. The common-face,
volume and boundary tests above select the complete collections.
At height one these are the two and $n+1$ fans of
\cref{push:src:A.2.1,push:src:B.2.1}, respectively.''','Preserve the bounded candidate count and the complete height-one classification; the earlier proof already establishes the infinite family.')
sub('push:src:A.4.2',r'''Thus the
nonzero Smith factors are five ones and eleven. The fully
integral check uses an explicit $E_8$ basis in
\texttt{ab\_push\_monodromy.py}; its output records the
kernel basis, quotient projection, and all entries of the
seven-by-seven monodromy block. This supplies a second,
exact lattice verification of the discriminant argument.''',r'''Thus the nonzero Smith factors are five ones and eleven.''','The integral discriminant proof remains complete; the second program verification is recorded in the end-table/check file.')
sub('push:src:A.4.6','[an infinite explicit subclass]','[An infinite explicit subclass]','Capitalize the title.')
delete('push:src:A.4.6',r''' The exact saved
certificates check all determinants, boundary faces,
slice volumes and these integer formulas for $0\leq m\leq8$;
the displayed induction proves them for every $m$.''')
item('push:src:A.4.7','The program \\path{code/ab_push_all_fan_topology.py}',r'''\item For the nonreduced conductor-star family with added pure top
rays $(0,1,0,j)$, $2\leq j\leq m+1$, the pure-top ray-orbit count increases by $m$
and the maximal-cone-orbit count increases by $m$. The formula therefore gives
$\chi(D_m)=14+12m$. Equivalently, each conductor blow-up adds the Euler
number $12$ of its centre.
''')
sub('push:src:A.4.8','[integral homology of every toroidal output]','[Integral homology of every toroidal output]','Capitalize the title.')
item('push:src:A.4.8','The exact program \\path{code/ab_push_all_fan_homology.py}')
sub('push:src:A.4.9','[a second integral central-space computation]','[Integral cohomology under central blowups]','Title the unique sheaf splitting rather than its verification role.')
item('push:src:A.4.9','The program \\path{code/ab_push_central_pushforward.py}')
# Coherent cohomology and Hopf models.
sub('push:src:B.4.5',r'''\item We give a degree-one argument directly on $D$; no nearby
Hodge-de Rham degeneration theorem is needed. Let''',r'''\item Let''')
delete('push:src:B.4.5',r'''The finite simplex and permutation identities for the at most
four branches in our threefold application are checked exactly
in \path{code/b_nc_degree_one.py}.
''')
sub('push:src:B.4.5',r'''This proves
exactness for analytic functions, not just for formal series.''',r'''This proves exactness in the convergent analytic local rings.''')
sub('push:src:B.4.5',r'''This proves surjectivity. Notice that no
$\partial\bar\partial$ hypothesis on $D^{[1]}$ or higher
branch spaces was used; compactness suffices for the only
function argument there.''',r'''This proves surjectivity. The argument on $D^{[1]}$ uses its
compactness through the constancy of pluriharmonic functions.''')
delete('push:src:B.4.6',r'''
This excludes the stated cap construction even when
an invariant Kato surface in an overlap kills a
fundamental-group generator of a Kato component.
It is not a classification of arbitrary analytic
cusp components or of their possible overlaps.
''')
sub('push:src:B.4.6',r'''The obstruction uses the cohomology maps
on the overlaps; it does not assume that every
Kato component's loop survives in the union.''',r'''The obstruction is the stated surjectivity comparison on the blocks
and injectivity comparison on their pairwise overlaps.''')
sub('push:src:B.4.7','[A parabolic analytic model and its comparison failure]','[A Hopf surface degeneration and its comparison map]','Describe the proved degeneration and comparison map.')
sub('push:src:B.4.7',r'''Consequently $\mathcal H\times\PP^1\to\Delta$ is an actual
semistable family of compact threefolds''',r'''Consequently $\mathcal H\times\PP^1\to\Delta$ is a
semistable family of compact threefolds''')
sub('push:src:B.4.7',r'''zero and fundamental group $\Z$.  It is not a filling of the
six-sphere family.''',r'''zero and fundamental group $\Z$.''')
sub('push:src:B.4.7',r'''The construction
gives an actual holomorphic product $H_-\times\Delta^*$,
not merely an isotrivial set of fibres.''',r'''The cocycle coboundary therefore gives a holomorphic product
isomorphism with $H_-\times\Delta^*$.''')
sub('push:src:B.4.7',r'''These explicit invariants prevent this example
from being mistaken for a filling of $S^6$.''',r'''The resulting fundamental group and Euler number are the stated
invariants of these smooth fibres.''')
# Exact ordinary torsor/class maps and primary locators.
sub('push:src:B.4.9',r'''Changing only these transition
units cannot repair the component permutations
$+4,-3,0$ refuted in \ref{push:src:B.3.1}.
This is not a classification of all torus-torsor
descent.  In fact, for the sheaf $\mathscr T$ of''',r'''These transition units preserve the component permutations
$+4,-3,0$ of \ref{push:src:B.3.1}. For the sheaf $\mathscr T$ of''')
sub('push:src:B.4.9',r'''Thus nonzero classes in this
$\Z^2$ do not have its prescribed marked punctured
cusp germ.  No compactification of an arbitrary
torsor is asserted.''',r'''A marked torsor isomorphism preserves this cohomology class, so a
torsor with a nonzero class cannot be isomorphic to this marked cusp
torsor.''')
sub('push:src:B.4.9',r'''\item To exhibit the scope left outside that calculation,
retract $U$ to its real two-torus.''',r'''\item Retract $U$ to its real two-torus.''')
delete('push:src:B.4.9',r'''The exact matrix and Smith calculation is saved
in \path{code/ab_push_hopf_winding.py}.
''')
sub('push:src:B.4.9',r'''These classes do define holomorphic torsors by
translation gluing, but this calculation contains
no compactness assertion at either missing axis.''',r'''The representatives of $H^1(U,\mathscr T)$ give holomorphic torsors
on $U$ by translation gluing.''')
delete('push:src:B.4.9',r'''  A holomorphic trivializing
gauge over $U$ need not extend at the missing
axes.  The proof thus neither identifies
arbitrary descent data with monomial cocycles
nor asserts a meromorphic comparison of
arbitrary analytic fillings.''')
sub('push:src:B.4.9',r'''The quadratic
dependence on $c=-(12/(2\pi i))\log r$ is retained:
it supplies no extension across $r=0$ and no
global comparison with the finite-place models.''',r'''The displayed comparison is defined on the full $q$ disc for
$r\ne0$, with $c=-(12/(2\pi i))\log r$ on its parameter cover.''')
delete('push:src:B.4.9',r'''The explicit polynomial identity is checked in
\path{code/ab_push_hopf_winding.py}.
''')
# Keep precise normal/Cartier maps; remove repetitive scope prose.
sub('push:src:B.4.10',r'''Here $n[-s]$ is the weighted total exceptional correction, not the
intersection with the reduced final exceptional locus.''',r'''Here $n[-s]$ is the total exceptional correction, with the
multiplicity of each successive blow-up retained.''')
sub('push:src:B.4.10',r'''It is an auxiliary construction and first-order
matching result. No attachment to the prescribed punctured
$S^6$ family, compact third component, or global smoothing is asserted.''',r'''The matching is the displayed isomorphism of the two normal lines,
with the stated triple-curve factor.''')
delete('push:src:B.4.10',r''' These are invariants
of the auxiliary surface, not of a proposed $S^6$ central fibre.''')
sub('push:src:B.4.10',r'''Adding a vertical elliptic component does not help: remove that
Cartier component, and the remaining proper horizontal divisor of''',r'''After removing a vertical Cartier elliptic component, an extending
divisor would still have a proper horizontal part of''')
sub('push:src:B.4.10',r'''Drifting translations cannot
remove both requirements. The present Kato family escapes exactly
because $D_{\rm exc}=n[-s]$ has no such extension.''',r'''In this Kato family the correction is exactly $D_{\rm exc}=n[-s]$,
whose nonextension was proved above.''')
sub('push:src:B.4.10',r'''Thus no effective triple divisor
repairs that particular bare interface.''',r'''Thus the required triple-divisor line has no effective section
on this interface.''')
delete('push:src:B.4.11',r'''
This concerns globalization of a specified local deformation of
an auxiliary compact surface.  It does not assert an attachment to
the punctured $S^6$ family or a compactification of the resulting
threefold over the open parameter disc.
''')
sub('push:src:B.4.11',r'''\item We first retain the analytic neighbourhood, not merely its normal
line.''',r'''\item We first identify the analytic neighbourhood.''')
sub('push:src:B.4.11',r'''\item We spell out the local-to-global criterion used in the final
step, since the rational-cycle contraction theorem does not
apply to this elliptic contraction.''',r'''\item The local-to-global lifting criterion follows from the
following explicit obstruction calculation.''')
sub('push:src:B.4.12',r'''Here $C$ is a proper family over an open disc and is not a compact
threefold.  This assertion supplies the indicated surface smoothing
and normal-line products only.  It does not construct a compact
three-component central fibre, a compatible global smoothing of
such a fibre, or a comparison with the prescribed punctured
$S^6$ family.''',r'''Here $C$ is the constructed proper surface family over an open
disc. Its continuous surjection onto that disc proves that $C$ is
noncompact.''')
sub('push:src:B.4.12',r'''These are pairwise line-bundle identities.  They do not supply
a compact third component or a compatible global smoothing
section for a compact normal-crossings threefold.
In fact the third space constructed here maps surjectively and
properly to an open disc, so it cannot itself be compact.''',r'''The three displayed evaluation maps are the required pairwise
normal-line trivializations. The third space maps surjectively and
properly to an open disc, which proves its noncompactness.''')
sub('push:src:B.4.12',r'''\item For a useful topological check on the local model,
the affine smooth fibre $Q\setminus E$ has''',r'''\item The affine smooth fibre $Q\setminus E$ has''')
sub('push:src:B.4.12',r'''In particular no simply connected local Milnor fibre is being
assumed.  The compact noncentral surface has Euler number
$\chi(S)+\chi(Q)-2\chi(E)=8+4=12$ by the local
$\xi z=t$ retraction, not the Euler number of an $S^6$ fibre.
Exact polynomial, Hilbert-function, normal-product and Smith-form
checks appear in \texttt{code/root\_quadric\_smoothing.py}.''',r'''The compact noncentral surface has Euler number
$\chi(S)+\chi(Q)-2\chi(E)=8+4=12$ by the local $\xi z=t$ retraction.''')
sub('push:src:B.4.13','[The second period does not lift to a finite marked Hopf modification]','[The obstruction to a marked period lift]','Title the exact proved obstruction.')
sub('push:src:B.4.13',r'''It concerns a holomorphic period action on
these full modifications. It does not exclude a meromorphic
correspondence, a different connected unfolding made from
noncompact pieces, or a cap present only over the central parameter.''',r'''The period action in these assertions is a holomorphic action on
the full finite modifications with the specified marked core.''')
sub('push:src:B.4.13','direct attempt\nto lift','extension\nof')
# The entire sixth item is a report/scope paragraph; the geometric singular locus and cohomology are already in the statement/proof.
item('push:src:B.4.14','The singular locus here is not isolated')
sub('push:src:B.4.15',r'''This is a statement about a proper model over a bidisc,
flat over the degeneration parameter. It does not assert
joint flatness over the bidisc, a one-parameter degeneration
of compact surfaces with Hopf components, or a global
$S^6$ filling. All twelve component labels, and hence the
obstruction of \ref{push:src:B.3.1}, are unchanged.''',r'''The map is proper over the bidisc and flat over the degeneration
parameter. Its vertical threefolds have the dimensions stated above.
All twelve component labels, and hence the obstruction of
\ref{push:src:B.3.1}, are unchanged.''')
sub('push:src:B.4.16','[Scope of the insertion operations]','[The dual complex under local insertions]','Title the invariant proved by the statement.')
delete('push:src:B.4.16',r'''This statement concerns the specified generated class
of operations. It makes no assertion that arbitrary
analytic caps or arbitrary changes of the punctured
comparison belong to that class.
''')
item('push:src:B.4.16','The finite incidence and collapse certificates themselves',r'''\item For the twelve-cycle, use the oriented edge-to-vertex and
triangle-to-edge incidence maps of the triangulated cylinder in Step~1.
Their chain ranks are $24,48,24$, and their nonzero Smith entries are
$1^{23}$ and $1^{24}$, respectively. Hence its integral homology is
$(\Z,\Z,0)$. The explicit retraction pulls the integral angular cocycle
back with winding one.
''')
sub('push:src:B.4.18',r'''The overlap is an explicit holomorphic translation,
including the retained affine marking. This proposition
does not assert a proper completion over the missing
origin, nor the global finite-place overlap maps.''',r'''The overlap is the displayed holomorphic translation with its
affine marking on the two specified base opens.''')
sub('push:src:B.4.18',r'''The second difference is a period, not zero; that is
exactly what is needed for descent to the torus.''',r'''The second difference is the displayed integral period, so the
translation descends to the torus.''')
sub('push:src:B.4.18',r'''Thus
properness and proper discontinuity are supplied
by the compact core and collars, not inferred
from determinants alone.''',r'''The compact core and collars therefore prove properness and
proper discontinuity.''')
sub('push:src:B.4.18',r'''This is exactly the
limitation established in \ref{push:src:B.3.3}. We do not identify
this full $q$-boundary with the prescribed cusp.''',r'''This is the $q$-multiplicity computed in \ref{push:src:B.3.3}.''')
item('push:src:B.4.18','The exact symbolic differences, finite norm')
# Global partial family and Kato collars: retain the exact domains and all maps.
item('push:src:B.4.19','The exact scalar, finite-root, cusp and node-chart')
sub('push:src:B.4.19',r'''The sole missing base point
is $(\infty,0)$. This proposition constructs only the
partial family: \ref{push:src:B.4.30} proves its noncompletion, and''',r'''The sole missing base point is $(\infty,0)$.
Theorem~\ref{push:src:B.4.30} proves its noncompletion, and''')
sub('push:src:B.4.19',r'''All identities
retain the actual punctured marking; there is no
unresolved scalar or translation cocycle.''',r'''The identities give the exact scalar and translation cocycles
with the prescribed punctured marking.''')
sub('push:src:B.4.19',r'''At $r=0$ the
base omits $\infty$; properness over the full
parameter disc does not follow and is not claimed.''',r'''At $r=0$ the target is the finite base $\mathbb P^1\setminus\{\infty\}$,
as specified in $\Omega$.''')
sub('push:src:B.4.20',r'''This is an embedded Cartier and normal-line comparison,
not an identification of relative tubular neighbourhoods.
No lift of the whole second period, attachment to the
global partial filling, or origin completion is asserted.''',r'''The comparison identifies the embedded Cartier divisor and its
normal line. At each central node the ambient base map has the local
form $s=uv-h$ computed below.''')
sub('push:src:B.4.20',r'''This is a literal local
singularity distinction, not only a possible
global obstruction to linearization.''',r'''An isomorphism over the base would identify the critical loci of
the two base maps, contradicting these explicit differentials.''')
sub('push:src:B.4.20',r'''Thus this local plumbing changes
the behaviour at the Tate node; (\ref{push:src:B.4.20}.3) by
itself does not identify the prescribed two-period
Mumford cusp. This auxiliary proposition supplies neither
global plumbing data nor that period comparison. \ref{push:src:B.4.33}
subsequently excludes any proper filling of the actual family.''',r'''Thus the map to $s$ on this local nonzero-$r$ fibre is a submersion
at the displayed locus.''')
item('push:src:B.4.20','The Cartier factor, Tate multiplier, reduced')
sub('push:src:B.4.21',r'''The construction supplies an actual linear collar with this
marking.  It does not extend the whole second period, construct
an origin cap for \ref{push:src:B.4.19}, or identify the modified Kato family
with the prescribed torus family. Such a proper filling of
the actual family is excluded by \ref{push:src:B.4.33}; the present
statement retains its auxiliary embedded-collar scope.''',r'''The displayed function $H$ and the closing factors specify the
linear-collar isomorphism on a neighbourhood of $\mathcal D^*$.''')
delete('push:src:B.4.21',r'''We do not assert that the modified ambient map is a submersion
at $s=0$.
''')
item('push:src:B.4.21','The exact exponents, intersection vector, blow-up count')
sub('push:src:B.4.22',r'''This is a local statement and does not identify its
global smooth fibres with the prescribed tori.
''','')
sub('push:src:B.4.22',r'''has multiplicity $n$. No descent removing that multiplicity
is asserted.''',r'''has multiplicity $n$.''')
item('push:src:B.4.22','This local equation and its resolution do not')
item('push:src:B.4.22','The full period action is a separate condition.',r'''\item The first collar action is $H\mapsto aH$, $f\mapsto a^{-1}f$,
which fixes $r=fH$. The function $G(q,H)$ of \ref{push:src:B.4.21}
conjugates this action on its stated small collar. For fixed $q$,
the product converges locally uniformly for $H\in\C$, because
$\sum_j|a(q)^jH|$ does so on compact sets. At $H=-a^{-j}$ it
vanishes, and the coordinate change $Z=xG(q,H)$ has zero derivative
in $x$. For $b\in\C^*$, on the open set where $r\ne0$, $f\ne0$ and
$W=1+r/f\notin\{1,b^{-1}\}$, the map $f=r/(W-1)$ conjugates
multiplication $W\mapsto bW$ to the rational map
\[
 f\longmapsto\frac{rf}{(b-1)f+br}.
\]
Indeed substituting $b(1+r/f)$ into $r/(W-1)$ gives the displayed
formula. This is the exact coordinate comparison for the test variable $W$.
''')
sub('push:src:B.4.23',r'''The conclusion applies to the
whole complementary Kato component with these hypotheses;
it makes no assertion about a different central component,
a curve meeting the conductor, or a replacement changing
the holomorphic base map.''',r'''The conclusion uses the specified complementary Kato component,
its conductor-disjoint curve and the displayed holomorphic base map.''')
sub('push:src:B.4.23','the repaired degree-one','the modified degree-one')
sub('push:src:B.4.23','the directly opened\n\\citet','\\citet')
sub('push:src:B.4.23',r'''The normal sequence need no longer supply the $r$ direction
in (\ref{push:src:B.4.23}.2). The proposition therefore does not exclude
such a changed central arrangement; its proper construction
and comparison with the prescribed family remain separate
requirements.''',r'''At the conductor intersection $dr$ vanishes on the normal fibre
of $C$, so $(dQ,dr)$ is not the bundle epimorphism of
(\ref{push:src:B.4.23}.2). This computes precisely where that
normal-sequence argument uses the conductor-disjoint hypothesis.''')
sub('push:src:B.4.25',r'''This concerns that specified auxiliary
Hopf family. It is not a nonexistence theorem for a
completion of the actual two-torus family in \ref{push:src:B.4.19}.''',r'''The conclusion applies to the indicated Hopf family with its two
specified multipliers.''')
sub('push:src:B.4.25',r'''This argument uses coherence and a direct exact
sequence; it does not use the corrected closedness
assertion discussed in the Grauert source audit.''',r'''The displayed coherent direct-image exact sequence proves the
required local constancy on the punctured disc.''')
sub('push:src:B.4.26',r'''The conclusion still permits the vertical threefold
components allowed in B.4. It is not an assertion that
an arbitrary $r$-proper filling initially has a holomorphic
extension of $q$; if $q$ is only meromorphic, a graph
modification must first be supplied and its resulting
geometry retained. \ref{push:src:B.4.30} subsequently excludes even
the permitted vertical-component completions of the
fixed partial family, and \ref{push:src:B.4.33} excludes every proper
filling of the actual global family.''',r'''The stated map to the bidisc includes a holomorphic extension of
$q$. Theorem~\ref{push:src:B.4.30} excludes completions of this fixed
partial family, including the displayed vertical-component geometry;
Theorem~\ref{push:src:B.4.33} excludes proper fillings of the global family.''')
sub('push:src:B.4.28',r'''and
\emph{assume in addition} that $\omega_D\simeq\OO_D$.''',r'''and that $\omega_D\simeq\OO_D$.''')
sub('push:src:B.4.28',r'''No K\"ahler hypothesis on $\mathcal X$ is used. The
additional triviality of $\omega_D$ is not inferred from
the neighbouring two-tori. The proposition does not
produce a modification with this property from an
arbitrary analytic completion.''',r'''The trivialization of $\omega_D$ in the hypotheses is the central
section used in the residue and nearby-period arguments below.''')
# Current primary-page locators. These are citation changes, not new proof checks.
for key in ['push:src:B.4.9','push:src:B.4.15']:
 a,b=span(key);block=s[a:b]
 old=r'\citep[Definition 1.1]{Fujimoto1990AB}'
 if old in block:
  add(block,block.replace(old,r'\citep[construction, p.~85; Definition~1.1, p.~86]{Fujimoto1990AB}'),'Authenticate the precise primary construction/definition pages.',[key])
 a,b=span(key);block=s[a:b]
 changes={r'\citet[Definition~1.1]{Fujimoto1990AB}':r'\citet[construction, p.~85; Definition~1.1, p.~86]{Fujimoto1990AB}',r'\citep[Section 5]{Cartan1952B_AB}':r'\citep[expos\'e~19, \S5, pp.~14--15]{Cartan1952B_AB}',r'\citep{Cartan1952B_AB}':r'\citep[expos\'e~19, \S5, pp.~14--15]{Cartan1952B_AB}'}
 new=block
 for old,rep in changes.items():new=new.replace(old,rep)
 if new!=block:add(block,new,'Insert the actually viewed Cartan/Fujimoto primary locators.',[key])
# Mathematical status of the external label: replace source navigation by exact theorem citation and local transport.
old=r'''identification are \cref{fam:src:C.2.3}, \cref{fam:src:A.5.1}; the latter is also Theorem~1.4
(label \texttt{p2:thm:exact-period}) of
\cite{DuGuoKusakabeXie2026v1}. Its hypotheses specify precisely the
retained period family, affine finite twists and cusp collar. They
coincide with the marked family $X_c$; the normalization differs
only by the fixed choice of the particular solution, which does not
alter parameter differences. Version 2 drops that theorem; we infer
no mathematical conclusion from this omission.'''
new=r'''identification are \cref{fam:src:C.2.3,fam:src:A.5.1}.
The exact-period classification is
\cite[Theorem~1.4, p.~3]{DuGuoKusakabeXie2026v1}; the constant
translation between its particular period solution and the present
one is the explicit parameter transport of \cref{fam:src:A.5.1}.'''
if old in s:
 add(old,new,'Replace an external source label/process sentence by the exact primary theorem and the proved local parameter-transport map.',['push:src:D.4.3'])
else:
 assert '(label \\texttt{p2:thm:exact-period})' not in s
 print('D4.3 external label already replaced by root/provenance exact parameter map; no guard/event here.')

# Complete the exact primary locators and the positive bundle scope.
sub('push:src:B.4.14','[Tangent weights and the compact-bundle obstruction reduction]','[Tangent representations and associated bundles]','Title the representations and associated bundle calculation.')
sub('push:src:B.4.14',r"""These are cohomological reductions.  They do not, by themselves,
globalize a prescribed deformation along the nonisolated
singular section of $Z_L$ or construct a compact third component.""",r"""The singular locus of the associated bundle is the section induced
by the cone vertex of $Y$; the displayed groups are the relative
tangent cohomology and its specified fibre twist.""")
a,b=span('push:src:B.4.14');block=s[a:b];new=block.replace(r'\citet[Section~2, equations~(1)--(8)]{Fujiki2009D}',r'\citet[Section~2, equations~(1)--(8), p.~4]{Fujiki2009D}').replace(r'\citet[Theorem~1.1]{Fujiki2009D}',r'\citet[Theorem~1.1, pp.~1--2]{Fujiki2009D}')
add(block,new,'Use actually viewed Fujiki v1 pages for the toric action and automorphism statement.',['push:src:B.4.14'])
i=s.index('\\label{I:elliptic-bundle-primary-comparisons}');a=s.rfind('\\begin{remark}',0,i);b=s.index('\\end{remark}',i)+len('\\end{remark}');block=s[a:b]
new=block.replace('Proposition~1.14 and Example~1.15, pp.~93--94','Proposition~1.14, pp.~92--93; Example~1.15, pp.~93--94').replace('Proposition~1.14, p.~93,','Proposition~1.14, pp.~92--93,').replace('Definition~1.1, pp.~85--86','construction, p.~85; Definition~1.1, p.~86')
add(block,new,'Correct the primary Proposition1.14 locator to include its statement start on p92; retain Example1.15 scope.',['I:elliptic-bundle-primary-comparisons'])

# Validate all stable anchors across the entire preview.
anchors=lambda t:sorted(re.findall(r'\\(?:label|hypertarget)\{([^}]+)\}',t))
assert anchors(s)==anchors(source),'lost anchors'
record={'input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'patches':patches}
(o/'editorial/S6_SERIES_PUBLISH_I_boundary_batch7_guarded.json').write_text(json.dumps(record,indent=2)+'\n')
(o/'editorial/S6_SERIES_PUBLISH_I_boundary_batch7_before.tex').write_text(source)
(o/'editorial/S6_SERIES_PUBLISH_I_boundary_batch7_preview.tex').write_text(s)
(o/'editorial/S6_SERIES_PUBLISH_I_boundary_batch7_changed_ids.json').write_text(json.dumps(sorted(changed),indent=2)+'\n')
print('PATCHES',len(patches),'CHAR_DELTA',len(s)-len(source),'CHANGED',len(changed),'ANCHORS_PRESERVED')
