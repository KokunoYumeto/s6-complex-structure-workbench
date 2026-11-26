from pathlib import Path
import json, re, datetime
from S6_SERIES_PUBLISH_editing import Editor, block

r=Path(__file__).resolve().parents[1]
ed=Editor('I')
original=ed.text
standard=block(ed.text,'fam:st:A.5.2')
general=block(ed.text,'push:src:E.2.1')
p53=block(ed.text,'night:P5.3')
p54=block(ed.text,'night:P5.4')
app_start=ed.text.index(r'\section{Tangent cohomology and deformations}')
app_end=ed.text.index(r'\section{The integral parameter comparison}',app_start)
old_appendix=ed.text[app_start:app_end]
kp_start=old_appendix.index(r'\begin{proof}[Koszul and direct-image proof')
kp_end=old_appendix.index(r'\end{proof}',kp_start)+len(r'\end{proof}')
koszul=old_appendix[kp_start:kp_end]

def replace_once(s,a,b):
 if s.count(a)==0 and s.endswith(a.rstrip()):
  a=a.rstrip()
 assert s.count(a)==1,(s.count(a),a[:120])
 return s.replace(a,b)

def proof_items(s):
 a=s.index(r'\begin{enumerate}[label=\arabic*.,leftmargin=*]')+len(r'\begin{enumerate}[label=\arabic*.,leftmargin=*]')
 b=s.index(r'\end{enumerate}',a)
 return re.split(r'\n\s*\\item ',s[a:b].strip())[1:] if not s[a:b].strip().startswith(r'\item ') else re.split(r'\n\s*\\item ',s[a:b].strip()[6:])

gi=proof_items(general)
assert len(gi)==8,len(gi)
ki=proof_items(koszul)
assert len(ki)==5,len(ki)

gi[0]=r'''The root lift, its proper flat Gorenstein charts, base change and
relative duality are those of \cref{push:src:E.3.1}.
Write $m=3k$ and $n=4l$. The finite root charts have the specified
free affine cyclic actions, and the cusp charts are $q=z_0z_1z_2$.'''
gi[1]=replace_once(gi[1],r'''The original determinant calculation can also
be repeated: its quotient line $L$ has
$L^{12}=\mathcal O(-p_0)=\mathcal O(-12z)$, so
$L=\mathcal O(-z)$ because the Picard group is torsion-free.
''','')
gi[1]=gi[1].replace('For completeness, the analytic Picard group','The analytic Picard group')
gi[2]=r'''Under the marked root-forgetting map in the preceding step,
the constant lattice cocycle $\gamma$ is unchanged. Its finite-chart
representatives and its cusp edge values $(0,-1,-1)$ therefore
give the nowhere-zero cohomology line proved in \cref{inv:D1.2}.
The cusp resolution and cup-product pairing are those of
\cref{push:src:E.3.1}; pulling the linear period factors through $r$
gives the quotient line $\mathcal O(-z)$.
Relative duality gives
$R^2\bar f_*\mathcal O_X=\mathcal O(-z)$ and
$\det R^1\bar f_*\mathcal O_X=\mathcal O(-z)$.
The extension of that quotient by the specified $[\gamma]$-line
splits because $H^1(\mathcal O(z))=0$, as computed in step~5.
Connected fibres give $\bar f_*\mathcal O_X=\mathcal O$.
These maps prove the three structure-sheaf direct images.'''
gi[3]=gi[3].replace(r'\bar f^*\mathcal E',r'\bar f^*E')
gi[4]=replace_once(gi[4],'''We give the weighted cohomology calculation explicitly; simply
replacing $1$ by $kl$ in an acyclicity assertion would be incorrect.
''','')
gi[5]=replace_once(gi[5],r'''The program \texttt{e\_push\_exact.py} independently checks these
counts for all $1965$ coprime pairs with $k,l\le80$; the monomial
argument proves them for all pairs.
''','')
gi[7]=replace_once(gi[7],'''Finally $\\partial_c\\Pi''',r'''The derivative $\partial_c\Pi''')
cut=gi[7].index('The Kuranishi local algebra is')
ks=gi[7][:cut]
ks+=r'''With the tangent-lift convention $[\bar\partial h]$, this
class changes sign, as the explicit lift comparison in
\cref{fam:src:A.4.2} shows. The parameter and the transition-arrow
convention in the statement specify the displayed sign.'''
gi[7]=ks

