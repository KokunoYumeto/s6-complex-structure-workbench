from S6_SERIES_PUBLISH_c3_foundations_sec07_helpers import *

s=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
p=Package('cubic_tensor','night:P4R.19')
start=s.index(r'\subsection{A triple spectral root with nonzero cubic tensor}')
stop=s.index(r'\subsection',start+12)
oldunit=s[start:stop]
old=block(oldunit,'night:P4R.19')
new=old
oldhead=r'''Let $f$ be the actual reduced local equation of the remaining
positive ruled support, and let $C_0$ be a smooth local branch
of its critical curve with generic transverse type $D_4$.
At a point where the cubic normal tensor along $C_0$ is
nonzero, that tensor is not the cube of a linear form.
Other critical-curve branches at the point are retained,
without a restriction on their generic transverse types.'''
newhead=r'''In the setting of \cref{lem:II:positive-ruled-conductor-graph},
let $f$ be the reduced local equation of $S$, and let
$C_0$ be a smooth local branch of its critical curve
with generic transverse type $D_4$.
At a point where the cubic normal tensor along $C_0$ is
nonzero, that tensor is not the cube of a linear form.
The generic transverse types on the other critical-curve
branches at that point are arbitrary.'''
new=p.edit(new,oldhead,newhead,'D01,D02,D08,D14,D25','night:P4R.19',
 'Name the existing complete positive-ruled global domain at P314 and the identical reduced equation; retain the nonzero-tensor exclusion and arbitrary other transverse types.')
new=new.replace(r'\StatementRecord{night:P4R.19}{proved}{02YC}{}',r'\StatementRecord{night:P4R.19}{proved}{02YC}{\cref{lem:II:positive-ruled-conductor-graph,lem:II:monomial-curve-matching-sphere,lem:II:weighted-initial-monodromy,night:P4.51}; \cite[Chapter~II, \S2.A, Theorem~(2.1), p.~80]{Demailly2012E}; \cite[Theorem~3.35, p.~245]{Hatcher2002}}')
oldinverse=r'''Its Jacobian determinant is one, and the two lower coefficients
are $a_1-a_2^2/3$ and $a_0-a_1a_2/3+2a_2^3/27$.'''
newinverse=r'''Its inverse is $x_{\mathrm{new}}=x_{\mathrm{old}}+a_2(y,z)/3$,
with $y,z$ fixed. Its Jacobian determinant is one, and
the two lower coefficients are $a_1-a_2^2/3$ and
$a_0-a_1a_2/3+2a_2^3/27$.'''
new=p.edit(new,oldinverse,newinverse,'D20','night:P4R.19',
 'Give the inverse of the exact depressing coordinate change, retaining its normal ideal and both transformed coefficients.')
new=p.edit(new,'The unit remains in this equality and in the scaling\ncomparison below.\n',
 '', 'D03,D08','night:P4R.19',
 'The complete displayed preparation and the later exact c=alpha0 U(0) already specify the unit; remove the prospective repetition.')
new=p.edit(new,'A double\nfactor of $Q$ is allowed throughout the argument.',
 'The last case includes cubics $Q$ with a double factor.',
 'D02','night:P4R.19','State the included algebraic case positively.')
new=p.edit(new,'monic equation $z^r=w$ and the other coordinates are\nretained.',
 'monic equation $z^r=w$, while $x=X(b)$ and $y=u$.',
 'D08,D20','night:P4R.19','Identify the unchanged source coordinates explicitly through the target projections.')
new=p.edit(new,r'''$-2r$ on the source. In particular this argument
retains $Q=(X-\lambda V)^2(X+2\lambda V)$,
$\lambda\ne0$, without a perturbation of its
repeated factor.''',r'''$-2r$ on the source. For
$Q=(X-\lambda V)^2(X+2\lambda V)$, $\lambda\ne0$,
this same degree-$r$ map gives the square $-2r$.''',
 'D02,D08,D20','night:P4R.19',
 'Preserve the exact repeated-factor polynomial and its map as a positive application, deleting process-relative perturbation rhetoric.')
