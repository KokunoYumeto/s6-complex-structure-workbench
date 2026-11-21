"""Number the assigned analytic setups; preserve the model tables exactly."""
from pathlib import Path
import json,hashlib,datetime,re
B=Path(__file__).parent;source=Path('/workspace/scratch/653608133b22/work/S6_SERIES_PUBLISH_I.tex')
original=source.read_text();s=original;guards=[];removed=[]
def patch(old,new,reason,ids=()):
 global s
 assert s.count(old)==1,(reason,s.count(old),old[:100])
 guards.append(dict(id=f'IA-SETUP-{len(guards)+1:02}',old=old,new=new,expected_count=1,reason=reason,statement_ids=list(ids)))
 s=s.replace(old,new,1)
def block(start,end):
 a=s.index(start);b=s.index(end,a);return s[a:b]
for n in range(21,29):assert f'tag-IA{n}' not in s

old=block('We use the odd Jacobi function',r'\begin{proposition}[The normalized theta period]')
new=r'''\begin{definition}[Theta functions and the cusp branch]
\hypertarget{tag-IA21}{}\label{I:theta-series-cusp-branch}
The odd Jacobi function and the Dedekind function are
\[
 \begin{aligned}
 \vartheta_1(v,\tau)&=2\sum_{n\geq0}(-1)^n
 e^{\pi i\tau(n+1/2)^2}\sin((2n+1)\pi v),\\
 \eta_D(\tau)=\eta(\tau)&=
 e^{\pi i\tau/12}\prod_{n\geq1}(1-e^{2\pi in\tau}).
 \end{aligned}
\]
Choose the cusp lift reached from $\tau=iT$, $T>1$, on which
$\mu=1/2-iy(T)$ and $0<y(T)<T/2$. Put
$a=5+2\sqrt6$ and $\rho=e^{\pi i/3}$.
\end{definition}

'''
patch(old,new,'Number the existing theta/eta series and cusp-branch setup; make eta_D=eta explicit.',('fam:src:C.1.1',))

old=block(r'We write $\rho=(1+i\sqrt3)/2$',r'\begin{proposition}')
new=r'''\begin{definition}[The logarithmic norm on a lattice]
\hypertarget{tag-IA22}{}\label{I:logarithmic-lattice-norm}
Write $\rho=(1+i\sqrt3)/2$ and $T=\operatorname{Im}\tau$.
For the norm of \cref{I:def:theta-height}, put
\[
 U_\tau(z)=\log N(z,\tau)
 =\log\left|\frac{\vartheta_1(z,\tau)}{\eta(\tau)}\right|
       -\frac{\pi(\operatorname{Im}z)^2}{T}.
\]
The theta variable has periods $1,\tau$; a convention with
first period $\pi$ therefore uses the argument $\pi z$.
For $\Lambda=\omega(\mathbb Z+\tau\mathbb Z)$ and $z\notin\Lambda$
set $U_\Lambda(z)=U_\tau(z/\omega)$.
\end{definition}
\begin{proof}[Well-definedness]
Write $v=z/\omega$. An oriented basis change has
\[
 \tau'=\frac{a\tau+b}{c\tau+d},\qquad
 \omega'=\omega(c\tau+d),\qquad v'=\frac v{c\tau+d},
 \qquad ad-bc=1.
\]
The theta transformations
\cite[Equations~20.7.26 and 20.7.30]{DLMFTheta2026}, with
the first argument multiplied by $\pi$, and the eta law
\cite[Equations~23.18.5--23.18.6]{DLMFTheta2026} give the
two modular generators; the eta translation law also follows
directly from its product. Composition gives
\[
 \log\left|\frac{\vartheta_1(v',\tau')}{\eta(\tau')}\right|
 =\log\left|\frac{\vartheta_1(v,\tau)}{\eta(\tau)}\right|
   -\pi\Im\frac{cv^2}{c\tau+d}.
\]
The identity
\[
 \frac{(\Im v')^2}{\Im\tau'}
 =\frac{(\Im v)^2}{\Im\tau}
     -\Im\frac{cv^2}{c\tau+d}
\]
cancels this term, so $U_{\tau'}(v')=U_\tau(v)$.
This proves independence of the basis of $\Lambda$.
For a homothety $\lambda\ne0$, the same normalized argument gives
$U_{\lambda\Lambda}(\lambda z)=U_\Lambda(z)$.
\end{proof}

'''
patch(old,new,'Number the lattice norm and give the exact basis and homothety maps for the existing invariance assertion.',('ari:C.1.1',))

