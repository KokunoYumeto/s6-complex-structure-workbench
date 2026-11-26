#!/usr/bin/env python3
"""Prepare the complete elliptic-star consolidation outside the central source."""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import csv, re, hashlib

root = Path(__file__).resolve().parents[1]
out = root/'agents/continuation3_conductor'
stem = 'S6_SERIES_PUBLISH_c3_conductor_16'
current = (root/'S6_SERIES_PUBLISH_II.tex').read_text()
reference = (out/'S6_SERIES_PUBLISH_c3_conductor_sec10_initial_reference.tex').read_text()

def block(text, label, env):
    p = text.index(r'\label{'+label+'}')
    a = text.rfind(r'\begin{'+env+'}', 0, p)
    b = text.index(r'\end{proof}', p)+len(r'\end{proof}')
    return text[a:b]

def freeze(name, text):
    p = out/(stem+'_'+name+'.tex')
    if p.exists():
        assert p.read_text() == text, name
    else:
        p.write_text(text, newline='\n')

original = {n:block(reference, f'cdp:st:C.2.UN.{n}', 'proposition') for n in [49,50,53]}
for n, text in original.items():
    assert block(current, f'cdp:st:C.2.UN.{n}', 'proposition') == text
    freeze(f'UN{n}_input', text)
owner_labels = {325:'lem:II:reduced-anticanonical-hopf',
                330:'lem:II:zero-chern-elliptic-torsor',
                331:'lem:II:logarithmic-period-family',
                337:'lem:II:hopf-curve-restriction'}
owners = {n:block(current, label, 'lemma') for n,label in owner_labels.items()}
for n,text in owners.items():
    if n == 337 and (out/(stem+'_P337_input.tex')).exists():
        previous = (out/(stem+'_P337_input.tex')).read_text()
        assert previous[previous.index(r'\begin{proof}'):] == text[text.index(r'\begin{proof}'):]
    else:
        freeze(f'P{n}_input', text)

with (root/'agents/continuation2_B/D19/S6_SERIES_PUBLISH_II_B2_D19_v1_equation_map.tsv').open() as f:
    established = {row['old_tag']:row['target_label'] for row in csv.DictReader(f, delimiter='\t') if row['old_tag']}
equations = {}
for n,text in original.items():
    for m in re.finditer(r'\\\[.*?\\\]', text, re.S):
        tags = re.findall(r'\\tag\{([^}]+)\}', m.group())
        if tags:
            assert len(tags) == 1
            equations[tags[0]] = m.group()

used = []
alias_maps = []
def eq(key, aliases=(), map_text='The variables and maps are unchanged.'):
    key = 'C.'+key if not key.startswith('C.') else key
    s = equations[key]
    lab = re.search(r'\\label\{([^}]+)\}', s).group(1)
    assert established[key] == lab
    s = s.replace(r'\[', r'\begin{equation}', 1)
    s = s[:-2]+r'\end{equation}'
    s = s.replace(r'\tag{'+key+'}', '')
    used.append(key)
    targets, labels = [], []
    for alias in aliases:
        alias = 'C.'+alias if not alias.startswith('C.') else alias
        d = equations[alias]
        tag = re.search(r'\\hypertarget\{([^}]+)\}', d).group(1)
        label = re.search(r'\\label\{([^}]+)\}', d).group(1)
        targets.append(r'\hypertarget{'+tag+r'}{}')
        labels.append(r'\label{'+label+'}')
        alias_maps.append(dict(old_tag=alias,target_label=label,owner_tag=key,map=map_text))
        used.append(alias)
    if targets:
        s=s.replace(r'\end{equation}', '\n'+'\n'.join(targets)+'\n'+r'\SsixEquationAliases{'+''.join(labels)+'}\n'+r'\end{equation}')
    return re.sub(r'\n[ \t]*\n+', '\n', s)

def hook(key):
    key = 'C.'+key if not key.startswith('C.') else key
    s = equations[key]
    tag = re.search(r'\\hypertarget\{([^}]+)\}',s).group(1)
    label = re.search(r'\\label\{([^}]+)\}',s).group(1)
    used.append(key)
    return r'\hypertarget{'+tag+r'}{}\SsixEquationAliases{\label{'+label+'}}'

p325new = owners[325]
needle = r'$D=dC$ for one smooth elliptic curve $C$ and an integer $d\ge2$.'
replacement = r'''$D=dC$ for one smooth elliptic curve $C$ and an integer $d\ge2$.
There is a finite unramified central primary cover $\pi:H'\to H$ for
which $\pi^{-1}(C)$ is one curve. In coordinates marking this
curve by $w=0$, the primary contraction is either
$(z,w)\mapsto(\beta^r z+w^r,\beta w)$ or
$(z,w)\mapsto(\beta^r z,\beta w)$, with $r\ge1$,
$0<|\beta|<1$ and $d=r+1$.'''
assert p325new.count(needle) == 1
p325new = p325new.replace(needle, replacement, 1)
start = p325new.index('Otherwise choose positive integers $u,v$')
end = p325new.index('The monomials of $g$', start)
part = p325new[start:end]
part = part.replace('$u=dq$, $v=dp$', '$u=eq$, $v=ep$').replace('$F^d$', '$F^e$').replace('F^d','F^e').replace(r'\alpha^d',r'\alpha^e').replace(r'\beta^d',r'\beta^e')
p325new = p325new[:start]+part+p325new[end:]
needle = 'Pullback to this cover retains every coefficient of $D_P$.\nThe monomials of $g$ now have weight $p+q$.'
replacement = r'''Pullback to this cover retains every coefficient of $D_P$.
Writing $F$ for its central generator $F^e$, its coordinate form is
'''+eq('AS.8')+r'''
The monomials of $g$ now have weight $p+q$. A weighted homogeneous
polynomial factors, after removing its axis monomial, into binomials
$z^q-cw^p$, each of weight $pq$: the ratios of two monomials of
equal weight are powers of $z^q/w^p$, and the resulting one-variable
polynomial factors over $\C$. Consequently, when the zero divisor
is $a$ times an orbit of $m$ such non-axis curves, its weight gives
'''+eq('AS.9')
assert p325new.count(needle) == 1
p325new = p325new.replace(needle, replacement, 1)
needle = 'In particular a coefficient-one component excludes the latter case.'
replacement = r'''In particular a coefficient-one component excludes the latter case.
In the nonreduced case its pullback to this primary cover also
has a coefficient greater than one, so the classification just
proved leaves exactly one curve. The nonlinear form gives
$d=r+1$ on its axis. In the diagonal calculation a single curve
comes from $w^{p+1}$ when $q=1$, from the exchanged case when
$p=1$, or from a repeated linear factor when $p=q=1$.
The coordinate changes above therefore mark it by $w=0$ and
put the contraction in the second form of the statement,
with $r=d-1$. These are the asserted primary-cover maps.'''
assert p325new.count(needle) == 1
p325new = p325new.replace(needle, replacement, 1)
needle = 'The logarithmic form $dz/z\\wedge dw/w$ is a nowhere-zero\nsection of the pulled-back canonical-boundary line, and spans\nits section space because the primary surface is compact and connected.'
replacement = r'''The logarithmic form
'''+eq('AS.11')+r'''
is a nowhere-zero section of the pulled-back canonical-boundary
line, and spans its section space because the primary surface
is compact and connected.'''
assert p325new.count(needle) == 1
p325new = p325new.replace(needle, replacement, 1)

p330new = owners[330]
needle = r'\hypertarget{tag-00WB}{}\SsixEquationAliases{\label{cdp:eq:C.PT.8}}'
assert p330new.count(needle) == 1
p330new = p330new.replace(needle, needle+'\n'+hook('NS.14'), 1)
alias_maps.append(dict(old_tag='C.NS.14', target_label='cdp:eq:C.NS.14', owner_tag='C.KX.14', map='The given torsor q0:T0->B is E1->B; (z,w) in KX14 is (p,z) in NS14, Gamma is Gamma_B and Lambda_F1 is Lambda_F. The cocycle coboundary map and its inverse preserve the full torsor over the same B.'))

p331new = owners[331]
needle = r'\hypertarget{tag-010P}{}\label{cdp:eq:C.TL.3}'
if needle not in p331new:
    needle = re.search(r'\\hypertarget\{[^}]+\}\{\}\\label\{cdp:eq:C.TL.3\}', p331new).group()