a=new.index(r'\par\medskip\noindent\textbf{The compact class used in the comparison.}')
b=new.index(r'For the compactly supported Poincar',a)
oldmatching=new[a:b]
newmatching=r'''\paragraph{The compact class and its finite pullbacks.}
Each curve below is a smooth connected embedded curve
$B\subset\C^2_{x,h}$, with the second coordinate $h$
having simple zeros. Choose two of these zeros and an
embedded joining arc whose interior avoids the others.
Put
\[
 Z_h=\{(b,u,v)\in B\times\C^2:uv=h(b)\},\qquad
 X_B=\{(x,u,v):(x,uv)\in B\}.
\]
The holomorphic maps
\[
 (b,u,v)\longmapsto(x(b),u,v),\qquad
 (x,u,v)\longmapsto((x,uv),u,v)
\]
are inverse. Thus \cref{lem:II:monomial-curve-matching-sphere},
with $b'=c'=1$, gives the same smoothly embedded sphere
on $Z_h$, with self-intersection $-2$.
'''
new=p.edit(new,oldmatching,newmatching,'D12,D17,D20','night:P4R.19',
 'P297 already owns the full arc, endpoint polar charts, determinant/framing and square−2 proof. The displayed mutually inverse holomorphic maps identify precisely its b′=c′=1 surface with each Z_h used here. Keep the application-specific compact dual and finite-degree pullback formula.')
new=p.edit(new,'homology two-class with that square. Its representative need not itself\nbe a sphere.',
 'homology two-class with that square.', 'D02,D11','night:P4R.19',
 'State the positive Poincare-duality conclusion directly; no subsequent argument requires an embedded representative of the finite pullback.')
new=new.replace(r'\par\medskip\noindent\textbf{The exact finite maps.}',r'\paragraph{The finite maps.}')
new=new.replace(r'''           h(x)=\frac{1-x^3}{ax},\qquad x\in\mathbb C^*.
\]
The map''',r'''           h(x)=\frac{1-x^3}{ax},\qquad x\in\mathbb C^*.
\]
Here $B$ is the graph $\{(x,h(x)):x\in\C^*\}$.
The map''')
new=new.replace('It has degree $3l$, and the base is $\\mathbb C$.',
 'It has degree $3l$; here $B$ is the graph\n$\\{(x,(1-x^3)/b):x\\in\\C\\}$.')
p.record('D20','night:P4R.19','The base is C* or C.',
 'Embed the two bases as the graphs of h in C²; the balanced base is B_Q itself.',
 'Match the exact embedded-curve hypothesis of P297 without changing either finite map or degree.')
a=new.index(r'\par\medskip\noindent\textbf{Transport to the actual local fibre.}')
b=new.index(r'\par\medskip\noindent\textbf{Two colliding spectral directions.}',a)
oldtransport=new[a:b]
newtransport=r'''\paragraph{Transport to the full fibre.}
The global data are those of
\cref{lem:II:positive-ruled-conductor-graph}, which gives
$\pi_1(S)\simeq\mathbb Z$ and hence $b_1(S)>0$.
Thus the first assertion of \cref{night:P4.51} applies
to this same full fibre $mS$. Write its local function as
$\Phi=Vf^m$, choose a holomorphic logarithm of the unit
$V$, and put
\[
 f_V=\exp((\log V)/m)f,\qquad
 \alpha_0=\exp((\log V(0))/m),\qquad c=\alpha_0 U(0).
\]
The identity inclusion
$f_V^{-1}(\delta)\hookrightarrow\Phi^{-1}(\delta^m)$
is the full-fibre map in that proof, so the local
$f_V$-levels have zero intersection pairing.

Let $w=(w_x,w_y,w_z)$ be the positive integer weights
obtained above and let $d$ be their degree. The weighted
initial polynomial of $f_V$ is $cP$, including both
the original Weierstrass unit and the root of the
full-function unit. Apply the first clause of
\cref{lem:II:weighted-initial-monodromy} to $f_V$ with
\[
 D_\epsilon(x,y,z)=
 (\epsilon^{w_x}x,\epsilon^{w_y}y,\epsilon^{w_z}z),
 \qquad G_\epsilon=\epsilon^{-d}f_V\circ D_\epsilon.
\]
Its initial level is $\{cP=c\}=\{P=1\}$. The lemma
preserves each compact pairing under transport to
$f_V=c\epsilon^d$ in the original coordinate ball,
and then the identity inclusion places it in
$\Phi=(c\epsilon^d)^m$. The finite-map classes above
therefore have their same nonzero squares $-4k$, $-6l$
or $-2r$ on a local $f_V$-level, contradicting its zero
pairing. This proves the assertion, including the
balanced model with a repeated factor.

'''
new=p.edit(new,oldtransport,newtransport,'D12,D14,D20,D25','night:P4R.19',
 'P322 owns compact gradient transport and permits a nonreduced initial polynomial. Apply it to the exact full-function root, with initial cP and c=alpha0 U(0), keeping every multiplicity and both units. The subscript distinguishes this scalar from the compact cohomology class alpha. P314 supplies the same S with b1(S)>0, so P451 applies without a contracted-section hypothesis.')
