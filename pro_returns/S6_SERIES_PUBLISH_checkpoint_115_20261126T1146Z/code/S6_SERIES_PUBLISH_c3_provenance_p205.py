#!/usr/bin/env python3
"""Prepare a bounded P205 unit pass, preserving all construction maps."""
from pathlib import Path
import csv, hashlib, re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation3_provenance/p205'
OUT.mkdir(parents=True,exist_ok=True)
OLD=ROOT.parents[1]/'tmp/c3_provenance_p205_old.tex'
old=OLD.read_text()
new=old
changes=[]

def replace(before,after,kinds,reason):
    global new
    assert old.count(before)==1,('base',before[:100],old.count(before))
    assert new.count(before)==1,('receiving',before[:100],new.count(before))
    new=new.replace(before,after)
    changes.append(dict(change_id=f'II-C3-P205-{len(changes)+1:03d}',type=kinds,
        statement_id='ii:three-doubled-nodal-fibres',
        old_location='Three doubled nodal supports; complete P205 example',
        old_page='final concordance pending',new_location='same complete example and proof',
        new_page='integrated build pending',old_text=before,new_text=after,reason=reason,
        review_status='Draft prepared; complete receiving read pending'))

replace(r'\subsection{Three doubled nodal supports}',
    r'\subsection{Three doubled nodal supports}\label{subsec:II:three-doubled-nodal-supports}',
    'D14','Give the complete one-owner unit a stable local section destination; its placement immediately after the refined conductor theorem is preserved.')
replace(r'\item We first specify the integral local system. Put',r'\item Let',
    'D08','Begin with the defined punctured base rather than an announcement of the proof step.')
replace('Each $N_i$ has\nrank one and square zero for real $\\epsilon>0$.',
    'Each $N_i$ has\nrank one and square zero for real $\\epsilon>0$. On the\nfour-dimensional space, extend $N_i$ by zero on $e_0$.',
    'D20','Specify the exact extension used by the later four-dimensional exponentials and exterior-algebra action.')
replace('$A_i$. This retains the integral marking while making its real\nnilpotent parts small.',
    '$A_i$. Thus $D_\\epsilon P:\\mathbb Z^4\\to\\Lambda_\\epsilon$\nintertwines the fixed integral representation with these real\nmatrices, whose nilpotent entries tend to zero.',
    'D08;D20','State the displayed lattice isomorphism and its intertwining property explicitly.')
replace('The deck\nmaps extend: coordinate changes introduce logarithms of holomorphic\nunits, and at a fixed point their action is the semisimple part of the\noriginal monodromy. Their group identities extend from the punctured\ncurve.',r'''The deck
maps extend because coordinate changes introduce logarithms of
holomorphic units. At a fixed point their homology action is
\[
 \operatorname{diag}(1,B_i(\epsilon))\exp(-N_i/2).
\]
Its square is the identity, since the squared monodromy is
$\exp N_i$ and the two factors commute. The inverse transpose
gives the cohomology action in the canonical frame. This is the
finite part of the half-turn comparison, as follows by inserting
$\log(-s)=\log s+\pi i$ into the frame formula. The group
identities extend from the punctured curve.''',
    'D20;D25','Give the exact matrix relating the monodromy and the extended deck action, including its cohomology convention.')
replace('Choose generators specializing to the real\ncharacter basis at zero. Evaluation gives an equivariant holomorphic\ntrivialization of $\\mathcal E$ with the four fixed character matrices.',r'''Choose a holomorphic frame of $W$ whose values at zero are
the real character basis, and denote its sections by
$e_\chi(\epsilon)$. The section
$P_\chi(\epsilon)e_\chi(\epsilon)$ is holomorphic and remains nonzero
after shrinking. These four sections and the evaluation isomorphism
give an equivariant holomorphic trivialization of $\mathcal E$
with the four fixed character matrices.''',
    'D22;D25','Construct the character-line generators by the already-displayed projectors, so the trivialization map is explicit.')
replace('These are\nthe required invertible row changes on the overlapping charts. Take',
    'These invertible row changes identify the planes on the overlapping\ncharts. Take',
    'D08','State the plane identifications directly.')
replace('At the marked lifts $0,-i,1$ its complex\naxes are $-e_1,-e_2,-e_3$.',r'''At the marked lifts $0,-i,1$, its limiting frames are,
respectively, the displayed frame at $\zeta=\infty$,
$\Pi_{\rm tw}(i)$ and $\Pi_{\rm tw}(-1)$: these are the
values of $-1/z^3$ at those three lifts.''',
    'D20;D22','Replace the undefined complex-axis shorthand by the exact frames used in the subsequent three determinant substitutions.')
