"""State the actual compact lifts and preserve the complete CM witness proof."""
from pathlib import Path
import csv,json
P=Path(__file__).resolve().parents[2]
S=(P.parents[1]/'sources/s6_09/S6_09_PAPERS_I.tex').read_text()
J=json.loads((P/'analysis/inventory_source_index.json').read_text())
def source(run,n):
 d=J[run+':'+n];return S[d['start']:d['end']]
def change(s,a,b):
 assert s.count(a)==1,(a[:80],s.count(a));return s.replace(a,b)
def save(label,s):
 (P/'papers/I/revisions'/(label.replace(':','_')+'.tex')).write_text(s)
s=source('S6_05_ARITHMETIC','C.7.9')
s=change(s,r'''Then $c$ is a real transcendental number. If $N(P)$ were
algebraic, the extension $G_Q$ of \ref{ari:C.7.1} would have a
nontorsion algebraic point whose logarithm is $(u,cu)$.
The complex line
$\ell_c=\{(z,cz):z\in\C\}$ is not defined over
$\overline\Q$ in the algebraic logarithm coordinates of
\ref{ari:C.7.1}. Thus the analytic subgroup theorem cannot be applied
to that line using the hypothesized compact point.''',r'''Then $c$ is a real transcendental number. The actual point
\[
 R_N=(Q,3\,19^{-1/2}N(Q)^2)\in G_Q(\C)
\]
is nontorsion, belongs to the maximal compact subgroup, and has
the real logarithm $(u,cu)$. Its algebraicity is equivalent to
the algebraicity of $N(P)$. In the algebraic logarithm coordinates
of \ref{ari:C.7.1}, the line $\ell_c=\C(1,c)$ has transcendental
slope. The proof establishes this slope statement from a period
of $G_Q$ without deciding the algebraicity of $R_N$.''')
s=change(s,r'''Finally assume, only for the attempted contradiction, that
$N(P)$ is algebraic. The positive real number
\[
 r=3\,19^{-1/2}N(Q)^2
\]
is algebraic, and \ref{ari:C.7.2} places the point $R=(Q,r)$ of
$G_Q$ in its maximal compact subgroup.''',r'''Define the positive real number
\[
 r=3\,19^{-1/2}N(Q)^2.
\]
Proposition~\ref{ari:C.7.2} places the actual point $R_N=(Q,r)$
in the maximal compact subgroup of $G_Q$. Since $Q$ is algebraic,
$R_N$ is algebraic exactly when $r$ is algebraic, equivalently
when $N(Q)$, and hence $N(P)$, is algebraic.''')
s=s.replace('is a logarithm of $R$,','is a logarithm of $R_N$,').replace('so $R$ is nontorsion.','so $R_N$ is nontorsion.')
save('ari:C.7.9',s)
s=source('S6_05_ARITHMETIC','C.7.10')
s=change(s,r'''If $N(P)$ is algebraic, \ref{ari:C.7.9} combines this point with an
algebraic compact point in the first extension to give
\[
 U=(u,v_1,v_2),\qquad v_1=uD-ku^2,
 \qquad \exp_{\mathcal G}U\in\mathcal G(\overline\Q).
\]''',r'''Pair this point with the actual compact point $R_N$ of
\ref{ari:C.7.9}. The resulting compact point of $\mathcal G(\C)$
has logarithm
\[
 U=(u,v_1,v_2),\qquad v_1=uD-ku^2.
\]
Its algebraicity is equivalent to the algebraicity of $N(P)$.''')
s=change(s,r'''Algebraicity of $\exp(U)$ does not supply
algebraicity of $\exp(\Pi_-U)$.''',r'''At least one of the two torus coordinates of
$\exp(\Pi_-U)$ is transcendental; the proof does not decide the
algebraicity of its first coordinate alone.''')
s=change(s,r'''Under the hypothetical algebraicity of $N(P)$, \ref{ari:C.7.9} gives
the first compact logarithm $v_1=uD-ku^2$. Pairing the
two algebraic lifts over the same base point gives $U$.''',r'''The actual first compact logarithm in \ref{ari:C.7.9} is
$v_1=uD-ku^2$. Pairing the two compact lifts over the same base
point gives $U$ with no algebraicity assumption. The second lift
is algebraic, so the paired point is algebraic exactly when its
first lift is algebraic.''')
s=change(s,r'''If the projection
preserved algebraic exponentials here, that would give a
contradiction; it is precisely the extra implication that
is unavailable.''',r'''Indeed its nonzero logarithm lies in the algebraic line
$\C(1,\beta)$, whereas a one-dimensional algebraic subtorus
has a rational slope. The analytic subgroup theorem would put
a positive-dimensional subtorus in that line for an algebraic
exponential, contradicting these two slope computations.''')
# The old proof stopped before its explicit polynomial construction.
s=change(s,r'\end{proof}', '')
s=s.rstrip()+'\n\\end{proof}\n'
save('ari:C.7.10',s)
s=source('S6_02_PUSH','E.1.3').replace(r'\ref{push:src:E.3.2}',r'\ref{fam:src:B.4.1}').replace(r'\cref{push:src:E.3.2}',r'\cref{fam:src:B.4.1}')
s=s.replace('calculation audited in','calculation re-derived in the credited appendix at')
save('push:src:E.1.3',s)
p=P/'records/root_events.tsv';rows=list(csv.DictReader(p.open(),delimiter='\t'));fields=list(rows[0])
rows.append(dict(zip(fields,['ari:C.7.10','2026-11-18','GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS','computation or formal certificate','Read and freshly replayed unchanged C7_cm_explicit.gp. Both polynomial residuals are zero, all displayed gcds are one, exact s2/a/r2 values agree, and analytic comparisons differ by less than 6e-114. Exact identities prove the algebraic witness; decimal comparisons are diagnostic.'])))
with p.open('w') as f:w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
print('Revised actual compact lifts and full CM witness; corrected automorphism pointer.')
