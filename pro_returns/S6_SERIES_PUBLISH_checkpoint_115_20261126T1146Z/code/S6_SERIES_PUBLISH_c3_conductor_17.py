#!/usr/bin/env python3
"""Prepare the full weighted-cycle consolidation; never mutate central files."""
from pathlib import Path
from collections import Counter
import csv,re,hashlib
root=Path(__file__).resolve().parents[1]
out=root/'agents/continuation3_conductor'
stem='S6_SERIES_PUBLISH_c3_conductor_17'
current=(root/'S6_SERIES_PUBLISH_II.tex').read_text()
def block(text,label,env):
 p=text.index(r'\label{'+label+'}');a=text.rfind(r'\begin{'+env+'}',0,p);b=text.index(r'\end{proof}',p)+len(r'\end{proof}');return text[a:b]
def freeze(name,text):
 p=out/(stem+'_'+name+'.tex')
 if p.exists():assert p.read_text()==text,name
 else:p.write_text(text,newline='\n')
original={n:(out/f'S6_SERIES_PUBLISH_c3_conductor_tail_UN{n}_input.tex').read_text() for n in (52,56,59)}
for n,s in original.items():
 assert block(current,f'cdp:st:C.2.UN.{n}','proposition')==s,n
 freeze(f'UN{n}_input',s)
p333=block(current,'lem:II:moving-marked-cycle','lemma');freeze('P333_input',p333)
un48=block(current,'cdp:st:C.2.UN.48','proposition');freeze('UN48_input',un48)
with (root/'agents/continuation2_B/D19/S6_SERIES_PUBLISH_II_B2_D19_v1_equation_map.tsv').open() as f:
 established={r['old_tag']:r['target_label'] for r in csv.DictReader(f,delimiter='\t') if r['old_tag']}
equations={}
for s in original.values():
 for m in re.finditer(r'\\\[.*?\\\]',s,re.S):
  tags=re.findall(r'\\tag\{([^}]+)\}',m.group())
  if tags:assert len(tags)==1;equations[tags[0]]=m.group()
used=[];alias_maps=[]
aliases={
 'C.EW.1': [('C.WH.4','Set a=gA,b=gB,N=gABh. The same uv=s^h,x=u^B,y=v^A normalization is WH4; EW1 also displays the identical t=s^N=x^a y^b.')],
 'C.EW.17':[('C.WH.12','J_axis is the pointwise axis stabilizer J of WH12. The same subgroup of order h and residual independent B,A characters give the identical invariant ring and t equation.')],
 'C.EW.4':[('C.WH.7','The same u=-sum h_j n_j is written d p, with d the former primitive divisor delta.'),('C.WM.9','The same weighted normal sum is displayed here; its nonzero transverse height is stated and proved immediately with this formula.')],
 'C.EW.3':[('C.WH.9','Set R=I, so n_sigma(j)=n_j and -l_j 2pi i/N=h_j n_j/N. Both overlap and order equations are exactly WH9.')]
}
def eq(key):
 key='C.'+key if not key.startswith('C.') else key
 s=equations[key];assert re.search(r'\\label\{([^}]+)\}',s).group(1)==established[key]
 s=s.replace(r'\[',r'\begin{equation}',1);s=s[:-2]+r'\end{equation}';s=s.replace(r'\tag{'+key+'}','');used.append(key)
 targets=[];labels=[]
 for alias,mapping in aliases.get(key,[]):
  old=equations[alias];tag=re.search(r'\\hypertarget\{([^}]+)\}',old).group(1);label=established[alias]
  targets.append(r'\hypertarget{'+tag+r'}{}');labels.append(r'\label{'+label+'}');used.append(alias)
  alias_maps.append(dict(old_tag=alias,target_label=label,owner_tag=key,map=mapping))
 if labels:s=s.replace(r'\end{equation}','\n'+'\n'.join(targets)+'\n'+r'\SsixEquationAliases{'+''.join(labels)+'}\n'+r'\end{equation}')
 if key in ('C.WH.1','C.WH.2','C.WH.3','C.WM.2','C.WM.4'):
  s=s.replace(r'\mathcal L',r'\mathcal N')
 if key in ('C.WH.1','C.WH.2','C.WH.6'):s=s.replace('H_i','V_i').replace('H_{i+1}','V_{i+1}')
 if key=='C.WM.1':s=s.replace('L_i',r'\mathcal L_i')
 if key in ('C.WM.3','C.WM.6'):s=s.replace("L'",r"\mathcal L'").replace(r'\pi^*L',r'\pi^*\mathcal L').replace(r'\oplus L)',r'\oplus\mathcal L)')
 if key.startswith('C.EW.'):
  s=s.replace('b_j',r'\mathbf b_j').replace(r'b_{\sigma j}',r'\mathbf b_{\sigma j}')
 if key=='C.WH.10':s=s.replace(r'\delta','d')
 return re.sub(r'\n[ \t]*\n+','\n',s)
def render(s):return re.sub(r'@@([A-Z]+\.\d+)@@',lambda m:eq(m.group(1)),s)

