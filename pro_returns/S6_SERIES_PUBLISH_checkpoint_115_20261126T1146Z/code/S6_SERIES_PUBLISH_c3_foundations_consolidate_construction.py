from pathlib import Path
import csv
import datetime
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation3_foundations'
p4 = (OUT / 'S6_SERIES_PUBLISH_II_construction_P4_input.tex').read_text()
d27 = (OUT / 'S6_SERIES_PUBLISH_II_construction_D27_input.tex').read_text()

def owner(label):
    pos = p4.index('\\label{' + label + '}')
    begin = p4.rfind(r'\begin{proposition}', 0, pos)
    end = p4.index(r'\end{proof}', pos) + len(r'\end{proof}')
    return p4[begin:end]

def proof(label):
    text = owner(label)
    return text[text.index(r'\begin{proof}'):]

definition = r'''\begin{definition}[The square elliptic curve and its lattice]
\hypertarget{tag-P241}{}\label{def:II:identity-example-lattice}
\StatementRecord{def:II:identity-example-lattice}{proved}{P241}{}
Put
\[
 E=\C/(\Z+i\Z),\qquad q=e^{-2\pi},\qquad
 A=E^2,\qquad \Lambda=H_1(A;\Z)=\bigoplus_{j=1}^4\Z e_j,
\]
where $(e_1,e_2,e_3,e_4)=((1,0),(i,0),(0,1),(0,i))$.
We identify the additive and multiplicative presentations of $E$ by
the holomorphic group isomorphism
\begin{equation}
 \C/(\Z+i\Z)\longrightarrow\C^*/q^\Z,
 \qquad z\longmapsto e^{2\pi i z}.
\hypertarget{tag-0199}{}\label{cdp:eq:D.22}
\end{equation}
The lattice generators $1$ and $i$ multiply the exponential by $1$
and $q$, respectively. Homology in these torus constructions has
coefficients in $\Z$. A base meridian is counterclockwise in its
holomorphic coordinate; at infinity that coordinate is $1/t$.
\end{definition}
'''

local_statement = r'''\begin{proposition}[An elliptic bundle degeneration]\hypertarget{tag-02WG}{}\label{night:P4.1}\label{stmt:P4.1}
\StatementRecord{night:P4.1}{proved}{02WG}{\SeriesRef{def:II:identity-example-lattice}}
Take labelled copies $C=B=E$ and identify $C\times B$ with $A$
by $(z,w)\mapsto(z,w)$. Put
$V=\operatorname{Bl}_{(0,0)}(B\times\Delta)$, and let $b:V\to\Delta$
be the composition of the blowdown with the projection. Let $R$ be
the exceptional curve and put $L=\OO_V(R)$, with $L^\times$ denoting
the complement of its zero section. The holomorphic quotient
\begin{equation}
 U=L^\times/q^\Z\xrightarrow{\ p\ }V\xrightarrow{\ b\ }\Delta
\hypertarget{tag-019A}{}\label{cdp:eq:D.23}
\end{equation}
is a smooth Hausdorff threefold, proper over $\Delta$.
Its noncentral fibres are $C\times B$. Its central fibre is the reduced
union of a primary Kodaira surface and the scalar Hopf surface
$(\C^2\setminus\{0\})/q^\Z$, meeting transversally in one elliptic curve.
\end{proposition}
'''
local_proof = proof('night:P4.1')
old = '''give the holomorphic product trivialization over $\\Delta^*$.
'''
new = r'''give the holomorphic product trivialization
\begin{equation}
 U|_{\Delta^*}\simeq C\times B\times\Delta^*.
\hypertarget{tag-019B}{}\label{cdp:eq:D.24}
\end{equation}
'''
assert local_proof.count(old) == 1
local_proof = local_proof.replace(old, new)