assert p331new.count(needle) == 1
p331new = p331new.replace(needle, needle+'\n'+hook('NS.15'), 1)
alias_maps.append(dict(old_tag='C.NS.15', target_label='cdp:eq:C.NS.15', owner_tag='C.TL.3', map='Set the TL3 base parameter z equal to t and its vector w equal to (p,z) in NS15. Then ell_t(p,z)=V_t((p,z)) exactly.'))
needle = r'In particular $V_0^\infty(w)=J\overline w$, where $J=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$.'
extension = needle+r'''

For every full rank-four lattice $\Lambda_0\subset\C^2$, the
sections $V_t(\lambda)$, $\lambda\in\Lambda_0$, define a free
translation action on $\OO_{\PP^1}(1)^{\oplus2}$, using
$V_s^\infty(\lambda)=J\overline\lambda+s\lambda$ in the frame
$s=t^{-1}$. Its quotient
\begin{equation}\label{eq:II:compact-twistor-lattice}
 \mathcal T(\Lambda_0)=\OO_{\PP^1}(1)^{\oplus2}/\Lambda_0
                  \longrightarrow\PP^1
\end{equation}
is a smooth proper family of connected complex two-tori with
central fibre $\C^2/\Lambda_0$. Its total space is compact.
In the coordinates $w=(p,z)$ and base parameter $t$, the same
sections are $\ell_t(p,z)=V_t((p,z))$ in
\eqref{cdp:eq:C.NS.15}. Pullback along $t=s^R$, for every
integer $R\ge1$, remains a smooth compact family. 
'''
assert p331new.count(needle) == 1
p331new = p331new.replace(needle, extension, 1)

definition = r'''\subsection{Elliptic star data and inverse transforms}\label{subsec:II:elliptic-star-data}

\begin{definition}[Marked elliptic stars and inverse transforms]\hypertarget{tag-P350}{}\label{def:II:elliptic-star-data}
\StatementRecord{def:II:elliptic-star-data}{proved}{P350}{\cref{lem:II:identity-monodromy-elliptic}}
The leaf pairs are
'''+eq('AS.1', aliases=['SN.1'], map_text='SN1 is the nonlinear pair in AS1; its finite action is exactly the action written in AS2. The primary specialization has n_i=1.')+r'''
with marked axis $J_i=\{w=0\}$ and contractions and finite action
'''+eq('AS.2')+r'''
A marked elliptic star consists of these pairs, a smooth compact
complex surface with a connected elliptic quasibundle
'''+eq('AS.3')+r'''
over a smooth compact connected curve $B$, and pairwise distinct
marked fibres with full divisors $r_iJ_i$. Here a quasibundle has
only positive multiples of smooth elliptic curves as fibres.
Its integral $H_1$ monodromy is the identity, and its smooth
fibres are torsors under one fixed elliptic curve $F$.
The data include the isomorphism from each marked leaf axis to
the corresponding $J_i\subset P$ and a duality between their
normal lines. These identifications form the reduced surface
$S=P\cup H_1\cup\cdots\cup H_n$, with $n\ge1$, disjoint
double curves and no other intersections.

For one marked fibre suppress the index and choose integers $k,l$ with
'''+eq('SN.3')+r'''
The paired neighbourhood in $P$, in the axis coordinate $z$
of the leaf cover, has the invariant coordinates
'''+eq('SN.4', aliases=['NS.1'], map_text='For n=1 choose k=0,l=-1. Then gamma=beta,u=z,X=x and p=X^r u=x^r z; the deck map is (z,x)->(beta^r z,beta^-1 x), exactly NS1.')+r'''
Here $u\ne0$. Its punctured product map and inverse are
'''+eq('SN.5', aliases=['NS.2'], map_text='For n=1,k=0,l=-1, (u,X)=(z,x) and W=x^-1 is the product coordinate w of NS2; u=pW^r and X=W^-1 give exactly its inverse.')+r'''
Replace each marked neighbourhood by the product $F\times\Delta_p$
through this punctured isomorphism, keeping every transition map
of $P$ away from the marked values. The resulting map is the
\emph{inverse logarithmic transform}
'''+eq('NS.3')+r'''
If there are no unmarked multiple fibres, it is a holomorphic
principal $F$-torsor. Its integral Chern vector is the connecting
class $c(T_0)\in H^2(B,\Lambda_F)$ of the sheaf sequence in
\eqref{cdp:eq:C.KX.13}, with $F_1=F$.
The transform preserves the full analytic torsor transition maps
and is independent, up to an isomorphism over $B$, of the
compatible local coordinates used in its construction.
\end{definition}
\begin{proof}
Every vertical prime of a quasibundle is elliptic, so it has
no vertical exceptional curve of the first kind and is relatively
minimal. The normalized root of a smooth full fibre $mJ$ is a
smooth elliptic product over a disc by
\cref{lem:II:identity-monodromy-elliptic}. In its fixed integral
marking, the cyclic deck map has the form
$(s,v)\mapsto(\zeta_m s,v+\tau(s))$.
Its central translation has exact order $m$, because this cyclic
action is free. Lift $\tau(s)$ near its central value to
$t(s)\in\C$, and put $u(s)=t(s)-t(0)$. The cyclic law gives
$\sum_{j=0}^{m-1}u(\zeta_m^j s)=0$. The holomorphic change
$v'=v+h(s)$, where
\[
 h(s)=-\frac1m\sum_{j=0}^{m-1}j\,u(\zeta_m^j s),
 \qquad h(\zeta_m s)-h(s)=-u(s),
\]
makes the translation constant. Thus the germ is the quotient
of $F\times\Delta_s$ by a fixed order-$m$ translation of $F$
and the primitive normal character $s\mapsto\zeta_m s$.
The associated normal line on $J$ has exact order $m$:
a trivial power would pull back to a nowhere-zero holomorphic
function on the compact elliptic cover, hence a constant,
and its character would have to be trivial. Its unit-frame
cover identifies this cyclic elliptic cover and its normal
character.

For the marked Hopf pair, the finite quotient acts on the axis
and a transverse coordinate by $(z,x)\mapsto
(\zeta^r z,\zeta^{-1}x)$ on the paired side.
The invariant monomials are $u=z^n$, $X=xz^k$, because
$rk-1=nl$. They have the deck factors in
\eqref{cdp:eq:C.SN.4}, and $p=x^r z=X^r u^{-l}$.
Conversely, every choice of an $n$th root $z$ of $u$ gives
$x=Xz^{-k}$; the $n$ choices are exactly the finite orbits.
This proves the coordinate isomorphism, including its inverse.
The marked curve is $\C^*/\gamma^{r\Z}$, and its paired
normal has factor $\gamma^l$. On the Hopf side the invariant
normal coordinate is $Y=wz^{-k}$, with factor $\gamma^{-l}$.
The relation $rk-nl=1$ gives $\gcd(l,r)=1$, so these dual
normal lines have exact order $r$.

In the normalized root write $u=y^r$, $X=s y^l$;
then $p=s^r$. The deck action from the root is
$(y,s)\mapsto(\xi y,\xi^{-l}s)$, $\xi^r=1$,
and the infinite period is $y\mapsto\gamma y$.
Writing its positive normal character as $s\mapsto\zeta s$
gives $y\mapsto\zeta^n y$, since $-nl\equiv1\pmod r$.
The unit-frame cover of the dual normal line is therefore
precisely the cyclic elliptic cover of the preceding paragraph.
The given axis and normal-line maps identify the two quotients,
so this is a chart of the given quasibundle germ.

The exponent matrix of \eqref{cdp:eq:C.SN.5} is
$\left(\begin{smallmatrix}-l&r\\k&-n\end{smallmatrix}\right)$,
with determinant $nl-rk=-1$. Direct substitution gives
$u=p^nW^r$, $X=p^kW^l$, so the maps are mutually inverse.
The infinite deck map sends $W$ to $\gamma W$ and fixes $p$.
They are consequently product isomorphisms over the punctured
disc. For a primary leaf, $n=1,k=0,l=-1$, these are exactly
the coordinates and product maps in
\eqref{cdp:eq:C.NS.1,cdp:eq:C.NS.2}.

The product pieces glue to the unchanged outside of $P$ by
these isomorphisms. A finite cover of the compact base by
smaller discs and their compact complement gives compact
inverse images, because every local product and every
unchanged quasibundle piece is proper. The resulting map
is therefore proper. It is smooth at the replaced fibres,
and all its remaining fibre models are those of $q$.
If they are smooth, its overlap maps preserve the integral
marking and hence have identity linear part; it is the
stated principal torsor.

Changing the integers to $k'=k+na$, $l'=l+ra$ changes
$X$ to $X'=Xu^a$ and leaves $p$ and $W$ unchanged in
\eqref{cdp:eq:C.SN.5}. More generally, two compatible root
trivializations differ by a holomorphic translation in the
elliptic product and a constant origin-preserving linear map.
The marked axis and normal cover identify that linear map.
The remaining translation is invariant under the root group,
so descends to a holomorphic translation on the ordinary
$p$-disc. The same map extends across its centre in the
replacement product. Ratios of two normal dualities are
nowhere-zero holomorphic functions on the compact axis,
thus nonzero constants, and give the same extending
translation comparison. These maps glue with the unchanged
outside transitions and have inverse translations. They
prove the asserted choice independence while retaining the
analytic torsor class.
\end{proof}

'''

