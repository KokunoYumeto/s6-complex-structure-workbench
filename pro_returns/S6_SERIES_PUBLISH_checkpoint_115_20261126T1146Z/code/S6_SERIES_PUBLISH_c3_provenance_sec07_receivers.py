from pathlib import Path
import re, csv

ROOT=Path('/workspace/scratch/9fcd229a9ed4/base/S6_SERIES_PUBLISH_checkpoint_35')
OUT=ROOT/'agents/continuation3_provenance/sec07_tail'
MAIN=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()

def old(key):
    return (OUT/f'S6_SERIES_PUBLISH_{key}_original.tex').read_text()

def replace(s,a,b):
    assert s.count(a)==1, (s.count(a),a[:100])
    return s.replace(a,b,1)

def span(s,a,b,new):
    i=s.index(a); j=s.index(b,i)
    return s[:i]+new+s[j:]

def finish(s):
    def display(m):
        text=m.group(1)
        if r'\tag{' not in text: return m.group(0)
        text=re.sub(r'\s*\\tag\{[^}]+\}', '', text)
        text=re.sub(r'\n[ \t]*\n+', '\n',text).strip()
        return '\\begin{equation}\n'+text+'\n\\end{equation}'
    s=re.sub(r'\\\[(.*?)\\\]',display,s,flags=re.S)
    s=re.sub(r'\\tag\{[^}]+\}', '',s)
    s=re.sub(r'(?:(?:Proposition|Lemma|Theorem|Corollary)~)?\\SeriesRef\{(cdp:st:[^}]+|night:[^}]+|lem:II:[^}]+|prop:II:[^}]+)\}',r'\\cref{\1}',s)
    s=re.sub(r'\\SeriesRef\{(cdp:eq:[^}]+)\}',r'\\eqref{\1}',s)
    s=re.sub(r'(?<![A-Za-z])\\ref\{(cdp:st:[^}]+|night:[^}]+)\}',r'\\cref{\1}',s)
    s=re.sub(r'(?:Proposition|Lemma|Theorem|Corollary)~(?=\\cref\{)', '', s)
    s=re.sub(r'\((C\.[A-Z]+\.\d+)\)',lambda m:r'\eqref{cdp:eq:'+m.group(1)+'}',s)
    def earlier_equation(m):
        label='cdp:eq:'+m.group(1)
        assert r'\label{'+label+'}' in MAIN, label
        return r'\eqref{'+label+'}'
    s=re.sub(r'\((A\.(?:RT|T)\.\d+)\)',earlier_equation,s)
    s=re.sub(r'\n(?:[ \t]*\n){2,}', '\n\n',s)
    return s.strip()+'\n\n'

def save(key,s):
    s=finish(s)
    (OUT/f'S6_SERIES_PUBLISH_{key}_proposed.tex').write_text(s)
    return s

s=old('INT_1')
s=s.replace('The actual restriction homomorphism','The restriction homomorphism').replace('The actual pullback','The pullback')
s=s.replace(r'\cite[Lemma~2.2 and \S2]{BrinzanescuMoraru2005}',r'\cite[Lemma~2.2, pp.~1664--1665; \S2, pp.~1666--1667]{BrinzanescuMoraru2005}')
s=s.replace(r'\cite[Remark~2.7]{DlousskyTeleman2012}',r'\cite[arXiv v2, Remark~2.7, p.~9]{DlousskyTeleman2012}')
s=replace(s,r'\item We spell out the blowdown comparison. Put',r'\item Put')
s=span(s,r'\item For a Hopf $Z_0$',r'\item For a non-K\"ahler elliptic',r'''\item For a Hopf $Z_0$, apply \cref{lem:II:hopf-curve-restriction}
to this surface and its same elliptic curve $E_0$.
It gives an isomorphism on $H^1(\OO)$ induced by the inclusion.
The coefficient maps commute with this inclusion, and
\cref{cdp:st:D.1.7} makes the real coefficient map on $Z_0$
injective. Consequently the same square gives a nonzero map
\[
 H^1(Z_0,\R)\longrightarrow H^1(E_0,\R).
 \tag{C.INT.3}\hypertarget{tag-00OA}{}\label{cdp:eq:C.INT.3}
\]
The differential of $\Pic^0(Z_0)\to\Pic^0(E_0)$ is that
$H^1(\OO)$ isomorphism, so its kernel has zero identity
component. Under the assumed zero restriction, the connected
image of $\rho$ lies in this kernel and is zero. This
contradicts the positive-degree line in
\eqref{cdp:eq:C.INT.1}--\eqref{cdp:eq:C.INT.2}.

''')
s=replace(s,'''on its minimal model is a reduced elliptic fibre.
The actual covering construction of''',r'''on its minimal model is a reduced elliptic fibre. Indeed
\cite[Lemma~2.2, pp.~1664--1665]{BrinzanescuMoraru2005}
gives degree zero for the restriction of every divisor line to
a smooth fibre; a horizontal effective curve would have
positive intersection with that fibre. The quasibundle
description in \cite[\S2, p.~1663]{BrinzanescuMoraru2005}
makes each reduced fibre smooth elliptic.
The covering construction of''')
s=span(s,'To include multiple fibres, take a base cover','\n\n\\item On this principal bundle',r'''At a multiple fibre $mE_0$, the normalized base change
$t=s^m$ in \cref{def:II:elliptic-root-curve}, applied to
this same elliptic surface tube, is given by
$w^m=u$, $s=wh$ when $t=u h^m$.
Its inverse over $h\ne0$ is $w=s/h$, and its central
free translation quotient is an isogeny onto $E_0$.
A branching order divisible by $m$ is the base change of
this chart, so gives the same reduced-curve map after
normalization. At the additional ordinary branch values
in the source's construction the reduced-curve map is
an isomorphism. These are precisely the fibre maps
used by $\psi$ above.''')
s=replace(s,"On this principal bundle the source's explicit\npresentation is",r'''For this principal bundle,
\cite[\S2, pp.~1666--1667]{BrinzanescuMoraru2005}
gives the presentation and automorphy coordinates''')
s=span(s,'divisor on a Hopf surface or a positive multiple of the\nrational cycle on an Enoki surface. If the source states',' Formula \\eqref{cdp:eq:C.INT.2}',r'''divisor on a Hopf surface or a positive multiple of the
rational cycle on an Enoki surface. To apply its integral
homological-triviality hypothesis, multiply the divisor
by an integer killing its torsion integral Chern class
and use Poincar\'e duality. Multiplication changes each
coefficient by that integer and preserves the support,
so the stated support and proportionality conclusion
holds for the original divisor.''')
save('INT_1',s)