homology_statement = r'''\begin{proposition}[Integral homology of the local degeneration]\hypertarget{tag-02X2}{}\label{night:P4.3}\label{stmt:P4.3}
\StatementRecord{night:P4.3}{proved}{02X2}{\SeriesRef{night:P4.1}}
For the degeneration $U$ of Proposition~\ref{night:P4.1}, order the
regular fibre lattice as $(a,c,b,d)$, where $(a,c)$ are the cycles
$(1,i)$ in $C$ and $(b,d)$ are the cycles $(1,i)$ in $B$.
Use the product trivialization \eqref{cdp:eq:D.24}.
The space $U$ deformation retracts onto its central fibre.
The regular-fibre inclusions induce the quotient maps
\begin{equation}
 H_1(C\times B)=\Lambda\longrightarrow\Lambda/\Z a=H_1(U),\qquad
 H_2(C\times B)=\bigwedge^2\Lambda\longrightarrow
 \bigwedge^2\Lambda/\Z(a\wedge c)=H_2(U).
\hypertarget{tag-019C}{}\label{cdp:eq:D.25}
\end{equation}
Both target groups are free. For the positive base meridian $\mu$,
the boundary inclusions satisfy
\begin{equation}
 \mu\longmapsto0\quad\text{in }H_1(U),\qquad
 x\wedge\mu\longmapsto0\quad\text{in }H_2(U)
 \quad(x\in\Lambda).
\hypertarget{tag-019D}{}\label{cdp:eq:D.26}
\end{equation}
\end{proposition}
'''
homology_proof = proof('night:P4.3')
old = '''the logarithm of the norm modulo $\\log q$. We first specify a homotopy
model for $V$.'''
new = '''the logarithm of the norm modulo $\\log q$. Orient $S^1_c$ by the
lattice period $i$, whose norm-logarithm increment is $\\log q$.
We first specify a homotopy model for $V$.'''
assert homology_proof.count(old) == 1
homology_proof = homology_proof.replace(old, new)
old = '''joining their base points by a path.

\\item The circle Chern class'''
new = r'''joining their base points by a path.

Let $B'$ be the strict transform of $B\times\{0\}$.
The inclusion $B'\cup R\hookrightarrow V$ induces an isomorphism
on fundamental groups: the point blowup preserves $\pi_1$, and
the blowdown maps $B'$ isomorphically onto $B$.
On the simply connected covers, the lift of $B'$ is contractible
and each exceptional sphere maps to the corresponding sphere
added by the blowup. The same homology comparison therefore
makes this inclusion a homotopy equivalence. A triangulation
compatible with the normal-crossings divisor $B'\cup R$ makes
the inclusion a cofibration, so it admits a strong deformation
retraction. The relative homotopy lifting property of the
principal elliptic bundle, with the identity lift on the central
fibre, gives the asserted deformation retraction of $U$.

\item The circle Chern class'''
assert homology_proof.count(old) == 1
homology_proof = homology_proof.replace(old, new)

