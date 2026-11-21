"""Critical-point proof presentation; all rational bounds are retained."""
from pathlib import Path
import json,hashlib,datetime
B=Path(__file__).parent
base=B/'S6_SERIES_PUBLISH_I_editorial_batch_d_preview.tex'
original=base.read_text();s=original;guards=[];removed=[]
def patch(old,new,reason,ids=()):
 global s
 assert s.count(old)==1,(reason,s.count(old),old[:150])
 guards.append(dict(id=f'IA-E-{len(guards)+1:02}',old=old,new=new,
 expected_count=1,reason=reason,statement_ids=list(ids)))
 s=s.replace(old,new,1)
def archive(name,text,why):
 removed.append(dict(name=name,reason=why,original=text,
 sha256=hashlib.sha256(text.encode()).hexdigest()))

a=s.index(r'We continue to write $L(t)=\log N')
b=s.index(r'\begin{proposition}[a radial derivative identity]',a)
old=s[a:b]
archive('critical_source_setup',old,'Original external formula, branch discussion and literature-search narrative.')
formula=old[old.index(r'\begin{equation}'):old.index(r'\end{equation}')+len(r'\end{equation}')]
new=r'''Use the function $L=\log N$ and the modular coordinate
$t=j/1728$ of \cref{I:def:theta-height}.

\begin{lemma}[The bounded cusp zero and its differential equation]
\hypertarget{tag-IA09}{}\label{I:cusp-zero-equation}
For the cusp-bounded lift of the zero of $\wp_\tau$, one has
'''+formula+r'''
The branch of $E_6^{3/2}$ tends to one at the cusp. The series
holds on $\Im\tau>1$ and continues on the chosen logarithm
branch away from half-period branch points.
\end{lemma}
\begin{proof}
Use the Eichler--Zagier formula
\cite[unnumbered theorem, p.~399]{EichlerZagier1982},
in the form of
\cite[Section~2, unnumbered Eichler--Zagier theorem and equation~(6),
author preprint p.~4]{DukeImamoglu2008}.
In equation~(6), take $m=n=0$ and the minus sign, so that the
resulting zero $z_0$ tends to $1/2+i\beta_{\rm cusp}$.
The exact affine map is $\mu=1-z_0$, as in \cref{inv:A2.3};
periodicity and evenness give
$\wp(1-z_0,\tau)=\wp(z_0,\tau)$.
Termwise integration uses
$\int_\tau^{i\infty}(\sigma-\tau)e^{2\pi in\sigma}\,d\sigma
=-q^n/(4\pi^2n^2)$ and gives the displayed series.
Termwise differentiation using $q'=2\pi iq$ gives its
second derivative. At $i$ the continuation uses the square-root
coordinate of \cref{ari:C.3.1}.
\end{proof}

'''
patch(old,new,'Number the external differential equation and give its exact branch morphism; archive search history.',
      ('ari:eq:cc-EZ',))
for oldtitle,newtitle in [
 ('a radial derivative identity','The radial derivative'),
 ('the cusp exclusion','A bound on the cusp region'),
 ('the compact exclusion by one Cayley disc','A bound on the compact modular region'),
 ('every critical point and every level set','The critical points and global level curves')]:
 patch('['+oldtitle+']','['+newtitle+']','Use a descriptive mathematical title.')
patch(r'''We give the coefficient arithmetic and all tails, rather than
leaving these inequalities to sampling a circle. In''',
r'''The following recurrences and tails determine the coefficient
bounds. In''',
'State the actual certificate directly.',('ari:C.8.14',))
old=r'''The recurrences, cutoffs and remainders above specify each finite
comparison completely. The attached exact integer/rational
script reproduces them with outward rounding on denominator
$10^{100}$ and independently checks every rational ODE
coefficient; no point of the modular domain is enumerated.'''
archive('C814_implementation_comparison',old,'Independent implementation details.')
patch(old,r'''The recurrences, cutoffs and remainders above specify each
finite comparison by rational arithmetic.''',
'Retain the complete mathematical finite certificate.',('ari:C.8.14',))
patch(r'''For an exact independent recipe, if $P(r)/r=\sum q_nr^n$,''',
      r'''Explicitly, if $P(r)/r=\sum q_nr^n$,''',
      'Present the Bernstein coefficient transformation directly.',('ari:C.8.14',))
patch(r'''are checked by squaring. The complete exact coefficient list is
also retained with the code. Every Bernstein basis function is''',
r'''are verified by squaring. Every Bernstein basis function is''',
'Keep the exact rational endpoint check and remove output inventory.',('ari:C.8.14',))
old=r'''\item The proposed route in the stated conventions that posits one saddle on
$(0,1)$ is therefore false. The corrected statement is the
strict radial foliation above. It supplies, in addition to
the separate duplication proof, a global proof of Theorem~\ref{fam:src:C.2.3} and
resolves the critical-point and global-level-set question
posed for this normalized norm function.
'''
archive('C815_historical_conclusion',old,'Problem-history summary after the full global proof.')
patch(old,'','End after the complete critical-set and level-curve proof.',('ari:C.8.15',))

out=dict(source_path=str(base),source_sha256=hashlib.sha256(original.encode()).hexdigest(),
 generated_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
 requires_batch='S6_SERIES_PUBLISH_I_editorial_batch_d_guards.json',guards=guards)
(B/'S6_SERIES_PUBLISH_I_editorial_batch_e_guards.json').write_text(json.dumps(out,indent=2)+'\n')
(B/'S6_SERIES_PUBLISH_I_editorial_batch_e_removed.json').write_text(json.dumps(removed,indent=2)+'\n')
(B/'S6_SERIES_PUBLISH_I_editorial_batch_e_preview.tex').write_text(s)
print(json.dumps({'guards':len(guards),'removed_blocks':len(removed),
 'preview_sha256':hashlib.sha256(s.encode()).hexdigest()},indent=2))
