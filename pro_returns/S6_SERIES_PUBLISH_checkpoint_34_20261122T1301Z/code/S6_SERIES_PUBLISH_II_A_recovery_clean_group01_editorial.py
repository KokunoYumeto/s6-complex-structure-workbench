"""Build literal editorial guards for four newly checked recovery owners.

Only released target blocks are read; canonical source and ledger are untouched.
"""
from pathlib import Path
import hashlib, json, datetime, re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/ii_checks_A/recovery_20261121T195642Z/clean_group01'
OUT.mkdir(parents=True,exist_ok=True)
sha=lambda b: hashlib.sha256(b).hexdigest()
paths={'01AZ':'4e4fc149f959124b','01B4':'522bd4b69fb725d1','01FJ':'bf65669bb7c7a000','01BB':'2d1e46b693b1cb90'}
blocks={t:(ROOT/f'agents/ii_infra/released_proofs/{t}/{p}/S6_SERIES_PUBLISH_full_owning_block.tex').read_text() for t,p in paths.items()}
original=blocks.copy()
guards=[]

def edit(tag,old,new,types,reason,transport):
    assert blocks[tag].count(old)==1,(tag,old[:120],blocks[tag].count(old))
    offset=blocks[tag].index(old)
    before_sha=sha(blocks[tag].encode())
    after=blocks[tag].replace(old,new,1)
    guards.append({'tag':tag,'guard_id':f'A_REC_CLEAN01_{len(guards)+1:03d}','defect_types':types,
      'literal_old':old,'literal_new':new,'reason':reason,'mathematical_transport':transport,
      'offset_before':offset,'intermediate_before_sha256':before_sha,'intermediate_after_sha256':sha(after.encode())})
    blocks[tag]=after

def numbered_displays(s):
    return re.sub(r'\\\[(.*?)\\\]',lambda m: '\\begin{equation}'+m[1]+'\\end{equation}' if '\\label{' in m[1] else m[0],s,flags=re.S)

def statement_display(tag,legacy):
    at=blocks[tag].index(legacy)
    start=blocks[tag].rfind('\\[',0,at)
    end=blocks[tag].index('\\]',at)+2
    old=blocks[tag][start:end]
    new=numbered_displays(old.replace(legacy,''))
    edit(tag,old,new,['D19'],'Use a numbered equation environment with section numbering.','The entire displayed formula, ordered label, and hypertarget are identical; only the inherited literal tag is replaced by the equation counter.')

def proof(tag,new,types,reason,transport):
    old=blocks[tag][blocks[tag].index('\\begin{proof}'):]
    edit(tag,old,numbered_displays(new),types,reason,transport)

edit('01AZ','What trivial normalization pullback forces','Conormal sections with trivial normalization pullback',['D16'],
     'Name the sheaf-theoretic conclusion in the title.','Identical hypothesis eta*A trivial and identical canonical image.')
edit('01AZ','the ambient group contains the canonical image','the group $H^0(S,V\\otimes A)$ contains the canonical image',['D08','D20'],
     'Identify the group using the standing conormal-filtration notation.','V=Omega_Y^1|S; this is the exact ambient group in the preceding notation and A.1.1.')
edit('01AZ','Proposition~7.3','\\cite[Proposition~7.3, pp.~693--694]{CDP20}',['D18'],
     'Bind the published subcase to the opened journal edition.','The same S and A=L_t|S, with eta*A trivial; published text lines 897--944, journal pp.693--694.')
edit('01AZ','the exact maps of \\ref{cdp:st:A.1.1}','the maps in Proposition~\\ref{cdp:st:A.1.1}',['D08','D23'],
     'Use the mathematical statement kind in the reference.','The maps remain K tensor A to V tensor A to Q tensor A.')
