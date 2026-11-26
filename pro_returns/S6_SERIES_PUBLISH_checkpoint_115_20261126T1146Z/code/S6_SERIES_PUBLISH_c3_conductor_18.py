#!/usr/bin/env python3
"""Prepare support-graph common owners and exact receiving guards; no main writes."""
from pathlib import Path
from collections import Counter
import csv,re

root=Path(__file__).resolve().parents[1]
out=root/'agents/continuation3_conductor'
stem='S6_SERIES_PUBLISH_c3_conductor_18'
current=(root/'S6_SERIES_PUBLISH_II.tex').read_text()
names=['UN17','UN54','UN58','UN60','UN61','UN62','UN63','UN80','UN83','P306','P350','P351','P337']
old={k:(out/f'{stem}_{k}_input.tex').read_text() for k in names}
for k,s in old.items():assert current.count(s)==1,(k,current.count(s))
for n in (54,58,60,61,62,63):
 assert old[f'UN{n}']==(out/f'S6_SERIES_PUBLISH_c3_conductor_tail_UN{n}_input.tex').read_text(),n

with (root/'agents/continuation2_B/D19/S6_SERIES_PUBLISH_II_B2_D19_v1_equation_map.tsv').open() as f:
 established={r['old_tag']:r['target_label'] for r in csv.DictReader(f,delimiter='\t') if r['old_tag']}
equations={}; equation_tags={}; moved=[]; formula_maps=[]
for name,s in old.items():
 for m in re.finditer(r'\\\[.*?\\\]|\\begin\{equation\}.*?\\end\{equation\}',s,re.S):
  text=m.group()
  for label in re.findall(r'\\label\{([^}]+)\}',text):
   equations[label]=(name,text)
   tags=re.findall(r'\\hypertarget\{(tag-[^}]+)\}\{\}',text)
   labels=re.findall(r'\\label\{([^}]+)\}',text)
   if len(tags)==len(labels):equation_tags[label]=tags[labels.index(label)]

def eq(content,*keys):
 labels=[established.get(k,k) for k in keys]
 targets=[]
 for label in labels:
  assert label in equations,label
  moved.append(label)
  if label in equation_tags:targets.append(r'\hypertarget{'+equation_tags[label]+r'}{}')
 text=r'\begin{equation}'+'\n'+content.strip()+'\n'
 if targets:text+='\n'.join(targets)+'\n'
 text+=r'\label{'+labels[0]+'}'+'\n'
 if len(labels)>1:text+=r'\SsixEquationAliases{'+''.join(r'\label{'+v+'}' for v in labels[1:])+'}\n'
 return text+r'\end{equation}'

def render(s):
 return re.sub(r'@@([A-Z]+\.\d+)@@',lambda m:retained('C.'+m.group(1)),s)

def retained(key):
 label=established[key];name,text=equations[label]
 moved.append(label)
 text=text.replace(r'\tag{'+key+'}','')
 if text.startswith(r'\['):text=r'\begin{equation}'+text[2:-2]+r'\end{equation}'
 return re.sub(r'\n[ \t]*\n+','\n',text)

def cut(s,start,end,replacement):
 assert s.count(start)==1,(start,s.count(start))
 a=s.index(start);b=s.index(end,a)
 return s[:a]+replacement+s[b:]

new={}
p306=old['P306']
p306=p306.replace('The smooth fibres are torsors under one fixed elliptic curve, and',
 'The smooth fibres are torsors under one fixed elliptic curve $F$, and')
root_chart=eq(r'''(F\times\Delta_s)/\mu_m,\qquad
 (z,s)\longmapsto(z+\tau,\zeta_m s),\qquad
 q=s^m,\qquad\operatorname{ord}(\tau)=m.''','C.HT.4','C.QT.2','cdp:eq:C.EP.8')
canonical=eq(r'''K_{E_0}\simeq q^*K_B\otimes
 \OO_{E_0}\Bigl(\sum_b(m_b-1)C_b\Bigr),
 \qquad q_*K_{E_0}\simeq K_B.''','eq:II:quasibundle-canonical')
vertical_form=eq(r'''q^*\theta\wedge\alpha_F,''','C.HT.5')
vertical_order=eq(r'''\operatorname{ord}_{C_b}(q^*\theta\wedge\alpha_F)
       =m_b\operatorname{ord}_b(\theta)+m_b-1.''','C.HT.6','C.QT.6')
genus_zero=eq(r'''q_*\OO_{E_0}=\OO_{\PP^1},\qquad
 R^1q_*\OO_{E_0}=\OO_{\PP^1},\qquad
 (h^0,h^1,h^2)(E_0,\OO_{E_0})=(1,1,0).''','C.QT.3')