needle='The assertion about moving data assumes $M=I$ at the central value.'
assert p333.count(needle)==1
p333new=p333.replace(needle,needle+r'''

For fixed positive integers $h_i$, the same constructed marked
component neighbourhoods admit the compressed equations
$xy=t^{h_i}$ at their edges. They give a proper normal threefold
over $\Delta$, with the same reduced central surface and marked
maps. A neck has the transverse surface singularity $A_{h_i-1}$;
its resolution inserts $h_i-1$ degree-zero ruled elliptic
components. For fixed data its nearby fundamental group is
\eqref{cdp:eq:C.HC.7}. When $M=I$, the complete fixed or moving
punctured family is the coframe quotient with periods
\begin{equation}\label{eq:II:compressed-moving-cycle-periods}
 \Lambda(t)+\Z\left(b(t)+\frac{\log t}{2\pi i}u_h(t)\right),
 \qquad b(t)=\sum_i\mathbf b_i(t),\qquad
 u_h(t)=-\sum_i h_i n_i(t).
\end{equation}
The moving hypotheses and integer transport are the ones above.
The case $h_i=1$ for every edge is the smooth construction already
stated.''',1)
extra=r'''

For the compressed clause use exactly the same component families,
normal-line maps and metrics. Replace an edge chart by $xy=t^{h_i}$;
on its $x$-end the inverse inserts $y=t^{h_i}/x$, and on its
$y$-end it inserts $x=t^{h_i}/y$. Choose the same four radii
$r_0<r_1<R_1<R_0$ and a closed base radius $\delta$ with
$\delta^{h_i}<r_0^2$ for every edge. Then both attaching ends
cannot meet. An open-core point with normal norm between $r_0$
and $r_1$ has its other neck norm at most
$\delta^{h_i}/r_0<r_0$; a neck point beyond $R_1$ lies in
the same closed component core as before. Thus the identical
closed-graph and finite compact-cover maps prove Hausdorffness
and properness, including for the moving components.

The transverse hypersurface $xy=t^{h_i}$ is normal: it is a
two-dimensional hypersurface smooth away from the origin, hence
regular in codimension one and Cohen--Macaulay. Its resolution
has the following $h_i$ charts $(a_j,b_j)$:
\begin{equation}\label{eq:II:compressed-neck-resolution}
 t=a_jb_j,\qquad x=t^j a_j,\qquad
 y=t^{h_i-j-1}b_j,\qquad 0\le j<h_i.
\end{equation}
The adjacent transition is $a_{j+1}=b_j^{-1}$,
$b_{j+1}=t b_j=a_jb_j^2$. To prove properness, take the closure
of the graph of
$([x:t],[x:t^2],\ldots,[x:t^{h_i-1}])$ in the product of the
hypersurface with $(\PP^1)^{h_i-1}$. In chart $j$ its $k$th
coordinate is $[t^{j-k}a_j:1]$ for $k\le j$ and
$[1:t^{k-j-1}b_j]$ for $k>j$. These formulas extend the
graph map and cover its closure; conversely its consecutive
finite ratio coordinates recover $a_j=x/t^j$ and
$b_j=t^{j+1}/x$ with their displayed regular extensions.
Thus the charts describe that proper graph closure. For
$h_i=1$ the product of projective lines is empty and the
single chart is the identity $x=a_0$, $y=b_0$, $t=a_0b_0$.
For $h_i>1$, over the
origin their zero axes glue by the stated reciprocal transition
to a chain of $h_i-1$ projective lines, and there are no other
exceptional curves. The constant factors of the two normal lines
glue these monomial charts over the elliptic curve. Their inserted
components are projective completions of degree-zero lines,
with two marked sections.
Every resolved central branch has multiplicity one because
$t=a_jb_j$. The resolution is an isomorphism for $t\ne0$.

Each inserted ruled complement has opposite incoming and outgoing
normal meridians. Composing its edge maps gives the same compressed
linear map, while the $h_i$ logarithmic terms sum to
$-h_i n_i(t)\log t/(2\pi i)$. Apply the smooth construction above
to this resolved marked cycle, with those very component and edge
maps. It gives the same injected lattice presentation and coframe
isomorphism on the unchanged nearby fibre. Composing the resolution
isomorphism for $t\ne0$ with that coframe map yields exactly
\eqref{eq:II:compressed-moving-cycle-periods}. The accumulated-edge
coordinate maps and their holomorphic inverses are the previous
ones with each term multiplied by $h_i$; a logarithm change adds
the integral vector $u_h(t)$. This proves the entire compressed
family comparison on its constructed marked neighbourhoods.
'''
assert p333new.endswith(r'\end{proof}')
p333new=p333new[:-len(r'\end{proof}')]+extra+r'\end{proof}'
un48oldpart=r'''Its resolution has charts $(u_j,v_j)$, $0\le j<d$, with
\[
 x=u_j^{j+1}v_j^j,\qquad
 y=u_j^{d-j-1}v_j^{d-j},\qquad s=u_jv_j,
\]
and adjacent gluing $u_{j+1}=v_j^{-1}$, $v_{j+1}=u_jv_j^2$. These maps are isomorphisms off the node and insert the chain of $d-1$ projective lines between its two branches. Their central equations are $u_jv_j=0$, so together with the original component they give the $I_d$ fibre.'''
assert un48.count(un48oldpart)==1
un48new=un48.replace(un48oldpart,r'''Apply the resolution in
\cref{lem:II:moving-marked-cycle} with $h_i=d$, $t=s$ and
the same $x,y$. Its chart map
\eqref{eq:II:compressed-neck-resolution}, with
$(a_j,b_j)=(u_j,v_j)$, is
$x=u_j^{j+1}v_j^j$, $y=u_j^{d-j-1}v_j^{d-j}$ and $s=u_jv_j$.
It inserts the same chain of $d-1$ projective lines between the
two node branches. Together with the original component its
reduced central equations give the $I_d$ fibre.''',1)
un48new=un48new.replace(r'\end{proposition}',r'''
The pencil, Tate and suspension construction used here is defined
for every $q_0,a\in\C^*$ with $0<|q_0|<1$, $a\ne1$, and
every integer $d\ge1$. It gives a smooth compact suspension
\eqref{cdp:eq:C.HG.10} over $\PP^1$, whose elliptic-surface
factor has the selected $I_d$ fibre and a section of central
group coordinate $a$. Its selected punctured periods are
\eqref{cdp:eq:C.HG.11}; its general fibre is a connected
two-torus and every reduced support has Euler number zero.
\end{proposition}''',1)
un48new=un48new.replace('Form the suspension\n',r'''The construction from the nodal cubic onward uses only
$0<|q_0|<1$, $a\ne0,1$ and $d\ge1$. It therefore also
proves the stated arbitrary-parameter clause. Form the suspension
''',1)

definition=render(r'''\subsection{Weighted normal data on marked cycles}\label{subsec:II:weighted-cycle-data}

\begin{definition}[Weighted normal data on an oriented marked cycle]\hypertarget{tag-P355}{}\label{def:II:weighted-normal-cycle}
\StatementRecord{def:II:weighted-normal-cycle}{proved}{P355}{\cref{def:II:marked-normal-cycle}}
Let $S=\bigcup_i V_i$ be a compact simple normal-crossing oriented
cycle with at least two smooth embedded components, and with
every edge joining distinct components. Each $V_i$ is a diagonal
primary or secondary Hopf surface with its two marked axes,
or a surface
@@WM.1@@
with its zero and infinity sections. The maps
$\phi_i:C_i^+\to C_{i+1}^-$ identify the outgoing and incoming
marked elliptic curves. Fix positive component multiplicities
$m_i$. Weighted normal data consist of holomorphic lines
$\mathcal N_i$ on $V_i$, sections
@@WH.1@@
and the line isomorphisms
@@WH.2@@
whose leading section coefficients agree on each edge.
Equivalently these coefficients give the same trivialization of
$N_{C_i^+/V_i}^{m_{i+1}}\otimes
 \phi_i^*N_{C_{i+1}^-/V_{i+1}}^{m_i}$.
The data include every nonzero constant in these line maps.
Here $\mathcal L_i$ is the degree-zero ruling line, and
$\mathcal N_i$ is the weighted normal line.

A holomorphic function on a smooth threefold with full fibre
$\sum_i m_iV_i$ and this marked support induces these data.
In local coordinates $x=0$ for $V_i$ and $y=0$ for $V_{i+1}$,
their edge function is $x^{m_i}y^{m_{i+1}}$ after absorbing a unit.
\end{definition}
\begin{proof}
Take $\mathcal N_i=\OO_Y(V_i)|_{V_i}$. Divide the defining
function by the $m_i$th power of the canonical divisor section
and restrict to $V_i$. This gives \eqref{cdp:eq:C.WH.1}.
At a double curve the two divisor sections identify each
restricted ambient normal with the normal of that curve in
the other component, giving \eqref{cdp:eq:C.WH.2}. Their
product is the same defining function, so their leading
coefficients give the stated single weighted trivialization.
A local holomorphic root of its unit gives the displayed
edge equation. These constructions commute with the given
elliptic identifications.
\end{proof}
''')