boundary = r'''\subsection{Boundary maps and periods of elliptic stars}\label{subsec:II:star-boundary-periods}

\begin{lemma}[Boundary maps and canonical periods of elliptic stars]\hypertarget{tag-P351}{}\label{lem:II:elliptic-star-boundary}
\StatementRecord{lem:II:elliptic-star-boundary}{proved}{P351}{\cref{def:II:elliptic-star-data,lem:II:normal-product-collars,cdp:st:C.2.UN.17}}
Every leaf pair in \eqref{cdp:eq:C.AS.1,cdp:eq:C.AS.2} has
$K_H\simeq\OO_H(-(r+1)J)$, and $\OO_H(J)$ has infinite order.
The canonical formula \eqref{eq:II:quasibundle-canonical}
holds for every compact fixed-Jacobian elliptic quasibundle
with identity integral monodromy. The canonical-order
identities \eqref{cdp:eq:C.NS.8,cdp:eq:C.NS.9} and the
individual core expansions
\eqref{cdp:eq:C.NS.11,cdp:eq:C.AS.15,cdp:eq:C.AS.16}
hold for every full reduced SNC torus smoothing whose
leaves are these pairs, with arbitrary smooth central
component $P$; in each expansion $\gamma$ denotes the
core of the leaf in question.
Let $q:P\to B$ be a fixed-Jacobian elliptic quasibundle with
identity integral monodromy, and identify the axes of leaf
pairs \eqref{cdp:eq:C.AS.1} with distinct reduced fibres $J_i$.
Suppose their normal lines are dual. The marked full fibres
are $r_iJ_i$, so these data define the inverse transform of
\cref{def:II:elliptic-star-data}.

For a marked fibre use $r,n,k,l,\gamma$ and $(u,X,p,W)$ from
that definition. Let $a$ be its positive angular $u$-loop,
$b$ its deck-period loop, and $\mu_P$ its positive normal
$X$-loop. Let $\delta$ be the positive $p$-loop at fixed $W$,
and let $e,h$ be the angular and deck-period loops of
$F=\C^*/\gamma^{\Z}$. Their integral comparison is
'''+eq('SN.6', aliases=['NS.4'], map_text='The primary substitution n=1,k=0,l=-1 makes the displayed matrix [[1,0,r],[0,0,-1],[0,1,0]], so a=delta,b=h,mu_P=r delta-e, exactly NS4.')+r'''
In particular $\mu_P=r\delta-ne$ is primitive.
The Hopf complement fills the meridian
$\delta_H=na-k\mu_H$ and carries the fibre loops
$e_H=ra-l\mu_H$, $h_H=b$. The normal-product identification
$\mu_H=-\mu_P$ sends them to $\delta,e,h$ respectively.
For the primary choice $n=1,k=0,l=-1$, this is
'''+eq('NS.6')+r'''
When there are no unmarked multiple fibres, choose a
trivialization over the complement of small marked
base discs, write $\delta_i=\delta_{\rm ext}+\nu_i$,
where $\nu_i\in\Lambda_F$ is its translation winding.
The integral Chern vector and meridians are
'''+eq('SN.2', aliases=['NS.7'], map_text='Set every secondary order n_i=1; the same winding classes nu_i, exterior base loop and angular fibre generators give exactly NS7.')+r'''
Thus the rational Seifert vector before replacement is
$\sum_i(\nu_i-n_ie_i/r_i)$, and the replacements add
$\sum_i n_ie_i/r_i$ while preserving all holomorphic
transition maps.

For every such quasibundle, with full fibres $m_bJ_b$,
the canonical map and its direct image are
\begin{equation}\label{eq:II:quasibundle-canonical}
 K_P\simeq q^*K_B\otimes\OO_P\Bigl(\sum_b(m_b-1)J_b\Bigr),
 \qquad q_*K_P\simeq K_B.
\end{equation}
If $S=P\cup_iH_i$ is the full reduced fibre of a proper
two-torus degeneration from a smooth threefold, a nearby
fibre is smoothly identified with $T_0$. Under this
identification every oriented Hopf core two-torus is the
ordinary fibre class $\gamma$ of $q_0$. For a canonical
evaluation generator with orders $k_P,k_i$ one has
'''+eq('NS.8', aliases=['AS.12'], map_text='The second equality k_i-k_P=r_i is precisely AS12, with the same evaluation generator and the same components.')+eq('NS.9', aliases=['AS.13'], map_text='AS13 is the same line-bundle identity, expressed in divisor notation; P and each marked elliptic curve J_i are unchanged.')+r'''
After division by $t^{k_P}$, the leading relative two-form
on the $i$th Hopf core is $t^{r_i}\eta_i$, where
'''+eq('NS.11', aliases=['AS.14'], map_text='The relative form, marked Hopf coordinates and nonzero constant c_i are identical in NS11 and AS14.')+r'''
For a nonlinear leaf its period is
'''+eq('AS.15', aliases=['NS.12'], map_text='The n_i=1 specialization of AS15 is exactly NS12, with the same oriented integral core class gamma and the same coefficient c_i.')+r'''
For a diagonal leaf it satisfies
'''+eq('AS.16')+r'''
These are expansions of the same holomorphic period function.

When $B$ is elliptic and $q_0$ has no multiple fibres, its
fundamental group has the presentation
'''+eq('NS.13')+r'''
The fibre subgroup $\langle e,h\rangle\simeq\Lambda_F$
is injected. Consequently, in a two-torus smoothing its
Chern vector is zero.
\end{lemma}
\begin{proof}
The root-product calculation in the proof of
\cref{def:II:elliptic-star-data}, applied with the given
marked multiplicity $m$, gives normal order exactly $m$.
The dual Hopf normal has exact order $r$, including its
finite character $\gamma^{-l}$. Hence $m=r$ and the local
maps in that definition apply to this quasibundle.

Apply the angular and deck loops to the monomials
$p=X^ru^{-l}$ and $W=X^{-n}u^k$.
The resulting columns are $(-l,k,0)$, $(0,0,1)$,
and $(r,-n,0)$, giving \eqref{cdp:eq:C.SN.6}.
Its determinant is $rk-nl=1$.
The identities for $\delta,e,h$ follow by multiplying
these columns by the displayed integral coefficients.
They also give $\mu_P=r\delta-ne$ and its primitivity.

On the Hopf side put $Y=wz^{-k}$ and $u=z^n$.
Then $Y^r u^l=w^r/z$ and $Y^n u^k=w^n$.
Use $U=z/w^r$ as the positive complementary base coordinate;
it is the reciprocal of $Y^r u^l$.
The loops $na-k\mu_H$ and $ra-l\mu_H$ therefore change
$(\arg U,\arg(w^n))$ by $(2\pi,0)$ and $(0,2\pi)$,
respectively. The deck loop is the period $w^n\mapsto
\gamma w^n$. The normal product is $XY=xw=t$, so its
positive normal meridians are opposite. Substitution gives
$\delta_H=\delta$, $e_H=e$ and $h_H=h$, including
\eqref{cdp:eq:C.NS.6} in the primary case.

For a diagonal leaf its complement is
$\C_U\times(\C^*/\langle\beta,\mu_n\rangle)$, and
$[w]\mapsto[w^n]$ identifies the second factor with $F$.
For a nonlinear leaf the smooth coordinates
'''+eq('NS.5')+r'''
make $V$ invariant under the infinite deck map and under
the finite action. They give the same smooth product
$\C_V\times F$. Its compact core fills the complementary
disc and keeps the two fibre circles just calculated.
The normal framing agrees with the diagonal reference
through a smooth comparison of pairs: vary the resonant
coefficient in $(\beta^r z+c w^r,\beta w)$ from $c=1$ to
$c=0$. Its iterates have a uniform polynomial factor times
a contracting exponential, so one compact annulus meets
every orbit throughout this interval. The quotient is a
smooth proper family of pairs with the axis and its normal
characters fixed. A horizontal vector field tangent to the
axis, extended by a partition of unity, has a complete
flow over the compact parameter interval. Its flow gives
the pair diffeomorphism and fixes the displayed peripheral
maps. The product formula above identifies the fibre
circles in that comparison.

Apply \cref{lem:II:normal-product-collars} to the given
full reduced SNC star. Its double curves have two embedded
branches, its normal-product line maps are the given ones,
and there are no triple points. Its compatible core and
collar diffeomorphisms identify the nearby fibre with the
union of the $P$ core and these Hopf fillings. Each Hopf
filling kills $\delta$ and keeps $e,h$, exactly as the
product inserted by \eqref{cdp:eq:C.SN.5}. Gluing these
maps and their inverses gives the claimed diffeomorphism
to $T_0$. Along any path in $B$ joining two marked values
and avoiding the remaining multiple values, the ordinary
elliptic fibres are homologous. Thus all oriented Hopf
cores give the same integral class $\gamma$.

When $q_0$ is smooth, its translation trivialization on the punctured base gives
$\delta_i=\delta_{\rm ext}+\nu_i$. Substitution into
$\mu_{P,i}=r_i\delta_i-n_ie_i$ gives
\eqref{cdp:eq:C.SN.2}. The obstruction to extending that
trivialization over all base discs is the sum of their
winding vectors, which is the connecting Chern class of
\eqref{cdp:eq:C.KX.13}. This proves both the integral
and rational Seifert comparisons. The full punctured product
maps also preserve the analytic transitions in the preceding
diffeomorphism.

To prove \eqref{eq:II:quasibundle-canonical}, normalize
the invariant relative one-form by one fixed primitive
period on every smooth fibre. Translations between marked
products change that form only by a base one-form.
Its wedge with a local base form is therefore independent
of the product coordinates. On a normalized root chart
$t=s^m$ this wedge is
$m s^{m-1}ds\wedge\alpha_F$, where $\alpha_F$ is the
invariant elliptic form. Its divisor is $(m-1)J$.
These expressions glue to the first isomorphism.
For the direct image, a holomorphic two-form upstairs is
$a(s)ds\wedge\alpha_F$, since its coefficient is a
holomorphic function on each compact elliptic fibre.
Invariance under the root action says
$a(\zeta_m s)\zeta_m=a(s)$; hence
$a(s)=s^{m-1}b(s^m)$ with $b$ holomorphic.
It descends exactly to a local base form, proving the
second isomorphism including every multiple value.

For the smoothing, apply the evaluation construction of
\cref{cdp:st:C.2.UN.17} with all full-fibre multiplicities
equal to one. Its principal fibre identity and adjunction
give $(k_P-k_i)J_i=K_{H_i}+J_i$. The form
$dz\wedge dw/w^{r_i+1}$ is invariant under both deck
groups, for both contractions in \eqref{cdp:eq:C.AS.2}.
It gives $K_{H_i}=-(r_i+1)J_i$.
The line $\OO_{H_i}(J_i)$ has infinite order: a trivial
positive power would make its canonical section a
nonconstant holomorphic function on a compact surface.
Thus the coefficient equality is precisely
\eqref{cdp:eq:C.NS.8}. Adjunction on $P$ gives
\eqref{cdp:eq:C.NS.9}.

In a product chart $t=xw$, with $H_i:x=0$ and $P:w=0$,
the total canonical generator is
$x^{k_i}w^{k_P}g\,dz\wedge dw\wedge dx$, with $g$ a
holomorphic unit. Dividing its relative residue by
$t^{k_P}$ gives
$t^{r_i}g\,dz\wedge dw/w^{r_i+1}$.
On the compact leaf, the leading coefficient is a
nowhere-zero section of $K_{H_i}((r_i+1)J_i)$, whose
invariant trivialization just displayed makes it a
nonzero constant. This proves \eqref{cdp:eq:C.NS.11}.
In the logarithmic variables $(U,\log w)$ the nonlinear
core has primitive periods
'''+eq('SN.7')+r'''
and its form is $c_i\,dU\wedge d\log w$.
Their determinant is nonzero and gives
\eqref{cdp:eq:C.AS.15}, with the sign fixed by orientation.
For a diagonal leaf both periods have zero $U$-component,
so this leading integral is zero, giving
\eqref{cdp:eq:C.AS.16}. Differentiation under the integral
and Stokes' theorem make the integral over the transported
closed cycle holomorphic; the displayed local expressions
give its holomorphic extension and stated orders at zero.

Finally, for a principal elliptic bundle over an elliptic
base, the homotopy sequence injects $\pi_1(F)=\Lambda_F$
because $\pi_2(B)=0$. Its structure group acts by
translations, so this subgroup is central. Lift the two
generators of a fundamental polygon for $B$ through a
trivialization over its one-skeleton. The attaching map
of its two-cell is the Chern winding $(c_1,c_2)$ in the
fibre lattice, giving \eqref{cdp:eq:C.NS.13}.
An abelian total group forces $e^{c_1}h^{c_2}=1$;
the injected lattice then gives $c_1=c_2=0$.
The nearby two-torus has abelian fundamental group, so
the conclusion follows through the constructed diffeomorphism.
\end{proof}

'''