s=old('INT_2')
s=s.replace(r'\SeriesRef{cdp:st:A.4.4}',r'\cref{cdp:st:C.2.UN.17}')
s=s.replace(r'\cite[Lemma~2.22 and the following paragraph]{Dloussky2006}',r'\cite[arXiv v3, Definition~2.20, p.~14; Lemma~2.22 and the following paragraph, p.~15]{Dloussky2006}')
s=replace(s,'''The effective numerically anticanonical divisor on
an Enoki minimal model makes it parabolic Inoue;
this is the Enoki case in''',r'''Push the effective $D_i$ to the Enoki minimal model.
A positive multiple of its canonical-boundary line is
topologically trivial. On this class VII surface the
coefficient isomorphism and flat-character map
\eqref{cdp:eq:C.CA.11} identify it with a complex-flat
line. Thus the pushed divisor is numerically
anticanonical in Definition~2.20 of
\cite[arXiv v3, p.~14]{Dloussky2006}.
Its minimal model is therefore parabolic Inoue by''')
s=replace(s,'''\\item The canonical evaluation used in \\cref{cdp:st:C.2.UN.17} gives, on a
neighbourhood of this fibre,''',r'''\item Apply \cref{cdp:st:C.2.UN.17} to the restriction
$f:f^{-1}(\Delta)\to\Delta$ and the same full divisor
$F=\sum_i m_iS_i$. Its canonical evaluation gives''')
s=replace(s,'''Applying the
canonical divisor formula to the second equality
\\eqref{cdp:eq:C.INT.5} therefore gives at every blowup''',r'''Apply \cref{lem:II:canonical-boundary-blowup} at each
point blowup, with its upstairs boundary equal to
$(D_i^{\rm self})_{\rm new}$ and its downstairs boundary
the pushforward $(D_i^{\rm self})_{\rm old}$. The second
identity in \eqref{cdp:eq:C.INT.5} has zero real
canonical-boundary class, so the lemma's coefficient
formula gives''')
s=replace(s,'''The derivative of $\\Phi$ at the origin is
invertible, proving the required equivalence
of the local fibres.''',r'''The derivative of $\Phi$ at the origin is invertible.
More explicitly, near the chosen root of $u(0)$ solve
\[
 \tau^d=u(\tau^{-n}X,\tau^{-n}Y,\tau^{-2}Z).
\]
Its derivative in $\tau$ at $(X,Y,Z)=0$ is nonzero.
The implicit function theorem gives a holomorphic
solution, and
$(X,Y,Z)\mapsto(\tau^{-n}X,\tau^{-n}Y,\tau^{-2}Z)$
is the inverse of $\Phi$. Thus it identifies the same
full fibres with their original multiplicities $a,b$.''')
s=span(s,'The circle collapses to a smooth disc at each','The whole sphere lies in the local chart:',r'''Apply \cref{lem:II:monomial-curve-matching-sphere}
with $b'=c'=1$ to the smooth connected graph
$B_t=\{(z,v):v=g(z)\}$ over this sector. The function
$v$ on $B_t$ has the two specified simple zeros.
Its surface $y_{\rm lem}z_{\rm lem}=v$ is identified
with \eqref{cdp:eq:C.INT.13} by
\[
 (x_{\rm lem},y_{\rm lem},z_{\rm lem})
       \longmapsto (x,y,z)=(y_{\rm lem},z_{\rm lem},x_{\rm lem}),
 \qquad (x,y,z)\longmapsto(z,x,y).
\]
The displayed circle is exactly that lemma's circle
over the chosen path. Its endpoint charts give a
smooth embedded sphere of self-intersection $-2$.
The inverse of $\Phi$ transports it to the original
unit-bearing fibre. These holomorphic coordinate
isomorphisms preserve the complex orientation
and the compact intersection pairing.
''')
save('INT_2',s)

s=old('INT_3')
s=replace(s,'''This is an actual factorization, not a replacement
of the normalization by its minimal model.
''','')
s=replace(s,'''\\item We next prove a simultaneous cohomological
comparison on the entire, possibly nonreduced,
conductor. Relative duality applied to
$R\\pi_{i*}\\OO_{Z_i}=\\OO_{T_i}$ gives
$R\\pi_{i*}\\omega_{Z_i}=\\omega_{T_i}$.
Finite conductor duality identifies''',r'''\item Apply analytic proper duality
\cite[\S2.2.2, p.~60]{vanStraten1987} to
$\pi_i:Z_i\to T_i$ and $\OO_{Z_i}$.
Both spaces are Cohen--Macaulay of pure dimension two,
so their dualizing complexes are $\omega_{Z_i}[2]$
and $\omega_{T_i}[2]$. The already proved identity
$R\pi_{i*}\OO_{Z_i}=\OO_{T_i}$ identifies its two
derived Hom complexes and gives
$R\pi_{i*}\omega_{Z_i}=\omega_{T_i}$.
Apply \cref{lem:II:conductor-duality} to the finite
normalization of this same reduced hypersurface $S$.
On its component $T_i$ it identifies''')
s=replace(s,'''For completeness the canonical pushforward for a
point blowup is elementary:''',r'''For the canonical pushforward at each point blowup,''')
s=replace(s,'''Projection formula and
\\eqref{cdp:eq:C.INT.20}--\\eqref{cdp:eq:C.INT.21} identify the actual spaces''',r'''The two lines $\nu^*M|_{T_i}$ and $\tau_i^*M_i^0$
pull back under $\pi_i$ to the same line
$h_i^*M=\sigma_i^*M_i^0$. Applying $\pi_{i*}$ to
this isomorphism and using $\pi_{i*}\OO_{Z_i}=\OO_{T_i}$
and projection formula identifies the two lines on $T_i$.
Now projection formula and
\eqref{cdp:eq:C.INT.20}--\eqref{cdp:eq:C.INT.21} identify the spaces''')
s=replace(s,'''This is where the full conductor scheme is used;
no passage to its reduction is assumed harmless.
''','')
s=replace(s,r'Lemma~\ref{lem:II:last-blowup-minimal-resolution}',r'\cref{lem:II:last-blowup-minimal-resolution}')
save('INT_3',s)
print('Prepared INT.1--3 receivers; no main/shared writes.')

# Complete earlier-owner guards: only permanent-equation aliases are transferred.
owner_guards=[]
def owner(label):
    pos=MAIN.index(r'\label{'+label+'}')
    start=MAIN.rfind(r'\begin{',0,pos)
    stop=MAIN.index(r'\end{proof}',pos)+len(r'\end{proof}')
    return MAIN[start:stop]
def alias_display(s,label,tags,labels):
    marker=r'\label{'+label+'}'
    idx=s.index(marker)
    left=s.rfind(r'\begin{equation}',0,idx)
    right=s.index(r'\end{equation}',idx)
    display=s[left:right]
    anchors=''.join(r'\hypertarget{tag-'+x+r'}{}' for x in tags)
    aliases=''.join(r'\label{'+x+'}' for x in labels)
    if r'\SsixEquationAliases{' in display:
        # All extant aliases are simple label calls; preserve one macro per display.
        display=re.sub(r'\\SsixEquationAliases\{((?:\\label\{[^}]+\})+)\}',lambda m:r'\SsixEquationAliases{'+m.group(1)+aliases+'}',display)
        display=display.replace(r'\SsixEquationAliases{',anchors+r'\SsixEquationAliases{',1)
    else:
        display=display.replace(marker,anchors+r'\SsixEquationAliases{'+aliases+'}'+marker)
    return s[:left]+display+s[right:]
def guarded_owner(label,new,change_id,key):
    before=owner(label)
    (OUT/f'S6_SERIES_PUBLISH_{key}_original.tex').write_text(before)
    (OUT/f'S6_SERIES_PUBLISH_{key}_proposed.tex').write_text(new)
    owner_guards.append(dict(change_id=change_id,old_text=before,new_text=new))

p=owner('lem:II:delta-two-curve-rings')
p=alias_display(p,'cdp:eq:A.T.14',['00XK','00XL'],['cdp:eq:C.RA.7','cdp:eq:C.RA.8'])
guarded_owner('lem:II:delta-two-curve-rings',p,'II-C3-SEC07-P228-ALIASES','P228')
p=owner('cdp:st:A.5.18')
p=alias_display(p,'cdp:eq:A.T.15',['00XM'],['cdp:eq:C.RA.9'])
p=alias_display(p,'cdp:eq:A.T.16',['00WS'],['cdp:eq:C.RA.11'])
p=replace(p,r'''Furthermore
$x(zG)=(xz)G$, $y(zG)=(yz)G$, and
$z(zG)=(yz)^2-x(xz)^2$ all lie in $I^2$.''',r'''Furthermore the following products lie in $I^2$:
\begin{equation}
 x(zG)=(xz)G,\qquad y(zG)=(yz)G,\qquad
 z(zG)=(yz)^2-x(xz)^2.
 \hypertarget{tag-00WT}{}\label{cdp:eq:C.RA.12}
\end{equation}''')
guarded_owner('cdp:st:A.5.18',p,'II-C3-SEC07-A518-ALIASES','A5_18')
p=owner('lem:II:canonical-boundary-blowup')
p=alias_display(p,'cdp:eq:A.T.22',['00OJ'],['cdp:eq:C.IR.4'])
guarded_owner('lem:II:canonical-boundary-blowup',p,'II-C3-SEC07-P232-ALIAS','P232')

s=old('IRR_1')
s=replace(s,'''No assumption on the initial normalization singularities or
on the ambient Picard pullback is made.
''','')
s=span(s,r'\item We justify the numerical comparison','In the reverse sequence,',r'''\item At each ruling blowdown $\sigma:W\to W'$, apply
\cref{lem:II:canonical-boundary-blowup} with
$Z_1=W$, $Z_2=W'$, $D_1=D_W$, $D_2=\sigma_*D_W$,
and $m=d=\operatorname{mult}_{\sigma(E)}D_2$.
Its coefficient $a$ is the coefficient of this same
exceptional curve in $D_W$.
Identity \eqref{cdp:eq:C.IR.4} gives $a=d-1$
and zero rational canonical-boundary class downstairs.
This establishes the numerical class used in the preceding
step through the ruling map $\rho$.

''')
s=s[:s.index('\n\n\nThe elliptic ruled geometry')].rstrip()+'\n'
save('IRR_1',s)