ki[0]=replace_once(ki[0],r'''The first connecting map of (D.3) is''',r'''The first connecting map of \eqref{fam:eq:ab-log-tangent} is''')
ki[0]=replace_once(ki[0],'''These arguments establish the three nonzero coefficients; they do not
infer them from a global cohomology dimension. Rescaling the two
quotient frames and the source frame makes all three coefficients one.''',r'''For the following matrices only, write the frames of $E,G$ as
$(e_1,e_2)$ and $(g_1,g_2)$ and replace them by
\[
 e'_1=(a/c_0)e_1,\quad e'_2=e_2,\qquad
 g'_1=b g_1,\quad g'_2=c_0g_2.
\]
The coefficients of $e'_1\otimes g'_2$, $e'_2\otimes g'_1$ and
$e'_2\otimes g'_2$ are then $y,y,x$.
The geometric cocycle $\xi\otimes\gamma$ keeps its original
meaning; $e'_1\otimes g'_1=(ab/c_0)\xi\otimes\gamma$ in these
matrix frames.''')
ki[1]=replace_once(ki[1],'''Indeed one constant linear combination of the two $\\OO(-1)$ summands
is unused, and the remaining quotient is given by the exact sequence''',r'''Use the ordered frames
$u=e'_1\otimes g'_2+e'_2\otimes g'_1$ and
$v=e'_1\otimes g'_2$ for the two $\OO(-1)$ summands.
The change matrix has determinant $-1$, the image is $yu+xe'_2g'_2$,
and $v$ gives the unused summand. The remaining quotient is the exact sequence''')
ki[2]=replace_once(ki[2],'''There
$x$ is a unit, and elementary row and column operations identify it
with''',r'''There $x$ is a unit. For target generators $q_1,q_2$, the
relations are $-yq_1-xq_2=0$ and $yq_2=0$. Eliminating
$q_2=-(y/x)q_1$ gives the single relation $y^2q_1=0$ and hence''')
ki[2]=ki[2].replace('where $2p_1$ means the length-two divisor on the root chart, not the\ndouble coarse point.','where $2p_1$ is the length-two divisor in the root coordinate $y$.')
ki[3]=replace_once(ki[3],'''Thus the quotient is the
pushforward of the normal line of $\\nu$, not $\\OO_W(W)$.''',r'''Thus the normal-coefficient map identifies the quotient with
the pushforward of the normal line of $\nu$.''')
ki[4]=replace_once(ki[4],'''Finally Leray over a curve has only columns zero and one. The usual
cohomology of these displayed line bundles gives the four asserted
dimensions. This is a direct-image computation, not an inference from
the tangent Euler characteristic.''',r'''The coarse direct images are the ones displayed in the statement;
their Leray cohomology agrees with the tuple obtained in step~7.''')

heads=general[:general.index(r'\StatementRecord')]
heads=heads.replace('[tangent cohomology and local miniversality]','[Tangent cohomology, direct images and miniversality]')
for old in (standard,p53,p54):
 heads+=''.join(re.findall(r'\\hypertarget\{tag-[^}]+\}\{\}|\\label\{[^}]+\}',old[:old.index(r'\StatementRecord')]))+'\n'