construction = r'''\subsection{Compact insertion of elliptic stars}\label{subsec:II:compact-elliptic-star-insertion}

\begin{lemma}[Compact insertion with prescribed Hopf leaves]\hypertarget{tag-P353}{}\label{lem:II:compact-elliptic-star-insertion}
\StatementRecord{lem:II:compact-elliptic-star-insertion}{proved}{P353}{\cref{def:II:elliptic-star-data,lem:II:zero-chern-elliptic-torsor,lem:II:logarithmic-period-family,cdp:st:C.2.UN.42}; \eqref{cdp:eq:C.NH.6,cdp:eq:C.NH.7,cdp:eq:C.NH.9,cdp:eq:C.NH.10}}
Let a marked elliptic star have elliptic base $B$, no unmarked
multiple fibres, and
'''+eq('AS.4')+r'''
Suppose there is a positive integer $R$ with
'''+eq('AS.5')+r'''
Then its specified reduced surface $S$ is the full fibre over
zero of a proper map $f:Y\to\PP^1$, where $Y$ is a smooth
compact complex threefold and every other fibre is a smooth
connected two-torus. The central main component is the given
$P$, with its entire analytic torsor and marked normal covers;
each leaf and each elliptic gluing map is the prescribed one.
Every reduced fibre support has Euler characteristic zero.
\end{lemma}
\begin{proof}
Apply \cref{lem:II:zero-chern-elliptic-torsor} to the
principal torsor $q_0:T_0\to B$ of
\cref{def:II:elliptic-star-data}, using $F_1=F$ and its
zero Chern class. Use the coordinate change
$(z,w)_{\mathrm{KX}}=(p,z)$, with
$\Gamma=\Gamma_B$ and $\Lambda_{F_1}=\Lambda_F$.
The resulting full lattice presentation is exactly
\eqref{cdp:eq:C.NS.14}. The local translations by the
zero-cochain in that lemma and their inverse translations
identify this quotient with the original analytic torsor
over the same $B$. Write it as $T_0=\C^2/\Lambda_0$, with
the fibre direction $p=0$ and the disjoint marked fibres $F_i$.

Apply the full rank-four clause of
\cref{lem:II:logarithmic-period-family} to this exact lattice
$\Lambda_0$, and pull its compact family back by $t=s^R$.
Its periods are $V_{s^R}(\Lambda_0)$ and its central fibre
is the same $T_0$. For the $i$th marked fibre, the product
map \eqref{cdp:eq:C.SN.5} identifies its elliptic curve with
$\C^*/\gamma_i^{\Z}$, where $\gamma_i=\beta_i^{n_i}$.
Choose the corresponding oriented fibre-period basis
$\lambda_i=(0,a_i)$, $\mu_i=(0,b_i)$, with
$\gamma_i=\exp(2\pi i b_i/a_i)$. The projection of
$\Lambda_0$ onto the base lattice is surjective with this
fibre lattice as kernel, so these two periods extend to
an integral basis of all four periods.
In the vector coordinates $(P,Z)$ after $V_{s^R}$, set
'''+eq('NS.16').replace('s^r','s^R')+r'''
The period $\lambda_i$ becomes $(0,2\pi i)$, and $\mu_i$ becomes
'''+eq('NS.17').replace(r'\log\beta_i',r'\log\gamma_i').replace('s^r','s^R')+r'''
where $d_i=\overline b_i-\overline a_i b_i/a_i\ne0$ by
the real independence of $a_i,b_i$.
The two remaining periods have coordinates
$(P_{ij}(s),Z_{ij}(s))$, $j=1,2$.
At zero their first coordinates are a base-period basis,
so remain real-linearly independent on a smaller disc.
They define the elliptic curve
$B_{i,s}=\C/\langle P_{i1}(s),P_{i2}(s)\rangle$ and the
degree-zero line $M_{i,s}$ with constant factors
$\exp Z_{ij}(s)$.
Quotienting first by these two periods and by $(0,2\pi i)$,
then by the last period, gives
'''+eq('AS.17', aliases=['SN.8','NS.18'], map_text='For all-nonlinear leaves set R=r, giving SN8. Set additionally n_i=1, gamma_i=beta_i and delta_i(s)=d_i s^r to obtain NS18, with the same quotient by the four period generators.')+r'''
This is an isomorphism of holomorphic families: the first
quotient uses $(p,z)\mapsto(p,e^z)$ and the two constant
line factors, and the last quotient uses exactly the
remaining period. The inverse is given by local logarithms
modulo those same four generators. All four periods and
their original flat torsor parameters are therefore preserved.
The line $M_{i,s}$ may be any degree-zero line. In particular
when $T_0=F\times B$ and its complementary periods have zero
fibre coordinate, $M_{i,0}$ is trivial.

At the marked point of the smooth elliptic surface family
$\mathcal B_i\to\Delta_s$, take the weighted blowup of
weights $(r_i,1)$ in $(p-p_i,s)$ and denote its exceptional
divisor by $E_i$. Pull back $M_i$ and tensor by
$\OO(n_iE_i)$. The weighted presentation
\eqref{cdp:eq:C.NH.6}, with $r=r_i$, is
$p-p_i=x^{r_i}z$, $s=xw$, with weights
$(r_i,1,-1)$ on $(z,w,x)$.
The extra line coordinate has weight $-n_i$.
Setting it equal to one leaves the finite action
'''+eq('SN.9').replace(r'\zeta^{r}',r'\zeta^{r_i}')+r'''
on $(\C^2_{z,w}\setminus\{0\})\times\C_x$.
It is free: a nonzero $w$ or $x$ makes $\zeta=1$,
and when both vanish, $z\ne0$ and $\gcd(r_i,n_i)=1$
has the same consequence. Equivalently, the order-$r_i$
weighted inertia in \eqref{cdp:eq:C.NH.7} acts faithfully
on this line because of that coprimality. Thus the coarse
nonzero line space is smooth.

Choose the given $n_i$th root $\beta_i$ of $\gamma_i$.
The lift of the last period in \eqref{cdp:eq:C.AS.17} is
'''+eq('AS.18', aliases=['SN.10','NS.19'], map_text='When R=r_i=r, x^(R-r_i)w^R=w^r, giving SN10. With n_i=1 this is NS19, including its base maps p-p_i=x^r z and s=xw, stated immediately before this formula.')+r'''
The monomial $x^{R-r_i}w^R$ has weighted degree $r_i$,
so this map commutes with the finite action. It fixes
$s=xw$ and changes $p$ by exactly $d_i s^R$.
On $x=0$, equality $R=r_i$ gives the nonlinear contraction
after $Z=z/(\beta_i^{r_i}d_i)$; strict inequality gives
the diagonal contraction. On $w=0$ it is always
$(z,x)\mapsto(\beta_i^{r_i}z,\beta_i^{-1}x)$.
Thus its main-component chart is
\eqref{cdp:eq:C.SN.4} and its leaf is the prescribed
primary or secondary surface.

We prove uniform properness of this quotient with its
varying line. On a closed smaller base disc, solve
\[
 \operatorname{Re}\bigl(Z_{ij}(s)-c_i(s)P_{ij}(s)\bigr)=0,
 \qquad j=1,2.
\]
The real period matrix is invertible, so the solution
$c_i(s)$ is smooth and bounded. The norm
$|\ell|\exp(-\operatorname{Re}(c_i(s)p))$ is invariant
under the two line-factor identifications. The last
period multiplies it by
\[
 \lambda_i(s)=|\gamma_i|
              \exp\bigl(-\operatorname{Re}(c_i(s)d_i s^R)\bigr).
\]
After shrinking, $0<\lambda_-\le\lambda_i(s)\le\lambda_+<1$
uniformly for all marked indices.

For the exceptional line, use the weighted norm
comparison \eqref{cdp:eq:C.NH.9} with $r=r_i$.
Uniform flat metrics on $B_{i,s}$ give
\[
 d(p+j d_i s^R,p_i)\le d(p,p_i)+C|j||s|^{r_i}
\]
for every integer $j$, since $R\ge r_i$.
The same inequality for the inverse translation gives
the reverse comparison. The $j$th lift on $\OO(n_iE_i)$
therefore changes its norm by a factor between
$C^{-1}(1+|j|)^{-n_i/r_i}$ and
$C(1+|j|)^{n_i/r_i}$, exactly the $n_i$th tensor power
of \eqref{cdp:eq:C.NH.10}. This comparison extends over
the exceptional divisor by continuity of the positive
line-norm ratio. Multiplication by $\lambda_i(s)^j$
makes the full norm tend uniformly to zero as
$j\to+\infty$ and to infinity as $j\to-\infty$.
Any two compact sets have line norms bounded above and
away from zero, proving proper discontinuity. A fixed
point of a nonzero power would be fixed by arbitrarily
large powers, contradicting these limits, so the action
is free, including after its finite quotient.

Choose one positive integer $N$ such that the $N$th
iterate decreases every line norm. Its norm ratio has
a positive minimum $c_N$ over the compact weighted base
above a closed base disc. Every orbit meets
$c_N\le\|\ell\|\le1$, a compact annulus there.
The quotient $\mathcal Y_i\to\Delta_s$ is therefore a
smooth proper local family.

Outside its exceptional Hopf component, the canonical
section of $\OO(n_iE_i)$ trivializes that factor and gives
'''+eq('NS.20')+r'''
where the right side is the compact torus family restricted
to the same disc, with its marked central fibre curve removed.
In the normalized line gauge the torus-family flat coordinate is
$W=x^{-n_i}$. On the main component its other coordinate
is $u=z^{n_i}$, and
$u=p^{n_i}W^{r_i}$, $X=p^kW^l$ are precisely the inverse
maps in \eqref{cdp:eq:C.SN.5}. On $s\ne0$ the map and
its inverse are the period quotient of
\eqref{cdp:eq:C.AS.17}.

For simultaneous replacement, choose a compact fundamental
domain on each Hopf component. Along a sequence approaching
it, $z,w$ remain bounded and not both zero, while $x\to0$.
The torus-family flat coordinate $x^{-n_i}$ is put into a fixed
compact norm annulus by $O(1+|\log|x||)$ deck iterates;
this follows from the uniform exponential bounds and
their polynomial factors. The total base displacement is
'''+eq('AS.19')+r'''
because $s=xw$ and $w$ is bounded. The initial base
coordinate $p-p_i=x^{r_i}z$ also tends to zero.
Consequently every cluster point of the images of this
sequence lies on $F_i$ in the original torus family.

Choose disjoint relatively compact neighbourhoods $W_i$
of the $F_i$ in a smaller closed tube. The subsets
$H_i\cup\Psi_i^{-1}(W_i\setminus F_i)$ of $\mathcal Y_i$,
where $\Psi_i$ is \eqref{cdp:eq:C.NS.20}, are open by the
cluster property. Glue them to the torus family with
the $F_i$ deleted by the same isomorphisms. A pair of
distinct limiting points in different pieces could only
arise from a cluster on one of the $F_i$; those loci have
been deleted from the torus piece and are disjoint for
different $i$. The gluing graphs are thus closed and
the glued space is Hausdorff.
Choose smaller closed neighbourhoods inside the $W_i$.
Their inverse images under $\Psi_i$, together with $H_i$,
are closed subsets of the proper $\mathcal Y_i$ over a
closed base disc and hence compact. Together with the
compact unmodified complement they cover the inverse
image of that disc. This proves properness of the glued
family. All maps are biholomorphic on the overlaps,
so its total space is smooth.

On the central main component the gluing reverses the
same inverse-transform maps used to define $T_0$.
It therefore recovers the original $P$ with every
analytic transition. The chosen fibre-period basis
retains the linear part of each marked normal cover.
The maps $(z,w)\mapsto(a^{r_i}z,aw)$ commute with both
contractions and with the finite action; as $a$ varies,
they realize every constant translation of the marked
axis. They therefore retain the given remaining gluing
constants. The full local equation is $s=xw$ in the
free coarse charts, so all central components have
multiplicity one and meet transversely as the given $S$.

Outside this tube the compact family
\eqref{eq:II:compact-twistor-lattice}, pulled back by
$t=s^R$, is unchanged. The proper local replacement and
that compact complement give a smooth compact threefold
over $\PP^1$. Every nonzero fibre is the original smooth
connected two-torus. The central quasibundle has Euler
number zero by \cref{lem:II:identity-monodromy-elliptic};
the Hopf leaves and double elliptic curves also have
Euler number zero. Additivity gives $e(S)=0$, completing
the construction.
\end{proof}

'''