proof('01AZ',r'''\begin{proof}
\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]
\item Proposition~\ref{cdp:st:A.2.2} gives the inclusion in
\eqref{cdp:eq:A.3}. Tensoring it by the invertible sheaf $A$ and applying
the finite projection formula gives
\[
 \eta_*\eta^*(N^*\otimes A)\hookrightarrow K\otimes A
                         \hookrightarrow V\otimes A.
\]
Locally, for a defining equation $F$ of $S$, the first map sends
$b\otimes[F]$ to $b\,dF|_S$. The inclusion of the Jacobian ideal in the
conductor makes its coefficients holomorphic on $S$. Under $F'=uF$,
both the conormal frame and $dF|_S$ are multiplied by $u$, so these maps
glue. Taking global sections gives the claimed canonical injection.

\item A coordinate $t$ about the image point on the base defines the full
fibre by $F=t\circ f$. Since this full fibre is reduced, $[F]$ is a frame
of $N^*$. Its pullback, together with the chosen trivialization of
$\eta^*A$, identifies the source with
$H^0(\widetilde S,\OO_{\widetilde S})$. The nonempty compact normalization
has the nonzero constant function $1$ on each connected component.
This proves nonvanishing and applies to each $A=L_t|_S$ in the stated
published subcase.

\item The image lies in $H^0(S,K\otimes A)$, the kernel of
$H^0(S,V\otimes A)\to H^0(S,Q\otimes A)$ by
\eqref{cdp:A:filtration2}. Thus these nonzero sections map to zero in
the quotient group. Proposition~\ref{cdp:st:A.4.1} gives the stated
example with vanishing quotient group.
\end{enumerate}
\end{proof}''',['D02','D04','D08','D10'],
'Give the local map, full-fibre trivialization, and quotient kernel in three mathematical steps; replace the inherited equation number by its label.',
'Identity on S, eta, A, N*, K, V, Q; [F] maps to dF. The projection formula transports the same injection. The original crossing scope is unchanged because no crossing condition is added.')

edit('01B4','Arithmetic genus two and the embedded delta-one comparison','The genus bound and delta-one curve germs',['D16','D08'],
     'Identify both conclusions in the title.','The same bound p_a(D)<=2 and embedded node/cusp conclusion.')
statement_display('01B4','\\tag{A.J.30}')
edit('01B4','These conclusions do not require a nonconstant ambient\nPicard pullback.\n','',['D02','D11'],
     'The complete hypotheses already specify the theorem scope.','Every original hypothesis is retained, and no Picard condition is added.')