extra_statement=r'''

More precisely, the tube of $mC$ is isomorphic over its base disc to
@@ROOT@@
The quotient map is finite \'etale, its central cover
$\pi_C:F\to C$ is connected, and the normal line $N_{C/E_0}$
has exact order $m$. The connected cover of unit frames of its
$m$th-power trivialization is this same $F\to C$; replacing the
normal by its dual reverses the cyclic character.
Restriction followed by $\pi_C^*$ is evaluation of the fixed
$H^1(F,\OO_F)$ frame of $R^1q_*\OO_{E_0}$. Thus
\[
 0\longrightarrow H^1(B,\OO_B)\xrightarrow{q^*}
 H^1(E_0,\OO_{E_0})
 \xrightarrow{\ \pi_C^*\circ\operatorname{res}_C\ }
 H^1(F,\OO_F)\longrightarrow0
\]
is exact. For $B=\PP^1$ this restriction composite is an
isomorphism, and
@@GENUSZERO@@

Let $m_bC_b$ denote the full fibres with $m_b>1$. Then
@@CANONICAL@@
Fix a nonzero invariant one-form $\alpha_F$ on $F$.
For every meromorphic differential $\theta$ on $B$, the local
expressions
@@FORM@@
glue to a meromorphic two-form on $E_0$. Every meromorphic
two-form with vertical divisor has this form for a unique
$\theta$, and its order is
@@ORDER@@
'''
extra_statement=extra_statement.replace('@@ROOT@@',root_chart).replace('@@GENUSZERO@@',genus_zero).replace('@@CANONICAL@@',canonical).replace('@@FORM@@',vertical_form).replace('@@ORDER@@',vertical_order)
p306=p306.replace(r'\end{lemma}',extra_statement+'\n'+r'\end{lemma}',1)
for a,b in [('Set $A=','Set $F='),('with $A$','with $F$'),('by the same elliptic curve $A$','by the same elliptic curve $F$'),('as $A$-torsors','as $F$-torsors'),(r'\operatorname{Aut}(A,0)',r'\operatorname{Aut}(F,0)')]:p306=p306.replace(a,b)
gauge=r'''

Choose a local section of the smooth root family near one point
of its central fibre. The marked integration maps then give a
product $F\times\Delta_s$ after shrinking the disc. Write the
cyclic map as $(z,s)\mapsto(z+\tau+A(s),\zeta_ms)$, where
$\tau$ is its central translation and $A$ is a small holomorphic
complex lift with $A(0)=0$. The order-$m$ law gives
$\sum_{j=0}^{m-1}A(\zeta_m^js)=0$: the sum is lattice-valued
and vanishes at zero. Set
\[
 b(s)=-\frac1m\sum_{j=0}^{m-1}jA(\zeta_m^js),\qquad
 z'=z+b(s),\qquad z=z'-b(s).
\]
Subtracting the shifted sums gives
$b(\zeta_ms)-b(s)=-A(s)$. These inverse coordinate maps
give \eqref{cdp:eq:C.HT.4}. The central action is free, so
$\tau$ has exact order $m$. The conormal frame upstairs is
$ds$, with character $\zeta_m$. If its $a$th tensor power
had a nowhere-zero section downstairs, its pullback would
be $h(ds)^a$ with $h$ holomorphic on the connected compact
$F$. Invariance gives $h(z+\tau)\zeta_m^a=h(z)$.
The function $h$ is a nonzero constant, so $m\mid a$.
The full fibre trivializes the $m$th power, proving the
exact normal order. The unit-frame cover has precisely this
primitive character and is the same connected cyclic cover;
duality inverts that character.
'''
needle='It consequently acts trivially on the relative $H^1(\\OO)$ generator.'
assert needle in p306
p306=p306.replace(needle,needle+gauge,1)
restriction=r'''

The square formed by the root tube, its central inclusion
$F\hookrightarrow E'$, the quotient tube and $C\hookrightarrow E_0$
commutes. On coherent cohomology its upper restriction evaluates
the constant $H^1(F,\OO_F)$ frame. Finite invariants and this
restriction commute, by the same averaging operator. Therefore
restriction on the quotient followed by $\pi_C^*$ equals
evaluation of the frame used above. This proves the stated
restriction map, including at a multiple fibre. The Leray
edge sequence is exact with kernel $q^*H^1(B,\OO_B)$ and
quotient $H^0(B,R^1q_*\OO_{E_0})=H^1(F,\OO_F)$.
For $B=\PP^1$ its left term is zero; together with
\eqref{cdp:eq:C.RG.13} it gives \eqref{cdp:eq:C.QT.3}.

\item Normalize the relative invariant form by the fixed marking.
Translations between product charts change an absolute lift of
$\alpha_F$ only by a base one-form. Wedge with $q^*\theta$
therefore gives the same two-form on overlaps. In the root
chart $t=s^m$, the pullback of $dt\wedge\alpha_F$ is
$m s^{m-1}ds\wedge\alpha_F$. Its divisor there has order
$m-1$ on $s=0$. The finite \'etale map preserves that order,
giving the first canonical isomorphism in
\eqref{eq:II:quasibundle-canonical} and the full formula
\eqref{cdp:eq:C.HT.6}.

A holomorphic two-form upstairs is
$a(s)ds\wedge\alpha_F$, because its coefficient is constant
on every compact elliptic fibre. Root invariance is
$a(\zeta_ms)\zeta_m=a(s)$, so
$a(s)=s^{m-1}c(s^m)$ with $c$ holomorphic. Its descent is
the form corresponding to $m^{-1}c(t)dt$ on the base.
This proves $q_*K_{E_0}=K_B$ across every multiple value.

Choose a nonzero meromorphic base differential to form one
reference two-form. The ratio of any vertical-divisor
meromorphic two-form to that reference has vertical divisor.
On each regular compact fibre outside that divisor it is a
nonzero holomorphic function and hence constant. It descends
to the regular base. On the root tube its Laurent expansion
is a meromorphic function of $s$ invariant under
$s\mapsto\zeta_ms$, so it is a meromorphic function of
$s^m$. This extends the descended ratio through every omitted
value and proves existence and uniqueness of $\theta$ in
\eqref{cdp:eq:C.HT.5}.
'''
assert p306.endswith(r'\end{enumerate}'+'\n'+r'\end{proof}')
p306=p306[:-len(r'\end{enumerate}'+'\n'+r'\end{proof}')]+restriction+r'\end{enumerate}'+'\n'+r'\end{proof}'
new['P306']=p306

p350=cut(old['P350'],
 'The normalized root of a smooth full fibre $mJ$',
 'For the marked Hopf pair,',r'''Apply \cref{lem:II:identity-monodromy-elliptic} to this
same quasibundle $q:P\to B$ and full fibre $mJ$.
Its chart \eqref{cdp:eq:C.HT.4} gives the fixed-translation
quotient, exact normal order $m$, and the connected
unit-frame cover with its primitive character. These are
the surface germ, root map and normal line used below.

''')
new['P350']=p350

p351=old['P351']
opening='The canonical formula '+r'\eqref{eq:II:quasibundle-canonical}'
end='Let $q:P'+r'\to B$'
p351=cut(p351,opening,end,r'''For a full reduced SNC torus degeneration, let one
component be such a leaf, with its only double curve $J$
on a neighbouring smooth component $P$. The difference
of the canonical evaluation orders and the individual
core expansions are
\cref{cdp:eq:C.NS.8,cdp:eq:C.NS.11,cdp:eq:C.AS.15,cdp:eq:C.AS.16},
with $k_P$ the order of this neighbour. These conclusions
use only that leaf and its double curve; the rest of the
support may contain other components and intersections.
In these expansions $\gamma_{\rm core}$ is the oriented
core of this leaf, and the relative evaluation is divided
by $t^{k_P}$.

For a full star $P\cup_iH_i$ with arbitrary smooth main
component $P$, the main canonical divisor is
\eqref{cdp:eq:C.NS.9}. The global comparison with the
inverse transform and the common core class below use
the following quasibundle and star hypotheses.
''')
canonical_old=equations['eq:II:quasibundle-canonical'][1]
canonical_intro='For every such quasibundle, with full fibres $m_bJ_b$,\nthe canonical map and its direct image are\n'
assert canonical_intro+canonical_old in p351
p351=p351.replace(canonical_intro+canonical_old,r'''The canonical line and direct image of this $q$ are
\eqref{eq:II:quasibundle-canonical} in
\cref{lem:II:identity-monodromy-elliptic}, with
$(E_0,C_b)=(P,J_b)$.''',1)
p351=cut(p351,'The root-product calculation in the proof of',
 'The dual Hopf normal has exact order',r'''Apply \cref{lem:II:identity-monodromy-elliptic} to the
given quasibundle $q$ and marked full fibre $mJ$.
Its connected root and primitive normal character give
normal order exactly $m$.
''')
p351=cut(p351,'To prove '+r'\eqref{eq:II:quasibundle-canonical}',
 'For the smoothing, apply the evaluation construction of',
 r'''The canonical isomorphism and direct image are the
application of \cref{lem:II:identity-monodromy-elliptic}
to this same $q:P\to B$, its marked and unmarked full
fibres, and its fixed integral elliptic marking.

''')
p351=p351.replace('For the smoothing, apply the evaluation construction of',
 'For any one of the stated leaf occurrences, apply the evaluation construction of',1)
p351=p351.replace('Adjunction on $P$ gives\n'+r'\eqref{cdp:eq:C.NS.9}.',
 'When the entire support is the star, adjunction on its main\ncomponent $P$ gives '+r'\eqref{cdp:eq:C.NS.9}.',1)
p351=p351.replace('These are expansions of the same holomorphic period function.',
 'In the full star case with this quasibundle $P$, these are\nexpansions of its one common holomorphic core period.',1)
p351=p351.replace('maps in that definition apply to this quasibundle.',
 r'maps of \cref{def:II:elliptic-star-data} apply to this quasibundle.',1)
new['P351']=p351

un80=cut(old['UN80'],'At a full fibre $mC$ of $q_Z$,',
 'The invariant vertical field is fixed by this free action',r'''At a full fibre $mC$ apply
\cref{lem:II:identity-monodromy-elliptic} with
$(E_0,q,B)=(Z,q_Z,B)$. Use its fixed elliptic curve $F$
with the period marking of $W$. Its root quotient
\eqref{cdp:eq:C.EP.8} is written here with elliptic
coordinate $u'$, root base coordinate $z$, and
order-$m$ translation $\eta$. Thus its coordinate map
is $(z,s,\tau)=(u',z,\eta)$ and the
original base function is $t=z^m$. The inverse gauge
maps in that lemma identify the original root family
and this constant-translation quotient over the same
base disc; their derivative in the elliptic direction
is the identity.
''')
new['UN80']=un80