leaf_classification = r'''\subsection{Canonical divisors on Hopf leaf pairs}\label{subsec:II:hopf-leaf-pairs}

\begin{lemma}[A canonical divisor supported on one Hopf curve]\hypertarget{tag-P352}{}\label{lem:II:hopf-single-canonical-curve}
\StatementRecord{lem:II:hopf-single-canonical-curve}{proved}{P352}{\cref{lem:II:hopf-curve-restriction,lem:II:central-primary-hopf-cover,lem:II:reduced-anticanonical-hopf,lem:II:elliptic-star-boundary}; \eqref{cdp:eq:C.SH.3,cdp:eq:C.SH.4}}
Let $H$ be a compact primary or secondary Hopf surface and
$J\subset H$ a connected smooth curve. An identity
$K_H\simeq\OO_H(-aJ)$ with $a\in\Z$ holds exactly for
the marked pairs in \eqref{cdp:eq:C.AS.1}, with the full
deck actions \eqref{cdp:eq:C.AS.2}; in these coordinates
$a=r+1$. The isomorphism marks $J$ as the image of $w=0$.
\end{lemma}
\begin{proof}
By \cref{lem:II:hopf-curve-restriction} and Serre duality,
$H^0(H,K_H)=0$. For $a\le0$ the canonical section of
$\OO_H(-aJ)$ would be nonzero, so $a>0$.
Apply \cref{lem:II:reduced-anticanonical-hopf} with the
effective divisor $aJ$. Its reduced alternative has two
distinct curve images and cannot equal this single-curve
support. Its other alternative gives $a\ge2$ and a finite
unramified central primary cover $\pi:H'\to H$ on which
$D=\pi^{-1}(J)$ is one marked curve. The unramified
differential and divisor pullback give
'''+eq('AS.7')+r'''
The primary-cover clause of that lemma gives either the
nonlinear contraction $(\beta^rz+w^r,\beta w)$ or the
diagonal contraction $(\gamma^rz,\gamma w)$, with
$D=\{w=0\}$ and $a=r+1$. Its weight comparison
\eqref{cdp:eq:C.AS.8,cdp:eq:C.AS.9} and its logarithmic
form \eqref{cdp:eq:C.AS.11} are on this same central-cover
construction; thus all inverse images of the marked curve
and all divisor coefficients are fixed in this application.

In the nonlinear case use the full centralizer map
\eqref{cdp:eq:C.SH.3} for this same central contraction.
Every member of the full deck group commutes with it.
The quotient and splitting maps \eqref{cdp:eq:C.SH.4}
therefore identify $H$ with
$H_r(\beta)/\mu_n$, with finite action
$(z,w)\mapsto(\zeta^rz,\zeta w)$ and $\gcd(r,n)=1$.
The rescaling of $z$ used there keeps $w=0$, and the
nonlinear primary curve is unique, so these maps carry
its image precisely to the given $J$.

For the diagonal central contraction, every deck lift
preserves its marked axis. Commutation with
$(\gamma^rz,\gamma w)$ and comparison of power-series
monomials give
'''+eq('AS.10')+r'''
with $A,B\ne0$. For $r=1$ commutation makes the lift
linear and preservation of $w=0$ makes its matrix upper
triangular, giving the same formula. Its action on
$z/w^r$ is affine. The central contraction acts trivially
on that coordinate, so the induced affine group is finite.
The average of its finite orbit of zero is a common fixed
point $c$. The maps $z'=z-cw^r$, $w'=w$ and
$z=z'+c(w')^r$, $w=w'$ conjugate the whole group to
diagonal maps while preserving the marked curve and
commuting with the central contraction.

The invariant form $dz\wedge dw/w^{r+1}$ trivializes
$K_{H'}((r+1)D)$. The section pulled back from
$K_H(aJ)$ differs from it by a constant, since $H'$ is
compact and connected. Invariance under every diagonal
deck element gives $AB=B^{r+1}$, hence $A=B^r$.
The full group is consequently the weighted scalar group
given by its second-coordinate multipliers. It has a
cyclic subgroup of finite index, so it is generated by
one contracting multiplier $\beta$, together with its
finite subgroup $\mu_n$. Freeness on $w=0$ gives
$\gcd(r,n)=1$: a root with $\zeta^r=1$ would fix a
nonzero point of that axis. Thus its quotient is exactly
the diagonal pair of \eqref{cdp:eq:C.AS.1,cdp:eq:C.AS.2},
with the same marked curve.

Conversely, for each displayed pair the invariant form
and infinite order of $\OO_H(J)$ in the proof of
\cref{lem:II:elliptic-star-boundary} give
$K_H=-(r+1)J$ and uniqueness of the integer $a$.
This proves both directions with the stated pair maps.
\end{proof}

'''

