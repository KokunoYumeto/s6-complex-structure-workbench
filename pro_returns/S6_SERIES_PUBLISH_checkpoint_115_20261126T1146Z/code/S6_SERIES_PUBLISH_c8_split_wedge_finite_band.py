"""Give the wedge recognition and finite-band maps their full local units."""
from datetime import datetime, timezone
from collections import Counter
import re
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r

path = u.WORK / 'root/retained_angle.tex'
before = path.read_text()
qc_start = before.index(r'\begin{lemma}[The three-dimensional coned Seifert target]')
qe_start = before.index(r'\begin{proposition}[The actual degree-three finite-band map]')
old_qc, old_qe = before[qc_start:qe_start], before[qe_start:]
qc = r'''\subsection{Recognition of a two-sphere and three-sphere wedge}

\begin{lemma}[The two-generator wedge]
\hypertarget{tag-02QC}{}\label{mapsIII:carrier-three-complex-wedge}
{\normalfont\scriptsize tag 02QC}\par
Let $C$ be a simply connected CW complex with
$\widetilde H_2(C;\mathbb Z)=\widetilde H_3(C;\mathbb Z)=\mathbb Z$
and zero reduced integral homology in every other degree.
For any chosen generators $u\in H_2(C;\mathbb Z)$ and
$v\in H_3(C;\mathbb Z)$, there are based maps
$a:S^2\to C$ and $b:S^3\to C$ carrying the oriented sphere
classes to $u$ and $v$. The map $F=a\vee b:S^2\vee S^3\to C$
is a based homotopy equivalence.
\end{lemma}

\begin{proof}
The Hurewicz isomorphism $\pi_2(C)\to H_2(C;\mathbb Z)$
supplies a based cellular map $a$ representing $u$.
Naturality shows that $a$ induces an isomorphism on $\pi_2$
as well as on $H_2$. Form its mapping cylinder
\[
 M=(S^2\times[0,1])\amalg C/((z,1)\sim a(z)),
 \qquad A=S^2\times\{0\}.
\]
The retraction $r:M\to C$ has $r([z,t])=a(z)$ and is the
identity on $C$. Its deformation retraction sends
$[z,t]$ to $[z,(1-s)t+s]$ and fixes $C$. The basepoint path
$[z_0,t]$ identifies the bottom basepoint with $a(z_0)$;
all homotopy groups below use this path. If $i:A\to M$ is
the inclusion, then $ri=a$ and
$i_\#=r_\#^{-1}a_\#$, with inverse basepoint transport along
the reversed path. Both $A$ and $M$ are simply connected.
The pair exact sequence therefore gives
$\pi_1(M,A)=\pi_2(M,A)=0$.

Relative Hurewicz and the homology exact sequence give the
isomorphisms
\[
 h:\pi_3(M,A)\xrightarrow{\cong}H_3(M,A;\mathbb Z),
 \qquad q_H:H_3(M;\mathbb Z)\xrightarrow{\cong}H_3(M,A;\mathbb Z).
\]
Here $H_3(A)=0$ and $i_*:H_2(A)\to H_2(M)$ is an isomorphism,
which prove both sides of the second assertion. The next
homotopy boundary has image
$\ker(i_\#: \pi_2(A)\to\pi_2(M))=0$; thus
$q_\pi:\pi_3(M)\to\pi_3(M,A)$ is surjective. Choose
$[g]\in\pi_3(M)$ with
\[
 q_\pi[g]=h^{-1}q_H(r_*^{-1}v),\qquad b=rg.
\]
Give $S^3=D^3/\partial D^3$ its disk orientation.
Naturality gives
$q_H(g_*[S^3])=h(q_\pi[g])=q_H(r_*^{-1}v)$.
The injectivity of $q_H$ proves $b_*[S^3]=v$.
These are the canonical relative maps of
\cite[Theorem~4.37 and Lemma~4.38, pp.~370--372]{Hatcher2002}.

The wedge map $F=a\vee b$ induces the chosen generator maps
in degrees two and three, the identity on the connected
degree-zero groups, and the unique isomorphisms between zero
groups in every other degree. It is an integral homology
equivalence between simply connected CW complexes. To specify
its homotopy inverse, form its mapping cylinder $N$ with
bottom inclusion $j_W:W\to N$, $W=S^2\vee S^3$, top inclusion
$j_C:C\to N$ and retraction $p:N\to C$. The pair $(N,W)$
is acyclic. Relative Hurewicz, starting with its simply
connected pair and proceeding through every degree, gives
$\pi_n(N,W)=0$ for all $n\ge1$. The CW Whitehead theorem
\cite[Theorem~4.5 and Corollary~4.33, pp.~346--347 and~367--368]{Hatcher2002}
therefore gives a retraction $k:N\to W$ and a deformation
$T_s$ from $1_N$ to $j_Wk$, fixed on $W$. Set $G=kj_C$.
The cylinder paths $U_t(w)=[w,t]$ give
$kU_t:1_W\simeq GF$, and $pT_sj_C$ gives
$1_C\simeq FG$. In a reduced based mapping cylinder these
homotopies fix the basepoint. This constructs the inverse
for the actual chosen generator map, without imposing a bound
on the dimension or number of cells of $C$.
\end{proof}

'''
qe = r'''\subsection{Integral degree-three maps of the finite band}

\begin{definition}[The marked finite-band coverings]
\hypertarget{tag-Q020}{}\label{mapsIII:def:finite-band-coverings}
{\normalfont\scriptsize tag Q020}\par
Use the three-filling datum of
Definition~\ref{mapsIII:def:three-filling-datum} and the actual
quotients $\pi_j:F\to S_j=F/\langle h_j\rangle$ of
\eqref{maps:eq:B.5.3}. On the ordered basis
$(g,u_h,w_h,d)=(\widehat\gamma,\widehat u,\widehat w,\widehat\delta)$
of $\Lambda$, their affine actions are
\[
 h_j(x)=A_jx+v_j/m_j,\qquad (m_1,m_2)=(3,4),
\]
\[
 A_1=\begin{pmatrix}1&0&0&0\\6&0&1&0\\-6&-1&-1&0\\-2&1&0&1\end{pmatrix},
 \quad
 A_2=\begin{pmatrix}1&0&0&0\\0&0&-1&0\\-6&1&0&0\\3&0&1&1\end{pmatrix},
 \quad
 v_1=\begin{pmatrix}1\\2\\-4\\0\end{pmatrix},\quad
 v_2=\begin{pmatrix}-1\\-3\\3\\0\end{pmatrix}.
\]
The inverse naming map sends $(g,u_h,w_h,d)$ to its displayed
hatted basis. Write $(\gamma,u,w,\delta)$ for the dual basis
of $V=H^1(F;\mathbb Z)$; thus $u=u^*$, $w=w^*$ and
$\delta=\delta^*$ in the cell-presentation proof, with the
inverse assignments $u^*=u$, $w^*=w$, $\delta^*=\delta$.
Orient $F$ by $\operatorname{vol}=\gamma uw\delta$ and $S_j$
by its quotient orientation. Define
\[
 b=\gamma uw,\qquad c_1=uw\delta-4\gamma u\delta-2\gamma w\delta,
 \qquad c_2=uw\delta-3\gamma u\delta-3\gamma w\delta.
\]
\end{definition}

\begin{proposition}[The degree-three finite-band map]
\hypertarget{tag-02QE}{}\label{mapsaudit:finite-degree-three}
{\normalfont\scriptsize tag 02QE}\par
For Definition~\ref{mapsIII:def:finite-band-coverings},
\[
 \pi_1^*H^3(S_1;\mathbb Z)=\mathbb Zb\oplus\mathbb Zc_1,
 \qquad
 \pi_2^*H^3(S_2;\mathbb Z)=\mathbb Z(2b)\oplus\mathbb Zc_2.
\]
Choose the unique cohomology bases having these ordered
pullbacks and the Kronecker-dual bases of $H_3(S_j;\mathbb Z)$.
Relative to the homology basis dual to
$(\gamma uw,\gamma u\delta,\gamma w\delta,uw\delta)$,
the finite-band Mayer--Vietoris map is
\[
 \alpha_3=(\pi_{1*},-\pi_{2*})=
 \begin{pmatrix}1&0&0&0\\0&-4&-2&1\\-2&0&0&0\\0&3&3&-1\end{pmatrix}.
\]
Its nonzero Smith entries are $(1,1,1)$ and its integral
kernel is generated by $(0,1,1,6)^t$. The degree-three
pushforward images have indices one and two, respectively;
the degree-one images have indices three and four. The
corresponding pairs of covariant maps admit no commuting
identification by integral isomorphisms. Their pullback and
covering-transfer maps satisfy
$D_F\pi_j^*=\operatorname{tr}_jD_{S_j}$, where
$\langle\alpha,D_M\xi\rangle=\int_M\alpha\wedge\xi$.
\end{proposition}

\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item The quotient actions, their free affine covering
presentations and the free integral homology of $S_j$ are
proved in Theorem~\ref{maps:src:B.5.2} for these identical
matrices and translations. Under the identity of the ordered
marked lattices, with inverse the same identity, its bases
$(\rho_1,w_h)$ and $(\rho_2,w_h)$ give the degree-one maps
\[
 Q_1=\begin{pmatrix}3&0&0&0\\0&2&1&3\end{pmatrix},\qquad
 Q_2=\begin{pmatrix}-4&0&0&0\\0&1&1&2\end{pmatrix}.
\]
The integral dual bases have pullbacks
$(3\gamma,\eta_1)$ and $(-4\gamma,\eta_2)$, where
$\eta_1=2u+w+3\delta$ and $\eta_2=u+w+2\delta$.
Replacing the second downstairs basis by $(-\rho_2,w_h)$
uses $\operatorname{diag}(-1,1)$, inverse itself, and gives
the positive pullback basis $(4\gamma,\eta_2)$.

For the degree-three basis in the statement, the duality map
$D_F:H^3(F)\to H_1(F)$ has matrix
\[
 J=\begin{pmatrix}0&0&0&1\\0&0&-1&0\\0&1&0&0\\-1&0&0&0\end{pmatrix},
 \qquad J^{-1}=-J.
\]
It sends $b$ to $-d$, $c_1$ to $v_1$ and $c_2$ to $-v_2$.
Change of variables for the orientation-preserving deck map
gives $D_Fh_j^*=A_j^{-1}D_F$. Solving $(A_j-I)x=0$ gives
\[
 x=(a,2a,-4a,e)\quad(j=1),\qquad
 x=(a,3a,-3a,e)\quad(j=2),\qquad a,e\in\mathbb Z.
\]
The inverse parameter maps read the first and fourth
coordinates. Applying $J^{-1}$ proves that the full integral
fixed lattices in degree three are
$I_1=\mathbb Z\langle b,c_1\rangle$ and
$I_2=\mathbb Z\langle b,c_2\rangle$.

Exterior multiplication pairs the positive degree-one bases
above with $(b,c_j)$ by
\[
 K_1=\begin{pmatrix}0&3\\-3&0\end{pmatrix},\qquad
 K_2=\begin{pmatrix}0&4\\-2&0\end{pmatrix}.
\]
The downstairs integral pairing is unimodular because these
oriented closed four-manifolds have free integral homology.
Pullback multiplies the pairing by $m_j$, as follows by
lifting an oriented fundamental triangulation. For the
coordinate matrix $C_j$ of a basis of the pullback image
in $I_j$, this says $K_jC_j=m_jU_j$ with $U_j$ unimodular.
The image has full rank: covering transfer gives
$\operatorname{tr}\pi_j^*=m_j$ on cohomology over
$\mathbb Q$, and all the groups used here are free.
Thus
\[
 [I_j:\pi_j^*H^3(S_j;\mathbb Z)]
 =|\det C_j|=m_j^2/|\det K_j|=1,2.
\]
For a descended class $rb+sc_2$, pairing with $\eta_2$
gives $-2r\in4\mathbb Z$. Hence its $b$ coefficient is
even. The lattice $\mathbb Z(2b)\oplus\mathbb Zc_2$
already has index two in $I_2$; equality of the indices
proves equality of the full sublattices. This gives both
pullback formulas and their sufficiency. Pullback is
injective over $\mathbb Z$, because its kernel is killed
by the degree and its domain is free. Consequently the
ordered downstairs bases in the statement exist uniquely.

\item Kronecker naturality gives
$\langle a,\pi_{j*}z\rangle=\langle\pi_j^*a,z\rangle$.
Thus each degree-three pushforward is the transpose of
its displayed pullback matrix, and the second summand of
the Mayer--Vietoris difference has the stated minus sign.
Row three of $\alpha_3$ is minus twice row one, while the
minor on rows $(1,2,4)$ and columns $(1,2,4)$ is one.
Its rank is three and all three positive Smith entries are
one. The kernel equations give $z_1=0$, $z_3=z_2$ and
$z_4=6z_2$, with $z_2$ an arbitrary integer.
The first pushforward sends the first and fourth basis
cycles to $(1,0)$ and $(0,1)$. The second sends them to
$(2,0)$ and $(0,1)$, and its first coordinate is always
even. These are the full images and prove the two indices.

The degree-one matrices $Q_j$ have images of indices
three and four. Their cokernels have orders three and
four; the corresponding degree-three cokernels have
orders one and two. A commuting square of these maps
with integral isomorphisms on source and target induces
an isomorphism of the cokernels, contradicting these
orders in each case. This is the stated obstruction to
that precise commuting identification.
The relation between degrees is instead given by the
actual duality and transfer maps: lifting every simplex
of an oriented fundamental chain gives
\[
 D_F\pi_j^*=\operatorname{tr}_jD_{S_j},\qquad
 (\pi_j)_*\operatorname{tr}_j=m_j\operatorname{id},\qquad
 \operatorname{tr}_j(\pi_j)_*=\sum_{k=0}^{m_j-1}A_j^k
 \quad\hbox{on }H_1(F;\mathbb Z).
\]
These identities, together with the Kronecker transpose
above, describe the maps in the fixed integral markings.
\end{enumerate}
\end{proof}

'''