un83=old['UN83'].replace('the general quasibundle clause of '+r'\cref{lem:II:elliptic-star-boundary}',
 r'\cref{lem:II:identity-monodromy-elliptic}',1)
un83=un83.replace('with $(P,q,B)=(Z,q_0,B_0)$',
 'with $(E_0,q,B)=(Z,q_0,B_0)$',1)
un83=cut(un83,'For the full fibre $nJ_0$,',
 'A rational boundary cannot map nonconstantly',r'''For the full fibre $nJ_0$, apply
\cref{lem:II:identity-monodromy-elliptic} to this same
$(Z,q_Z,B)$ and $C=J_0$. Its connected root cover and
primitive conormal character give exact normal order
$n$ on $J_0$. The neighbourhood isomorphism $\pi$ pulls
that line back to $N_{J/T}$, whose order is $m$;
therefore $n=m$. ''')
new['UN83']=un83

# The two graph owners and their full receivers are supplied below.

restriction_eq=eq(r'''r_{v,e}:H^1(T_v,\OO_{T_v})
                 \longrightarrow H^1(C_e,\OO_{C_e}),''','C.HR.1')
incidence_eq=eq(r'''d_1:\bigoplus_vH^1(T_v,\OO_{T_v})
             \longrightarrow\bigoplus_eH^1(C_e,\OO_{C_e}),
 \qquad(d_1a)_e=r_{v,e}a_v-r_{w,e}a_w
 \quad(e:v\to w).''','C.HR.2')
normalization_eq=eq(r'''0\longrightarrow\OO_S
 \longrightarrow\bigoplus_{v\in V}\OO_{T_v}
 \xrightarrow{\ d\ }\bigoplus_{e\in E}\OO_{C_e}
 \longrightarrow0.''','C.HR.5','C.PT.3','C.QT.4')
long_exact=eq(r'''\begin{gathered}
 0\longrightarrow\operatorname{coker}d_0
 \longrightarrow H^1(S,\OO_S)
 \longrightarrow\ker d_1\longrightarrow0,\\
 H^2(S,\OO_S)\simeq\operatorname{coker}d_1.
 \end{gathered}''','C.HR.6')
cohS=eq(r'''(h^0,h^1,h^2)(S,\OO_S)=(1,2,1).''','C.HR.3','C.QT.5')
rootcoh=eq(r'''H^2(S,\OO_S)\xrightarrow{\sim}H^2(P,\OO_P),
 \qquad H^1(S,\OO_S)\xrightarrow{\sim}H^1(P,\OO_P).''','C.PT.4')
residue=eq(r'''0\longrightarrow K_{T_v}
 \longrightarrow K_{T_v}(D_v)
 \xrightarrow{\operatorname{Res}}\bigoplus_{e\ni v}K_{C_e}
 \longrightarrow0.''','C.HR.7')
rootforms=eq(r'''H^0(S,\omega_S)\xrightarrow{\sim}H^0(P,K_P).''','C.PT.5')
eval_eq=eq(r'''\frac{x^{k_v-k_0}y^{k_w-k_0}\,dx\wedge dy\wedge dz}{xy}
 \quad\longmapsto\quad
 y^{k_w-k_0-1}\,dy\wedge dz\quad\text{on }x=0,
 \qquad k_v=k_0.''','C.HR.8')
p363=r'''\begin{lemma}[Cohomology and residues on a support graph]\hypertarget{tag-P363}{}\label{lem:II:support-incidence-residues}
\StatementRecord{lem:II:support-incidence-residues}{proved}{P363}{\cref{cdp:st:C.2.UN.17,cdp:st:C.2.UN.44}}
Let $f:U\to\Delta$ be a proper degeneration of connected
complex two-tori from a smooth threefold. Suppose its full
central fibre $S=\bigcup_{v\in V}T_v$ is reduced SNC,
with connected smooth components, disjoint smooth elliptic
double curves $C_e$, and no triple points. Let $G=(V,E)$
be its incidence graph. For an oriented edge $e:v\to w$,
identify its two copies with $C_e$ by the given gluing map,
and write
@@RESTRICTION@@
for the endpoint restrictions. Define
@@INCIDENCE@@
The normalization sequence is
@@NORMALIZATION@@
where $d$ is the difference of the two restrictions at each
edge. Its map on constants is the signed incidence map $d_0$.

\begin{enumerate}[label=(\arabic*),leftmargin=*]
\item Suppose $h^\bullet(T_v,\OO_{T_v})=(1,1,0)$ for every
vertex and every $r_{v,e}$ is nonzero. Then $G$ is unicyclic,
$d_1$ has rank $|V|-1$, and
@@LONG@@
In any nonzero endpoint and edge bases, the product of
$r_{v,e}/r_{w,e}$ along the oriented cycle is one. It is
independent of those bases, and
@@COHS@@
Every nonzero section of $\omega_S$ has nonzero residues
exactly on the cycle edges. Its component two-forms are
nonzero exactly on the cycle components. A canonical
evaluation generator has its minimum vertical order
exactly on those components.

\item Suppose $G$ is a nontrivial tree with distinguished
vertex $P$, and the preceding dimensions and nonzero
restriction conditions hold at every vertex other than $P$.
The restriction maps at $P$ are arbitrary. Restriction gives
@@ROOTCOH@@
and
@@ROOTFORMS@@
The inverse of the last map puts the given holomorphic
two-form on $P$ and zero on all other components. Every
edge residue is zero. The minimum canonical evaluation
order is attained uniquely at $P$.
\end{enumerate}
\end{lemma}
\begin{proof}
At a double curve the local functions on $xy=0$ are the
pairs of functions on $x=0$ and $y=0$ agreeing on $x=y=0$.
Their difference map is surjective onto the functions on
that curve. These descriptions, with the given gluing maps,
prove \eqref{cdp:eq:C.HR.5}. Connectedness makes
$\operatorname{rank}d_0=|V|-1$. When all component second
cohomology groups vanish, its long exact sequence is
\eqref{cdp:eq:C.HR.6}.

Choose a spanning tree and a nonzero value at one vertex.
The equations $r_{v,e}a_v=r_{w,e}a_w$ determine nonzero
values successively along it. Hence its $|V|-1$ rows are
independent, with a one-dimensional kernel. For a tree
$d_1$ would be surjective and $H^2(S,\OO_S)$ would vanish.
The map $f$ is flat: its nonzero base parameter is a
non-zero-divisor in the regular local rings of $U$, and a
torsion-free module over the base discrete valuation ring
is flat. Proper flat semicontinuity instead gives
$h^2(S,\OO_S)\ge h^2(F_t,\OO_{F_t})=1$.

Apply \cref{cdp:st:C.2.UN.44} to this $f$, with every
component multiplicity equal to one. Its meridian quotient
makes $\pi_1(S)$ abelian. Its map to the SNC dual complex
is a surjection onto $\pi_1(G)$, because the absence of
triple points makes that complex this same graph.
The free graph group is therefore abelian and has rank
at most one. The preceding exclusion of trees gives
$|E|=|V|$. After the spanning-tree equations there is
one remaining row. It vanishes on their kernel precisely
when the endpoint-ratio product around the cycle is one.
A nonzero last row would make $d_1$ invertible and again
give $H^2(S,\OO_S)=0$. Thus its rank is $|V|-1$.
Equation \eqref{cdp:eq:C.HR.6} now proves
\eqref{cdp:eq:C.HR.3}. A vertex-basis scalar occurs once
in a numerator and once in a denominator; an edge-basis
scalar cancels inside its ratio. This proves the stated
basis independence with the given restriction maps.

For the rooted tree, order the nonroot columns from leaves
towards $P$. The submatrix of $d_1$ on these columns is
square. Its leaf pivot is the nonzero restriction at that
leaf, and successive elimination proves it invertible.
Consequently $d_1$ is onto, and projection from its kernel
to $H^1(P,\OO_P)$ is an isomorphism: every root value
has one uniquely determined vector of nonroot values.
The tree map $d_0$ is onto. The normalization long exact
sequence therefore gives both restriction isomorphisms
in \eqref{cdp:eq:C.PT.4}, using the vanishing of
$H^2(T_v,\OO_{T_v})$ away from $P$.

Put $D_v=\bigcup_{e\ni v}C_e$ on $T_v$. Its disjoint
smooth branches give the residue sequence
@@RESIDUE@@
Serre duality identifies its residue connecting map with
the duals of the same endpoint restrictions. In a double
chart $xy=0$, a dualizing two-form has opposite residues
on its two branches. Assign the edge residue on its tail
and its negative on its head. When every component has
$H^0(K_{T_v})=0$, the global residue vector is exactly
$\ker d_1^\vee$: the component residue obstruction
vanishes precisely on that kernel, and the component
lifts are unique. Conversely those unique lifts glue by
the opposite-residue rule. These constructions are inverse.

At a leaf of an attached tree, its nonzero dual restriction
coefficient forces the edge residue to vanish. Delete that
leaf and repeat. Thus all tree residues vanish. On the
remaining cycle the two adjacent residues at each vertex
are related by nonzero coefficients; its one-dimensional
kernel has every cycle residue nonzero. A component with
all residues zero has an ordinary holomorphic two-form,
which is zero in the unicyclic case. A cycle component
has its two nonzero residues and hence a nonzero form.
For a rooted tree the same elimination stops at $P$.
Every other component form vanishes, and the form on $P$
has zero residues and is holomorphic. Extension by zero
and restriction are inverse, proving
\eqref{cdp:eq:C.PT.5}.

Take the canonical evaluation section from
\cref{cdp:st:C.2.UN.17}, using $dt$ to identify its
canonical and relative canonical lines. Write its
vertical divisor as $\sum k_vT_v$ and set $k_0=\min k_v$.
Since the full fibre is the reduced divisor of $t$,
division by $t^{k_0}$ is holomorphic and has nonzero
restriction to $S$. Near an edge, with $t=xy$, its
adjunction map is, up to a holomorphic unit,
@@EVALUATION@@
The restriction on $x=0$ is zero when $k_v>k_0$.
At a smooth point of a minimum-order component it is
nonzero. Thus its nonzero component forms identify
exactly the minimum-order components. The residue
descriptions just proved give the two asserted minimum
loci. In the tree case they also show that
$H^0(P,K_P)$ contains the resulting nonzero form.
\end{proof}'''
for marker,value in [('RESTRICTION',restriction_eq),('INCIDENCE',incidence_eq),('NORMALIZATION',normalization_eq),('LONG',long_exact),('COHS',cohS),('ROOTCOH',rootcoh),('ROOTFORMS',rootforms),('RESIDUE',residue),('EVALUATION',eval_eq)]:p363=p363.replace('@@'+marker+'@@',value)
new['P363']=p363