replace('Let $\\omega$ be the wedge of the two canonical-frame covectors.\nRank one gives',
    'Let $\\omega$ be the wedge of the two canonical-frame covectors,\nand let $N^t$ act on exterior powers by its induced derivation.\nRank one gives',
    'D20','Specify the exterior-algebra operator in the exact logarithmic determinant identity.')
replace('At the three limiting\ntwistor planes, substitution of the displayed rows and nilpotents\ngives, with $y=\\operatorname{Im}Z$,',r'''At $\epsilon=0$ the three canonical frames are the twistor
frames just listed. Substituting those frames and the polynomial
matrices $N_i(\epsilon)$ gives, with $y=\operatorname{Im}Z$,''',
    'D20;D25','Identify the exact central frames used for the limiting determinant calculation; the following normalized-coefficient continuity argument applies to the moving canonical frames.')
replace('Real marking\nchanges have determinant one, and a change of Hodge-row basis\nmultiplies $D$ by $|\\det K|^2$, so the inequalities agree on overlaps.',
    'The real transition matrices $\\operatorname{diag}(1,B_i)$ have\ndeterminant one, and a change of Hodge-row basis multiplies $D$\nby $|\\det K|^2$. Hence these inequalities agree on overlaps.',
    'D20;D25','Name precisely the determinant-one transition matrices. The distinct lattice coordinate map D_epsilon P has negative determinant and is correctly accounted for in the next item.')
replace(r'\item We next extend each puncture with its exact marking $C_i$.',
    r'\item At each puncture use the marking $C_i$.',
    'D08','Begin the local extension with its specified mathematical marking.')
replace('On nonzero fibres $u=r^kx_k$ is their common multiplicative coordinate.',r'''The chain is Hausdorff. For $j>k$ on a nonzero fibre the
transition is $x_j=r^{k-j}x_k$, $y_j=r^{j-k}y_k$. If a
sequence with $r\to0$ converges in both charts,
boundedness of $x_j$ forces a nonzero limiting $y_k$. Then
$x_k\to0$, and $j\ge k+2$ would make $x_j$ unbounded. For
$j=k+1$ the limits satisfy $x_{k+1}=1/y_k$, $y_{k+1}=0$,
so they are already identified by the adjacent transition.
The same-chart limits agree, and these cases also cover
central sequences. Thus distinct points have disjoint
neighbourhoods. On nonzero fibres $u=r^kx_k$ is the common
multiplicative coordinate.''',
    'D22;D25','Verify Hausdorff separation for the infinite chain before passing to its free properly discontinuous group quotient; the transition maps are unchanged.')
replace('These estimates also prove proper discontinuity at the centre.\nA compact set is covered by finitely many charts, say $|k|\\le L$,\nwith both chart-coordinate norms bounded by $R_0\\ge1$.',r'''The invariant chart norms are
\[
 \begin{aligned}
 \|x_k\|&=|x_k|\exp\!\left(
 \frac{2\pi\operatorname{Im}\beta(r)}{\operatorname{Im}\tau(r)}
 \operatorname{Im}z\right),\\
 \|y_k\|&=|y_k|\exp\!\left(
 -\frac{2\pi\operatorname{Im}\beta(r)}{\operatorname{Im}\tau(r)}
 \operatorname{Im}z\right).
 \end{aligned}
\]
They satisfy $\|x_k\|\|y_k\|=|r|$ and
$\|u\|=|r|^k\|x_k\|$. They extend to the respective
line-bundle charts at the centre.

These estimates also prove proper discontinuity at the centre.
A compact set is covered by finitely many charts, say $|k|\le L$,
with both chart norms bounded by $R_0\ge1$.''',
    'D20;D22;D25','Define the two invariant chart norms, their product and their relation to u before using their uniform bounds at the central fibre.')
replace('$X$ has the actual lattice $(p,b,c,d)$.',
    '$X$ has period lattice $(p,b,c,d)$.',
    'D08','Name the lattice obtained from the explicit exponential quotient.')
replace('The local étale quotient retains the reduced equation $xy=0$ and\nits transverse disc.',
    'The quotient map is a local biholomorphism, so its inverse chart\nidentifies the reduced germ with $xy=0$ times the $z$-disc.',
    'D08;D25','State the local inverse chart that transfers the reduced product germ through the free finite quotient.')
