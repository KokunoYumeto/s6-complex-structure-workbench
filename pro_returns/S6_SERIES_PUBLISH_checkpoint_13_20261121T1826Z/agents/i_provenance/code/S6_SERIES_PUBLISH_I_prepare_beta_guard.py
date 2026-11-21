"""Prepare the bounded complex-beta citation/application replacement; no root writes."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re

W = Path('/workspace/scratch/653608133b22/work')
O = W / 'agents/i_provenance'
L = O / 'literature'
T = W / 'S6_SERIES_PUBLISH_I.tex'
B = W / 'S6_SERIES_PUBLISH_references.bib'
now = datetime.now(timezone.utc).isoformat()
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def writej(p, x): p.write_text(json.dumps(x, indent=2, ensure_ascii=False) + '\n')
tex, bib = T.read_text(), B.read_text()
assert 'Neretin2024Beta' not in tex and 'Neretin2024Beta' not in bib
start = tex.index(r'\begin{proposition}[The two complex beta integrals]')
end = tex.index(r'\end{proof}', start) + len(r'\end{proof}')
oldblock = tex[start:end]
old = r'''We include a proof of the integral evaluation. For
$0<a,b$ and $a+b<1$, insert
\[
 |w|^{2a-2}=\frac1{\Gamma(1-a)}
       \int_0^\infty t^{-a}e^{-t|w|^2}\,dt
\]
and the corresponding formula for $|1-w|^{2b-2}$.
Tonelli's theorem applies to the positive integrand. The
Gaussian integral over $w$ is
$\pi(t+s)^{-1}\exp(-ts/(t+s))$.
Putting $t=rv$, $s=r(1-v)$ reduces the remaining integrals
to $\Gamma(1-a-b)$ and the beta integral $B(a,b)$, proving
the displayed formula. The same integrable bounds justify
differentiation in a neighbourhood of $s=0$.'''
new = r'''The complex beta identity \cite[\S\S1.1--1.2, equations~(1.6)--(1.7),
pp.~38--39]{Neretin2024Beta} applies with parameter pairs $a\mid a$ and $b\mid b$.
In that notation $\Gamma^{\mathbb C}(a\mid a)=\Gamma(a)/\Gamma(1-a)$ and
\[
 B_{\C}(a,b)=\int_{\C}|w|^{2a-2}|1-w|^{2b-2}\,dA_w
           =\pi B^{\mathbb C}(a\mid a,b\mid b).
\]
The source's absolute-convergence conditions are
$\Re a>0$, $\Re b>0$ and $\Re(a+b)<1$. Under
$a=1/(2m)$ and $b=(s+1)/2$, these give exactly the stated strip.
The strict inequalities give integrable power bounds at $u=0$, at each
root of $1-u^m$, and at infinity. On a sufficiently small closed
neighbourhood of $s=0$, their positive margins also absorb the
logarithmic factor introduced by differentiation. Thus differentiation
under the integral at $s=0$ is justified.'''
assert oldblock.count(old) == 1 and tex.count(old) == 1
closing_old = r'Equation \eqref{ari:eq:ca-mahler} completes the normalization test.'
closing_new = r'Equation \eqref{ari:eq:ca-mahler} gives the stated values of $N$.'
assert oldblock.count(closing_old) == 1 and tex.count(closing_old) == 1
newblock = oldblock.replace(old, new).replace(closing_old, closing_new)
for pattern in [r'\\label\{[^}]+\}', r'\\hypertarget\{[^}]+\}', r'\\StatementRecord\{[^}]+\}']:
    assert re.findall(pattern, oldblock) == re.findall(pattern, newblock)
stem = O / 'S6_SERIES_PUBLISH_I_candidate11_beta'
Path(str(stem) + '_old.tex').write_text(oldblock + '\n')
Path(str(stem) + '_proposed.tex').write_text(newblock + '\n')
inline = r'''\bibitem[Neretin(2024)]{Neretin2024Beta}
Yury A. Neretin.

\newblock On the Dotsenko--Fateev complex twin of the Selberg integral and its extensions.

\newblock \emph{The Ramanujan Journal}, 64\penalty0 (1):\penalty0 37--55, 2024.

\newblock \doi{10.1007/s11139-023-00804-3}.

\newblock URL \url{https://link.springer.com/content/pdf/10.1007/s11139-023-00804-3.pdf}.

'''
anchor = r'\bibitem[Nguyen(2023)]{nguyen2023}'
assert tex.count(anchor) == 1
changes = [
    dict(id='IP-C11-BETA01', statement='ari:C.8.7', old=old, new=new,
         reason='Replace the reproof of a classical complex beta evaluation with an exact published citation and explicit pair/measure/convergence map. The m-sheet substitution, displayed gamma quotient, differentiated gamma calculation and normalization conclusion remain intact.'),
    dict(id='IP-C11-BETA02', statement='bibliography:Neretin2024Beta', old=anchor, new=inline+anchor,
         reason='Add the actually opened published source in alphabetical order, with exact volume, pages, DOI and primary PDF URL.'),
    dict(id='IP-C11-BETA03', statement='ari:C.8.7', old=closing_old, new=closing_new,
         reason='State the mathematical conclusion of the unchanged normalization identity directly.')]
writej(Path(str(stem)+'_guards.json'), dict(created_utc=now, source=str(T), source_sha256=sha(T), source_writes=False, changes=changes))
entry = '''@article{Neretin2024Beta,
  author = {Neretin, Yury A.},
  title = {On the {Dotsenko--Fateev} complex twin of the {Selberg} integral and its extensions},
  journal = {The Ramanujan Journal},
  volume = {64},
  number = {1},
  pages = {37--55},
  year = {2024},
  doi = {10.1007/s11139-023-00804-3},
  url = {https://link.springer.com/content/pdf/10.1007/s11139-023-00804-3.pdf},
  verification = {verified at listed scope},
  current_run_locator = {Actually viewed published pp.37--39 on 21 November 2026. Section1.1 p38 defines the parameter-pair notation and area measure; Section1.2 p39 equations1.6--1.7 give the complex gamma and beta identities with their complete absolute-convergence domain. Receiving parameters a|a,b|b and measure factor pi are explicit. No full-paper reading or new mathematical check is claimed for this source opening.}
}

'''
banchor = '@article{nguyen2023,'
assert bib.count(banchor) == 1
writej(Path(str(stem)+'_shared_bib_guards.json'), dict(created_utc=now, source=str(B), source_sha256=sha(B), source_writes=False, changes=[dict(id='IP-C11-BETA-SHARED01', old=banchor, new=entry+banchor, reason='Add the exact primary source and bounded actual-page verification scope; no other entry is changed.')]))
retrieval = json.loads((L/'S6_SERIES_PUBLISH_I_Neretin2024_beta_retrieval.json').read_text())
pdf = L/'S6_SERIES_PUBLISH_I_Neretin2024_complex_beta.pdf'
assert sha(pdf) == retrieval['pdf_sha256']
receipt = dict(recorded_utc=now, source=str(T), source_sha256=sha(T), author='Yury A. Neretin',
    title='On the Dotsenko–Fateev complex twin of the Selberg integral and its extensions',
    publication='The Ramanujan Journal 64(1) (2024), 37–55', doi='10.1007/s11139-023-00804-3',
    publication_note='Issue year2024; first published online29December2023. Both are printed on the actually viewed title page.',
    retrieval=retrieval, primary_pdf=str(pdf), pdf_sha256=sha(pdf),
    actually_viewed_pages=[dict(pdf_page=i, printed_page=36+i, image=str(L/f'S6_SERIES_PUBLISH_I_Neretin2024_complex_beta_p{i:03}.png'), image_sha256=sha(L/f'S6_SERIES_PUBLISH_I_Neretin2024_complex_beta_p{i:03}.png')) for i in (1,2,3)],
    exact_locator='Section1.1,p38; Section1.2,equations1.6--1.7,p39, including the entire convergence statement.',
    parameter_map=dict(pair_parameters='a|a and b|b', area_measure='dA=dRe(w)dIm(w); source beta carries factor1/pi, so receiving B_C=pi B^C.', complex_gamma='Gamma^C(a|a)=Gamma(a)/Gamma(1-a); all phase factors are1.',
      source_domain='Re(a)>0, Re(b)>0, Re(a+b)<1', receiving_parameters='a=1/(2m), b=(s+1)/2, m=2 or3', receiving_domain='-1<Re(s)<1-1/m',
      sheet_jacobian='For w!=0, each sheet has |du/dw|^2=m^-2 |w|^(2/m-2); multiplying by |u|^-1 and summing all m sheets gives m^-1 |w|^(1/m-2).',
      derivative_scope='On a closed neighbourhood of0 contained in the strip, positive endpoint power margins dominate the derivative logarithm. The original digamma calculation and normalization remain unchanged.'),
    scope='Only title/metadata, notation, gamma/beta statements and full convergence domain were actually viewed; no reading of later sections or independent proof derivation is claimed.',
    mathematical_events_added_for_source_opening=0)
writej(L/'S6_SERIES_PUBLISH_I_Neretin2024_beta_locator_receipt.json',receipt)
print(json.dumps(dict(source_sha256=sha(T), guard=str(Path(str(stem)+'_guards.json')), shared_bib_guard=str(Path(str(stem)+'_shared_bib_guards.json')), old=str(Path(str(stem)+'_old.tex')), proposed=str(Path(str(stem)+'_proposed.tex')), receipt=str(L/'S6_SERIES_PUBLISH_I_Neretin2024_beta_locator_receipt.json')),indent=2))