un54=r'''\begin{proposition}[Hopf support graphs and diagonal cycles]\hypertarget{tag-01DZ}{}\label{cdp:st:C.2.UN.54}
\StatementRecord{cdp:st:C.2.UN.54}{proved}{01DZ}{\cref{lem:II:hopf-curves,lem:II:hopf-curve-restriction,lem:II:support-incidence-residues,cdp:st:C.2.UN.38,cdp:st:C.2.UN.43,cdp:st:C.2.UN.46,cdp:st:C.2.UN.48}}
Let $f:U\to\Delta$ be a proper degeneration of connected
complex two-tori from a smooth threefold, whose full
central fibre $S=\bigcup_vH_v$ is reduced SNC and whose
components are primary or secondary Hopf surfaces.
Its connected double curves are elliptic, it has no
triple points, and its incidence graph is unicyclic.

For these same components and their given curve-gluing
maps, the restrictions \eqref{cdp:eq:C.HR.1} are
isomorphisms, the incidence map \eqref{cdp:eq:C.HR.2}
has rank $|V|-1$, and the endpoint-ratio product around
the cycle is one. In particular
$h^\bullet(S,\OO_S)=(1,2,1)$. A nonzero section of
$\omega_S$ has nonzero residues exactly on the cycle
edges, and its component forms are nonzero exactly on
the cycle components. These are precisely the components
of minimum canonical evaluation order.

When every component has algebraic dimension zero, each
is diagonal and the graph is a cycle with at least two
vertices. More generally, a compact reduced SNC surface
all of whose components are algebraic-dimension-zero
Hopf surfaces is a full fibre of a smooth-total
two-torus degeneration exactly when its components
are diagonal, its graph is such a cycle, its axis
normal lines are dual, and the integral edge product
$M$ of \cref{cdp:eq:C.HC.3,cdp:eq:C.HC.4,cdp:eq:C.HC.5,cdp:eq:C.HC.6}
is the identity. Every such marked support has the
compact realization of \cref{cdp:st:C.2.UN.48}, with
Euler number zero for every reduced fibre support.
\end{proposition}
\begin{proof}
Apply \cref{lem:II:hopf-curves} to every $H_v$.
Its irreducible compact curves are smooth elliptic
and pairwise disjoint. Thus the double curves have
these properties and there are no triple points.
\Cref{lem:II:hopf-curve-restriction} gives
$h^\bullet(H_v,\OO_{H_v})=(1,1,0)$ and a nonzero
restriction for each inclusion $C_e\hookrightarrow H_v$.
At the other endpoint compose its restriction with
pullback by the given elliptic gluing isomorphism.
These are exactly the two endpoint maps in
\eqref{cdp:eq:C.HR.1}. For a secondary component the
same lemma compares them through the finite unramified
primary cover and the component of its inverse curve;
the two finite pullbacks and the restriction square
are its stated maps. The primary constant deck class
restricts with the covering-subgroup multiplicity $d$
in \eqref{cdp:eq:C.HR.4}.

Apply the first clause of
\cref{lem:II:support-incidence-residues} with
$T_v=H_v$ and these $C_e,r_{v,e}$. It gives the
unicyclic graph, rank, exact cycle product, coherent
dimensions, residue support and minimum-order locus.

In algebraic dimension zero,
\cref{cdp:st:C.2.UN.38,cdp:st:C.2.UN.43} give the
nonlinear single elliptic curve and the diagonal
two-axis alternatives, including their finite primary
covers. The inverse image of a quotient curve is a
nonempty union of primary curves, and different
quotient curves have disjoint inverse images.
Since the primary surface has at most two curves,
each quotient component has at most two boundary
curves. A connected unicyclic graph satisfies
$|E|=|V|$, so its average degree is two. Every degree
is therefore two. Its two boundary curves lift to
the two distinct primary axes, so the finite deck
group preserves each axis and the marked component
is diagonal. Thus the graph is a diagonal cycle.
Its components are embedded
and smooth, so an edge joins two distinct components;
there are at least two vertices.

For this cycle the equation $t=xy$ identifies the
two actual normal lines as dual. Removing the axes
gives the open groups and affine logarithmic maps
of \cref{cdp:eq:C.HC.3,cdp:eq:C.HC.4,cdp:eq:C.HC.5,cdp:eq:C.HC.6}.
Their integral product is this same $M$.
\Cref{cdp:st:C.2.UN.46} gives necessity of $M=I$
through the included lattice in the nearby fundamental
group. Conversely its plumbing uses the given component,
axis and normal-product maps, and
\cref{cdp:st:C.2.UN.48} compactifies that family with
the same central support and all gluing constants.
Its Euler conclusion applies to every reduced support
of this compact realization.
\end{proof}'''
new['UN54']=un54