root_owner=render(r'''\subsection{Root covers and inertia of weighted cycles}\label{subsec:II:weighted-cycle-roots}

\begin{lemma}[Weighted cycle plumbing, root maps and inertia]\hypertarget{tag-P356}{}\label{lem:II:weighted-cycle-roots}
\StatementRecord{lem:II:weighted-cycle-roots}{proved}{P356}{\cref{def:II:weighted-normal-cycle,def:II:marked-normal-cycle,lem:II:moving-marked-cycle,lem:II:normal-product-collars}}
Every datum in \cref{def:II:weighted-normal-cycle} gives a
smooth proper local plumbing with full central fibre
$\sum_i m_iV_i$. Set $N=\operatorname{lcm}_i m_i$.
Its normalized base change $t=s^N$ has strict component covers
@@WH.3@@
of total degree $m_i$. At an edge put
$a=m_i$, $b=m_{i+1}$, $g=\gcd(a,b)$,
$A=a/g$, $B=b/g$ and $h=N/\operatorname{lcm}(a,b)$.
Its $g$ local branches have the finite normalization maps
@@EW.1@@
after choosing their constant roots of unity. A connected
strict cover of a Hopf component is a smooth marked diagonal
Hopf surface, and has the same algebraic dimension as that
component. Its two inverse axes are connected.

At a ruled vertex of multiplicity $m$, with neighbouring
multiplicities $a,b$, one has
@@WM.2@@
Every connected strict cover is a marked
$\PP(\OO_{E'}\oplus\mathcal L')$, with a finite \'{e}tale
elliptic base map $\pi:E'\to E$ and a line isomorphism
@@WM.3@@
Its fibre map has degree $q$ and ramification $q$ along each
marked section.

The root support graph is a union of cycles; resolving a
compressed edge inserts $h-1$ degree-zero ruled elliptic
components. Its graph is connected exactly when the nearby
fibre is connected. On a connected graph let $M$ be the
product of its integral complement-lattice maps. Then
@@WH.5@@
with the displayed lattice injected. For $M=I$ the complete
coframe map identifies the nearby fibre with a two-torus.
For a given smooth-total degeneration with this full weighted
support, the same root maps and the same fundamental-group
comparison apply.

For a connected root graph there is one integer $r$ such that,
for each connected strict cover $E_i$ of $V_i$,
@@WH.6@@
There are $r$ strict covers over each component. Write
$g_i=\gcd(m_i,m_{i+1})$ and
$h_i=N/\operatorname{lcm}(m_i,m_{i+1})$.
Each connected axis cover is \'{e}tale of degree $g_i/r$.
The common strict-component stabilizer $K$ and generic
component inertias $I_i$ satisfy
@@WH.0@@
At a ruled vertex the base degree is $\gcd(m,a)/r$.

These same characters determine the local quotient of every
constructed moving compressed root plumbing with its finite
root action, base rotation $s\mapsto\zeta_Ns$, and the same
central component, branch and inertia maps. Its quotient is
smooth near the central fibre and has precisely the full
multiplicities $m_i$.
\end{lemma}
\begin{proof}
On a diagonal Hopf component the $m_i$th power of
$\mathcal N_i$ is the inverse of the boundary divisor line.
The two marked axes have constant factors of automorphy in
their diagonal quotient, so this power has a flat holomorphic
connection. Transfer it through \eqref{cdp:eq:C.WH.1}.
In a local frame divide its connection form by $m_i$; the
frame-change formula divides as well. This gives a flat
holomorphic connection on $\mathcal N_i$. Each entire axis
chart is the total space of its degree-zero normal line and
retracts to the axis. The flat line there has the same
monodromy as the pullback of its axis restriction, giving
the required holomorphic line isomorphism.

For a ruled vertex $R=\PP(\OO_E\oplus\mathcal L)$, write
@@WM.4@@
Restriction to a ruling fibre gives
$m\deg(\mathcal N|_{\PP^1})=-(a+b)$. Thus $m\mid a+b$,
$b\equiv-a\pmod m$, and both gcds and the number $q$ in
\eqref{cdp:eq:C.WM.2} follow. On either entire section chart,
the removed divisor is trivial and the remaining zero-section
divisor is pulled back from its degree-zero normal line.
Consequently $\mathcal N^m$ is flat on that chart. Dividing
the transferred connection by $m$, and comparing monodromy
under the chart retraction, identifies $\mathcal N$ there
with its axis pullback. Globally, if
$d_0=\deg(\mathcal N|_{\PP^1})$, then
$\mathcal N\otimes\OO_R(-d_0C^+)$ is trivial on every
ruling fibre. Its direct image is a line $A_0$ on $E$;
fibrewise evaluation is an isomorphism by proper base change
and Nakayama. Hence
$\mathcal N=\OO_R(d_0C^+)\otimes\pi_R^*A_0$.
Equation \eqref{cdp:eq:C.WM.4} and the degree-zero class of
$C^--C^+$ give $\deg A_0=0$. This also describes the same
local pullback maps. The $m_i$th tensor of each parallel
identification agrees with the divisor-line identification
up to a constant. Fix that constant by the leading coefficient
of $\sigma_i$ and choose its $m_i$th root in the line map.
Then on each entire axis chart $\sigma_i$ is exactly that
leading coefficient times the indicated power of the normal
coordinate. Thus the chart comparison also preserves the
full functions used below.

On a component core use the total line $\mathcal N_i$ and
the function $\sigma_i(v^{m_i})$. On each edge use the two
lines of \eqref{cdp:eq:C.WH.2} and their function
$x^{m_i}y^{m_{i+1}}$, where $x$ is normal to $V_i$.
The entire chart maps just proved identify these functions
exactly. Choose the flat metrics through the weighted
trivialization, with bounded component normal norms. The
two ends of an edge cannot meet when both attaching norms
exceed $r_0$ and $|t|<r_0^{m_i+m_{i+1}}$.
Use the same four radii and finite closed-core/closed-neck
cover as \cref{lem:II:moving-marked-cycle}; choose the base
radius smaller than all these weighted bounds. On an
attaching annulus one norm is bounded below, so the equation
bounds the other by the corresponding positive root of
$|t|$. The same maps and closed-graph argument give a
Hausdorff proper space. Core line bundles and edge normal
bundles are smooth; the function has exactly the stated
central multiplicities and is a submersion off zero.

On the normalized root of a component core the formula
$\xi=s^{N/m_i}/v$ gives \eqref{cdp:eq:C.WH.3}, with root
generator $\xi\mapsto\zeta_N^{N/m_i}\xi$. For an edge,
$(x^Ay^B)^g=s^{gABh}$ first gives its $g$ branches. On one
branch the map in \eqref{cdp:eq:C.EW.1} is finite and is
one-to-one off $xy=0$: coprimality of $A,B$ makes the choices
$u^B=x$, $v^A=y$, $uv=s^h$ unique. Its source is the normal
surface $A_{h-1}$ times the axis. Thus this is its finite
normalization; the maps glue by uniqueness of normalization.

The open part of a connected Hopf root component is the
finite-index lattice cover
$\C^2/\Lambda_i'\to\C^2/\Lambda_i$. Let $q_+,q_-$ be
the least positive angular multiples in $\Lambda_i'$.
The local equations $\xi^{m_i}=z^{m_{i+1}}$ and its incoming
version give $q_+=m_i/\gcd(m_i,m_{i+1})$ and the analogous
$q_-$. Divide the two logarithmic coordinates by these
integers and exponentiate. The resulting deck group contains
a contraction and the standard two angular periods. A finite
element fixing a nonzero axis point would give a smaller
positive angular multiple, contradicting the definition of
$q_\pm$. Its quotient is therefore a smooth marked primary
or secondary diagonal Hopf surface. The coordinate-power map
$(z,w)\mapsto(z^{q_+},w^{q_-})$ is equivariant, finite on
compact quotients and equal to the open lattice cover.
Uniqueness of finite normalization identifies it with this
root component, including its two connected axes.
Algebraic dimension is preserved: pullback injects meromorphic
function fields, and multiplication by a meromorphic function
on the finite direct-image module, locally after clearing poles,
gives its monic characteristic polynomial. Its coefficients
glue meromorphically on the base. Thus the field extension
is algebraic and the transcendence degrees are equal.

For a ruled root component remove its sections. Its open group
is $\mathcal L^\times=\C^2/\Lambda$, with primitive normal
$n\in\Lambda$. For its finite-index sublattice $\Lambda'$,
let $q$ be least with $qn\in\Lambda'$. Projection gives
@@WM.5@@
The projected rank-two lattices are discrete of finite index,
so this is an \'{e}tale elliptic cover. Its kernel in the open
group is $\C n/\Z qn\simeq\C^*$. Logarithmic base lifts
give constant factors for a degree-zero line $\mathcal L'$.
The open finite map is $z\mapsto z^q$ on this kernel;
exponentiating the two base lifts gives precisely
\eqref{cdp:eq:C.WM.3}. It extends by the homogeneous power map to
@@WM.6@@
This is finite, has ramification $q$ on both sections and agrees
with the root cover on its dense open group. Its source is smooth
and normal, so finite-normalization uniqueness identifies it
with the strict root component. The two local equations give
the stated common $q$. The lattice index is
@@WM.7@@
where the second factor is the base degree.

Every strict component now has two connected inverse marked
curves, so the root graph is a union of cycles. Apply the
compressed clause of \cref{lem:II:moving-marked-cycle} with
these component maps and the exponents $h_i$ in
\eqref{cdp:eq:C.EW.1}. Its resolution inserts exactly $h_i-1$
degree-zero ruled elliptic components; the full resolved fibre
is reduced. In its proper Stein factor, a connected central
support has one point above zero, and reducedness forces the
local base multiplicity to be one. Its finite map to the disc
therefore has degree one. Applied on each connected graph,
this proves the connectedness assertion. The same lemma gives
\eqref{cdp:eq:C.WH.5} and, for $M=I$, the closed-coframe quotient.
The map over $s\ne0$ to the original fibre over $t=s^N$ is an
isomorphism.

For a given weighted degeneration, its canonical divisor
sections give the data of \cref{def:II:weighted-normal-cycle}.
On a compact component core, a smooth tubular map expresses
its function as $v^{m_i}\sigma_i$ times a unit equal to one
on the zero section; the unique small smooth $m_i$th root
absorbs this unit. On double curves use both canonical
sections and the same weighted product trivialization.
These maps give the stated root covers and collar homomorphisms.
Resolve the explicit root necks and apply
\cref{lem:II:normal-product-collars} to that full reduced SNC
support. It has these same smooth normalization components
and labelled double curves, so its core and boundary maps
are exactly the ones used in \eqref{cdp:eq:C.WH.5}.

The root group preserves each map to the original component
and its two distinct labelled branches. It preserves the
lifted cyclic orientation and acts on the connected graph
by rotations. The stabilizer of a vertex is the kernel of
this rotation action, hence is one group $K$ at every vertex.
It acts transitively on covers of each original component.
Writing $r=N/|K|$, count the $N$ sheets at a generic component
point, whose normal inertia is $N/m_i$. This gives
\eqref{cdp:eq:C.WH.6}. There are $g_i$ points over a generic
axis and $r$ lifted edges, so each connected axis cover has
degree $g_i/r$. The local normalization makes it etale at
every axis point. Its pointwise stabilizer has order $N/g_i$.
The product and intersection of the cyclic subgroups of
orders $N/m_i,N/m_{i+1}$ have orders $N/g_i,h_i$; this proves
\eqref{cdp:eq:C.WH.0}. Equation \eqref{cdp:eq:C.WM.7} then
gives the ruled base degree $(m_i/r)/q=\gcd(m_i,a)/r$.

Finally consider a moving compressed root action with these
central maps. At an axis the pointwise stabilizer $J_{\rm axis}$
has order $hAB$. Its order-$h$ subgroup fixes $u,v$ and rotates
$s$; the residual independent characters on $u,v$ have orders
$B,A$. Explicitly choose integers $c_0,d_0$ with
$c_0A+d_0B=1$; a generator has characters
$(\zeta_B^{c_0},\zeta_A^{d_0},\zeta_{hAB})$ on $(u,v,s)$.
Their product is the character of $s^h$.

To obtain these exact coordinates throughout the holomorphic
action, average $u,v$ to their central eigencharacters. Since
the action preserves both branches the averages are $u'=uU$
and $v'=vV$ with units $U,V$. Average an axis coordinate to
an invariant one; its derivative on the axis is unchanged.
The identity $u'v'=s^hUV$ and the character product show that
$UV$ is invariant. Replace $u'$ by $u'/(UV)$. The product is
then exactly $s^h$, the characters and base coordinate $s$
are unchanged, and the differential is invertible on the axis.
The analytic local quotient ring is
@@EW.17@@
The first invariants, under the order-$h$ subgroup, are
$\C\{u,v\}$; the two residual power invariants give the
displayed ring. The residual axis cover is etale. At a general
component point the generic inertia is a normal reflection
of order $N/m_i$. Off the central fibre the base rotation is
free. Thus the quotient is smooth near the whole fibre and
has exactly the stated multiplicities and central component
maps. Finite quotients preserve the properness just proved.
\end{proof}
''')

