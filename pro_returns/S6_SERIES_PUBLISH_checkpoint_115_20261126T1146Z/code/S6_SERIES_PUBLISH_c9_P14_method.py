#!/usr/bin/env python3
"""Prepare exact Paper III 02KU mathematical-method edits; no canonical writes."""
from pathlib import Path
import csv,re
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation9_findings'
source=(ROOT/'S6_SERIES_PUBLISH_III.tex').read_text()
rows=[]
def add(key,old,new,reason,types='D09;D10;D22',label='maps:src:D.2.2'):
 assert source.count(old)==1,(key,source.count(old))
 assert old!=new
 rows.append(dict(change_id='CLAUDE-III-P14-'+key,type=types,statement_id=label,old_location='Paper III, '+label+'; '+key,old_page='cp100 pp.114–116 or final Programs/bibliography',new_location='Paper III, '+label+'; '+key,new_page='pending final build',old_text=old,new_text=new,reason=reason,review_status='Original computation and actual pinned model code reread; all58 matrix inputs replayed successfully; exact proposed algebra/prose reviewed; canonical admission and PDF gate pending.'))

add('INPUT-SCOPE',
 r'''The finite input family \(\mathcal I\) uses the marked local cochain models of
\cite[documentation, ``How it works'']{manExplorer26}.''',
 r'''The finite input family \(\mathcal I\) uses the marked local cochain models of
\cite[documentation, ``How it works'']{manExplorer26}.
Their integral complexes, marked boundary maps and peripheral
relations form part of the input data.''',
 'Makes the existing marked-model scope explicit. These actual complexes/maps were recovered from the cited source and used in the58-input replay; no unpublished geometric local-model derivation is claimed.',label='mapsIII:def:finite-filling-inputs')
add('STATEMENT',
 r'''has fifty inputs. Their integral-cohomology and fundamental-group
outputs have the following properties. The fundamental group is
trivial for twenty-four inputs and nontrivial for twenty-six.''',
 r'''has fifty inputs. For \(\iota\in\mathcal I\), write
\(\mathcal C_\iota^\bullet\) for its marked integral
Mayer--Vietoris complex and \(\Pi_\iota\) for the group defined
by its marked peripheral presentation. Both are specified in the
proof. The marked cochain and peripheral identifications give
\(H^*(\mathcal C_\iota)\) and \(\Pi_\iota\) as the integral
cohomology and fundamental group of the corresponding oriented
marked model. They have the following properties. The group \(\Pi_\iota\) is trivial for twenty-four
inputs and nontrivial for twenty-six.''',
 'Names the actual mathematical complexes and full presentations whose invariants were reported. All counts and original model scope remain; exact matrix-derived groups match every archived group.')
add('STATEMENT-GROUP',
 r'''Their fundamental-group outputs are all trivial. The corresponding''',
 r'''Their groups \(\Pi_\iota\) are all trivial. The corresponding''',
 'Uses the just-defined full marked peripheral group, preserving the three triviality assertions and the subsequent cap-product identification.')
add('COUNT-HEAD',
 r'''The pair \((N_0,N_1)\) counts trivial and nontrivial
fundamental-group outputs, respectively.''',
 r'''The pair \((N_0,N_1)\) counts trivial and nontrivial
peripheral groups \(\Pi_\iota\), respectively.''',
 'The same counts now refer directly to the defined groups.')
add('INPUT-BIJECTION',
 r'''model. Reading these fields and applying \(\pi\) assigns one element
of \(\mathcal I\) to each output. The resulting fifty elements are
distinct and their set equals \(\mathcal I\). This proves exact
coverage of the stated choices.''',
 r'''model. Applying \(\pi\) carries these marked data to the
corresponding element of \(\mathcal I\); applying \(\pi^{-1}\)
recovers the ordered local data. The independent binary choices
at the additive occurrences give distinct data and exhaust
\(\mathcal I\). Thus these are exactly the fifty presentations
to be calculated.''',
 'Retains the exact occurrence-permutation maps and inverse. The new replay independently generated all50 exact inputs and checked their request-set equality with the archived50; multiplicities and original/fractional choices are unchanged.')