s=old('RAT_1')
s=s.replace('Here is a direct bound for arbitrary coefficients,\nnot only for the polynomial $F$.','For arbitrary holomorphic coefficients, the bound is as follows.')
s=span(s,r'\item For two branches, the exact sequence',r'\item Let $N$ be the dual',r'''\item The remaining germs have at most two branches.
Apply \cref{lem:II:delta-two-curve-rings} to the same
reduced germ $H\subset Y$ and its normalization.
Its embedded ideals \eqref{cdp:eq:C.RA.7}--\eqref{cdp:eq:C.RA.8}
are obtained by lifting the specified normalization
coordinate functions to the ambient regular local ring;
the inverse function theorem makes that lift a
biholomorphic ambient coordinate change. Thus every
remaining non-lci germ is exactly one of those two ideals.

For the space cusp, use the identical generators
$g_1=y^2-xz$, $g_2=yz-x^3$, $g_3=z^2-x^2y$ and
$F=x^5+xy^3+z^3-3x^2yz$ in
\eqref{cdp:eq:A.T.15}. The finite-module calculation there
identifies $I^{(2)}=I^2+(F)$ in this same convergent
local ring: it uses the nine-element residue basis over
$\mathbb C\{x\}$ and generic rank nine, hence
$x$-saturation. The products \eqref{cdp:eq:C.RA.9}
are the identities under the coordinate identity map.
Our reduced equation belongs to $I^{(2)}$, since its
generic normal order is two.

''')
s=span(s,r'\item Write the local equation of $S$ as $cF+f_2$',r'\item The intrinsic cubic',r'''\item Write the local equation as $cF+f_2$, $f_2\in I^2$.
The conormal basis in \eqref{cdp:eq:C.RA.10} is
$(a,b)=(a_1,b_1)$ in \eqref{cdp:eq:A.T.16}.
The quadratic form of $F$ and its determinant are
therefore exactly \eqref{cdp:eq:C.RA.11}.
The local calculation following that identity uses
only the generic rank-one Hessian: its pole-four
term cannot cancel against a regular quadratic
form, so $c(0)=0$ and \eqref{cdp:eq:C.RA.9} gives
$cF\in I^2$. The resulting quadratic form is regular.
This transfers the rank-one calculation to the present
$A_2$ equation; its radical cubic is considered next.

''')
s=replace(s,'The exact derivatives are in the cited computation.',r'''In these lifts $dx=0$, so explicitly
$D^2g_1=2(dy)^2$, $D^2g_2=2\,dy\,dz$, and
$D^2g_3=2(dz)^2$; their pole orders are at most
ten, nine, and eight, respectively.
The Leibniz rule gives exactly the asserted bound
for every product with an arbitrary holomorphic coefficient.''')
s=span(s,r'\item The same argument is shorter for \eqref{cdp:eq:C.RA.7}.',r'\item In either non-lci case',r'''\item For the cusp-plus-line ideal \eqref{cdp:eq:C.RA.7},
use $(g_1,g_2,g_3)=(xz,yz,y^2-x^3)$.
The identity map of these generators identifies
$G=g_3$, $P=(z,G)$ and $Q_1=(x,y)$ with
\eqref{cdp:eq:A.T.17}. Its direct ideal-intersection
calculation gives $I^{(2)}=I^2+(zg_3)$,
and \eqref{cdp:eq:C.RA.12} gives the three annihilating
products in the same ring.
On the cusp branch $(t^2,t^3,0)$ use
$a=dg_1$, $b=dg_3$. The quadratic form of $zg_3$
is $t^{-2}ab$. Its determinant has pole four,
while a cross term with a regular form has pole at
most two. The generic rank-one condition therefore
makes its coefficient vanish at the origin;
\eqref{cdp:eq:C.RA.12} then puts the surface equation
in $I^2$.

The determinant corrections are four on the cusp
branch and two on the smooth branch $(0,0,t)$,
so the total determinant degree is again four.
Dual lifts on the cusp branch are
$t^{-2}\partial_z$ and $\frac12t^{-3}\partial_y$;
on the smooth branch they are
$t^{-1}\partial_x,t^{-1}\partial_y$.
The same product derivative formula bounds the
radical-cubic poles by six and two, respectively,
of total degree eight.

''')
s=s[:s.index('\n\n\nThe two classes')].rstrip()+'\n'
s=s.replace('This excludes the two non-lci cases, without assuming\nthat the conductor-image scheme is reduced.','This excludes the two non-lci reduced image germs; the conductor-image scheme retains its full structure throughout.')
save('RAT_1',s)

s=old('RAT_3')
s=s[:s.index('\n\n\nThe degree-one result')].rstrip()+'\n'
s=s.replace('[Every uncontracted degree-one horizontal image has nonnegative Euler number]','[Attachments of a rational horizontal boundary]')
a=s.index('Retain the torus-fibre')
b=s.index(r'\end{proposition}',a)
s=s[:a]+r'''Retain the torus-fibre, rational-normalization and ruled-boundary
morphism of \cref{cdp:st:C.2.RAT.1}. Suppose that $C$ is not
contracted, and put $H=h(C)_{\rm red}$.
Let $r_{\rm dom}$ count the original ruling fibres $F_j$
whose positive vertical boundary contains a strict
conductor component dominating $H$.
Among the other fibres retain those with a component
not exceptional for $\pi$, and write $K$ for their number.
They meet $C$ in $K$ distinct points. Let $\ell$ be the
number of identifications among their images on $H^\nu$,
so those images have $k=K-\ell$ distinct points.
Then
\[
 K\ge r-N_0-r_{\rm dom},\qquad
 e(S)\ge2-r_{\rm dom}-\ell .
\]
For a degree-one map $C\to H^\nu$, one has $\ell=0$ and
\[
       0\le r_{\rm dom}\le2,\qquad
       e(S)\ge2-r_{\rm dom}\ge0.
\tag{C.RA.21}\hypertarget{tag-00X3}{}\label{cdp:eq:C.RA.21}
\]
The generic transverse type and the conductor scheme
are those of the given fibre.
''' +s[b:]
s=replace(s,r'\item The conductor coefficient on $C$',r'\item In the degree-one case the conductor coefficient on $C$')
s=replace(s,'''\\item Discard those fibres and the $r_{\\rm dom}$ fibres counted
above. There remain at least
\\[
                        k\\ge r-N_0-r_{\\rm dom}''',r'''\item Discard those fibres and the $r_{\rm dom}$ fibres counted
above. The retained number satisfies
\[
                        K\ge r-N_0-r_{\rm dom},\qquad k=K-\ell''')
s=replace(s,'fibres with a surviving strict conductor component and\nnone dominating $H$.','The retained fibres have a surviving strict conductor\ncomponent and none dominating $H$.')
s=replace(s,'''Every intervening connected chain is contracted by
$\\pi$, so this is an actual intersection in $S$, not
an identification imposed on an auxiliary graph.''',r'''Every intervening connected chain is contracted by
$\pi$, so its common image is the stated intersection
of curves in $S$.''')
s=replace(s,'''The preceding $k$
intersections give $k$ distinct edges adjacent to the
vertex belonging to $H$. They remain distinct even
when two of their images are the same singular point:
$C\\to H^\\nu$ is an isomorphism, and the points on $C$
were distinct.''',r'''After identifying the retained points with the same
image on $H^\nu$, the $k$ distinct images give $k$
distinct branch-preimage edges at the vertex of $H$.
They remain distinct when their images on $H$ agree
but the points on $H^\nu$ differ. This is precisely
the definition of edges in the normalization-incidence graph.''')
s=replace(s,'''\\item Contract a spanning tree in each of those $c$ graph
components. The $k$ retained edges then give a connected
multistar with $c+1$ vertices and $k$ edges. Its first
Betti number is $k-c$, so the first Betti number
$\\beta$ of the full incidence graph satisfies''',r'''\item Contract a spanning tree in each of those $c$ graph
components. The $k$ retained edges give a connected
multistar with $c+1$ vertices and $k$ edges. Its first
Betti number is $k-c$. For $k=0$ the inequality
$n_G\ge k$ is immediate; otherwise this multistar
gives the displayed bound. Hence the first Betti
number $\beta$ of the full incidence graph satisfies''')
s=replace(s,'''      \\ge2-r+N_0+(r-N_0-r_{\\rm dom})
       =2-r_{\\rm dom}.''',r'''      \ge2-r+N_0+(r-N_0-r_{\rm dom}-\ell)
       =2-r_{\rm dom}-\ell.''')