affine_owner=render(r'''\subsection{Finite affine data on root cycles}\label{subsec:II:weighted-cycle-affine-data}

\begin{lemma}[Finite root actions and the total normal period]\hypertarget{tag-P357}{}\label{lem:II:weighted-cycle-affine-data}
\StatementRecord{lem:II:weighted-cycle-affine-data}{proved}{P357}{\cref{lem:II:weighted-cycle-roots,def:II:marked-normal-cycle,lem:II:moving-marked-cycle,cdp:st:C.2.UN.57}; \cite[arXiv v2, Theorem~2.1, p.~5]{Khaled2024Hopf}}
Take weighted data whose root graph is connected and has $M=I$.
Identify its open complements by their complex linear edge maps
with $G=\C^2/\Lambda$, where $\Lambda$ has rank three. At root
vertex $j$ let $n_j$ be its outgoing normal meridian and $h_j$
its outgoing compressed-edge exponent. The root generator and
edges have affine expressions
@@EW.2@@
where $\sigma$ is a rotation,
$R\Lambda=\Lambda$, $R^N=I$, $Rn_j=n_{\sigma j}$ and
$h_{\sigma j}=h_j$. For lattice elements $\lambda_j,\mu_j$
their complete compatibility and order equations are
@@EW.3@@
The full vector $u$ and affine constant $b$ are
@@EW.4@@
with $p$ primitive and $d>0$. For
$W=\operatorname{span}_{\R}\Lambda=\ker\ell$, one has
$\ell(iu)\ne0$, $Ru=u$ and $Rp=p$. There are complex
coordinates in which
@@EW.5@@
The eigenvalue $\rho$ has order $1,2,3,4$ or $6$;
$\rho^N=1$ and $R^r=I$, where $r$ is the strict-cover count.
The full affine descent relation is
@@EW.6@@
Changing normal-product constants on whole rotation orbits
preserves every central component, elliptic gluing and finite
action map. Such a choice can arrange
@@EW.7@@
and when $\rho\ne1$ this leaves the first coordinate of $b$
unchanged.
\end{lemma}
\begin{proof}
The orientation and rotation assertion are those of
\cref{lem:II:weighted-cycle-roots}, with each branch mapped
to its original marked branch. An isomorphism of two diagonal
Hopf covers preserving both axes lifts to their universal
$\C^2\setminus0$ covers. Hartogs extends the map and its inverse
across zero. The derivative is diagonal and invertible because
both axes are preserved. The image of a contracting diagonal
deck generator is a diagonal target deck element; conjugating
their derivatives identifies its two multipliers with the
source multipliers. The lift therefore commutes with that
same diagonal contraction. Apply
\cite[arXiv v2, Theorem~2.1, p.~5]{Khaled2024Hopf}:
class $\mathrm{IIc}$ gives a diagonal centralizer; class
$\mathrm{III}$ gives $(Az+Cw^r,Bw)$, whose two-axis
condition forces $C=0$; and class $\mathrm{IV}$ gives
$\operatorname{GL}(2,\C)$, whose two-axis subgroup is diagonal.
These are exactly the marked lifts in all diagonal cases.

For a marked ruled isomorphism, each ruling fibre maps to a
point of the target elliptic base because every holomorphic
map $\PP^1\to E$ is constant. Its base map has an affine lift.
The line multiplier on the universal base cover has constant
automorphy ratios. Its logarithmic derivative is holomorphic
and doubly periodic, hence constant; its logarithm is affine.
Thus both sorts of marked maps are affine in the logarithmic
coordinates of \cref{def:II:marked-normal-cycle}.
Compatibility on the same necks makes their linear part one
map $R$. Finite order and preservation of the entire lattice
give $R^N=I$ and $R\Lambda=\Lambda$. The labelled normal maps
give $Rn_j=n_{\sigma j}$. Composition on a logarithm chart,
with $\log\zeta_N=2\pi i/N$, gives exactly
\eqref{cdp:eq:C.EW.3}; the $N$fold composition gives its
second equation with every affine translation included.

Resolve each compressed edge by
\eqref{eq:II:compressed-neck-resolution}. The inserted ruled
vertices repeat the same outgoing normal. Apply the normal
height calculation in \cref{cdp:st:C.2.UN.57} to this resolved
marked cycle: on Hopf vertices its contracting periods give
\cref{cdp:eq:C.HG.4,cdp:eq:C.AD.3}, and on ruled vertices the
two outgoing normals agree. In the all-ruled case its elliptic
quotient gives the same nonzero sign. Therefore all
$\ell(in_j)$ have one nonzero sign, and the $h_j$ repetitions
give $\ell(iu)\ne0$ for the vector in
\eqref{cdp:eq:C.EW.4}. Rotation preserves this sum, so
$Ru=u$ and $Rp=p$.

The complex line $W\cap iW$ is $R$-invariant and complementary
to $\C p$, since $p\in W$ but $ip\notin W$. Send these lines
to the first and second coordinate axes, with $p=(0,1)$.
Then $W=\C\times\R$. Extend $p$ to an integral basis of
$\Lambda$; its two projected vectors form a real lattice in
the first coordinate, and orient it to make $C>0$. This is
\eqref{cdp:eq:C.EW.5}. The induced integral two-dimensional
matrix of $R$ has determinant one and trace
$2\operatorname{Re}\rho\in\Z$. Its finite order gives exactly
the listed five possible orders. The stabilizer of a root
vertex acts on its finite open-group cover by deck translations.
Since its graph rotation has order $r$, this also gives $R^r=I$.

Sum the first equation of \eqref{cdp:eq:C.EW.3} around the
cycle. The $\tau_j$ cancel, yielding
\eqref{cdp:eq:C.EW.6}. For a whole $\sigma$-orbit, add
$c n_j$ to each $\mathbf b_j$ with the same $c\in\C$.
The first equation is unchanged because $Rn_j=n_{\sigma j}$;
the order equation has no $\mathbf b_j$. These additions are
precisely changes of the normal-product constants in the
marked charts, so every central elliptic map and action stays
fixed. In the chosen coordinates, the second components of
all $n_j$ are real, nonzero and of one sign. Their sum on an
orbit has nonzero second component. Choose $c$ to make the
second component of $b$ equal to $i$. The orbit sum is $R$-fixed;
when $\rho\ne1$ its first component is zero, proving the last
assertion and \eqref{cdp:eq:C.EW.7}.
\end{proof}
''')