criterion = r'''\subsection{The reduced Hopf-star criterion}\label{subsec:II:reduced-hopf-star-criterion}

\begin{proposition}[Reduced Hopf stars with torus smoothings]
\hypertarget{tag-01DY}{}\label{cdp:st:C.2.UN.53}
\StatementRecord{cdp:st:C.2.UN.53}{proved}{01DY}{\cref{def:II:elliptic-star-data,lem:II:elliptic-star-boundary,lem:II:hopf-single-canonical-curve,lem:II:compact-elliptic-star-insertion,cdp:st:C.2.UN.17,cdp:st:C.2.UN.28,cdp:st:C.2.UN.31,lem:II:cyclic-component-cover,lem:II:zero-chern-elliptic-torsor}}
\hypertarget{tag-01DT}{}\label{cdp:st:C.2.UN.49}
\StatementRecord{cdp:st:C.2.UN.49}{proved}{01DT}{}
\hypertarget{tag-01DV}{}\label{cdp:st:C.2.UN.50}
\StatementRecord{cdp:st:C.2.UN.50}{proved}{01DV}{}
Let $S$ be a specified compact connected SNC surface with
smooth components $P,H_1,\ldots,H_n$, $n\ge1$, where each
$H_i$ is a primary or secondary Hopf surface. Its intersection
with $P$ is one connected smooth curve $J_i$, the $J_i$ are
disjoint on $P$, and there are no other intersections.
The following assertions are equivalent:
\begin{enumerate}
\item $S$ is the full reduced central fibre of a proper
degeneration of connected two-tori with smooth total threefold.
\item $S$ is the full fibre over zero of a proper map from
a smooth compact complex threefold to $\PP^1$, every other
fibre being a smooth connected two-torus.
\item The leaf pairs are the marked pairs
\eqref{cdp:eq:C.AS.1,cdp:eq:C.AS.2}, their normal lines
are dual across every $J_i$, and $P$ admits the
quasibundle \eqref{cdp:eq:C.AS.3} over an elliptic curve,
with fixed Jacobian and identity integral monodromy.
Its marked full fibres are $r_iJ_i$ and it has no
unmarked multiple fibres. The inverse transform of
\cref{def:II:elliptic-star-data} has the zero Chern vector
\eqref{cdp:eq:C.AS.4}, and its leaf exponents satisfy
\eqref{cdp:eq:C.AS.5} for a positive integer $R$.
\end{enumerate}
All components, finite secondary actions, analytic torsor
parameters, primitive angular directions and specified
elliptic identifications are preserved in the compact
realization. Every reduced support there has Euler number zero.

When a fixed-Jacobian identity-monodromy quasibundle $q:P\to B$
with the $J_i$ as distinct reduced fibre supports is part
of the given data, the same tests use that given $q$.
For exclusively nonlinear leaves they say that $B$ is
elliptic, every marked full fibre is $r_iJ_i$, there are
no other multiple fibres, the normals are dual, all $r_i$
equal one integer $r$, and the inverse-transform Chern vector
is zero. Arbitrary secondary orders $n_i$ satisfying
$\gcd(r_i,n_i)=1$ remain allowed. The primary specialization
is $n_i=1$, with the local identifications
$k=0,l=-1,u=z,X=x,W=x^{-1}$ in
\eqref{cdp:eq:C.SN.4,cdp:eq:C.SN.5}.
If every leaf is diagonal, one can take
$R=1+\max_i r_i$. A nonlinear leaf determines $R=r_i$,
and every diagonal leaf then has strictly smaller exponent.
\end{proposition}
\begin{proof}
Assume the local occurrence. Apply the evaluation construction
of \cref{cdp:st:C.2.UN.17} to this proper disc map, with
all full-fibre multiplicities one. Write its canonical
divisor as $k_PP+\sum_i k_iH_i$.
The principal central fibre and adjunction on a leaf give
'''+eq('AS.6')+r'''
Apply \cref{lem:II:hopf-single-canonical-curve} to this
same $H_i$, its connected curve $J_i$, and
$a=k_i-k_P+1$. It gives the full marked pair
\eqref{cdp:eq:C.AS.1,cdp:eq:C.AS.2}, with
$k_i-k_P=r_i\ge1$.
Adjunction on $P$ gives exactly
\eqref{cdp:eq:C.NS.9}. Its effective canonical divisor
makes $\kappa(P)\ge0$ and $p_g(P)\ge1$.
The compact-component bound \cref{cdp:st:C.2.UN.28},
applied to this same fibre and its smooth component $P$,
gives $p_g(P)=1$.
The surface $P$ is minimal: an exceptional rational curve
$E$ is distinct from all the elliptic $J_i$ and intersects
them nonnegatively, whereas adjunction gives $K_P\cdot E=-1$.
This contradicts \eqref{cdp:eq:C.NS.9}.

To identify its fibration, apply the component-cover construction
\cref{lem:II:cyclic-component-cover}. The multiplicity of $P$
in this full fibre is one. In a generic chart of a normalized
root base change $t=s^N$, its equation is $x=s^N$ after
absorbing a unit. There is one strict covering component,
whose map to $P$ has degree one. Its subsequent resolution
remains birational to $P$. The smooth minimal model is
therefore this same $P$, by uniqueness of the minimal model
in nonnegative Kodaira dimension. Thus the cover conclusion
of \cref{cdp:st:C.2.UN.31} applies through this degree-one
map: $P$ is a two-torus or it has a fixed-Jacobian,
identity-monodromy elliptic quasibundle over a curve of
genus at most one. In the latter case
$p_g(P)=g(B)$ by \cref{lem:II:identity-monodromy-elliptic},
so $B$ is elliptic.

We choose this fibration so that all marked curves are fibres.
On a two-torus an embedded elliptic curve is a translate of
an elliptic subgroup: a lift to universal covers has periodic
holomorphic derivative, which is constant. Two such subgroups
with distinct tangent lines have a surjective product map
to the torus with finite kernel. Every two translates would
then meet. The disjoint $J_i$ have one common tangent line
and are therefore fibres of the quotient by that elliptic
subgroup; its connected quotient is an elliptic curve.

For the quasibundle over an elliptic base, use the canonical
map \eqref{eq:II:quasibundle-canonical}.
If there is a multiple fibre, its effective contribution
makes the intersection with every horizontal $J_i$ positive.
But normal duality gives $J_i^2=0$, because the leaf normal
has finite order, and adjunction gives $K_P\cdot J_i=0$.
Thus every $J_i$ is vertical.
If the quasibundle is smooth, it is a principal elliptic
torsor. For a nonzero Chern vector, a horizontal elliptic
curve would map to the elliptic base by a finite unramified
map of nonzero degree. Pullback to that curve has the
diagonal section $j\mapsto(j,j)$ and hence zero Chern class;
on $H^2(B,\Lambda_F)$ the same pullback multiplies the
Chern vector by the degree, a contradiction.
For zero Chern vector, \cref{lem:II:zero-chern-elliptic-torsor}
identifies this same total space with a two-torus through
its full analytic cocycle. The preceding subgroup argument
then supplies its quotient with all $J_i$ as fibres.

If a quasibundle with these marked fibre supports was already
given, keep that map throughout. Its relative minimality
follows from its smooth elliptic fibre supports, and
\cref{lem:II:identity-monodromy-elliptic} gives
$g(B)=p_g(P)=1$ directly. Thus this case has the same
elliptic-base conclusion for the given $q$.

For either resulting map, the normal-order comparison in
\cref{lem:II:elliptic-star-boundary} gives full marked
fibres $r_iJ_i$. Subtracting \eqref{cdp:eq:C.NS.9}
from its canonical formula leaves
'''+eq('NS.10')+r'''
Since $B$ is elliptic, this is an effective sum of unmarked
multiple fibres linearly equivalent to zero. A nonzero
such divisor would be the divisor of a holomorphic function
on the compact connected $P$, which must be constant.
There are therefore no unmarked multiple fibres.

The inverse transform is now a principal elliptic torsor
over $B$. The core and collar map of
\cref{lem:II:elliptic-star-boundary} identifies its underlying
four-manifold with a nearby torus, using the unimodular
matrices \eqref{cdp:eq:C.SN.6} and the full analytic maps
\eqref{cdp:eq:C.SN.5}. Its injected fibre lattice in
\eqref{cdp:eq:C.NS.13} forces \eqref{cdp:eq:C.AS.4}.
All oriented Hopf core classes are the same integral
class $\gamma$. The holomorphic period of the divided
canonical generator therefore has the expansions
\eqref{cdp:eq:C.AS.15,cdp:eq:C.AS.16} at every leaf.
A nonlinear leaf gives a nonzero leading coefficient and
finite vanishing order $R=r_i$. Every other nonlinear
leaf has that order, and every diagonal leaf has
$r_i<R$. When all leaves are diagonal, the integer
$1+\max_i r_i$ satisfies \eqref{cdp:eq:C.AS.5}.
This proves every test in the third assertion.

Conversely, use the given leaf presentations, quasibundle,
axis identifications and normal dualities as the marked
star data of \cref{def:II:elliptic-star-data}.
The third assertion supplies exactly the elliptic-base,
zero-Chern and exponent hypotheses of
\cref{lem:II:compact-elliptic-star-insertion}.
Its explicit inverse-transform maps recover the same $P$,
its weighted charts recover each specified leaf, and its
axis translations retain the given gluing maps. It gives
the second assertion with all other fibres smooth tori
and all support Euler numbers zero. Restricting that
proper map to a disc about zero gives the first assertion.

For exclusively nonlinear data, \eqref{cdp:eq:C.AS.5}
is the common-resonance identity $r_i=r=R$.
The matrix \eqref{cdp:eq:C.SN.6} and meridian
\eqref{cdp:eq:C.SN.2} retain each full secondary integer
$n_i$. For $n_i=1$, the substitutions in the statement
identify those maps with
\eqref{cdp:eq:C.NS.1,cdp:eq:C.NS.2,cdp:eq:C.NS.4,cdp:eq:C.NS.7};
the period \eqref{cdp:eq:C.AS.15} becomes
\eqref{cdp:eq:C.NS.12}, and the compact deck map
\eqref{cdp:eq:C.AS.18} becomes \eqref{cdp:eq:C.NS.19}.
These are the complete primary and secondary nonlinear
specializations for the given quasibundle and surface.
\end{proof}

'''
needle = r'Its inverse is $v\mapsto(v-zJ\overline v)/(1+|z|^2)$.'
extension = needle+r'''
For a full lattice $\Lambda_0$, these invertible real maps
carry any chosen real lattice basis to four real-independent
periods at every finite $t$. In the other frame the sections
are $J\overline\lambda+s\lambda$, whose squared norm is
$(1+|s|^2)\|\lambda\|^2$, by the same orthogonality identity.
They therefore remain a full lattice at $s=0$ as well.
On a closed subdisc in either chart the real period matrices
and their inverses are uniformly bounded. Integral translations
act freely and properly discontinuously there; their closed
real fundamental parallelepipeds cover the quotient over the
closed subdisc and are compact. The frame change
$\eta_\infty=\eta/t$ sends $V_t(\lambda)$ exactly to
$V_s^\infty(\lambda)$, so these local quotients glue as
\eqref{eq:II:compact-twistor-lattice}. The covering quotient is
a holomorphic submersion and is proper by these compact
parallelepipeds. A finite closed cover of $\PP^1$ makes its
total space compact. Base change of a proper holomorphic
submersion preserves both properties; the base-changed total
space is compact because its base is again $\PP^1$.
'''
assert p331new.count(needle) == 1
p331new = p331new.replace(needle, extension, 1)

