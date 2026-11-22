from pathlib import Path
import json, datetime
from S6_SERIES_PUBLISH_editing import Editor, block

r=Path(__file__).resolve().parents[1]
ed=Editor('I')
p51=block(ed.text,'night:P5.1')
p52=block(ed.text,'night:P5.2')
start=ed.text.index(r'\subsection{Credited re-derivations: local charts and coherent direct images}')
end=ed.text.index(p51,start)
oldsetup=ed.text[start:end]
setup=r'''\subsection{Ordinary tangent sheaves and the conductor}
\begin{definition}[The double locus and its tangent quotient]
\hypertarget{tag-PI12}{}\label{I:ordinary-tangent-sheaves}
For the $(3,4)$ family, let
$D_{\mathrm{dbl}}=(\operatorname{Sing}W)_{\mathrm{red}}$.
It consists of three rational curves joining the two triple points.
Put
\[
 L=f^*\mathcal O_B(-1)\otimes\mathcal O_X(2S_1+S_2),\qquad
 F=\mathcal O_X(S_1+S_2),\qquad
 \mathcal V=\ker(df),\qquad
 J=\mathcal I_{D_{\mathrm{dbl}}}\otimes F.
\]
The root conventions give
$\rho^*\mathcal O_B(1)=\mathcal O_{\mathcal B}(12)$,
$\mathcal O_X(S_1)=\bar f^*\mathcal O_{\mathcal B}(4)$ and
$\mathcal O_X(S_2)=\bar f^*\mathcal O_{\mathcal B}(3)$.
The tensor maps on their canonical divisor sections therefore give
\[
 L=\bar f^*\widehat L,\quad \widehat L=\mathcal O_{\mathcal B}(-1),
 \qquad F=\bar f^*\widehat F,\quad
 \widehat F=\mathcal O_{\mathcal B}(7).
\]
The weights are $-12+2\cdot4+3=-1$ and $4+3=7$.
The vertical root bundle is $E$ of \cref{inv:D1.2}.
\end{definition}

'''
head=p51[:p51.index(r'\StatementRecord')]
head=head.replace(r'\begin{theorem}',r'\begin{theorem}[The ordinary tangent sequence]')
n51=head+r'''\StatementRecord{night:P5.1}{proved}{02YM}{\cref{I:ordinary-tangent-sheaves,inv:D1.2}}
The sheaf $\mathcal V$ is locally free of rank two and equals
$\bar f^*E$. The differential induces an exact sequence
\begin{equation}\hypertarget{tag-01OK}{}\label{eq:P5tangent}
 0\longrightarrow\mathcal V\longrightarrow T_X
 \longrightarrow J\longrightarrow0.
\end{equation}
\end{theorem}
\begin{proof}
On a finite root chart $t=s^m$, the differential has image
$(s^{m-1})f^*T_B$. The free cyclic quotient makes the root chart
\'etale over $X$, so the orders along $S_1,S_2$ are $2,3$.
At a cusp double point $q=xy$, its image is $(x,y)$; at a triple
point $q=xyz$, its image is $(xy,xz,yz)$, the reduced ideal of the
three axes. At a smooth point of $W$, it is surjective.
Thus the global image is
\[
 \mathcal I_{D_{\mathrm{dbl}}}\otimes f^*T_B
 \otimes\mathcal O_X(-2S_1-3S_2)=J.
\]
Here $t(t-1)\partial_t$ trivializes $T_B(-p_1-p_2)$,
and $f^*(p_1)=3S_1$, $f^*(p_2)=4S_2$ identify the remaining
line factor with $\mathcal O_X(S_1+S_2)$.
The kernel and its finite, toric and period-transition maps were
computed in \cref{inv:D1.2}; those evaluation maps identify it
with $\bar f^*E$, including at the double and triple points.
\end{proof}
'''
head=p52[:p52.index(r'\StatementRecord')]
head=head.replace(r'\begin{theorem}',r'\begin{theorem}[The ordinary direct images]')
table_start=p52.index(r'\[',p52.index('On $B$, the direct images'))
table_end=p52.index(r'\]',table_start)+2
table=p52[table_start:table_end].replace('\n E&','\n \\mathcal V&')
assert '\\mathcal V&' in table
tail_start=p52.index(r'\item For the last row')
tail_end=p52.index(r'\end{enumerate}',tail_start)
tail=p52[tail_start:tail_end]
tail=tail.replace('$D$','$D_{\\mathrm{dbl}}$').replace('\\mathcal O_D','\\mathcal O_{D_{\\mathrm{dbl}}}')
tail=tail.replace('H^1(D,','H^1(D_{\\mathrm{dbl}},').replace('H^2(D,','H^2(D_{\\mathrm{dbl}},')
tail=tail.replace('F|_D','F|_{D_{\\mathrm{dbl}}}')
n52=head+r'''\StatementRecord{night:P5.2}{proved}{02YN}{\cref{inv:D1.1,inv:D1.2,push:src:E.3.1,night:P5.1}}
For the sheaves of \cref{I:ordinary-tangent-sheaves}, the coarse
direct images are
'''+table+r'''
\end{theorem}
\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item The root splitting and structure-sheaf direct images are
\cref{inv:D1.2,push:src:E.3.1}; in the standard data these are also
\cite[Proposition~6.6, pp.~77--78; Lemma~6.7, p.~78;
Proposition~6.10, pp.~79--80]{DuEtAl2026v1}.
The determinant line in these conventions is
\begin{equation}\hypertarget{tag-01OG}{}\label{eq:P5L}
 \det E=\widehat L
 =\rho^*\mathcal O_B(-1)\otimes
   \mathcal O_{\mathcal B}(2p_1/3+p_2/4)
 =\mathcal O_{\mathcal B}(-1).
\end{equation}
The equality is the tensor product of the divisor-section maps
in \cref{I:ordinary-tangent-sheaves}; its degree is $-12+8+3$.
For integers $d,a,b$, the invariant root-line formula is
\begin{equation}\hypertarget{tag-01OI}{}\label{eq:P5floor}
 \rho_*\bigl(\rho^*\mathcal O_B(d)\otimes
 \mathcal O_{\mathcal B}(ap_1/3+bp_2/4)\bigr)
 =\mathcal O_B\bigl(d+\lfloor a/3\rfloor+\lfloor b/4\rfloor\bigr).
\end{equation}
Indeed writing $a=3q+r$, $b=4q'+r'$ with
$0\leq r<3$, $0\leq r'<4$ separates the coarse divisor
$(d+q+q')$ from the two root characters. This is the same
invariant-section map as \cref{inv:D1.1}, and applies to all
integer $a,b$.

\item For a root line bundle $A$, projection and exact finite
invariants give
\[
 R^qf_*\bar f^*A=\rho_*\bigl(A\otimes
              \bigwedge^q(\mathcal O\oplus\widehat L)\bigr).
\]
For $A=\mathcal O,\widehat L,\widehat F$, and for
$E=\mathcal O\oplus\widehat L$, the formula
\eqref{eq:P5floor} gives the first four rows. The root-to-coarse
map, including the full scheme fibres, is \cref{I:root-coarse-comparison}.

'''+tail+r'''\end{enumerate}
\end{proof}
'''
ed.replace(oldsetup,setup,'D13','Number the ordinary sheaves, identify each root line by its canonical divisor-section tensor map, and name the reduced double locus distinctly from the full logarithmic divisor.','I:ordinary-tangent-sheaves')
ed.replace(p51,n51,'D12','Use the shared kernel proof and retain the unique image-ideal calculation and exact ordinary tangent quotient, including its global divisor map.','night:P5.1')
ed.replace(p52,n52,'D12','Retain the complete five-row direct-image result and conductor proof, replacing repeated root/discriminant/cusp proofs by the already proved common inputs with explicit root-line transport.','night:P5.2')
for label in ['night:P5.5','night:P5.6']:
 old=block(ed.text,label)
 new=old.replace(r'\widehat B',r'\mathcal B')
 new=new.replace(r'\longrightarrow V\longrightarrow',r'\longrightarrow E\longrightarrow')
 new=new.replace(r'\mathcal B,V',r'\mathcal B,E').replace(r'\pi_*V',r'\rho_*E')
 assert old!=new
 ed.replace(old,new,'D20','Use the same root stack and translation bundle notation: the canonical root-section construction gives h=bar f and pi=rho, and its translation Lie bundle is exactly E; the former sheaf ker(df) is now mathcal V. No map or class changes.',label)
ed.save()
(r/'records/S6_SERIES_PUBLISH_I_ordinary_direct_images_removed.json').write_text(json.dumps({
 'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'setup':oldsetup,'P51':p51,'P52':p52,
 'comparison':'The complete old proofs were read. Shared local kernels, cyclic characters, base change, root degrees and cusp cup complex are proved once in the earlier foundations. The five direct-image rows, conductor graph, zero boundary map and evaluation kernels remain here. No independent reproof event is added.'
},indent=2)+'\n')