global_statement = r'''\begin{proposition}[A simply connected compact torus fibration]
\hypertarget{tag-01GE}{}\label{cdp:st:D.2.7}
\hypertarget{tag-02WR}{}\label{night:P4.2}\label{stmt:P4.2}
\hypertarget{tag-02XD}{}\label{night:P4.4}\label{stmt:P4.4}
\hypertarget{tag-02XO}{}\label{night:P4.5}\label{stmt:P4.5}
\StatementRecord{cdp:st:D.2.7}{proved}{01GE}{\SeriesRef{night:P4.1}, \SeriesRef{night:P4.3}, \SeriesRef{cdp:st:E1}}
Let $E$, $A$ and $\Lambda$ be as in
Definition~\ref{def:II:identity-example-lattice}. Define a principal
$A$-bundle $Y_0\to\PP^1$ by the clutching translation
\begin{equation}
 a_{\rm out}=a_{\rm in}+(\ell(t),0),\qquad
 \ell(t)=\frac{\log t}{2\pi i}\pmod{\Z+i\Z}
\hypertarget{tag-019F}{}\label{cdp:eq:D.28}
\end{equation}
between a coordinate disc at zero and the exterior chart.
On disjoint discs about $0,1,\infty$, replace the product models
by the degeneration of Proposition~\ref{night:P4.1}, using the
canonical-section trivialization \eqref{cdp:eq:D.24} and the
ordered product markings, with $C_i=B_i=E$,
\begin{equation}
 \Psi_i:C_i\times B_i\longrightarrow A,\qquad
 \Psi_1(z,w)=(w,z),\quad
 \Psi_2(z,w)=(iz,iz+w),\quad
 \Psi_3(z,w)=(z,iz+w).
\hypertarget{tag-019E}{}\label{cdp:eq:D.27}
\end{equation}
These transitions define a smooth compact connected complex
threefold $f:Y\to\PP^1$ with connected fibres and
\begin{equation}
 H_1(Y;\Z)=H_2(Y;\Z)=0,\qquad
 a(Y)=1,\qquad c_3(Y)=0,\qquad b_3(Y)=2.
\hypertarget{tag-0198}{}\label{cdp:eq:D.21}
\end{equation}
Moreover $\pi_1(Y)=1$, and all integral homology groups are free,
of ranks $(1,0,0,2,0,0,1)$ in degrees zero through six.
Pullback gives the function-field isomorphism
$f^*:\mathcal M(\PP^1)\xrightarrow{\simeq}\mathcal M(Y)$.
Every smooth fibre is the fixed abelian surface $A$, and the
marked integral monodromy on $H_1(A;\Z)$ is the identity.
There are exactly three singular fibres. Each is reduced with
simple normal crossings and consists of a primary Kodaira surface
and a primary Hopf surface meeting along one smooth elliptic curve.
\end{proposition}
'''