b4=blocks['01B4'][blocks['01B4'].index('\\begin{proof}'):]
a=r'''The evaluation, adjunction and fibre-equation comparisons
in (A.CD.1) use no Picard assumption and apply with
rational second-cohomology vanishing. They give a torsion
dualizing line $\omega_S$. The divisor Riemann--Roch
calculation gives $\chi(\OO_S)=0$. Thus, for
$e=h^0(S,\omega_S)\in\{0,1\}$, the same Serre-duality
calculation as in (A.CD.2) gives
$h^1(\OO_S)=1+e$; if $e=1$, then
$\omega_S\simeq\OO_S$.'''
b=r'''Restrict $f$ to a disc about the image of $mS$ and trivialize the
canonical line of the disc. The sheaf $f_*K_Y$ is torsion-free of rank
one, hence locally free there. The evaluation of a generator is
nonzero on the smooth nearby fibres, where their canonical lines are
trivial. Its zero divisor is therefore $aS$ for an integer $a\ge0$.
Thus $K_Y\simeq\OO_Y(aS)$ on this neighbourhood. The full-fibre equation
trivializes $\OO_Y(mS)$, and adjunction gives
$\omega_S\simeq\OO_Y((a+1)S)|_S$, a torsion line.
The Cartier sequence and Riemann--Roch on $Y$ give $\chi(\OO_S)=0$,
since $c_1(\OO_Y(S))=0$ in rational cohomology. A nonzero section of a
torsion line on the compact irreducible surface has a nonzero constant
tensor power; it therefore trivializes the line. Consequently
$e=h^0(S,\omega_S)\in\{0,1\}$, and Serre duality gives
$h^1(\OO_S)=1+e$. For $e=1$, the line $\omega_S$ is trivial.'''
assert a in b4
b4=b4.replace(a,b)
a='Conductor duality and curve Serre duality\ntherefore give'
b=r'''To identify the conductor-duality map, put
$\mathcal B=\eta_*\OO_T$ and $\mathfrak c=\operatorname{Ann}(\mathcal Q)$.
The normal surface $T$ is Cohen--Macaulay. Thus $\mathcal B$ is a
maximal Cohen--Macaulay module on the Gorenstein surface $S$.
Multiplication in the total quotient sheaf identifies
$\mathcal Hom(\mathcal B,\omega_S)$ with $\mathfrak c\omega_S$.
Applying $\mathcal Hom(-,\omega_S)$ to
$0\to\OO_S\to\mathcal B\to\mathcal Q\to0$ therefore gives
$\mathcal Ext^1(\mathcal Q,\omega_S)=\omega_S|_\Gamma$ and vanishing
of the other sheaf Ext groups. The local-to-global Ext sequence and
Serre duality identify
$H^0(S,\mathcal Q)^*$ with
$H^1(\Gamma,\omega_S|_\Gamma)$. Taking dimensions gives'''
assert a in b4
b4=b4.replace(a,b)
b4=b4.replace('\\tag{A.J.31}','').replace('\\tag{A.J.32}','')
b4=b4.replace('the exact numerical\ncomparison','the identity')
b4=b4.replace('the\nactual injection','the\ninjection')
b4=b4.replace('the specified\nthreefold','the threefold $Y$')
b4=b4.replace('Statement \\ref{cdp:st:A.5.5} now applies','Proposition~\\ref{cdp:st:A.5.5} applies')
proof('01B4',b4,['D04','D08','D19'],
'Expand the torsion-canonical and conductor-duality steps and replace inherited display tags; retain the complete embedded delta-one argument.',
'The same canonical evaluation is on the neighbourhood of mS. The Ext map identifies (H0 Q)* with H1(omega_S|Gamma), preserving A.J.31. The normalization and node/cusp ring maps are unchanged. All labels and hypertargets survive.')

statement_display('01FJ','\\tag{C.J.1}')
edit('01FJ','a finite etale cover of degree two, or a finite etale cover of degree three.',
     "a finite \\'etale cover of degree two, or a finite \\'etale cover of degree three.",['D23'],
     'Restore the accents.','The same two normalization-cover maps and degrees.')