height_eq=eq(r'''h_v:=k_v-k_0=
 \begin{cases}
 0,&v\in V_0,\\
 \displaystyle\sum_{e\text{ on the path from }V_0\text{ to }v}m_e,
       &v\notin V_0.
 \end{cases}''','C.HT.2','C.PT.1')
period_eq=eq(r'''P(t)=\int_{\gamma_t}\omega_t.''','C.HT.3')
component_divisor=eq(r'''\operatorname{div}(\eta_v)
       =\sum_{e=(v,w)}(k_w-k_v-1)J_e.''','C.HT.7','C.QT.7')
edge_integer=eq(r'''\begin{gathered}
 d_{v,e}:=\frac{k_w-k_v}{m_e}
       =\operatorname{ord}_{q_v(J_e)}\theta_v+1\in\Z,\\
 \sum_{e\ni v}d_{v,e}=\operatorname{val}(v)-2
       \qquad (B_v=\PP^1).
 \end{gathered}''','C.HT.8','C.HT.9','C.PT.9','C.QT.8')
collar_eq=eq(r'''xy=t,\qquad q_v=x^{m_e},\qquad q_w=y^{m_e},
 \qquad x^{m_e}=c\ \longleftrightarrow\ y^{m_e}=t^{m_e}/c.''','C.HT.10')
regular_period=eq(r'''P(t)=O(t^{h_v+1})
       \qquad\text{at every quasibundle vertex}.''','C.HT.11','C.QT.9')
nonlinear_period=eq(r'''P(t)=t^{h_v}
 \left(\frac{\pm2\pi i c_v\beta_v^{-m_e}}{n_v}+O(t)\right),
 \qquad c_v\ne0,
 \quad\text{at a nonlinear leaf}.''','C.HT.12','C.PT.10','C.QT.10')
root_canonical=eq(r'''\operatorname{div}(\eta_P)=\sum_{e\ni P}(m_e-1)J_e,
 \qquad K_P\simeq\OO_P\Bigl(\sum_{e\ni P}(m_e-1)J_e\Bigr).''','C.PT.2')