global_proof = r'''\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item The map $\ell(t)$ in \eqref{cdp:eq:D.28} is single-valued and
holomorphic on an annulus because changing the logarithm adds an
integer. Thus it defines a holomorphic transition for a principal
$A$-bundle $Y_0$ on $\PP^1$. Its product charts make $Y_0$ smooth
and Hausdorff, and their compact fibre makes it proper over the
compact base. Hence $Y_0$ is compact.

Multiplication by $i$ preserves $\Z+i\Z$. The three inverse maps
in \eqref{cdp:eq:D.27} are
$(x,y)\mapsto(y,x)$, $(x,y)\mapsto(-ix,y-x)$ and
$(x,y)\mapsto(x,y-ix)$, respectively. Their complex matrices have
determinants $-1,i,1$, which are units in $\Z[i]$; their real
lattice determinants are one. Glue the three local models using
these maps, the canonical-section product identification, and
the local trivializations of $Y_0$. Different base points separate
in the base, and points over one base point lie in a Hausdorff
local model. The gluing is therefore Hausdorff. Properness holds
over each base chart and hence over the base; compactness of
the base implies that $Y$ is compact.

The two central components have connected elliptic fibres over
connected curves and meet each other. All remaining fibres equal
$A$, so all fibres and $Y$ are connected. The equations $uv=t$
from Proposition~\ref{night:P4.1} give precisely the three stated
singular fibres, with multiplicity one and simple normal crossings.
All changes of the marked smooth fibre are translations, so they
induce the identity on $H_1(A;\Z)$.

\item For the integral maps, write $(a_i,c_i,b_i,d_i)$ for the
images under $\Psi_i$ of the ordered local basis $(a,c,b,d)$ in
Proposition~\ref{night:P4.3}. The lattice matrices, with these
columns in the common basis $(e_1,e_2,e_3,e_4)$, are
\[
S_1=\begin{pmatrix}0&0&1&0\\0&0&0&1\\1&0&0&0\\0&1&0&0\end{pmatrix},\quad
S_2=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&-1&1&0\\1&0&0&1\end{pmatrix},\quad
S_3=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&-1&1&0\\1&0&0&1\end{pmatrix}.
\]
Put $Q_i=S_i^{-1}$. Deleting the first row of $Q_i$ gives $R_{1,i}$.
The row indices of $\bigwedge^2Q_i$ are $(ac,ab,ad,cb,cd,bd)$ and its
column indices are $(12,13,14,23,24,34)$; deleting its first row gives
$R_{2,i}$. These are the integer matrices of the local quotient maps
\eqref{cdp:eq:D.25}, with target bases $(c_i,b_i,d_i)$ and
$(a_ib_i,a_id_i,c_ib_i,c_id_i,b_id_i)$.

Let $P$ be the complement of three small open base discs and
$W=f^{-1}(P)=A\times P$. Let $s_1,s_2$ generate $H_1(P)$ and
put $s_3=-s_1-s_2$. The overlaps are $N_i=A\times S^1$.
Positive continuation of $\ell$ around zero adds $e_1$. With
\[
 g_1=e_1,\quad g_2=g_3=0,\qquad
 v_1=\binom10,\quad v_2=\binom01,\quad v_3=\binom{-1}{-1},
\]
the overlap maps into $W$, in the basis $(s_1,s_2)$ for its base
factor, are
\begin{equation}
 x\longmapsto x\quad(x\in\Lambda),\qquad
 s_i^{\rm loc}\longmapsto g_i+v_i.
\hypertarget{tag-019G}{}\label{cdp:eq:D.29}
\end{equation}
The induced maps on products of these cycles are
\begin{equation}
 x\wedge y\longmapsto x\wedge y,\qquad
 x\wedge s_i^{\rm loc}\longmapsto x\wedge g_i+x\otimes v_i.
\hypertarget{tag-019H}{}\label{cdp:eq:D.30}
\end{equation}
They include the degree-two contribution of the clutching
translation, with fibre cycles preceding the base cycle.

\item Use the ordered basis $(e_1,e_2,e_3,e_4,s_1,s_2)$ for $H_1(W)$
and append the three bases $(c_i,b_i,d_i)$ for the local groups.
On the source concatenate the three bases
$(e_1,e_2,e_3,e_4,s_i^{\rm loc})$. The $15\times15$
Mayer--Vietoris matrix $F_1$ has, in its $i$th five-column block,
upper block
\[
 \begin{pmatrix}I_4&g_i\\0_{2\times4}&v_i\end{pmatrix}
\]
and local block $(-R_{1,i},0)$ in the $i$th summand; its other local
blocks vanish. The sign is the difference of the two inclusions.

For $H_2(W)$ use
\[
 (12,13,14,23,24,34,e_1s_1,\ldots,e_4s_1,e_1s_2,\ldots,e_4s_2)
\]
and append the three local five-element bases. The source is the
concatenation of
$(12,13,14,23,24,34,e_1s_i^{\rm loc},\ldots,e_4s_i^{\rm loc})$.
The $29\times30$ matrix $F_2$ has top six rows
$[I_6,(e_j\wedge g_i)_{j=1}^4]$ in its $i$th block; its next eight
rows have the coefficients of $e_j\otimes v_i$ in the displayed
order, and its $i$th local block is $[-R_{2,i},0]$. All other blocks
vanish, by \eqref{cdp:eq:D.26}. Finally
\[
 F_0=\begin{pmatrix}1&1&1\\-1&0&0\\0&-1&0\\0&0&-1\end{pmatrix}
\]
has zero kernel. Thus the relevant exact sequence is
\[
 \Z^{30}\xrightarrow{F_2}\Z^{29}\longrightarrow H_2(Y)
 \longrightarrow\Z^{15}\xrightarrow{F_1}\Z^{15}\longrightarrow H_1(Y)
 \longrightarrow\Z^3\xrightarrow{F_0}\Z^4.
\]

\item Eliminate the local $H_1$ groups and two independent base
meridians. The remaining quotient is
\begin{equation}
 H_1(Y;\Z)=\Lambda/\langle e_1,a_1,a_2,a_3\rangle=0.
\hypertarget{tag-019I}{}\label{cdp:eq:D.31}
\end{equation}
Indeed its relation matrix is
\[
 R_{H_1}=\begin{pmatrix}1&0&0&1\\0&0&1&0\\0&1&0&0\\0&0&1&1\end{pmatrix},
 \qquad\det R_{H_1}=-1.
\]
Since $F_1$ has equal source and target rank fifteen, its integral
surjectivity makes it an isomorphism. Its kernel contributes
nothing to $H_2(Y)$.

In degree two, the pure fibre columns eliminate the fifteen local
generators, leaving the three relations $\eta_i=a_i\wedge c_i$.
The second meridian columns kill $\Lambda\otimes s_2$, the third
then kill $\Lambda\otimes s_1$, and the first leave
$e_1\wedge\Lambda$. Hence
\begin{equation}
 H_2(Y;\Z)=
 \frac{\bigwedge^2\Lambda}
 {e_1\wedge\Lambda+\Z\eta_1+\Z\eta_2+\Z\eta_3}=0.
\hypertarget{tag-019J}{}\label{cdp:eq:D.32}
\end{equation}
The six relations in the order
$e_{12},e_{13},e_{14},\eta_1,\eta_2,\eta_3$ have matrix
\[
R_{H_2}=\begin{pmatrix}
1&0&0&0&1&1\\0&1&0&0&0&-1\\0&0&1&0&1&0\\
0&0&0&0&-1&0\\0&0&0&0&0&-1\\0&0&0&1&1&1
\end{pmatrix},\qquad \det R_{H_2}=1.
\]
Thus $F_2$ is surjective over $\Z$, including all integral torsion.
In the ordered bases above, $\det F_1=-1$, and the Smith normal
forms of $F_1$ and $F_2$ have fifteen and twenty-nine unit invariant
factors, respectively. The relation matrix $R_{H_2}$ also has only
unit invariant factors. The programs are listed in
\cref{tab:II:programs}.

\item The local pushout in Proposition~\ref{night:P4.3} gives
$\pi_1(U_i)=\Lambda/\Z a_i$, and the marked meridian is trivial.
For van Kampen, choose based positive meridians with
$s_1s_2s_3=1$ in $\pi_1(P)$. Write
$\pi_1(W)=\Lambda\times F(s_1,s_2)$, and denote the image of
$x\in\Lambda$ by $t_x$, so $t_xt_y=t_{x+y}$ and each $t_x$
commutes with the two base generators. The boundary maps impose
\[
 t_{a_1}=t_{a_2}=t_{a_3}=1,\qquad
 t_{e_1}s_1=1,\quad s_2=1,\quad (s_1s_2)^{-1}=1.
\]
Thus $s_1=s_2=t_{e_1}=1$. The same unimodular relation matrix
$R_{H_1}$ kills the fibre lattice, proving $\pi_1(Y)=1$.

\item The regular fibre has Euler number zero. Both components of
each special fibre are elliptic bundles over compact curves, and
their intersection is elliptic, so additivity gives zero for each
special support. Stratifying the base and applying multiplicativity
to the smooth bundle gives $e(Y)=0$. The Euler class of the real
bundle underlying a complex rank-three tangent bundle is its top
Chern class with the complex orientation. Hence $c_3(Y)=0$.
Duality and \eqref{cdp:eq:D.31}--\eqref{cdp:eq:D.32} give
$b_4=b_5=0$ and $e(Y)=2-b_3$, so $b_3=2$.
Integral duality and the universal coefficient theorem identify
the torsion of $H_3$ with that of $H_2$, which is zero. They also
give $H_4=H_5=0$, while connectedness and the complex orientation
give $H_0=H_6=\Z$. This proves all the stated integral homology
groups.

\item The universal coefficient theorem gives
$H^1(Y;\Z)=H^2(Y;\Z)=0$. The smooth fibre $A=E^2$ is K\"ahler,
and the constructed $f$ is a proper surjection with connected
fibres from a smooth compact connected threefold. Apply
Proposition~\ref{cdp:st:E1} to this same $f$: every effective
divisor is vertical, and pullback identifies the function fields
through $f^*:\mathcal M(\PP^1)\xrightarrow{\simeq}\mathcal M(Y)$.
Consequently $a(Y)=1$.
\end{enumerate}
\end{proof}
'''