fj=blocks['01FJ'][blocks['01FJ'].index('\\begin{proof}'):]
fj=fj.replace('\\tag{C.J.2}','').replace('\\tag{C.J.3}','').replace('etale',"\\'etale")
fj=fj.replace('Its normal line $P=N_{C/\\widetilde S}$ satisfies $P^2=R$ and $P^3=Q$, so has degree zero.',
r'''The leading terms $y=u^2$ and $x=u^3$ identify
$P^2$ with $R$ and $P^3$ with $Q$, where
$P=N_{C/\widetilde S}$. Adapted coordinate changes preserve these
leading terms through the corresponding line transitions. Thus
$\deg P=0$.''')
fj=fj.replace('Etale descent',"\\'{E}tale descent")
start=fj.index('\\item Finally')
end=fj.index('\\end{enumerate}',start)
fj=fj[:start]+r'''\item Compute the inverse Jacobian ideal in the parameter-preserving
normal forms, with coefficients holomorphic in the curve parameter $z$.
A biholomorphic coordinate change transforms the gradient by its
invertible Jacobian matrix; multiplication of the defining equation
by a unit multiplies the gradient by that unit modulo the equation.
These maps transport the following fractional ideals to $S$.

For the cusp set $B=\C\{u,z\}$ and
$A=\C\{u^2,u^3,z\}=\C\{z\}+u^2B$.
The Jacobian ideal has images $u^3,u^4$. For a multiplier $h$, put
$a=u^3h$. The conditions $a,ua\in A$ kill respectively the linear
and constant coefficients of $a$. Hence
$\mathcal J^{-1}=u^{-1}B$, agreeing with
Proposition~\ref{cdp:st:A.2.4} under the displayed normalization map.

For the tacnode the two maps are $x=\pm u^2,y=u$, and the image ring is
\[
 A=\{(f,g)\in B^2:f-g\in u^2B\}.
\]
Indeed, the inverse expression is
$(f+g)/2+x(f-g)/(2u^2)$. The Jacobian generators have images
$(u^2,-u^2)$ and $(u^3,u^3)$, up to nonzero scalar factors.
For $a=u^2h_1$ and $b=u^2h_2$ the membership conditions are
$a+b\in u^2B$ and $a-b\in uB$. Their constant coefficients vanish,
so each $h_i$ has at most a simple pole. Their residues are opposite:
\[
 \mathcal J^{-1}=B^2+\C\{z\}(u^{-1},-u^{-1}).
\]

For the ordinary triple point use the branches
$(0,u),(u,0),(u,u)$. The image ring consists of triples with a common
constant and with third linear coefficient equal to the sum of the
first two. All coefficients of degree at least two are independent:
for $k\ge2$ the polynomials
$y^k-xy^{k-1}$, $x^k-x^{k-1}y$, and $x^{k-1}y$ have respectively
the three individual order-$k$ branch values.
The Jacobian generators have images
$(-u^2,0,u^2)$ and $(0,u^2,-u^2)$.
For $a_i=u^2h_i$, the common-constant condition on both products forces
all three constant coefficients to vanish. The linear relations
give residues $(a,a,-a)$. Thus
\[
 \mathcal J^{-1}=B^3+\C\{z\}(u^{-1},u^{-1},-u^{-1}).
\]
For the tacnode and triple point, regularity of the products on each
normalization branch excludes poles of order greater than two before
these coefficient conditions are imposed. The three displayed modules are contained in the
invertible sheaf allowing a simple pole on the reduced inverse-image
curve. This proves the claimed bound at every point.

'''+fj[end:]
proof('01FJ',fj,['D08','D09','D19','D23'],
'Retain the jet argument, identify the normal-line maps, and replace program bookkeeping by the complete fractional-ideal calculation.',
'The notation transport from the frozen derivation is M=Q_old^*, Q_new=R_old^*, L=B_old; Delta_new=4 Delta_old. The cusp map is (u^3,u^2,z), the tacnode maps are (+/-u^2,u,z), and the triple branch order differs from the prefreeze program by transposition (1 2). All degree conclusions, covariance identities, pole bounds, labels, and tags survive.')

edit('01BB','This permits an initially singular normalization;\nsmoothness is part of the conclusion.\n','',['D11'],
     'The statement already gives a general normalization and concludes that it is smooth.',
     'The initial T remains an arbitrary normal surface satisfying the original hypotheses; no initial smoothness or minimality assumption is added.')