period_owner=render(r'''\subsection{Finite-equivariant logarithmic periods}\label{subsec:II:finite-equivariant-periods}

\begin{lemma}[Logarithmic period families with a finite root action]\hypertarget{tag-P358}{}\label{lem:II:finite-equivariant-periods}
\StatementRecord{lem:II:finite-equivariant-periods}{proved}{P358}{\cref{lem:II:weighted-cycle-affine-data,lem:II:logarithmic-period-family}}
Use the full lattice and affine data of
\cref{lem:II:weighted-cycle-affine-data}, with
$b=(\sigma_0,i)$ and $R=\operatorname{diag}(\rho,1)$.
Choose $1\le k\le N$ with $\rho=\zeta_N^k$, taking $k=N$
when $\rho=1$. Put
@@EW.8@@
Then
@@EW.9@@
and the periods
@@EW.10@@
define a smooth proper family of connected two-tori on
$\C^*_s$. In the real coordinate order of
\cref{lem:II:logarithmic-period-family}, its determinant is
@@EW.11@@
where $r_s=|s|$ and $C$ is the oriented lattice constant in
\eqref{cdp:eq:C.EW.5}.

Transport the full edge and action data by
@@EW.12@@
Their overlap identity is
@@EW.13@@
and their $N$fold action has translation $V_s\mu_j$.
The last period satisfies
@@EW.14@@
Thus they define a holomorphic finite action on the entire
punctured family. More precisely, set
$\theta_j(s)=\sum_{a<j}(\mathbf b_a(s)+l_a(s)\log s)$.
In the common coordinate $v_j-\theta_j(s)$ its translation is
@@EW.15@@

At infinity put $w=s^{-1}$ and divide the vector frame by
$s^k$. Then
@@EW.18@@
and the periods are $W_w\Lambda$ and
@@EW.19@@
The transformed finite action is exactly
@@EW.20@@
At $w=0$ its lattice and affine data are the conjugates of
the data at zero through $v\mapsto J\overline v$ and the
conjugate base rotation.
\end{lemma}
\begin{proof}
For fixed $c$, $V_s c$ is holomorphic in $s$. The identity
$RJ\overline R^{-1}=\rho J$ gives
\eqref{cdp:eq:C.EW.9}. The map $V_s$ is the map $V_z$ of
\cref{lem:II:logarithmic-period-family} at $z=s^k$; its
displayed norm identity and inverse therefore apply to the
same real vector space and every period vector.
For the fourth period take the logarithmic coefficient
$d\log s/(2\pi i)$. On a logarithm chart this is
$(d/k)\log z/(2\pi i)$. The determinant identity
\eqref{cdp:eq:C.TL.6}, with its coefficient denoted by $c$,
is affine in $c$ on both sides and is proved for every positive
integer $c$. It is consequently the same polynomial identity
at $c=d/k$.
Substituting $z=s^k$ gives exactly
\eqref{cdp:eq:C.EW.11}, with no change of real coordinates.
It is positive since $(r_s^{2k}-1)\log r_s\ge0$.
Logarithm monodromy adds $dV_sp\in\Lambda_s$. Uniformly
bounded period matrices and inverses on compact logarithm
charts give the proper quotient, as in the same lemma.

Apply $V_{\zeta_Ns}$ to the first equation of
\eqref{cdp:eq:C.EW.3} and use \eqref{cdp:eq:C.EW.9}.
The correction $h_jn_{\sigma j}/N$ is a real rational
multiple of an integral vector, so it transports to the
correction in \eqref{cdp:eq:C.EW.13}. The translation is in
the target frame, as expressed by
$\tau_j(s)=V_{\zeta_Ns}\tau_j$. For the order equation,
$R^{N-1-a}V_{\zeta_N^{a+1}s}=V_sR^{N-1-a}$; summing gives
the period $V_s\mu_j$. These are the full overlap and
finite-order equations. Likewise \eqref{cdp:eq:C.EW.6}
gives \eqref{cdp:eq:C.EW.14}.

On each successive component chart subtract the accumulated
edge term $\theta_j(s)$. Its transformed coordinate differs
by \eqref{cdp:eq:C.EW.15}. Changing $j$ changes this by an
integral period, using \eqref{cdp:eq:C.EW.13}; the last edge
adds $B_s$. Changing the logarithm adds an integral normal
vector. Thus these maps descend to a single holomorphic
action on the entire punctured period quotient, with the
already proved order and full affine constants.

Multiplying every vector by $s^{-k}$ gives
\eqref{cdp:eq:C.EW.18} and \eqref{cdp:eq:C.EW.19}.
The image vector is multiplied by $(\zeta_Ns)^{-k}$, so the
linear part is $\rho^{-1}R=J\overline R J^{-1}$ and its
translation is exactly \eqref{cdp:eq:C.EW.20}. These are
the frame changes of the same action, hence preserve every
overlap and order identity. At $w=0$ the frame is
$J\overline{(\cdot)}$; it conjugates the lattice, affine
constants and finite action with the displayed inverse base
rotation. This proves the final comparison.
\end{proof}
''')