basis_remark = r'''\begin{remark}[Integral coordinates for the quotient maps]
\hypertarget{tag-P214}{}\label{rem:II:torus-quotient-coordinates}
\StatementRecord{rem:II:torus-quotient-coordinates}{proved}{P214}{\SeriesRef{cdp:st:D.2.7}}
For a vector $v\in\Z^n$ with a coordinate equal to $\pm1$, let
$p$ be its first such coordinate and define
\[
 Q_v(x)=\bigl(x_j-(v_j/v_p)x_p\bigr)_{j\ne p},
\]
with the remaining coordinates in their original order. This is
the coordinate quotient by $\Z v$: its kernel is $\Z v$, and
inserting zero in coordinate $p$ gives a right inverse.
For the vectors $a_i$ and $\eta_i=a_i\wedge c_i$ in
Proposition~\ref{cdp:st:D.2.7}, put
$\widehat R_{1,i}=Q_{a_i}$ and $\widehat R_{2,i}=Q_{\eta_i}$,
using the lexicographic exterior-square basis. The exact changes
to the quotient coordinates $R_{1,i},R_{2,i}$ used in its proof are
\[
 R_{1,i}=M_{1,i}\widehat R_{1,i},\qquad
 R_{2,i}=M_{2,i}\widehat R_{2,i},
\]
where
\[
 M_{1,1}=\begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix},\quad
 M_{1,2}=\begin{pmatrix}-1&0&0\\-1&1&0\\0&0&1\end{pmatrix},\quad
 M_{1,3}=\begin{pmatrix}1&0&0\\1&1&0\\0&0&1\end{pmatrix}
\]
have determinants $1,-1,1$, respectively, and for $y\in\Z^5$,
\[
\begin{aligned}
 M_{2,1}y&=(-y_2,-y_4,-y_3,-y_5,y_1),\\
 M_{2,2}y&=(y_3,y_4,-y_1,-y_2,-y_2+y_3+y_5),\\
 M_{2,3}y&=(y_1,y_2,y_3,y_4,y_1+y_4+y_5).
\end{aligned}
\]
Their determinants are $-1,1,1$, respectively. These identities
follow by applying the displayed maps to the basis vectors, using
$R_{1,i}$ from $S_i^{-1}$ and $R_{2,i}$ from
$\bigwedge^2S_i^{-1}$. Thus all six changes are integral
isomorphisms.

Let $\widehat F_1,\widehat F_2$ use these $Q_v$ target coordinates,
with the same source and exterior target bases as $F_1,F_2$.
The signed inclusion maps then give the identities
\[
\begin{aligned}
 F_1&=\operatorname{diag}(I_6,M_{1,1},M_{1,2},M_{1,3})\widehat F_1,\\
 F_2&=\operatorname{diag}(I_{14},M_{2,1},M_{2,2},M_{2,3})\widehat F_2.
\end{aligned}
\]
In particular $\det\widehat F_1=+1$, while $\det F_1=-1$,
and the two coordinate choices have the same Smith invariant
factors in each degree.
\end{remark}
'''