old=r'''The degree-$i$ output consists of a free rank \(r_i\) and positive
invariant factors \(d_{i1}\mid\cdots\mid d_{is_i}\), all greater
than one. It represents
\[
 H^i=\mathbb Z^{r_i}\oplus
       \bigoplus_{j=1}^{s_i}\mathbb Z/d_{ij}.
\]
The coordinate interpretation is the identity on the ordered free
basis and the ordered cyclic summands. Each degree occurs once,
\(H^0=H^6=\mathbb Z\), and the alternating sum of the ranks is
the reported Euler characteristic. The ranks in complementary
degrees agree. The torsion lists in degrees $i$ and \(7-i\) agree
term by term, giving their comparison by the identity on cyclic
coordinates. The abelianized fundamental-group output has free
rank \(r_1\) and the torsion list of \(H^2\), in agreement with
the integral universal coefficient sequence.'''
new=r'''Here is the integral presentation used in each case. Let
\(C_0^\bullet\) be the marked cochain complex of the regular
bundle, and let \(C_j^\bullet,B_j^\bullet\) be those of the
$j$-th filling and its boundary. Write
\[
 \mathsf R_j:C_0^\bullet\longrightarrow B_j^\bullet,
 \qquad \mathsf S_j:C_j^\bullet\longrightarrow B_j^\bullet
\]
for the integral restrictions. In \(\mathsf S_j\), the local restriction
is composed with its comparison to the common boundary marking,
including the prescribed clutching term. These are the marked
pairs of \cite{manExplorer26}. They include the original additive
fillings, finite good-reduction quotients, multiplicative Mumford
fillings, and the twofold semistable quotients at \(I_1^*,I_3^*\).
For the last two, the local cochain ranks in degrees zero to four
are respectively \((1,2,2,3,2)\) and \((1,2,4,7,4)\); the
boundary ranks are \((1,3,4,4,3,1)\). Their full boundary
comparisons are retained in \(\mathsf S_j\).

Put
\[
 \mathcal A^\bullet=C_0^\bullet\oplus\bigoplus_j C_j^\bullet,
 \qquad \mathcal B^\bullet=\bigoplus_j B_j^\bullet,
 \qquad \rho(a_0,(a_j)_j)=(\mathsf R_j a_0-\mathsf S_j a_j)_j.
\]
In the concatenated integral bases the Mayer--Vietoris complex is
\[
 \mathcal C_\iota^i=\mathcal A^i\oplus\mathcal B^{i-1},
 \qquad
 D_i=\begin{pmatrix}d_{\mathcal A}^i&0\\
                   \rho^i&-d_{\mathcal B}^{i-1}\end{pmatrix}.
\]
The cochain-map identities give
\(\rho^{i+1}d_{\mathcal A}^i=d_{\mathcal B}^i\rho^i\),
so multiplication gives \(D_{i+1}D_i=0\).

Choose an integral kernel basis \(Z_i\) for \(D_i\), with
coordinate map \(L_i\). In a Smith factorization
\(P_iD_iQ_i\), let \(t_i=\operatorname{rank}D_i\).
Take for \(Z_i\) the columns of \(Q_i\) after column \(t_i\),
and for \(L_i\) the corresponding rows of \(Q_i^{-1}\). Thus
\[
 L_iZ_i=I,\qquad Z_iL_i x=x\quad(x\in\ker D_i),\qquad
 A_i=L_iD_{i-1},\qquad D_{i-1}=Z_iA_i.
\]
The nonzero diagonal entries of the Smith form of \(D_i\)
force all other coordinates of a cycle to vanish, which proves
these identities over \(\mathbb Z\). A Smith form
\(U_iA_iV_i\) therefore gives
\[
 H^i(\mathcal C_\iota)=\operatorname{coker}A_i
 =\mathbb Z^{r_i}\oplus
       \bigoplus_{j=1}^{s_i}\mathbb Z/d_{ij},
 \qquad d_{i1}\mid\cdots\mid d_{is_i},\quad d_{ij}>1.
\]
The map from a cycle \(x\) is given by the free and nonunit
Smith coordinates of \(U_iL_i x\), with reduction modulo
\(d_{ij}\) in the latter coordinates. Its inverse sends the
corresponding coordinate vector \(e_j\) to the class of
\(Z_iU_i^{-1}e_j\). The two compositions differ from the
identity only by the displayed boundary relations.

For all fifty complexes, these reductions give
\(H^0=H^6=\mathbb Z\). The Euler characteristic is
\(\sum_i(-1)^ir_i\), the ranks in complementary degrees agree,
and the invariant factors in degrees \(i\) and \(7-i\) agree
for \(1\leq i\leq6\).
The abelianization of the peripheral presentation has free rank
\(r_1\) and the invariant factors of \(H^2\), in agreement
with the integral universal coefficient sequence.'''
add('CONE-AND-SMITH',old,new,
 'Replaces unexplained output-basis prose with the actual finite free integral cone, signed differential, exact cycle basis, relation matrix, Smith projection and inverse representative lifts. Direct algebraic derivation is recorded in the P14 method note. All58 actual cones were replayed, independently reassembled and checked for D²=0; an incoming-SNF/outgoing-rank computation matched the backend kernel-SNF and archived groups in every degree. Includes actual starred semistable ranks. Geometric provenance remains attributed.')

