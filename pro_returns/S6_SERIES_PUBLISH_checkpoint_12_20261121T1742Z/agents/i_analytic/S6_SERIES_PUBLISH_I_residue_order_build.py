from pathlib import Path
import json,hashlib,re,csv,datetime
R=Path('/workspace/scratch/653608133b22'); O=R/'work/agents/i_analytic'; s=(R/'work/S6_SERIES_PUBLISH_I.tex').read_text(); old=(R/'source/S6_SERIES_GRIND_I.tex').read_text()
def block(t,lab):
 k=t.index('\\label{'+lab+'}');a=t.rfind('\\begin{proposition}',0,k);b=t.index('\\end{proof}',k)+len('\\end{proof}');return t[a:b]
a=block(s,'inv:A1.3');g=block(s,'inv:A2.4')
lemma=r'''\begin{lemma}[Residues and the kernel of the logarithmic connecting map]
\hypertarget{tag-S6_NEW_RESIDUE_TAG}{}\label{pub:I:residue-kernel-rank}
\StatementRecord{pub:I:residue-kernel-rank}{proved}{S6_NEW_RESIDUE_TAG}{\SeriesRef{inv:A1.0}, \SeriesRef{inv:A1.1}, \SeriesRef{inv:A1.2}, \SeriesRef{inv:A2.1}}
For every admissible parameter, the logarithmic connecting map
$\kappa_1:R^1f_*\mathcal E\to\mathcal L\otimes R^2f_*\OO=\OO$
is surjective. Put
$\mathcal K=\ker\kappa_1$ and
$r=\operatorname{rank}H^0(\kappa_1)$. The residue maps give
\[
f_*\Omega_X^1=\Omega_B^1,\qquad
R^1f_*\Omega_X^1=\mathcal K,\qquad
R^2f_*\Omega_X^1=R^2f_*\mathcal E.
\]
Thus the first and third bundles are isomorphic to $\OO(-2)$ and
$\OO\oplus\OO(-1)$, respectively; the latter splitting is \cref{inv:A1.2}.
Moreover,
\[
h^0(\mathcal K)=2-r,\qquad h^1(\mathcal K)=1-r,\qquad
h^{1,2}=2-r,\qquad h^{1,1}=3-r.
\]
\end{lemma}
\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item Let $d_{ij}(s)$ be the cover Kodaira--Spencer coefficients in the
eigenframes of \cref{inv:A2.1} after removing $ds$.
The invariant coarse matrix and its cup-product row have the forms
\[
[\kappa_0]=\begin{pmatrix}A&t_jB\\C&D_0\end{pmatrix},\qquad
[\kappa_1]=(-C,A,-D_0,B),
\]
in the ordered basis
$e_0b_0,s^ae_0b_1,s^{m-a}e_1b_0,e_1b_1$. Specifically
$A=sd_{00}/m$, $B=s^{1-a}d_{01}/m$,
$C=s^{1-a}d_{10}/m$, $D_0=s^{m+1-2a}d_{11}/m$.
These are holomorphic invariant functions; the row follows by
wedging the connecting class with $b_0,b_1$.
If the row had no unit at a finite point, every entry would vanish
modulo $t_j$ and $\det\kappa_0$ would vanish to order at least two,
contradicting \cref{inv:A2.1}. Away from the finite points, including
the cusp, $\kappa_0$ is invertible, which gives a unit in the
cup-product row. Thus $\kappa_1$ is surjective.

\item By \cref{inv:A2.1},
$\coker\kappa_0=\C_{p_1}\oplus\C_{p_2}$.
The logarithmic conormal sequence and \cref{inv:A1.2} give
\[
f_*\mathcal A=\OO(1),\quad
0\to T\to R^1f_*\mathcal A\to\mathcal K\to0,\quad
R^2f_*\mathcal A=\OO\oplus\OO(-1),\qquad
T=\C_{p_1}\oplus\C_{p_2}.
\]
Let $\nu:\widetilde D=\mathrm{dP}_6\sqcup S_1\sqcup S_2\to D$
be normalization. The local bases in \cref{inv:A1.1} give the exact
residue sequence
\[
0\to\Omega_X^1\to\mathcal A\to\nu_*\OO_{\widetilde D}\to0.
\]
Its three residue direct images are
$\C_{p_0}\oplus\C_{p_1}\oplus\C_{p_2}$,
$\C_{p_1}\oplus\C_{p_2}$, and zero: the normalization of $W$ is
rational, and a bielliptic surface has
$(h^0,h^1,h^2)(\OO)=(1,1,0)$.
In degree zero the map from $\OO(1)$ is local evaluation with the
nonzero multipliers $1,3,4$. Its kernel is $\OO(-2)$.
Under the base logarithmic inclusion this kernel is $\Omega_B^1$,
and its map to $f_*\Omega_X^1$ is pullback.

\item At $p_j$, in the invariant frame $(b_0,s^ab_1)$ of $G$, residue
of $(dt_j/t_j)(x b_0+y s^ab_1)$ in $H^1(S_j,\OO)$ is
$m_jx[b_0]$. The residue factors through the base logarithmic line
on the covering chart. Naturality of the connecting map gives
$\operatorname{res}_1\kappa_0=0$.
The determinant of $\kappa_0$ has a simple zero, so its reduction
has rank one, and its image is exactly the one-dimensional kernel
$\C s^ab_1$ of this residue. Hence
$\coker\kappa_0\to H^1(S_j,\OO)$ is an isomorphism.
Both torsion summands cancel, giving the stated canonical
identifications of $R^1f_*\Omega_X^1$ and $R^2f_*\Omega_X^1$.

\item The long exact cohomology sequence of
\[
0\to\mathcal K\to\OO^2\oplus\OO(-1)^2
 \xrightarrow{\kappa_1}\OO\to0
\]
gives $h^0(\mathcal K)=2-r$ and $h^1(\mathcal K)=1-r$.
Leray on the curve $B$ and the preceding direct images then give
\[
h^{1,2}=h^1(\mathcal K)+h^0(\OO\oplus\OO(-1))=2-r,
\qquad
h^{1,1}=h^1(\OO(-2))+h^0(\mathcal K)=3-r.
\]
\end{enumerate}
\end{proof}'''
absproof=r'''\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item By \cref{pub:I:residue-kernel-rank}, the first-column direct
images are $\OO(-2)$, $\mathcal K=\ker\kappa_1$, and
$\OO\oplus\OO(-1)$. By \cref{inv:A2.4}, the global map
$H^0(\kappa_1)$ has rank one. Hence the bundle map
$\OO^2\oplus\OO(-1)^2\to\OO$ has a nonzero constant component
on a trivial summand. Eliminating all other components by bundle
automorphisms gives $\mathcal K=\OO\oplus\OO(-1)^2$.

\item Finally $\Omega_X^2=(\Omega_X^1)^\vee\otimes K_X$. Relative
duality, with the locally free direct images now established, gives
\[
R^qf_*\Omega_X^2
=\bigl(R^{2-q}f_*\Omega_X^1\bigr)^\vee\otimes K_B.
\]
Substitution of $K_B=\OO(-2)$ gives every entry of the second column.
\end{enumerate}
\end{proof}'''
newa=a[:a.index('\\begin{proof}')]+absproof
newa=newa.replace(r'\SeriesRef{inv:A2.1}, \SeriesRef{inv:A2.2}, \SeriesRef{inv:A2.4}, \SeriesRef{inv:A1.1}',r'\SeriesRef{pub:I:residue-kernel-rank}, \SeriesRef{inv:A2.4}')
gproof=g[g.index('\\begin{proof}'):]
first_end=gproof.index('\\item The lift $h$')
second=gproof[first_end:]
endold=r'''zero.  For the global rank $r$, the long exact cohomology sequence of
$0\to\mathcal K\to\OO^2\oplus\OO(-1)^2\to\OO\to0$
gives $h^0(\mathcal K)=2-r$ and $h^1(\mathcal K)=1-r$.
The residue calculation in \cref{inv:A1.3} and Leray give
$h^{1,2}=2-r$ and $h^{1,1}=3-r$, as stated.'''
assert endold in second
second=second.replace(endold,r'''zero. The Hodge-number formulas follow from
\cref{pub:I:residue-kernel-rank}, and the nonzero scalar above gives
$r=1$.''')
second=second.replace('\\item The lift $h$ exists',r'''\item Sheaf surjectivity is proved in
\cref{pub:I:residue-kernel-rank}. The lift $h$ exists''')
second=second.replace('the four\nexplicit invariant generators above','the four\nexplicit invariant generators of \\cref{pub:I:residue-kernel-rank}')
newg=g[:g.index('\\begin{proof}')]+r'''\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
'''+second
newg=newg.replace(r'\SeriesRef{inv:A2.1}, \SeriesRef{inv:A1.3}',r'\SeriesRef{pub:I:residue-kernel-rank}, \SeriesRef{inv:A2.1}, \SeriesRef{inv:A2.2}')
# All original statement text, including aliases and mathematical clauses, is preserved;
# only the fourth (dependency) StatementRecord argument changes.
def stmt(t):
 t=t[:t.index('\\begin{proof}')]
 return re.sub(r'\\StatementRecord[^\n]*\n','',t)