a=new.index(r'\par\medskip\noindent\textbf{Two colliding spectral directions.}')
b=new.index(r'\end{enumerate}',a)
oldexample=new[a:b]
new=new[:a]+new[b:]
remark=r'''\begin{remark}[Affine fibres with two colliding spectral directions]
\hypertarget{tag-P324}{}\label{rem:II:two-direction-affine-fibres}
\StatementRecord{rem:II:two-direction-affine-fibres}{proved}{P324}{}
The reduced equation $f=y(x^2+y^2z^2)$ has generic
$D_4$ along $x=y=0$ and generic $A_1$ along $x=z=0$.
Two spectral directions collide at their intersection.
Its non-plane normalization sheets $x=\pm\mathrm i yz$
have pole divisor $2(y=0)+(z=0)$, with simple normal
crossings. Its affine fibre $f=1$ is isomorphic to
$(\C^*)^2$ and has zero intersection form. More generally,
for every integer $n\ge1$, the affine fibre of
$y(x^2+y^2z^n)$ has zero intersection form.
\end{remark}
\begin{proof}
For $z\ne0$, the three linear normal factors
$y$, $x+\mathrm i yz$, $x-\mathrm i yz$ are distinct,
giving the ordinary triple point $D_4$. For $y\ne0$,
the last two factors are coordinates transverse to
$x=z=0$: their Jacobian in $(x,z)$ is $-2\mathrm i y$.
They give the transverse node $A_1$.
On the smooth sheet $x=\pm\mathrm i yz$, the residue
of $dx\wedge dy\wedge dz/f$ is
$dy\wedge dz/(\pm2\mathrm i y^2z)$, proving the
stated pole divisor in the coordinates $(y,z)$.

For $n=2$ the maps are
\[
 \begin{split}
 a&=x+\mathrm i yz,\qquad b=x-\mathrm i yz,\\
 x&=(a+b)/2,\qquad y=(ab)^{-1},\qquad
 z=(a-b)ab/(2\mathrm i).
 \end{split}
\]
They are inverse by substitution, and their values satisfy
$y(x^2+y^2z^2)=1$. The product of two unit circles
generates $H_2((\C^*)^2;\Z)$; a radial translation
gives a disjoint homologous copy, so its square is zero.

For general $n$, the map $t=1/y$, $u=x/y$, with $z$
fixed, identifies the affine fibre with
\[
 W_n=\{u^2+z^n=t^3,\ t\ne0\};
 \qquad y=1/t,\quad x=u/t
\]
is its inverse. This is a smooth surface, since the
$t$-derivative is nonzero. Positive real dilation acts by
\[
 (u,z,t)\longmapsto(s^{3n}u,s^6z,s^{2n}t),\qquad s>0.
\]
Both sides of its equation scale by $s^{6n}$. It gives
the product diffeomorphism
\[
 (0,\infty)\times\{(u,z,t)\in W_n:|t|=1\}
 \longrightarrow W_n
\]
with inverse obtained from $s=|t|^{1/(2n)}$ and the
dilation by $s^{-1}$. Compact cycles have bounded
intervals in this positive real coordinate. A sufficiently
large dilation displaces one from another and is isotopic
to the identity, proving that all their pairings vanish.
\end{proof}
'''
p.record('D02,D03,D11,D12,D13,D20,D25','rem:II:two-direction-affine-fibres',oldexample,remark,
 'Give the independent original affine-family result one numbered owner. Keep the exact inverse maps and all local type/pole conclusions. Supply the explicit weighted real-product map for every positive n. The affine calculation itself does not assert a global torus-fibration counterexample; the original broad collision rhetoric is removed without changing R19 or its arbitrary other-branch domain.')
new=p.clean(new,'night:P4R.19')
newunit=r'\subsection{Cubic normal tensors along a critical branch}\label{subsec:II:cubic-normal-tensors}'+'\n\n'+new+'\n'+remark+'\n'
p.guard('R19-complete-subsection',oldunit,newunit,
 'Complete old/current and receiving subsection comparison; all old assertions and R19.1–5 identifiers retain their scope. P297/P322 exact maps replace the repeated constructions, and the existing affine example becomes P324.')
p.write(newunit)