s=replace(s,'This proves the assertion.',r'''For degree one $C\to H^\nu$ is an isomorphism, so
$\ell=0$, and the first step gives $r_{\rm dom}\le2$.
This proves both assertions.''')
save('RAT_3',s)

# The complete stronger and weaker tacnode statements receive one numbered owner.
a=old('RAT_2'); b=old('RAT_4')
header=a[:a.index(r'\end{proposition}')+len(r'\end{proposition}')]
header=header.replace('[A rational double cover of a smooth tacnode image]','[Rational double covers of tacnode images]')
header=header.replace(r'\label{cdp:st:C.2.RAT.2}',r'\label{cdp:st:C.2.RAT.2}\hypertarget{tag-01CG}{}\label{cdp:st:C.2.RAT.4}',1)
generic=b[b.index('Retain the torus-fibre'):b.index(r'\end{proposition}')]
header=header.replace('Retain the torus-fibre',generic+'\nFor a smooth image the stronger assertion is as follows.\nRetain the torus-fibre',1)
header=header.replace(r'\end{proposition}',r'\StatementRecord{cdp:st:C.2.RAT.4}{proved}{01CG}{\cref{cdp:st:C.2.RAT.3,cor:II:nonplanar-tacnode-cover}; \eqref{cdp:eq:C.RA.26}--\eqref{cdp:eq:C.RA.32}}'+'\n'+r'\end{proposition}',1)
proof=b[b.index(r'\begin{proof}'):b.index(r'\end{proof}')+len(r'\end{proof}')]
proof=span(proof,r'\item The low-delta classification',r'\item Let $\Xi$',r'''\item Apply \cref{lem:II:delta-two-curve-rings} to $H$
after excluding the three-branch germ by $b_1(H)\le1$.
Each nonplanar alternative has its single delta-two
singularity and the specified embedded ideal.
Apply \cref{cor:II:nonplanar-tacnode-cover} with its
rational normalization $\Sigma=H^\nu$, its same
degree-two conductor component $C\simeq\mathbb P^1$,
and its generic $A_3$ equation. All other boundary
components are vertical and supply no additional
branch over $H$. That corollary excludes exactly
these two alternatives, so $H$ is lci.

''')
# General loss-count is now the explicit application of the preceding shared owner.
proof=span(proof,r'\item As in \ref{cdp:st:C.2.RAT.3}',r'\end{enumerate}',r'''\item Apply \cref{cdp:st:C.2.RAT.3} to this same
ruled-boundary map and its selected attachments.
Here $r_{\rm dom}=0$, and its loss is $\ell=d'$:
a degree-two fibre loses one distinct image exactly
when both selected points lie over that value.
The preceding bound gives $d'\le d\le1$, so
\[
\begin{split}
 e(S)&=2-r+N_0+e(G)\ge2-K+e(G)\\
     &\ge2-K+(K-d')=2-d'\ge1 .
\end{split}
\tag{C.RA.32}\hypertarget{tag-00XG}{}\label{cdp:eq:C.RA.32}
\]
These are the same maps $Z\to T\to S$ and
$C\to\Sigma\to H$ as in the statement.

''')
# Append the stronger smooth-case arithmetic, retaining its exact fields and targets.
smooth=a[a.index(r'\item The two branches'):a.index(r'\item The initial reduced boundary')]
smooth=smooth.replace(r'\item The two branches',r'\item For the smooth-image refinement, the two branches',1)
# Its quadratic-field comparison has already been proved at full scope above.
smooth=span(smooth,'At the generic point of $H$, write the normal jet','Since\n$C\\simeq\\PP^1$',r'''Use the same normalized cover and quadratic field
from \eqref{cdp:eq:C.RA.26}: now $\Xi=0$ and
$\sigma=\Delta$. The inverse field maps are
$d=aw+b/2$, $w=(d-b/2)/a$, and the odd-order
normalization parameters are exactly those proved above.
''')
smooth+=r'''\item The maps \eqref{cdp:eq:A.RT.18}--\eqref{cdp:eq:A.RT.20}
apply to this same rational tree boundary and identify
$\pi_1(G)$ with the virtually abelian group $\pi_1(S)$.
Thus its free normalization-incidence group has rank
$\beta\le1$ and $e(G)=n_G+1-\beta\ge n_G$.
For $n_G=1$ the entire reduced image is the smooth
curve $H\simeq\mathbb P^1$, with Euler number two;
for $n_G\ge2$ the inequality also gives $e(G)\ge2$.
The complement identity \eqref{cdp:eq:A.RT.12} gives
\[
 e(S)=2-r+N_0+e(G)\ge4-r+N_0\ge2+N_0 .
\]
This proves \eqref{cdp:eq:C.RA.18} with its full vertical
boundary and normalization scope.
'''
proof=proof.replace(r'\end{enumerate}',smooth+'\n'+r'\end{enumerate}',1)
save('RAT_2_4',header+'\n\n'+proof)

s=old('RAT_5')
s=span(s,r'\item At most $3-d$ generic normalization branches','This proves the assertion.',r'''\item At most $3-d$ generic normalization branches are
supplied by vertical strict conductor components,
so $r_{\rm dom}\le3-d$.
Apply \cref{cdp:st:C.2.RAT.3} to the same
$Z\to T\to S$, its ruling and its $C\to H$.
The preceding simple-root argument proves that
the selected attachment points have distinct images
on $H=H^\nu$; hence its loss $\ell$ is zero.
Its exact attachment inequality gives
\[
 e(S)\ge2-r_{\rm dom}\ge d-1 .
\]
''')
save('RAT_5',s)