replace('These are exactly the asserted conductor maps\nand product germs. ','',
    'D08','Delete the recapitulation after the complete normalization and conductor-map construction.')
replace('Thus $\\Phi$ descends to the required biholomorphism on the punctured\noriginal disc.',
    'Thus $\\Phi$ descends to a biholomorphism with $J$ on the punctured\noriginal disc.',
    'D08','Name the receiving Jacobian family of the affine conjugacy.')
replace('Normalization additivity gives $e(S)=0$.',r'''The conductor pushout of \cref{lem:II:proper-conductor-pushout}
gives $e(S)=e(N)-e(D)+e(C_{\rm im})$. Here $D$ is the union
of the two sections and $C_{\rm im}$ the union of their image
curves. All three terms vanish, since $N$ is a projective-line
bundle over an elliptic curve and all four conductor curves
are elliptic. Thus $e(S)=0$.''',
    'D12;D22','Apply the same single conductor-pushout owner to the exact normalization map, with all Euler terms identified.')
replace(r'''A sufficiently small tube retracts onto its central fibre, as in
the proper analytic neighbourhood retraction of
\cite[p.~85, paragraph following Definition~1]{BobadillaKollar2012}.''',r'''Apply \cref{lem:II:compact-analytic-tube} to the proper
map $X\to\Delta_r$ just constructed: its total space is smooth
and its punctured fibres are smooth two-tori. The inclusion of
$E\times I_2$ in a sufficiently small closed root tube is a
homotopy equivalence. This inclusion is equivariant for $g$,
so its induced cohomology isomorphism commutes with $g^*$.''',
    'D12;D18;D25','Apply the existing exact compact-tube owner to this root model. Equivariance is needed only for the inclusion-induced cohomology map; no equivariant choice of the retraction is assumed.')
replace('The graph one-class restricts to $d^*$.',r'''The graph one-class restricts to $d^*$. In the plumbing
description, collapse the circular $c$ direction in each neck.
The longitudinal path from $U_0$ to $U_2$, closed by $T$,
traverses the two-component graph once and represents $d$.
Thus this graph map sends $c$ to zero and $d$ to its oriented
generator.''',
    'D22;D25','Give the exact nearby-cycle-to-dual-graph map determining the primitive graph restriction.')
replace('a single smaller disc retains all norm estimates and keeps',
    'the norm estimates hold uniformly on a single smaller disc, with',
    'D08','State uniformity over the real deformation parameter directly.')
replace('The period\ngenerators vary continuously and retain the homology marking.',
    'The period\ngenerators vary continuously with the fixed integral homology marking.',
    'D08','State the continuous marked family in mathematical terms.')
replace(r'''\item Integrally, the conductor pushout has two lattices generated
by $p/4,b$, amalgamated along the common sublattice generated by
$p/2,b$. Its abelianization is''',r'''\item Apply \cref{lem:II:proper-conductor-pushout} to the finite
normalization $N\to S$, its two disjoint conductor sections and
their two image curves. For the local groups use a sufficiently
small tube in $M$. Applying \cref{lem:II:compact-analytic-tube}
to $M\to\Delta_t$ identifies its integral homology with that
of $S$ through the inclusion. Choose compatible finite CW structures
with those sections as subcomplexes. The incidence graph is a
tree. Projection identifies $\pi_1(N)$ and each section group
with $\langle p/2,b\rangle$, while the two image groups are
$\langle t_1,b\rangle$ and $\langle t_2,b\rangle$, with
$t_i=p/4$. Each section-to-image map sends $(p/2,b)$ to
$(2t_i,b)$. Thus the two image lattices are amalgamated along
this common sublattice. Their abelianization has relation
$2t_1=2t_2$; put $t=t_2$ and $\delta=t_1-t_2$. It is''',
    'D12;D22;D25','Apply the single conductor-pushout owner with every vertex and edge map identified. The explicit edge matrix diag(2,1) gives the displayed free and order-two summands.')
replace(r'\item We compute its actual affine obstruction. The primitive',
    r'\item The primitive',
    'D08','Remove the process announcement; the full invariant vector and affine loop values follow unchanged.')
replace('The integral calculation retains the actual torsor. An integral',
    'An integral',
    'D08','The preceding affine translations already identify this torsor; proceed directly to the integral extension condition.')
replace(r'\item Finally put $V=R^1f_*\mathbb Q|B^\circ$. The actual local',
    r'\item Put $V=R^1f_*\mathbb Q|B^\circ$. The local',
    'D08','State the cohomology sheaf and its restriction maps directly.')