p364=r'''\begin{lemma}[Canonical heights and the common elliptic period]\hypertarget{tag-P364}{}\label{lem:II:support-heights-period}
\StatementRecord{lem:II:support-heights-period}{proved}{P364}{\cref{lem:II:support-incidence-residues,lem:II:identity-monodromy-elliptic,lem:II:elliptic-star-boundary,lem:II:hopf-curve-restriction,lem:II:normal-product-collars,cdp:st:C.2.UN.17}}
Let $f:U\to\Delta$ be a proper degeneration of connected
complex two-tori from a smooth threefold, with full
reduced SNC central fibre, disjoint smooth elliptic
double curves, and no triple points. Every component
is either a nonlinear Hopf leaf from
\cref{cdp:eq:C.AS.1,cdp:eq:C.AS.2}, or a smooth elliptic
quasibundle $q_v:T_v\to B_v$ with fixed Jacobian and
identity integral monodromy. Every double curve on a
quasibundle is a fibre support. Consider the following
two domains:
\begin{enumerate}[label=(\arabic*),leftmargin=*]
\item Every $B_v$ is $\PP^1$. Then the incidence graph is
unicyclic. Let $V_0$ be its cycle vertices.
\item The graph is a nontrivial tree, one distinguished
component $P$ has elliptic base $B_P$, and every other
quasibundle base is $\PP^1$. Put $V_0=\{P\}$.
\end{enumerate}
Let $k_v$ be the canonical evaluation orders of
\cref{cdp:st:C.2.UN.17}. Their minimum $k_0$ is attained
exactly on $V_0$. Every multiple fibre of every $q_v$
is a double curve. At an edge $e$, the common exact
normal order $m_e$ is the full fibre multiplicity at
each quasibundle endpoint and the resonance at a
nonlinear endpoint. The dual-normal map identifies
the connected normal-root covers and their Jacobians.
In the unicyclic case the product of these Jacobian
identifications around the cycle is the identity;
the corresponding elliptic product may be a translation.

Root the trees at $V_0$. The heights are
@@HEIGHT@@
On a quasibundle write the canonical component form as
$\eta_v=q_v^*\theta_v\wedge\alpha_{F_v}$, using the
fixed invariant fibre form of
\cref{lem:II:identity-monodromy-elliptic}. On a cycle
vertex, a coordinate with its two cycle points at
$0,\infty$ gives $\theta_v=c_v\,dz/z$.
On a genus-zero tree vertex, a coordinate with its
parent point at infinity gives $\theta_v=c_v\,dz$.
Each constant is nonzero. In the rooted case
$\theta_P$ is a nowhere-zero holomorphic differential
on $B_P$ and
@@ROOTCANONICAL@@

Every regular elliptic fibre of every $q_v$ and every
oriented nonlinear Hopf core represents one transported
integral class $\gamma$ in the nearby two-torus.
For the relative canonical evaluation divided by
$t^{k_0}$, put
@@PERIOD@@
This period extends holomorphically to zero and satisfies
@@REGULAR@@
and
@@NONLINEAR@@
where $H_{m_e}^{\rm nl}(\beta_v)/\mu_{n_v}$ is the marked
leaf pair and the sign is its orientation sign.
When a nonlinear leaf occurs, $P$ has finite positive
order $R$, every nonlinear leaf has height $R$, and
every quasibundle vertex has height less than $R$.
In the absence of nonlinear leaves, $P$ may vanish
identically.
\end{lemma}
\begin{proof}
Every quasibundle is relatively minimal, since its
vertical curves are elliptic. Apply
\cref{lem:II:identity-monodromy-elliptic} to its
given $q_v$ and full fibre $mJ$. The root quotient
\eqref{cdp:eq:C.HT.4} gives exact normal order $m$
and connected normal-root cover $F_v\to J$.
The nonlinear leaf's normal has order equal to its
resonance, by \cref{def:II:elliptic-star-data}, including
the finite character in \eqref{cdp:eq:C.SN.4}.
The equation $xy=t$ identifies the two normal lines
as dual. Taking their unit-frame covers, and inverting
one normal character, gives the same connected cyclic
cover over this double curve. It identifies their
exact orders and their elliptic Jacobians. Choices
of the root trivialization change these cover maps
only by deck translations.

For a genus-zero quasibundle, \eqref{cdp:eq:C.QT.3}
gives $h^\bullet(\OO)=(1,1,0)$ and nonzero boundary
restrictions through its stated root square.
For a nonlinear leaf these conclusions follow from
\cref{lem:II:hopf-curve-restriction}. In the first
domain apply the unicyclic clause of
\cref{lem:II:support-incidence-residues}; in the
second apply its rooted-tree clause with this $P$.
They give the asserted graph and precisely the
minimum-order set $V_0$.

The adjunction construction of
\cref{cdp:st:C.2.UN.17}, with every full-fibre
multiplicity equal to one, gives a nonzero
meromorphic two-form $\eta_v$ on each component,
with exact divisor
@@COMPONENT@@
In a double chart this is the residue after dividing
the canonical evaluation by $t^{k_v+1}$.
On the component core the evaluation has no other
zero or pole, so the divisor has exactly this support.
For a quasibundle apply the vertical-form clause of
\cref{lem:II:identity-monodromy-elliptic} to this
particular $\eta_v$. At an unmarked fibre its order
is zero. Formula \eqref{cdp:eq:C.HT.6} would give
$m\operatorname{ord}\theta_v+m-1=0$, which forces
$m=1$. Thus every multiple fibre is marked.
At a marked fibre the same formula gives
@@EDGE@@
The sum in the second line follows because the
divisor of a rational differential has degree $-2$.
At a smooth unmarked value its order
is zero. Opposite edge orientations negate $d_{v,e}$,
since their common $m_e$ is the exact normal order.

On an edge inside $V_0$ both endpoint orders are
$k_0$, so its difference is zero. A terminal
quasibundle vertex has just its parent edge;
\eqref{cdp:eq:C.HT.9} makes its outward height
increment $m_e$. At a nonlinear leaf apply the
leaf-local clause of \cref{lem:II:elliptic-star-boundary}
with its own neighbouring component as $P$.
Equation \eqref{cdp:eq:C.NS.8} gives the same
increment, with $r=m_e$ and the same evaluation
orders. Now proceed from leaves towards $V_0$.
At a vertex with $c$ child edges of outgoing value
one, \eqref{cdp:eq:C.HT.9} reads
$-d_{\rm parent}+c=c-1$. Therefore the parent
increment also equals $m_e$. This proves
\eqref{cdp:eq:C.HT.2} along every path.

At a cycle vertex the two cycle points have
$d=0$, hence simple poles of $\theta_v$;
each child point has $d=1$ and order zero.
There are no other zeros or poles, giving
$c_v\,dz/z$. At a genus-zero tree vertex the
parent has $d=-1$, hence a double pole at
infinity, and every child has order zero.
This gives $c_v\,dz$. At the elliptic root
all outgoing values are one, so $\theta_P$
has no zero or pole; substitution into
\eqref{cdp:eq:C.HT.7} gives
\eqref{cdp:eq:C.PT.2} as the divisor of that
same canonical section.

In the unicyclic case use the restriction square
of \cref{lem:II:identity-monodromy-elliptic} on
each cycle component. Its composite restriction
and root pullback evaluates the fixed
$H^1(F_v,\OO_{F_v})$ frame. Thus the product of
the given lifted elliptic identifications acts
on this line by the endpoint-ratio product
in \eqref{cdp:eq:C.HR.2}. That product is one
by \cref{lem:II:support-incidence-residues}.
An elliptic isomorphism lifted to universal
covers is $z\mapsto az+b$. It multiplies
the invariant holomorphic one-form by $a$
and its conjugate, representing $H^1(\OO)$,
by $\overline a$. Hence the product has
linear part one and is a translation. This
retains its translation and the given root
cover maps.

To compare integral cycles, pass to the common
normal-root cover at an edge between quasibundles.
Their normal-power trivializations differ by a
nonzero holomorphic function on the compact
double curve, hence by a constant. Multiplying
one base coordinate by that constant gives
the exact collar equations
@@COLLAR@@
The two levels are the same connected elliptic
cover with its complex orientation. Varying
the nonzero normal level gives an oriented
isotopy between them. Apply
\cref{lem:II:normal-product-collars} to this
same full reduced SNC support, its normal
line product maps, and these component cores.
Its product-preserving smooth comparison
carries the collar isotopies to the given
smoothing, and its core transport agrees
on both attaching ends. Within each
quasibundle the regular fibres are isotopic
along paths avoiding the finite marked set.
At a nonlinear leaf the boundary map
\eqref{cdp:eq:C.SN.6} in
\cref{lem:II:elliptic-star-boundary} sends
the Hopf fibre generators to the same $e,h$
and its meridian to the product-filling
meridian. Its smooth pair map identifies
the oriented Hopf core with that regular
elliptic fibre. These maps preserve the
full secondary integer $n_v$. Composing
along edges proves equality of the stated
integral classes in the nearby fibre.

On a compact regular fibre in $T_v$, the
leading coefficient of the relative form
is $t^{h_v}\eta_v$. Its restriction to
that holomorphic curve is zero. Smooth
compact-core transport therefore gives
\eqref{cdp:eq:C.HT.11}. At a nonlinear
leaf apply the individual period clause
of \cref{lem:II:elliptic-star-boundary}
with its own parent order $k_{\mathrm{par}}$.
Multiplying its expression by
$t^{k_{\mathrm{par}}-k_0}$ changes the leading
power from $r$ to $k_v-k_0=h_v$ and gives
\eqref{cdp:eq:C.HT.12}, with exactly its
primitive core lattice and coefficient
$\pm2\pi i c_v\beta_v^{-r}/n_v$.
Differentiation under the integral and
Stokes' theorem show that all these
integrals are the same holomorphic period
on the punctured disc. Their compact-core
expressions give a holomorphic extension
at zero and the displayed orders. A
nonlinear coefficient is nonzero, so one
leaf fixes its order $R=h_v>0$; the other
leaf expansions give the same height,
and \eqref{cdp:eq:C.HT.11} makes every
quasibundle height smaller.
\end{proof}'''
for marker,value in [('HEIGHT',height_eq),('ROOTCANONICAL',root_canonical),('PERIOD',period_eq),('REGULAR',regular_period),('NONLINEAR',nonlinear_period),('COMPONENT',component_divisor),('EDGE',edge_integer),('COLLAR',collar_eq)]:p364=p364.replace('@@'+marker+'@@',value)
new['P364']=p364