parts = [definition, local_statement + local_proof,
         homology_statement + homology_proof,
         global_statement + global_proof, basis_remark]
receiving = '\n\n'.join(parts) + '\n'
output = OUT / 'S6_SERIES_PUBLISH_II_single_torus_construction.tex'
output.write_text(receiving)
for stem, part in zip(('P241', 'P41', 'P43', 'global', 'basis_remark'), parts):
    (OUT / f'S6_SERIES_PUBLISH_II_single_torus_{stem}.tex').write_text(part + '\n')

# Every original owner label and hypertarget is transported, never recreated
# as a second numbered construction. No old manual equation tag is introduced.
old_labels = set(re.findall(r'\\label\{([^}]+)\}', d27 + p4))
old_targets = set(re.findall(r'\\hypertarget\{([^}]+)\}', d27 + p4))
new_labels = re.findall(r'\\label\{([^}]+)\}', receiving)
new_targets = re.findall(r'\\hypertarget\{([^}]+)\}', receiving)
assert old_labels.issubset(new_labels), old_labels - set(new_labels)
assert old_targets.issubset(new_targets), old_targets - set(new_targets)
assert len(new_labels) == len(set(new_labels))
assert len(new_targets) == len(set(new_targets))
assert r'\tag{' not in receiving
assert receiving.count(r'S_1=\begin{pmatrix}') == 1
assert receiving.count(r'R_{H_1}=\begin{pmatrix}') == 1
assert receiving.count(r'R_{H_2}=\begin{pmatrix}') == 1
assert len(re.findall(r'\\begin\{(?:proposition|definition|remark)\}', receiving)) == 5