replace(r'''We give the needed matrix ranks explicitly.
The common homology fixed space is generated by $(0,0,0,1)^t$,
and the common cohomology fixed space by $\alpha$; row reduction
of the stacked $(A_i-I)$ and $(A_i^t-I)$ gives respectively
\[
 \begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\end{pmatrix},\qquad
 \begin{pmatrix}1&0&0&-1/2\\0&1&0&-1/2\\0&0&1&-1/2\end{pmatrix}.
\]''',r'''For every invertible $T$, the identity
$T^{-1}-I=-T^{-1}(T-I)$ identifies the fixed kernels of
$T$ and $T^{-1}$. Apply it to each $A_i^t$ and its exterior
powers for the parallel cohomology monodromies $A_i^{-t}$.
For a homology vector $x$, the equations $(A_1-I)x=0$
give $x_2=x_3=0$, and $(A_2-I)x=0$ then gives $x_1=0$;
$A_3$ also fixes $(0,0,0,1)^t$. The common homology fixed
space is therefore $\mathbb Q(0,0,0,1)^t$. For a cohomology vector $u$, the
first transpose gives $u_4=2u_2$ and $u_3=u_2$, and the
second gives $u_1=u_3$. The displayed $\alpha$ satisfies
the third as well. Thus the common cohomology fixed space
is exactly $\mathbb Q\alpha$.''',
    'D09;D12;D25','Replace the two row-reduction dumps by the exact equations and solution maps in the same displayed bases. The fixed spaces and ranks are identical.')
replace(r'''In the exterior-pair order $12,13,14,23,24,34$, rows $1,2,4,5$ of
$\bigwedge^2A_1^t-I$ and rows $1,2$ of $\bigwedge^2A_2^t-I$ form
the matrix
\[
 \begin{pmatrix}
 -2&0&1&0&0&0\\2&-2&0&0&0&0\\
 0&0&0&0&-2&1\\0&0&0&0&-2&0\\
 -2&0&0&-2&0&0\\0&0&-1&0&0&2
 \end{pmatrix},\qquad\det=-16.
\]
Thus''',r'''Let $\lambda_1^*,\ldots,\lambda_4^*$ be the basis dual to
the displayed integral lattice basis. Write an exterior
class as $\sum_{i<j}v_{ij}\lambda_i^*\wedge\lambda_j^*$.
Invariance under
$\bigwedge^2A_1^t$ and $\bigwedge^2A_2^t$ implies
\[
 v_{14}=2v_{12},\quad v_{13}=v_{12},\quad
 v_{34}=2v_{24},\quad v_{24}=0,\quad
 v_{23}=-v_{12},\quad v_{14}=2v_{34}.
\]
They force all six coefficients to vanish. In coefficient
order $12,13,14,23,24,34$, the six corresponding linear
forms $-2v_{12}+v_{14}$, $2v_{12}-2v_{13}$,
$-2v_{24}+v_{34}$, $-2v_{24}$,
$-2v_{12}-2v_{23}$ and $-v_{14}+2v_{34}$ have determinant
$-16$. Thus''',
    'D09;D25','Keep the exact six exterior-linear constraints, their coefficient order and determinant -16, while replacing selected matrix-row bookkeeping by their direct kernel calculation.')
replace('$b_3(Y)=2$, completing all\nthe assertions.','$b_3(Y)=2$.',
    'D08','End with the proved Betti number.')
replace('; fixed spaces for the\ninverse-transpose parallel matrices are the same. ',
    '. ', 'D12;D25','The exact inverse-kernel identity is now proved once before both fixed-space calculations.')

new=new.rstrip()+'\n'
assert '\r' not in new
(OUT/'S6_SERIES_PUBLISH_p205_proposed.tex').write_text(new)

def write(name,rows):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t',lineterminator='\n')
        w.writeheader();w.writerows(rows)

write('S6_SERIES_PUBLISH_p205_defects.tsv',changes)
sha=lambda s:hashlib.sha256(s.encode()).hexdigest()
write('S6_SERIES_PUBLISH_p205_guards.tsv',[dict(change_id='II-C3-P205-GUARD-001',
    statement_id='ii:three-doubled-nodal-fibres',source_file='S6_SERIES_PUBLISH_II.tex',
    old_sha256=sha(old),new_sha256=sha(new),old_text=old,new_text=new,
    proposed_file='agents/continuation3_provenance/p205/S6_SERIES_PUBLISH_p205_proposed.tex')])
print('Prepared',len(changes),'exact changes; receiving full read still required; main unchanged.')