assert stmt(a)==stmt(newa)
assert stmt(g)==stmt(newg)
assert r'\label{pub:I:residue-kernel-rank}' not in s
combined=lemma+'\n\n'+newg+'\n\n\\subsection{Absolute cotangent direct images}\n\n'+newa
patches=[{'id':'I-RES-01','action':'Remove this complete absolute-table block for relocation after the global scalar result','old':a,'new':''},{'id':'I-RES-02','action':'Insert common residue lemma, preserve scalar statement with supplying proof, then relocate absolute table with kernel-splitting/duality proof','old':g,'new':combined}]
for x in patches: assert s.count(x['old'])==1
meta={'source_path':str(R/'work/S6_SERIES_PUBLISH_I.tex'),'source_sha256':hashlib.sha256(s.encode()).hexdigest(),'method':'EXPOSED complete original/current proof reread and extraction comparison; no independent or computational credit.','new_label':'pub:I:residue-kernel-rank','tag_placeholder':'S6_NEW_RESIDUE_TAG','guards':patches}
(O/'S6_SERIES_PUBLISH_I_residue_order_guards.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
archive={'original_source_path':str(R/'source/S6_SERIES_GRIND_I.tex'),'original_source_sha256':hashlib.sha256(old.encode()).hexdigest(),'current_source_sha256':meta['source_sha256'],'exposure':'All target printed proofs were already exposed. Full original/current source blocks and the proposed extracted proof were read for this editorial comparison.','blocks':{lab:{'original':block(old,lab),'current':cur,'replacement':new} for lab,cur,new in [('inv:A1.3',a,newa),('inv:A2.4',g,newg)]},'new_common_lemma':lemma,'moved_spans':[{'from':'inv:A2.4 proof Step 1, complete','to':'pub:I:residue-kernel-rank proof Step 1','content':'Invariant κ0 matrix, cup row, local determinant order and global sheaf surjectivity.'},{'from':'inv:A1.3 proof Step 1 after the opening dependency claim, plus Step 2 through the torsion cancellation','to':'pub:I:residue-kernel-rank proof Steps 2–3','content':'Log conormal sequence, residue direct images, evaluation weights 1,3,4, local residue map and exact torsion cancellation.'},{'from':'inv:A2.4 proof Step 3 final cohomology paragraph','to':'pub:I:residue-kernel-rank proof Step 4','content':'Rank-r kernel cohomology and Leray Hodge formulas, now with explicit additions.'},{'from':'inv:A1.3 whole block before finite-coordinate subsection','to':'After inv:A2.4 and the new common lemma','content':'Original complete statement and all labels/tags unchanged; proof retains only rank-one splitting and duality.'}],'order_after':['inv:A1.0','inv:A1.1','inv:A1.2','I:def:finite-coordinates','inv:A2.3','inv:A2.1','inv:A2.2','pub:I:residue-kernel-rank','inv:A2.4','inv:A1.3','inv:A3.1'],'dependency_edges':[['inv:A1.1','pub:I:residue-kernel-rank'],['inv:A1.2','pub:I:residue-kernel-rank'],['inv:A2.1','pub:I:residue-kernel-rank'],['pub:I:residue-kernel-rank','inv:A2.4'],['inv:A2.2','inv:A2.4'],['pub:I:residue-kernel-rank','inv:A1.3'],['inv:A2.4','inv:A1.3'],['inv:A1.3','inv:A3.1']]}
(O/'S6_SERIES_PUBLISH_I_residue_order_archive.json').write_text(json.dumps(archive,ensure_ascii=False,indent=2)+'\n')
(O/'S6_SERIES_PUBLISH_I_residue_order_replacement.tex').write_text(combined+'\n')
preview=s
for p in patches:preview=preview.replace(p['old'],p['new'],1)
# Guard-only preview is never the root TeX.
(O/'S6_SERIES_PUBLISH_I_residue_order_preview.tex').write_text(preview)
print(json.dumps({'guards':len(patches),'source_sha256':meta['source_sha256'],'statement_preservation':'exact after removing dependency-only StatementRecord lines','new_label_count':preview.count(r'\label{pub:I:residue-kernel-rank}')},indent=2))