general=render(r'''\subsection{The weighted cycle criterion and compact realization}\label{subsec:II:weighted-cycle-criterion}

\begin{proposition}[Weighted diagonal Hopf and ruled cycles]\hypertarget{tag-01E4}{}\label{cdp:st:C.2.UN.59}
\StatementRecord{cdp:st:C.2.UN.59}{proved}{01E4}{\cref{def:II:weighted-normal-cycle,lem:II:weighted-cycle-roots,lem:II:weighted-cycle-affine-data,lem:II:finite-equivariant-periods,lem:II:moving-marked-cycle}}
For the full marked data of \cref{def:II:weighted-normal-cycle},
the smooth weighted plumbing has connected two-torus fibres
exactly when its normalized $N$th-root graph is connected and
its rank-three integral complement-lattice product satisfies
@@WM.8@@
Every smooth-total two-torus degeneration with this marked
weighted support induces these data and satisfies the test.

Every weighted support satisfying it occurs over $\PP^1$ in
a smooth compact complex threefold, with all marked components,
elliptic gluings and full multiplicities preserved. Its only
other singular fibre is the complex conjugate weighted support.
All reduced fibre supports have Euler number zero. The
realization chooses the normal-product constants. The Hopf
components may have any algebraic dimension, and the cycle
may consist entirely of ruled components.

All component, axis, inertia and ruled-line maps and degrees
are those of \cref{lem:II:weighted-cycle-roots}. The finite
root action, including its linear eigenvalue of order
$1,2,3,4$ or $6$ and all its affine constants, is preserved
through the compact construction.
\end{proposition}
\begin{proof}
Apply \cref{lem:II:weighted-cycle-roots} to these precise
normal lines, sections and maps. Its smooth plumbing has
the full divisor $\sum_i m_iV_i$. On a connected root graph,
the lattice in \eqref{cdp:eq:C.WH.5} is injected. A two-torus
has abelian fundamental group, so the displayed conjugation
action is the identity. Conversely $M=I$ gives its complete
coframe isomorphism to a two-torus. The root fibre over $s$
is isomorphic to the original fibre over $s^N$; connectedness
is exactly the root-graph condition. Its final given-smoothing
comparison proves necessity for the same canonical normal data.

For compact realization use \cref{lem:II:weighted-cycle-affine-data}
on this connected root and choose $b=(\sigma_0,i)$ by its
orbitwise normal changes. The central components, elliptic
gluings and finite action are unchanged. Apply
\cref{lem:II:finite-equivariant-periods} to that entire lattice,
the same $R,\sigma,\tau_j$, and $u=dp$. This gives the
proper punctured two-torus family and its full finite action.

At zero transport the lattice by $V_s$. At a Hopf vertex the
component frame is
@@EW.16@@
This is exactly the Hopf frame in
\cref{lem:II:moving-marked-cycle}, with its fixed integer
angular relations and contracting generator. At a ruled
vertex use that lemma's primitive normal, transverse base
lift and third lattice vector, so the family is the same
$\PP(\OO_{E'(s)}\oplus\mathcal L'(s))$ at $s=0$.
Apply its compressed clause to these components, the constants
$\mathbf b_j(s)$ of \eqref{cdp:eq:C.EW.12}, and the same
integers $h_j$. The period formula
\eqref{eq:II:compressed-moving-cycle-periods} is exactly
\eqref{cdp:eq:C.EW.10}. The lemma's accumulated-edge logarithmic
maps give a biholomorphism of the entire punctured filling
with that period family, with holomorphic inverse.

The action extends over the marked curves and necks.
On a Hopf chart $RP_j(s)=P_{\sigma j}(\zeta_Ns)$, so its
component logarithm changes by a translation; exponentiation
gives the diagonal map of the full primary or secondary
quotient with its fixed angular characters. On a ruled chart
the normal-period map and the affine elliptic base map give
the line-bundle map and its homogeneous projective extension
of \cref{lem:II:weighted-cycle-roots}. In particular a
translation of $\mathcal L^\times$ extends: its base is a
translation of $E$, and its group law gives the fibre-line
isomorphism, extending to zero and infinity. The exact
overlap identity \eqref{cdp:eq:C.EW.13} extends these maps
across $uv=s^{h_j}$; its order identity makes the $N$th
iterate a deck period. Thus this is an action on the whole
normal filling. In its period coordinates the action is
\eqref{cdp:eq:C.EW.15}, so the punctured biholomorphism is
equivariant, including every affine constant.

Apply the quotient clause of \cref{lem:II:weighted-cycle-roots}
to these same central component and inertia maps. Its explicit
eigencharacter coordinates and invariant ring
\eqref{cdp:eq:C.EW.17} prove a smooth quotient and exactly
the original multiplicities. The central root covers and
their maps were fixed throughout, so its reduced quotient
is the prescribed marked surface.

At infinity use $w=s^{-1}$ and the frame $W_w$ in
\eqref{cdp:eq:C.EW.18}. Take outgoing normals $-W_wn_j$,
edge exponents $h_j$, and constants $W_w\mathbf b_j$.
Their logarithmic coefficients are $h_jW_wn_j/(2\pi i)$,
so their complete period is \eqref{cdp:eq:C.EW.19}.
The compressed moving construction applies again. At zero
in this infinity chart its Hopf frame is
$J\overline{P_j(0)}$: complex conjugation changes $2\pi i$
to $-2\pi i$, exactly accounting for the chosen minus sign
on every normal. The contracting logarithms and finite
characters are therefore the conjugate ones. The separate
ruled frame likewise gives the conjugate line and marked
sections. In each component frame the edge constant is
the conjugate of its original value, since
$(J\overline P)^{-1}J\overline b=\overline{P^{-1}b}$.

Use exactly the infinity action \eqref{cdp:eq:C.EW.20}.
It is the frame change of the action already constructed,
so all overlap and finite-order identities hold. Its central
map is conjugated by $v\mapsto J\overline v$ and the base
rotation is conjugate. The quotient clause of
\cref{lem:II:weighted-cycle-roots}, applied to these conjugate
weighted data, gives the conjugate smooth quotient charts
and the same positive multiplicities.

Glue the two proper equivariant fillings to the full family
\eqref{cdp:eq:C.EW.10} by their logarithmic biholomorphisms
and the frame change \eqref{cdp:eq:C.EW.18}. As in the
closed-base cover of \cref{lem:II:moving-marked-cycle}, take
closed smaller discs in each filling and a closed annulus
in the proper punctured family. They cover the inverse image
of $\PP^1_s$ by compact sets. At either overlap boundary only
one open piece includes its limiting base value; the gluing
graphs are closed. The resulting normal root total space is
Hausdorff, proper and compact. Take its finite quotient with
base $t=s^N$. It is smooth at zero and infinity by the proved
invariant rings and elsewhere because the base action is
free. A general quotient fibre is isomorphic to any one of
its $N$ root fibres. Hence it is the specified connected
two-torus, and only the two stated weighted supports are
singular. Every component and every double elliptic curve
of these supports has Euler number zero, so additivity proves
the final Euler assertion.
\end{proof}
''')