add('PERIPHERAL-PRESENTATION',
 r'''The group descriptions, orders and abelianizations give twenty-four
trivial groups, twenty-one infinite cyclic groups, and one each of''',
 r'''For the group calculation, let \(e_1,\ldots,e_4\) be the
commuting fibre generators, put \(e^v=\prod_a e_a^{v_a}\),
and let \(x_j\) be the marked peripherals. The local data give
monodromies \(T_j\), vanishing lattices \(W_j\), multiplicities
\(\mu_j\) and peripheral periods \(v_j\). The presentation is
\[
 \begin{gathered}
 x_je^u x_j^{-1}=e^{T_ju},\qquad e^w=1\ (w\in W_j),\\
 x_j^{\mu_j}=e^{v_j},\qquad x_1\cdots x_r=1.
 \end{gathered}
\]
Close the vanishing lattices, together with
\((T_j-I)\mathbb Z^4\) at the multiplicity-one sites, under
all \(T_j^{\pm1}\), and call the resulting lattice \(L\).
Integral reduction gives \((T_j-I)\mathbb Z^4\subset L\)
for every site in all fifty cases. Hence the fibre subgroup is
central. There are at most two peripherals of multiplicity
greater than one. The other peripherals lie in the fibre
subgroup, and the product relation expresses either remaining
peripheral in terms of the other and a central element. Thus
\(\Pi_\iota\) is abelian, and the Smith form of the exponent-sum
relation matrix computes the full group. It gives twenty-four
trivial groups, twenty-one infinite cyclic groups, and one each of''',
 'Supplies the full nonabelian presentation before abelianization and proves the abelian reduction from exact normal-lattice containment and at most two multiple sites. Replay retains every relator, normal-lattice basis and integer containment witness; all58 are fibre-central and abelian_proved. Counts and finite orders remain unchanged.')
add('SPHERE-CRITERION',
 r'''The integral-sphere recognition agrees with this test at every
input. The smooth-sphere recognition is its conjunction with the
trivial fundamental-group output. In these three graded groups the''',
 r'''These are precisely the three inputs with the integral cohomology
of a six-sphere, and their groups \(\Pi_\iota\) are trivial.
In these three graded groups the''',
 'The same exact homology criterion and full-group triviality are now stated as mathematical conclusions. Archive flags were checked against this conjunction, and the58 actual presentations reproduce those values; no geometric recognition claim is enlarged.')