source = (ROOT / 'S6_SERIES_PUBLISH_II.tex').read_text()
def extract_current(label, env):
    position = source.index('\\label{' + label + '}')
    start = source.rfind('\\begin{' + env + '}', 0, position)
    end_tag = r'\end{proof}' if env == 'proposition' else '\\end{' + env + '}'
    end = source.index(end_tag, position) + len(end_tag)
    return source[start:end]

p213 = extract_current('rem:II:extended-torus-groups', 'remark')
d28 = extract_current('cdp:st:D.2.8', 'proposition')
assert p213.count('\\Z w') == 1 and p213.count('$w\\ne0$') == 1 and p213.count('kills $w$') == 1
new_p213 = p213.replace(r'\cref{cdp:st:D.2.7}', r'\cref{night:P4.1}').replace(r'\Z w', r'\Z a').replace(r'$w\ne0$', r'$a\ne0$').replace('kills $w$', 'kills $a$')
assert d28.count('w_i') == 2
new_d28 = d28.replace('w_i', 'a_i')
old_retraction = '''threefold. A local filling $U_i$ retracts onto its central
fibre $S_i$: the retraction of the blown-up base onto
$B_0\\cup R$ lifts through its principal compact torus
bundle, by the homotopy lifting property. Therefore \\eqref{cdp:eq:D.25}
identifies'''
new_retraction = r'''threefold. The deformation retraction of a local filling $U_i$
onto its central fibre $S_i$ in Proposition~\ref{night:P4.3},
together with \eqref{cdp:eq:D.25}, identifies'''
assert new_d28.count(old_retraction) == 1
new_d28 = new_d28.replace(old_retraction, new_retraction)
old_record = re.search(r'\\StatementRecord\{[^\n]+', new_d28).group()
new_record = old_record[:-1] + r', \SeriesRef{night:P4.3}}'
new_d28 = new_d28.replace(old_record, new_record, 1)

guards = [
    dict(key='earlier_common_construction', old=d27.rstrip('\n'), new=receiving.rstrip('\n'),
         reason='Replace the earlier D.2.7 owner by the single earlier P241/local geometry/local homology/global result/basis-conversion unit. All original construction labels and tags occur once.'),
    dict(key='remove_later_duplicate_subsection', old=p4, new='',
         reason='Move every mathematical owner from the later duplicate subsection to the earlier common construction unit. Its global result labels P4.2/P4.4/P4.5 are aliases of D.2.7, with all stronger conclusions retained.'),
    dict(key='P213_exact_local_cycle_name', old=p213, new=new_p213,
         reason='The same local killed cycle is called a in the receiving local owner (old w=a under the identity E marking). Point the local filling directly to P4.1; the exact obstruction map and all hypotheses are unchanged.'),
    dict(key='D28_exact_global_cycle_names', old=d28, new=new_d28,
         reason='Each old w_i is exactly the first column a_i of the same integral marking S_i. Both annihilator occurrences change names. The retraction is proved once at earlier P4.3 and cited here; all equations, tags, statement hypotheses, coefficient maps and other proof inferences remain unchanged.'),
]
(OUT / 'S6_SERIES_PUBLISH_torus_consolidation_guards.json').write_text(json.dumps(guards, ensure_ascii=False, indent=2) + '\n')
(OUT / 'S6_SERIES_PUBLISH_II_torus_P213_receiving.tex').write_text(new_p213 + '\n')
(OUT / 'S6_SERIES_PUBLISH_II_torus_D28_receiving.tex').write_text(new_d28 + '\n')
print('One construction unit:', len(receiving.splitlines()), 'lines;', len(old_labels), 'old labels and', len(old_targets), 'old hypertargets preserved; 4 integration/consumer guards. New tag P214.')