definition = definition.replace('$u(s)=t(s)-t(0)$',r'$\upsilon(s)=t(s)-t(0)$').replace(r'u(\zeta_m^j s)',r'\upsilon(\zeta_m^j s)').replace('=-u(s)',r'=-\upsilon(s)')
definition = definition.replace('On the Hopf side the invariant\nnormal coordinate is', 'On the normal bundle of the Hopf axis, the invariant\nfibre coordinate is')
boundary = boundary.replace('whose\nleaves are these pairs, with arbitrary smooth central\ncomponent $P$;', 'whose\ncentral fibre is the star $P\\cup_iH_i$ with these leaf pairs,\none disjoint marked curve per leaf and no other intersections,\nand with arbitrary smooth component $P$;')
boundary = boundary.replace('On the Hopf side put $Y=wz^{-k}$ and $u=z^n$.', 'On the diagonal reference Hopf pair put $Y=wz^{-k}$ and $u=z^n$.')
boundary = boundary.replace(r'\end{equation}\begin{equation}', '\\end{equation}\nOn the main component,\n\\begin{equation}')
boundary = boundary.replace(r'$\gamma$',r'$\gamma_{\rm core}$').replace(r'\int_{\gamma}',r'\int_{\gamma_{\rm core}}').replace(r'\int_\gamma',r'\int_{\gamma_{\rm core}}')
boundary = boundary.replace(r'\langle a,b,e,h:',r'\langle a_B,b_B,e,h:').replace('[a,b]','[a_B,b_B]')
boundary = boundary.replace('generators of a fundamental polygon for $B$ through a', 'generators $a_B,b_B$ of a fundamental polygon for $B$ through a')
construction = construction.replace(r'\lambda_i(s)',r'\varrho_i(s)').replace(r'\lambda_-',r'\varrho_-').replace(r'\lambda_+',r'\varrho_+')
construction = construction.replace(r'In the coordinate change'+'\n'+r'$(z,w)_{\mathrm{KX}}=(p,z)$, with',r'Denote its coordinates in \eqref{cdp:eq:C.KX.14} by $(z_0,w_0)$.'+'\n'+r'Use the coordinate change $(z_0,w_0)=(p,z)$, with')
construction = construction.replace('p_i=P-',r'p^{(i)}=P-')
construction = construction.replace('At the marked point of the smooth elliptic surface family',r'Write $p=p^{(i)}$ in this presentation, and choose a constant'+ '\n'+r'lift $p_i^0$ of its marked central base point. At that point'+ '\n'+r'of the smooth elliptic surface family')
construction = construction.replace('$(p-p_i,s)$',r'$(p-p_i^0,s)$').replace('$p-p_i=x^{r_i}z$',r'$p_{\rm loc}=p-p_i^0=x^{r_i}z$')
construction = construction.replace(r'd(p+j d_i s^R,p_i)\le d(p,p_i)',r'd(p+j d_i s^R,p_i^0)\le d(p,p_i^0)')
construction = construction.replace('The extra line coordinate has weight $-n_i$.\nSetting it equal to one leaves the finite action',r'''The extra line coordinate $\ell$ has weight $-n_i$.
Choose $\lambda$ with $\lambda^{n_i}=\ell$ and apply the
weighted action to set $\ell=1$. Two choices differ exactly
by the action below; its inverse sends a finite orbit to
the weighted orbit represented with $\ell=1$.
The residual finite action is''')
construction = construction.replace('$u=p^{n_i}W^{r_i}$, $X=p^kW^l$',r'$u=p_{\rm loc}^{n_i}W^{r_i}$, $X=p_{\rm loc}^kW^l$')
construction = construction.replace('maps in \\eqref{cdp:eq:C.SN.5}. On $s\\ne0$',r'maps in \eqref{cdp:eq:C.SN.5}, with its base coordinate'+ '\n'+r'identified with $p_{\rm loc}$. On $s\ne0$')
construction = construction.replace('coordinate $p-p_i=x^{r_i}z$',r'coordinate $p-p_i^0=x^{r_i}z$')
construction = construction.replace('the Hopf leaves and double elliptic curves also have\nEuler number zero.',r'\cref{lem:II:hopf-curve-restriction} gives Euler number zero'+ '\n'+r'for the Hopf leaves, and each double curve is elliptic.')
leaf_classification = leaf_classification.replace(r'By \cref{lem:II:hopf-curve-restriction} and Serre duality,',r'The curve $J$ is elliptic by \cref{lem:II:hopf-curves}.'+'\n'+r'By \cref{lem:II:hopf-curve-restriction} and Serre duality,')
leaf_classification = leaf_classification.replace(r'nonlinear contraction $(\beta^rz+w^r,\beta w)$',r'nonlinear contraction $(\beta_0^rz+w^r,\beta_0w)$')
leaf_classification = leaf_classification.replace(r'The rescaling of $z$ used there keeps $w=0$, and the',r'Here $\beta$ is the second-coordinate multiplier of the'+ '\n'+r'primitive contracting generator in \eqref{cdp:eq:C.SH.4};'+ '\n'+r'the central generator with multiplier $\beta_0$ is a positive'+ '\n'+r'power of it times a finite deck element. The rescaling of'+ '\n'+r'$z$ used there keeps $w=0$, and the')
leaf_classification = leaf_classification.replace(r'''For the diagonal central contraction, every deck lift
preserves its marked axis. Commutation with
$(\gamma^rz,\gamma w)$ and comparison of power-series
monomials give''',r'''For the diagonal central contraction, every deck lift
preserves its marked axis. For $r\ge2$, this contraction is
class $\mathrm{III}$ of \cite[arXiv v2, Theorem~2.1(3), p.~5]{Khaled2024Hopf}.
Its source parameters $(a,b,d)=(A,C,B)$ give''')
leaf_classification = leaf_classification.replace('with $A,B\\ne0$. For $r=1$ commutation makes the lift\nlinear and preservation of $w=0$ makes its matrix upper\ntriangular, giving the same formula.',r'''with $A,B\ne0$. For $r=1$, class $\mathrm{IV}$ in the same
theorem gives $\operatorname{GL}(2,\C)$; preservation of
$w=0$ sets its lower-left matrix entry to zero and gives
the same formula.''')
leaf_classification = leaf_classification.replace(r'\cref{lem:II:hopf-curve-restriction,lem:II:central-primary-hopf-cover',r'\cref{lem:II:hopf-curves,lem:II:hopf-curve-restriction,lem:II:central-primary-hopf-cover',1)
criterion = criterion.replace(r'$\gamma$',r'$\gamma_{\rm core}$')
criterion = criterion.replace('Assume the local occurrence. Apply the evaluation construction',r'''Assume the local occurrence. Along each double curve the
defining function has local product equation $xy=t$.
Its bilinear normal term identifies
$N_{J_i/P}\otimes N_{J_i/H_i}$ with $\OO_{J_i}$,
so the given curve identifications have dual normal lines.
Apply the evaluation construction''')
p325new = p325new.replace('Unramified descent gives the second alternative on $H$.', 'Unramified descent gives the second alternative on $H$.\nHere $H\'=P$, $r=a$, and the same multiplier $\\beta$ give\nthe asserted central primary cover and its marked contraction.')
p325new = p325new.replace('Pullback to this cover retains every coefficient', 'Pullback to this cover preserves every coefficient').replace('It remains to retain the full marking in the reduced case.', 'For the reduced case, the following coordinate maps preserve its full marking.')
definition = definition.replace('while retaining the', 'while preserving the')
construction = construction.replace('its specified reduced surface', 'its given reduced surface').replace('retains the linear part', 'preserves the linear part').replace('They therefore retain the given', 'They therefore preserve the given')
criterion = criterion.replace('a specified compact connected SNC surface', 'a compact connected SNC surface').replace('and specified\n', 'and given\n').replace('each specified leaf', 'each given leaf').replace('axis translations retain the given', 'axis translations preserve the given').replace('retain each full secondary integer', 'preserve each full secondary integer')

