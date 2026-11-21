"""Prepare guarded analytic-section edits; never write the root TeX."""
from pathlib import Path
import re,json,hashlib,datetime
B=Path(__file__).parent
ROOT=Path('/workspace/scratch/653608133b22')
P=ROOT/'work/S6_SERIES_PUBLISH_I.tex'
original=P.read_text()
s=original
guards=[];removed=[]

def patch(old,new,reason,ids=()):
    global s
    assert s.count(old)==1,(reason,s.count(old),old[:120])
    guards.append(dict(id=f'IA-A-{len(guards)+1:02}',old=old,new=new,
                       expected_count=1,reason=reason,statement_ids=list(ids)))
    s=s.replace(old,new,1)

def block(label,proof=True):
    i=s.index(r'\label{'+label+'}')
    starts=[(s.rfind(r'\begin{'+env+'}',0,i),env)for env in
            ['proposition','theorem','lemma','cited','remark','corollary']]
    a,env=max(starts)
    assert a>=0
    z=s.index(r'\end{'+env+'}',i)+len(r'\end{'+env+'}')
    if proof:
        p=s.find(r'\begin{proof}',z)
        nextst=re.search(r'\\begin\{(?:proposition|theorem|lemma|cited|remark|corollary)\}',s[z:])
        if p>=0 and (not nextst or p<z+nextst.start()):
            z=s.index(r'\end{proof}',p)+len(r'\end{proof}')
    return s[a:z]

def preserve(name,old,reason):
    removed.append(dict(name=name,reason=reason,original=old,
                        sha256=hashlib.sha256(old.encode()).hexdigest()))

# One notation and the exact period formula. The convention definition is
# owned by the parent and is cited rather than changed.
old=r'''\section{The normalized periods, quantitative bounds, and the boundary}\hypertarget{tag-01PK}{}\label{fam:section:C}'''
patch(old,r'''\section{Normalized periods and the real determinant}\hypertarget{tag-01PK}{}\label{fam:section:C}''','Descriptive section title.')
patch(r'''\subsection{A theta expression for the missing period}''',
      r'''\subsection{The normalized theta period}''','Remove problem-history framing.')
patch(r'''\begin{proposition}\hypertarget{tag-01QH}{}''',
      r'''\begin{proposition}[The normalized theta period]\hypertarget{tag-01QH}{}''',
      'Mathematical title.',('fam:src:C.1.1',))

# Retain the unique finite-period difference as an exact corollary after
# the exact special values. The old decimals/independent algorithms remain
# in the comparison records.
oldnum=block('fam:src:C.1.2')
preserve('fam_C1_2_decimal_evaluations',oldnum,'Independent numerical verification and its unique kappa bound.')
patch(oldnum,'','Move the unique finite-period difference after its exact-value input; archive duplicate decimal verification.',('fam:src:C.1.2',))
oldcross=block('ari:C.1.3')
preserve('ari_C1_3_decimal_evaluations',oldcross,'Duplicate numerical checks of exact special values.')
newcross=r'''\begin{corollary}[Difference of the finite invariant periods]
\hypertarget{tag-01QI}{}\label{fam:src:C.1.2}\label{fam:st:C.1.2}
\hypertarget{tag-000K}{}\label{ari:C.1.3}
\StatementRecord{fam:src:C.1.2}{proved}{01QI}{\cref{ari:C.1.2}}
Put $\kappa_1^{\rm part}=\beta^{\rm part}(z_1)+2\mu(z_1)$ and
$\kappa_2^{\rm part}=\beta^{\rm part}(z_2)+3\mu(z_2)$. Then
\[
 \kappa_1^{\rm part}-\kappa_2^{\rm part}
   =-1-\frac{3i}{2\pi}\log\frac43,
 \qquad
 -\frac15<\Im(\kappa_1^{\rm part}-\kappa_2^{\rm part})
             <-\frac1{10}.
\]
\end{corollary}
\begin{proof}
Substitution of the exact values in \cref{ari:C.1.2} gives
$\kappa_1^{\rm part}=\frac12-\frac{3i}{2\pi}\log48$ and
$\kappa_2^{\rm part}=\frac32-\frac{3i}{\pi}\log6$.
Their difference is the displayed expression.
Integrating $1/(1+x)$ on $0\le x\le1/3$ gives
$1/4<\log(4/3)<1/3$; together with $3<\pi<15/4$,
these inequalities give the stated strict bounds.
\end{proof}'''
patch(oldcross,newcross,'Consolidate duplicate decimal assertions; retain and prove the unique finite-period separation exactly.',('fam:src:C.1.2','ari:C.1.3'))