suspension=render(r'''\subsection{Weighted cycles of algebraic dimension zero}\label{subsec:II:weighted-cycle-suspensions}

\begin{proposition}[Elliptic suspensions realizing weighted Hopf and ruled cycles]
\hypertarget{tag-01E1}{}\label{cdp:st:C.2.UN.56}
\StatementRecord{cdp:st:C.2.UN.56}{proved}{01E1}{\cref{cdp:st:C.2.UN.59,lem:II:weighted-cycle-affine-data,lem:II:weighted-cycle-roots,cdp:st:C.2.UN.48,lem:II:moving-marked-cycle}}
\hypertarget{tag-01DX}{}\label{cdp:st:C.2.UN.52}
\StatementRecord{cdp:st:C.2.UN.52}{proved}{01DX}{}
Take the data of \cref{def:II:weighted-normal-cycle}, with
at least one Hopf component, and with every Hopf component
of algebraic dimension zero. The connected-root and $M=I$
test in \cref{cdp:st:C.2.UN.59} is necessary and sufficient
for connected two-torus fibres in the smooth weighted plumbing,
and every smooth-total torus degeneration in this marked
class induces data satisfying that test.

Every support satisfying it has a compact realization over
$\PP^1$ obtained by replacing one tube in an elliptic
suspension. It preserves every marked component, elliptic
gluing, finite secondary action and full multiplicity, and
chooses the normal-product constants. Every reduced support
in this compact family has Euler number zero.
All component, axis, inertia and ruled-cover formulas of
\cref{lem:II:weighted-cycle-roots} apply. There are at least
two original Hopf vertices, and every ruling line
$\mathcal L_i$ has infinite order in $\operatorname{Pic}^0(E_i)$.
The all-Hopf case is included. In particular the examples in
\cref{ex:II:weighted-cycle-examples} give multiplicities $(1,n)$
for every $n\ge1$ and a primary three-component support of
multiplicities $(1,2,2)$.
\end{proposition}
\begin{proof}
The local criterion and all root-cover maps are the exact
specialization of \cref{cdp:st:C.2.UN.59,lem:II:weighted-cycle-roots}
to the stated algebraic dimensions. Assume the test passes
and use the same common $G=\C^2/\Lambda$, $u=dp$ and finite
affine data of \cref{lem:II:weighted-cycle-affine-data}.
Projection along $\C p$ gives an elliptic curve $E$ and
identifies $G$ with $\mathcal L^\times$ for a degree-zero
line $\mathcal L$; its logarithmic period construction is
\cref{def:II:marked-normal-cycle}. This line has infinite
order. Otherwise a multiplication isogeny trivializing it
would give a finite map $E'\times\C^*\to G$, whose image of
$E'\times\{1\}$ is a compact curve. One of the identical
open complements is a Hopf axis complement of algebraic
dimension zero. On a primary cover its diagonal contraction
is nonresonant, and \cite[arXiv v1, \S2.2.6, p.~5]{AbashevaDeev2024AB}
gives only the two axes as curves. For a secondary component,
\cref{lem:II:central-primary-hopf-cover} preserves algebraic
dimension on the central primary cover; the inverse image
of a compact curve would be a union of its axes, whose images
are the two marked axes. This excludes a curve in the common
complement.

The finite linear part fixes $p$, so it induces the identity
on the kernel $\C^*$ and an origin-preserving elliptic
automorphism $\beta$ with $\beta^*\mathcal L\simeq\mathcal L$.
For $\beta\ne1$, the nonzero linear map $\beta^*-1$ on the
dual elliptic curve is an isogeny, with finite kernel; it
would make $\mathcal L$ torsion. For $\beta=1$, the two
eigenvalues of $R$ are one and a finite-order shear is the
identity. Hence
@@WH.8@@
The full affine relation \eqref{cdp:eq:C.EW.6} consequently gives
@@WH.10@@
Here $d$ is the primitive divisor of $u=-\sum_jh_jn_j$.
The resolved root cycle has $\sum_jh_j$ vertices: each edge
of exponent $h_j$ contributes its $h_j-1$ inserted ruled
components. The monomial resolution is an isomorphism on
each fibre over $s\ne0$, and the normalized-root projection
identifies that fibre with the weighted fibre over $t=s^N$.
Their common coframe takes the cycle period
$(\log s)u/(2\pi i)$ to $(\log t)(u/N)/(2\pi i)$.
Consequently the resolved graph computes the vector $u$
through these $h_j$ repeated meridians, while the finite
root quotient gives the suspension integer $q=d/N$.

Write $q_i$ for the fibre degree in \eqref{cdp:eq:C.WM.2}
at the $i$th ruled vertex. A torsion ruling line $\mathcal L_i$
would pull back to a
torsion line under the finite etale base map in
\eqref{cdp:eq:C.WM.3}; its $q_i$th root $\mathcal L'$ would
then be torsion as well. A trivializing isogeny would give
a compact elliptic curve in this same common open group,
contradicting the previous paragraph. Thus all ruling lines
have infinite order. If there were only one original Hopf
vertex, follow a lifted Hopf vertex to the next one above
that original vertex. Every intermediate strict or resolved
vertex is ruled and repeats the outgoing normal. A deck
rotation takes the first Hopf to the second with $R=I$,
so their outgoing normals agree. The second Hopf would have
equal incoming and outgoing normal directions, contrary to
the independent two-axis frame. This proves the Hopf count.

For the compact suspension adjust edge constants on whole
rotation orbits. With $R=I$, $n_j$ is constant on an orbit.
At a Hopf vertex the two adjacent independent normal vectors
belong to different orbits. Their two orbit-normal sums span
$\C^2$, so solve their two-by-two linear equation to arrange
$\sum_j\mathbf b_j=0$. The full central elliptic and finite
action maps stay fixed by \cref{lem:II:weighted-cycle-affine-data}.
Its compatibility equations reduce exactly to the
$R=I$ specialization \eqref{cdp:eq:C.WH.9}, with
$-l_j2\pi i/N=h_jn_j/N$.

Use the lattice-coordinate isomorphism in
\eqref{cdp:eq:C.HG.6}, with this same primitive $p$. It sends
$u$ to $d(0,2\pi i)$ and gives $0<|q_0|<1$ and $a\ne1$.
The exclusion of $a=1$ is the same embedded elliptic map
\eqref{cdp:eq:C.HG.7} into this common Hopf complement.
Apply the arbitrary-parameter suspension clause of
\cref{cdp:st:C.2.UN.48} with its integer $d$ equal to the
present $q=d/N$, and with these exact $q_0,a$.
It gives a compact suspension whose selected periods are
@@WH.11@@
Put $t=s^N$. Every normal, contracting period and finite
angular relation is transported by its fixed integer
coefficients in this rank-three lattice. At Hopf vertices
use the two independent normal frames of
\cref{lem:II:moving-marked-cycle}; at ruled vertices use its
primitive normal, transverse base lift and third period.
Thus the strict central component maps remain the given
finite Hopf power maps or ruled maps \eqref{cdp:eq:C.WM.6}.

The unknown vectors $\mathbf b_j(t),\tau_j(t)$ can be chosen
holomorphically through their central values to satisfy
\eqref{cdp:eq:C.WH.9} and $\sum\mathbf b_j(t)=0$.
Indeed their coefficient matrix has constant integers.
Its right side is a rational linear combination of the
three moving lattice generators. Every rational left-kernel
relation vanishes at zero; the three original generators
are rationally independent, so each rational coefficient
vanishes separately. The same relation therefore vanishes
after transport. A fixed linear right inverse on the matrix
image gives a holomorphic solution. Add its constant kernel
difference from the prescribed central solution to recover
those exact central values.

Apply the compressed construction of
\cref{lem:II:moving-marked-cycle} to these moving components,
edge constants and the original $h_j$. On component cores the
finite maps are translations of the common open group; they
extend to diagonal maps on Hopf quotients and to the line
and projective maps on ruled components. On necks they are
the induced line maps of $uv=s^{h_j}$.
Equation \eqref{cdp:eq:C.WH.9} is their exact overlap identity
and its order equation makes the $N$th iterate a deck period.
Thus these maps give the full finite action. The quotient
clause of \cref{lem:II:weighted-cycle-roots}, with the same
central characters, proves smoothness and precisely the
original weighted support.

The punctured quotient has periods \eqref{cdp:eq:C.WH.11}:
$\log s=(\log t)/N$ and a branch change adds
$u/N\in\Lambda$. The coframe descends because $R=I$.
Its local origins define a holomorphic torsor under this
marked family of tori. The descended coframe identifies the
Lie-algebra bundle with $\OO^{\oplus2}$. On the punctured disc
its sheaf sequence is
@@WH.13@@
The coherent sheaf $\OO^{\oplus2}$ has vanishing $H^1$ by
\cite[\S2, fundamental theorem~B, p.~80]{Cartan1957}, applied
to the Stein punctured disc. The lattice local system has
vanishing $H^2$: the circle retract has a cellular complex
with cells only in degrees zero and one, also with these
local coefficients. The cohomology sequence therefore gives
$H^1(\mathscr A)=0$. Lifting the translation cocycle and
taking its coboundary produces a holomorphic section and
an isomorphism of this entire punctured quotient with the
period family in \eqref{cdp:eq:C.WH.11}, including its
affine translation data.

Use this isomorphism for the nested-annulus replacement in
\cref{cdp:st:C.2.UN.48}, on the same compact suspension base.
Its closed-base compact cover and closed gluing graphs prove
properness and compactness of the smooth replacement. The
central quotient maps were unchanged, so every original
component, finite action and elliptic gluing is preserved.
At the selected value Hopf and ruled components and double
elliptic curves have Euler number zero. At every other value
the support is the unchanged elliptic-suspension support,
whose Euler number is zero by that same suspension clause.
This proves the stated compact realization.
\end{proof}
''')