bb=r'''\begin{proof}
\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]
\item The section identifies $C$ with the positive-genus curve $B$.
The proper nonconstant map $C\to D$ is finite. At a general point of
$D$, the cusp normalization
\[
 (u,z)\longmapsto(u^3,u^2,z)
\]
has one branch and degree one on its singular curve. Thus $C\to D$ is
the normalization of $D$.
Proposition~\ref{cdp:st:A.5.14}, applied to the same $Y,S,D$, makes
$D$ smooth elliptic with constant cusp transversal. It follows that
$C\to D$ is an isomorphism and $B$ is elliptic.
Let $C_T\subset T$ be the inverse-image curve.
Proposition~\ref{cdp:st:C2d} gives a smooth neighbourhood of $C_T$,
the isomorphism $C_T\to D$, and
$\deg N_{C_T/T}=0$. Its leading normal terms identify the square and
cube of this normal line with the radical and Hessian quotient lines.

\item Factor the given resolution as
\[
 Z\xrightarrow{\sigma}Z'\xrightarrow{\mu}T,
 \qquad \pi=\mu\sigma,
\]
where $\mu$ is the minimal resolution and $\sigma$ is a sequence of
point blowups. Every $\sigma$-exceptional curve is $\pi$-exceptional
and is vertical for $p$. The map $p$ therefore descends to
$p':Z'\to B$. Explicitly, the proper image of $(\sigma,p)$ in
$Z'\times B$ projects finitely and bimeromorphically to the normal
surface $Z'$ with one point in every fibre. This projection is an
isomorphism and defines $p'$, with $p=p'\sigma$.
The curve $C'=\sigma(C)$ is a section and $\sigma|_C$ is an isomorphism.
Since $\mu$ is an isomorphism near $C_T$, one has
$(C')^2=\deg N_{C_T/T}=0$.

The strict transform of every $\mu$-exceptional curve is
$\pi$-exceptional, so those curves are vertical for $p'$.
Proposition~\ref{cdp:st:A.5.3} supplies the canonical effective divisor
on this minimal resolution. Its nonexceptional components have the
same conductor valuations as on $Z$. Consequently it has the form
$2C'+V'$, with $V'$ effective and vertical, and
\[
 \omega_{Z'}(2C'+V')\simeq(\eta\mu)^*\omega_S,
 \qquad c_1(K_{Z'}+2C'+V')=0\quad\hbox{in }H^2(Z',\Q).
\]
The constant cusp charts and the isomorphism of $\mu$ there show that
$V'$ is disjoint from $C'$.

\item Contract the vertical $(-1)$-curves of the irrational ruled
surface to obtain $\rho:Z'\to Z_0$, a $\mathbf P^1$-bundle over $B$.
Every rational curve is vertical because $B$ has positive genus.
Write $C_0=\rho(C')$ and $V_0=\rho_*V'$.
The image $C_0$ remains a section. The point-blowup formula for its
self-intersection gives $C_0^2=(C')^2+n=n\ge0$, where $n$ counts the
centres lying on the successive strict transforms of the section.
The divisor $V_0$ is an effective sum of fibres.
Pushing the canonical equality forward and intersecting with $C_0$
gives, by adjunction on the elliptic section,
\[
 0=(K_{Z_0}+2C_0+V_0)\cdot C_0
   =C_0^2+V_0\cdot C_0=n+V_0\cdot C_0.
\]
Thus $n=0$ and $V_0=0$.

For completeness, the conductor transform at a point blowup
$\beta:X\to X_0$ is determined by
$K_X=\beta^*K_{X_0}+E$: its exceptional coefficient is
$\operatorname{mult}_p(D_0)-1$. This is the same canonical divisor
identity used above. A ruling $(-1)$-curve meeting $C'$ cannot be a
component of $V'$, since $C'\cap V'=\varnothing$; its intersection
with $K_{Z'}+2C'+V'$ would be at least $-1+2=1$.

Since $n=0$, one has $C'=\rho^*C_0$.
All components of $V'$ are $\rho$-exceptional, and
\[
 K_{Z'}=\rho^*K_{Z_0}+E_\rho
\]
with $E_\rho$ effective and positive on every exceptional prime.
Hence $E_\rho+V'$ is numerically trivial and exceptional.
The total transforms of the successive exceptional curves of a
point-blowup sequence give an orthogonal basis with square $-1$.
The exceptional intersection form is therefore negative definite.
It follows that $E_\rho+V'=0$. Effectiveness gives
$E_\rho=V'=0$, so $\rho$ is an isomorphism and $Z'$ is the minimal
ruled bundle.

\item A vertical irreducible curve of this bundle is a fibre and has
square zero. To compare it with the exceptional curves of $\mu$,
use the local-function form of the intersection argument in
\cite[\S1, p.~6]{Mumford1961}.
For an exceptional fibre over a normal point, choose a nonzero
holomorphic function $g$ vanishing at that point. On the resolution
its divisor is $G+\sum m_iE_i$, with $m_i>0$ and $G$ the strict
transform of the zero curve. Pairing this principal divisor with
$E_j$ gives
$\sum_i m_i(E_i\cdot E_j)=-G\cdot E_j\le0$, with a strict inequality
for some $j$. The strict transform meets the exceptional fibre by
properness, and that fibre is connected because the target is normal.
For $A_{ij}=m_im_j(E_i\cdot E_j)$, its off-diagonal entries are
nonnegative and
\[
 x^{\mathsf T}Ax
 =\sum_i\left(\sum_jA_{ij}\right)x_i^2
     -\sum_{i<j}A_{ij}(x_i-x_j)^2.
\]
A vector in its zero locus has zero coordinate at a strict row, and
connectedness forces all coordinates to vanish. The exceptional
intersection form is negative definite. This argument uses the
displayed local holomorphic divisor and applies to the analytic
surface $T$.
Thus a square-zero fibre cannot be $\mu$-exceptional. The map $\mu$
has no exceptional curves, hence is finite and bimeromorphic; the
normality of $T$ makes it an isomorphism. Therefore $T=Z'$ is smooth
and minimal ruled over the elliptic curve $B$.

\item Finite duality on the smooth normalization identifies the
conductor ideal with the invertible ideal of its divisor, now
$2C_T$. Thus $\eta$ is an isomorphism off $C_T$, and its restriction
$C_T\to D$ is an isomorphism. The normalization is consequently a
proper continuous bijection and a homeomorphism of the underlying
compact spaces. Equivalently, additivity of Euler characteristic
gives
\[
 e(S)=e(T)-e(C_T)+e(D)=0.
\]
Here $e(T)=e(\mathbf P^1)e(B)=2\cdot0$, and both curves have genus one.
The full scheme fibre $mS$ has the same underlying space as $S$,
so its topological Euler characteristic is also zero.
\end{enumerate}
\end{proof}'''
proof('01BB',bb,['D04','D08','D11','D18'],
'Make the arbitrary-resolution to minimal-resolution transport, conductor effectiveness, ruling contraction, and analytic exceptional-intersection argument explicit.',
'The original pi factors as mu sigma, p=p_prime sigma, and C maps isomorphically to C_prime and C_T. The effective conductor is invoked only for mu via A.5.3; no effectiveness is imposed on the original V. The canonical transform coefficient mult_p(D0)-1, all normal-line conclusions, minimality, and Euler equality are preserved.')