# The norm identity is needed before the maximum proof. The coarse and
# duplicate local estimates are archived; their conclusions follow from
# the stronger exact theorem and local lemma retained below.
oldcoarse=block('fam:src:C.2.1')
preserve('fam_C2_1_coarse_bound',oldcoarse,'Coarse global estimates superseded by exact maximum; determinant/cusp content retained.')
newcoarse=r'''\begin{proposition}[The norm and the real determinant]
\hypertarget{tag-01QJ}{}\label{fam:src:C.2.1}\label{fam:st:C.2.1}
\StatementRecord{fam:src:C.2.1}{proved}{01QJ}{\cref{fam:src:C.1.1,I:def:theta-height,I:period-determinant}}
For the conventions of \cref{I:def:theta-height,I:def:family-parameter},
\begin{equation}\hypertarget{tag-01P6}{}\label{fam:eq:cd-norm}
 D_{\rm part}=\frac6\pi\log\frac{N(\mu,\tau)}{2\sqrt3},
 \qquad \mathcal N(v,\tau)=N(v,\tau).
\end{equation}
The norm is preserved by integral translations and sign change of $v$,
and by the lattice isomorphism
\[
 [v]\longmapsto[v/(c\tau+d)],\qquad
 \tau\longmapsto\frac{a\tau+b}{c\tau+d},
 \qquad \begin{pmatrix}a&b\\c&d\end{pmatrix}\in\mathrm{SL}_2(\mathbb Z).
\]
At the cusp, $D_{\rm part}=-\Im\tau+o(1)$.
\end{proposition}
\begin{proof}
The imaginary part of \eqref{fam:eq:cd-beta} is
$(6/\pi)\log|\vartheta_1(\mu,\tau)/(2\sqrt3\eta_D(\tau))|$.
Subtracting $6(\Im\mu)^2/\Im\tau$ gives \eqref{fam:eq:cd-norm}.
Thus the two notations $\mathcal N$ and $N$ denote the identical
function of \cref{I:def:theta-height}.
The theta transformation formulas in \cref{fam:src:C.1.1} have
exactly the exponential moduli cancelled by this Gaussian; the
theta and eta square-root factors cancel in their quotient.
The displayed lattice map also sends $\wp_\tau(v)=0$ to the
zero equation on the transformed lattice, since $\wp$ has weight two.
Finally $\beta^{\rm part}+\tau\to0$ and the bounded cusp limit of
$\mu$ give the stated asymptotic directly from the real determinant.
\end{proof}'''
patch(oldcoarse,newcoarse,'Retain exact norm transport and cusp calculation; remove superseded coarse bounds and program bookkeeping.',('fam:src:C.2.1',))
patch(r'''\subsection{Bounds for the sharp parameter disc}''',
      r'''\subsection{The invariant norm}''','Match the retained content.')
oldlocal=block('fam:src:C.2.2')
preserve('fam_C2_2_local_and_grid',oldlocal,'Duplicate local proof and exploratory grid moved to records.')
patch(oldlocal,'','Use the stronger local theorem once; retain its old anchors on that theorem.',('fam:src:C.2.2',))
localhead=r'''\begin{proposition}[the local maximum]\hypertarget{tag-000M}{}\label{ari:C.8.2}'''
# The exact title in the current source may differ; derive only the header.
i=s.index(r'\label{ari:C.8.2}')
a=s.rfind(r'\begin{',0,i);z=i+len(r'\label{ari:C.8.2}')
localhead=s[a:z]
patch(localhead,localhead+r'''\hypertarget{tag-01QK}{}\label{fam:src:C.2.2}\label{fam:st:C.2.2}''',
      'Preserve the old local-maximum anchors on the stronger single statement.',('ari:C.8.2','fam:src:C.2.2'))

