from S6_SERIES_PUBLISH_c3_edit import *
import json

apply_edit(r'''On the normalization of
that branch the induced contraction can be
written $t\mapsto\eta t$, $0<|\eta|<1$.
For completeness, if the initial coordinate
has return map $g(t)=\eta t+O(t^2)$, choose
$|\eta|<\rho<\sqrt{|\eta|}$. On a sufficiently
small disc, $|g(t)|\le\rho|t|$, and the
successive differences in $g^j(t)/\eta^j$
are bounded by a constant times
$(\rho^2/|\eta|)^j|t|^2$. Their convergent sum
gives the asserted linearizing coordinate.''',
    r'''In a coordinate $u$ on the normalization of that branch,
the return map is a holomorphic contraction
$g(u)=\eta u+O(u^2)$ with $0<|\eta|<1$.
Koenigs' theorem \cite[\S III.10, Theorem~III, p.~S15;
\S IV.11--12, p.~S16]{Koenigs1884} supplies a holomorphic
function $B$ with $B(0)=0$, $B'(0)\ne0$ and
$B(g(u))=\eta B(u)$. Thus $t=B(u)$, with its holomorphic
inverse at zero, conjugates this return map to $t\mapsto\eta t$.''',
    'II-C3-HOPF-KOENIGS', ['D17','D18'], 'night:P4.24', 'Step 4',
    'Opened the original theorem and its two following properties in text and rendered pages. Replaces the standard convergence re-proof by its primary citation while displaying the exact local biholomorphic conjugacy and inverse.')

anchor=r'\bibitem[Koll\'ar(1997)]'
s=SOURCE.read_text()
import re
matches=[m for m in re.finditer(r'^\\bibitem[^\n]+',s,re.M) if 'Koll' in m.group()]
assert matches
anchor=matches[0].group()
bib=r'''\bibitem[Koenigs(1884)]{Koenigs1884}
Gabriel Koenigs.
\newblock Recherches sur les int\'egrales de certaines \'equations fonctionnelles.
\newblock \emph{Annales scientifiques de l'\'Ecole Normale Sup\'erieure},
3e s\'erie, 1:3--41 (suppl\'ement), 1884.
\newblock \doi{10.24033/asens.247}.
\newblock URL \url{https://www.numdam.org/article/ASENS_1884_3_1__S3_0.pdf}.

'''
apply_edit(anchor,bib+anchor,'II-C3-KOENIGS-BIB',['D18'],'Koenigs1884','Bibliography',
           'Adds the opened original linearization source with exact journal, DOI and persistent publisher scan.')
metadata=[json.loads(line) for line in (ROOT/'code/S6_SERIES_PUBLISH_c3_primary_fetch.out').read_text().splitlines()]
sha={r['source']:r['sha256'] for r in metadata}
rows=[
    dict(source='Koenigs 1884',url='https://www.numdam.org/article/ASENS_1884_3_1__S3_0.pdf',
         version='Annales scientifiques de ENS, series3,1(1884), supplement3–41; Numdam original scan',
         locus='SectionIII.10 TheoremIII and its proof, pS15; SectionIV.11–12, pS16; complete text and both rendered pages read',
         date_utc=now(),sha256=sha['Koenigs1884'],
         own_word_summary='The normalized iterates of an attracting one-variable holomorphic germ converge to a holomorphic function with a simple zero at the fixed point. The following two properties give the local coordinate and its exact multiplicative conjugacy equation.',
         use='night:P4.24: t=B(u), B composed with g equals eta B, with nonzero derivative and a local holomorphic inverse'),
    dict(source='Liu–Rollenske 2012 SLC',url='https://lematematiche.dmi.unict.it/index.php/lematematiche/article/download/922/837/3577',
         version='Le Matematiche67(2)(2012),185–202, publisher PDF',
         locus='Complete printed pp186–187,189,192,196–200: Theorem1.1/Table1, Lemma2.2/Definition2.3, Proposition3.1 statement, Proposition4.1 and its proof',
         date_utc=now(),sha256=sha['LiuRollenske2012SLC'],
         own_word_summary='The theorem lists analytic equations of all surface hypersurface slc germs. The definition uses the normalization with its conductor boundary, and the birational lemma preserves log canonicity under the displayed canonical pullback identity. The nonnormal lists have the stated double and triple equations and parameter ranges.',
         use='night:P4.25: reduced resolved boundary implies slc, then the exact analytic list fixes the local equations while component multiplicities of the full map are retained')
]
print('Primary rows',append_rows(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv',rows,'source'))
add_event('night:P4.24','II-C3-ROOT-HOPF-KOENIGS','used and rechecked in this run',
          'Compared the entire former one-variable convergence paragraph with the exact original theorem and receiving coordinate B. The finite-branch return map is unchanged, and the coefficient comparisons in the following diagonal and resonant cases use the same linearized parameter. This is an exposed proof/source comparison, not an independent proof.',
          'S6_SERIES_PUBLISH_II.tex',source='code/S6_SERIES_PUBLISH_c3_koenigs.py')
print('Exact Koenigs input admitted.')