old=block('We use throughout this subsection the rational model',r'\begin{cited}[Siegel functions and local heights]')
new=r'''\begin{remark}[The arithmetic model in the division identities]
\hypertarget{tag-IA23}{}\label{I:division-model-convention}
Use the model and point of \cref{I:def:theta-height}, written as
\[
 E_t:\quad y^2=x^3+A(t)x+B(t),\qquad
 A=-\tfrac34t^3(t-1),\quad B=\tfrac14t^4(t-1)^2,
 \quad P=(0,t^2(t-1)/2).
\]
Its discriminant is $\Delta_E(t)=27t^8(t-1)^3$.
Under $(x,y)\mapsto(\lambda^2x,\lambda^3y)$ the period lattice
and its logarithm change by $(\Lambda,z)\mapsto
(\lambda^{-1}\Lambda,\lambda^{-1}z)$ for the invariant differential.
The identity in \cref{I:logarithmic-lattice-norm} therefore preserves $N$.
\end{remark}

'''
patch(old,new,'Keep the arithmetic model and replace an unspecified model-change assertion by its exact differential/lattice transport.',('ari:C.4.1',))

old=block('Throughout this section $q=e^{2\\pi i\\tau}$',r'\begin{proposition}[Three uniform bounds on the elliptic norm]')
removed.append({'name':'maximum_setup_original','text':old})
new=r'''\begin{remark}[Modular and arithmetic discriminants]
\hypertarget{tag-IA24}{}\label{I:modular-arithmetic-discriminants}
Use $q=e^{2\pi i\tau}$, $T=\Im\tau$, $\Delta_0$ and $t$
from \cref{I:def:theta-height}. Thus
$t=E_4^3/(1728\Delta_0)$ and
$t-1=E_6^2/(1728\Delta_0)$.
On the smooth rational model $t\ne0,1$, choose $\lambda$ with
\[
 \lambda^2=-\frac{t(t-1)g_2}{3g_3}.
\]
The exact uniformization is
$(x,y)=(\lambda^2\wp(z),\lambda^3\wp'(z)/2)$, where
$\wp$ has lattice $\mathbb Z+\tau\mathbb Z$.
Choose the sign of $\lambda$ so that the marked zero $\mu$
maps to $P_t$.
Indeed $g_2^3/g_3^2=27t/(t-1)$ gives
\[
 A=-\lambda^4g_2/4,\qquad B=-\lambda^6g_3/4,
 \qquad \Delta_E=\lambda^{12}(2\pi)^{12}\Delta_0.
\]
The invariant differential pulls back to $\lambda^{-1}dz$,
so its period lattice is $\lambda^{-1}(\mathbb Z+\tau\mathbb Z)$.
The division identity \eqref{ari:eq:cs-division} and the
modular invariance in \cref{I:logarithmic-lattice-norm}
will be used below.
\end{remark}

'''
patch(old,new,'Replace the unnumbered modular setup by an exact uniformization/discriminant comparison and remove proof-process narration.',('ari:C.8.1',))

old=r'''We use the arithmetic equation, invariant differential, place weights,
and height normalization of \cref{I:def:theta-height}.
'''
new=r'''\begin{remark}[Arithmetic normalization]
\hypertarget{tag-IA25}{}\label{I:global-height-convention}
The arithmetic equation, invariant differential, place weights,
and height normalization are those of \cref{I:def:theta-height}.
\end{remark}
'''
patch(old,new,'Number the existing convention reminder without defining a second height normalization.')