# Relocate the exact maximum statement to its retained division-ladder proof.
oldmax=block('fam:src:C.2.3')
preserve('fam_C2_3_interval_proof',oldmax,'Full older interval proof, tails and cover records retained outside the body.')
patch(oldmax,'','Relocate the exact maximum and keep the division-ladder proof as its single body proof.',('fam:src:C.2.3',))
maxstmt=r'''\begin{theorem}[Exact norm maximum and parameter discs]
\hypertarget{tag-01QL}{}\label{fam:src:C.2.3}\label{fam:st:C.2.3}
\label{ari:C.8.5}\label{push:src:E.4.3}
\StatementRecord{fam:src:C.2.3}{proved}{01QL}{\cref{ari:C.8.1,ari:C.8.2,ari:C.8.3,ari:C.8.4,fam:eq:cd-norm,I:period-determinant}}
At every zero of $\wp_\tau$,
\[
 N\le\sqrt2,
\]
with equality precisely in the modular orbit of $\tau=i$.
For the cusp normalization $\beta^{\rm part}+\tau\to0$ this gives
\[
 M=-\frac3\pi\log6,\qquad
 \operatorname*{arg\,max}_{B\setminus\{p_0\}}D_{\rm part}=\{1\}.
\]
The real period determinant is nonzero throughout the base exactly
when $\Im c<-M$. Consequently the parameter domains are
\[
 0<|w|<216,\qquad 0<|u_{\rm Engel}|<46656.
\]
Changing the reference to $u_{\lambda_0}=\lambda_0w^2$ multiplies
the latter radius by $|\lambda_0|$.
\end{theorem}

\begin{proof}'''
oldbegin=r'''\begin{proof}[Division-ladder proof of Theorem~\ref{fam:st:C.2.3}]'''
patch(oldbegin,maxstmt,'Place the exact maximum immediately before its sole retained proof.',('fam:src:C.2.3',))
oldend=r'''modulus. The only equality occurs at $t=1$.
\end{enumerate}
\end{proof}'''
newend=r'''modulus. The only equality occurs at $t=1$.

\item The norm identity \eqref{fam:eq:cd-norm} gives
$M=(6/\pi)\log(\sqrt2/(2\sqrt3))=-3\log6/\pi$.
The cusp asymptotic in \cref{fam:src:C.2.1} and continuity show
that $D_{\rm part}+\Im c$ has a zero for $\Im c\ge-M$:
use the maximum at $t=1$ and a path to the cusp.
For $\Im c<-M$ it is strictly negative everywhere.
By \cref{I:period-determinant}, this is exactly nonvanishing of
the real period determinant throughout the base.
Since $|w|=e^{\pi\Im c}$ and $u_{\rm Engel}=w^2$,
the radii are $e^{-\pi M}=6^3$ and $e^{-2\pi M}=6^6$.
The reference change is the displayed multiplication by $\lambda_0$.
\end{enumerate}
\end{proof}'''
patch(oldend,newend,'Retain the original admissibility/path argument and exact radius calculation after the maximum.',('fam:src:C.2.3','fam:src:C.2.1'))

# The second independent interval section adds verification, not a second
# body proof. Its original mathematics and all diagnostic data are saved.
start=s.index(r'\subsection{An independent interval certificate}')
end=s.index(r'\clearpage\appendix',start)
oldinterval=s[start:end]
preserve('push_E4_independent_interval',oldinterval,'Independent interval proof and duplicate local argument moved to verification records.')
newinterval=r'''\begin{remark}[Independent interval verification]
\hypertarget{tag-034N}{}\label{push:section:E.4}\label{sec:e4}
\hypertarget{tag-033L}{}\label{push:src:E.4.1}
\hypertarget{tag-033M}{}\label{push:src:E.4.2}
An independent proof of \cref{fam:src:C.2.3} uses contraction
enclosures for the zeros of $\wp$, explicit theta and eta tails,
and an exact cover of the compact modular region. That proof and
its separate local argument are retained in the verification records.
\end{remark}

'''
patch(oldinterval,newinterval,'One proof in the body; preserve every interval-proof anchor in a single remark.',('push:src:E.4.1','push:src:E.4.2'))

# Remove implementation narration around the retained analytic proof.
old=r'''Theorems~\ref{fam:src:C.2.3} and \cref{push:src:E.4.1}, \cref{push:src:E.4.2} establish this inequality by
computer-assisted proofs. Statements \ref{ari:C.8.1}--\ref{ari:C.8.5} give another
proof with a three-step division ladder and the explicit radius
$1/50$ in the $\tau$-plane. The programs
\path{code/C_ladder_estimates.py} and
\path{code/C_local_analytic_bounds.py} record numerical diagnostics
of the constants; the proof uses the displayed rational estimates
and their series remainder bounds alone.'''
patch(old,'','Delete repeated proof-history summary; the retained argument is already complete.',('fam:src:C.2.3',))

out=dict(source_path=str(P),source_sha256=hashlib.sha256(original.encode()).hexdigest(),
         generated_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
         guards=guards)
(B/'S6_SERIES_PUBLISH_I_editorial_batch_a_guards.json').write_text(json.dumps(out,indent=2)+'\n')
(B/'S6_SERIES_PUBLISH_I_editorial_batch_a_removed.json').write_text(json.dumps(removed,indent=2)+'\n')
(B/'S6_SERIES_PUBLISH_I_editorial_batch_a_preview.tex').write_text(s)
print(json.dumps({'guards':len(guards),'removed_blocks':len(removed),
 'source_sha256':out['source_sha256'],'preview_sha256':hashlib.sha256(s.encode()).hexdigest()},indent=2))