def aggregate_aliases(text):
    text = re.sub(r'\\eqref\{([^{}]*,[^{}]*)\}',r'\\cref{\1}',text)
    pattern = re.compile(r'\\SsixEquationAliases\{((?:\s*\\label\{[^}]+\})+)\s*\}')
    def one_equation(m):
        text = m.group()
        matches = list(pattern.finditer(text))
        if len(matches) <= 1:
            return re.sub(r'\n[ \t]*\n+', '\n', text)
        labels = ''.join(''.join(re.findall(r'\\label\{[^}]+\}', x.group(1))) for x in matches)
        count = 0
        def repl(x):
            nonlocal count
            count += 1
            return r'\SsixEquationAliases{'+labels+'}' if count == len(matches) else ''
        return re.sub(r'\n[ \t]*\n+', '\n', pattern.sub(repl, text))
    return re.sub(r'\\begin\{equation\}.*?\\end\{equation\}', one_equation, text, flags=re.S)

fragments = {'P350':definition, 'P351':boundary, 'P352':leaf_classification,
             'P353':construction, 'criterion':criterion,
             'P325_replacement':p325new, 'P330_replacement':p330new,
             'P331_replacement':p331new}
fragments = {key:aggregate_aliases(text) for key,text in fragments.items()}
heading = r'\subsection{Stars and weighted component constructions}\label{subsec:II:star-weighted-constructions}'
a = current.index(heading)
b = current.index(original[50],a)+len(original[50])
main_old = current[a:b]
freeze('input',main_old)
main_new = '\n'.join(fragments[key] for key in ['P350','P351','P352','P353','criterion'])
main_new = main_new.replace(r'\label{subsec:II:elliptic-star-data}',r'\label{subsec:II:elliptic-star-data}\label{subsec:II:star-weighted-constructions}',1)
main_new += r'''\subsection{Weighted Hopf cycles}\label{subsec:II:weighted-hopf-cycles}

'''
following_heading = r'''\subsection{Hopf support graphs and rational-root trees}\label{subsec:II:hopf-support-tree-remainder}

'''
insert_anchor = owners[337][owners[337].index(r"For the cover $\pi:H'\to H$"):]
remote_rows = [
    dict(statement_id='cdp:st:C.2.UN.53',old_text=original[53],new_text=following_heading,reason='Transfer the complete broad star criterion into the preceding common theorem, preserving its identity and all original formulas; give the untouched following support/tree material its own open subsection.'),
    dict(statement_id='lem:II:reduced-anticanonical-hopf',old_text=owners[325],new_text='',reason='Move this complete shared owner before every star consumer; its previous terminal-ruled subsection still contains its nonempty UN64 material.'),
    dict(statement_id='lem:II:reduced-anticanonical-hopf',old_text=insert_anchor,new_text=insert_anchor+'\n\n'+fragments['P325_replacement'],reason='Insert P325 after the unchanged P337 final trace square. Its strengthened nonreduced primary-cover clause is proved by the same complete weight calculation, with AS8/AS9/AS11 transferred into it.'),
    dict(statement_id='lem:II:zero-chern-elliptic-torsor',old_text=owners[330],new_text=fragments['P330_replacement'],reason='Transfer the duplicate NS14 period target to the proved KX14 torsor map, with NS14 and PT8 in one alias call; statement and proof unchanged.'),
    dict(statement_id='lem:II:logarithmic-period-family',old_text=owners[331],new_text=fragments['P331_replacement'],reason='Add the full rank-four compact twistor clause and its complete proof using the same V_t and infinity frame; preserve every existing logarithmic-family statement and proof step. Transfer NS15 through the explicit vector/base-coordinate identity.')
]

if __name__ == '__main__':
    for key,text in fragments.items():
        (out/(stem+'_'+key+'.tex')).write_text(text,newline='\n')
    (out/(stem+'_replacement.tex')).write_text(main_new,newline='\n')
    with (out/(stem+'_remote_repairs.tsv')).open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=['statement_id','old_text','new_text','reason'],delimiter='\t',lineterminator='\n')
        writer.writeheader();writer.writerows(remote_rows)
    assert current.count(main_old)==1
    for row in remote_rows:
        assert current.count(row['old_text'])==1,row['statement_id']
    all_old='\n'.join(original.values())+'\n'+'\n'.join(owners[n] for n in [325,330,331])
    all_new=main_new+'\n'+'\n'.join(fragments[f'P{n}_replacement'] for n in [325,330,331])
    assert set(used)==set(equations)
    assert all(n==1 for n in Counter(used).values())
    for pattern in [r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}']:
        old_counts=Counter(re.findall(pattern,all_old));new_counts=Counter(re.findall(pattern,all_new))
        assert all(new_counts[k]==v for k,v in old_counts.items()),[(k,v,new_counts[k]) for k,v in old_counts.items() if new_counts[k]!=v]
    assert not re.search(r'\\tag\{|night:P4R\.13|night:P4\.40|\.py|\.json|code/',all_new)
    for equation in re.findall(r'\\begin\{equation\}.*?\\end\{equation\}',all_new,re.S):
        assert equation.count(r'\SsixEquationAliases')<=1
        assert not re.search(r'\n[ \t]*\n',equation)
    for text in fragments.values():
        begins=Counter(re.findall(r'\\begin\{([^}]+)\}',text));ends=Counter(re.findall(r'\\end\{([^}]+)\}',text))
        assert begins==ends,(begins-ends,ends-begins)
        assert '\r' not in text
    import runpy
    runpy.run_path(str(root/'code/S6_SERIES_PUBLISH_c3_conductor_16_records.py'),run_name='__main__')