examples=render(r'''\subsection{Explicit weighted cycles and finite linear actions}\label{subsec:II:weighted-cycle-examples}

\begin{example}[Unequal Hopf multiplicities and finite linear actions]\hypertarget{tag-P359}{}\label{ex:II:weighted-cycle-examples}
\StatementRecord{ex:II:weighted-cycle-examples}{proved}{P359}{\cref{cdp:st:C.2.UN.56,cdp:st:C.2.UN.59,ex:II:three-hopf-cycle}}
There are compact smooth-total weighted Hopf-cycle realizations
with multiplicities $(1,n)$ for every $n\ge1$, and one with
three primary Hopf components of multiplicities $(1,2,2)$.
There are also compact realizations with two ruled components
of multiplicity $N$ and finite root linear part of exact order
$N$ for $N=2,3,4,6$.
\end{example}
\begin{proof}
Choose nonresonant contractions $\alpha,\beta$ and put
@@WH.14@@
Use the two-copy inversion construction of
\cref{cdp:st:C.2.UN.57} with this same secondary Hopf surface.
Over $s\mapsto\zeta_ns$, take the identity on the first
copy and $(Z,W)\mapsto(Z,\zeta_nW)$ on the second.
The first neck $(z,w)\mapsto(z^{-1},s/w)$ intertwines these
maps. The other neck gives $(Z,W)\mapsto(\zeta_nZ,W)$;
it differs by the anti-diagonal deck element already in
\eqref{cdp:eq:C.WH.14}. These maps therefore give an order-$n$
action on the whole plumbing.

At a double curve the action is $(x,y)\mapsto(x,\zeta_ny)$.
The invariant coordinates are $x,Y=y^n$, with
@@WH.15@@
The quotient is smooth, with the first component of
multiplicity one and the second of multiplicity $n$.
The first is the given $H$. On the second the anti-diagonal
finite group and the extra action generate the two independent
scalar groups. The map $(Z,W)\mapsto(Z^n,W^n)$ therefore
identifies its quotient with the primary Hopf surface
$H(\alpha^n,\beta^n)$. The axis maps $z\mapsto z^{-n}$ are
isomorphisms of their elliptic quotients, since their kernels
are exactly the respective finite angular groups.

The explicit compact comparison uses common coordinates
$(b,y)=(zw,w^n)$, so $q_0=\alpha\beta$ and $a=\beta^n$.
The root normal divisor is $d=n$ and the root degree is $N=n$;
thus the suspension index in \eqref{cdp:eq:C.WH.10} is one.
Take the parameter clause of \cref{cdp:st:C.2.UN.48} with
these $q_0,a$ and index one. On its pullback $t=s^n$, choose
$\beta(s)=a(s^n)^{1/n}$ with the given central root and set
$\alpha(s)=q_0/\beta(s)$. The same neck and finite-action
equations hold in these families. On the punctured common
quotient the action is exactly the base deck action.
The smooth finite quotient therefore replaces a tube in
that compact suspension and realizes \eqref{cdp:eq:C.WH.15}.

For the primary triangle of
\cref{ex:II:three-hopf-cycle}, use $s\mapsto-s$ and the
three component actions
@@WH.16@@
Substitution in its three maps \eqref{cdp:eq:C.HG.16}
intertwines the actions. On the middle double curve the
action is a free elliptic translation; on the other two it
is a normal reflection. The quotient has multiplicities
$(1,2,2)$ and primary contraction pairs
@@WH.17@@
with axis maps inversion, identity and inversion. The root
normal divisor is two and its root degree is two, so the
same quadratic pullback of the index-one suspension and
the preceding finite quotient give this compact realization.

Finally let $N=2,3,4,6$ and take an elliptic curve $E$ with
an origin-preserving automorphism $\rho$ of exact order $N$.
For $N=2$ take any elliptic curve and $\rho=-1$; for $N=4$
use $\C/(\Z+i\Z)$ and $\rho=i$; for $N=3,6$ use
$\C/(\Z+e^{\pi i/3}\Z)$ and multiplication by
$e^{2\pi i/3},e^{\pi i/3}$, respectively. Start with a root
cycle of $2N$ copies of $E\times\PP^1$, joined by the
identity on their elliptic sections. Its complete data are
@@EW.21@@
In the first equation of \eqref{cdp:eq:C.EW.3} all terms
sum to zero except at the cyclic endpoint, where they give
$-2p$. The $N$fold translation sum is $(N-1)p$ on even
vertices and $Np$ on odd vertices. These are integral periods,
so the full action has the required order. It acts freely
on the central graph. The quotient has two components
$E\times\PP^1$, each of full multiplicity $N$. Identify
vertex two with vertex zero by the inverse generator: one
elliptic gluing is the identity and the other is $\rho^{-1}$.
The root cycle has identity lattice product, and its finite
linear part is this exact $R$. Apply
\cref{cdp:st:C.2.UN.59} to obtain the compact realization and
its conjugate weighted support with these same maps.
\end{proof}
''')

root_owner=re.sub(r'\betale\b',r"\\'{e}tale",root_owner)
suspension=re.sub(r'\betale\b',r"\\'{e}tale",suspension)

fragments={
 'P333_replacement':p333new,'UN48_replacement':un48new,
 'P355':definition,'P356':root_owner,'P357':affine_owner,
 'P358':period_owner,'UN59_replacement':general,
 'UN56_replacement':suspension,'P359':examples,
}
old_heading=r'\subsection{Weighted Hopf cycles}\label{subsec:II:weighted-hopf-cycles}'
main_start=current.index(old_heading)
main_end=current.index(original[52],main_start)+len(original[52])
main_old=current[main_start:main_end]
main_new='\n\n'.join([definition,root_owner,affine_owner,period_owner,general,suspension,examples]).replace(
 r'\label{subsec:II:weighted-cycle-data}',
 r'\label{subsec:II:weighted-cycle-data}\label{subsec:II:weighted-hopf-cycles}',1)
remote_rows=[
 dict(statement_id='cdp:st:C.2.UN.56',old_text=original[56],
      new_text=r'\subsection{Canonical and period reductions on Hopf trees}\label{subsec:II:hopf-tree-reductions}',
      reason='Move the complete weighted mixed criterion and proof into the earlier common weighted-cycle owners; preserve its permanent identity in the merged UN52/56 statement. The new actual heading begins the untouched UN58 and remaining tree units.'),
 dict(statement_id='cdp:st:C.2.UN.59',old_text=original[59],new_text='',
      reason='Move the complete general weighted-cycle statement and all finite-action/period/infinity proof into the earlier weighted unit, preserving the exact permanent statement and equation targets.'),
 dict(statement_id='lem:II:moving-marked-cycle',old_text=p333,new_text=p333new,
      reason='Proved compressed-neck extension with full proper compact-annulus maps, monomial resolution/graph closure, component transitions and complete coframe periods; every h=1 clause and proof remains.'),
 dict(statement_id='cdp:st:C.2.UN.48',old_text=un48,new_text=un48new,
      reason='Transfer the entire monomial resolution proof to earlier P333 with exact variable map and expose the same proved arbitrary q0,a,d pencil/Tate/suspension clause. Preserve the entire marked-cycle construction and all smoothness, periods, multiplicities and Euler conclusions.'),
]
assert current.count(main_old)==1
integrated=current.replace(main_old,main_new,1)
for row in remote_rows:
 assert current.count(row['old_text'])==1,row['statement_id']
 assert integrated.count(row['old_text'])==1,row['statement_id']
 integrated=integrated.replace(row['old_text'],row['new_text'],1)
old_all=main_old+'\n'+'\n'.join(r['old_text'] for r in remote_rows)
new_all=main_new+'\n'+'\n'.join(r['new_text'] for r in remote_rows)
for pattern in (r'\\label\{([^}]+)\}',r'\\hypertarget\{(tag-[^}]+)\}\{\}'):
 before=Counter(re.findall(pattern,old_all));after=Counter(re.findall(pattern,new_all))
 for ident,count in before.items():assert after[ident]==count,(ident,count,after[ident])
 for ident,count in after.items():assert count==1,(ident,count)
assert Counter(used)==Counter(equations.keys()), (set(equations)-set(used),Counter(used)-Counter(equations.keys()))
for disp in re.findall(r'\\begin\{equation\}.*?\\end\{equation\}',new_all,re.S):
 assert disp.count(r'\SsixEquationAliases')<=1,disp
 assert not re.search(r'\n[ \t]*\n',disp),disp
assert not re.search(r'\\tag\{',new_all)
for ref in re.finditer(r'\\(?:[Cc]ref|eqref|ref)\{([^}]+)\}',new_all):
 for lab in ref.group(1).split(','):
  assert r'\label{'+lab+'}' in integrated,lab
assert not re.search(r'night:P4R\.13|night:P4\.40',new_all)

if __name__=='__main__':
 for key,value in fragments.items():
  (out/(stem+'_'+key+'.tex')).write_text(value,newline='\n')
 freeze('input',main_old)
 (out/(stem+'_replacement.tex')).write_text(main_new,newline='\n')
 with (out/(stem+'_remote_repairs.tsv')).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=['statement_id','old_text','new_text','reason'],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(remote_rows)
 print('17 mathematical fragments and main plus4 remote guards prepared;48 equation identities and all old labels/tags preserved. Records/comparison not yet READY. No central writes.')