records=[]
for tag,new in blocks.items():
    before=OUT/f'S6_SERIES_PUBLISH_II_{tag}_full_original.tex'
    after=OUT/f'S6_SERIES_PUBLISH_II_{tag}_full_proposed.tex'
    before.write_text(original[tag]);after.write_text(new)
    labels=lambda s: re.findall(r'\\(?:label|hypertarget)\{([^}]*)\}',s)
    assert labels(original[tag])==labels(new),(tag,'anchor change')
    records.append({'tag':tag,'original_path':str(before.relative_to(ROOT)),
      'original_sha256':sha(before.read_bytes()),'proposed_path':str(after.relative_to(ROOT)),
      'proposed_sha256':sha(after.read_bytes()),'original_characters':len(original[tag]),
      'proposed_characters':len(new),'guards':[g['guard_id'] for g in guards if g['tag']==tag],
      'anchors_exact':True})
for g in guards:
    g['full_original_path']=next(r['original_path'] for r in records if r['tag']==g['tag'])
    g['full_proposed_path']=next(r['proposed_path'] for r in records if r['tag']==g['tag'])
manifest={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'checker':'ii_check_a_recovery_blind','canonical_writes':False,'guards':guards,'blocks':records,
 'note':'New recovery proposals with current timestamps. No lost original B guard bytes are claimed restored. Complete comparative rereading is recorded separately after these files are read.'}
out=OUT/'S6_SERIES_PUBLISH_II_A_recovery_clean_group01_editorial_proposals.json'
out.write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'manifest':str(out.relative_to(ROOT)),'sha256':sha(out.read_bytes()),'guard_count':len(guards),'blocks':records},indent=2))