retained = before[:qc_start].rstrip() + '\n\n'
combined = retained + qc + qe
u.check_permanent_identifiers(before, combined,
    {'mapsIII:def:finite-band-coverings'}, {'tag-Q020'})
assert Counter(re.findall(r'\\label\{([^}]+)\}', old_qc)) == Counter(re.findall(r'\\label\{([^}]+)\}', qc))
assert before.count(old_qc) == before.count(old_qe) == 1
df, ds = r.table(r.DEFECTS)
changes = [
 ('WEDGE-UNIT', 'D12', 'mapsIII:carrier-three-complex-wedge', old_qc, qc,
  'Move the complete general lemma into its own preceding subsection; retain every original conclusion and supply the chosen generator maps, exact mapping cylinders and homotopy inverse. The orphan coned-Seifert application is wholly contained in the carrier proof at its pi1, boundary kernel, H2/H3 and wedge calculation; that proof is being consolidated through this unique owner with the same u and v.'),
 ('FINITE-BAND-UNIT', 'D22', 'mapsaudit:finite-degree-three', old_qe, qe,
  'Move the whole finite-band proposition after its actual cell-presentation prerequisites. Define all affine and orientation data, give exact coefficient maps and inverse basis change, prove the full integral images, and replace the working-proof phrase by its precise cokernel obstruction and duality/transfer relation. No old mathematical conclusion or identity is removed.')
]
for suffix, kind, label, old, new, reason in changes:
    ident = 'III-C8-ROOT-' + suffix
    assert not any(x['change_id'] == ident for x in ds)
    ds.append(dict(change_id=ident, type=kind, statement_id=label,
        old_location='retained_angle full input, tail after03BE', old_page='pending page concordance',
        new_location='separate complete wedge/finite-band subsection', new_page='pending final PDF',
        old_text=old, new_text=new, reason=reason,
        review_status='staged exact edit; complete final-fragment reading and canonical placement pending'))
for name, value in [('carrier_wedge_recognition', qc), ('finite_band_homology', qe)]:
    dest = u.WORK / 'root' / (name + '.tex')
    assert not dest.exists()
    dest.write_text(value, encoding='utf-8', newline='\n')
path.write_text(retained, encoding='utf-8', newline='\n')
r.write_table(r.DEFECTS, df, ds)
print('UTC', datetime.now(timezone.utc).isoformat())
print('WEDGE_LINES', qc.count('\n'), 'FINITE_BAND_LINES', qe.count('\n'))
print('EXACT_DEFECT_ROWS', len(changes), 'ALL_OLD_IDENTITIES_PRESERVED; NEW_Q020')
print('STAGED_ONLY; COMPLETE_READBACK_AND_CANONICAL_PLACEMENT_REQUIRED')