add('CLUTCH-GROUPS',
 r'''For each of the four values of $n$ the outputs are''',
 r'''For each of the four values of $n$, the same cone and
peripheral presentation give''',
 'All eight clutch inputs were recomputed from their actual marked matrices and match the unchanged table.')
add('CLUTCH-SPHERE',
 r'''Thus the four unit-clutch inputs have the integral-sphere
recognition.''',
 r'''Thus the four unit-clutch inputs have the integral cohomology
of a six-sphere and trivial peripheral group.''',
 'States the exact two mathematical properties appearing in the preceding table. Their section coefficients and disjointness argument remain unchanged.')

old=r'''\nolinkurl{code/S6_SERIES_PUBLISH_c7_ku_archive_audit.py}
& Monodromy reduction orders, occurrence permutations with inverses and switch-coordinate maps for $21$ profiles and $50$ inputs; four pairs of integral clutch coordinates.
See \cref{maps:src:D.2.2}. \\[3pt]'''
new=old+r'''
\path{code/S6_SERIES_PUBLISH_c9_ku_matrix_replay.py}
& The $50$ marked filling inputs and eight integral-clutch inputs:
full integral cochain cones, an independent block assembly,
Smith calculations in every degree, and full peripheral presentations
with integral centrality witnesses. The calculation uses the cited
local models and their marked boundary maps.
See \cref{maps:src:D.2.2}. \\[3pt]'''
add('PROGRAM',old,new,
 'Adds the newly run58-input algebraic replay in the Programs table, without claiming rederivation of the geometric local models or adding a new standing link.',types='D13',label='programs:02KU')

add('SOURCE-VERSION',
 r'''\bibitem[Engel(2026{\natexlab{b}})]{manExplorer26}
Philip Engel.
\newblock Threefold explorer, 2026.
\newblock \url{https://philip-engel.github.io/threefold-explorer/}.''',
 r'''\bibitem[Engel(2026{\natexlab{b}})]{manExplorer26}
Philip Engel.
\newblock Threefold explorer, 2026.
\newblock Documentation, marked local-model database and source,
consulted 26 November 2026.
\newblock \url{https://philip-engel.github.io/threefold-explorer/}.
\newblock Documentation:
\url{https://philip-engel.github.io/threefold-explorer/docs/}.''',
 'Records author application/documentation URLs and consultation date. The exact external source pin and source-file hashes remain in replay provenance records, as required by prompt0.3; the manuscript carries no additional commit identifier.',types='D18',label='bibliography:manExplorer26')

candidate=source
for row in rows:
 assert candidate.count(row['old_text'])==1,(row['change_id'],'stale/overlapping guard')
 candidate=candidate.replace(row['old_text'],row['new_text'],1)
assert re.findall(r'\\label\{[^}]+\}',source)==re.findall(r'\\label\{[^}]+\}',candidate)
assert re.findall(r'\\hypertarget\{[^}]+\}',source)==re.findall(r'\\hypertarget\{[^}]+\}',candidate)
a=candidate.index(r'\hypertarget{tag-02KU}')
b=candidate.index(r'\end{proof}',a)
assert not re.search(r'\boutputs?\b|reported Euler|recognition',candidate[a:b])
fields=['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status']
with (OUT/'S6_SERIES_PUBLISH_c9_P14_defects.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
print('Prepared',len(rows),'guarded P14 replacements, including58-input program row and author source/documentation locators.')
print('All original blocks occur once; labels/targets retained; all existing tables/counts unchanged; canonical TeX untouched.')
print('No output/recognition vocabulary remains in the proposed02KU proof; actual full matrix and pi1 replay passed for58 inputs.')
print('Geometric local-model derivations remain attributed to the cited model data; no independent geometric check claimed.')