# Both tables retain every entry and move into the proposition that states them.
table_start=s.index(r'\begingroup\footnotesize\setlength{\tabcolsep}{4pt}',s.index(r'\label{ari:C.6.3}'))
table_end=s.index(r'\endgroup',table_start)+len(r'\endgroup')
tables=s[table_start:table_end]
assert tables.count(r'\begin{longtable}')==2
patch(tables,'','Attach both exact data tables to their existing model proposition.',('ari:C.6.3',))
i=s.index(r'\label{ari:C.6.3}');e=s.index(r'\end{proposition}',i)
end_anchor=s[s.rfind('The constants $A_t$',i,e):e+len(r'\end{proposition}')]
new=end_anchor.replace(r'\end{proposition}',tables.replace(r'\begingroup\footnotesize',r'\begingroup\normalfont\footnotesize')+'\n'+r'\end{proposition}')
patch(end_anchor,new,'Move the unchanged minimal-model and finite-height tables inside the statement before its proof.',('ari:C.6.3',))

old=block('Write $E_i$ for the eleven minimal models',r'\begin{proposition}[Mordell--Weil ranks and primitive sections]')
new=r'''\begin{remark}[The real period and diagonal height pairing]
\hypertarget{tag-IA26}{}\label{I:rank-period-pairing}
'''+old.strip()+r'''
\end{remark}

'''
patch(old,new,'Number the existing real-period/Poincare-bundle pairing convention without changing its factor two.')

old=r'''Use the function $L=\log N$ and the modular coordinate
$t=j/1728$ of \cref{I:def:theta-height}.
'''
new=r'''\begin{remark}[Critical-point coordinates]
\hypertarget{tag-IA27}{}\label{I:critical-point-convention}
Use $L=\log N$ and $t=j/1728$ as in \cref{I:def:theta-height}.
\end{remark}
'''
patch(old,new,'Number the existing critical-point convention.')

old=r'''\subsection{CM theta normalization and further unconditional deductions}

The multiplication law below retains the finite sign character.
Its exact relation to the metric norm is \eqref{ari:eq:ct-Gaussian}.
'''
new=r'''\subsection{CM theta normalization}

\begin{remark}[The theta and metric normalizations]
\hypertarget{tag-IA28}{}\label{I:CM-theta-metric-convention}
The multiplication law in \cref{ari:C.7.6} retains its finite sign
character. Its exact relation to the metric norm is
\eqref{ari:eq:ct-Gaussian}.
\end{remark}
'''
patch(old,new,'Number the existing finite-sign/Gaussian comparison and give the subsection a mathematical title.')

meta={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'source':str(source),'source_sha256':hashlib.sha256(original.encode()).hexdigest(),
 'guards':guards,'scope':'Nine specified setup spans, with the table move in two guards. Main TeX not modified.'}
(B/'S6_SERIES_PUBLISH_I_analytic_setup_guards.json').write_text(json.dumps(meta,indent=2)+'\n')
(B/'S6_SERIES_PUBLISH_I_analytic_setup_preview.tex').write_text(s)
(B/'S6_SERIES_PUBLISH_I_analytic_setup_removed.json').write_text(json.dumps(removed,indent=2)+'\n')
assert set(re.findall(r'\\label\{([^}]+)\}',original))<=set(re.findall(r'\\label\{([^}]+)\}',s))
assert set(re.findall(r'\\hypertarget\{tag-([^}]+)\}',original))<=set(re.findall(r'\\hypertarget\{tag-([^}]+)\}',s))
assert s.count(tables.replace(r'\begingroup\footnotesize',r'\begingroup\normalfont\footnotesize'))==1
print(json.dumps({'guards':len(guards),'new_tags':['IA'+str(n) for n in range(21,29)],'table_entries_unchanged':True,'main_source_modified':False}))