un58=render(r'''\begin{proposition}[Canonical heights of Hopf support trees]\hypertarget{tag-01E3}{}\label{cdp:st:C.2.UN.58}
\StatementRecord{cdp:st:C.2.UN.58}{proved}{01E3}{\cref{cdp:st:C.2.UN.54,cdp:st:C.2.UN.38,cdp:st:C.2.UN.37,lem:II:support-heights-period,def:II:elliptic-star-data}}
Let $S$ be the full reduced SNC central fibre of a
proper degeneration of connected complex two-tori
from a smooth threefold, with every component a
primary or secondary Hopf surface. A diagonal
algebraic-dimension-zero component forces the whole
support to be a diagonal cycle classified by
\cref{cdp:st:C.2.UN.46,cdp:st:C.2.UN.48}.

In every other case the graph is unicyclic. Every
cycle vertex and every nonterminal tree vertex
has algebraic dimension one and its elliptic
reduction is
@@HT.1@@
with fixed Jacobian, identity integral monodromy
and only smooth multiple fibre supports. Every
other vertex is a nonlinear algebraic-dimension-zero
Hopf leaf or has this same elliptic reduction.
Every multiple fibre is a double curve.

The exact normal order $m_e$ on an edge equals
the full multiplicity at each elliptic endpoint
and the resonance at a nonlinear endpoint.
The given dual-normal map identifies the
connected normal-root covers and their Jacobians.
The Jacobian product around the cycle is the
identity; the elliptic product may be a translation.

For the canonical evaluation orders, put
$k_0=\min k_v$. This minimum is attained exactly
on the cycle, and the heights are
\eqref{cdp:eq:C.HT.2}, with $V_0$ its cycle vertices.
After factoring out the invariant relative
elliptic form, the component base differential
is $c_v\,dz/z$ on a cycle vertex with its cycle
points at $0,\infty$, and $c_v\,dz$ on a tree
vertex with its parent point at infinity,
where $c_v\ne0$.

All regular elliptic fibres and nonlinear
cores represent the integral class $\gamma$
of \cref{lem:II:support-heights-period}.
For its period \eqref{cdp:eq:C.HT.3}, a nonlinear
leaf forces a finite positive order $R$.
Every nonlinear leaf has height $R$, and
every algebraic-dimension-one vertex has
height less than $R$. With no nonlinear
leaf this period may vanish identically.
\end{proposition}
\begin{proof}
Apply the normal-character calculation in
\cref{cdp:st:C.2.UN.38} to the same diagonal
primary surface and its marked axis $w=0$.
Its normal is exactly the quotient line
$(z,v)\sim(\alpha z,\beta v)$ in that
calculation, so it has infinite order in
algebraic dimension zero. Interchanging
the coordinates gives the other axis.
A torsion line on
a secondary surface pulls back to a torsion
line on its finite primary cover, so the
axis normals there are also nontorsion.

For an algebraic-dimension-one Hopf surface,
\cref{cdp:st:C.2.UN.37} gives the stated
elliptic reduction. A horizontal compact
curve would meet a regular fibre, whereas
$H^2(H,\mathbb Q)=0$ makes their intersection
zero. Positivity of local intersections
therefore makes every curve a fibre support.
Apply \cref{lem:II:identity-monodromy-elliptic}
to this reduction: every boundary normal
has finite exact order equal to its full
fibre multiplicity. For a nonlinear Hopf
axis, \cref{def:II:elliptic-star-data} gives
the finite exact resonance order, including
its secondary normal character.

At an SNC edge the map $xy=t$ identifies
the normals as dual and preserves whether
their tensor powers are trivial. Hence
a diagonal algebraic-dimension-zero vertex
can meet only another such vertex.
Connectedness makes all components of that
type, and \cref{cdp:st:C.2.UN.54} gives the
diagonal-cycle conclusion.

Otherwise each algebraic-dimension-zero
component is nonlinear and has its one
elliptic curve, so it is a leaf. The
remaining components have the reductions
\eqref{cdp:eq:C.HT.1}. Their full support
therefore satisfies the first domain of
\cref{lem:II:support-heights-period}, with
$T_v=H_v$ and these given reductions,
double-curve maps and normal dualities.
That lemma proves absence of unmarked
multiple fibres, the normal-root and
Jacobian comparisons, the stated heights
and base differentials, and the integral
core and period conclusions. Its nonlinear
coefficient uses the full primitive lattice
of each given $H_r(\beta)/\mu_n$; it is
\eqref{cdp:eq:C.HT.12} for these same leaves.
\end{proof}''')
new['UN58']=un58

un61=old['UN61']
un61=un61.replace('Set $h_P=0$ and\n'+equations['cdp:eq:C.PT.1'][1],
 'Define the heights by \\eqref{cdp:eq:C.PT.1}, with $V_0=\\{P\\}$.')
un61=un61.replace('and its actual canonical\ndivisor is\n'+equations['cdp:eq:C.PT.2'][1],
 'and its canonical\nsection has the divisor \\eqref{cdp:eq:C.PT.2}.')
start=r'\item \par\medskip\noindent\textbf{The root cohomology is forced by the actual incidence maps.}'
end=r'\item \par\medskip\noindent\textbf{The actual elliptic fibration on the root.}'
un61=cut(un61,start,end,render(r'''\item Every double curve has a nonroot endpoint.
At a Hopf endpoint, \cref{lem:II:hopf-curves} makes it
smooth elliptic and makes the distinct boundary curves
disjoint. At a quasibundle endpoint these properties
hold because the curves are distinct smooth fibre
supports. Hence there are no triple points, and the
curves on $P$ are also pairwise disjoint.

For each Hopf nonroot component use
\cref{lem:II:hopf-curve-restriction} for its coherent
dimensions and each given curve inclusion. For each
quasibundle use \cref{lem:II:identity-monodromy-elliptic}
with that same $q_v:T_v\to\PP^1$.
Equation \eqref{cdp:eq:C.QT.3} and its restriction
square give dimensions $(1,1,0)$ and the nonzero
endpoint maps through its connected normal-root cover.
Compose at each edge with the given gluing map.
The rooted-tree clause of
\cref{lem:II:support-incidence-residues}, with root
this arbitrary $P$, now applies. It gives the
restriction isomorphisms \eqref{cdp:eq:C.PT.4}
through the normalization sequence
\eqref{cdp:eq:C.PT.3}.

Flat semicontinuity gives $h^2(S,\OO_S)\ge1$,
and the compact-core bound of
\cref{cdp:st:C.2.UN.28} gives $p_g(P)\le1$.
Thus $p_g(P)=1$. Coherent Euler characteristic
is zero in this proper flat family. In the
normalization sequence every nonroot component
and every elliptic edge has coherent Euler
characteristic zero, so $\chi(\OO_P)=0$ and
$h^1(P,\OO_P)=2$. This proves both stated
coherent dimension vectors.

\item The same rooted-tree clause gives
\eqref{cdp:eq:C.PT.5} by restriction to $P$
and extension by zero to the other components.
Its canonical evaluation comparison
\eqref{cdp:eq:C.HR.8} identifies $P$ as the
unique minimum-order component. Write its
order as $k_0$. The resulting holomorphic
two-form on $P$ has exact divisor
@@PT.6@@
Its coefficients are nonnegative integers,
and its section has no zero away from this
boundary. A rational exceptional curve
$E$ of square $-1$ would satisfy
$K_P\cdot E=-1$ by adjunction. Each curve
in the displayed effective divisor is
elliptic and different from $E$, so their
intersections with $E$ are nonnegative.
This contradiction proves minimality of $P$.

'''))
start=r'\item \par\medskip\noindent\textbf{Finite normal roots and the exact height equations.}'
end=r'\item \par\medskip\noindent\textbf{The exact inverse torsor and its integral obstruction.}'
un61=cut(un61,start,end,r'''\item Apply \cref{lem:II:identity-monodromy-elliptic}
to the root map $q_P$ just constructed. Its normal-root
chart gives finite exact normal order at each marked
fibre. Duality carries that order to the adjacent
component. The nontorsion-axis calculation of
\cref{cdp:st:C.2.UN.58} excludes a first diagonal
algebraic-dimension-zero vertex along any path from
$P$. All such vertices are therefore absent.
A nonlinear Hopf component has its unique elliptic
curve and is terminal. Every other nonroot component
has the given genus-zero quasibundle, or the elliptic
Hopf reduction of \cref{cdp:st:C.2.UN.37}.
The boundary curves are fibre supports of these
maps. For an elliptic Hopf component this follows
from its vanishing rational second cohomology and
positivity of intersection, as in
\cref{cdp:st:C.2.UN.58}.

Apply the rooted domain of
\cref{lem:II:support-heights-period} to these
same maps, the distinguished $q_P:P\to B$,
the given full reduced SNC smoothing, and its
normal dualities. It excludes every unmarked
multiple fibre, identifies the connected normal
roots along the tree, and gives the common
Jacobian with its edge maps. Its integer
equation \eqref{cdp:eq:C.PT.9} gives precisely
the heights \eqref{cdp:eq:C.PT.1}; at the
root its canonical section has divisor
\eqref{cdp:eq:C.PT.2}.

Its collar comparison \eqref{cdp:eq:C.HT.10}
uses this same $xy=t$ smoothing and its
normal products. At a nonlinear leaf its
map \eqref{cdp:eq:C.SN.6} includes the full
secondary integer and both primitive fibre
circles. Thus its integral class is the
class of every regular fibre of these
given quasibundles, including the root.
Equations \cref{cdp:eq:C.HT.11,cdp:eq:C.PT.10}
are the expansions of that one period
for the evaluation divided by $t^{k_0}$.
They give the stated common value $R$ at
nonlinear leaves and the strict inequalities
at quasibundle vertices. This proves the
height test in every actual occurrence.

''')
new['UN61']=un61