statement=r'''\StatementRecord{push:src:E.2.1}{proved}{032U}{\cref{push:section:E.1,push:src:E.3.1,inv:D1.1,inv:D1.2}}
Let $k,l$ be positive integers with $\gcd(3k,4l)=1$, and let $X$
be a sphere member with multiplicities $(3k,4l)$ and the admissible
logarithmic data of \cref{push:section:E.1}. Put $z=kl$ and
$d=3k+4l$. On $\mathfrak B_{k,l}=\mathbb P(3k,4l)$, the vertical
root bundle $E$, the root lift $\bar f$ and its direct images satisfy
\[
 \begin{split}
 E&=\mathcal O\oplus\mathcal O(-z),\\
 R^q\bar f_*\mathcal O_X&=
 \mathcal O,\quad\mathcal O\oplus\mathcal O(-z),\quad\mathcal O(-z),\\
 K_X&=\bar f^*\mathcal O(z-d).
 \end{split}
\]
The tangent cohomology is
$\bigl(h^0,h^1,h^2,h^3\bigr)(X,T_X)=(1,1,1,0)$.
For the transition-arrow convention
$\kappa(\Phi)=(\partial_c\Phi)\Phi^{-1}$, the Kodaira--Spencer
class of $\partial_c$ is $e\otimes[\gamma]$, and the class of
$\partial_u$ is $-(2\pi i u)^{-1}e\otimes[\gamma]$.
Both classes are nonzero. The primary Kuranishi bracket vanishes,
the Kuranishi germ is a smooth reduced disc, and the fixed-data
period family is locally miniversal.

For the standard $(3,4)$ data, $e=\xi$ and the coarse direct
images are
\[
 f_*T_X=\mathcal O\oplus\mathcal O(-1),\qquad
 R^1f_*T_X=\mathcal O\oplus\mathcal O(-1)^2,\qquad
 R^2f_*T_X=\mathcal O.\tag{D.4}
\]
\end{theorem}
'''
deform=r'''Let $\alpha$ denote the nonzero tangent class just constructed.
The holomorphic family gives a convergent deformation with this tangent.
Differentiating its integrability equation gives
$\bar\partial\alpha_2=-[\alpha,\alpha]/2$. Thus the primary
bracket vanishes; bilinearity and $h^1(T_X)=1$ give vanishing on
every pair.

Douady's principal theorem in \S VII.8 and Theorem~1 and its
corollary in \S VIII.1 give a minimal versal analytic germ with
tangent space $H^1(T_X)$. The identification of this tangent space
uses tangent-valued \v Cech cocycles of transition maps, with changes
of trivialization acting by coboundaries. Its local algebra is
$\mathbb C\{t\}/I$. The parameter family induces
$t\mapsto g(c)$ with $g'(c_0)\ne0$. By the analytic inverse
function theorem, substitution by $g$ is injective; it annihilates
$I$, so $I=0$. The classifying map is an isomorphism of germs.
Pullback of the versal family realizes every sufficiently small
deformation and proves local miniversality.'''
fullproof='\n\\begin{proof}\n\\begin{enumerate}[label=\\arabic*.,leftmargin=*]\n'
fullproof+='\n\n'.join('\\item '+x.strip() for x in gi)
fullproof+='\n\n\\item '+deform+'\n\n'
fullproof+=r'''\item For the standard data we compute the coarse direct images
by the following Koszul maps. All root bundles in this step are on
$\mathcal B=\mathbb P(3,4)$.
\begin{enumerate}[label=(\alph*),leftmargin=*]
'''
fullproof+='\n\n'.join('\\item '+x.strip() for x in ki)
fullproof+='\n\\end{enumerate}\n\\end{enumerate}\n\\end{proof}\n'
newappendix=r'''\section{Tangent cohomology and deformations}
\subsection{Tangent direct images and local miniversality}
\hypertarget{tag-000D}{}\label{app:rederive:fam-src-A.5.2}
\hypertarget{tag-02ZF}{}\label{push:section:E.2}
\begin{remark}[The standard deformation theorem]
\hypertarget{tag-PI11}{}\label{I:standard-deformation-credit}
For the standard data $(\ell_0,\ell_1,\ell_2)=(0,1,-1)$,
the tangent dimensions and smooth reduced Kuranishi germ are
\cite[Theorem~6.12, pp.~81--82; Proposition~6.16, p.~85]{DuEtAl2026v1}.
We re-derive that case in this appendix. The weighted calculation
also covers the coprime multiplicities stated below, and the
standard case includes the coarse tangent direct images.
\end{remark}

'''+heads+statement+fullproof+'\n\n'

ed.replace(standard,'','D12','Merge the standard tangent statement into the single general theorem, retaining the standard coarse direct-image clause and every original anchor.','fam:st:A.5.2')
ed.replace(p53,'','D12','Archive the alternate ordinary-tangent cohomology proof; its complete conclusion and identifiers are attached to the unified tangent theorem. The unique ordinary direct-image tables and conductor proof remain separate.','night:P5.3')
ed.replace(p54,'','D12','Archive the alternate first-order period proof; retain the full common transition-arrow Kodaira--Spencer proof and the analytic ideal argument, including the versal-germ input, in the unified theorem.','night:P5.4')
ed.replace(general,'','D12','Move and consolidate the weighted tangent proof in the credited appendix, using the shared root/cusp foundations and preserving its weighted monomial and residue calculations.','push:src:E.2.1')
old_heading=r'''\subsection{Tangent cohomology for arbitrary coprime multiplicities}\hypertarget{tag-02ZF}{}\label{push:section:E.2}'''
ed.replace(old_heading,'','D15','Move the existing subsection anchor with its theorem to the credited tangent appendix.','push:section:E.2')
credit_start=ed.text.index(r'\paragraph{Source and re-derivation of the tangent theorem.}')
credit_end=ed.text.index('\n\n',ed.text.index('section; this does not alter',credit_start))
oldcredit=ed.text[credit_start:credit_end]
ed.replace(oldcredit,'','D01','Replace the run-history paragraph by the precisely cited numbered credit remark in the appendix.','I:standard-deformation-credit')
ed.replace(old_appendix,newappendix,'D12','One full tangent theorem and proof combines the weighted calculation, standard direct images, exact frame maps, transition-arrow class, primary bracket and reduced Kuranishi germ. Remove duplicate introductory conventions and alternative standard proofs; preserve every anchor and equation.','push:src:E.2.1')
ed.save()
(r/'records/S6_SERIES_PUBLISH_I_tangent_consolidation_removed.json').write_text(json.dumps({
 'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'standard_statement':standard,'weighted_original':general,'standard_original_appendix':old_appendix,
 'ordinary_alternate':p53,'period_alternate':p54,'old_credit':oldcredit,
 'scope':'Complete source comparisons after prior exposure; no new independent mathematical check is claimed. Unique weighted and standard proof components are both in the final unified proof.',
 'frame_map':"e1'=(a/c0)e1, e2'=e2, g1'=b g1, g2'=c0 g2; matrix coefficients become y,y,x and e1'g1'=(ab/c0)xi gamma."
},indent=2)+'\n')