with (OUT/'S6_SERIES_PUBLISH_sec07_earlier_owner_guards.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['change_id','old_text','new_text'],delimiter='\t',lineterminator='\n')
    w.writeheader();w.writerows(owner_guards)
print('Prepared IRR.1, RAT.1--5 consolidation and three complete earlier-owner guards.')

# Shared cover owner: add exact aliases for the repeated specializations.
p=(OUT/'S6_SERIES_PUBLISH_P362.tex').read_text()
if r'\label{cdp:eq:C.RD.33}' not in p:
    p=p.replace(r'\mathcal Ext^2',r'\mathcal{E}xt^2')
    p=alias_display(p,'cdp:eq:C.DD.16',['00YO','00EA'],['cdp:eq:C.RD.33','cdp:eq:C.D4.18'])
    p=alias_display(p,'cdp:eq:C.DD.18',['00EB'],['cdp:eq:C.D4.19'])
    p=alias_display(p,'cdp:eq:C.RD.30',['00E8'],['cdp:eq:C.D4.16'])
    p=replace(p,'''Consequently every summand in \\eqref{cdp:eq:C.DD.6}
    has vanishing $H^1$.''',r'''Consequently
    \begin{equation}
     H^1(W,\OO_W)=H^1(W,L^{-1})=H^1(W,L^{-2})=0.
     \hypertarget{tag-00Y2}{}\label{cdp:eq:C.RD.13}
    \end{equation}''')
    p=replace(p,'''The exceptional first Betti numbers equal those of the
    corresponding links: the boundary sequence of a plumbed
    neighbourhood identifies the intervening second-homology
    map with its invertible exceptional intersection matrix.''',r'''The exceptional first Betti numbers equal those of the
    corresponding links: the boundary sequence of a plumbed
    neighbourhood identifies the intervening second-homology
    map with its invertible exceptional intersection matrix.
    
    For later use, each reduced exceptional divisor $E$
    satisfies $b_1(E)\le2p_g(X_0,x)$.
    To verify this, restrict a good resolution to a Stein
    representative. The finite-length stalk
    $M=(R^1\rho_*\OO_X)_x$ equals its completion.
    The ideals $I=\OO_X(-E)$ and
    $J=\mathfrak m_x\OO_X$ have the same radical and
    $I^a\subset J\subset I$ for some $a>0$, since $E$
    is compact. The containments
    $I^{an}\subset J^n\subset I^n$ identify their
    cohomology inverse limits. Analytic formal functions
    identifies this limit with
    $\varprojlim H^1(nE,\OO_{nE})$
    \cite[\S6, Haupts\"atze I and IIa, p.~59]{Grauert1960D},
    with \cite[pp.~35--36]{Grauert1963ErratumD}.
    The kernels of successive thickening restrictions
    have one-dimensional support, hence no $H^2$;
    all restrictions on $H^1$ are surjective.
    Successively lifting a class gives a surjection
    $M\to H^1(E,\OO_E)$.
    For the connected SNC curve $E$, its normalization
    sequence gives $h^1(\OO_E)=\sum g_i+\beta$ and
    $b_1(E)=2\sum g_i+\beta$, where $\beta$ is the
    rank of its incidence graph. This proves the bound.
    ''')
    p=replace(p,''' q(X)=P_g-1\\ (P_g>0),\\qquad q(X)=0\\ (P_g=0).''',r''' q(X)=P_g-1\ (P_g>0),\qquad q(X)=0\ (P_g=0),
     \qquad q(X)=\max(P_g-1,0).''')
    (OUT/'S6_SERIES_PUBLISH_P362.tex').write_text(p)

s=old('D4_1')
s=span(s,r'\item Put $N=N_{H/Y}$',r'Write'+'\n'+r'\[',r'''\item Restrict the compact map to the stated disc.
It is proper, with connected fibres because its
nearby two-tori and its irreducible central support
are connected. Apply \cref{lem:II:normal-cubic-compact-core}
to this same $f$, full divisor $mS$, and smooth
rational curve $H$.
Its $N,M,P,U_P$ are the present normal bundle,
normal line, cubic jet and level surface; put $U=U_P$.
The transport \eqref{cdp:eq:C.D4.2} uses the same
function $f$, with its unit and multiplicity.
Thus $b_1(U)\le3$ forces zero compact pairing,
and a spherical class of nonzero square is excluded
without any first-Betti hypothesis.

''')
# The first remaining Write is the splitting of N.
s=span(s,r'\paragraph{The cyclic compactification and its local invariants.}',r'\item Let $\rho:X\to X_0$',r'''\item Apply \cref{lem:II:cyclic-cubic-boundary} with
$W=E$, $L=\OO_E(1,1)$, and this same section
$b=P$ of $L^3$. Its equation \eqref{cdp:eq:C.D4.6}
defines the normal connected cover $X_0$.
Its inverse maps $w(v)=1$ identify the complement
with this $U$ in every tautological frame.

''')
s=span(s,r'\item \paragraph{Homology and the compact intersection pairing.}',r'For $c=1$,',r'''\item The cohomology bound
\eqref{cdp:eq:C.DD.8}, for this same resolution, and
\eqref{cdp:eq:C.D4.7} give
\[
                         b_1(X;\Q)=2q(X)\le2.
\tag{C.D4.8}\hypertarget{tag-00EJ}{}\label{cdp:eq:C.D4.8}
\]
For $c=1$ the branch class is the nonzero class $(3,3)$.
For $c=2$ the classes $(3,2)$ and $(0,1)$ are independent.
Thus the shared owner's parameters are
$b_0=1$, $r_B=c$, $\varepsilon=0$ and $g_B=g$.
Its formula \eqref{cdp:eq:C.D4.9} identifies the same
compact pairing on $U$, and its boundary estimate with
$\lambda\le2$ becomes
\[
                         b_1(D)\le2g+\nu-c+3.
\tag{C.D4.11}\hypertarget{tag-00E3}{}\label{cdp:eq:C.D4.11}
\]
Its unramified-cover Euler formula is exactly
\eqref{cdp:eq:C.D4.12} for these $c,g,\nu$.
''')
s=s.replace('proved immediately after \\eqref{cdp:eq:C.D4.2}.','in \\cref{lem:II:normal-cubic-compact-core}, applied at the first step.')
save('D4_1',s)

s=old('D4_2')
s=replace(s,'''normal-cone comparison \\eqref{cdp:eq:C.D4.1}--\\eqref{cdp:eq:C.D4.2}, and write''',r'''normal-cone maps of \cref{lem:II:normal-cubic-compact-core},
applied to this same proper disc restriction, $mS$ and $H$.
Write''')
s=span(s,'These conventions give',r'Let $A$ be the common zero divisor',r'''The tautological-bundle clause of
\cref{lem:II:cyclic-cubic-boundary} uses only $\deg N=-2$.
With $W=E$, $N=N_{H/Y}$ and this tautological $L$,
its identities \eqref{cdp:eq:C.DD.2} give
$\xi^2=2$, $\xi F=1$, $F^2=0$ and $K_E=-2\xi$.
''')
s=span(s,r'\paragraph{The exact cyclic-cover homology formulas.}',r'\paragraph{No common zero.}',r'''\item For each reduced total divisor below, use
\cref{lem:II:cyclic-cubic-boundary} with
$B=B_{\rm tot}$ and the same cubic $P$.
Its cover \eqref{cdp:eq:C.DD.6} has complement $U$
under the mutually inverse evaluation maps $w(v)=1$.
Write $c$ for the number of branch components,
$b_0=b_0(B)$, $\nu=\sum_x(r_x(B)-1)$,
$r=r_B$ for the rank of their classes, and
$\varepsilon=c-r$. Its total normalization genus
is $g_B=g$, because the section and vertical fibres
are rational. Let $\lambda$ be its exceptional
first-Betti sum. Thus \eqref{cdp:eq:C.DD.7}--\eqref{cdp:eq:C.DD.10}
apply with exactly these symbols, including disconnected
boundary and dependent classes.

''')
s=span(s,r'\paragraph{A double common zero: normalization of the cyclic cover.}',r'\item In our global double-fibre case',r'''\item For $p^*A=2F_0$, apply the weighted clause of
\cref{lem:II:cyclic-cubic-boundary} to
$B_{\rm tot}=R_1+R_2+2F_0$, with the same $L$ and $P$.
Its normalized character algebra and relative direct image
are \eqref{cdp:eq:C.DD.16}--\eqref{cdp:eq:C.DD.17}.
The only intersections are those of $F_0$ with one
smooth horizontal branch, with contact $k=1$ or $2$
by \eqref{cdp:eq:C.DD.14}. Take $s$ as a defining
coordinate of this $F_0$ and $u$ its contact parameter.
Then the actual local cover is
\eqref{cdp:eq:C.DD.18}; its unit is absorbed by the
cube-root change of $w$ with inverse multiplication
by that unit root. The successive root-line and
character maps are exactly
\eqref{cdp:eq:C.DD.19}--\eqref{cdp:eq:C.DD.20}.
The shared owner's complete resolution therefore
makes these singularities rational and their
exceptional first Betti numbers zero.

''')
save('D4_2',s)

s=old('RAT_7')
s=span(s,r'\item Form the cyclic triple cover',r'\item Write'+'\n'+r'\[',r'''\item Apply \cref{lem:II:cyclic-cubic-boundary}
with the present $N,W$, $L=\OO_W(1)$,
$P=q_3$, and reduced divisor $B=R_1+R_2$.
Its finite cover is $p_0:X_0\to W$,
its resolution is $X$, and its complement is
$U=\{q_3=1\}$ under the inverse maps $w(v)=1$.
Its three character vanishings are
\eqref{cdp:eq:C.RD.13}; hence
$H^1(X_0,\OO_{X_0})=0$ for this splitting of $N$.
By \eqref{cdp:eq:C.DD.8} and
\cref{cdp:st:C.2.RAT.6}, using the delta-five
identity \eqref{cdp:eq:C.RD.12},
$q(X)\le\sum p_g(X_0,x)\le1$, so $b_1(X)\le2$.

''')
s=span(s,r'\item Let $d_D$',r'Now use $e(X)',r'''\item In the notation of
\cref{lem:II:cyclic-cubic-boundary}, take
$c_{\rm lemma}=2$, $b_0=c$, $g_B=0$, and
$r_B=\dim\operatorname{span}\{[R_1],[R_2]\}$.
Thus
\[
 \varepsilon=2-\dim\operatorname{span}\{[R_1],[R_2]\}
       \in\{0,1\}.
\]
Its relation maps use precisely
$g^*R_i=3B_i+\sum_j a_{ji}E_j$, where
$g=p_0\rho$ and $B_i$ is the strict ramification curve.
Its pair sequence therefore gives
$b_1(U)=b_1(X)+\varepsilon\le3$ and the same compact
intersection pairing. Let $d_D$ be the number of
components of $D$.
''')
s=span(s,'The compact-core transport after \\eqref{cdp:eq:C.D4.2}','contradiction proves $\\nu\\le1$.',r'''Apply \cref{lem:II:normal-cubic-compact-core}
to the same $f,mS,H$ and cubic $q_3$.
Its level is this $U$ and its transport preserves
this compact pairing. Since $b_1(U)\le3$, its
vanishing conclusion contradicts the positive rank.
This ''')
s=span(s,'With\n$K\\ge r-N_0-r_{\\rm dom}$',r'The Euler formulas',r'''The remaining generic triple branch gives
$r_{\rm dom}\le1$. In \cref{cdp:st:C.2.RAT.3}
use the same ruling, map $C\to H$, and selected
vertical boundaries. Their loss $\ell$ is at most
one by the just proved bound. The exact attachment
inequality, with $K\ge r-N_0-r_{\rm dom}$, gives
''')
s=replace(s,r'''The Euler formulas \eqref{cdp:eq:A.RT.4} and
\eqref{cdp:eq:A.RT.12} give
''','')
save('RAT_7',s)

s=old('RAT_8')
s=replace(s,'''its compact Newton face is $(1,1,1)$. Its
geometric genus is therefore one by''',r'''its compact Newton face is $(1,1,1)$.
The local duality map in \cref{lem:II:cyclic-cubic-boundary}
identifies the colength of the adjunction ideal
$\rho_*\omega_X\subset\omega_{X_0}$ with $p_g$ at
this same isolated hypersurface singularity.
Thus its geometric genus is one by''')
s=span(s,r'\item Let $\rho:V\to T$ be a good resolution',r'Equation \eqref{cdp:eq:C.RD.22} yields',r'''\item Apply the exceptional-divisor bound in
\cref{lem:II:cyclic-cubic-boundary} to each actual
cubic-suspension singularity of $X_0$ and its good
resolution. Its $E$ is the corresponding reduced
exceptional divisor, and the same plumbed-neighbourhood
map identifies $H_1(E;\Q)$ with link homology.
Thus $b_1(\operatorname{link}(X_0,x))\le2p_g(X_0,x)$.
''')
s=span(s,r'\paragraph{The compact pairing and the attachment count.}',r'Put $\nu=\sum_p(r_p(B)-1)$.',r'''\item Apply \cref{lem:II:cyclic-cubic-boundary}
to the same $W,N,L=\OO_W(1),P=q_3$ and reduced
divisor $B=R_1+R_2+F$. Its evaluation maps identify
the complement with $U=\{q_3=1\}$.
The parameters are $c=3$, $b_0=1$, $g_B=0$,
$r_B=2$ and $\varepsilon=1$: the section $R_1$
and fibre $F$ have independent classes, and the
third is in their two-dimensional span.
Together with \eqref{cdp:eq:C.RD.22}, its cohomology
formula gives $b_1(X)\le2$ and $b_1(U)\le3$.
''')
s=span(s,'The rank identity is the same Gysin, Hodge-index','This proves $\\nu\\le3$.',r'''This is \eqref{cdp:eq:C.DD.9} with the
displayed parameter substitution and
\eqref{cdp:eq:C.RD.23}. For $\nu\ge4$ it has positive
rank, contrary to \cref{lem:II:normal-cubic-compact-core}
for this same $q_3=1$ and full fibre $mS$.
''')+'' # following sentence remains as exact conclusion
s=span(s,'Finally $r_{\\rm dom}\\le1$ and',r'\['+'\n'+r'                 e(S)',r'''The remaining generic branch gives $r_{\rm dom}\le1$.
Apply \cref{cdp:st:C.2.RAT.3} to this same ruled
boundary and selected attachments, with the loss
$\ell$ of \eqref{cdp:eq:C.RD.26}. Its inequality is
''')
save('RAT_8',s)

s=old('RAT_9')
s=replace(s,r'Use the ordinary cyclic algebra of \eqref{cdp:eq:C.RD.13}.',r'''Apply the reduced-cover construction of
\cref{lem:II:cyclic-cubic-boundary} with $P=q_3$
and $L=\OO_W(1)$. Write $p_0:X_0\to W$ for its
finite cover, whose algebra is \eqref{cdp:eq:C.DD.6}.''')
s=span(s,r'\item The irregularity of a resolution is zero.',r'\item Put $U=X_0',r'''\item Apply the reduced clause of
\cref{lem:II:cyclic-cubic-boundary} to this same
$W$, $L=\OO_W(1)$ and reduced total branch divisor.
Its $P_g$ is the present $P=\sum_xp_g(X_0,x)$.
Formula \eqref{cdp:eq:C.RD.30} therefore gives
$q(X)=0$, since \eqref{cdp:eq:C.RD.29} has $P\le1$.
Thus $b_1(X)=0$.

''')
s=span(s,'Write $g^*B_i=3\\widetilde B_i',r'The branch divisor and resolved boundary are connected.',r'''Apply \cref{lem:II:cyclic-cubic-boundary}
with $c=4$, $b_0=1$, $g_B=0$ and $r_B=2$.
Its pullback and strict-coefficient relation maps
are those of this same $g=p_0\rho$ and these
four branch curves. Hence $\varepsilon=2$,
$b_1(U)=2$, and its compact-pairing identity applies.
''')
s=span(s,'The evaluation isomorphism in the proof of',r'Thus this compact pairing'+'\n'+r'has rank zero.',r'''The evaluation maps of
\cref{lem:II:cyclic-cubic-boundary} identify this
$U$ with the same normal level $\{q_3=1\}$.
Apply \cref{lem:II:normal-cubic-compact-core}
to this full fibre and $H$; since $b_1(U)=2$,
the preserved compact pairing has rank zero.
''')
s=s.replace('Thus this compact pairing\nhas rank zero. ','')
s=span(s,'Apply the graph count at the end of the proof of',r'\paragraph{One double common zero value.}',r'''Apply \cref{cdp:st:C.2.RAT.3} to the same curve
$C$, its degree-two map to $H$, and the specified
vertical trees. Its loss is the present $\ell$,
and the remaining generic branch gives
$r_{\rm dom}\le1$. The resulting inequality is
$e(S)\ge2-r_{\rm dom}-\ell\ge0$.

''')
s=span(s,r'\paragraph{One double common zero value.}',r'\item We check that every singularity',r'''\item Now let $A=2p$. Apply the weighted clause of
\cref{lem:II:cyclic-cubic-boundary} with
$B_{\rm tot}=R_1+R_2+2F_p$ and $L=\OO_W(1)$.
Its normalized character algebra is
\eqref{cdp:eq:C.RD.33}, with the identical generator
$w^2/s$ along this $F_p$.
Its relative image \eqref{cdp:eq:C.DD.17} is
$\OO_H(-1)$, so $H^1(X_0,\OO_{X_0})=0$.

''')
s=s.replace('The graph inequality yields',r'Apply \cref{cdp:st:C.2.RAT.3} with this loss $\ell=0$ and $r_{\rm dom}\le1$. It gives')
save('RAT_9',s)

s=old('D4_3')
s=s.replace('The local\ntable gives precisely',r'The table in \cref{cdp:st:C.2.RAT.6} gives precisely')
s=span(s,r'\item A finite attachment bound',r'\item At a point where the cubic',r'''\item Apply \cref{cdp:st:C.2.RAT.3} to this same
Hirzebruch-boundary map. Since all three generic branches
come from $C$, its $r_{\rm dom}=0$.
Let $K$ and $k$ be its retained attachment counts
before and after mapping to $H=H^\nu$, and set
$\ell=K-k$. Its exact inequality gives
\[
             e(S)=2-r+N_0+e(\Gamma_{\rm red})\ge2-\ell.
\tag{C.D4.13}\hypertarget{tag-00E5}{}\label{cdp:eq:C.D4.13}
\]

''')
s=span(s,'The cyclic cover $X_0$ has $\\omega_{X_0}',r'Modulo the exceptional classes,',r'''Apply \cref{lem:II:cyclic-cubic-boundary} to this
reduced divisor, with $W=\mathbb P^1\times\mathbb P^1$,
$L=\OO(1,1)$ and its same cubic section.
Its $P_g$ equals this number $P$ by
\eqref{cdp:eq:C.D4.15}. Formula \eqref{cdp:eq:C.D4.16}
gives $q(X)=\max(P-1,0)$.

''')
s=span(s,r'\paragraph{A double common zero.}',r'\item The reduced boundary has two components',r'''\item For the double common zero, the divisor is
$R_{(3,1)}+2F$ on the same $W$.
Apply \cref{lem:II:cyclic-cubic-boundary} with
$L=\OO_W(1,1)$. Its character algebra
\eqref{cdp:eq:C.D4.18} is the one with local basis
$1,w,v=w^2/s$ and multiplication
$w^2=sv$, $wv=sr$, $v^2=wr$, where $s=0$
defines $F$ and $r=0$ defines $R$.
Its three character lines have bidegrees
$(0,0)$, $(-1,-1)$, $(-2,-1)$ and zero $H^1$.

The smooth curve $R$ meets $F$ with contact
$k=1,2$ or $3$. The exact local equation is
\eqref{cdp:eq:C.D4.19}, with $s$ the equation of
this $F$ and $u$ its contact parameter; a local
unit is removed by the cube-root change of $w$
and its inverse. The same successive maps
\eqref{cdp:eq:C.DD.19}--\eqref{cdp:eq:C.DD.20}
are therefore its resolution. They give rational
singularities, so $q(X)=0$ and the exceptional
first-Betti sum is zero.

''')
s=s.replace('the same exact homology\ncalculation now gives',r'''the parameter substitution
$c=2$, $b_0=1$, $g_B=0$, $r_B=2$, $\varepsilon=0$
in \eqref{cdp:eq:C.DD.9}--\eqref{cdp:eq:C.DD.10} gives''')
save('D4_3',s)
print('Prepared D4.1--3 and RAT.7--9 complete receiving fragments.')

# The monodromy and angular equations move to their full earlier owners.
p=owner('night:P4.13')
p=alias_display(p,'cdp:eq:C.MS.6',['014Y'],['cdp:eq:C.UI.6'])
p=replace(p,r'''The open stratum of a strict
transform is exactly the''',r'''In particular the exceptional components satisfy
\begin{equation}
 N_j\ge2m_0\quad\text{for every exceptional }E_j.
 \hypertarget{tag-014X}{}\label{cdp:eq:C.UI.5}
\end{equation}
The open stratum of a strict
transform is exactly the''')
p=replace(p,r'''\[
 m e(S_{\mathrm{reg}})=\det(I-A^m),\qquad
 0\le e(S_{\mathrm{reg}})\le16/m,
 \qquad m>1\ \Longrightarrow\ e(S_{\mathrm{reg}})=0.
\]''',r'''\begin{equation}
\begin{gathered}
 m e(S_{\mathrm{reg}})
   =\sum_{q=0}^4(-1)^q\operatorname{Tr}(\Lambda^qT^m)
   =\det(I-A^m),\\
 0\le e(S_{\mathrm{reg}})\le16/m,\qquad
 m>1\ \Longrightarrow\ e(S_{\mathrm{reg}})=0 .
\end{gathered}
 \hypertarget{tag-0150}{}\label{cdp:eq:C.UI.8}
\end{equation}''')
guarded_owner('night:P4.13',p,'II-C3-SEC07-P413-ALIASES','P4_13')
p=owner('cdp:st:C.2.NC.1')
p=replace(p,r'''\[
 \{(u_1,\ldots,u_r)\in(S^1)^r:
                 u_1^{a_1}\cdots u_r^{a_r}=e^{i\theta}\}.
\]''',r'''\begin{equation}
 \{(u_1,\ldots,u_r)\in(S^1)^r:
                 u_1^{a_1}\cdots u_r^{a_r}=e^{i\theta}\}.
 \hypertarget{tag-014Z}{}\label{cdp:eq:C.UI.7}
\end{equation}''')
guarded_owner('cdp:st:C.2.NC.1',p,'II-C3-SEC07-NC1-ALIAS','NC_1')

s=old('UN_7')
s=replace(s,'''The alternatives in the last three items exhaust the
irrational ruled case. No vanishing of $b_1(Y)$ or $b_2(Y)$
is used in the first four conclusions.''',r'''The alternatives in the last three items exhaust the
irrational ruled case.''')
s=s.replace(r'\begin{proof}\leavevmode\par',r'\begin{proof}')
s=s.replace('leftmargin=0pt,labelsep=.5em','leftmargin=*')
s=re.sub(r'\\item \\par\\medskip\\noindent\\textbf\{([^}]+)\}\\quad',r'\\item \\textbf{\1}',s)
s=span(s,r'\item \textbf{The proper analytic Lefschetz formula.}',r'\item \textbf{Finite-character comparison.}',r'''\item \textbf{Monodromy.}
Apply \cref{night:P4.13} to $f|_U:U\to\Delta$.
Its cohomology monodromy $T$ is this $T_1$, and
its minimum full multiplicity $m_0$ is $m$.
The resolution is chosen over $\operatorname{Sing}S$,
so the strict open stratum is $S_{\rm reg}$ and
\eqref{cdp:eq:C.UI.5} excludes exceptional contributions
at the power $m$. The local angular fibre is
\eqref{cdp:eq:C.UI.7} of \cref{cdp:st:C.2.NC.1}
with the same multiplicities $a_i$.
Thus \eqref{cdp:eq:C.UI.6} and the torus
cup-product identification in that owner give
\eqref{cdp:eq:C.UI.8} for this same $T_1$.
Quasi-unipotence and the real/conjugate eigenvalue
products there give \eqref{cdp:eq:C.UI.1}.

''')
s=span(s,r'\item \textbf{Strict positivity for a rational normalization.}',r'\item \textbf{All noncontracted irrational ruled alternatives.}',r'''\item \textbf{Rational normalization.}
Apply \cref{prop:II:rational-torus-fibre-euler} to
this same proper map, its full irreducible fibre
$mS$, and its minimal normalization resolution
$h=\eta\pi$. It proves item~1, including the
nonzero-$H^1$ refinement. The conductor and
complement maps in \eqref{cdp:eq:C.UI.12}--\eqref{cdp:eq:C.UI.13}
are exactly those of these same $\eta,\pi$.

''')
s=span(s,'''The proof of \\ref{cdp:st:C.2.IRR.1} uses the
ambient condition''','''including its assertion that no horizontal
component is contracted.''',r'''Use the proof of
\cref{cdp:st:C.2.IRR.1} with this same $h,Z,D$
and ruling. Its numerical input is precisely
$c_1(K_Z+D)=0$ in \eqref{cdp:eq:C.IR.2};
\cref{lem:II:torus-tube-numerical} gives this
torsion line on the present tube.
The ruling contractions and their divisor
pullbacks are unchanged, so
\eqref{cdp:eq:C.IR.4}--\eqref{cdp:eq:C.IR.5}
give the same disjoint elliptic horizontal curves.
The finite conductor rings, their sheet involution,
and the maps $(u,t)\mapsto(ut,u,t^2)$ are local to
these same normalization maps. Their full local
function is still a unit times the $m$th power,
so \cref{cdp:st:A.5.15,cdp:st:A.5.17} give the
same isolated-point and ramified-pinch exclusions.
Finally \cref{cdp:st:C.2.NC.1} applies to this
proper disc restriction and proves
\eqref{cdp:eq:C.IR.9}. Thus the complete blowdown,
ring and Euler comparison proves item~2, ''')
s=replace(s,'including its assertion that no horizontal\ncomponent is contracted.','including that no horizontal component is contracted.')
a=s.index(r'\item  The local numerical hypotheses of')
b=s.index(r'\item  Consequently the image',a)
s=s[:a]+r'''\item For the conductor genus bound, put
$e=h^0(S,\omega_S)\in\{0,1\}$.
The identities already supplied by
\cref{lem:II:torus-tube-numerical} give
$h^1(\OO_S)=1+e$. For this same finite normalization
the injection $H^0(\eta_*\OO_T/\OO_S)\hookrightarrow
H^1(\OO_S)$ and conductor section duality
\eqref{eq:II:conductor-section-duality}
give \eqref{cdp:eq:A.J.31}.
Restriction to each reduced image component and
degree-zero curve Riemann--Roch give
$p_a(H)\le2$, with the same formula
\eqref{cdp:eq:A.J.32} on its normalization.
These are the maps in the first two steps of
\cref{cdp:st:A.5.14}, now with the torsion and
Euler identities established on this tube.
Its delta-one local ring identifications are
unchanged analytic local rings in the same smooth
threefold chart.

For the jet comparisons, take exactly
$I=\mathcal I_{H/U}$, its torsion-free normalized
conormal, its dual $N$, and
$M=\OO_U(S)|_{H^\nu}$.
The degree-zero lines $M$ and $K_U|_{H^\nu}$
come from \cref{lem:II:torus-tube-numerical}.
Thus the determinant, radical, intrinsic cubic,
quartic and conductor-clearing maps in
\cref{cdp:st:A.5.5} are defined on these identical
bundles, with the same orders along the identical
curve conductor. The cusp proof
\cref{cdp:st:A.5.20} and the tacnode proof
\cref{cdp:st:A.5.18} use these genus and degree
identities. Their local normalizations,
root-field maps and unit-preserving coordinate
changes apply to the same equations on this tube.
The rational-image group map in the latter is
the tube quotient of $\mathbb Z^4\rtimes\mathbb Z$,
which this proper family supplies.

For the ordinary-triple proof
\cref{cdp:st:A.5.19}, the same low-delta ideals,
their symbolic cubes and their conormal
determinants apply to $I$; the above genus bound
and zero ambient degrees are its global inputs.
Its singular rational-image conclusion
therefore excludes a positive-genus covering
component here as well. For a smooth rational
image, \cref{lem:II:normal-cubic-compact-core}
gives $M=\OO_H$, $\deg N=-2$ and the actual
transport into this nearby torus.
The complete root-divisor and cover arguments
of \cref{cdp:st:C.2.D4.1,cdp:st:C.2.D4.2}
then apply to this same cubic and exclude
degrees three and two respectively.
The ruled differential comparison
\cref{cdp:st:A.5.10} uses the same map
$h^*T_U\leftarrow T_Z$; its Chern input
$c_2(h^*T_U)=0$ is also supplied by
\cref{lem:II:torus-tube-numerical}.

''' +s[b:]
s=replace(s,'''The same actual topological
pushout as above and van Kampen give''',r'''Apply \cref{lem:II:proper-conductor-pushout}
with $(X,Y,A,C,h)=(Z,S,D_{\rm red},\Gamma_{\rm red},\eta\pi)$.
Its support and complement hypotheses are
\eqref{cdp:eq:C.UI.14}; analytic triangulation
makes $D_{\rm red}\hookrightarrow Z$ a cofibration.
Its double mapping cylinder and van Kampen give''')
s=span(s,r'\item  For its comparison with the nearby torus,','If $n\\ge1$ is the number',r'''\item The quotient map in \cref{night:P4R.1}
makes this $\pi_1(S)$ virtually abelian.
Since \eqref{cdp:eq:C.UI.15} identifies it with
the free incidence-graph group, its rank
$\beta$ is at most one: a finite-index subgroup
of a free group of rank at least two contains
nonzero powers of two free generators, whose
commutator is nontrivial.
''')
s=s[:s.index('\n\n\nThe assertion $e(S)=2$')].rstrip()+'\n'
save('UN_7',s)

s=old('UN_12')
s=replace(s,'cases, stated for these actual maps.','cases, for these normalization and resolution maps.')
s=span(s,'This is an equivalence for fibres of the specified map.',r'\end{proposition}','')
s=span(s,r'\item For clarity, the horizontal possibilities',r'All these comparisons remove vertical conductor',r'''\item Apply \cref{cdp:st:C.2.UN.7} to the same proper
map $f$, full fibre $mS$, minimal resolution $Z$,
and its ruling. Its reduced-horizontal clause is
the first row of \eqref{cdp:eq:C.IZ.1}. Its twice-section
clause has the same branchwise conductor exponent
two and gives exactly the remaining three rows,
with the respective normalized conductor maps
of degrees one, two and three. Its contracted-section
clause has positive Euler number, so contributes
no zero case.
''')
s=span(s,r'\item It remains to check and extend the class VII part.',r'\item We sharpen the exceptional terms',r'''\item Apply \cref{cdp:st:C.2.VII.1} directly to the
compact class VII surface $Z$ and its effective
divisor $D$, whose canonical-boundary line is
the torsion line $h^*\omega_S$. With its
$r(R)=r$ and $R=D_{\rm red}$, it gives
\[
 e(R)=r,\qquad r\le b_2(Z).
 \tag{C.IZ.4}\hypertarget{tag-00OQ}{}\label{cdp:eq:C.IZ.4}
\]
Apply \cref{cdp:st:C.2.VII.2} to this same compact
hypersurface $S\subset U$, finite normalization
$\eta:T\to S$, conductor image $\Gamma$ and
class VII resolution $\pi:Z\to T$.
Its hypotheses $\omega_S$ torsion and
$\chi(\OO_S)=0$ were established in the first step.
For $C=\Gamma_{\rm red}$ it gives
\[
 \chi(\OO_C)\ge-1,\qquad e(C)\ge0 .
 \tag{C.IZ.5}\hypertarget{tag-00OR}{}\label{cdp:eq:C.IZ.5}
\]
Its normalized components are rational or elliptic,
as finite images of the strict conductor curves
classified by \cref{cdp:st:C.2.VII.1}.

''')
s=span(s,r'\item We sharpen the exceptional terms',r'\item A class VII surface',r'''\item Apply \cref{lem:II:proper-conductor-divisor}
to $f|_U$, with its $(X,N,T,\nu,\rho)$ equal to
$(U,T,Z,\eta,\eta\pi)$ here.
Its canonical divisor is this same $D$.
It gives $R=h^{-1}(C)$, excludes all normalization
singularities outside the conductor, and identifies
the two restrictions in
\[
 Z\setminus R\xrightarrow{\ \simeq\ }
 T\setminus(\eta^{-1}C)_{\rm red}
 \xrightarrow{\ \simeq\ }S\setminus C .
 \tag{C.IZ.6}\hypertarget{tag-00OS}{}\label{cdp:eq:C.IZ.6}
\]
The first arrow is $\pi$ on this open set and the
second is $\eta$ on its unit-conductor locus.

''')
s=replace(s,'''The curve normalization sequence identifies the remaining
term, rather than replacing its singular points by a
model:''',r'''Apply \cref{lem:II:curve-euler-delta} to this
same reduced conductor curve $C$, with its
$r_x=s_x$ and $n_0$ as in the statement. Its
normalization sequence gives''')
s=s[:s.index('\n\n\nThe class VII surface input')].rstrip()+'\n'
save('UN_12',s)

s=old('MH_4')
s=span(s,r'\item Use the prime-order rational augmentation local system',r'\item If the cyclic character',r'''\item Under the full CDP hypotheses,
\cref{cdp:st:D.1.9} supplies a nonzero class
$\gamma_S\in H^1(S,\mathbb Z)$.
Apply \cref{lem:II:torus-tube-character} to
this same fibre, nearby torus and resolution
$h=\eta\pi$. Choose its prime $\ell$ and
augmentation local system $V$, of rank $d=\ell-1$.
Its support-duality map gives
$h^0(S,V)=h^1(S,V)=0$ and
$h^2(S,V)=h^4(S,V)$.
Its third-cohomology surjection and fourth-cohomology
isomorphism are induced by these same $\eta,\pi$.
Consequently
\[
 \begin{gathered}
 h^3(S,V)\ge h^3(Z,V),\qquad h^4(S,V)=h^4(Z,V),\\
 d\,e(S)\le 2h^4(Z,V)-h^3(Z,V).
 \end{gathered}
 \tag{C.MH.17}\hypertarget{tag-00QI}{}\label{cdp:eq:C.MH.17}
\]

''')
s=s.replace('Consequently every such actual fibre','Consequently every such fibre')
s=s.replace('the Euler number of every actual torus-degeneration','the Euler number of every torus-degeneration')
save('MH_4',s)

with (OUT/'S6_SERIES_PUBLISH_sec07_earlier_owner_guards.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['change_id','old_text','new_text'],delimiter='\t',lineterminator='\n')
    w.writeheader();w.writerows(owner_guards)
print('Prepared UN.7/UN.12/MH.4 and five earlier-owner guards.')