un62=old['UN62']
start=r'\item \par\medskip\noindent\textbf{The actual root chart and its cohomology maps.}'
end=r'\item \par\medskip\noindent\textbf{Pruning with the full torsors.}'
un62=cut(un62,start,end,r'''\item Each given quasibundle
$q_v:T_v\to\PP^1$ is relatively minimal,
because its vertical primes are elliptic.
Apply \cref{lem:II:identity-monodromy-elliptic}
to this same map and each marked full fibre.
Its quotient \eqref{cdp:eq:C.QT.2} is the
normalized root of that fibre, and its
primitive character gives the exact normal
order. Formula \eqref{cdp:eq:C.QT.3} gives
the coherent dimensions and the commuting
restriction and root-pullback square.
For a nonlinear component use
\cref{lem:II:hopf-curve-restriction}; for
its secondary normal character use
\cref{def:II:elliptic-star-data}.
All boundary curves on each component are
disjoint, so the SNC support has no
triple points.

For an actual full reduced occurrence,
the first clause of
\cref{lem:II:support-incidence-residues}
applies to these components and exactly
these restriction and gluing maps. Its
normalization sequence is
\eqref{cdp:eq:C.QT.4}. It gives the
unicyclic graph, product-one coherent
holonomy, dimensions \eqref{cdp:eq:C.QT.5},
and the minimum canonical order precisely
on the cycle.

\item Apply the first domain of
\cref{lem:II:support-heights-period} with
the given maps \eqref{cdp:eq:C.QT.1},
the same nonlinear leaves and all the
normal-product identifications from the
smooth-total occurrence. The component
divisor is \eqref{cdp:eq:C.QT.7}; its
vertical-form expression and order are
\cref{cdp:eq:C.HT.5,cdp:eq:C.QT.6} in
\cref{lem:II:identity-monodromy-elliptic}.
The common owner consequently excludes
unmarked multiples, gives the exact
edge and degree equations
\eqref{cdp:eq:C.QT.8}, and identifies
the path heights and the base forms
$c\,dz/z$ and $c\,dz$ on the same
cycle and tree vertices. Its root-square
comparison also proves that the lifted
elliptic cycle product has identity
linear part, with its translation
unchanged.

The common integral class is obtained
by the normal-root collars of this
smoothing and the full secondary
boundary maps of its nonlinear leaves.
Its regular and nonlinear expansions
are \cref{cdp:eq:C.QT.9,cdp:eq:C.QT.10}
for the canonical evaluation divided
by its cycle minimum. A nonlinear leaf
fixes the one finite order $R$;
every other nonlinear leaf has that
height and every quasibundle vertex
has smaller height. With no nonlinear
leaf, any integer above all the
finitely many heights meets the
stated height requirement. This
proves necessity of the first three
conditions for the full given
quasibundle class.

''')
new['UN62']=un62

def identifiers(s):
 return Counter(re.findall(r'\\(?:label|hypertarget)\{([^}]+)\}',s))

# Every edit is a unique, full-statement-and-proof guard. The two
# new owners are inserted atomically with the first full consumers.
guards=[]
for name in ('P306','P350','P351','UN80','UN83','UN61','UN62'):
 guards.append(dict(statement_id=re.search(r'\\label\{([^}]+)\}',old[name]).group(1),old_text=old[name],new_text=new[name],reason='Complete proof compared; exact common-owner transfer and maps in package18 comparison.'))
heading=r'\subsection{Hopf support graphs and rational-root trees}\label{subsec:II:hopf-support-tree-remainder}'
a=current.index(heading);b=current.index(old['UN54'],a)+len(old['UN54'])
first_old=current[a:b]
assert current[a:b].endswith(old['UN54'])
first_new=r'\subsection{Cohomology and residues of support graphs}\label{subsec:II:hopf-support-tree-remainder}'+'\n\n'+new['P363']+'\n\n'+new['UN54']
guards.append(dict(statement_id='cdp:st:C.2.UN.54',old_text=first_old,new_text=first_new,reason='Place full P363 owner before full Hopf receiver; preserve original subsection identity.'))
second_heading=r'\subsection{Canonical and period reductions on Hopf trees}\label{subsec:II:hopf-tree-reductions}'
a=current.index(second_heading);b=current.index(old['UN58'],a)+len(old['UN58'])
second_old=current[a:b]
second_new=r'\subsection{Canonical heights and elliptic periods}\label{subsec:II:canonical-tree-heights}\label{subsec:II:hopf-tree-reductions}'+'\n\n'+new['P364']+'\n\n'+new['UN58']
guards.append(dict(statement_id='cdp:st:C.2.UN.58',old_text=second_old,new_text=second_new,reason='Place full P364 owner before full Hopf-height receiver; preserve the preceding subsection identity as an alias and leave no empty heading.'))
# An explicit open boundary keeps the later full realization work separate.
guards.append(dict(statement_id='subsec:II:tree-pruning-remainder',old_text=old['UN60'],new_text=r'\subsection{Pruning and compact realization of elliptic trees}\label{subsec:II:tree-pruning-remainder}'+'\n\n'+old['UN60'],reason='Insert the following open-unit heading; its statement and proof are byte-identical.'))

before='\n'.join(g['old_text'] for g in guards)
after='\n'.join(g['new_text'] for g in guards)
delta=identifiers(after)-identifiers(before)
lost=identifiers(before)-identifiers(after)
expected=Counter({'tag-P363':1,'lem:II:support-incidence-residues':1,'tag-P364':1,'lem:II:support-heights-period':1,'subsec:II:canonical-tree-heights':1,'subsec:II:tree-pruning-remainder':1})
assert not lost,lost
assert delta==expected,(delta,expected)
for g in guards:assert current.count(g['old_text'])==1,g['statement_id']
assert not re.search(r'@@[^@]+@@',after)
assert not re.search(r'\\eqref\{[^}]*,[^}]*\}',after)
for m in re.finditer(r'\\begin\{equation\}.*?\\end\{equation\}',after,re.S):
 assert m.group().count(r'\SsixEquationAliases')<=1,m.group()
 assert not re.search(r'\n\s*\n',m.group()),m.group()
for name,s in new.items():(out/f'{stem}_{name}_replacement.tex').write_text(s,newline='\n')
with (out/f'{stem}_remote_repairs.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['statement_id','old_text','new_text','reason'],delimiter='\t');w.writeheader();w.writerows(guards)
(out/f'{stem}_input.tex').write_text(first_old+'\n\n'+second_old,newline='\n')
(out/f'{stem}_replacement.tex').write_text(first_new+'\n\n'+second_new,newline='\n')
with (out/f'{stem}_equations.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['old_tag','target_label','old_owner','receiving_owner'],delimiter='\t');w.writeheader()
 for key,label in established.items():
  if label in moved:
   receiver=next(n for n,s in new.items() if r'\label{'+label+'}' in s)
   w.writerow(dict(old_tag=key,target_label=label,old_owner=equations[label][0],receiving_owner=receiver))
print('DRAFT',len(guards),'guards;',len(new),'full receiving blocks;',len(set(moved)),'numbered targets handled')
print('Identifier multiplicities preserved; additions:',dict(delta))

